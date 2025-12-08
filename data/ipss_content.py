# File: data/ipss_content.py

# --- SKOR GEJALA (0-5) ---
SKOR_FREKUENSI = [
    "Sama sekali tidak",          
    "Kurang dari 1 kali dalam 5", 
    "Kurang dari setengah waktu", 
    "Sekitar setengah waktu",     
    "Lebih dari separuh waktu",   
    "Hampir selalu"               
]

SKOR_NOKTURIA = [
    "0 kali", "1 kali", "2 kali", 
    "3 kali", "4 kali", "5 kali atau lebih"
]

# --- SKOR QOL (0-6) ---
SKOR_QOL_OPTS = [
    "Sangat Senang (Delighted)",
    "Senang (Pleased)",
    "Puas (Mostly Satisfied)",
    "Biasa Saja / Campur Aduk (Mixed)",
    "Kurang Puas (Mostly Dissatisfied)",
    "Tidak Senang / Kecewa (Unhappy)",
    "Sengsara / Sangat Buruk (Terrible)"
]

PERTANYAAN_IPSS = [
    {
        "id": "q1", "title": "Rasa Tidak Tuntas", "icon": "💧",
        "detail": "Setelah selesai pipis, seberapa sering Bapak merasa seperti masih ada sisa atau belum keluar semua?",
        "note": "Rasanya seperti ingin pipis lagi tak lama setelah selesai.", "scoring": SKOR_FREKUENSI
    },
    {
        "id": "q2", "title": "Sering Pipis (Frekuensi)", "icon": "⏱️",
        "detail": "Seberapa sering Bapak harus balik lagi ke kamar mandi untuk pipis, padahal baru saja pipis kurang dari 2 jam yang lalu?",
        "note": "", "scoring": SKOR_FREKUENSI
    },
    {
        "id": "q3", "title": "Kencing Terputus-putus", "icon": "🚧",
        "detail": "Saat sedang pipis, seberapa sering alirannya berhenti lalu jalan lagi (nyendat-nyendat)?",
        "note": "Bukan sengaja ditahan, tapi berhenti sendiri.", "scoring": SKOR_FREKUENSI
    },
    {
        "id": "q4", "title": "Tidak Bisa Menahan", "icon": "🏃",
        "detail": "Seberapa sering Bapak merasa kebelet sekali sampai susah menahannya (harus buru-buru ke WC takut mengompol)?",
        "note": "", "scoring": SKOR_FREKUENSI
    },
    {
        "id": "q5", "title": "Pancaran Lemah", "icon": "🚿",
        "detail": "Seberapa sering aliran pipis Bapak terasa lemah atau pelan?",
        "note": "Pancarannya tidak jauh, atau jatuhnya dekat kaki.", "scoring": SKOR_FREKUENSI
    },
    {
        "id": "q6", "title": "Harus Mengedan", "icon": "💪",
        "detail": "Seberapa sering Bapak harus ngeden atau memaksa dulu supaya air kencingnya bisa keluar?",
        "note": "", "scoring": SKOR_FREKUENSI
    },
    {
        "id": "q7", "title": "Pipis Malam Hari", "icon": "🌙",
        "detail": "Rata-rata, seberapa sering Bapak harus bangun dari tidur malam untuk pipis?",
        "note": "Hitungan adalah jumlah kali terbangun karena dorongan ingin pipis.", "scoring": SKOR_NOKTURIA
    },
]

PERTANYAAN_QOL = {
    "id": "q8_qol",
    "title": "Kualitas Hidup (Quality of Life)",
    "icon": "❤️",
    "detail": "Kalau seandainya kondisi kencing Bapak terus begini seumur hidup, apa yang Bapak rasakan?",
    "note": "Pilihlah yang paling menggambarkan perasaan Bapak.",
    "scoring": SKOR_QOL_OPTS
}

# --- LOGIKA KLASIFIKASI ---
def classify_score(total_score):
    if 0 <= total_score <= 7:
        return "Ringan (Mildly Symptomatic)", "Perubahan gaya hidup mungkin sudah cukup. Pantau terus.", "success"
    elif 8 <= total_score <= 19:
        return "Sedang (Moderately Symptomatic)", "Gejala cukup mengganggu. Disarankan konsultasi ke dokter.", "warning"
    elif 20 <= total_score <= 35:
        return "Berat (Severely Symptomatic)", "Gejala sangat mengganggu kualitas hidup. Segera ke dokter spesialis.", "error"
    else:
        return "Error", "Hitung ulang.", "info"

