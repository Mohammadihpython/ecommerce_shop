import random
from optparse import Values
from pprint import pprint
from random import choices

import pandas as pd
import pathlib
import os
file_path = pathlib.Path('../inventory/fixtures/_db_product_fixture.json')

# .joinpath('inventory', 'fixtures','db_product_fixture_add_category.json')
print(file_path)
# file_path = os.path.dirname(__file__) + "/../inventory/fixtures/db_product_fixture_add_category.json"

df = pd.read_json(file_path, orient='records',)

print(df)
for field in df.fields:
    field["category"] = str(random.choice(range(1,20)))
    
df.to_json(file_path ,orient='records' )

