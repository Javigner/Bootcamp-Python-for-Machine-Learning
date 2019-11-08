def Proportionbysport(df, year, sport, gender):
    df = df.drop_duplicates(subset=['Sport', 'Year','ID'])
    df_M = df.loc[(df['Sex'] == 'M') & (df['Year'] == year)]
    df_F = df.loc[(df['Sex'] == 'F') & (df['Year'] == year)]
    M_size = df_M.shape[0]
    F_size = df_F.shape[0]
    if (gender == 'M'):
        df_M = df_M.loc[(df_M['Sport'] == sport)]
        return(df_M.shape[0] / M_size)
    elif (gender == 'F'):
        df_F = df_F.loc[(df_F['Sport'] == sport)]
        return(df_F.shape[0] / F_size)
    