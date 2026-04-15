/**
 * ACE Popup Overlay — ace-popup.js  v1.0
 *
 * Per-question feedback popup. ACE appears center-screen after each
 * answer with a comment, optional correct answer reveal, and explanation.
 *
 * Usage:
 *   AcePopup.show({
 *     correct:       boolean,      // true = correct answer
 *     explanation:   string|null,  // explanation text (optional)
 *     correctAnswer: string|null,  // correct answer text (shown if wrong)
 *     aceComment:    string|null,  // override comment (auto-selected if null)
 *     sprite:        string|null,  // 'happy'|'proud'|'thinking'|'concerned' (auto if null)
 *     onNext:        function,     // callback when "Continue" is clicked
 *   });
 *
 *   AcePopup.hide();   // programmatic dismiss
 *
 * Keyboard: ESC dismisses (calls onNext)
 * Backdrop click dismisses (calls onNext)
 *
 * Requires: ace-popup.css loaded, ace-theme.css tokens available
 */

const AcePopup = (() => {

  /* ─── Comment pools ───────────────────────────────────────── */
  const COMMENTS_CORRECT = [
    "Nailed it.",
    "Exactly right.",
    "Correct — keep that in your memory bank.",
    "Spot on. You're building the right foundations.",
    "Perfect. Keep this momentum going.",
    "Solid recall. The FAA would be pleased.",
    "Right answer. Safety starts with knowing your regs cold.",
    "Excellent. That one catches a lot of techs off-guard.",
    "Affirmative. That's exactly what you need for the exam.",
    "That's the one. Building good instincts."
  ];

  const COMMENTS_WRONG = [
    "Not quite — but now you know.",
    "Common miss. Check the explanation.",
    "Easy to mix up. Read the reasoning carefully.",
    "That one trips people up.",
    "Worth adding to your weak list.",
    "These details matter in the field.",
    "No worries — mistakes in drill mean mastery later.",
    "Close, but not quite. Review the explanation.",
    "Flag this one for extra review.",
    "Good guess, wrong answer. Learn the logic."
  ];

  /* ─── Sprite → filename mapping ───────────────────────────── */
  const SPRITE_FILES = {
    happy:     'ace-192-happy.png',
    proud:     'ace-192-proud.png',
    thinking:  'ace-192-thinking.png',
    concerned: 'ace-192-concerned.png',
    neutral:   'ace-192-happy.png',    // fallback
  };

  /* ─── State ────────────────────────────────────────────────── */
  let backdrop = null;
  let onNextCallback = null;
  let isOpen = false;

  /* ─── Build DOM once ───────────────────────────────────────── */
  function build() {
    if (document.getElementById('acePopupBackdrop')) return;

    const html = `
      <div class="ace-popup-backdrop" id="acePopupBackdrop" role="dialog" aria-modal="true" aria-labelledby="acePopupTitle">
        <div class="ace-popup" id="acePopupPanel">

          <div class="ace-popup-strip" id="acePopupStrip"></div>

          <div class="ace-popup-character">
            <div class="ace-popup-sprite-wrap">
              <img class="ace-popup-sprite" id="acePopupSprite" src="" alt="ACE">
            </div>
            <div class="ace-popup-speech">
              <div class="ace-popup-name" id="acePopupTitle">ACE — Aviation Mentor</div>
              <div class="ace-popup-comment" id="acePopupComment"></div>
              <div class="ace-popup-result" id="acePopupResult">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" id="acePopupResultIcon"></svg>
                <span id="acePopupResultText"></span>
              </div>
            </div>
          </div>

          <div class="ace-popup-correct-answer" id="acePopupCorrectAnswer">
            <div class="ace-popup-correct-label">Correct Answer</div>
            <div class="ace-popup-correct-text" id="acePopupCorrectText"></div>
          </div>

          <div class="ace-popup-explanation" id="acePopupExplanation">
            <div class="ace-popup-explanation-label">Why?</div>
            <div class="ace-popup-explanation-text" id="acePopupExplanationText"></div>
          </div>

          <div class="ace-popup-footer">
            <button class="ace-popup-next" id="acePopupNext">
              <span id="acePopupNextLabel">Continue</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <path d="M5 12h14M12 5l7 7-7 7"/>
              </svg>
            </button>
          </div>

          <div class="ace-popup-hint">
            Press <kbd>Space</kbd> or <kbd>Enter</kbd> to continue
          </div>

        </div>
      </div>
    `;

    document.body.insertAdjacentHTML('beforeend', html);
    backdrop = document.getElementById('acePopupBackdrop');

    /* Backdrop click dismisses */
    backdrop.addEventListener('click', (e) => {
      if (e.target === backdrop) dismiss();
    });

    /* Continue button */
    document.getElementById('acePopupNext').addEventListener('click', dismiss);
  }

  /* ─── Resolve sprite path ──────────────────────────────────── */
  function getSpriteSrc(spriteName) {
    const file = SPRITE_FILES[spriteName] || SPRITE_FILES.happy;
    // Walk up from the page to find shared/ace-sprites/ dynamically
    // Check if there's a data-root attribute on <html>, else use common relative paths
    const root = document.documentElement.dataset.aceRoot || '';
    if (root) return root + 'shared/ace-sprites/' + file;

    // Auto-detect based on common path depths
    const paths = [
      'shared/ace-sprites/' + file,           // from root
      '../shared/ace-sprites/' + file,        // 1 deep
      '../../shared/ace-sprites/' + file,     // 2 deep
      '../../../shared/ace-sprites/' + file,  // 3 deep
      '../../../../shared/ace-sprites/' + file, // 4 deep
    ];
    // Return first path that "looks right" based on current URL depth
    const depth = (window.location.pathname.match(/\//g) || []).length - 1;
    return paths[Math.min(depth, paths.length - 1)];
  }

  /* ─── Show ─────────────────────────────────────────────────── */
  function show(options = {}) {
    build();

    const {
      correct       = false,
      explanation   = null,
      correctAnswer = null,
      aceComment    = null,
      sprite        = null,
      onNext        = null,
    } = options;

    onNextCallback = onNext;
    isOpen = true;

    /* Pick sprite */
    let spriteName = sprite;
    if (!spriteName) {
      spriteName = correct ? (Math.random() < 0.5 ? 'happy' : 'proud') : (Math.random() < 0.5 ? 'thinking' : 'concerned');
    }

    /* Pick comment */
    const pool = correct ? COMMENTS_CORRECT : COMMENTS_WRONG;
    const comment = aceComment || pool[Math.floor(Math.random() * pool.length)];

    /* Set result styling */
    const strip    = document.getElementById('acePopupStrip');
    const result   = document.getElementById('acePopupResult');
    const resultIcon = document.getElementById('acePopupResultIcon');
    const resultText = document.getElementById('acePopupResultText');
    const nextBtn  = document.getElementById('acePopupNext');
    const nextLabel = document.getElementById('acePopupNextLabel');

    strip.className    = 'ace-popup-strip ' + (correct ? 'correct' : 'wrong');
    result.className   = 'ace-popup-result ' + (correct ? 'correct' : 'wrong');
    nextBtn.className  = 'ace-popup-next '   + (correct ? 'correct' : 'wrong');

    if (correct) {
      resultIcon.innerHTML = '<path d="M20 6L9 17l-5-5"/>';
      resultText.textContent = 'Correct';
      nextLabel.textContent = 'Continue';
    } else {
      resultIcon.innerHTML = '<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>';
      resultText.textContent = 'Incorrect';
      nextLabel.textContent = 'Got it — next';
    }

    /* Set content */
    document.getElementById('acePopupComment').textContent = comment;
    document.getElementById('acePopupSprite').src = getSpriteSrc(spriteName);

    /* Correct answer reveal */
    const correctAnswerEl = document.getElementById('acePopupCorrectAnswer');
    if (!correct && correctAnswer) {
      document.getElementById('acePopupCorrectText').textContent = correctAnswer;
      correctAnswerEl.classList.add('visible');
    } else {
      correctAnswerEl.classList.remove('visible');
    }

    /* Explanation */
    const explanationEl = document.getElementById('acePopupExplanation');
    if (explanation) {
      document.getElementById('acePopupExplanationText').textContent = explanation;
      explanationEl.classList.add('visible');
    } else {
      explanationEl.classList.remove('visible');
    }

    /* Open backdrop */
    backdrop.classList.remove('closing');
    backdrop.classList.add('open');

    /* Focus the continue button for keyboard access */
    setTimeout(() => {
      document.getElementById('acePopupNext').focus();
    }, 50);
  }

  /* ─── Dismiss ──────────────────────────────────────────────── */
  function dismiss() {
    if (!isOpen) return;
    isOpen = false;

    backdrop.classList.add('closing');

    setTimeout(() => {
      backdrop.classList.remove('open', 'closing');
      if (typeof onNextCallback === 'function') {
        onNextCallback();
        onNextCallback = null;
      }
    }, 180);
  }

  /* ─── Keyboard handler ─────────────────────────────────────── */
  document.addEventListener('keydown', (e) => {
    if (!isOpen) return;
    if (e.key === 'Escape' || e.key === ' ' || e.key === 'Enter') {
      e.preventDefault();
      dismiss();
    }
  });

  /* ─── Public API ───────────────────────────────────────────── */
  return { show, hide: dismiss };

})();

// Make available globally
window.AcePopup = AcePopup;
