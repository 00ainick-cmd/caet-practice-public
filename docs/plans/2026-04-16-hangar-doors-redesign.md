# Hangar-Doors Animation Redesign Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Upgrade the hangar-doors transition animation in `shared/drill.html` to a cyber-hangar aesthetic with distinct door color, CAET logo split at the seam, and four layered sci-fi effects.

**Architecture:** Pure CSS enhancement — no new files, no new assets. All changes localized to `shared/drill.html`: ~150 lines added to the existing `<style>` block, a handful of new `<div>` elements inside the existing `.hangar-doors-overlay`, and minor class-toggle additions to the existing `doorsTransition()` function.

**Tech Stack:** Vanilla HTML/CSS/JS, deployed via GitHub Pages. Uses `transform` + `opacity` keyframes for GPU-accelerated animation. `clip-path` for logo halves. `@media (prefers-reduced-motion)` for accessibility.

---

## Conventions for this plan

Each task follows: **make change → verify via grep/read → commit**. Visual verification is done at the end (Task 10) since CSS animation effects need the full stack assembled to evaluate. Commits are per-task so the animation state is never broken mid-way.

**File under test:** `shared/drill.html`

**Verify each commit with:** `python3 -c "import json, glob; [json.load(open(p, encoding='utf-8')) for p in glob.glob('training/caet/*/data/*.json')] + [json.load(open('master-bank.json', encoding='utf-8'))]; print('JSON OK')"` — confirms we didn't accidentally break an unrelated JSON file.

---

## Task 1: Door face — distinct color + subtle hex texture

**Why:** The current doors are `#0d1117` which blends into the page background. Students can't clearly see the doors close. Fix: lighter slate-navy face + subtle hexagonal pattern so the doors read as a distinct visual layer.

**Files:**
- Modify: `shared/drill.html` lines 102-110 (the `.door-left, .door-right` block)

**Step 1: Update door face CSS**

Replace:

```css
    .door-left,
    .door-right {
      position: absolute;
      top: 0;
      bottom: 0;
      width: 50%;
      background: #0d1117;
      transition: transform 1.1s cubic-bezier(0.4, 0, 0.2, 1);
    }
```

with:

```css
    .door-left,
    .door-right {
      position: absolute;
      top: 0;
      bottom: 0;
      width: 50%;
      background:
        /* subtle hexagonal pattern overlay */
        radial-gradient(circle at 25% 25%, rgba(34, 211, 238, 0.04) 2px, transparent 3px) 0 0 / 40px 40px,
        radial-gradient(circle at 75% 75%, rgba(34, 211, 238, 0.03) 2px, transparent 3px) 0 0 / 40px 40px,
        /* base slate-navy with vertical depth gradient */
        linear-gradient(180deg, #1a2332 0%, #14202e 50%, #101a26 100%);
      overflow: hidden;
      transition: transform 1.1s cubic-bezier(0.4, 0, 0.2, 1);
    }
```

**Step 2: Verify change applied**

Run: `grep -n "slate-navy\|linear-gradient(180deg, #1a2332" shared/drill.html`
Expected: at least one match (the comment + gradient are now in the file).

**Step 3: Commit**

```bash
git add shared/drill.html
git commit -m "drill: lighter slate-navy door face with subtle hex pattern"
```

---

## Task 2: Animated scan-line overlay on door faces

**Why:** Adds depth and the "active display" feel. Horizontal CRT-style lines sweep down the door face slowly.

