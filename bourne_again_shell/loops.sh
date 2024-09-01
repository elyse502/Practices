#!/bin/bash

# for loop
for task in {1..100}; do
	echo "$task Hello, World!"
done
echo ""

# while loop
counter=0
while [ $counter -lt 100 ]; do
	echo "$counter Hello, World!"
	((counter++))
done

