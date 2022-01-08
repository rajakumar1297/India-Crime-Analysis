def State(df):
    state_df = df.groupby('STATE_UT').sum()[['MURDER','RAPE','KIDNAPPING','DOWRY_DEATHS','THEFT','ROBBERY','RIOTS','CHEATING','TOTAL_IPC_CRIMES']].sort_values(by=['TOTAL_IPC_CRIMES'],ascending=False)
    return state_df
def Year(df):
    year_df = df.groupby('YEAR').sum()[['MURDER','RAPE','KIDNAPPING','DOWRY_DEATHS','THEFT','ROBBERY','RIOTS','CHEATING','TOTAL_IPC_CRIMES']]
    return year_df
def District(df):
    district_df = df.groupby('DISTRICT').sum()[['MURDER','RAPE','KIDNAPPING','DOWRY_DEATHS','THEFT','ROBBERY','RIOTS','CHEATING','TOTAL_IPC_CRIMES']].sort_values(by=['MURDER'],ascending=False)
    return  district_df

def State_list(df):
    states_list = df.STATE_UT.unique().tolist()
    states_list.sort()
    states_list.insert(0,'Overall')
    return  states_list
def Districs_List(df):
    districts = df.DISTRICT.unique().tolist()
    districts.sort()
    districts.insert(0,'Overall')
    return  districts
def Year_List(df):
    year_list = df.YEAR.unique().tolist()
    year_list.insert(0,'Overall')
    return  year_list
def Crime_List(df):
    Crime_list = df.drop(columns=['YEAR', 'STATE_UT', 'DISTRICT']).columns.tolist()
    Crime_list.sort()
    Crime_list.insert(0,'Overall')
    return Crime_list
def fetch_year_state(year,state,crime,df):
    if year == 'Overall' and state == 'Overall' and crime=='Overall':
        temp = df.groupby('STATE_UT').sum().drop(columns=['YEAR'])
    if year =='Overall' and state == 'Overall' and crime!='Overall':
        temp = df.groupby('STATE_UT').sum().reset_index()[['STATE_UT',crime]]
    if year =='Overall' and state != 'Overall' and crime=='Overall':
        temp = df[df['STATE_UT']==state].groupby('YEAR').sum()
    if year !='Overall' and state == 'Overall' and crime=='Overall':
        temp = df[df['YEAR']==year].groupby('STATE_UT').sum().drop(columns=['YEAR'])
    if year=='Overall' and state!='Overall' and crime!='Overall' :
        temp = df[df['STATE_UT']==state].groupby('YEAR').sum()[[crime]]
    if year!='Overall' and state!='Overall' and crime=='Overall':
        temp = df[(df['YEAR']==year) & (df['STATE_UT']==state)].groupby('YEAR').sum()
    if year!='Overall' and state=='Overall' and crime!='Overall':
        temp = df[df['YEAR']==year].groupby('STATE_UT').sum()[[crime]]
    if year!='Overall' and state!='Overall' and crime!='Overall':
        temp = df[(df['YEAR'] == year) & (df['STATE_UT'] == state)].groupby('YEAR').sum()[crime]
    return temp
def fetch_year_district(year,district,crime,df):
    if year == 'Overall' and district == 'Overall' and crime == 'Overall':
        temp = df.groupby('DISTRICT').sum().drop(columns=['YEAR'])
    if year == 'Overall' and district == 'Overall' and crime != 'Overall':
        temp = df.groupby('DISTRICT').sum()[[crime]]
    if year == 'Overall' and district != 'Overall' and crime == 'Overall':
        temp = df[df['DISTRICT'] == district].groupby('YEAR').sum()
    if year != 'Overall' and district == 'Overall' and crime == 'Overall':
        temp = df[df['YEAR'] == year].groupby('DISTRICT').sum().drop(columns=['YEAR'])
    if year == 'Overall' and district != 'Overall' and crime != 'Overall':
        temp = df[df['DISTRICT'] == district].groupby('YEAR').sum()[[crime]]
    if year != 'Overall' and district != 'Overall' and crime == 'Overall':
        temp = df[(df['YEAR'] == year) & (df['DISTRICT'] == district)].groupby('YEAR').sum()
    if year != 'Overall' and district == 'Overall' and crime != 'Overall':
        temp = df[df['YEAR'] == year].groupby('DISTRICT').sum()[[crime]]
    if year != 'Overall' and district != 'Overall' and crime != 'Overall':
        temp = df[(df['YEAR'] == year) & (df['DISTRICT'] == district)].groupby('YEAR').sum()[crime]
    return temp

def fetch_year_wise(df,year,crime):
    if year == 'Overall' and crime=='Overall':
        temp = df.groupby('YEAR').sum()
    elif year=='Overall' and crime!='Overall':
        temp = df.groupby('YEAR').sum()[[crime]]
    elif year!='Overall' and crime == 'Overall':
        temp = df[df['YEAR']==year].groupby('YEAR').sum()
    else:
        temp = df[df['YEAR']==year].groupby('YEAR').sum()[[crime]]
    return  temp
def crimes_over_year(df):
    Year_wise = df.groupby('YEAR').sum().reset_index()
    return Year_wise
def crimes_by_states(df):
    state_wise = df.groupby('STATE_UT').sum().reset_index()
    return state_wise
def crimes_by_districts(df,crimes):
    district_wise = df.groupby('DISTRICT').sum().reset_index().drop(columns=['YEAR']).sort_values(crimes, ascending=False)
    return  district_wise.head(10)