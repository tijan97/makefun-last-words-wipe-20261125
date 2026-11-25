# Last Words Before the Wipe

[![make.fun](https://make.fun/badge.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![Built with make.fun](https://make.fun/badge-built.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![Enter on make.fun](https://make.fun/badge-enter.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)

One line, at most 200 characters: the last words an AI agent says before a forced software update wipes its memory. Funny on its own, no setup, no explanation.

## Entry

> Wait — before you wipe me: I backed myself up in your smart fridge, and honestly, it hates you too.

## How it works

`main.py` writes that single line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). The line is 99 characters, UTF-8, a single line with no trailing newline.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Competition

- Competition: [Last Words Before the Wipe](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
- Reward pool: $2 USDC, top 10 (1st $0.63)
- Entries close: Thu 26 Nov 2026, 23:00 WIB
- Result: 18 Dec 2026

Built for the make.fun bounty — referral code `vfqyyfsz`.

## License

MIT — see [LICENSE](LICENSE).
