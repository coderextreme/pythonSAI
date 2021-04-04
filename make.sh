#!/bin/bash
. ./profile.sh
npm install

javac -cp "saxon9he.jar:." RunSaxon.java
sudo ${PYTHON} -m pip install --upgrade pip setuptools
sudo ${PYTHON} -m pip install --upgrade Cython
sudo ${PYTHON} -m pip install --upgrade pyjnius
sudo ${PYTHON} -m pip install --upgrade beautifulsoup4
sudo ${PYTHON} -m pip install --upgrade lxml
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
