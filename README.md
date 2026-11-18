# world-news-in-one-image

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/RanggaMurphy/world-news-in-one-image/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/RanggaMurphy/world-news-in-one-image/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

**The World Today — Wednesday, 18 November 2026, on one page.** A broadsheet
front page that sums up the day's world news in a single 1024×1024 image:

- **U.S. strikes Iran missile site; Iran hits back at U.S. bases** — jets bomb a
  Revolutionary Guards launch site on Qeshm Island at the mouth of the Strait of
  Hormuz; Tehran answers with drone attacks on bases in Bahrain and Kuwait.
- **Xi, Putin and Trump converge on Shenzhen** — the APEC summit ahead of
  Thursday's three-way talks.
- **Ukraine strikes the Crimea Bridge again** — a second day of attacks drops
  part of the Kerch Bridge's road span into the strait.
- **Democrats take the U.S. Senate 56–44** — Mary Peltola's Alaska win, the
  party's biggest Senate majority since 2009.
- **Ebola cases in DR Congo pass 11,000** — the second-largest outbreak on
  record.
- **U.S. loses measles-free status** — 5,412 cases in 2026, ending 26 years of
  elimination.
- **Voyager 1 reaches one light-day from Earth** — 16.1 billion miles out, its
  signal now takes a full day to reach home.

Every story was reported that day by the wires credited on the page (Reuters,
Associated Press, AFP, NASA, the United Nations). The page is drawn in
`frontpage.html` (HTML/CSS with hand-drawn SVG maps, flags and diagrams) and
rendered to `entry.png` at exactly 1024×1024.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program copies `entry.png` to the output directory as `entry.png` — byte
for byte, no network, the same bytes on every run.

---

<sub>Entered on [make.fun](https://make.fun/?ref=kk4vhpqg&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
