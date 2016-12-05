#!/bin/sh
PYJHOME=.
export CLASSPATH=${PYJHOME}/../pythoncode/jslint4java-2.0.5.jar:${PYJHOME}/../pythoncode/json-schema-validator-2.2.6-lib.jar:${PYJHOME}/../pythoncode/X3dJavaSceneAccessInterface3.3.classes.jar:${PYJHOME}/../pythoncode/X3dJavaSceneAccessInterface3.3.full.jar
export CLASSPATH=${PJYHOME}/../pyjnius/build/classes:${CLASSPATH}
export PYTHONPATH=${PJYHOME}/../pyjnius:${PYTHONPATH}
export PYTHON=python3
export NODE=nodejs
