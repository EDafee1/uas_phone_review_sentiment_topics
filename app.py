import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df_pos = pd.read_csv('res_pos.csv')
df_neg = pd.read_csv('res_neg.csv')

st.set_page_config(page_title='Phone Review Topics', layout='wide')

st.title('Looking for a phone?')
st.header('Search phone by brand and see the positive and negative result', divider='violet')

brand = st.selectbox(
    'Brand',
    ('Samsung', 'Apple', 'Nokia'),
    index = None,
    placeholder = "Select Brand...")

def search():
    res_pos = df_pos[df_pos['Brand'] == brand]
    res_neg = df_neg[df_neg['Brand'] == brand]

    res_pos = res_pos['Result'].drop_duplicates()
    res_neg = res_neg['Result'].drop_duplicates()

    st.session_state.pos = res_pos
    st.session_state.neg = res_neg

    st.session_state.len_pos = len(res_pos)
    st.session_state.len_neg = len(res_neg)

    labels = ['Positive', 'Negative']
    values = [st.session_state.len_pos, st.session_state.len_neg]
    fig1, ax1 = plt.subplots()

st.button('Search', on_click=search)

col1, col_pos, col2, col3, col4, col_neg, col5 = st.columns([1,3,1,2,1,3,1])

if 'len_pos' not in st.session_state:
    st.session_state.len_pos = 1

if 'len_neg' not in st.session_state:
    st.session_state.len_neg = 1

labels = ['Positive', 'Negative']
values = [st.session_state.len_pos, st.session_state.len_neg]

fig1, ax1 = plt.subplots()
ax1.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'color':"w", 'fontsize':18}, 
        colors=['purple', 'crimson'])
ax1.axis('equal')
fig1.patch.set_alpha(0.0)
col3.pyplot(fig1)


try:
    col_pos.write('Positive Result')
    col_pos.dataframe(st.session_state.pos)
except:
    col_pos.write('No Data')

try:
    col_neg.write('Negative Result')
    col_neg.dataframe(st.session_state.neg)
except:
    col_neg.write('No Data')
