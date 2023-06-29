#!/bin/sh

# Run the Test Suite

# accepts files with .x3d extension
export PROCESSORS=${PROCESSORS-8}

. ./profile.sh

javac -cp "saxon-he-12.1.jar;.;xmlresolver-5.1.1.jar;xmlresolver-5.1.1-data.jar" RunSaxon.java

ls *.x3d | xargs -P $PROCESSORS java -cp "saxon-he-12.1.jar;.;xmlresolver-5.1.1.jar;xmlresolver-5.1.1-data.jar" RunSaxon ---overwrite | xargs -P $PROCESSORS ${NODE} json2py.js

#for i in *.x3d
#do
#	echo node_modules/.bin/xslt3 -xsl:X3dToJson.xslt -s:$i -o:`dirname $i`/`basename $i .x3d`.json
#	     node_modules/.bin/xslt3 -xsl:X3dToJson.xslt -s:$i -o:`dirname $i`/`basename $i .x3d`.json && echo "Success"
#done
