import os
import sys
import stat
import pathlib
import errno

req_file                = tdu.expandPath(ipar.ExtPython.Pyreqs)
install_target          = tdu.expandPath(ipar.ExtPython.Target)
install_script_path     = pathlib.Path(install_target).parents[0] # list of steps in absolute path in reverse. Similart to Parent()

win_file                = install_script_path / "dep_install.cmd"
mac_file                = install_script_path / "dep_install.sh"

# windows template
win_txt = '''
:: update pip
python -m pip install --user --upgrade pip


:: install from requirements file
py -3.9 -m pip install -r "{reqs}" --target="{target}"
'''

mac_txt = '''
#!/bin/bash

dep=$(dirname "$0")
pythonDir=/python

# change current direcotry to where the script is run from
dirname "$(readlink -f "$0")"

# fix up pip with python3
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py

# Update dependencies
# make sure pip is up to date
python3 -m pip install --user --upgrade pip

# install requirements
python3 -m pip install --upgrade -r "{reqs}" --target="{target}"
'''

formatted_win_txt          = win_txt.format(reqs=req_file, target=install_target)
formatted_mac_txt          = mac_txt.format(reqs=req_file, target=install_target)

print("Generating dependency install scripts...")

try:
    os.makedirs('{}/python'.format(install_script_path))
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

with open(str(win_file), "w+") as win_script :
    win_script.write(formatted_win_txt)

with open(str(mac_file), "w+") as mac_script :
    mac_script.write(formatted_mac_txt)

# os.chmod(str(mac_file), stat.S_IXUSR) # TODO: make mac script executable

print("Run dependency install script in Dep/ before beginning")
