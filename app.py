import streamlit as st
# Import Views dari folder views
from views.home import show_home
from views.calculator import show_calculator
from views.about import show_about
from views.prevention import show_prevention

# --- KONFIGURASI HALAMAN UTAMA ---
st.set_page_config(
    page_title="ProstataCheck",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- FUNGSI LOAD CSS ---
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"File {file_name} tidak ditemukan. Pastikan struktur folder benar.")

local_css("assets/style.css")

# --- MANAJEMEN NAVIGASI ---
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

# --- ROUTING UTAMA ---
# Mengarahkan user ke file view yang sesuai
if st.session_state['page'] == 'home':
    show_home()
elif st.session_state['page'] == 'calculator':
    show_calculator()
elif st.session_state['page'] == 'about':
    show_about()
elif st.session_state['page'] == 'prevention':
    show_prevention()