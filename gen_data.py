import argparse
import csv
from enum import Enum
import random
from faker import Faker
import datetime as DT

# from importlib import reload
# from inspect import getsource


class CsvDataType(Enum):
    """
    Enum of supported data types
    """
    NULL = 0
    BOOL = 1
    INT = 2
    STRING = 3
    FLOAT = 4
    DATE = 5
    DATETIME = 6


MAX_INT_VALUE = 1000

# 1 million
MAX_FLOAT_VALUE = 1000_000.0

# 10 years
MAX_DATE_RANGE = 10*365


def gen_data(nrows=10, ncols=5, titles=None, types=None):
    """
    Generate a list of objects with specified rows and cols.
    """

    if titles is not None and types is not None:
        assert len(titles) == len(types)

    bool_vals = [False, True]

    if titles is None:
        titles = [f'col_{i}' for i in range(1, ncols + 1)]
    # add ID column
    titles.insert(0, 'id')

    if types is None:
        types = [1 for i in range(ncols)]

    rows = []
    fake = Faker()
    today = DT.datetime.now()

    for i in range(nrows):

        row = [i + 1]
        for j in range(ncols):

            if type(types[j]) is tuple:
                col_type, col_len = types[j]
            else:
                col_len = 0
                col_type = types[j]
            
            if col_type == CsvDataType.NULL:
                col = None
            elif col_type == CsvDataType.BOOL:
                col = random.choice(bool_vals)
            elif col_type == CsvDataType.INT:
                col = random.randint(0, MAX_INT_VALUE + 1)
            elif col_type == CsvDataType.STRING:
                col = fake.text(col_len) if col_len else fake.name()
            elif col_type == CsvDataType.FLOAT:
                col = random.random() * MAX_FLOAT_VALUE
            elif col_type == CsvDataType.DATE:
                col = today.date() + DT.timedelta(days=-random.random() * MAX_DATE_RANGE)
            elif col_type == CsvDataType.DATETIME:
                col = today + DT.timedelta(days=-random.random() * MAX_DATE_RANGE)
            else:
                raise Exception(f"Unsupported type: {types[j]}")
            
            row.append(col)
            
        rows.append(row)
    
    return [titles, *rows]


def write_csv(data, file):
    """
    Write data list to file.
    """

    with open(file, 'w') as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        for row in data:
            wr.writerow(row)


def test():

    # Text column definition
    TEXT_COL = (CsvDataType.STRING, 40)

    # Define column types
    cols = [
        *([CsvDataType.NULL]*1),
        *([CsvDataType.BOOL]*1),
        *([CsvDataType.INT]*1),
        *([CsvDataType.STRING]*2),
        *([TEXT_COL]*2),
        *([CsvDataType.FLOAT]*2),
        *([CsvDataType.DATE]*2),
        *([CsvDataType.DATETIME]*2),
    ]

    rows = gen_data(10, len(cols), None, cols)

    return rows


def main():
    parser = argparse.ArgumentParser(
                        prog='gen_data',
                        description='Generate CSV file with specfied number of rows, and column types.',
                        epilog='''List of supported types: 
        BOOL=1
        INT=2
        STRING=3
        FLOAT=4
        DATE=5
        DATETIME=6                        
    ''')

    parser.add_argument('csvfile')
    parser.add_argument('-r', '--rows', required=True, type=int, help='number of rows')
    parser.add_argument('-c', '--columns', required=False, help='List of colume type, in this format: "t t t:n ..." Where t is type (number), n is column length.')
    parser.add_argument('-t', '--titles', required=False, type=str, help='List of column titles')

    # Parse params
    args = parser.parse_args()

    # colume types param
    col_args = args.columns and args.columns.split(',') or None
    cols = []
    for c in col_args:
        if ':' in c:
            c = c.split(':')
            col_type, col_len = CsvDataType(int(c[0])), int(c[1])
            if col_type == CsvDataType.STRING and col_len < 5:
                print('Mininum string length is 5.')
                exit()
            cols.append((col_type, col_len))
        else:
            cols.append(CsvDataType(int(c)))

    # colume titles param
    titles = args.titles and args.titles.split(',') or None

    # generate data
    rows = gen_data(args.rows, len(cols), titles or None, cols or None)

    # save csv
    write_csv(rows, args.csvfile)


if __name__ == '__main__':
    # test()
    main()
