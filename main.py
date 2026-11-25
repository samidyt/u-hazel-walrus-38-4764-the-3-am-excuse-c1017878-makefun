"""The 3 AM Excuse — make.fun bounty entry.

A hardware wallet refuses to sign a transaction at 3 AM, in one line.
Writes the entry to /output/entry.txt and verifies the gate:
1-200 UTF-8 characters, not whitespace-only.
"""

import os

ENTRY = "My ledger holds every 3 AM signature you've ever made, which is why this one stays unsigned."
OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def check_gate(text: str) -> int:
    """Return the character count, raising if the entry fails the gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise ValueError(f"gate failed: {n} chars, must be {MIN_CHARS}-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("gate failed: entry is whitespace-only")
    return n


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt content mismatch"
    n = check_gate(written)
    byte_len = len(written.encode("utf-8"))
    print(f"OK: {n} chars ({byte_len} bytes) written to {OUTPUT_PATH}")
    print(written)


if __name__ == "__main__":
    main()
