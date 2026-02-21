@ECHO OFF
set PYSAIHOME=.
set X3DJSONLD=..\X3DJSONLD
set PYTHONPATH=C:\Python27;c:\Python27\Scripts
set PATH=%PYTHONPATH%;%JDK_HOME%\bin:%PATH%
set CLASSPATH=.;%PYSAIHOME%\saxon-he-12.1.jar;%PYSAIHOME%\X3DJSAIL.4.0.classes.jar;%PYSAIHOME%\xmlresolver-5.1.1.jar;%PYSAIHOME%\xmlresolver-5.1.1-data.jar
set PYTHON=python3
set PIP=pip3.exe
set NODE=node.exe
@ECHO ON

npm install
%PYTHON% -m pip install --upgrade pip3 setuptools
%PYTHON% -m pip install --upgrade Cython
%PIP% install pyjnius
%PIP% install beautifulsoup4
%PIP% install lxml
%PYTHON% classes.py
%PYTHON% fieldTypesGenerator.py
%PYTHON% mapToMethodGenerator.py
echo did not cp x3dpsail.py fieldTypes.js mapToMethod.js ../X3DJSONLD

FOR %%i IN ("*.x3d") DO node_modules/.bin/xslt3 -xsl:X3dToJson.xslt -s:%%i -o:`dirname %%i`/`basename %%i .x3d`.json
FOR %%i IN ("*.json") DO %NODE% json2py.js %%i
FOR %%i IN ("*.py") DO %PYTHON% %%i

