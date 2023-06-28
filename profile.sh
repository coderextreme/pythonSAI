#!/bin/bash
export PYTHON=py.exe
export PIP=pip
export NODE=node
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH};/c/openjdk-20_windows-x64_bin/jdk-20/bin"

export PYSAIHOME=.

export PATH="${PYTHONPATH};${PATH}"
export CLASSPATH=".;${PYSAIHOME}/saxon-he-12.1.jar;${PYSAIHOME}/X3DJSAIL.4.0.full.jar"
