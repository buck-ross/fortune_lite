# Fortune Lite

The lightweight python-based fortune cookie generator

## Installing

The latest version can be installed by running `pip3 install fortune-lite` from the command line.

## Usage

```
fortune <options>
```
| Argument | Description |
| :--- | :--- |
| -h,<br>--help | Prints a help-dialogue and exits. |
| -v,<br>--version | Prints out version information and exits. |
| -a,<br>-all | Selects from all databases, including offensive fortunes. |
| -e,<br>--equal | Makes it equally likely that the fortune will be selected from any given category, as opposed to making all fortunes equally likely regardless of category. |
| -f,<br>--categories | Instead of printing a fortune, just print a list of all fortune categories (files). |
| -o,<br>--offensive | Only print fortunes marked as offensive. |
| -w,<br>--wait | Wait the specified number of seconds after printing the fortune before exiting. |

## Database Locations

Unlike other fortune programs, Fortune Lite is designed to parse fortunes out of specialized SQLite databases. By default, the Fortune Lite program looks for a database at *~/.fortune.db*, and falls back to the prepackaged database if no database is found in the user's home directory.  
Additionally, the `$FORTUNE_DB` environment variable can be used to override the default database locations, in which case the fortune program will only fall back to the default locations in the event that no database is found at the location stored in `$FORTUNE_DB`.

## Building from Source

  1. Acquire the source code: `git clone https://github.com/buck-ross/fortune_lite.git`.
  2. Enter the source directory: `cd fortune_lite`
  3. **(optional)** Checkout the version you want to build: `git checkout tags/v1.0.1`
  4. Build and install the package: `python3 setup.py install`

## Credit to [fortune-mod](https://github.com/shlomif/fortune-mod)

While *Fortune Lite* is a completely distinct and independent project from *fortune-mod*, we do currently use the datfile sources provided by *fortune-mod* in order to generate the SQLite fortune database. As such, the *fortune-mod* project deserves all credit for creating and the default fortune database.

## [<img src="https://opensource.org/files/osi_symbol.png" width="50">](https://opensource.org/licenses/Apache-2.0) License
Copyright &copy; 2019 Buckley Ross<br/>
**This project is licensed under the [Apache License, Version 2.0 (Apache-2.0)](https://opensource.org/licenses/Apache-2.0).**<br>
For a complete copy of the license, please see the included "LICENSE" file.

