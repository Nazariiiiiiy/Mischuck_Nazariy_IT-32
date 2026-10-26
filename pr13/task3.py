import math
import shutil
import sys
from datetime import datetime
from pathlib import Path

NAME = "Ivan"
SURNAME = "Petrenko"
GROUP = "PZ-11"


UNITS = ["B", "KB", "MB", "GB"]


def human_size(size):
    """Розмір у зручному вигляді; одиницю обираємо через math.log."""
    if size <= 0:
        return "0.0 B"
    index = int(math.log(size, 1024))
    if index > len(UNITS) - 1:
        index = len(UNITS) - 1
    value = size / 1024 ** index
    return f"{value:.1f} {UNITS[index]}"


print(f"{NAME} {SURNAME}, {GROUP}")

args = sys.argv[1:]
dry_run = "--dry-run" in args
rest = [a for a in args if a != "--dry-run"]
if len(rest) != 1 or rest[0].startswith("--"):
    print("usage: python3 task3.py [--dry-run] <dir>", file=sys.stderr)
    sys.exit(2)

folder = Path(rest[0])
if not folder.is_dir():
    print(f"error: {folder} is not a directory", file=sys.stderr)
    sys.exit(1)

files = []
for item in folder.iterdir():
    if item.is_file():
        info = item.stat()
        modified = datetime.fromtimestamp(info.st_mtime)
        files.append((modified, item, info.st_size))

if not files:
    print("no files in directory, nothing to do")
    sys.exit(0)

files.sort(key=lambda x: x[0])  


plan = []  # (файл, куди)
width = max(len(item.name) for _, item, _ in files)
for modified, item, size in files:
    month = modified.strftime("%Y-%m")
    target = folder / month / item.name
    plan.append((item, target))
    print(f"{item.name:<{width}}  {human_size(size):>9}  "
          f"{modified:%d.%m.%Y %H:%M}  -> {month}/")

folders = {target.parent for _, target in plan}
summary = f"{len(plan)} files, {len(folders)} folders"

if dry_run:
    print(summary + " (dry run, nothing moved)")
    sys.exit(0)

for _, target in plan:
    if target.exists():
        print(f"error: {target} already exists, nothing was moved", file=sys.stderr)
        sys.exit(1)

start = datetime.now()
for source, target in plan:
    target.parent.mkdir(exist_ok=True)
    shutil.move(str(source), str(target))
print(summary)

reports = Path(__file__).parent / "reports"
reports.mkdir(exist_ok=True)
report_path = reports / f"organize_{start:%Y%m%d_%H%M}.txt"
with report_path.open("w", encoding="utf-8") as f:
    f.write(f"{NAME} {SURNAME}, {GROUP}\n")
    f.write(f"run: {start:%d.%m.%Y %H:%M}\n")
    f.write(f"directory: {folder}\n")
    for source, target in plan:
        f.write(f"{source.name} -> {target.parent.name}/\n")
    f.write(summary + "\n")
print(f"report saved to: reports/{report_path.name}")
