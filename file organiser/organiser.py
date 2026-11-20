from pathlib import Path
import shutil

# 1. Define file categories and extensions
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".json", ".sql"]
}

def get_unique_path(destination: Path) -> Path:
    """Appends a number if a file with the same name already exists."""
    counter = 1
    new_destination = destination
    while new_destination.exists():
        new_destination = destination.with_name(f"{destination.stem}_{counter}{destination.suffix}")
        counter += 1
    return new_destination

def organize_folder(target_dir: str):
    base_path = Path(target_dir).expanduser().resolve()
    
    if not base_path.is_dir():
        print(f"Error: '{base_path}' is not a valid directory.")
        return

    # Map extensions directly to category names for fast lookup
    ext_map = {ext: cat for cat, exts in CATEGORIES.items() for ext in exts}
    moved_count = 0

    for item in base_path.iterdir():
        # Skip folders and the script itself
        if item.is_dir() or item.name == Path(__file__).name:
            continue

        category = ext_map.get(item.suffix.lower(), "Others")
        dest_folder = base_path / category
        dest_folder.mkdir(exist_ok=True)

        dest_path = get_unique_path(dest_folder / item.name)
        shutil.move(str(item), str(dest_path))
        print(f"Moved: {item.name} -> {category}/{dest_path.name}")
        moved_count += 1

    print(f"\nDone! Organized {moved_count} files.")

if __name__ == "__main__":
    # Change this path to target a specific folder, e.g., "~/Downloads"
    folder_to_clean = input("Enter folder path to organize (leave blank for Downloads): ").strip()
    target = folder_to_clean if folder_to_clean else "~/Downloads"
    organize_folder(target)
