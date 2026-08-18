import json
import os

IMG_DIR = os.path.join("img", "beton")
MANIFEST = "betonlijst.json"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}


def load_manifest(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_manifest(entries, filename):
    entries.sort(key=lambda e: e["file"].lower())
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(entries, file, indent=2, ensure_ascii=False)


def main():
    entries = load_manifest(MANIFEST)
    known_files = {e["file"] for e in entries}

    disk_files = {
        name for name in os.listdir(IMG_DIR)
        if os.path.splitext(name)[1].lower() in IMAGE_EXTENSIONS
    }

    added = sorted(disk_files - known_files)
    for file in added:
        entries.append({"file": file, "group": "beton-1", "title": ""})

    removed = [e for e in entries if e["file"] not in disk_files]
    entries = [e for e in entries if e["file"] in disk_files]

    save_manifest(entries, MANIFEST)

    if added:
        print(f"Added {len(added)} new photo(s): {', '.join(added)}")
    if removed:
        print(f"Removed {len(removed)} missing photo(s): {', '.join(e['file'] for e in removed)}")
    if not added and not removed:
        print("No changes, manifest already up to date.")


if __name__ == "__main__":
    main()
