import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import  preprosser
import helper
df = pd.read_csv('District_wise_crimes_committed_IPC_2001_2012.csv')
def preprocess():
    # droping useless columns
    df.drop(columns=['ATTEMPT_TO_MURDER', 'BURGLARY', 'COUNTERFIETING', 'CRUELTY_BY_HUSBAND_OR_HIS_RELATIVES',
                     'OTHER_IPC_CRIMES', 'DACOITY'], inplace=True)
    index = np.where(df['DISTRICT'] == 'TOTAL')
    df.drop(df['DISTRICT'].index[index], inplace=True)
    # dropping duplicates
    df.drop_duplicates(inplace=True)
    return (df)

df = preprocess()

st.sidebar.title("India Crime Analysis")
st.sidebar.image('https://www.deccanherald.com/sites/dh/files/styles/article_detail/public/articleimages/2020/11/07/shot-istock-912619-1604764634.jpg?itok=eh2kHaau')
user_menu = st.sidebar.radio(
    'select an option',
    ('State Wise Analysis','District Wise Analysis','Year Wise Analysis','Overall Analysis')
)
if(user_menu == 'State Wise Analysis'):
    state_list = helper.State_list(df)
    #state_df = helper.State(df)
    year_list = helper.Year_List(df)
    Crimes = helper.Crime_List(df)
    YEAR = st.sidebar.selectbox('Select Year', year_list)
    STATE = st.sidebar.selectbox('Select State',state_list)
    CRIME = st.sidebar.selectbox('Select Crime',Crimes)
    state_wise = helper.fetch_year_state(YEAR,STATE,CRIME,df)
    if YEAR == 'Overall' and STATE == 'Overall' and CRIME=='Overall':
        st.title((STATE.capitalize() +' Statistics').capitalize())
        st.table(state_wise)
    elif YEAR =='Overall' and STATE == 'Overall' and CRIME!='Overall':
        st.title((CRIME + " in all states (2002-2012)").capitalize())
        sort = st.sidebar.selectbox('sort', ['Overall', 'Ascending', 'Descending'])
        if sort=='Overall':
            st.table(state_wise)
        elif sort=='Ascending':
            st.table(state_wise.sort_values(CRIME,ascending=True))
        else:
            st.table(state_wise.sort_values(CRIME,ascending=False))
    elif YEAR =='Overall' and STATE != 'Overall' and CRIME=='Overall':
        st.title((STATE + ' Statistics').capitalize())
        st.table(state_wise)
    elif YEAR !='Overall' and STATE == 'Overall' and CRIME=='Overall':
        st.title((str(YEAR)+' Statistics').capitalize())
        st.table(state_wise)
    elif YEAR=='Overall' and STATE!='Overall' and CRIME!='Overall' :
        st.title((CRIME+' in '+STATE.capitalize()))
        sort = st.sidebar.selectbox('sort', ['Overall', 'Ascending', 'Descending'])
        if sort=='Overall':
            st.table(state_wise)
        elif sort=='Ascending':
            st.table(state_wise.sort_values(CRIME,ascending=True))
        else:
            st.table(state_wise.sort_values(CRIME,ascending=False))
    elif YEAR!='Overall' and STATE!='Overall' and CRIME=='Overall':
        st.title('Overall crime in '+STATE+" in "+str(YEAR))
        st.table(state_wise)
    elif YEAR!='Overall' and STATE=='Overall' and CRIME!='Overall':
        st.title((CRIME+' in all the states in'+str(YEAR)).capitalize())
        sort = st.sidebar.selectbox('sort', ['Overall', 'Ascending', 'Descending'])
        if sort == 'Overall':
            st.table(state_wise)
        elif sort == 'Ascending':
            st.table(state_wise.sort_values(CRIME, ascending=True))
        else:
            st.table(state_wise.sort_values(CRIME, ascending=False))
    elif YEAR!='Overall' and STATE!='Overall' and CRIME!='Overall':
        st.title((CRIME+' in '+STATE+' in '+str(YEAR)).capitalize())
        st.table(state_wise)

