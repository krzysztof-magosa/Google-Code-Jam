#! /usr/bin/env bash

sets[0]=sample
sets[1]=C-small-practice
sets[2]=C-large-practice

#

path=$(cd $(dirname ${BASH_SOURCE}) && pwd)

for set in ${sets[@]} ; do
    echo "Processing $set..."
    /usr/bin/env time "$path/main.py" < "$path/$set.in" > "$path/$set.out"
    echo
done
