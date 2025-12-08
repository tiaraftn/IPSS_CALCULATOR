import streamlit as st

def show_about():
    # --- HEADER ---
    st.markdown('<div class="header-container"><h2 class="app-title">Tentang BPH</h2></div>', unsafe_allow_html=True)

    # --- KONTEN UTAMA (ANIMASI FADE IN) ---
    
    # 1. KARTU DEFINISI (Apa itu BPH?) - LIGHT THEME
    # Background Putih, Teks Gelap
    st.markdown("""
    <div style="
    background-color: #ffffff; 
    border-radius: 15px; 
    padding: 30px; 
    border: 1px solid #e2e8f0;
    border-left: 6px solid #0284c7;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    animation: fadeIn 0.8s ease-out;
    margin-bottom: 25px;">
    
    <h3 style="color: #0284c7; margin-bottom: 15px; display: flex; align-items: center; gap: 10px;">
        🔍 Apa itu BPH?
    </h3>
    <p style="font-size: 1.1rem; line-height: 1.8; color: #334155; text-align: justify;">
        <strong style="color: #1e293b;">BPH (Benign Prostatic Hyperplasia)</strong> adalah kondisi pembesaran kelenjar prostat yang 
        bersifat <span style="background-color: #dcfce7; color: #166534; padding: 2px 8px; border-radius: 4px; font-weight: 600;">jinak (bukan kanker)</span> 
        dan sangat umum terjadi pada pria seiring bertambahnya usia.
        <br><br>
        Kondisi ini terjadi ketika ukuran prostat membesar dan <strong>menekan saluran kencing</strong> (uretra).
    </p>
    </div>
    """, unsafe_allow_html=True)

    # 2. VISUALISASI GEJALA (Akibatnya...)
    st.markdown("""
    <div style="margin-bottom: 15px; animation: fadeInUp 1s ease-out;">
    <p style="font-size: 1.2rem; color: #64748b; text-align: center; margin-bottom: 20px; font-weight: 500;">
        Gejala yang mungkin Anda rasakan:
    </p>
    </div>
    """, unsafe_allow_html=True)

    # Menggunakan Columns untuk ikon gejala
    col1, col2, col3 = st.columns(3)

    # Style Kartu Gejala: Putih dengan border tipis & shadow
    card_style = """
        background: #ffffff; 
        border: 1px solid #e2e8f0; 
        border-radius: 12px; 
        padding: 20px; 
        text-align: center; 
        height: 100%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        transition: transform 0.2s;
    """

    with col1:
        st.markdown(f"""
    <div style="{card_style} animation: fadeInUp 1.2s ease-out;">
    <div style="font-size: 3rem; margin-bottom: 10px;">🚿</div>
    <div style="font-weight: bold; color: #0284c7; margin-bottom: 5px; font-size: 1.1rem;">Aliran Lemah</div>
    <div style="font-size: 0.95rem; color: #475569;">Pancaran air seni tidak kuat atau terputus-putus.</div>
    </div>
    """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
    <div style="{card_style} animation: fadeInUp 1.4s ease-out;">
    <div style="font-size: 3rem; margin-bottom: 10px;">💧</div>
    <div style="font-weight: bold; color: #0284c7; margin-bottom: 5px; font-size: 1.1rem;">Rasa Tidak Tuntas</div>
    <div style="font-size: 0.95rem; color: #475569;">Merasa masih ada sisa urin setelah selesai buang air kecil.</div>
    </div>
    """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
    <div style="{card_style} animation: fadeInUp 1.6s ease-out;">
    <div style="font-size: 3rem; margin-bottom: 10px;">🌙</div>
    <div style="font-weight: bold; color: #0284c7; margin-bottom: 5px; font-size: 1.1rem;">Sering Bangun Malam</div>
    <div style="font-size: 0.95rem; color: #475569;">Tidur terganggu karena harus bolak-balik ke kamar mandi.</div>
    </div>
    """, unsafe_allow_html=True)

    # 3. PESAN PENUTUP (Call to Action)
    # Background Kuning Muda
    st.markdown("""
    <div style="
    margin-top: 30px;
    background-color: #fff7ed; 
    border-left: 5px solid #f59e0b;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    animation: fadeInUp 1.8s ease-out;">
    <p style="font-size: 1.05rem; line-height: 1.6; color: #7c2d12; margin: 0;">
        💡 <strong>Catatan Penting:</strong> Meskipun kondisi ini wajar terjadi karena faktor usia, 
        gejalanya perlu dikenali dan dipantau agar tidak mengganggu kenyamanan hidup Anda.
    </p>
    </div>
    """, unsafe_allow_html=True)

    # --- TOMBOL KEMBALI ---
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        # Type Primary agar warna biru/putih mengikuti tema
        if st.button("⬅️ Kembali ke Menu Utama", type="primary", use_container_width=True):
            st.session_state['page'] = 'home'
            st.rerun()