**Files:**
- Modify: `shared/drill.html` — add new CSS rules after the `.door-left, .door-right` block (around line 110 after Task 1's changes)

**Step 1: Add scan-line pseudo-element + keyframe**

Insert after the closing `}` of the `.door-left, .door-right` rule:

```css
    /* Scan-line overlay on each door face (inside ::before of each door) */
    .door-left::before,
    .door-right::after {
      content: '';
      position: absolute;
      inset: 0;
      background: repeating-linear-gradient(
        0deg,
        transparent 0,
        transparent 3px,
        rgba(34, 211, 238, 0.045) 3px,
        rgba(34, 211, 238, 0.045) 4px
      );
      pointer-events: none;
      opacity: 0;
      transition: opacity 0.3s ease;
    }

    .hangar-doors-overlay.active .door-left::before,
    .hangar-doors-overlay.active .door-right::after {
      opacity: 1;
      animation: scanlineSlide 4s linear infinite;
    }

    @keyframes scanlineSlide {
      0%   { background-position: 0 0; }
      100% { background-position: 0 40px; }
    }
```

**Step 2: Verify change applied**

Run: `grep -n "@keyframes scanlineSlide" shared/drill.html`
Expected: one match.

**Step 3: Commit**

```bash
git add shared/drill.html
git commit -m "drill: add animated CRT scan-lines to door faces"
```

---

## Task 3: Multi-stop neon seam + intensifying glow

**Why:** Replace the flat blue seam with a cyan→blue→purple gradient, and make the glow pulse stronger as doors close.

**Files:**
- Modify: `shared/drill.html` lines 122-158 (the seam `::after` / `::before` rules)

**Step 1: Replace seam rules**

Replace the existing:

```css
    .door-left::after {
      content: '';
      position: absolute;
      top: 0;
      right: -3px;
      bottom: 0;
      width: 3px;
      background: var(--accent);
      box-shadow: 0 0 24px 4px var(--accent);
    }

    /* Closed state */
    .hangar-doors-overlay.doors-closed .door-left {
      transform: translateX(0);
    }

    .hangar-doors-overlay.doors-closed .door-right {
      transform: translateX(0);
    }

    /* Seam highlight when closed */
    .door-right::before {
      content: '';
      position: absolute;
      top: 0;
      left: -3px;
      bottom: 0;
      width: 3px;
      background: var(--accent);
      box-shadow: 0 0 24px 4px var(--accent);
    }

    /* Seam highlight when closed */
    .hangar-doors-overlay.doors-closed .door-left::after,
    .hangar-doors-overlay.doors-closed .door-right::before {
      box-shadow: 0 0 40px 8px var(--accent);
    }
```

with:

```css
    /* The rising-glow seam on the inside edge of each door */
    .door-left > .seam-glow,
    .door-right > .seam-glow {
      content: '';
      position: absolute;
      top: 0;
      bottom: 0;
      width: 3px;
      background: linear-gradient(180deg, #22d3ee 0%, #3b82f6 50%, #a78bfa 100%);
      box-shadow:
        0 0 24px 4px rgba(59, 130, 246, 0.85),
        0 0 48px 12px rgba(167, 139, 250, 0.35);
      transition: box-shadow 0.4s ease;
      pointer-events: none;
    }
    .door-left > .seam-glow { right: -3px; }
    .door-right > .seam-glow { left: -3px; }

    /* Closed state — doors slide to center */
    .hangar-doors-overlay.doors-closed .door-left,
    .hangar-doors-overlay.doors-closed .door-right {
      transform: translateX(0);
    }

    /* Seam highlight intensifies when closed */
    .hangar-doors-overlay.doors-closed .door-left > .seam-glow,
    .hangar-doors-overlay.doors-closed .door-right > .seam-glow {
      box-shadow:
        0 0 60px 8px rgba(59, 130, 246, 1),
        0 0 120px 24px rgba(167, 139, 250, 0.6);
    }
```

**Step 2: Add matching HTML elements for the seam-glow divs**

Find the HTML at around line 2316:

```html
  <!-- Hangar Doors Overlay -->
  <div class="hangar-doors-overlay" id="hangarDoorsOverlay">
    <div class="door-left"></div>
    <div class="door-right"></div>
  </div>
```

Replace with:

```html
  <!-- Hangar Doors Overlay -->
  <div class="hangar-doors-overlay" id="hangarDoorsOverlay" aria-hidden="true">
    <div class="door-left">
      <span class="seam-glow"></span>
    </div>
    <div class="door-right">
      <span class="seam-glow"></span>
    </div>
  </div>
```

**Step 3: Verify changes applied**

Run: `grep -n "seam-glow" shared/drill.html`
Expected: 5+ matches (2 CSS selectors for left/right base, 2 for closed state, 2 HTML uses).

Run: `grep -n "aria-hidden=.true." shared/drill.html | head -3`
Expected: at least one new match for the `hangarDoorsOverlay` element.

**Step 4: Commit**

```bash
git add shared/drill.html
git commit -m "drill: upgrade seam to cyan-blue-purple gradient with layered glow"
```

---

## Task 4: CAET logo split at the seam

**Why:** Gives the transition a branding moment. The left half of the logo sits on the inside edge of the left door; the right half on the inside edge of the right door. They meet at the seam to form the full logo centered on the viewport.

**Files:**
- Modify: `shared/drill.html` — add CSS rules (continuing after Task 3's seam-glow CSS) and add HTML elements inside the existing doors

**Step 1: Add logo-half CSS**

Insert after the Task 3 seam-glow rules:

```css
    /* CAET logo halves — anchored to inside edges of doors, clipped to each side */
    .door-logo {
      position: absolute;
      top: 50%;
      width: 280px;
      height: 240px;
      background: url('./logo.png') center/contain no-repeat;
      pointer-events: none;
      opacity: 0;
      transition: opacity 0.35s ease 0.35s, transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
    }

    .door-logo-left {
      right: 0;
      transform: translate(50%, -50%) scale(0.94);
      clip-path: inset(0 50% 0 0);
    }

    .door-logo-right {
      left: 0;
      transform: translate(-50%, -50%) scale(0.94);
      clip-path: inset(0 0 0 50%);
    }

    /* When doors are closed, logo halves are visible + at full scale */
    .hangar-doors-overlay.doors-closed .door-logo-left {
      opacity: 1;
      transform: translate(50%, -50%) scale(1);
    }
    .hangar-doors-overlay.doors-closed .door-logo-right {
      opacity: 1;
      transform: translate(-50%, -50%) scale(1);
    }

    /* Scale-pulse at the moment of slam (via .slam-pulse class toggled in JS) */
    .hangar-doors-overlay.slam-pulse .door-logo-left {
      animation: logoSlamL 250ms ease-out;
    }
    .hangar-doors-overlay.slam-pulse .door-logo-right {
      animation: logoSlamR 250ms ease-out;
    }
    @keyframes logoSlamL {
      0%   { transform: translate(50%, -50%) scale(1); }
      40%  { transform: translate(50%, -50%) scale(1.10); }
      100% { transform: translate(50%, -50%) scale(1); }
    }
    @keyframes logoSlamR {
      0%   { transform: translate(-50%, -50%) scale(1); }
      40%  { transform: translate(-50%, -50%) scale(1.10); }
      100% { transform: translate(-50%, -50%) scale(1); }
    }
```

**Step 2: Add logo-half HTML inside the doors**

Update the hangar overlay HTML from Task 3 to:

```html
  <!-- Hangar Doors Overlay -->
  <div class="hangar-doors-overlay" id="hangarDoorsOverlay" aria-hidden="true">
    <div class="door-left">
      <span class="seam-glow"></span>
      <div class="door-logo door-logo-left"></div>
    </div>
    <div class="door-right">
      <span class="seam-glow"></span>
      <div class="door-logo door-logo-right"></div>
    </div>
  </div>
```

**Step 3: Verify**

Run: `grep -n "door-logo" shared/drill.html`
Expected: at least 6 matches (CSS for base + left + right + closed-left + closed-right + HTML references).

**Step 4: Commit**

```bash
git add shared/drill.html
git commit -m "drill: add CAET logo split at seam with slam scale-pulse"
```

---

## Task 5: Corner HUD brackets

**Why:** Four L-shaped targeting-reticle brackets slide in from the viewport corners when doors close. Classic sci-fi heads-up-display feel.

**Files:**
- Modify: `shared/drill.html` — more CSS + more HTML

**Step 1: Add HUD bracket CSS**

Insert after Task 4 logo CSS:

```css
    /* HUD corner brackets — L-shaped targeting reticle, one per viewport corner */
    .hangar-corners {
      position: absolute;
      inset: 0;
      pointer-events: none;
    }
    .hangar-corner {
      position: absolute;
      width: 48px;
      height: 48px;
      opacity: 0;
      transition: opacity 0.3s ease, transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    .hangar-corner::before,
    .hangar-corner::after {
      content: '';
      position: absolute;
      background: #22d3ee;
      box-shadow: 0 0 8px #22d3ee;
    }
    /* Horizontal bar of the L */
    .hangar-corner::before { height: 2px; width: 100%; }
    /* Vertical bar of the L */
    .hangar-corner::after  { width: 2px; height: 100%; }

    .hangar-corner.tl { top: 24px;    left: 24px;    transform: translate(-40px, -40px); }
    .hangar-corner.tl::before { top: 0; left: 0; }
    .hangar-corner.tl::after  { top: 0; left: 0; }

    .hangar-corner.tr { top: 24px;    right: 24px;   transform: translate(40px, -40px); }
    .hangar-corner.tr::before { top: 0; right: 0; }
    .hangar-corner.tr::after  { top: 0; right: 0; }

    .hangar-corner.bl { bottom: 24px; left: 24px;    transform: translate(-40px, 40px); }
    .hangar-corner.bl::before { bottom: 0; left: 0; }
    .hangar-corner.bl::after  { bottom: 0; left: 0; }

    .hangar-corner.br { bottom: 24px; right: 24px;   transform: translate(40px, 40px); }
    .hangar-corner.br::before { bottom: 0; right: 0; }
    .hangar-corner.br::after  { bottom: 0; right: 0; }

    /* Slide in with 80-120ms stagger when doors close */
    .hangar-doors-overlay.doors-closed .hangar-corner { opacity: 1; transform: translate(0, 0); }
    .hangar-doors-overlay.doors-closed .hangar-corner.tl { transition-delay: 0.08s; }
    .hangar-doors-overlay.doors-closed .hangar-corner.tr { transition-delay: 0.16s; }
    .hangar-doors-overlay.doors-closed .hangar-corner.bl { transition-delay: 0.24s; }
    .hangar-doors-overlay.doors-closed .hangar-corner.br { transition-delay: 0.32s; }
```

**Step 2: Add HUD bracket HTML**

Update the overlay HTML from Task 4 to add the brackets container INSIDE `.hangar-doors-overlay` (as a sibling of the doors):

```html
  <!-- Hangar Doors Overlay -->
  <div class="hangar-doors-overlay" id="hangarDoorsOverlay" aria-hidden="true">
    <div class="door-left">
      <span class="seam-glow"></span>
      <div class="door-logo door-logo-left"></div>
    </div>
    <div class="door-right">
      <span class="seam-glow"></span>
      <div class="door-logo door-logo-right"></div>
    </div>
    <div class="hangar-corners">
      <div class="hangar-corner tl"></div>
      <div class="hangar-corner tr"></div>
      <div class="hangar-corner bl"></div>
      <div class="hangar-corner br"></div>
    </div>
  </div>
```

**Step 3: Verify**

Run: `grep -c "hangar-corner" shared/drill.html`
Expected: ≥12 matches (multiple CSS selectors + 4 HTML elements + 1 container class).

**Step 4: Commit**

```bash
git add shared/drill.html
git commit -m "drill: add HUD corner brackets with staggered slide-in"
```

---

## Task 6: Glitch burst at slam

**Why:** 150ms full-screen chromatic-aberration + hue-rotate flash at the moment doors meet. Cinematic system-switch feel.

**Files:**
- Modify: `shared/drill.html` — CSS + HTML for the glitch layer

**Step 1: Add glitch-burst CSS**

Insert after Task 5 HUD bracket CSS:

```css
    /* Glitch-burst overlay — 150ms flash activated at slam moment */
    .hangar-glitch {
      position: absolute;
      inset: 0;
      pointer-events: none;
      opacity: 0;
      mix-blend-mode: screen;
      background:
        linear-gradient(90deg, rgba(239, 68, 68, 0.0) 0%, rgba(239, 68, 68, 0.18) 50%, rgba(239, 68, 68, 0.0) 100%),
        linear-gradient(-90deg, rgba(34, 211, 238, 0.0) 0%, rgba(34, 211, 238, 0.18) 50%, rgba(34, 211, 238, 0.0) 100%);
    }
    .hangar-doors-overlay.glitch-active .hangar-glitch {
      animation: glitchBurst 150ms ease-out;
    }
    @keyframes glitchBurst {
      0%   { opacity: 0; transform: translateX(0); filter: hue-rotate(0deg); }
      30%  { opacity: 1; transform: translateX(-4px); filter: hue-rotate(80deg); }
      60%  { opacity: 0.7; transform: translateX(4px); filter: hue-rotate(-60deg); }
      100% { opacity: 0; transform: translateX(0); filter: hue-rotate(0deg); }
    }
```

**Step 2: Add glitch div to HTML**

Update the overlay HTML from Task 5 to include the glitch layer as the last child:

```html
  <div class="hangar-doors-overlay" id="hangarDoorsOverlay" aria-hidden="true">
    <div class="door-left">
      <span class="seam-glow"></span>
      <div class="door-logo door-logo-left"></div>
    </div>
    <div class="door-right">
      <span class="seam-glow"></span>
      <div class="door-logo door-logo-right"></div>
    </div>
    <div class="hangar-corners">
      <div class="hangar-corner tl"></div>
      <div class="hangar-corner tr"></div>
      <div class="hangar-corner bl"></div>
      <div class="hangar-corner br"></div>
    </div>
    <div class="hangar-glitch"></div>
  </div>
```

**Step 3: Verify**

Run: `grep -n "hangar-glitch\|glitchBurst" shared/drill.html`
Expected: 4+ matches (CSS rule + keyframe + HTML element + activate rule).

**Step 4: Commit**

```bash
git add shared/drill.html
git commit -m "drill: add glitch-burst chromatic flash at slam moment"
```

---

## Task 7: Boot-up scan line

**Why:** As doors retract, a thin horizontal gradient line sweeps top-to-bottom over 600ms, giving the feel of the underlying content "initializing."

**Files:**
- Modify: `shared/drill.html` — CSS + HTML for the boot-scan layer

**Step 1: Add boot-scan CSS**

Insert after Task 6 glitch CSS:

```css
    /* Boot-up scan — thin gradient line sweeps down after doors retract */
    .hangar-bootscan {
      position: absolute;
      left: 0;
      right: 0;
      top: 0;
      height: 2px;
      pointer-events: none;
      opacity: 0;
      background: linear-gradient(90deg,
        rgba(34, 211, 238, 0.0) 0%,
        rgba(34, 211, 238, 0.9) 50%,
        rgba(34, 211, 238, 0.0) 100%);
      box-shadow: 0 0 12px 2px rgba(34, 211, 238, 0.6);
    }
    .hangar-doors-overlay.scan-active .hangar-bootscan {
      animation: bootScan 600ms ease-out forwards;
    }
    @keyframes bootScan {
      0%   { top: 0; opacity: 0; }
      15%  { opacity: 1; }
      85%  { opacity: 1; }
      100% { top: 100%; opacity: 0; }
    }
```

**Step 2: Add boot-scan div to HTML**

Update the overlay HTML from Task 6 to include the boot-scan as the last child:

```html
  <div class="hangar-doors-overlay" id="hangarDoorsOverlay" aria-hidden="true">
    <div class="door-left">
      <span class="seam-glow"></span>
      <div class="door-logo door-logo-left"></div>
    </div>
    <div class="door-right">
      <span class="seam-glow"></span>
      <div class="door-logo door-logo-right"></div>
    </div>
    <div class="hangar-corners">
      <div class="hangar-corner tl"></div>
      <div class="hangar-corner tr"></div>
      <div class="hangar-corner bl"></div>
      <div class="hangar-corner br"></div>
    </div>
    <div class="hangar-glitch"></div>
    <div class="hangar-bootscan"></div>
  </div>
```

**Step 3: Verify**

Run: `grep -n "hangar-bootscan\|bootScan" shared/drill.html`
Expected: 3+ matches.

**Step 4: Commit**

```bash
git add shared/drill.html
git commit -m "drill: add boot-up scan line on door retract"
```

---

## Task 8: JS timing hooks — fire glitch burst and boot-scan at the right moments

**Why:** The CSS is ready; now wire up the JS so the `.slam-pulse`, `.glitch-active`, and `.scan-active` classes get toggled at the correct times during the transition.

**Files:**
- Modify: `shared/drill.html` lines 2906-2917 (the `doorsTransition` function from Task 8's baseline — note line numbers shift as we add CSS above, so search for the function by name)

**Step 1: Replace doorsTransition()**

Find the function:

```javascript
      // ---- HANGAR DOOR TRANSITION ----
      function doorsTransition(callback, midCallback) {
        const overlay = document.getElementById('hangarDoorsOverlay');
        overlay.classList.add('active');
        setTimeout(() => overlay.classList.add('doors-closed'), 80);
        setTimeout(() => { if (midCallback) midCallback(); }, 1100);
        setTimeout(() => overlay.classList.remove('doors-closed'), 1200);
        setTimeout(() => {
          overlay.classList.remove('active');
          if (callback) callback();
        }, 2300);
      }
```

Replace with:

```javascript
      // ---- HANGAR DOOR TRANSITION ----
      function doorsTransition(callback, midCallback) {
        const overlay = document.getElementById('hangarDoorsOverlay');
        overlay.classList.add('active');

        // 80ms: doors start closing
        setTimeout(() => overlay.classList.add('doors-closed'), 80);

        // 1080ms: doors about to meet — trigger slam-pulse + glitch-burst
        setTimeout(() => {
          overlay.classList.add('slam-pulse');
          overlay.classList.add('glitch-active');
        }, 1080);

        // 1100ms: content swap happens under the closed doors (existing behavior)
        setTimeout(() => { if (midCallback) midCallback(); }, 1100);

        // 1200ms: doors retract; boot-scan sweeps down over the revealed content
        setTimeout(() => {
          overlay.classList.remove('doors-closed');
          overlay.classList.remove('slam-pulse');
          overlay.classList.remove('glitch-active');
          overlay.classList.add('scan-active');
        }, 1200);

        // 2300ms: teardown
        setTimeout(() => {
          overlay.classList.remove('active');
          overlay.classList.remove('scan-active');
          if (callback) callback();
        }, 2300);
      }
```

**Step 2: Verify timing additions**

Run: `grep -n "slam-pulse\|glitch-active\|scan-active" shared/drill.html`
Expected: 6+ matches (CSS activators from earlier tasks + JS add/remove calls).

**Step 3: Commit**

```bash
git add shared/drill.html
git commit -m "drill: wire doorsTransition to fire slam-pulse, glitch, and boot-scan"
```

---

## Task 9: Accessibility — wrap decorative effects in prefers-reduced-motion

**Why:** Users with motion sensitivity shouldn't see the glitch, scan lines, boot-scan, or corner-bracket slide. Doors still need to slide (it's the core state transition) but all polish disables.

**Files:**
- Modify: `shared/drill.html` — wrap specific animations in the media query

**Step 1: Add reduced-motion overrides**

Insert after Task 7 boot-scan CSS (so this block is the last hangar-related CSS):

```css
    /* ===== Reduced-motion fallback ===== */
    @media (prefers-reduced-motion: reduce) {
      /* Scan lines are static (no sweep animation) */
      .hangar-doors-overlay.active .door-left::before,
      .hangar-doors-overlay.active .door-right::after {
        animation: none;
      }
      /* Corner brackets appear/disappear without slide-in */
      .hangar-doors-overlay.doors-closed .hangar-corner {
        transition: opacity 0.2s ease;
        transform: translate(0, 0) !important;
      }
      .hangar-doors-overlay.doors-closed .hangar-corner.tl,
      .hangar-doors-overlay.doors-closed .hangar-corner.tr,
      .hangar-doors-overlay.doors-closed .hangar-corner.bl,
      .hangar-doors-overlay.doors-closed .hangar-corner.br {
        transition-delay: 0s;
      }
      /* Glitch burst and boot-scan disabled */
      .hangar-doors-overlay.glitch-active .hangar-glitch { animation: none; opacity: 0; }
      .hangar-doors-overlay.scan-active .hangar-bootscan { animation: none; opacity: 0; }
      /* Logo scale-pulse disabled */
      .hangar-doors-overlay.slam-pulse .door-logo-left,
      .hangar-doors-overlay.slam-pulse .door-logo-right {
        animation: none;
      }
    }
```

**Step 2: Verify**

Run: `grep -n "prefers-reduced-motion" shared/drill.html`
Expected: one new match in the hangar block.

**Step 3: Commit**

```bash
git add shared/drill.html
git commit -m "drill: reduced-motion fallback for hangar-doors polish"
```

---

## Task 10: Deploy + live visual verification

**Why:** All the CSS/HTML/JS is assembled. Now push and check the animation end-to-end on the live site.

**Step 1: Validate all JSON files still parse (no collateral damage)**

Run:
```bash
cd ~/Downloads/caet-practice-public
python3 -c "
import json, glob
files = ['master-bank.json'] + glob.glob('training/caet/*/data/*.json')
for p in files: json.load(open(p, encoding='utf-8'))
print(f'Valid JSON: {len(files)} files')
"
```
Expected: `Valid JSON: 17 files`

**Step 2: Push to GitHub Pages**

```bash
git push origin main
```

**Step 3: Wait for Pages build**

Run:
```bash
for i in 1 2 3 4 5; do
  status=$(gh api repos/00ainick-cmd/caet-practice-public/pages/builds/latest --jq '.status' 2>/dev/null)
  [ "$status" = "built" ] && { echo "built"; break; }
  [ $i -lt 5 ] && sleep 20
done
```
Expected: `built` (within 1–2 minutes)

**Step 4: Verify the new CSS is present on the live site**

Run:
```bash
curl -s https://00ainick-cmd.github.io/caet-practice-public/shared/drill.html | grep -c "hangar-corner\|door-logo\|hangar-glitch\|hangar-bootscan\|slam-pulse"
```
Expected: ≥20 matches (all new classes present in live HTML/CSS).

**Step 5: Visual smoke test in browser (human step)**

1. Open https://00ainick-cmd.github.io/caet-practice-public/
2. Click "Drill Mode"
3. Pick any module → hit Start
4. Observe: doors slide in with slate-navy face + scan-lines; CAET logo halves meet at center and pulse; glitch flash at slam; doors retract with boot-scan sweep
5. End the drill → verify same sequence plays again
6. Start a second drill (without refresh) → verify no stuck classes, overlay tears down cleanly
7. Mobile viewport (DevTools iPhone 14) → verify frame rate and logo alignment
8. Toggle OS reduced-motion preference → verify simplified fallback

If any step looks wrong, note specifically what and we iterate.

**Step 6: No commit required for this task — it's verification only.** Final state is already pushed.

---

## Task 11 (if needed): Iterate on visual feedback

**Why:** Live smoke test may reveal specifics that need adjusting (color too bright, timing too fast, etc.). This task is a placeholder for iteration — scope depends on what the smoke test surfaces.

**Step 1:** Note specific feedback from Task 10 step 5.

**Step 2:** For each note, make the minimal CSS/JS change and commit.

**Step 3:** Re-deploy and re-verify.

---

## Rollback plan

If any task causes visible breakage after deploy:

```bash
git revert HEAD             # revert the last commit
git push origin main        # ship the revert
```

Each task is committed independently, so rolling back one won't undo earlier tasks.
