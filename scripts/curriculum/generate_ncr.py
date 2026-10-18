from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
src_file = ROOT / "docs/widgets/practice_engine.html"
dst_file = ROOT / "docs/widgets/practice_engine_ncr.html"

with open(src_file, "r", encoding="utf-8") as f:
    content = f.read()

# Convert non-ASCII to NCR
ncr_content = ''.join(c if ord(c) < 128 else f'&#{ord(c)};' for c in content)

with open(dst_file, "w", encoding="ascii") as f:
    f.write(ncr_content)

print(f"Generated {dst_file} ({dst_file.stat().st_size:,} bytes). All characters are pure ASCII.")
