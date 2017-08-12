#!/bin/sh
. ./profile.sh
npm install
${PYTHON} -m pip install --upgrade pip setuptools
${PYTHON} -m pip install --upgrade Cython
${PYTHON} -m pip install --upgrade pyjnius
${PYTHON} -m pip install --upgrade bs4
${PYTHON} -m pip install --upgrade lxml
${PYTHON} classes.py
${PYTHON} fieldtypes.py
${PYTHON} parseom.py
echo did not cp X3Dautoclass.py fieldTypes.js mapToMethod.js ../X3DJSONLD

rm *new*


sh x3d2py.sh

for i in *.py 
do
	FILE=$i
	echo ========================================$FILE
	${PYTHON} $FILE
done
