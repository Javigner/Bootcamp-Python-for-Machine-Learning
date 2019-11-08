def Youngestfellah(df, year):
     df = df.loc[df['Year'] == 2004]
     df_M = df.loc[df['Sex'] == 'M']
     df_F = df.loc[df['Sex'] == 'F']
     Man = df_M.nsmallest(1, 'Age').values[0][3]
     Woman = df_F.nsmallest(1, 'Age').values[0][3]
     result = {'Youngest Man' : Man, 'Youngest Woman' : Woman}
     print (type(result))
     return result