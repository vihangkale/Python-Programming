import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 10])
print("\nSeries1:")
print(ds1)
print("\nSeries2:")
print(ds2)
print("\nCompare the elements of the said Series:")
print("\nEquals:")
print(ds1 == ds2)
print("\nGreater than:")
print(ds1 > ds2)
print("\nLess than:")
print(ds1 < ds2)
