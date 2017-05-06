@ECHO OFF
set PYSAIHOME=.
set X3DJSONLD=..\X3DJSONLD
set PYTHONPATH=C:\Python27;c:\Python27\Scripts
set PATH=%PYTHONPATH%;%JDK_HOME%\bin:%JDK_HOME%\jre\lib\amd64\server:%PATH%
set CLASSPATH=.;%PYSAIHOME%\saxon9he.jar;%PYSAIHOME%\X3DJSAIL.3.3.classes.jar
set PYTHON=python.exe
set PIP=pip.exe
set NODE=node.exe
@ECHO ON

%PYTHON% -m pip install --upgrade pip setuptools
%PYTHON% -m pip install --upgrade Cython
%PIP% install pyjnius
%PIP% install bs4
%PIP% install lxml
%PYTHON% classes.py
%PYTHON% fieldtypes.py
%PYTHON% parseom.py
echo did not cp X3Dautoclass.py fieldTypes.js mapToMethod.js ../X3DJSONLD


javac -classpath "./saxon9he.jar" *.java

x3d2py

FOR %%i IN ("*.py") DO %PYTHON% %%i

