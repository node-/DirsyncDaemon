# pySyncd
Periodically syncs a specified list of folders with a target parent directory. Used for syncing lab data with network drives on Windows.

# Dependencies
Python 2.7, dirsync, schedule

# Config
Set the desired schedule under the "run_daemon" function in pySyncd.py.

Dirsync is not bi-directional, so you have to specify the source and target parent directories. Each line in the config file specifies which directories in the "source" parent directory will be synced with the target parent. 

For example:

sourceParent: '\~/source'

targetParent: '\~/target'

config file contains line: 'test'

This will sync '\~/source/test' with '\~/target/test'

# Install
Run the script on startup and pass the target and source directories as arguments.

For Windows, put a .vbs script with the following line in the startup folder:
```
CreateObject("Wscript.Shell").Run "C:\Python27\python.exe pySyncd.py --source <dir> --target <dir>", 0, True
```
