from csv import DictReader

import pandas as pd
a = pd.read_csv("test.txt", delimiter=None, header = 'infer').to_dict()[0]
print(a)