def get_qol_message(total_score, qol_score):
    if total_score <= 7:
        if qol_score >= 4:
            return "⚠️ Catatan Penting: Meskipun skor gejala Bapak tergolong ringan, namun Bapak merasa kurang puas dengan kondisi saat ini. Bapak bisa datang ke dokter untuk konsultasi lebih lanjut ya!"
        else:
            return None
    else:
        return "ℹ️ Catatan Penting: Bagaimanapun kualitas hidup yang Bapak rasakan karena gejala ini, tetap utamakan ikuti rekomendasi pengobatan yang diberikan ya!"

# --- LOGIKA REKOMENDASI DETIL (BARU) ---
def get_detailed_advice(total_score):
    """
    Mengembalikan teks saran berdasarkan kategori skor.
    Menggunakan format HTML sederhana untuk list agar rapi di Streamlit.
    """
    if total_score <= 7:
        # MILD
        return """
        <div style="text-align: left; margin-top: 10px;">
            <p><strong>Status:</strong> Kondisi Anda kemungkinan besar masih aman, namun perlu dipantau.</p>
            <p><strong>Rekomendasi Utama:</strong> <span style="color: #22c55e; font-weight: bold;">Watchful Waiting (Pemantauan Aktif).</span> Biasanya belum memerlukan obat-obatan atau operasi, cukup perubahan gaya hidup.</p>
            <p><strong>Saran Gaya Hidup:</strong></p>
            <ul style="line-height: 1.6;">
                <li><strong>Kurangi Cairan Malam Hari:</strong> Batasi minum setelah makan malam agar tidak sering bangun pipis.</li>
                <li><strong>Hindari Iritan:</strong> Kurangi konsumsi kopi (kafein), alkohol, dan makanan pedas/asin karena dapat mengiritasi kandung kemih.</li>
                <li><strong>Cek Obat Lain:</strong> Hati-hati dengan obat flu yang mengandung <em>fenilpropanolamin</em>, karena bisa memperparah gejala.</li>
                <li><strong>Jangan Menahan:</strong> Jangan biasakan menahan kencing terlalu lama.</li>
                <li><strong>Jadwal Ulang:</strong> Lakukan tes ini lagi dalam 6 bulan untuk melihat apakah ada perubahan.</li>
            </ul>
        </div>
        """
    elif 8 <= total_score <= 19:
        # MODERATE
        return """
        <div style="text-align: left; margin-top: 10px;">
            <p><strong>Status:</strong> Gejala Anda mulai mengganggu kualitas hidup dan memerlukan evaluasi medis.</p>
            <p><strong>Rekomendasi Utama:</strong> <span style="color: #f59e0b; font-weight: bold;">Disarankan untuk berkonsultasi dengan dokter (Urolog).</span></p>
            <p><strong>Langkah Selanjutnya:</strong></p>
            <ul style="line-height: 1.6;">
                <li><strong>Pemeriksaan Lanjutan:</strong> Dokter mungkin akan menyarankan pemeriksaan tambahan seperti USG prostat atau tes pancaran urine (Uroflowmetry).</li>
                <li><strong>Opsi Terapi:</strong> Jika gejala dirasa mengganggu aktivitas sehari-hari, dokter dapat meresepkan obat-obatan (seperti penghambat alfa atau penghambat 5-alfa reduktase) untuk melancarkan kencing dan mengecilkan prostat.</li>
                <li><strong>Catatan Harian:</strong> Disarankan membuat "Catatan Harian Berkemih" (Voiding Diary) sebelum ke dokter untuk membantu diagnosis.</li>
            </ul>
        </div>
        """
    else:
        # SEVERE (>= 20)
        return """
        <div style="text-align: left; margin-top: 10px;">
            <p><strong>Status:</strong> Kondisi ini memerlukan penanganan medis segera untuk mencegah komplikasi.</p>
            <p><strong>Rekomendasi Utama:</strong> <span style="color: #ef4444; font-weight: bold;">SEGERA konsultasi ke Dokter Spesialis Urologi.</span></p>
            <p><strong>Langkah Selanjutnya:</strong></p>
            <ul style="line-height: 1.6;">
                <li><strong>Risiko Komplikasi:</strong> Tanpa penanganan, kondisi ini berisiko menyebabkan kencing macet total (retensi urine), infeksi saluran kemih berulang, atau gangguan fungsi ginjal.</li>
                <li><strong>Terapi Agresif:</strong> Kemungkinan besar memerlukan kombinasi obat-obatan atau diskusi mengenai tindakan pembedahan (seperti TURP) jika obat tidak mempan.</li>
            </ul>
        </div>
        """