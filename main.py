import os
import argparse
import hashlib


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


def create_md5(file_path):
    with open(file_path, "rb") as f:
        file = f.read()
    h = hashlib.new("md5")
    h.update(file)
    return h.hexdigest()


def add_line(destination, data):
    with open(destination + "md5sum.md5", "a") as f:
        f.write(data)
        f.write("\n")


def recursive_dir(folder_path, root_folder):
    md5_files = []
    files = os.listdir(folder_path)
    for file in files:
        full_path = os.path.join(folder_path, file)
        if os.path.isdir(full_path):
            recursive_dir(full_path, root_folder)
        else:
            data = (
                str(create_md5(full_path))
                + " "
                + os.path.relpath(full_path, start=root_folder)
            )
            if args.verbose:
                print(data)
            md5_files.append(data)
            add_line(root_folder, data)
    return md5_files


if __name__ == "__main__":
    root_folder = args.folder
    recursive_dir(args.folder, root_folder)
