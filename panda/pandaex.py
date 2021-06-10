import matplitlib.pylot as plt
import pandas as pd

#creating a dataframe
#dataframes are standardized, agnostic data... frames
pokedf = pd.read_csv('pokedex.txt')

#no repeat pokemon!!!
pokedf.drop_duplicates(inplace=True)

pokedf= pokedf.sort_values(['Generation', 'Total'], ascending=True)

pokedf = pokedf.set_index('Name')

pokedf.head(10).plot(kind='barh')
plt.savefig('/home/student/static/weakpoke.png')

pokedf.head(10).to_excel('/home/student/static/weakopoke.xls')

pokedf.head(10).to_json('/home/student/static/weakopoke.json')

