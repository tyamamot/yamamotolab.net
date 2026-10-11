#!/usr/bin/env python3
"""記事用の画像を縮小して static/images/YYYY-MM-名前.jpg に保存し、貼り付け用の Markdown を表示する。

使い方（サイトのフォルダで）: 最初に保存先の年月を書き、そのあとに画像を並べる
    python3 tools/addimg.py 2026-09 ~/Desktop/IMG_1234.HEIC ~/Desktop/IMG_1235.jpg
        → static/images/2026-09-img_1234.jpg などに保存
    python3 tools/addimg.py content/posts/2026-09-18-webdb-summer-2026.md 写真/*.jpg
        → 記事ファイル名の日付から 2026-09- を付けて保存
    python3 tools/addimg.py 2026-09 original_images
        → フォルダを渡すと、その中の画像をまとめて処理（original_images/ は git で管理しない置き場）
    python3 tools/addimg.py --width 800 2026-09 thumb.png   # 長辺を変える（既定 1200px）

すること:
  - 長辺を 1200px 以下に縮小（小さい画像は拡大しない）。スマホ写真の向きも直す
  - 位置情報などのメタデータ（EXIF）を削除
  - JPEG / HEIC / その他 → JPEG（品質80）。PNG は PNG のまま（図やスクリーンショット向け）
  - ファイル名は小文字・空白なしに整える。保存先に同じ名前があればスキップ（上書きしない。何度実行しても重複しない）

必要なもの: pip install pillow   （iPhone の HEIC も扱うなら pip install pillow-heif も）
"""
import argparse, re, sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Pillow が必要です: pip install pillow")
try:
    import pillow_heif
    pillow_heif.register_heif_opener()
    HEIF = True
except ImportError:
    HEIF = False

SITE = Path(__file__).resolve().parent.parent


def clean_name(stem):
    s = re.sub(r"[^\w\-]+", "-", stem.strip().lower()).strip("-")
    return s or "image"


EXTS = {".jpg", ".jpeg", ".heic", ".heif", ".png", ".webp", ".gif", ".tif", ".tiff"}


def expand(paths):
    """フォルダが渡されたら、その直下の画像ファイルに展開する"""
    out = []
    for p in paths:
        if p.is_dir():
            out += sorted(f for f in p.iterdir() if f.is_file() and f.suffix.lower() in EXTS)
        else:
            out.append(p)
    return out


def main():
    ap = argparse.ArgumentParser(description="記事用の画像を縮小して static/images/YYYY-MM-名前 に保存する")
    ap.add_argument("month", help="ファイル名の先頭に付ける年月 YYYY-MM（例: 2026-09）、または記事ファイル（例: content/posts/2026-09-18-xxx.md）")
    ap.add_argument("files", nargs="+", type=Path, help="元の画像ファイル、またはフォルダ（例: original_images）")
    ap.add_argument("--width", type=int, default=1200, help="長辺の最大ピクセル数（既定: 1200）")
    ap.add_argument("--quality", type=int, default=80, help="JPEG の品質（既定: 80）")
    a = ap.parse_args()

    mm = re.match(r"(\d{4})-(\d{2})(?:-\d{2}-.*\.md)?$", Path(a.month).name)
    if not mm:
        sys.exit("最初に保存先の年月（例: 2026-09）か記事ファイル（例: content/posts/2026-09-18-xxx.md）を書いてください")
    y, m = mm.groups()
    outdir = SITE / "static" / "images"
    outdir.mkdir(parents=True, exist_ok=True)

    lines = []
    files = expand(a.files)
    if not files:
        sys.exit("処理する画像がありません")
    for src in files:
        if src.suffix.lower() in (".heic", ".heif") and not HEIF:
            print(f"× {src.name}: HEIC を読むには pip install pillow-heif が必要です", file=sys.stderr)
            continue
        dst = outdir / (f"{y}-{m}-" + clean_name(src.stem) + (".png" if src.suffix.lower() == ".png" else ".jpg"))
        if dst.exists():
            print(f"- {src.name}: {dst.relative_to(SITE)} が既にあるのでスキップ（別の画像なら元のファイル名を変えてください）", file=sys.stderr)
            lines.append(f"![](/images/{dst.name})")
            continue
        try:
            im = Image.open(src)
            im = ImageOps.exif_transpose(im)   # 向きを直す
        except Exception as e:
            print(f"× {src.name}: 読めませんでした（{e}）", file=sys.stderr)
            continue
        im.thumbnail((a.width, a.width), Image.LANCZOS)   # 長辺を a.width 以下に（拡大はしない）
        if src.suffix.lower() == ".png":
            im.save(dst, optimize=True)                      # メタデータは書かれない
        else:
            if im.mode != "RGB":
                bg = Image.new("RGB", im.size, "white")
                bg.paste(im, mask=im.getchannel("A") if "A" in im.getbands() else None)
                im = bg
            im.save(dst, "JPEG", quality=a.quality, optimize=True, progressive=True)  # exif を渡さない＝削除
        kb = dst.stat().st_size // 1024
        print(f"○ {src.name} → {dst.relative_to(SITE)}  ({im.width}x{im.height}, {kb}KB)", file=sys.stderr)
        lines.append(f"![](/images/{dst.name})")

    if lines:
        print("\n記事に貼り付け:", file=sys.stderr)
        print("\n\n".join(lines))


if __name__ == "__main__":
    main()
