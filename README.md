# 🤖 Chatbot NLP Bahasa Indonesia

Aplikasi chatbot berbasis **TF-IDF + Cosine Similarity** yang dibangun menggunakan **Streamlit**.  
Ringan, offline-capable, dan dapat dideploy ke **Streamlit Cloud** secara gratis.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)

---

## ✨ Fitur

- 💬 **Chat interaktif** dengan tampilan bubble chat modern
- 📄 **Upload dokumen .txt** sebagai sumber pengetahuan (knowledge base)
- 🧠 **NLP Bahasa Indonesia** — tokenisasi, stopword removal, stemming ringan
- 📊 **TF-IDF + N-Gram** untuk representasi teks
- 🔍 **Cosine Similarity** untuk mencari jawaban paling relevan
- 🎚️ **Threshold slider** untuk mengatur sensitivitas jawaban
- 💾 **Riwayat chat** tersimpan selama sesi berlangsung
- ☁️ **100% kompatibel** dengan Streamlit Cloud (tanpa GPU, tanpa library berat)

---

## 📁 Struktur File

```
chatbot-nlp/
├── chatbot_app.py        # Aplikasi utama Streamlit
├── requirements.txt      # Daftar library Python
├── dokumen.txt           # Knowledge base default
├── dokumen_unpam.txt     # Knowledge base khusus UNPAM (contoh)
└── README.md             # Dokumentasi ini
```

---

## 🚀 Cara Menjalankan Secara Lokal

### 1. Clone repository
```bash
git clone https://github.com/username/chatbot-nlp.git
cd chatbot-nlp
```

### 2. Buat virtual environment (opsional tapi disarankan)
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install library
```bash
pip install -r requirements.txt
```

### 4. Jalankan aplikasi
```bash
streamlit run chatbot_app.py
```

### 5. Buka browser
```
http://localhost:8501
```

---

## ☁️ Deploy ke Streamlit Cloud

1. **Push** semua file ke repository GitHub
2. Buka [share.streamlit.io](https://share.streamlit.io)
3. Login menggunakan akun GitHub
4. Klik **"New app"**
5. Pilih repository, branch `main`, dan file `chatbot_app.py`
6. Klik **"Deploy!"**
7. Tunggu 1–2 menit → aplikasi online! 🎉

---

## 📖 Cara Menggunakan

### Menggunakan Knowledge Base Default
Langsung ketik pertanyaan di kolom chat. Chatbot akan menjawab berdasarkan knowledge base bawaan yang mencakup topik AI, machine learning, NLP, dan tata kelola TI.

### Menggunakan Dokumen Sendiri
1. Siapkan file `.txt` berisi informasi yang ingin dijadikan sumber jawaban
2. Klik **"Browse files"** di sidebar kiri
3. Upload file `.txt` Anda
4. Mulai bertanya sesuai isi dokumen

### Contoh Pertanyaan (Knowledge Base UNPAM)
Upload `dokumen_unpam.txt` lalu coba tanyakan:
- *"Dimana lokasi kampus UNPAM?"*
- *"Apa saja fakultas di UNPAM?"*
- *"Bagaimana cara mendaftar di UNPAM?"*
- *"Berapa SKS minimal untuk lulus?"*
- *"Apa itu program magang di UNPAM?"*

---

## ⚙️ Pengaturan Threshold

| Nilai | Efek |
|-------|------|
| 0.05 – 0.10 | Mudah menjawab, cocok untuk pertanyaan umum |
| 0.15 – 0.20 | Seimbang (default) |
| 0.25 – 0.50 | Selektif, hanya menjawab jika sangat relevan |

---

## 🛠️ Teknologi yang Digunakan

| Library | Fungsi |
|---------|--------|
| `streamlit` | Framework UI web interaktif |
| `scikit-learn` | TF-IDF Vectorizer & Cosine Similarity |
| `nltk` | Tokenisasi & stopword Bahasa Indonesia |

---

## 📝 Membuat Knowledge Base Sendiri

Buat file `.txt` dengan format bebas. Setiap kalimat atau paragraf akan menjadi sumber jawaban chatbot.

**Tips:**
- Tulis setiap informasi dalam kalimat yang jelas dan lengkap
- Satu kalimat = satu fakta/informasi
- Semakin banyak kalimat, semakin pintar chatbot dalam menjawab
- Gunakan Bahasa Indonesia yang baku untuk hasil terbaik

**Contoh isi dokumen:**
```
Universitas Pamulang berlokasi di Pamulang, Tangerang Selatan.
Biaya kuliah UNPAM termasuk yang paling terjangkau di Indonesia.
Pendaftaran mahasiswa baru dilakukan melalui pmb.unpam.ac.id.
```

---

## 👨‍💻 Pengembangan Selanjutnya

- [ ] Integrasi PDF upload langsung
- [ ] Preprocessing Bahasa Indonesia dengan Sastrawi (lokal)
- [ ] Semantic search dengan IndoBERT ringan
- [ ] Simpan riwayat chat ke CSV
- [ ] Dashboard statistik percakapan
- [ ] Multi-dokumen knowledge base

---

## 📄 Lisensi

Project ini dibuat untuk keperluan akademik dan pembelajaran.  
Bebas digunakan dan dikembangkan dengan menyertakan atribusi.

---

> Dibuat dengan ❤️ menggunakan Python & Streamlit