import glob

with open(".tx/config", mode="r", encoding="utf-8") as f:
    tx_config_orig = f.read()

existing_filenames = list(glob.glob("gettext/**/*.pot", recursive=True))

for line in tx_config_orig.split("\n"):
    if line.startswith("source_file"):
        filename = line.split("=")[1].strip()
        if filename not in existing_filenames:
            print(f"Unable to find {filename} from tx config in existing files")
