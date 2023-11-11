import random
import pandas as pd
import pathlib

file_path = pathlib.Path('../inventory/fixtures/_db_product_fixture.json')
df = pd.read_json(file_path, orient='records',)

for field in df.fields:
    field["category"] = str(random.choice(range(1,20)))

df.to_json(file_path ,orient='records' )

