#!/bin/bash
source ../X3DJSONLD/venv/Scripts/activate
. ./profile.sh
npm install

javac -cp "saxon-he-12.1.jar;.;xmlresolver-5.1.1.jar;xmlresolver-5.1.1-data.jar" RunSaxon.java
${PYTHON} -m pip install --upgrade pip setuptools
${PYTHON} -m pip install --upgrade Cython
${PYTHON} -m pip install --upgrade pyjnius
${PYTHON} -m pip install --upgrade beautifulsoup4
${PYTHON} -m pip install --upgrade lxml
${PYTHON} classes.py
${PYTHON} fieldTypesGenerator.py
${PYTHON} mapToMethodGenerator.py
echo did not cp x3dpsail.py fieldTypes.js mapToMethod.js ../X3DJSONLD

rm *new* *Round*


bash x3d2py.sh

for i in *.py
do
	FILE=$i
	ls x3d.py package_lock.py mapToMethodGenerator.py X3Dpackage.py packagemaker.py old.py fieldTypesGenerator.py | grep $FILE || ${PYTHON} $FILE 1> /dev/null 2> /dev/null || echo ========================================ERROR $FILE && ${PYTHON} $FILE
done
