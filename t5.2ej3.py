import pandas as pd

df = pd.read_csv('adultos.csv', sep=';')
print(df)
df.replace({'sex':{0:'Hombre', 1:'Mujer'},
            'race':{0:'Blanco', 1:'Negro', 2:'Asiático', 3:'Otros'},
            'income': {-1:'<=50k', 1:'>=50k'}}, inplace=True)
mujeres = df[df['sex'] == 'Mujer']
mujeres_alto_ingreso = mujeres[df['income'] == '>=50k']
porcentaje = len(mujeres_alto_ingreso) * 100 / len(mujeres)
print("El porcentaje de mujeres que tienen un ingreso superior a 50k anual es del ", round(porcentaje,2), "%")