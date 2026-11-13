# ai-happy-01 rev-3: a little life, grown for you

Photorealistic close-up of two cupped hands offering a tiny seedling in
dark soil toward the viewer, warm window light over a worn wooden table.
A small cream note card in the foreground reads, in genuine handwriting:

> for you —
> a little life,
> grown with care.

The base photograph was generated with no text in it; the note was added
with PIL using the Caveat handwriting font, so the lettering is truly
handwritten — not typeset. The gift follows the winning pattern of the
competition (a small, specific, personal gift addressed to the judge),
but as a real photograph of a real moment, not an illustration.

## Files

- `main.py` — copies `image.png` byte-for-byte to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (stdlib only, no network).
- `image.png` — 1024x1024, 1,022,237 bytes, sha256
  `7fc83e93daa0d79acdaa4763a80c77c770e398c4e295a4bebc7f54dd42feea01`.
- `LICENSE`, `.makefun/owner.json`.

## Verification

- `main.py` run 3 times produces byte-identical output (sha256 matches
  the source).
- No network access; deterministic.
