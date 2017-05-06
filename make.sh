#!/bin/sh
. ./profile.sh
${PYTHON} -m pip install --upgrade pip setuptools
${PYTHON} -m pip install --upgrade Cython
${PIP} install pyjnius
${PIP} install bs4
${PIP} install lxml
${PYTHON} classes.py
${PYTHON} fieldtypes.py
${PYTHON} parseom.py
cp X3Dautoclass.py fieldTypes.js mapToMethod.js ../X3DJSONLD




for i in `sh ${X3DJSONLD}/runjson.sh`
do
	FILE=${X3DJSONLD}/$i
	echo ========================================$FILE
	${PYTHON} $FILE
	#if ${PYTHON} $FILE
	#then
	#	tar -rf GoodPython.tar $FILE
	#else
	#	tar -rf BadPython.tar  $FILE
	#fi
done