if(user_menu == 'District Wise Analysis'):
    #district_df = helper.District(df)
    #st.table(district_df)
    district_list = helper.Districs_List(df)
    year_list = helper.Year_List(df)
    Crimes = helper.Crime_List(df)
    YEAR = st.sidebar.selectbox('Select Year', year_list)
    DISTRICT = st.sidebar.selectbox("Select District",district_list)
    CRIME = st.sidebar.selectbox('Select Crime', Crimes)
    district_wise = helper.fetch_year_district(YEAR,DISTRICT,CRIME,df)
    if YEAR == 'Overall' and DISTRICT == 'Overall' and CRIME == 'Overall':
        st.title((DISTRICT.capitalize() + ' Statistics').capitalize())
        st.table(district_wise)
    elif YEAR == 'Overall' and DISTRICT == 'Overall' and CRIME != 'Overall':
        st.title((CRIME + " in all districts (2002-2012)").capitalize())
        sort = st.sidebar.selectbox('sort', ['Overall', 'Ascending', 'Descending'])
        if sort == 'Overall':
            st.table(district_wise)
        elif sort == 'Ascending':
            st.table(district_wise.sort_values(CRIME, ascending=True))
        else:
            st.table(district_wise.sort_values(CRIME, ascending=False))
    elif YEAR == 'Overall' and DISTRICT != 'Overall' and CRIME == 'Overall':
        st.title((DISTRICT + ' Statistics').capitalize())
        st.table(district_wise)
    elif YEAR != 'Overall' and DISTRICT == 'Overall' and CRIME == 'Overall':
        st.title((str(YEAR) + ' Statistics').capitalize())
        st.table(district_wise)
    elif YEAR == 'Overall' and DISTRICT != 'Overall' and CRIME != 'Overall':
        st.title((CRIME + ' in ' + DISTRICT.capitalize()))
        sort = st.sidebar.selectbox('sort', ['Overall', 'Ascending', 'Descending'])
        if sort == 'Overall':
            st.table(district_wise)
        elif sort == 'Ascending':
            st.table(district_wise.sort_values(CRIME, ascending=True))
        else:
            st.table(district_wise.sort_values(CRIME, ascending=False))
    elif YEAR != 'Overall' and DISTRICT != 'Overall' and CRIME == 'Overall':
        st.title('Overall crime in ' + DISTRICT + " in " + str(YEAR))
        st.table(district_wise)
    elif YEAR != 'Overall' and DISTRICT == 'Overall' and CRIME != 'Overall':
        st.title((CRIME + ' in all the districts in ' + str(YEAR)).capitalize())
        sort = st.sidebar.selectbox('sort', ['Overall', 'Ascending', 'Descending'])
        if sort == 'Overall':
            st.table(district_wise)
        elif sort == 'Ascending':
            st.table(district_wise.sort_values(CRIME, ascending=True))
        else:
            st.table(district_wise.sort_values(CRIME, ascending=False))
    elif YEAR != 'Overall' and DISTRICT != 'Overall' and CRIME != 'Overall':
        st.title((CRIME + ' in ' + DISTRICT + ' in ' + str(YEAR)).capitalize())
        st.table(district_wise)

if(user_menu == 'Year Wise Analysis'):
    #year_df = helper.Year(df)
    #st.table(year_df)
    year_list = helper.Year_List(df)
    Crimes = helper.Crime_List(df)
    YEAR = st.sidebar.selectbox('Select Year',year_list)
    CRIME = st.sidebar.selectbox('Select Crime', Crimes)
    year_wise = helper.fetch_year_wise(df,YEAR,CRIME)
    if(YEAR == 'Overall' and CRIME =='Overall'):
        st.title(CRIME + ' Statistics')
        st.table(year_wise)
    elif(YEAR == 'Overall' and CRIME !='Overall'):
        st.title(CRIME +' over the year' )
        sort = st.sidebar.selectbox('Sort',['Overall', 'Ascending', 'Descending'])
        if sort == 'Overall':
            st.table(year_wise)
        if sort == 'Ascending':
             st.table(year_wise.sort_values(CRIME,ascending=True))
        elif sort == 'Descending':
            st.table(year_wise.sort_values(CRIME, ascending=False))
    elif(YEAR != 'Overall' and CRIME == 'Overall'):
        st.title('Crimes' + ' in '+str(YEAR))
        st.table(year_wise)
    elif(YEAR != 'Overall' and CRIME != 'Overall'):
        st.title(CRIME + ' in '+str(YEAR))
        st.table(year_wise)


if(user_menu == 'Overall Analysis'):
    Crimes = helper.Crime_List(df)
    Crimes.pop(0)
    CRIME = st.sidebar.selectbox('Select Crime', Crimes)

    crime_over_year = helper.crimes_over_year(df)
    fig = px.line(crime_over_year, x="YEAR", y=CRIME ,title=('{} In India Over The Year'.format(CRIME)).capitalize())
    fig.update_layout(autosize=False,width=800,height=500)
    st.plotly_chart(fig)

    state_wise = helper.crimes_by_states(df)
    fig = px.bar(state_wise.sort_values(CRIME, ascending=False), x="STATE_UT", y=CRIME,title='ranking of states on the basis of {}'.format(CRIME).capitalize())
    fig.update_layout(autosize=False, width=800, height=500)
    st.plotly_chart(fig)

    crime_by_district = helper.crimes_by_districts(df,CRIME)
    fig = px.bar(crime_by_district,x='DISTRICT',y=CRIME,title='Top ten districts on the basis of {}'.format(CRIME).capitalize())
    fig.update_layout(autosize=False, width=800, height=500)
    st.plotly_chart(fig)

    fig = px.pie(state_wise, values=CRIME, names='STATE_UT', title="Percentage of {} in Diff-2 States".format(CRIME).capitalize())
    fig.update_layout(autosize=False, width=900, height=500)
    st.plotly_chart(fig)

    fig,ax = plt.subplots(figsize=(20, 20))
    ax = sns.heatmap(df.pivot_table(index='STATE_UT', columns='YEAR', values=CRIME, aggfunc='sum'), annot=True)
    st.pyplot(fig)