#!/usr/bin/env python3
"""Group files in a directory into folders based on their file extensions."""

from argparse import ArgumentParser
from collections import defaultdict
from pathlib import Path
import shutil
import sys


COMPOUND_EXTENSIONS = (
    ".tar.bz2",
    ".tar.gz",
    ".tar.xz",
    ".tar.zst",
)


def get_format(file_path: Path) -> str:
    """Return a folder name derived from the file's extension."""
    filename = file_path.name.casefold()

    for extension in COMPOUND_EXTENSIONS:
        if filename.endswith(extension):
            return extension[1:].upper()

    extension = file_path.suffix
    if not extension:
        return "TANPA_EKSTENSI"

    return extension[1:].upper()


def get_unique_destination(destination: Path) -> Path:
    """Choose a destination path without overwriting an existing file."""
    if not destination.exists() and not destination.is_symlink():
        return destination

    suffix = "".join(destination.suffixes)
    stem = destination.name[:-len(suffix)] if suffix else destination.name
    number = 1

    while True:
        candidate = destination.with_name(f"{stem} ({number}){suffix}")
        if not candidate.exists() and not candidate.is_symlink():
            return candidate
        number += 1


def parse_arguments():
    """Parse the optional directory path."""
    parser = ArgumentParser(
        description="Organize files into folders based on their extensions."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        type=Path,
        default=Path.cwd(),
        help="folder to organize (default: current working directory)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_arguments()
    root = args.directory.expanduser().resolve()
    script_path = Path(__file__).resolve()

    if not root.exists() or not root.is_dir():
        print(f"Error: folder does not exist or is not a directory: {root}")
        return 2

    groups = defaultdict(list)

    try:
        entries = list(root.iterdir())
    except OSError as error:
        print(f"Error: cannot scan folder: {error}")
        return 2

    for item in entries:
        # Only handle regular files directly inside the selected folder.
        # Do not follow symlinks or include hidden files.
        if item.is_symlink() or not item.is_file() or item.name.startswith("."):
            continue
        if item.resolve() == script_path:
            continue

        groups[get_format(item)].append(item)

    if not groups:
        print(f"No eligible files found in: {root}")
        return 0

    print(f"Folder: {root}")
    print("\nScan results:")

    for folder_name, files in sorted(groups.items()):
        print(f"\n{folder_name}/ ({len(files)} file(s))")
        for file_path in sorted(files, key=lambda path: path.name.casefold()):
            print(f"  - {file_path.name}")

    total = sum(len(files) for files in groups.values())
    print(f"\nTotal files to move: {total}")

    try:
        answer = input("Move these files? [y/N]: ").strip().casefold()
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled. No files were moved.")
        return 0

    if answer not in {"y", "yes", "ya"}:
        print("Cancelled. No files were moved.")
        return 0

    moved = 0
    failed = 0

    for folder_name, files in sorted(groups.items()):
        destination_dir = root / folder_name

        try:
            if destination_dir.is_symlink():
                raise OSError("destination folder is a symbolic link")

            destination_dir.mkdir(exist_ok=True)

            if not destination_dir.is_dir():
                raise NotADirectoryError(
                    f"destination is not a directory: {destination_dir}"
                )
        except OSError as error:
            print(f"FAILED to prepare {folder_name}/: {error}")
            failed += len(files)
            continue

        for source in files:
            try:
                destination = get_unique_destination(
                    destination_dir / source.name
                )
                shutil.move(str(source), str(destination))
                print(f"OK: {source.name} -> {folder_name}/{destination.name}")
                moved += 1
            except OSError as error:
                print(f"FAILED: {source.name}: {error}")
                failed += 1

    print("\n=== Finished ===")
    print(f"Moved successfully: {moved}")
    print(f"Failed:             {failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
