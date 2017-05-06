#!/bin/sh
export PYTHON=python
export PIP=pip
export NODE=nodejs
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
export JDK_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
export PYSAIHOME=.
export PYTHONPATH=/usr/bin:/c/Python27:/c/Python27/Scripts
export PATH=${PYTHONPATH}:${JAVA_HOME}/bin:${JAVA_HOME}/jre/lib/amd64/server:${PATH}
export CLASSPATH=".:${PYSAIHOME}/saxon9he.jar:${PYSAIHOME}/X3DJSAIL.3.3.classes.jar"
