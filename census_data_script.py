import json 
import requests 
import pandas as pd
import matplotlib
import hashlib

with open("census_apikey.txt", "r") as f:
    apikey = f.readline().strip()

year = "2021"
variables = "B19013_001E,B17001_002E"  
geo_level = "state:*"
url = (f"https://api.census.gov/data/{year}/acs/acs5?"
       f"get={variables}&for={geo_level}&key={apikey}")

response = requests.get(url)
response.raise_for_status()

json_data = response.json()

columns = json_data[0]  
data_rows = json_data[1:]  
df = pd.DataFrame(data_rows, columns=columns)

df.rename(columns={
    "B19013_001E": "Median_Income",
    "B17001_002E": "Poverty_Rate",
    "state": "State_Code"
}, inplace=True)

checksum = hashlib.md5(df.to_csv(index=False).encode()).hexdigest()
print(f"Data checksum: {checksum}")

output_path = "socioeconomic_data.csv"
df.to_csv(output_path, index=False)
print(f"Data saved to {output_path}")








