#!/bin/bash
while read -r a b; do
	for ((i=1;i<=$b;i++)); do
    	echo $a
    done
done < pt_br_full.txt > outt