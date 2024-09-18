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

    if types is None:
        types = [1 for i in range(ncols)]

    rows = []
    fake = Faker()
    today = DT.datetime.now()

    for _ in range(nrows):

        row = []
        for j in range(ncols):
            
            if types[j] == CsvDataType.NULL:
                col = None
            elif types[j] == CsvDataType.BOOL:
                col = random.choice(bool_vals)
            elif types[j] == CsvDataType.INT:
                col = random.randint(0, MAX_INT_VALUE + 1)
            elif types[j] == CsvDataType.STRING:
                col = fake.name()
            elif types[j] == CsvDataType.FLOAT:
                col = random.random() * MAX_FLOAT_VALUE
            elif types[j] == CsvDataType.DATE:
                col = today.date() + DT.timedelta(days=-random.random() * MAX_DATE_RANGE)
            elif types[j] == CsvDataType.DATETIME:
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


def run():

    cols = [
        *([CsvDataType.NULL]*1),
        *([CsvDataType.BOOL]*1),
        *([CsvDataType.INT]*3),
        *([CsvDataType.STRING]*3),
        *([CsvDataType.FLOAT]*3),
        *([CsvDataType.DATE]*3),
        *([CsvDataType.DATETIME]*3),
    ]

    rows = gen_data(10, len(cols), None, cols)

    return rows


run()
