// CountdownReel - the split-flap countdown reel template.
//
// Brand rules honoured here (couples CLAUDE.md + STILLS-BRIEF):
// - Marks are imported from brand/marks.jsx, never redrawn. The wordmark
//   row is assembled from the exported FlapChar atom using LogoA's exact
//   geometry (gap = 7.7% of tile width) so each tile can animate in.
// - Tokens only, no raw colors in this file.
// - One pink moment: the countdown reaching "Today." The AppIcon's pink V
//   is mark-internal and does not count against that budget.
// - Space Grotesk appears only inside the marks. Fraunces for headlines
//   and the hero number, Inter for the tagline, DM Mono for eyebrows.
import React, { useEffect, useState } from 'react';
import {
  AbsoluteFill,
  Sequence,
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  spring,
  Easing,
  delayRender,
  continueRender,
} from 'remotion';
import { FlapChar, AppIcon } from '../../../brand/marks.jsx';
import '../../../tokens/tokens.css';
import '@fontsource/fraunces/600.css';
import '@fontsource/fraunces/700.css';
import '@fontsource/fraunces/600-italic.css';
import '@fontsource/inter/400.css';
import '@fontsource/inter/500.css';
import '@fontsource/dm-mono/500.css';
import '@fontsource/space-grotesk/700.css';

const CREAM = 'var(--nv-cream-100)';
const CREAM_MUTED = 'var(--nv-text-on-dark-muted)';
const PINK = 'var(--nv-pink-500)';

const Eyebrow = ({ children, style }) => (
  <div
    style={{
      fontFamily: 'var(--nv-font-mono)',
      fontSize: 30,
      fontWeight: 500,
      letterSpacing: '0.34em',
      textTransform: 'uppercase',
      color: CREAM_MUTED,
      ...style,
    }}
  >
    {children}
  </div>
);

