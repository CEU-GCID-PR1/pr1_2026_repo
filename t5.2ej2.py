import pandas as pd

def normalizar(df, columnas, modo="Por_defecto"):
    dfn = df.copy()
    match modo:
        case "Por_defecto":
            norm(dfn, columnas)
        case "Centrada_en_cero":
            norm(dfn, columnas)
            dfn[columnas] -= 0.5
        case "Estandarizar":
            dfn[columnas] = (dfn[columnas] - dfn[columnas].mean()) / dfn[columnas].std()
    return dfn

def norm(df, columnas):
    for col in columnas:
        if (df[col] < 0).any():
            df[col] -= df[col].min()
        df[col] /= df[col].max()
    return df

dataframe = pd.DataFrame({'c1':[1,2,3], 'c2':[5,3,-1], 'c3':[6,-2,0]})
print(dataframe)
print(normalizar(dataframe, ['c1','c2']))
print(normalizar(dataframe, ['c1','c2'], "Centrada_en_cero"))
print(normalizar(dataframe, ['c1','c2'], "Estandarizar"))
