import streamlit as st


def check_login():
    if 'login' in st.session_state:
        vals = [item['login'] for item in st.secrets['user']]
        vals.append('visitante')
        if st.session_state['login'] in vals:
            return True
        else:
            st.error('Login Incorreto.')
    st.text_input(key='login_input', label='Login')
    columns = st.columns(6)
    with columns[0]:
        if st.button('Logar'):
            st.session_state['login'] = st.session_state['login_input']
            st.experimental_rerun()
    with columns[1]:
        if st.button('Visitante'):
            st.session_state['login'] = 'visitante'
            st.experimental_rerun()
    return False


