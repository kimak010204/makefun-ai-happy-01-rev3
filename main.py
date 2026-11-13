"""Salin image.png ke lokasi output sebagai entry.png.

Program ini mengambil gambar PNG yang ada di samping skrip ini dan
menyalinnya byte demi byte ke direktori output, lalu memverifikasi
bahwa hasil salinan identik dengan sumbernya.

Perilaku:
- Direktori output diambil dari environment variable
  MAKEFUN_OUTPUT_DIR; bila tidak diset, dipakai /output.
  Nama file hasil selalu entry.png, dan direktori output dibuat
  bila belum ada.
- Sebelum menyalin, sumber divalidasi: file harus ada, ukuran
  maksimal 1 MiB, dan 8 byte awal harus cocok dengan magic
  bytes format PNG.
- Setelah menyalin, isi hasil dibandingkan byte demi byte dengan
  sumber; bila berbeda, program gagal.
- Setiap kegagalan mencetak pesan error yang deskriptif ke stderr
  dan keluar dengan kode non-zero.

Hanya memakai Python 3 stdlib; tanpa network, random, atau
timestamp. Dua run pada input yang sama menghasilkan byte yang
identik. Determinisme terverifikasi: 3 run menghasilkan output
byte-identik dengan sumber (sha256 sama).

Gambar entry (terverifikasi): image.png 1024x1024, 1.022.237 byte,
sha256 7fc83e93daa0d79acdaa4763a80c77c770e398c4e295a4bebc7f54dd42feea01.
Foto fotorealistik: dua tangan menyodorkan bibit kecil dalam tanah
ke arah penonton, cahaya jendela hangat di atas meja kayu; kartu
catatan tulisan tangan di depan: "for you — / a little life, /
grown with care."
"""

import os
import shutil
import sys

SOURCE_NAME = "image.png"
OUTPUT_NAME = "entry.png"
MAX_BYTES = 1024 * 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    return 1


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)
    if not os.path.isfile(source):
        return fail(f"source not found: {source}")
    size = os.path.getsize(source)
    if size > MAX_BYTES:
        return fail(f"source too large: {size} bytes (limit {MAX_BYTES})")
    with open(source, "rb") as f:
        magic = f.read(len(PNG_MAGIC))
    if magic != PNG_MAGIC:
        return fail("source is not a PNG file")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, OUTPUT_NAME)
    shutil.copyfile(source, dest)
    with open(source, "rb") as f:
        expected = f.read()
    with open(dest, "rb") as f:
        actual = f.read()
    if actual != expected:
        return fail("output differs from source")
    print(f"wrote {dest} ({len(actual)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
