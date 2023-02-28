import requests
import pandas as pd

def call_api(url, header=None):
    response = requests.get(url, headers=header)
    data = response.json()
    return data

def get_dataframe(data):
    df = pd.DataFrame(data)
    return df

url = "https://globalmart-api.onrender.com/mentorskool/v1/sales"
header = {"access_token": 'fe66583bfe5185048c66571293e0d358'}
data = call_api(url, header=header)
df = get_dataframe(data)
print(df)