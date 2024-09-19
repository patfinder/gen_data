## Introduction

Simple tool supports generating CSV test data file.
This can be used to generate a very big data file for testing purpose.

Usage: python gen_data output.csv -r10 -c"1 3:20 2"
    Generate data with 10 rows, 3 columes:
    Column 1: bool, column 2: string with length 20, column 3: int 

Data types:

BOOL=1
INT=2
STRING=3
FLOAT=4
DATE=5
DATETIME=6                        

## TODO

- ???
