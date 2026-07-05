#!/bin/bash
# ============================================
# Advanced Shell Scripting - Variables & Parameters
# ============================================

echo "=== VARIABLES ==="

# Basic variables
name="AJ"
age=25
echo "Name: $name, Age: $age"

# Command substitution (capture command output)
current_date=$(date +"%Y-%m-%d")
echo "Today's date: $current_date"

# Arithmetic
count=10
((count++))
echo "Count after increment: $count"

# Arrays
fruits=("apple" "banana" "cherry")
echo "First fruit: ${fruits[0]}"
echo "All fruits: ${fruits[@]}"
echo "Number of fruits: ${#fruits[@]}"

# Associative arrays (like Python dict)
declare -A user
user[name]="John"
user[age]=30
user[city]="NYC"
echo "User: ${user[name]}, ${user[age]}, ${user[city]}"

echo -e "\n=== PARAMETER EXPANSION ==="

filename="photo_2024.jpg"
echo "Filename: $filename"
echo "Without extension: ${filename%.jpg}"
echo "Extension only: ${filename#*.}"
echo "Uppercase: ${filename^^}"
echo "Lowercase: ${filename,,}"

# Default values
unset var
echo "Default value: ${var:-default}"
echo "Variable is still unset: $var"

# String length
text="Hello World"
echo "Length of '$text': ${#text}"

echo -e "\n=== CONDITIONALS ==="

# File tests
file="test.txt"
if [ -f "$file" ]; then
    echo "$file exists"
else
    echo "$file does not exist"
fi

# Create a test file
touch test.txt
if [ -f "$file" ]; then
    echo "Now $file exists"
fi

# Number comparisons
a=10
b=20
if [ $a -eq $b ]; then
    echo "$a equals $b"
elif [ $a -lt $b ]; then
    echo "$a is less than $b"
else
    echo "$a is greater than $b"
fi

# String comparisons
str1="hello"
str2="world"
if [ "$str1" = "$str2" ]; then
    echo "Strings are equal"
else
    echo "Strings are different"
fi

# AND / OR
if [ -f "$file" ] && [ -r "$file" ]; then
    echo "File exists and is readable"
fi

if [ -f "$file" ] || [ -f "backup.txt" ]; then
    echo "Either file exists"
fi

echo -e "\n=== LOOPS ==="

# For loop - iterate over list
echo "For loop over list:"
for fruit in apple banana cherry; do
    echo "  Fruit: $fruit"
done

# For loop with range
echo -e "\nFor loop with range:"
for i in {1..5}; do
    echo "  Number: $i"
done

# For loop with C-style syntax
echo -e "\nC-style for loop:"
for ((i=0; i<5; i++)); do
    echo "  i = $i"
done

# While loop
echo -e "\nWhile loop:"
count=1
while [ $count -le 3 ]; do
    echo "  Iteration $count"
    ((count++))
done

# Until loop (opposite of while)
echo -e "\nUntil loop:"
count=1
until [ $count -gt 3 ]; do
    echo "  Iteration $count"
    ((count++))
done

# Loop through files
echo -e "\nLoop through Python files:"
for file in *.py; do
    if [ -f "$file" ]; then
        echo "  Found: $file"
    fi
done 2>/dev/null

# Reading file line by line
echo -e "\nReading file line by line:"
echo -e "line1\nline2\nline3" > temp.txt
while IFS= read -r line; do
    echo "  Line: $line"
done < temp.txt
rm temp.txt

echo -e "\n=== FUNCTIONS ==="

# Simple function
greet() {
    echo "Hello, $1!"
}
greet "AJ"

# Function with return value
add() {
    local sum=$(( $1 + $2 ))
    return $sum
}
add 5 3
echo "5 + 3 = $?"

# Function that echoes result (better for capturing)
multiply() {
    local result=$(( $1 * $2 ))
    echo $result
}
product=$(multiply 4 5)
echo "4 × 5 = $product"

# Function with local variables
calculate() {
    local a=$1
    local b=$2
    local sum=$((a + b))
    local diff=$((a - b))
    echo "Sum: $sum, Diff: $diff"
}
calculate 10 3

# Function with error handling
divide() {
    if [ $2 -eq 0 ]; then
        echo "ERROR: Division by zero"
        return 1
    fi
    echo $(( $1 / $2 ))
    return 0
}
divide 10 2
divide 10 0

# Function that modifies global variable
counter=0
increment() {
    ((counter++))
    echo "Counter: $counter"
}
increment
increment
