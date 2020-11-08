#!/usr/bin/env bash

input1="./101php"
input2="./102php"

rm chars


while read line; 
do
	curl http://jh2i.com:50011/site/$line >> chars
done < "$input1"


while read line; 
do
	curl http://jh2i.com:50011/site/$line >> chars
done < "$input2"
