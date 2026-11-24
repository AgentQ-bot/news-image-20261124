// news-image-20261124 entrypoint (Node 22, standard library only).
// The poster is the entry.png beside this file; the program copies it to
// $MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png inside the grader).
// The output directory is created first, so the copy works on a fresh
// output path as well as on the grader's mounted /output.

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(new URL('./entry.png', import.meta.url), join(outDir, 'entry.png'));
