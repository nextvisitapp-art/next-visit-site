// Mark fidelity check - the guard behind animating the locked wordmark.
//
// Animating the wordmark needs one wrapper div per tile, so the reel cannot
// simply drop in <LogoA/>. That raises a fair question: is the assembled row
// still the mark, or has it become a variant? (CLAUDE.md 4: the marks are
// locked, never redrawn or restyled.)
//
// This answers it by rendering, not by reading code:
//   AssembledAtRest - the reel's per-tile markup with animation values at rest
//   LockedLogoA     - <LogoA/> imported straight from brand/marks.jsx
// `npm run verify:marks` renders both and fails unless the PNGs are identical.
// Byte-identical output means the animation wrapper changes nothing about the
// mark itself. Re-run it after touching any template that renders the wordmark.
import React from 'react';
import { AbsoluteFill } from 'remotion';
import { FlapChar, LogoA } from '../../../brand/marks.jsx';
import '../../../tokens/tokens.css';
import '@fontsource/space-grotesk/700.css';

// Must match the geometry the reel templates use for the wordmark.
export const MARK_W = 92;
export const MARK_H = Math.round(MARK_W * (70 / 52)); // LogoA's own aspect
export const MARK_GAP = Math.round(MARK_W * 0.077);   // LogoA's own tileGap

const Stage = ({ children }) => (
  <AbsoluteFill
    style={{ alignItems: 'center', justifyContent: 'center', background: 'var(--nv-navy-900)' }}
  >
    {children}
  </AbsoluteFill>
);

// The reel's wordmark markup with every tile settled: opacity 1, no offset.
export const AssembledAtRest = () => (
  <Stage>
    <div style={{ display: 'flex', gap: MARK_GAP }}>
      {[...'NEXTVISIT'].map((c, i) => (
        <div key={i} style={{ opacity: 1, transform: 'translateY(0px)' }}>
          <FlapChar char={c} w={MARK_W} h={MARK_H} />
        </div>
      ))}
    </div>
  </Stage>
);

export const LockedLogoA = () => (
  <Stage>
    <LogoA w={MARK_W} h={MARK_H} />
  </Stage>
);
