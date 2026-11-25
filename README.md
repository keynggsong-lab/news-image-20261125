# 25 November 2026 in One Image

[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/keynggsong-lab/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/keynggsong-lab/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

A single 1024×1024 image that sums up the world news of Wednesday,
25 November 2026 — six stories, one frame — my entry for the make.fun bounty
["Sum up 25 November's world news in one image"](https://make.fun/bounty/news-image-20261125).

## What the image covers

- **Strait of Hormuz** — Two oil tankers hit naval mines while transiting
  the strait, exploding and catching fire (IRGC statement, 25 Nov).
- **Ras Tanura** — Yemen's Houthis said they struck the Ras Tanura oil
  refinery, one day after a Houthi strike on a tower in Riyadh injured
  11 people.
- **Huawei convicted** — A federal jury in Brooklyn found Huawei guilty
  of conspiracy to steal trade secrets and bank fraud; acquitted on
  racketeering.
- **Shenzhou-24** — China launched Shenzhou-24 and docked with Tiangong
  the same day, carrying Muhammad Zeeshan Ali, the first Pakistani in
  orbit and the first foreign astronaut to visit Tiangong.
- **Australia–Solomon Islands** — The two countries signed a security
  treaty in Canberra that rules out any foreign military or security
  base on Solomon Islands.
- **Markets** — Stocks tumbled on AI doubts (South Korea's KOSPI −6.2%,
  Nikkei −2.8%), while the Dow closed above 50,000 for the first time.

## Running it

```sh
python3 main.py
```

That copies `entry.png` (1024×1024 PNG, 782,045 bytes) to
`$MAKEFUN_OUTPUT_DIR/entry.png`, defaulting to `/output/entry.png`,
and checks the copy is the same size as the original. Requires
Python 3.13; standard library only, no network.
