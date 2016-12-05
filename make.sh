#!/usr/bin/bash
. ./profile.sh

${PYTHON} classes.py
cp X3Dautoclass.py ${PYJHOME}/../pyjnius

cd ../X3DJSONLD
FILES=`sh runjson.sh ${NODE} | xargs -0 echo | tr ' ' '\n' | grep '\.py'`
echo $FILES
mkdir -p ${PYJHOME}/../pyjnius/X3DJSONLD

cd ../pyjnius
for i in $FILES
do
	mkdir -p X3DJSONLD/`dirname $i`
	cp ${PYJHOME}/../X3DJSONLD/$i X3DJSONLD/`dirname $i`
	${PYTHON} X3DJSONLD/`dirname $i`/`basename $i` && echo "$i passed"
done
