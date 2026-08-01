// Fails unless the reel's animated wordmark renders pixel-identically to the
// locked LogoA. See src/MarkCheck.jsx for why this exists.
//
// Run: npm run verify:marks
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { readFileSync, mkdirSync, rmSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = dirname(dirname(fileURLToPath(import.meta.url)));
const OUT = join(ROOT, 'out', 'markcheck');
const ENTRY = join(ROOT, 'src', 'index.jsx');

const render = (composition, file) => {
  execFileSync(
    'npx',
    ['remotion', 'still', ENTRY, composition, file, '--frame=0', '--log=error'],
    { cwd: ROOT, stdio: 'inherit' },
  );
  return createHash('md5').update(readFileSync(file)).digest('hex');
};

rmSync(OUT, { recursive: true, force: true });
mkdirSync(OUT, { recursive: true });

const assembled = render('AssembledAtRest', join(OUT, 'assembled.png'));
const locked = render('LockedLogoA', join(OUT, 'logoa.png'));

console.log(`assembled : ${assembled}`);
console.log(`LogoA     : ${locked}`);

if (assembled !== locked) {
  console.error(
    '\nFAIL - the animated wordmark no longer matches the locked LogoA.\n' +
      `Compare ${join(OUT, 'assembled.png')} against ${join(OUT, 'logoa.png')}.\n` +
      'Either the template drifted from LogoA geometry, or brand/marks.jsx changed\n' +
      'and the templates need to follow it. Do not ship the reel until they match.',
  );
  process.exit(1);
}

console.log('\nOK - the animated wordmark is pixel-identical to the locked LogoA.');
