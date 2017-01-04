#!/bin/bash
. ./profile.sh

${PYTHON} classes.py
cp X3Dautoclass.py ${PYJHOME}/pyjnius
mkdir -p ${PYJHOME}/pyjnius/X3DJSONLD

cd ../X3DJSONLD

for i in `sh runjson.sh | grep '\.py'`
do
	cd ../pyjnius
	mkdir -p X3DJSONLD/`dirname $i`
	cp ${PYJHOME}/X3DJSONLD/$i X3DJSONLD/`dirname $i`
	${PYTHON} X3DJSONLD/`dirname $i`/`basename $i` && echo "$i passed"
done
