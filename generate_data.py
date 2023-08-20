#!/usr/bin/env python3

from emoji import EMOJI_DATA
from pathlib import Path


LANGUAGES = ("de", "en", "alias")

def normalize(emoji: str) -> str:
    return emoji.strip(":").lower()

emojis: dict[str, set[str]] = {}

for emoji, data in EMOJI_DATA.items():
    names = emojis.setdefault(emoji, set())
    for lang in LANGUAGES:
        if _n := data.get(lang):
            if isinstance(_n, str):
                _n = [_n]
            names.update(map(normalize, _n))


to_write: list[str] = [
    (f"{emoji}: " +  ", ".join(sorted(spam for spam in names)))
    for emoji, names in emojis.items()
]

Path("emoji_data.txt").write_text("\n".join(sorted(to_write)) + "\n", "utf-8")
