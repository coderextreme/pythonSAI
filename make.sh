#!/bin/bash
source venv/Scripts/activate
. ./profile.sh
npm install

# fix punycode require
perl -p -i -e "s/'punycode'/'punycode\/'/" node_modules/ajv-formats-draft2019/formats/idn-hostname.js

javac -cp "saxon-he-12.1.jar;.;xmlresolver-5.1.1.jar;xmlresolver-5.1.1-data.jar" RunSaxon.java
${PYTHON} -m pip install --upgrade pip setuptools
${PYTHON} -m pip install --upgrade Cython
${PYTHON} -m pip install --upgrade pyjnius
${PYTHON} -m pip install --upgrade beautifulsoup4
${PYTHON} -m pip install --upgrade lxml
${PYTHON} -m pip install --upgrade six
${PYTHON} classes.py
${PYTHON} fieldTypesGenerator.py
${PYTHON} mapToMethodGenerator.py
echo did not cp x3dpsail.py fieldTypes.js mapToMethod.js ../X3DJSONLD

rm *new* *Round*


bash x3d2py.sh
node xml2all.js *.x3d

for i in *.py
do
	FILE=$i
	ls x3d.py old.py mapToMethodGenerator.py X3Dpackage.py packagemaker.py old.py fieldTypesGenerator.py | grep $FILE || ${PYTHON} $FILE 1> /dev/null 2> /dev/null || echo ========================================ERROR $FILE && ${PYTHON} $FILE
done
