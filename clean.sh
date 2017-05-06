#!/bin/sh

# clean up test files

rm -f `ls *py | grep -v classes.py | grep -v abox.py | grep -v fieldtypes.py | grep -v old.py | grep -v parseom.py` *.sail.js *.x3d.new `ls *.class *.java | grep -v RunSaxon` *.intermediate.* *.diff *.x3d*.json *three.js *.bak *roundtrip* *Canonical* *.run*.txt [0-9]* *.new.json `ls *.json | grep -v Schema | grep -v package.json`
