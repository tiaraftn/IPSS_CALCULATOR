import streamlit as st

def show_home():
    # Header
    st.markdown("""
        <div class="header-container">
            <div class="big-icon">🩺</div>
            <h1 class="app-title">ProstataCheck</h1>
        </div>
    """, unsafe_allow_html=True)

    # Deskripsi
    st.markdown("""
        <div class="description-card">
            <div class="desc-title">
                Selamat datang di ProstataCheck.</div>
            <div class="desc-body">
                 Alat ini menggunakan metode IPSS (Skor Gejala Prostat Internasional), standar medis yang digunakan dokter di seluruh dunia untuk mendeteksi dini pembesaran prostat (BPH).
                <br><br>
                <i>Ketahui apakah gejala Bapak termasuk Ringan, Sedang, atau Berat, serta dapatkan saran perawatan yang tepat sekarang juga.</i>
            </div>
        </div>
    """, unsafe_allow_html=True)

   # 3. TOMBOL UTAMA (DI TENGAH)
    st.write("") # Spacer

    # --- PERBAIKAN DI SINI ---
    # Menggunakan rasio [1, 2, 1] 
    # Artinya: 25% Kiri Kosong - 50% Tombol Tengah - 25% Kanan Kosong
    # Ini menjamin tombol berada PERSIS di tengah garis lurus dengan footer.
    col_kiri, col_tombol, col_kanan = st.columns([1, 2, 1])

    with col_tombol:
        if st.button("📝   MULAI PENGECEKAN KESEHATAN (IPSS)"):
            st.session_state['page'] = 'calculator'
            st.rerun()
    # -------------------------
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # 4. TOMBOL INFO & PENCEGAHAN
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ℹ️  Tentang Penyakit Benign Prostatic Hyperplasia (BPH)"):
            st.session_state['page'] = 'about'
            st.rerun()
            
    with col2:
        if st.button("🛡️  Tips Pencegahan\n(Gaya Hidup Sehat)"):
            st.session_state['page'] = 'prevention'
            st.rerun()

    # Footer
    st.markdown("""
        <div style="text-align:center; margin-top:40px; color:#64748b; font-size:0.8rem;">
            Medical Disclaimer: Aplikasi ini adalah alat skrining awal
        </div>
    """, unsafe_allow_html=True)