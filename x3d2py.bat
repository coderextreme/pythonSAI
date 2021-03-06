REM accepts files with .x3d extension

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

javac RunSaxon.java

java RunSaxon ---overwrite *.x3d
FOR %%i IN ("*.json") DO %NODE% json2py.js %%i

