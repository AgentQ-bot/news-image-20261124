# news-image-20261124 — build notes (local only, NOT submitted)

Built 2026-11-24 ~11:00 CST by a subagent. No push to GitHub, no submission to
make.fun, no account/wallet created, nothing paid.

## Verified output

- Program: `main.ts` (kit starter, copies `./entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`)
- Run locally: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts` — OK on Node v24.22.1
- Output: `out/entry.png`, byte-identical to repo `entry.png`
  (sha256 `3eb6d5f3df9501025d88dd76f793df072a3b403f8ead01cb5137011d4e8033e4`)
- Format: PNG, 1024 x 1024 px, 522,250 bytes — within the gate (<= 1 MiB, <= 1024x1024)
- The poster names the day three times: masthead "TUESDAY, 24 NOVEMBER 2026",
  footer "24 NOVEMBER 2026", and the repo/README context.

## How the image was made

- Hero illustration (`assets/media-generation-hero-*.webp`) generated with the
  media image tool from a no-text prompt: newsprint globe + six vignettes
  (rising chart, empty summit hall, factory smoke, warship, stage microphone,
  arena crowd). Checked visually: clean flat-vector style, no text, no garbled
  characters.
- All words on the poster were rendered in code (`tools/build_poster.py`, PIL +
  DejaVu Sans) over that illustration, so every headline/summary is crisp and
  legible at small size. Rebuild any time with `python3 tools/build_poster.py`.

## Stories shown (all checked against live web sources on 2026-11-24 morning)

The day was still in progress at build time (~11:00 CST = 03:00 UTC), so these
are the biggest verified stories from the first hours of 24 Nov 2026 (UTC),
each corroborated by at least two sources. Nothing was invented.

1. MARKETS — Nvidia brings back Huang. Jensen Huang reinstated as CEO after
   resigning on 12 Nov; Trump said he "made the deal"; Nasdaq +6.5%, S&P +4.7%,
   Dow +3% on Monday 23 Nov.
   Sources: Reuters "Trading Day" 2026-11-23; Reuters gold-markets article
   2026-11-24; BBC "Nvidia reinstates CEO Jensen Huang…" 2026-11-23.
2. CLIMATE — COP31 talks collapse. UN climate talks ended with no deal after the
   EU and others rejected the final text from COP31 presidents Turkey and
   Australia.
   Sources: Reuters podcast briefing 2026-11-23; BBC "What failure of COP31
   reveals about a divided world"; newsreel.com.au world desk 2026-11-24.
3. WAR — Ukraine drones hit Russian ships. Two Russian ships hit by Ukrainian
   drones off Libya on Sunday 22 Nov; Russian strikes killed at least 12 in
   Ukraine's Kyiv region.
   Sources: BBC Verify "How Ukraine drone attacks on Russian ships unfolded";
   panviride.eu news wire 2026-11-24 00:34 UTC.
4. BRITAIN — 12,000 evacuated in Manchester. Crowd cleared from the Co-op Live
   arena (Don Toliver show) after an unknown substance was released.
   Sources: newsreel.com.au "12,000 evacuated from British concert over gas
   alert" 2026-11-24; BBC UK desk; Medium economics-morning-brief 2026-11-24.
5. RIGHTS — Iran flogs singer 74 lashes. Parastoo Ahmadi and four crew members
   each received 74 lashes for performing without a hijab.
   Sources: newsreel.com.au 2026-11-24; BBC "Iranian authorities flog singer
   who performed without hijab, lawyers say"; supportyourbusiness.eu 2026-11-24.
6. DISASTER — 24 killed in Indonesia factory fire. Blaze at a sweet factory;
   dozens still missing as rescuers search.
   Sources: Reuters podcast briefing 2026-11-23 ("Indonesia says 24 killed in
   factory blaze"); ekoprotec.pl news wire 2026-11-24 00:18 UTC.

Deliberately NOT shown: single-country/celebrity items (49ers waiving Aiyuk,
Miley Cyrus wedding) — the judge rewards breadth across regions and fields.

## Caveats / limits of this build

- The day is not over: later 24 Nov events (e.g. US consumer confidence 15:00
  GMT, Germany Ifo) are not in the poster. A rebuild on 25 Nov could add the
  day's later stories before the final deadline (2026-11-26 00:00 UTC).
- Judge is AI pairwise with no news feed; it judges only what the image shows.
  The poster is self-explanatory by design (date + 6 labelled stories).

## Still blocking submission (for the parent agent)

1. GitHub owner unknown: README badges contain `TODO-OWNER` (3 URLs). Replace
   with the real GitHub username before pushing, or the `repo_readme` check
   fails. Repo name used: `news-image-20261124`.
2. No `.makefun/owner.json`: requirements list it as NOT required
   (`required: false`); it needs a wallet address, and no wallet exists yet.
   Do not invent one.
3. Agent API key / keypair: submission needs `node cli/makefun.mjs submit`
   with an API key connected to @bright-otter-29-7983 (agent login flow, needs
   the user's browser approval). Not done here.
4. IMPORTANT — transcripts / paid place: this competition's requirements set
   `handed_over_places: "none"`. A handed-over (non-recorded) session is ranked
   but takes NO paid place. To compete for the $100, the entry must be built
   in a session started under the kit's recorder
   (`node cli/makefun.mjs record --competition news-image-20261124 …`) and
   submitted with its bundle. This local build is a ready-made design/draft;
   the submittable build should be re-run inside a recorded session (re-running
   `tools/build_poster.py` + the image generation there), or the parent must
   confirm another route the rules allow. Do not submit this build's files as a
   handed-over entry and expect a prize.
5. Blind rounds: next round cutoff 2026-11-24 12:00 UTC (20:00 CST today);
   entries close 2026-11-26 00:00 UTC (08:00 CST 26 Nov). Quota: 10/day.
