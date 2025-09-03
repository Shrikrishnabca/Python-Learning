# Reading an Excel File
from operator import index

import pandas as pd

# Create some data
data = {
    "Name": ["Krishan", "Ravi"],
    "Age": [30, 28],
    "City": ["Bangalore", "Delhi"]
}
df = pd.DataFrame(data)

# Write to Excel file
df.to_excel("output.xlsx", index=False, engine="openpyxl")

# Reading a specific sheet
df = pd.read_excel("output.xlsx", sheet_name="Sheet1", engine="openpyxl")
print(df)

# Writing multiple sheets:
df = pd.DataFrame(data)
with pd.ExcelWriter("output.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="People", index=False)
    df.to_excel(writer, sheet_name="Summary", index=False)



data = {
    "emp_id": [1,2,3],
    "name": ["shrikrishna", "nagraj", "madhu"],
    "location": ["banglore", "banglore", "banglore"]
}

df = pd.DataFrame(data)
df.to_excel("employs_details", index=False, engine="openpyxl")

df = pd.read_excel("employs_details", engine="openpyxl")
print(df)

data_1 = {
    "phone_number": [123, 435, 124],
    "name": ["shrikrishna", "nagraj", "madhu"],
}

data_2 = {
    "name": ["shrikrishna", "nagraj", "madhu"],
    "height": [5.4, 5.8, 6.0]
}
df_1 = pd.DataFrame(data_1)
df_2 = pd.DataFrame(data_2)
with pd.ExcelWriter("employs_details", engine="openpyxl") as writer:
    df_1.to_excel(writer, "phone_number", index= False)
    df_2.to_excel(writer, "height", index=False)

df_1 = pd.read_excel("employs_details", "phone_number", engine="openpyxl")
print(df_1)

df_2 = pd.read_excel("employs_details", "height", engine="openpyxl")
print(df_2)