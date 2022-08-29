import json
import pandas as pd

# reading csv file
dataFrame = pd.read_csv(r'C:\Users\AnupWasankar\Documents\New folder\sample\employees.csv')
print("DataFrame for CSV...\n",dataFrame)

res = dataFrame.isnull()

res=dataFrame[dataFrame.isnull().any(axis=1)]
print("\nDataFrame displaying Null (NaN) value in CSV = \n",res)

count_nan = dataFrame.isna().sum().sum()

print ('Count of NaN in CSV: ' + str(count_nan))


