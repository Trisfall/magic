import streamlit as st


def check_login():
    if 'login' in st.session_state:
        if st.session_state['login'] in ['LJWYX2', 'visitante', 'Rod27']:
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


