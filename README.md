First checkout from github (get git, if not on your system
```bash
git clone https://github.com/coderextreme/pythonSAI
cd pythonSAI
```
This program reads X3D files (provided) and generates python files.
For a simple smoke test, set your environment in profile.sh, then run the two commands:  You should probably use Python 3.6 with Java 9
Then run these for comparison
```bash
python MFString.py
python sphere.py
python text.py

```

```cmd
profile.bat
python abox.py
```

For more complex stuff, like installing pyjnius, see below

To install pyjnius, see:

https://pyjnius.readthedocs.io/

Python SAI testing harness for X3DJSAIL concrete classes

Install X3DJSONLD https://github.com/coderextreme/X3DJSONLD in sibling folder to pythonSAI

Configure per your environment for Python 3.6 and node.js in profile.sh

Run;
```
sh make.sh
```

Python source code is in local folder.

SAI found in X3Dautoclass.py

SAI generator in classes.py

X3DJSAIL documentation, source, and jars are found here:

http://www.web3d.org/specifications/java/X3dJavaSceneAuthoringInterface.html

classes.py generates X3Dautoclass.py, The PyJNIus interface to X3DJSAIL

The next two are for the PythonSerializer.js:

fieldtypes.py generates fieldTypes.js -- a way to look up info on fields
parseom.py generates mapToMethod.js -- a way to map fields to methods

old.py generates X3Dpackage.py, the old Python SAI, to be replaced by a full SAI

allsaxon.js  -- for Saxon
config.js -- configuration
convertJSON.js -- main convert script
fieldTypes.js – a way to look up info on fields -- generated
json2py.js – calls python serializer
mapToMethod.js – a way to map fields to methods -- generated
mapToMethod2.js – supplemental map to above
moverride.js -- IDK
PythonSerializer.js – main DOM to Python serializer
runAndSend.js -- for Saxon
X3DJSONLD.js -- JSON to DOM converter

Make.sh – main build script
Profile.sh – environment
X3d2py.sh – converts X3D files to JSON

