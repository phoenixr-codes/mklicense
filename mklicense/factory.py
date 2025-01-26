"""Query defaults for inputs."""

import os
from pathlib import Path
import platformdirs
import subprocess
from subprocess import PIPE, SubprocessError
from attrs import define


@define
class FactoryError(Exception):
    stderr: str | None


def find_script_path() -> Path:
    if (path := os.getenv("MKLICENSE_FACTORY")) is not None:
        return Path(path)
    return Path(platformdirs.user_config_dir("mklicense", "phoenixr"), "factory")


def query(key: str) -> str | None:
    """
    Queries a default value from the factory script for a certain key.

    This function raises an exception when the script ran unsuccessful.
    This function returns `None` when the script has not been found.
    """
    script = find_script_path()
    if not script.is_file():
        return None
    result = subprocess.run([script, key], capture_output=True)
    try:
        result.check_returncode()
    except SubprocessError:
        raise FactoryError(result.stderr.decode("utf8"))
    stdout = result.stdout.decode("utf8")
    if stdout is None:
        return None
    return stdout.rstrip() or None

