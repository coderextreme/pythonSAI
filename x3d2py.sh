#!/bin/sh

# Run the Test Suite

# accepts files with .x3d extension
export PROCESSORS=${PROCESSORS-8}

. ./profile.sh

javac RunSaxon.java

ls *.x3d | xargs -P $PROCESSORS java RunSaxon ---overwrite | xargs -P $PROCESSORS ${NODE} json2py.js
