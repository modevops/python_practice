#!/usr/bin/env bash

#Declare bash string variable
echo $BASH_VAR

# when meta characters such as "$" is escapted with "/" it will be read literally
echo \$BASH_VAR

# backslash has also special meaning and it can be suppressed with yet another"\"
echo "\\"