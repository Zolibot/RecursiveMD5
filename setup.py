from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='RecursiveMD5',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=["tqdm==4.66.1"],
    entry_points={
        "console_scripts": [
            "recursivemd5=recursivemd5:main",
        ],
    },
)
