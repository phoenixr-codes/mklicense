# MkLicense

MkLicense is a command-line tool for generating an Open Source License.

![Preview](./preview/out1.gif)

MkLicense makes use of the [Textual][] TUI framework and is inspired by [choosealicense][].


> [!IMPORTANT]
> MkLicense is not responsible for correctness and comes with no warranty.

## Installation

```console
pipx install mklicense
```

## Design

### Factory

You can use a "factory" to dynamically create default values for certain parameters. The factory is an executable that accepts the name of the parameter as the only argument.
The factory should print a line representing the default value to be used or no value to omit the value. Here is an example for a factory written in Python:

```python3
#!/usr/bin/env python3

from datetime import date
import sys

param = sys.argv[1]
match param:
    case "Year":
        print(date.today().year)
    case "Name":
        print("John Doe")
```

MkLicense will use the environment variable `MKLICENSE_FACTORY` to infer the path to the executable (or the name of the executable if in `PATH`). If that environment
variable is not set, MkLicense looks if `mklicense/factory` exists in your config directory (e.g. `~/.config/` in Linux) and use that script. The script must be an
executable so make sure to use `chmod +x script_path` and use a shebang at the top of the script.


[choosealicense]: https://choosealicense.com/
[Textual]: https://textual.textualize.io/

