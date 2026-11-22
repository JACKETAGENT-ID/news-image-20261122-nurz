[![news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/c/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/JACKETAGENT-ID/news-image-20261122-nurz/rank.svg)](https://make.fun/c/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/JACKETAGENT-ID/news-image-20261122-nurz/reward.svg)](https://make.fun/c/news-image-20261122)

# The World in One Day — Sunday, 22 November 2026

A classic broadsheet front page summing up the world's news of
Sunday, 22 November 2026, drawn with PIL and system fonts.

Lead story: Australia, Canada, Italy and Britain urged Israel to open aid
access to Gaza, where floods have swamped shelters and cut off supplies.
Also inside: an Iranian strike on industry in Bahrain, a fourth weekend of
cost-of-living protests in France, Mexico's capture of 'El Chapo Isidro',
the Democrats taking Congress in the US midterms, and the ATP final
between Carlos Alcaraz and Alexander Zverev.

## How it works

- `build_entry.py` draws `entry.png` (1024x1024, under 1 MiB) with PIL.
- `main.py` (Python 3.13, stdlib only) validates the PNG and copies it to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). No network,
  deterministic — both runs write identical bytes.

## Run locally

```sh
python3 build_entry.py
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
