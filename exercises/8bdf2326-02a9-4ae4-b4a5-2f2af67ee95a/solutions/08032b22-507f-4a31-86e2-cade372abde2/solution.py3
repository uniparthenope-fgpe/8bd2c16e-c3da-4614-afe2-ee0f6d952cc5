import pandas as pd

arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
ds = pd.Series(arr)

print(ds.to_string())