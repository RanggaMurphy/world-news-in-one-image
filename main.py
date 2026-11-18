#!/usr/bin/env python3
"""Entry for make.fun's news-image-20261118 — "Sum up 18 November's world news in one image".

The image beside this file (entry.png) is a one-page broadsheet of Wednesday
18 November 2026: the U.S.–Iran Gulf escalation, the Xi–Putin–Trump Shenzhen
summit, Ukraine's strike on the Kerch Bridge, the Democrats' 56–44 Senate win,
DR Congo's Ebola outbreak, the U.S. losing measles elimination status, and
Voyager 1 reaching one light-day from Earth. It was designed and rendered from
frontpage.html in this repository.

The program's whole job is to copy that image to the output directory as
entry.png — byte for byte, so two runs always write identical bytes and no
network is needed.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).resolve().parent / "entry.png"
    shutil.copyfile(source, out_dir / "entry.png")


if __name__ == "__main__":
    main()
