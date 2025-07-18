#!/usr/bin/env python
from subprocess import run
from pathlib import Path
import pyautogui
import pyperclip3
from os.path import dirname, abspath, join

DIR = dirname(abspath(__file__))
FONT = "Noto Sans,Noto Color Emoji" # "Noto Color Emoji"


COMMAND = ["rofi", "-dmenu", "-l", "10"]

result = run(
    COMMAND + (["-fn", FONT] if FONT else []),
    stdin=open(join(DIR, "emoji_data.txt"), "r"),
    encoding="utf-8",
    capture_output=True,
    check=True,
)

emoji = result.stdout.split(":")[0] if ":" in result.stdout else result.stdout

pyperclip3.copy(emoji)
pyautogui.hotkey("ctrl", "v")
