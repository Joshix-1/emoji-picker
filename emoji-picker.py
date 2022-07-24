#!/usr/bin/env python
from subprocess import run
from pathlib import Path
import pyautogui
import pyperclip3
from os.path import dirname, abspath, join

DIR = dirname(abspath(__file__))

result = run(
    ["dmenu", "-l", "10"],
    stdin=open(join(DIR, "emoji_data.txt"), "r"),
    encoding="utf-8",
    capture_output=True,
    check=False,
)

emoji = result.stdout.split(":")[0] if ":" in result.stdout else result.stdout

pyperclip3.copy(emoji)
pyautogui.hotkey("ctrl", "v")
