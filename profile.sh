#!/bin/sh
PYJHOME=/home/coderextreme
export PATH=/home/coderextreme/node-v7.3.0-linux-x64/bin:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/amd64/server:${PATH}
export CLASSPATH=${PYJHOME}/pythonSAI/jslint4java-2.0.5.jar:${PYJHOME}/pythonSAI/json-schema-validator-2.2.6-lib.jar:${PYJHOME}/pythonSAI/saxon9he.jar:${PYJHOME}/pythonSAI/X3dJavaSceneAccessInterface3.3.classes.jar:${PYJHOME}/pythonSAI/X3dJavaSceneAccessInterface3.3.full.jar
# export CLASSPATH=${PYJHOME}/pyjnius/build/classes:${CLASSPATH}
export PYTHONPATH=${PYJHOME}/pyjnius:${PYTHONPATH}
export PYTHON=python3
export NODE=node
