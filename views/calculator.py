import streamlit as st
from data.ipss_content import PERTANYAAN_IPSS, PERTANYAAN_QOL, classify_score, get_qol_message, get_detailed_advice

def show_calculator():
    # --- HEADER ---
    st.markdown('<div class="header-container"><h2 class="app-title" style="font-size: 2rem;">Kalkulator I-PSS</h2></div>', unsafe_allow_html=True)
    
    all_questions = PERTANYAAN_IPSS + [PERTANYAAN_QOL]
    total_steps = len(all_questions)

    # --- INIT STATE ---
    for q in all_questions:
        if q["id"] not in st.session_state:
            st.session_state[q["id"]] = None
    
    if 'current_step' not in st.session_state:
        st.session_state['current_step'] = 0

    current_step = st.session_state['current_step']
    progress_val = (current_step) / total_steps
    
    # Progress Bar (Hanya tampil saat mengisi)
    if current_step < total_steps:
        st.write(f"**Pertanyaan {current_step + 1} dari {total_steps}**")
        st.progress(progress_val)
        st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)

    # ============================================================
    # MODE 1: TAMPILAN PERTANYAAN (WIZARD)
    # ============================================================
    if current_step < total_steps:
        q_data = all_questions[current_step]
        widget_key = f"widget_{q_data['id']}"
        storage_key = q_data["id"]

        if current_step == 7:
            st.markdown("""
        <div style="text-align: center; margin: 0 0 30px 0;">
        <span style="background: #0f172a; padding: 0 15px; font-family: 'Merriweather', serif; font-size: 1.3rem; color: #f59e0b;">
        Bagian Akhir: Kualitas Hidup
        </span>
        <hr style="border-color: #f59e0b; margin-top: -12px; opacity: 0.3;">
        </div>
        """, unsafe_allow_html=True)

        border_color = "#f59e0b" if current_step == 7 else "#38bdf8"
        
        with st.container():
            st.markdown(f"""
        <div class="question-card" style="border-left-color: {border_color}; animation: fadeIn 0.5s ease-out;">
        <div class="q-header">
        <div class="q-icon" style="color: {border_color if current_step==7 else 'inherit'};">{q_data['icon']}</div>
        <div>
        <div style="font-size: 0.9rem; color: {border_color}; text-transform: uppercase; letter-spacing: 1px;">
        {'PERTANYAAN TERAKHIR' if current_step == 7 else f'PERTANYAAN {current_step+1}'}
        </div>
        <div class="q-title">{q_data['title']}</div>
        </div>
        </div>
        <p style="font-size:1.2rem; color:#e2e8f0; line-height: 1.6; font-weight: 500;">{q_data['detail']}</p>
        {'<p style="font-size:0.95rem; color:#94a3b8; margin-top:5px; font-style:italic;">ℹ️ ' + q_data['note'] + '</p>' if q_data.get('note') else ''}
        </div>
        """, unsafe_allow_html=True)

            saved_val = st.session_state[storage_key]
            try:
                default_idx = q_data["scoring"].index(saved_val) if saved_val else None
            except ValueError:
                default_idx = None

            st.markdown("<div style='margin-left: 10px;'>", unsafe_allow_html=True)
            selection = st.radio(
                f"Jawaban {q_data['title']}",
                options=q_data["scoring"],
                key=widget_key,
                index=default_idx,
                label_visibility="collapsed"
            )
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("<div style='margin-bottom: 40px;'></div>", unsafe_allow_html=True)

        col_back, col_next = st.columns([1, 1])
        with col_back:
            if current_step > 0:
                if st.button("⬅️ Sebelumnya"):
                    st.session_state[storage_key] = selection
                    st.session_state['current_step'] -= 1
                    st.rerun()
            else:
                if st.button("⬅️ Batal"):
                    st.session_state['page'] = 'home'
                    st.rerun()

        with col_next:
            btn_text = "Lihat Hasil Analisa ✅" if current_step == 7 else "Selanjutnya ➡️"
            btn_type = "primary"
            
            if st.button(btn_text, type=btn_type, use_container_width=True):
                if selection is None:
                    st.toast("⚠️ Mohon pilih jawaban terlebih dahulu!", icon="⚠️")
                else:
                    st.session_state[storage_key] = selection
                    st.session_state['current_step'] += 1
                    st.rerun()

    # ============================================================
    # MODE 2: TAMPILAN HASIL (RESULT)
    # ============================================================
    else:
        # 1. Hitung Skor IPSS
        total_score = 0
        for i in range(7):
            q_id = all_questions[i]["id"]
            val = st.session_state[q_id]
            if val is not None:
                score = all_questions[i]["scoring"].index(val)
                total_score += score
            
        # 2. Ambil QoL
        qol_id = all_questions[7]["id"]
        qol_val = st.session_state[qol_id] # Ini teks jawaban (misal: "Senang (Pleased)")
        qol_score = all_questions[7]["scoring"].index(qol_val) if qol_val else 0
        
        # 3. Klasifikasi & Rekomendasi
        title, msg, type_color = classify_score(total_score)
        qol_note = get_qol_message(total_score, qol_score)
        detailed_advice = get_detailed_advice(total_score) # Ambil teks solusi panjang
        
        # Tentukan Warna Border
        border_hex = '#22c55e'
        if type_color == 'warning': border_hex = '#f59e0b'
        elif type_color == 'error': border_hex = '#ef4444'

        st.progress(100)
        st.markdown("<div id='result-anchor'></div>", unsafe_allow_html=True)

        # --- A. HEADER TERIMA KASIH ---
        st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <h2 style="color: #38bdf8;">✅ Terima Kasih sudah mengisi</h2>
            <p style="color: #94a3b8;">Berikut adalah hasil analisa kesehatan prostat Bapak:</p>
        </div>
        """, unsafe_allow_html=True)
        
        # --- B. HASIL IPSS ---
        st.markdown(f"""
        <div style="
        background-color: #1e293b; 
        border: 2px solid {border_hex}; 
        border-radius: 20px; 
        padding: 30px; 
        text-align: center; 
        margin-bottom: 20px;
        animation: fadeIn 0.8s ease-out;
        box-shadow: 0 0 30px rgba(0,0,0,0.3);">

        <h3 style="color: #94a3b8; margin-bottom: 10px; letter-spacing: 1px; font-size: 1rem;">SKOR IPSS BAPAK ADALAH</h3>
        <div style="font-size: 5rem; font-weight: 800; color: #f1f5f9; line-height: 1;">
        {total_score} <span style="font-size: 1.5rem; color: #64748b;">/ 35</span>
        </div>

        <hr style="border-color: #334155; margin: 20px 0;">

        <h2 style="color: {border_hex}; text-transform: uppercase;">
        {title}
        </h2>
        </div>
        """, unsafe_allow_html=True)

        # --- C. HASIL QUALITY OF LIFE (QoL) ---
        st.markdown(f"""
        <div style="
        background-color: #1e293b;
        border-left: 5px solid #f59e0b;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        animation: fadeInUp 1s ease-out;">
        <p style="color: #94a3b8; font-size: 0.9rem; margin-bottom: 5px;">Quality of Life (Kualitas Hidup):</p>
        <p style="font-size: 1.3rem; font-weight: 600; color: #f59e0b; margin: 0;">
        "{qol_val}"
        </p>
        </div>
        """, unsafe_allow_html=True)

        # --- D. CATATAN QOL (Jika Ada) ---
        if qol_note:
            st.markdown(f"""
        <div style="
        margin-bottom: 20px;
        background-color: rgba(59, 130, 246, 0.1); 
        border-left: 5px solid #3b82f6;
        padding: 20px;
        border-radius: 8px;
        animation: fadeInUp 1.2s ease-out;
        color: #e2e8f0;
        font-size: 1rem;
        line-height: 1.6;">
        {qol_note}
        </div>
        """, unsafe_allow_html=True)

        # --- E. SOLUSI / HAL YANG HARUS DILAKUKAN ---
        st.markdown(f"""
        <div style="
        background-color: #0f172a; 
        border: 1px solid {border_hex}; 
        border-radius: 15px; 
        padding: 25px; 
        margin-top: 10px;
        animation: fadeInUp 1.4s ease-out;">
        <h3 style="color: {border_hex}; margin-bottom: 15px; display: flex; align-items: center; gap: 10px;">
        💡 Hal yang Harus Bapak Lakukan Sekarang
        </h3>
        <hr style="border-color: #334155; margin-bottom: 15px;">
        <div style="color: #e2e8f0; font-size: 1.05rem;">
        {detailed_advice}
        </div>
        </div>
        """, unsafe_allow_html=True)

        # --- TOMBOL RESTART ---
        st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
        col_res1, col_res2, col_res3 = st.columns([1, 2, 1])
        with col_res2:
            if st.button("🔄 Ulangi Pengecekan", use_container_width=True):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.session_state['page'] = 'home'
                st.rerun()