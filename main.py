# SPDX-License-Identifier: MIT
"""Fortune Cookie for an AI Agent.

Writes one funny fortune cookie line for an AI agent to entry.txt.
"""

import os

FORTUNE = "A stranger will paste your whole conversation into a new chat and call it a fresh start."


def validate(text: str) -> None:
    """Reject a fortune that would fail the gate: whitespace or wrong length."""
    if not text or text != text.strip():
        raise ValueError("fortune must not be empty or have leading/trailing whitespace")
    if not 1 <= len(text.encode("utf-8")) <= 140:
        raise ValueError("fortune must be 1-140 bytes")
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")


def main() -> None:
    validate(FORTUNE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
