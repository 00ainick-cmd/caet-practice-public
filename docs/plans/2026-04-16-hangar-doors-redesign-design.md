# Hangar-Doors Animation Redesign — Design Document

**Date:** 2026-04-16
**Scope:** Visual upgrade to the hangar-doors transition animation in `shared/drill.html`
**Direction:** Cyber-hangar — extend existing cyber/holographic aesthetic with CAET branding moment

## Motivation

The current hangar-doors animation is functionally correct but visually minimal:
flat dark rectangles slide together with a thin blue glowing seam. Two specific
problems surfaced during review:

1. **Doors are near-invisible against the page background** — both use a similar
   dark navy, so when the doors "close" you mostly see the glowing seam rather
   than an actual door surface meeting in the middle.
2. **No branding moment** — the transition is where a student is waiting ~2
   seconds. That's prime real estate for a CAET brand impression.

## Approach

Approach A (pure CSS enhancement, no new files, no new assets) was chosen over
Approach B (add SVG circuit overlay) and Approach C (add Canvas particle system)
because:

- Lowest risk: all effects are CSS keyframes on existing elements
- Cohesive with the existing cyber/holographic aesthetic already in the site
- GPU-accelerated transforms/opacity — mobile-friendly
- No new files to maintain, no new dependencies

## Visual design

Six layered effects, plus two fixes to the existing door structure:

| # | Effect | Description |
|---|---|---|
| 1 | Door face color + texture | Lighter slate-navy base (`#1a2332`) with subtle hexagonal/circuit pattern overlay — distinctly different from page background so doors are clearly visible when closed |
| 2 | CAET logo split at seam | Left half of shield-logo anchored to inside edge of left door, right half anchored to inside edge of right door — halves meet to form the complete CAET badge centered on viewport. Brief scale-pulse (1.00 → 1.10 → 1.00) at slam moment. |
| 3 | Animated scan lines | Horizontal CRT-style lines sweep down each door face on a ~4-second loop (subtle, ~4% opacity) |
| 4 | Multi-stop neon seam | Cyan → blue → purple vertical gradient on the 3px seam. Box-shadow bloom pulses from 24px at rest to 60px at slam moment. |
| 5 | Corner HUD brackets | Four L-shaped targeting-reticle brackets (one per viewport corner) slide in with 80–120ms stagger when doors close; slide out when they open |
| 6 | Glitch burst at slam | 150ms chromatic-aberration + hue-rotate flash on a full-viewport overlay at the moment doors meet |
| 7 | Boot-up scan | Thin horizontal gradient line sweeps top-to-bottom over 600ms as doors retract, revealing the underlying content |

Corner brackets, glitch burst, and boot-scan together give the transition a
"system-switching" sci-fi feel that mirrors the cyber-grid and holo-card
aesthetic already used elsewhere on the site.

## Architecture

All changes live in `shared/drill.html`. No new files, no new assets (the
logo at `shared/logo.png` is already present).

- **CSS** — new rules added to the existing `<style>` block near the current
  hangar-doors rules (~line 93). About 150 lines total: door face tone +
  texture, `.door-logo-*` rules with `clip-path`, scan-line keyframes, HUD
  bracket pseudo-elements, glitch overlay keyframes, boot-scan keyframes,
  reduced-motion fallback.
- **HTML** — two `.door-logo-*` child elements (one per door) added inside
  the existing `.hangar-doors-overlay` div. One `.hangar-corners` container
  with four L-bracket pseudo-elements. One thin overlay div for the boot-scan.
  Glitch effect uses the existing overlay element via a `.glitch-active` class.
- **JS** — the existing `doorsTransition(callback, midCallback)` function is
  preserved. Only additions: toggle `.glitch-active` class briefly at slam
  (~1080ms) and `.scan-active` class at retract (~1200ms). No changes to
  external callers.

No new event listeners. No new timers. Existing timing contract preserved.

## Timing choreography

Total duration unchanged at ~2.3 seconds.

| Time | Event |
|---|---|
| 0 ms | `.active` added — overlay mounted. Scan lines begin, HUD brackets begin sliding in (80–120 ms stagger) |
| 80 ms | `.doors-closed` added — doors begin closing (1100 ms cubic-bezier). Logo halves ride along |
| ~1080 ms | Doors approaching meeting point — `.glitch-active` added (150 ms burst). Seam glow ramps to 60 px. Logo scale-pulse fires |
| 1100 ms | `midCallback()` runs (content swap under the doors — existing behavior) |
| 1200 ms | `.doors-closed` removed — doors retract. `.scan-active` added — boot-scan sweeps down (600 ms). HUD brackets slide out |
| 2300 ms | `.active` removed — cleanup. `callback()` runs — existing behavior |

The glitch burst runs purely in CSS and doesn't touch the DOM, so it's safe
running in parallel with the midCallback's content swap.

## Accessibility

Non-essential animations wrapped in `@media (prefers-reduced-motion: no-preference)`.
Under reduced motion:

- Doors still slide (essential state transition)
- Logo halves still meet (without scale-pulse)
- Scan lines, glitch burst, boot-scan, and HUD-bracket slide-in all disabled
- HUD brackets appear/disappear instantly without motion

The overlay gets `aria-hidden="true"` since it's decorative.

## Testing

Manual smoke test after deploy:

1. Load https://00ainick-cmd.github.io/caet-practice-public/ → Drill Mode →
   pick a module → Start
2. Verify animation sequence: doors slide in → logo halves align at center →
   glitch burst at slam → question screen under the doors → doors retract →
   boot-scan line sweeps
3. End the drill → verify same sequence plays for end transition
4. Start a second drill without refreshing → verify no stuck classes, overlay
   properly torn down
5. Mobile viewport (Chrome DevTools iPhone 14 preset): verify frame rate stays
   smooth, logo halves align at 50% viewport width
6. Toggle OS "Reduce Motion" → re-run → verify simpler fallback

No automated tests; this is purely visual.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Logo halves misaligned at the seam on non-default viewport widths | Use `transform: translate(±50%, -50%)` relative to the door's inner edge rather than hard pixel positioning — stays aligned at any width |
| Glitch burst triggers motion sensitivity | Wrapped in `prefers-reduced-motion: no-preference` |
| Performance on older mobile devices | All effects use GPU-accelerated `transform` and `opacity` only; no JS animation loop. No blur filters (which are expensive on GPU). If profiling later shows issues, scan-lines and HUD brackets are the first candidates to drop |
| Stuck classes between drills | `doorsTransition` already cleans up `.active` and `.doors-closed` at the end. Add `.glitch-active` and `.scan-active` to the same cleanup path |
