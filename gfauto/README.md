# GraphicsFuzz auto

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Build Status](https://paulthomson.visualstudio.com/gfauto/_apis/build/status/google.graphicsfuzz?branchName=master)](https://paulthomson.visualstudio.com/gfauto/_build/latest?definitionId=2&branchName=master)


## GraphicsFuzz auto is a set of Python scripts for running GraphicsFuzz

[GraphicsFuzz](https://github.com/google/graphicsfuzz) provides tools that automatically find and simplify bugs in graphics shader compilers.
GraphicsFuzz auto (this project) provides scripts for running these tools with minimal interaction.

## Development setup

> Optional: if you have just done `git pull` to get a more recent version of GraphicsFuzz auto, consider deleting `.venv/` to start from a fresh virtual environment. This is rarely needed.

> On Windows, you can use the Git Bash shell, or adapt the commands (including those inside `dev_shell.sh.template`) to the Windows command prompt.

Execute `./dev_shell.sh.template`. If the default settings don't work, make a copy of the file called `dev_shell.sh` and modify according to the comments before executing. `pip` must be installed for the version of Python you wish to use. Note that you can do e.g. `export PYTHON=python3.6.8` to set your preferred Python binary. We currently target Python 3.6.

> Pip for Python 3.6 may be broken on certain Debian distributions.
> You can just use the newer Python 3.7+ version provided by your
> distribution.
> See "Installing Python" below if you want to use Python 3.6.

The script generates and activates a Python virtual environment (located at `.venv/`) with all dependencies installed.

* Execute `./check_all.sh` to run various presubmit checks, linters, etc.
* Execute `./fix_all.sh` to automatically fix certain issues, such as formatting.


### PyCharm

Use PyCharm to open the top-level `gfauto` directory.
It should pick up the Python virtual environment (at `.venv/`) automatically
for both the code
and when you open a `Terminal` or `Python Console` tab.

Install and configure plugins:

* Protobuf Support
* File Watchers (may already be installed)
  * The watcher task should already be under version control.
* Mypy: the built-in PyCharm type checking uses Mypy behind-the-scenes, but this plugin enhances it by using the latest version and allowing the use of stricter settings, matching the settings used by the `./check_all.sh` script.

Add `whitelist.dic` as a custom dictionary (search for "Spelling" in Actions). Do not add words via PyCharm's "Quick Fixes" feature, as the word will only be added to your personal dictionary. Instead, manually add the word to `whitelist.dic`.

## [Coding conventions](docs/conventions.md)

## Symlinking other scripts

GraphicsFuzz auto moves fast and so it is useful to add symlinks to other repositories that contain Python scripts that depend on GraphicsFuzz auto. This allows you to search for all references before changing a function. A `temp/` directory exists for this purpose. For example:

```sh
cd temp
ln -s /path/to/shader-generation shader-generation
```

Now any scripts in the `shader-generation` repository are visible in PyCharm.

You can execute scripts in this repository by opening a Terminal in PyCharm.

## Terminal

The `Terminal` tab in PyCharm is useful and will use the project's Python virtual environment. In any other terminal, use:

* `source .venv/bin/activate` (on Linux)
* `source .venv/Scripts/activate` (on Windows with the Git Bash shell)
* `.venv/Scripts/activate.bat` (on Windows with cmd)

You can alternatively execute the `./dev_shell.sh` script, but this is fairly slow as it checks and reinstalls all dependencies

## Fuzzing

To start fuzzing, create and change to a directory outside the `gfauto/` directory. E.g. `/data/temp/gfauto_fuzzing/2019_06_24`. From here, create `references/` and `donors/` directories containing GLSL shader jobs as used by GraphicsFuzz.
You can get some samples from the GraphicsFuzz project.

```sh
mkdir references/ donors/
cp /data/graphicsfuzz_zip/samples/310es/* references/
cp /data/graphicsfuzz_zip/samples/310es/* donors/
```

Now run the fuzzer.

```sh
gfauto_fuzz
```

It will fail because there is no settings file, but a default `settings.json` file will be created for you.
Review this file.
All plugged Android devices should have been added to the list of devices.
The `active_device_names` list should be modified to include only the unique devices that you care about:

* Including multiple, identical devices (with the same GPU and drivers) is not recommended, as it will currently result in redundant testing.
* `host_preprocessor` should always be included first, as this virtual device detects failures in tools such as `glslangValidator` and `spirv-opt`, and will ensure such failures will not be logged for real devices.
* You can use `--settings SETTINGS.json` to use a settings file other than `settings.json` (the default). In this way, you can run multiple instances of `gfauto_fuzz` in parallel to test *different* devices.

You can generate a space-separated list of seeds as follows:

```python
import secrets

" ".join([str(secrets.randbits(256)) for i in range(0, 1000)])
```

Assuming you saved those to `../seeds.txt`, you can run parallel instances of `gfauto_fuzz` using:

```sh
parallel -j 32 gfauto_fuzz --iteration_seed -- $(cat ../seeds.txt)
```

This is probably only suitable for testing the `host_preprocessor` and `swift_shader` virtual devices; running parallel tests on actual hardware is likely to give unreliable results.

You can run parallel instances of gfauto (just for increased throughput, not with fixed seeds) using:

```sh
parallel -j 32 -i gfauto_fuzz -- $(seq 100)
```

# Installing Python

To manually install Python on your Linux distribution, you can use `pyenv`.

https://github.com/pyenv/pyenv#basic-github-checkout

In summary:

* Install the required packages recommended [here](https://github.com/pyenv/pyenv/wiki/Common-build-problems).

* Then:

```sh
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# Add the following two lines to your ~/.bashrc file.
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

# In a new terminal:
eval "$(pyenv init -)"
pyenv install 3.6.9
pyenv global 3.6.9

# Now execute the development shell script, as usual.
export PYTHON="python"
./dev_shell.sh.template
```

You can reactivate the development shell later,
as explained above, using
`source .venv/bin/activate`,
without having to re-execute the above `pyenv` commands.
