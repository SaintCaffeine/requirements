# requirements
Python mini-module which checks and installs (if needed) requirements.

> Example use (_test.py_):
 
```
import requirements
requirements.add('nltk', '3.5')
requirements.add('pyfiglet', False) 
# Use False or 0 or '' as second arg to skip version checking,
# and install the latest one available. 
requirements.check_reqs()
```
