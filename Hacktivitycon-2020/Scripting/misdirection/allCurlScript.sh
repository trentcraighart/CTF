#!/usr/bin/env bash

input1="./allphp"

rm chars

curl http://jh2i.com:50011/site/ > site
cut -b 120-155 site > allphp


while read line; 
do
	curl http://jh2i.com:50011/site/$line >> chars
done < "$input1"

sort chars > chars
cat chars

