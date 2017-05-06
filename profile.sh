#!/bin/sh
PYSAIHOME=.
X3DJSONLD=../X3DJSONLD
PYTHONPATH=/c/Python27:/c/Python27/Scripts
export PATH=${PYTHONPATH}:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/amd64/server:${PATH}
export CLASSPATH="${PYSAIHOME}/jslint4java-2.0.5.jar;${PYSAIHOME}/json-schema-validator-2.2.6-lib.jar;${PYSAIHOME}/saxon9he.jar;${PYSAIHOME}/X3DJSAIL.3.3.classes.jar;${PYSAIHOME}/X3DJSAIL.3.3.full.jar"
export PYTHON=python
export PIP=pip
export NODE=node
