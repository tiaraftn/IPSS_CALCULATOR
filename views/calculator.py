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
    
    # Progress Bar
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

        # Divider Khusus QoL
        if current_step == 7:
            st.markdown("""
<div style="text-align: center; margin: 0 0 30px 0;">
<span style="background: #fff7ed; padding: 8px 20px; border-radius: 20px; font-family: 'Merriweather', serif; font-size: 1.1rem; color: #d97706; border: 1px solid #fed7aa;">
Bagian Akhir: Kualitas Hidup
</span>
</div>
""", unsafe_allow_html=True)

        # Warna Tema Terang
        border_color = "#f59e0b" if current_step == 7 else "#0284c7"
        icon_bg = "#fff7ed" if current_step == 7 else "#f0f9ff"
        
        with st.container():
            # KARTU PERTANYAAN (Light Theme & RATA KIRI)
            st.markdown(f"""
<div class="question-card" style="
background-color: #ffffff; 
border: 1px solid #e2e8f0;
border-left: 6px solid {border_color};
border-radius: 15px;
padding: 25px;
margin-bottom: 20px;
box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
animation: fadeIn 0.5s ease-out;">

<div class="q-header" style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
<div class="q-icon" style="
font-size: 2.5rem; 
background: {icon_bg}; 
width: 60px; height: 60px; 
display: flex; align-items: center; justify-content: center; 
border-radius: 50%;">
{q_data['icon']}
</div>
<div>
<div style="font-size: 0.85rem; color: {border_color}; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;">
{'PERTANYAAN TERAKHIR' if current_step == 7 else f'PERTANYAAN {current_step+1}'}
</div>
<div class="q-title" style="font-size: 1.25rem; font-weight: 700; color: #1e293b;">
{q_data['title']}
</div>
</div>
</div>

<p style="font-size:1.1rem; color:#334155; line-height: 1.6; font-weight: 500;">
{q_data['detail']}
</p>

{'<p style="font-size:0.9rem; color:#64748b; margin-top:5px; font-style:italic; background: #f8fafc; padding: 8px; border-radius: 6px;">ℹ️ ' + q_data['note'] + '</p>' if q_data.get('note') else ''}
</div>
""", unsafe_allow_html=True)

            # Logic Index Radio Button
            saved_val = st.session_state[storage_key]
            try:
                default_idx = q_data["scoring"].index(saved_val) if saved_val else None
            except ValueError:
                default_idx = None

            st.markdown("<div style='margin-left: 5px;'>", unsafe_allow_html=True)
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
            if st.button(btn_text, type="primary", use_container_width=True):
                if selection is None:
                    st.toast("⚠️ Mohon pilih jawaban terlebih dahulu!", icon="⚠️")
                else:
                    st.session_state[storage_key] = selection
                    st.session_state['current_step'] += 1
                    st.rerun()

    # ============================================================
    # MODE 2: TAMPILAN HASIL (RESULT) - LIGHT THEME
    # ============================================================
    else:
        # Hitung Skor
        total_score = 0
        for i in range(7):
            q_id = all_questions[i]["id"]
            val = st.session_state[q_id]
            if val is not None:
                score = all_questions[i]["scoring"].index(val)
                total_score += score
            
        qol_id = all_questions[7]["id"]
        qol_val = st.session_state[qol_id]
        qol_score = all_questions[7]["scoring"].index(qol_val) if qol_val else 0
        
        title, msg, type_color = classify_score(total_score)
        qol_note = get_qol_message(total_score, qol_score)
        detailed_advice = get_detailed_advice(total_score)
        
        # Warna Light Theme
        border_hex = '#16a34a' # Hijau
        if type_color == 'warning': border_hex = '#d97706' # Oranye
        elif type_color == 'error': border_hex = '#dc2626' # Merah

        st.progress(100)
        st.markdown("<div id='result-anchor'></div>", unsafe_allow_html=True)

        # --- A. HEADER TERIMA KASIH ---
        st.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
<h2 style="color: #0284c7; margin-bottom: 5px;">✅ Terima Kasih</h2>
<p style="color: #64748b; font-size: 1rem;">Berikut adalah hasil analisa kesehatan prostat Bapak:</p>
</div>
""", unsafe_allow_html=True)
        
        # --- B. HASIL IPSS ---
        st.markdown(f"""
<div style="
background-color: #ffffff; 
border: 2px solid {border_hex}; 
border-radius: 20px; 
padding: 30px; 
text-align: center; 
margin-bottom: 20px;
animation: fadeIn 0.8s ease-out;
box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);">

<h3 style="color: #64748b; margin-bottom: 10px; letter-spacing: 1px; font-size: 0.9rem; text-transform: uppercase;">Skor IPSS Bapak Adalah</h3>
<div style="font-size: 5rem; font-weight: 800; color: {border_hex}; line-height: 1;">
{total_score} <span style="font-size: 1.5rem; color: #94a3b8; font-weight: 500;">/ 35</span>
</div>

<hr style="border-top: 1px solid #e2e8f0; margin: 20px 0;">

<h2 style="color: #1e293b; text-transform: uppercase; font-size: 1.5rem; margin-bottom: 10px;">
{title}
</h2>
</div>
""", unsafe_allow_html=True)

        # --- C. HASIL QUALITY OF LIFE (QoL) ---
        st.markdown(f"""
<div style="
background-color: #ffffff;
border: 1px solid #e2e8f0;
border-left: 5px solid #d97706;
border-radius: 10px;
padding: 20px;
margin-bottom: 20px;
box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
animation: fadeInUp 1s ease-out;">
<p style="color: #64748b; font-size: 0.9rem; margin-bottom: 5px;">Quality of Life (Kualitas Hidup):</p>
<p style="font-size: 1.2rem; font-weight: 600; color: #d97706; margin: 0;">
"{qol_val}"
</p>
</div>
""", unsafe_allow_html=True)

        # --- D. CATATAN QOL ---
        if qol_note:
            st.markdown(f"""
<div style="
margin-bottom: 20px;
background-color: #eff6ff; 
border-left: 5px solid #3b82f6;
padding: 20px;
border-radius: 8px;
animation: fadeInUp 1.2s ease-out;
color: #1e40af;
font-size: 1rem;
line-height: 1.6;">
{qol_note}
</div>
""", unsafe_allow_html=True)

        # --- E. SOLUSI ---
        st.markdown(f"""
<div style="
background-color: #ffffff; 
border: 1px solid {border_hex}; 
border-radius: 15px; 
padding: 25px; 
margin-top: 10px;
box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
animation: fadeInUp 1.4s ease-out;">

<h3 style="color: {border_hex}; margin-bottom: 15px; display: flex; align-items: center; gap: 10px; font-size: 1.2rem;">
💡 Hal yang Harus Bapak Lakukan Sekarang
</h3>
<hr style="border-top: 1px solid #e2e8f0; margin-bottom: 15px;">

<div style="color: #334155; font-size: 1.05rem; line-height: 1.6;">
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