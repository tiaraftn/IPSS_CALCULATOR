import streamlit as st

def show_prevention():
    # --- HEADER ---
    st.markdown('<div class="header-container"><h2 class="app-title">Tips Gaya Hidup Sehat</h2></div>', unsafe_allow_html=True)

    # --- INTRO SECTION ---
    st.markdown("""
    <div style="
    background-color: #1e293b; 
    border-left: 6px solid #22c55e;
    border-radius: 15px; 
    padding: 25px; 
    margin-bottom: 30px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    animation: fadeIn 0.8s ease-out;">
    
    <h3 style="color: #22c55e; margin-bottom: 10px;">🛡️ Mencegah Lebih Baik</h3>
    <p style="font-size: 1.1rem; line-height: 1.6; color: #e2e8f0; text-align: justify; margin: 0;">
        Meskipun pembesaran prostat seringkali berkaitan dengan faktor usia, tips ini diambil dari 
        <strong>pedoman gaya hidup (lifestyle advice)</strong> untuk menjaga agar gejala tidak muncul atau tidak bertambah parah.
        Berikut adalah kebiasaan sederhana yang bisa Bapak lakukan sehari-hari.
    </p>
    </div>
    """, unsafe_allow_html=True)

    # --- DATA TIPS (List of Dictionary) ---
    # Kita buat data terstruktur agar mudah di-looping dan rapi
    tips_data = [
        {
            "icon": "🌶️",
            "title": "1. Kurangi Pedas & Asin",
            "desc": "Cobalah untuk membatasi konsumsi makanan yang terlalu pedas dan mengandung banyak garam, karena dapat memengaruhi kelancaran buang air kecil.",
            "color": "#ef4444" # Merah
        },
        {
            "icon": "☕",
            "title": "2. Hindari Kopi & Alkohol Malam",
            "desc": "Minuman berkafein (kopi, cokelat) dan alkohol dapat mengiritasi kandung kemih. Hindari konsumsi ini terutama setelah makan malam.",
            "color": "#f97316" # Oranye
        },
        {
            "icon": "💧",
            "title": "3. Atur Jadwal Minum",
            "desc": "Minum air putih itu sehat, tetapi cobalah untuk tidak banyak minum tepat sebelum tidur agar Bapak tidak perlu sering terbangun di malam hari.",
            "color": "#3b82f6" # Biru
        },
        {
            "icon": "⏱️",
            "title": "4. Jangan Menahan Kencing",
            "desc": "Jangan biasakan menahan buang air kecil terlalu lama. Jika rasa ingin pipis muncul, segera keluarkan agar kandung kemih tidak terbebani.",
            "color": "#eab308" # Kuning
        },
        {
            "icon": "💊",
            "title": "5. Hati-Hati Obat Flu",
            "desc": "Perhatikan obat flu yang mengandung <em>fenilpropanolamin</em>, karena bisa membuat buang air kecil menjadi lebih sulit saat sedang pilek.",
            "color": "#a855f7" # Ungu
        },
        {
            "icon": "👨‍⚕️",
            "title": "6. Cek Rutin Usia 50+",
            "desc": "Jika Bapak sudah berusia di atas 50 tahun, sangat disarankan untuk melakukan pemeriksaan prostat berkala ke dokter, meskipun belum ada gejala berat.",
            "color": "#22c55e" # Hijau
        }
    ]

    # --- GRID LAYOUT LOOP ---
    # Membuat layout 2 kolom per baris
    for i in range(0, len(tips_data), 2):
        col1, col2 = st.columns(2)
        
        # Kolom Kiri
        with col1:
            item = tips_data[i]
            st.markdown(f"""
<div style="
    background-color: #0f172a; 
    border: 1px solid #334155; 
    border-radius: 15px; 
    padding: 25px; 
    height: 100%; 
    margin-bottom: 20px;
    animation: fadeInUp 1s ease-out;
    transition: transform 0.3s;">
    <div style="font-size: 3rem; margin-bottom: 15px;">{item['icon']}</div>
    <h3 style="color: {item['color']}; font-size: 1.2rem; margin-bottom: 10px;">{item['title']}</h3>
    <p style="color: #cbd5e1; font-size: 1rem; line-height: 1.5;">{item['desc']}</p>
</div>
""", unsafe_allow_html=True)

        # Kolom Kanan (Cek apakah data masih ada)
        with col2:
            if i + 1 < len(tips_data):
                item = tips_data[i+1]
                st.markdown(f"""
<div style="
    background-color: #0f172a; 
    border: 1px solid #334155; 
    border-radius: 15px; 
    padding: 25px; 
    height: 100%; 
    margin-bottom: 20px;
    animation: fadeInUp 1.2s ease-out;">
    <div style="font-size: 3rem; margin-bottom: 15px;">{item['icon']}</div>
    <h3 style="color: {item['color']}; font-size: 1.2rem; margin-bottom: 10px;">{item['title']}</h3>
    <p style="color: #cbd5e1; font-size: 1rem; line-height: 1.5;">{item['desc']}</p>
</div>
""", unsafe_allow_html=True)

    # --- TOMBOL KEMBALI ---
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        if st.button("⬅️ Kembali ke Menu Utama", use_container_width=True):
            st.session_state['page'] = 'home'
            st.rerun()