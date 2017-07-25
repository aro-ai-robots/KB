#!/bin/bash

c="0"

while [ $c -lt 186605 ]
do
	d="splitFiles/block$c"
	echo scm | cat $d | nc localhost 17001
	wait
	#sleep 0.01
	echo Finished block $c
	#wait
	c=$[$c+1]
done
