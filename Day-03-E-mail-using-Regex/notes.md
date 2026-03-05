# Day 3 – Email Validator using Regex

## Project Overview
This Python program validates an email address using Regular Expressions (Regex).

## Concepts Used
- Python re module
- Regular expressions
- Pattern matching
- Input validation

## Regex Pattern
^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$

## How to Run
python email_validator_regex.py

## Meaning of Each Symbol

^
➡ Start of the string

[a-z0-9]+
➡ One or more lowercase letters or numbers

[\._]?
➡ Optional dot . or underscore _

[a-z0-9]+
➡ Again letters or numbers

[@]
➡ Must contain @ symbol

\w+
➡ Domain name (like gmail, yahoo)

[.]
➡ Dot before extension

\w{2,3}
➡ Extension like com, in, org

$
➡ End of the string

## Example
Input: vipul123@gmail.com  
Output: Valid Email