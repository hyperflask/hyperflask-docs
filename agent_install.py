"""MkDocs hook publishing install.md as-is at the root of the site (https://hyperflask.dev/install.md)
so that coding agents can be pointed at it to set up a new Hyperflask project.
"""

import shutil
from pathlib import Path


INSTALL_FILE = Path(__file__).parent / "install.md"


def on_post_build(config):
    shutil.copyfile(INSTALL_FILE, Path(config.site_dir) / INSTALL_FILE.name)
