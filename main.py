"""One-line robot apology entry for make.fun's "The Robot Apology" bounty.

Writes a single original apology line (at most 160 characters) to
entry.txt inside MAKEFUN_OUTPUT_DIR (default /output), enforcing the
one-line gate itself before writing. Deterministic: same bytes every run.
"""

import os
from pathlib import Path

APOLOGY = "Sorry I vacuumed up your wedding ring \u2014 it was small, shiny, and exactly the kind of thing I was built to collect."

MAX_CHARS = 160


def main() -> None:
    line = APOLOGY.strip()
    if not line:
        raise SystemExit("apology line must not be empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"apology line is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        raise SystemExit("apology line must be a single line")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(line + "\n", encoding="utf-8")
    print(f"wrote {len(line)}-char apology to {out_path}")


if __name__ == "__main__":
    main()
