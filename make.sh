#!/bin/sh
. ./profile.sh
npm install
${PYTHON} -m pip install --upgrade pip3 setuptools
${PYTHON} -m pip install --upgrade Cython
${PYTHON} -m pip install --upgrade pyjnius
${PYTHON} -m pip install --upgrade bs4
${PYTHON} -m pip install --upgrade lxml
${PYTHON} classes.py
${PYTHON} fieldTypesGenerator.py
${PYTHON} mapToMethodGenerator.py
echo did not cp x3dpsail.py fieldTypes.js mapToMethod.js ../X3DJSONLD

rm *new* *Round*


sh x3d2py.sh

for i in *.py
do
	FILE=$i
	echo ========================================$FILE
	${PYTHON} $FILE
done
