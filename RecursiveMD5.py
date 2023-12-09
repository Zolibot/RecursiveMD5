import os
import argparse
import hashlib

from tqdm import tqdm

parser = argparse.ArgumentParser(
    prog="RecursiveMD5",
    description="RecursiveMD5is a lightweight and efficient tool\
                that allows users to generate hash values for individual\
                files or entire directories. This software supports\
                a variety of hash algorithms and can be used to\
                verify the integrity of downloaded files or backup data",
    epilog="Don't dig a hole for another, you'll get into it yourself.",
)
parser.add_argument(
    "folder",
    help="Specify the directory path where you intend\
        to utilize the md5 function.",
)
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()

MD5_FILES = []
MAIN_FOLDER = ""


def add_line(destination, data):
    with open(destination + "md5sum.md5", "a") as f:
        f.write(data)
        f.write("\n")


def recursive_dir(folder_path):
    files = os.listdir(folder_path)
    for file in files:
        full_path = os.path.join(folder_path, file)
        if os.path.isdir(full_path):
            recursive_dir(full_path)
        else:
            MD5_FILES.append(full_path)
    return MD5_FILES


def create_md5(file_path):
    h = hashlib.new("md5")
    with open(file_path, "rb") as f:
        file = f.read()
        h.update(file)
    hsh_d = h.hexdigest() + " " + os.path.relpath(file_path, start=MAIN_FOLDER)
    if args.verbose:
        print(hsh_d)
    add_line(MAIN_FOLDER, hsh_d)


def seq_md5(files):
    for file in tqdm(files):
        create_md5(file)


if __name__ == "__main__":
    MAIN_FOLDER = args.folder
    if not os.path.isdir(args.folder):
        raise ValueError("Argument must be a directory")
    print("scan directory")
    f = recursive_dir(args.folder)
    seq_md5(f)
