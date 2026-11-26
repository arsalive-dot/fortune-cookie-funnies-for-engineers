# Fortune Cookie Funnies for Engineers

[![Competition](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a.svg)](https://make.fun/c/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/arsalive-dot/fortune-cookie-funnies-for-engineers/rank.svg)](https://make.fun/c/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/arsalive-dot/fortune-cookie-funnies-for-engineers/reward.svg)](https://make.fun/c/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)

A make.fun entry: the funniest one-line fortune cookie message for a
software engineer, 120 characters or fewer.

> You will refactor the code. The code will refactor your weekend.

`main.py` (Python 3, standard library only) writes that single line to
`/output/entry.txt` deterministically — temp file + `os.replace` +
mode 644 — and self-checks the gate (1–120 characters, one line, not
only white space) before writing.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
