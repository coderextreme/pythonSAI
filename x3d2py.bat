REM accepts files with .x3d extension

@ECHO OFF
set PYSAIHOME=.
set X3DJSONLD=..\X3DJSONLD
set PYTHONPATH=C:\Python27;c:\Python27\Scripts
set PATH=%PYTHONPATH%;%JDK_HOME%\bin:%PATH%
set CLASSPATH=.;%PYSAIHOME%\saxon-he-12.1.jar;%PYSAIHOME%\X3DJSAIL.4.0.classes.jar
set PYTHON=python.exe
set PIP=pip3.exe
set NODE=node.exe
@ECHO ON

FOR %%i IN ("*.x3d") DO node_modules/.bin/xslt3 -xsl:X3dToJson.xslt -s:%%i -o:`dirname %%i`/`basename %%i .x3d`.json
FOR %%i IN ("*.json") DO %NODE% json2py.js %%i

