#!/usr/bin/env python3

from emoji import EMOJI_DATA
from pathlib import Path

LANGUAGES = ["de", "en", "alias"]

to_write: list[str] = []

for emoji, data in EMOJI_DATA.items():
    data_list = []
    for lang in LANGUAGES:
        if _d := data.get(lang):
            if isinstance(_d, list):
                data_list.extend(_d)
            else:
                data_list.append(_d)
    to_write.append(f"{emoji}: " +  ", ".join(spam.strip(":") for spam in data_list))

sorted(to_write)

Path("emoji_data.txt").write_text("\n".join(to_write), "utf-8")
