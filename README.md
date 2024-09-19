

## Todo

- Add unit-test
- Add --skips param for skipping a specified number of rows.

## Introduction

`gen_data` is a convinient tool support generating CSV test data file.
It can be used to generate a very big data file for testing purpose.

```shell
usage: gen_data [-h] -r ROWS [-c COLUMNS] [-t TITLES] csvfile

Generate CSV file with specfied number of rows, and column types.

positional arguments:
  csvfile

options:
  -h, --help            show this help message and exit
  -r ROWS, --rows ROWS  number of rows
  -c COLUMNS, --columns COLUMNS
                        List of colume type, in this format: "t t t:n ..." Where t is type (number), n is column length.
  -t TITLES, --titles TITLES
                        List of column titles

List of supported types: BOOL=1 INT=2 STRING=3 FLOAT=4 DATE=5 DATETIME=6
```

## Setup

```shell

# Clone the repo
git clone git@github.com:patfinder/gen_data.git

# Move to the tool source folder. Then enter below command to setup the tool.
# After this, gen_data will become a script command that you can execute directly.
$ pip install -e .

# Show info of installed script
$ pip show gen_data
Name: gen-data
Version: 0.0.1
Summary: A convinient tool for generating big test data.
Home-page: https://github.com/patfinder/gen_data/
Author: Le Vuong Nguyen
Author-email: vuong.se@gmail.com
License: UNKNOWN
Location: ~/myrepos/gen_data
Requires: 
Required-by: 
```

## Usage

```shell
# Show Help for the command
$ gen_data --help

# Run sample command to generate csv with 5 rows
# and columns of (int, string, string with length 5, int) and column titles
$ gen_data f1.csv -r 5 -c"1,3,3:20,2" -t"is_active,name,job_desc,score"

# Sample output of above command is f1.csv with below content
$ cat f1.csv 
id,is_active,name,job_desc,score
1,False,Louis Martinez,Really tonight we.,559
2,True,Larry Williams,Moment word camera.,845
3,True,Brandon Williams,Wear your consumer.,677
4,False,Chelsea Zamora,Identify itself let.,384
5,True,Jonathan Collier MD,Offer popular.,502
```
