import pandas as pd

def elementos_mayores(df, col, num):
    return df[df[col] > num]

dataframe = pd.DataFrame({'v1': [1,2,3], 'v2':[4,6,7], 'v3': [4,7,9]})
print(dataframe)
print(elementos_mayores(dataframe, 'v3', 5))