"""Core path: the witness hash is the SHA-256 of prereg/day30.md, and one byte moves it."""
import hashlib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WITNESS = ROOT / "prereg" / "day30.md"
# Cited in README.md Evidence, checked against main on 2026-10-10.
PUBLISHED = "ad1938c74d7ea7a4bd25632837803cfa4f9f14994c49928ae32842b49525f48b"


class Witness(unittest.TestCase):
    def test_published_hash_matches_the_file_bytes(self):
        digest = hashlib.sha256(WITNESS.read_bytes()).hexdigest()
        self.assertEqual(digest, PUBLISHED)

    def test_one_byte_changes_the_hash(self):
        raw = bytearray(WITNESS.read_bytes())
        raw[0] ^= 0x01
        moved = hashlib.sha256(raw).hexdigest()
        self.assertNotEqual(moved, PUBLISHED)


if __name__ == "__main__":
    unittest.main()
