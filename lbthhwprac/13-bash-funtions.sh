#!/usr/bin/env bash
function function_A {
    echo $1
}
function function_B {
   echo $1
}
function function_C {
   echo $1
}
function function_D {
   echo Function D.
}
# function calls
# pass parameter to funtion
function_A "Function A."
function_B "Function B."
# pass parameters to function c
function_C "Function C."
function_D
