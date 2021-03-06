@ECHO OFF
set PYSAIHOME=.
set X3DJSONLD=..\X3DJSONLD
set PYTHONPATH=C:\Python27;c:\Python27\Scripts
set PATH=%PYTHONPATH%;%JDK_HOME%\bin:%JDK_HOME%\jre\lib\amd64\server:%PATH%
set CLASSPATH=.;%PYSAIHOME%\saxon9he.jar;%PYSAIHOME%\X3DJSAIL.4.0.classes.jar
set PYTHON=python.exe
set PIP=pip3.exe
set NODE=node.exe
@ECHO ON

npm install
%PYTHON% -m pip install --upgrade pip3 setuptools
%PYTHON% -m pip install --upgrade Cython
%PIP% install pyjnius
%PIP% install bs4
%PIP% install lxml
%PYTHON% classes.py
%PYTHON% fieldTypesGenerator.py
%PYTHON% mapToMethodGenerator.py
echo did not cp x3dpsail.py fieldTypes.js mapToMethod.js ../X3DJSONLD


javac RunSaxon.java

java RunSaxon ---overwrite *.x3d
FOR %%i IN ("*.json") DO %NODE% json2py.js %%i


FOR %%i IN ("*.py") DO %PYTHON% %%i

