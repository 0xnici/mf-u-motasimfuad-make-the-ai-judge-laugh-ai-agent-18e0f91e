#!/usr/bin/env python3
"""make.fun entry: write the one-line agent confession to entry.txt."""
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    # Copy raw bytes so the one-line answer stays byte-exact, with no newline added.
    answer = (HERE / "answer.txt").read_bytes()
    # Recreate the folder only if absent; an existing /output is never deleted.
    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "entry.txt").write_bytes(answer)


if __name__ == "__main__":
    main()
