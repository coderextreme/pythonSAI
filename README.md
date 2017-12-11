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

Retrieve python source code in ../X3DJSONLD

SAI found in X3Dautoclass.py

SAI generator in classes.py

X3DJSAIL documentation, source, and jars are found here:

http://www.web3d.org/specifications/java/X3dJavaSceneAuthoringInterface.html
