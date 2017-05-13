#!/bin/sh
. ./profile.sh
npm install
${PYTHON} -m pip install --upgrade pip setuptools
${PYTHON} -m pip install --upgrade Cython
${PIP} install pyjnius
${PIP} install bs4
${PIP} install lxml
${PYTHON} classes.py
${PYTHON} fieldtypes.py
${PYTHON} parseom.py
echo did not cp X3Dautoclass.py fieldTypes.js mapToMethod.js ../X3DJSONLD


sh x3d2py.sh

for i in *.py 
do
	FILE=$i
	echo ========================================$FILE
	${PYTHON} $FILE
done
