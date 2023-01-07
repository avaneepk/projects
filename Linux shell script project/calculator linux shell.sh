#!/bin/bash

read -p "enter text: " list
arr=($list) 
len=${#arr[@]}

if [ "$len" -ne 3 ]; then
	echo "Expected number of arguements is 3, you gave $len"
fi
num1=${arr[0]}
num3=${arr[2]}
if [ "${arr[1]}" == "+" ]; then
	sum=$(($num1 + $num3))
	echo "$num1 + $num3 = $sum"
	
elif [ "${arr[1]}" == "-" ]; then
	diff=$(($num1 - $num3))
	echo "$num1 - $num3 = $diff"
	
elif [ "${arr[1]}" == "x" ]; then
	mul=$(($num1 * $num3))
	echo "$num1 x $num3 = $mul"
	
elif [ "${arr[1]}" == "/" ]; then
	if [ $num3 == "0" ]; then
		echo "Cannot divide with 0"
	else
	quo=$(($num1 / $num3))
	rem=$(($num1 % $num3))
	echo "$num1 / $num3 = $quo with remainder $rem"
	fi
	
elif [ "${arr[1]}" == "^" ]; then
	pow=$(($num1 ** $num3))
	echo "$num1 ^ $num3 = $pow"
	
elif [ "${arr[1]}" == "%" ]; then
	if [ $num3 == "0" ]; then
		echo "Cannot divide with 0"
	else
	rem=$(($num1 % $num3))
	echo "$num1 % $num3 = $rem"
	fi
else
	echo "Invalid operator, supports +,-,x,/,^ and % operators."

fi
