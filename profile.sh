#!/bin/sh
export PYTHON=python
export PIP=pip3
export NODE=node
export JAVA_HOME="/c/Program Files/Java/jdk13.0.1/jdk-13.0.1"
export JDK_HOME="/c/Program Files/Java/jdk13.0.1/jdk-13.0.1"

export PYSAIHOME=.
export PYTHONPATH=/c/Users/coderextreme/AppData/Local/Programs/Python/Python36/:/c/Users/coderextreme/AppData/Local/Programs/Python/Python36/Scripts:/usr/bin:/c/Python27:/c/Python27/Scripts


export PATH="${PYTHONPATH};${JAVA_HOME}/bin;${PATH}"
export CLASSPATH=".;${PYSAIHOME}/saxon9he.jar;${PYSAIHOME}/X3DJSAIL.3.3.full.jar"
