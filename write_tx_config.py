import glob

with open(".tx/config", mode="r", encoding="utf-8") as f:
    tx_config_orig = f.read()

for filename in glob.glob("gettext/**/*.pot", recursive=True):
    basename = filename.removeprefix("gettext/").removesuffix(".pot")
    name = basename.replace("/", "_")
    if filename not in tx_config_orig:
        with open(".tx/config", mode="a", encoding="utf-8") as f:
            f.write(
f"""
[o:pymc:p:data-umbrella-sprints-website:r:{name}]
file_filter   = locales/<lang>/LC_MESSAGES/{basename}.po
source_file   = {filename}
type          = PO
minimum_perc  = 0
resource_name = {basename}
"""
            )
