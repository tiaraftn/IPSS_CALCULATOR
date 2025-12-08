import streamlit as st

def show_about():
    # --- HEADER ---
    st.markdown('<div class="header-container"><h2 class="app-title">Tentang BPH</h2></div>', unsafe_allow_html=True)

    # --- KONTEN UTAMA (ANIMASI FADE IN) ---
    
    # 1. KARTU DEFINISI (Apa itu BPH?)
    st.markdown("""
        <div style="
        background-color: #1e293b; 
        border-radius: 15px; 
        padding: 30px; 
        border-left: 6px solid #38bdf8;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        animation: fadeIn 0.8s ease-out;
        margin-bottom: 25px;">
        
        <h3 style="color: #38bdf8; margin-bottom: 15px; display: flex; align-items: center; gap: 10px;">
            🔍 Apa itu BPH?
        </h3>
        <p style="font-size: 1.1rem; line-height: 1.8; color: #e2e8f0; text-align: justify;">
            <strong style="color: #f1f5f9;">BPH (Benign Prostatic Hyperplasia)</strong> adalah kondisi pembesaran kelenjar prostat yang 
            bersifat <span style="background-color: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 2px 8px; border-radius: 4px;">jinak (bukan kanker)</span> 
            dan sangat umum terjadi pada pria seiring bertambahnya usia.
            <br><br>
            Kondisi ini terjadi ketika ukuran prostat membesar dan <strong>menekan saluran kencing</strong> (uretra).
        </p>
        </div>
        """, unsafe_allow_html=True)

    # 2. VISUALISASI GEJALA (Akibatnya...)
    st.markdown("""
    <div style="margin-bottom: 15px; animation: fadeInUp 1s ease-out;">
        <p style="font-size: 1.2rem; color: #94a3b8; text-align: center; margin-bottom: 20px;">
            Gejala yang mungkin Anda rasakan:
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Menggunakan Columns untuk ikon gejala agar lebih menarik
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="
            background: #0f172a; border: 1px solid #334155; border-radius: 12px; padding: 20px; 
            text-align: center; height: 180px; animation: fadeInUp 1.2s ease-out;">
            <div style="font-size: 3rem; margin-bottom: 10px;">🚿</div>
            <div style="font-weight: bold; color: #38bdf8; margin-bottom: 5px;">Aliran Lemah</div>
            <div style="font-size: 0.9rem; color: #cbd5e1;">Pancaran air seni tidak kuat atau terputus-putus.</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="
            background: #0f172a; border: 1px solid #334155; border-radius: 12px; padding: 20px; 
            text-align: center; height: 180px; animation: fadeInUp 1.4s ease-out;">
            <div style="font-size: 3rem; margin-bottom: 10px;">💧</div>
            <div style="font-weight: bold; color: #38bdf8; margin-bottom: 5px;">Rasa Tidak Tuntas</div>
            <div style="font-size: 0.9rem; color: #cbd5e1;">Merasa masih ada sisa urin setelah selesai buang air kecil.</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="
            background: #0f172a; border: 1px solid #334155; border-radius: 12px; padding: 20px; 
            text-align: center; height: 180px; animation: fadeInUp 1.6s ease-out;">
            <div style="font-size: 3rem; margin-bottom: 10px;">🌙</div>
            <div style="font-weight: bold; color: #38bdf8; margin-bottom: 5px;">Sering Bangun Malam</div>
            <div style="font-size: 0.9rem; color: #cbd5e1;">Tidur terganggu karena harus bolak-balik ke kamar mandi.</div>
        </div>
        """, unsafe_allow_html=True)

    # 3. PESAN PENUTUP (Call to Action)
    st.markdown("""
    <div style="
        margin-top: 30px;
        background-color: rgba(245, 158, 11, 0.1); 
        border-left: 5px solid #f59e0b;
        border-radius: 10px;
        padding: 20px;
        animation: fadeInUp 1.8s ease-out;">
        <p style="font-size: 1.05rem; line-height: 1.6; color: #f1f5f9; margin: 0;">
            💡 <strong>Catatan Penting:</strong> Meskipun kondisi ini wajar terjadi karena faktor usia, 
            gejalanya perlu dikenali dan dipantau agar tidak mengganggu kenyamanan hidup Anda.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --- TOMBOL KEMBALI ---
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        if st.button("⬅️ Kembali ke Menu Utama", use_container_width=True):
            st.session_state['page'] = 'home'
            st.rerun()