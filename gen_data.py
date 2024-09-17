import csv
import random
from faker import Faker


# from importlib import reload
# from inspect import getsource

def gen_data(nrows=10, ncols=5, titles=None, types=None):
    """
    Generate a list of objects with specified rows and cols.
    """

    if titles is not None and types is not None:
        assert len(titles) == len(types)

    bools = [False, True]

    if titles is None:
        titles = [f'col_{i}' for i in range(1, ncols + 1)]

    if types is None:
        types = [1 for i in range(ncols)]

    rows = []
    fake = Faker()
    for _ in range(nrows):

        row = []
        for j in range(ncols):
            
            if types[j] == 0:
                col = None
            if types[j] == 1:
                col = random.randint(0, 1000)
            elif types[j] == 2:
                col = fake.name()
            else:
                col = random.choice(bools)
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

