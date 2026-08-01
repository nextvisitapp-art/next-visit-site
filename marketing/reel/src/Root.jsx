import React from 'react';
import { Composition } from 'remotion';
import { CountdownReel } from './CountdownReel';

// 1080x1920 master per HANDOFF entry 21 (TikTok photo mode + Stories master).
// Must-read content stays inside the safe area: y=320 to y=1450.
export const Root = () => (
  <Composition
    id="CountdownReel"
    component={CountdownReel}
    durationInFrames={390}
    fps={30}
    width={1080}
    height={1920}
    defaultProps={{ days: 38, destination: 'BARCELONA' }}
  />
);
