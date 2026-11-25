import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('adultos.csv', sep=';')
data.replace({'sex':{0:'Hombre', 1:'Mujer'},
                   'race':{0:'Blanca',1:'Negra',2:'Asiatica',3:'Otros'},
                   'income':{-1: '<=50k', 1: '>50k'}}, inplace=True)

data.groupby(["sex", "income"]).size().unstack().plot(
    kind='bar',
    title='Ganancias de hombres y mujeres',
    figsize=[10,6]
)
plt.xticks(rotation='horizontal')
#plt.savefig('figura')
plt.show()
plt.close()