// Scene 1 - the hook. Frame-one rule from HANDOFF 21: name the feeling the
// viewer is already inside before showing anything of ours.
const Hook = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const line = (delay) => {
    const t = spring({ frame: frame - delay, fps, config: { damping: 16, stiffness: 90 } });
    return {
      opacity: interpolate(frame, [delay, delay + 10, 66, 80], [0, 1, 1, 0]),
      transform: `translateY(${interpolate(t, [0, 1], [46, 0])}px)`,
    };
  };
  return (
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
      <div style={{ textAlign: 'center', padding: '0 90px' }}>
        <Eyebrow style={{ marginBottom: 42, ...line(0) }}>The best bit of a trip</Eyebrow>
        <div
          style={{
            fontFamily: 'var(--nv-font-serif)',
            fontWeight: 600,
            fontSize: 96,
            lineHeight: 1.14,
            color: CREAM,
            textWrap: 'balance',
          }}
        >
          <div style={line(6)}>The trip is booked.</div>
          <div style={{ marginTop: 10, textWrap: 'balance', ...line(18) }}>Now comes the wait.</div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

// Scene 2 - the wordmark assembles tile by tile.
const Wordmark = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const W = 92;
  const H = Math.round(W * (70 / 52));
  const gap = Math.round(W * 0.077);
  const exit = interpolate(frame, [78, 90], [1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  return (
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center', opacity: exit }}>
      <div style={{ display: 'flex', gap }}>
        {[...'NEXTVISIT'].map((c, i) => {
          const t = spring({ frame: frame - i * 3, fps, config: { damping: 13, stiffness: 130 } });
          return (
            <div
              key={i}
              style={{
                opacity: interpolate(frame, [i * 3, i * 3 + 6], [0, 1], {
                  extrapolateLeft: 'clamp',
                  extrapolateRight: 'clamp',
                }),
                transform: `translateY(${interpolate(t, [0, 1], [-150, 0])}px)`,
              }}
            >
              <FlapChar char={c} w={W} h={H} />
            </div>
          );
        })}
      </div>
      <Eyebrow
        style={{
          marginTop: 64,
          opacity: interpolate(frame, [42, 54], [0, 1], {
            extrapolateLeft: 'clamp',
            extrapolateRight: 'clamp',
          }),
        }}
      >
        Count it down together
      </Eyebrow>
    </AbsoluteFill>
  );
};

// Scene 3 - the countdown. Cream all the way down, pink only at the arrival.
const Countdown = ({ days, destination }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const COUNT_END = 96;
  const progress = interpolate(frame, [0, COUNT_END], [0, 1], {
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });
  const n = Math.max(1, Math.ceil(days * (1 - progress)));
  const arrived = frame >= COUNT_END + 2;
  const pop = spring({ frame: frame - (COUNT_END + 2), fps, config: { damping: 12, stiffness: 140 } });
  const enter = interpolate(frame, [0, 10], [0, 1], { extrapolateRight: 'clamp' });
  return (
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center', opacity: enter }}>
      <div style={{ textAlign: 'center' }}>
        {!arrived ? (
          <div
            style={{
              fontFamily: 'var(--nv-font-serif)',
              fontWeight: 700,
              fontSize: 380,
              lineHeight: 1,
              color: CREAM,
              fontVariantNumeric: 'tabular-nums',
            }}
          >
            {n}
          </div>
        ) : (
          <div
            style={{
              fontFamily: 'var(--nv-font-serif)',
              fontWeight: 600,
              fontStyle: 'italic',
              fontSize: 210,
              lineHeight: 1,
              color: PINK,
              transform: `scale(${interpolate(pop, [0, 1], [0.72, 1])})`,
            }}
          >
            Today.
          </div>
        )}
        <Eyebrow style={{ marginTop: 56, opacity: arrived ? interpolate(pop, [0, 1], [0, 1]) : 1 }}>
          {arrived ? 'Enjoy every minute' : `Sleeps until ${destination}`}
        </Eyebrow>
      </div>
    </AbsoluteFill>
  );
};

// Scene 4 - end card on the real marks.
const EndCard = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const icon = spring({ frame, fps, config: { damping: 13, stiffness: 120 } });
  const at = (delay, len = 10) =>
    interpolate(frame, [delay, delay + len], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const W = 34;
  const H = Math.round(W * (70 / 52));
  const gap = Math.round(W * 0.077);
  return (
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <div style={{ transform: `scale(${interpolate(icon, [0, 1], [0.7, 1])})`, opacity: at(0, 6) }}>
          <AppIcon size={230} />
        </div>
        <div style={{ display: 'flex', gap, marginTop: 84, opacity: at(10) }}>
          {[...'NEXTVISIT'].map((c, i) => (
            <FlapChar key={i} char={c} w={W} h={H} />
          ))}
        </div>
        <div
          style={{
            marginTop: 60,
            fontFamily: 'var(--nv-font-sans)',
            fontWeight: 500,
            fontSize: 46,
            color: CREAM,
            opacity: at(18),
          }}
        >
          The countdown you share.
        </div>
        <div
          style={{
            marginTop: 26,
            fontFamily: 'var(--nv-font-mono)',
            fontSize: 30,
            letterSpacing: '0.18em',
            color: CREAM_MUTED,
            opacity: at(26),
          }}
        >
          next-visit.app
        </div>
      </div>
    </AbsoluteFill>
  );
};

export const CountdownReel = ({ days, destination }) => {
  const [fontsHandle] = useState(() => delayRender('fonts'));
  useEffect(() => {
    document.fonts.ready.then(() => continueRender(fontsHandle));
  }, [fontsHandle]);

  return (
    <AbsoluteFill style={{ background: 'var(--nv-navy-950)' }}>
      <AbsoluteFill
        style={{
          background: 'radial-gradient(120% 80% at 50% 32%, var(--nv-navy-900), transparent 62%)',
          opacity: 0.85,
        }}
      />
      <Sequence from={0} durationInFrames={84}>
        <Hook />
      </Sequence>
      <Sequence from={80} durationInFrames={94}>
        <Wordmark />
      </Sequence>
      <Sequence from={172} durationInFrames={130}>
        <Countdown days={days} destination={destination} />
      </Sequence>
      <Sequence from={300} durationInFrames={90}>
        <EndCard />
      </Sequence>
    </AbsoluteFill>
  );
};
