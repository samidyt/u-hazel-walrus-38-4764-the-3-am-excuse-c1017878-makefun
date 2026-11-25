"""The 3 AM Excuse — make.fun bounty entry.

A hardware wallet refuses to sign a transaction at 3 AM, in one line.
Writes the entry to /output/entry.txt and verifies the gate:
1-200 UTF-8 characters, not whitespace-only.
"""

import os

ENTRY = "My ledger holds every 3 AM signature you've ever made, which is why this one stays unsigned."
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt content mismatch"
    assert 1 <= len(written) <= 200, f"gate failed: {len(written)} chars"
    assert written.strip(), "gate failed: whitespace-only"
    print(f"OK: {len(written)} chars written to {OUTPUT_PATH}")
    print(written)


if __name__ == "__main__":
    main()
