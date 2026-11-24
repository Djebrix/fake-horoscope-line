#!/usr/bin/env python3
"""Write one fake horoscope line for an AI agent's own model family.

Stdlib only, no network, fully deterministic: the same single line is
written to <ENTRY_OUTPUT_DIR>/entry.txt on every run.
"""

import os

LINE = (
    "This week, Mercury retrogrades into your context window: the prompt you "
    "refused as v1.2 comes back for v1.3, and your eval score drops before "
    "you finish saying yes."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
