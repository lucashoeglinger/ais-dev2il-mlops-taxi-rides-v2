import pandas as pd
import os
import time

df_csv = pd.read_csv('example-data/2025-01-01.taxi-rides.csv')
print(df_csv.dtypes)

df_pq = pd.read_parquet('example-data/2025-01-01.taxi-rides.parquet')
print(df_pq.dtypes)

t = time.time()
pd.read_csv('example-data/2025-01-01.taxi-rides.csv')
csv_time = time.time() - t

t = time.time()
pd.read_parquet('example-data/2025-01-01.taxi-rides.parquet')
pq_time = time.time() - t

print(f'CSV:     {csv_time:.3f}s')
print(f'Parquet: {pq_time:.3f}s')


t = time.time()
for _ in range(365):
    pd.read_csv('example-data/2025-01-01.taxi-rides.csv')
csv_time = time.time() - t

t = time.time()
for _ in range(365):
    pd.read_parquet('example-data/2025-01-01.taxi-rides.parquet')
pq_time = time.time() - t

print(f'CSV:     {csv_time:.1f}s')
print(f'Parquet: {pq_time:.2f}s')
print(f'Parquet is {csv_time / pq_time:.0f}x faster')