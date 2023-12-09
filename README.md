## RecursiveMD5

RecursiveMD5 is a Python program that generates hash values for individual files. ~~It supports a variety of hash algorithms~~ and can be used to verify the integrity of downloaded files or backup data.

### Install

```bash
git clone https://github.com/Zolibot/RecursiveMD5
cd RecursiveMD5
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
python3 -m build
pip install dist/RecursiveMD5-0.0.3-py3-none-any.whl
```

### Usage

To use RecursiveMD5, navigate to the directory where the program is located and run the following command:

```bash
RecursiveMD5 folder
```

Replace "folder" with the path to the directory you want to generate hash values for.

### Optional Arguments

RecursiveMD5 also includes two optional arguments:

```bash
RecursiveMD5 --help
```

* -h, --help: Displays the program's help message and exits.
* -v, --verbose: Enables verbose output.

### Requirements

- RecursiveMD5 requires Python 3.x to run.
- [tqdm](https://tqdm.github.io/)

### License

RecursiveMD5 is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.