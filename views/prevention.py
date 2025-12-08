import streamlit as st

def show_prevention():
    # --- HEADER ---
    st.markdown('<div class="header-container"><h2 class="app-title">Tips Gaya Hidup Sehat</h2></div>', unsafe_allow_html=True)

    # --- INTRO SECTION ---
    # Background putih dengan aksen hijau
    st.markdown("""
    <div style="
    background-color: #ffffff; 
    border-left: 6px solid #22c55e;
    border: 1px solid #e2e8f0;
    border-radius: 15px; 
    padding: 25px; 
    margin-bottom: 30px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    animation: fadeIn 0.8s ease-out;">
    
    <h3 style="color: #15803d; margin-bottom: 10px;">🛡️ Mencegah Lebih Baik</h3>
    <p style="font-size: 1.1rem; line-height: 1.6; color: #334155; text-align: justify; margin: 0;">
        Meskipun pembesaran prostat seringkali berkaitan dengan faktor usia, tips ini diambil dari 
        <strong>pedoman gaya hidup (lifestyle advice)</strong> untuk menjaga agar gejala tidak muncul atau tidak bertambah parah.
        Berikut adalah kebiasaan sederhana yang bisa Bapak lakukan sehari-hari.
    </p>
    </div>
    """, unsafe_allow_html=True)

    # --- DATA TIPS ---
    tips_data = [
        {
            "icon": "🌶️",
            "title": "1. Kurangi Pedas & Asin",
            "desc": "Cobalah untuk membatasi konsumsi makanan yang terlalu pedas dan mengandung banyak garam, karena dapat memengaruhi kelancaran buang air kecil.",
            "color": "#dc2626", # Merah
            "bg_icon": "#fef2f2"
        },
        {
            "icon": "☕",
            "title": "2. Hindari Kopi & Alkohol Malam",
            "desc": "Minuman berkafein (kopi, cokelat) dan alkohol dapat mengiritasi kandung kemih. Hindari konsumsi ini terutama setelah makan malam.",
            "color": "#ea580c", # Oranye
            "bg_icon": "#fff7ed"
        },
        {
            "icon": "💧",
            "title": "3. Atur Jadwal Minum",
            "desc": "Minum air putih itu sehat, tetapi cobalah untuk tidak banyak minum tepat sebelum tidur agar Bapak tidak perlu sering terbangun di malam hari.",
            "color": "#2563eb", # Biru
            "bg_icon": "#eff6ff"
        },
        {
            "icon": "⏱️",
            "title": "4. Jangan Menahan Kencing",
            "desc": "Jangan biasakan menahan buang air kecil terlalu lama. Jika rasa ingin pipis muncul, segera keluarkan agar kandung kemih tidak terbebani.",
            "color": "#ca8a04", # Kuning Emas
            "bg_icon": "#fefce8"
        },
        {
            "icon": "💊",
            "title": "5. Hati-Hati Obat Flu",
            "desc": "Perhatikan obat flu yang mengandung <em>fenilpropanolamin</em>, karena bisa membuat buang air kecil menjadi lebih sulit saat sedang pilek.",
            "color": "#9333ea", # Ungu
            "bg_icon": "#faf5ff"
        },
        {
            "icon": "👨‍⚕️",
            "title": "6. Cek Rutin Usia 50+",
            "desc": "Jika Bapak sudah berusia di atas 50 tahun, sangat disarankan untuk melakukan pemeriksaan prostat berkala ke dokter, meskipun belum ada gejala berat.",
            "color": "#16a34a", # Hijau
            "bg_icon": "#f0fdf4"
        }
    ]

    # --- GRID LAYOUT LOOP ---
    for i in range(0, len(tips_data), 2):
        col1, col2 = st.columns(2)
        
        # Helper function untuk membuat HTML kartu
        def make_card(item):
            return f"""
    <div style="
    background-color: #ffffff; 
    border: 1px solid #e2e8f0; 
    border-radius: 15px; 
    padding: 25px; 
    height: 100%; 
    margin-bottom: 20px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    animation: fadeInUp 1s ease-out;
    transition: transform 0.3s;">
    
    <div style="
        font-size: 2.5rem; 
        margin-bottom: 15px; 
        background-color: {item['bg_icon']}; 
        width: 70px; height: 70px; 
        display: flex; align-items: center; justify-content: center; 
        border-radius: 50%;">
        {item['icon']}
    </div>
    
    <h3 style="color: {item['color']}; font-size: 1.15rem; margin-bottom: 10px; font-weight: 700;">
        {item['title']}
    </h3>
    <p style="color: #475569; font-size: 1rem; line-height: 1.6;">
        {item['desc']}
    </p>
    </div>
    """

        # Kolom Kiri
        with col1:
            st.markdown(make_card(tips_data[i]), unsafe_allow_html=True)

        # Kolom Kanan
        with col2:
            if i + 1 < len(tips_data):
                st.markdown(make_card(tips_data[i+1]), unsafe_allow_html=True)

    # --- TOMBOL KEMBALI ---
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        if st.button("⬅️ Kembali ke Menu Utama", type="primary", use_container_width=True):
            st.session_state['page'] = 'home'
            st.rerun()