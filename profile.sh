#!/bin/bash
export PYTHON=python3
export PIP=pip3
export NODE=node
export JAVA_HOME="/usr"
export JDK_HOME="/usr"
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/lib/jvm/java-15-openjdk-amd64/lib/server/

export PYSAIHOME=.
# export PYTHONPATH=/c/Users/coderextreme/AppData/Local/Programs/Python/Python38/:/c/Users/coderextreme/AppData/Local/Programs/Python/Python38/Scripts:/usr/bin:/c/Python27:/c/Python27/Scripts


export PATH="${PYTHONPATH}:${JAVA_HOME}/bin:${PATH}"
export CLASSPATH=".:${PYSAIHOME}/saxon9he.jar:${PYSAIHOME}/X3DJSAIL.4.0.full.jar"
