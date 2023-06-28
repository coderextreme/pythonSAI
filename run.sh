
#!/bin/bash

. ./profile.sh

for i in *.py
do
	FILE=$i
	${PYTHON} $FILE 1> /dev/null 2> /dev/null || echo ========================================ERROR $FILE && ${PYTHON} $FILE
done
