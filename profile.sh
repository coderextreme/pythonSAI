#!/bin/bash
export PYTHON=python3
export PIP=pip3
export NODE=node
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/lib/jvm/java-15-openjdk-amd64/lib/server/

export PYSAIHOME=.

export PATH="${PYTHONPATH}:${PATH}"
export CLASSPATH=".:${PYSAIHOME}/saxon-he-10.6.jar:${PYSAIHOME}/X3DJSAIL.4.0.full.jar"
