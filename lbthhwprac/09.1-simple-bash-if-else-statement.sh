#!/bin/bash
directory="./lbthhwprac"

# bash check if directory exsists
if [-d $directory ]; then
   echo "Directory exsists ${directory}"
else
    echo "Directory does not exsist"
fi