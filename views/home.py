import streamlit as st

def show_home():
    # 1. HEADER
    st.markdown("""
        <div class="header-container">
            <div class="big-icon">🩺</div>
            <h1 class="app-title">ProstataCheck</h1>
        </div>
    """, unsafe_allow_html=True)

    # 2. DESKRIPSI
    st.markdown("""
        <div class="description-card">
            <div class="desc-title">
                Selamat datang di ProstataCheck.
            </div>
            <div class="desc-body">
                Alat ini menggunakan kuesioner <b>I-PSS <i>(International Prostate Symptom Score)</i></b>, standar medis yang digunakan dokter di seluruh dunia untuk mendeteksi dini pembesaran prostat (BPH).
                <br><br>
                <i>Ketahui apakah gejala Bapak termasuk Ringan, Sedang, atau Berat, serta dapatkan saran perawatan yang tepat sekarang juga.</i>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 3. TOMBOL UTAMA (DI TENGAH)
    st.write("") # Spacer

    # Layout [1, 2, 1] agar tombol di tengah
    col_kiri, col_tombol, col_kanan = st.columns([1, 2, 1])

    with col_tombol:
        # Teks tombol dibuat agak panjang agar proporsional
        if st.button("📝   MULAI PENGECEKAN KESEHATAN (IPSS)"):
            st.session_state['page'] = 'calculator'
            st.rerun()
            
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # 4. TOMBOL INFO & PENCEGAHAN
    col1, col2 = st.columns(2)
    with col1:
        # Menggunakan \n agar baris baru rapi di HP
        if st.button("ℹ️  Tentang Penyakit"<i>"\nBenign Prostatic Hyperplasia (BPH)"</i>):
            st.session_state['page'] = 'about'
            st.rerun()
            
    with col2:
        if st.button("🛡️  Tips Pencegahan\n(Gaya Hidup Sehat)"):
            st.session_state['page'] = 'prevention'
            st.rerun()

    # Footer
    st.markdown("""
        <div style="text-align:center; margin-top:40px; color:#94a3b8; font-size:0.8rem;">
            Medical Disclaimer: Aplikasi ini adalah alat skrining awal
        </div>
    """, unsafe_allow_html=True)
