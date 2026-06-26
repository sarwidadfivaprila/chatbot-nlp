import streamlit as st
import re
import string
import nltk
import os

# =============================================
# KONFIGURASI HALAMAN
# =============================================
st.set_page_config(
    page_title="Chatbot NLP Indonesia",
    page_icon="🤖",
    layout="centered"
)

# =============================================
# CSS KUSTOM
# =============================================
st.markdown("""
<style>
    .stChatMessage { border-radius: 12px; margin-bottom: 8px; }
    .metric-card {
        background: #f0f2f6;
        border-radius: 10px;
        padding: 12px 16px;
        text-align: center;
    }
    .stAlert { border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

# =============================================
# DOWNLOAD NLTK (cloud-safe)
# =============================================
@st.cache_resource
def download_nltk():
    nltk_data_dir = os.path.expanduser("~/nltk_data")
    os.makedirs(nltk_data_dir, exist_ok=True)
    for pkg in ["punkt", "stopwords", "punkt_tab"]:
        try:
            nltk.download(pkg, quiet=True)
        except Exception:
            pass

download_nltk()

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# =============================================
# PREPROCESSING (tanpa Sastrawi, cloud-safe)
# =============================================
STOP_WORDS = set(stopwords.words("indonesian"))

# Kamus stemming manual ringan (menggantikan Sastrawi)
PREFIXES = ["me", "men", "mem", "meng", "meny", "ber", "be", "ter", "pe",
            "per", "pen", "pem", "peng", "peny", "ke", "se", "di", "ku", "kau"]
SUFFIXES = ["kan", "an", "i", "lah", "kah", "nya", "ku", "mu"]

def simple_stem(word):
    for suffix in SUFFIXES:
        if word.endswith(suffix) and len(word) - len(suffix) >= 3:
            word = word[:-len(suffix)]
            break
    for prefix in PREFIXES:
        if word.startswith(prefix) and len(word) - len(prefix) >= 3:
            word = word[len(prefix):]
            break
    return word

def preprocessing(text):
    text = text.lower()
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if w not in STOP_WORDS and len(w) > 2]
    tokens = [simple_stem(w) for w in tokens]
    return " ".join(tokens)

# =============================================
# KNOWLEDGE BASE DEFAULT
# =============================================
DEFAULT_KNOWLEDGE = """
COBIT 2019 adalah framework tata kelola teknologi informasi yang digunakan oleh organisasi di seluruh dunia.
Framework COBIT digunakan untuk meningkatkan governance dan manajemen TI organisasi secara efektif.
COBIT membantu organisasi mencapai tujuan bisnis melalui pengelolaan TI yang baik dan terstruktur.

DMBOK adalah framework standar untuk tata kelola dan manajemen data perusahaan.
DMBOK digunakan sebagai panduan dalam pengelolaan aset data organisasi secara menyeluruh.
Framework DMBOK mencakup berbagai aspek manajemen data mulai dari arsitektur hingga kualitas data.

Machine learning adalah cabang kecerdasan buatan yang memungkinkan sistem belajar dari data secara otomatis.
Algoritma machine learning dapat meningkatkan kinerjanya melalui pengalaman tanpa diprogram secara eksplisit.
Contoh penerapan machine learning adalah klasifikasi email, rekomendasi produk, dan deteksi penipuan.

Deep learning adalah subset dari machine learning yang menggunakan jaringan saraf tiruan berlapis-lapis.
Model deep learning membutuhkan data yang besar dan komputasi yang kuat untuk proses pelatihan.

Natural Language Processing atau NLP adalah bidang AI yang berkaitan dengan pemahaman bahasa manusia oleh komputer.
NLP digunakan dalam aplikasi seperti chatbot, penerjemah otomatis, dan analisis sentimen teks.
Teknik NLP meliputi tokenisasi, stemming, lemmatisasi, dan analisis sintaksis kalimat.

TF-IDF adalah metode pembobotan kata yang menggabungkan frekuensi kata dalam dokumen dan frekuensi inversi dokumen.
TF-IDF digunakan untuk mengukur seberapa penting sebuah kata dalam koleksi dokumen tertentu.
Nilai TF-IDF tinggi menunjukkan kata tersebut relevan dalam dokumen tetapi jarang muncul secara umum.

Cosine Similarity adalah metode untuk mengukur kesamaan antara dua vektor dalam ruang multidimensi.
Nilai cosine similarity berkisar antara 0 hingga 1, di mana 1 berarti identik dan 0 berarti tidak ada kesamaan.
Cosine similarity banyak digunakan dalam sistem pencarian informasi dan sistem rekomendasi konten.

Audit TI adalah proses pemeriksaan sistematis terhadap infrastruktur, kebijakan, dan operasi teknologi informasi.
Audit TI digunakan untuk mengevaluasi efektivitas penerapan teknologi informasi di dalam organisasi.
Hasil audit TI dapat digunakan sebagai dasar perbaikan tata kelola TI perusahaan ke depannya.

Streamlit adalah framework Python open-source untuk membuat aplikasi web interaktif dengan sangat cepat.
Streamlit sangat cocok digunakan untuk membuat dashboard data science dan aplikasi machine learning.
Dengan Streamlit, developer bisa membuat aplikasi web tanpa pengetahuan mendalam tentang HTML atau CSS.

Python adalah bahasa pemrograman tingkat tinggi yang populer untuk data science dan machine learning.
Python dikenal dengan sintaksnya yang bersih dan mudah dibaca sehingga cocok untuk pemula maupun ahli.
Library populer Python antara lain NumPy, Pandas, Scikit-learn, TensorFlow, dan PyTorch.

Kecerdasan buatan atau Artificial Intelligence adalah simulasi kecerdasan manusia yang diprogram pada mesin.
AI mencakup berbagai teknik termasuk machine learning, deep learning, computer vision, dan NLP.
Penerapan AI semakin luas di berbagai bidang seperti kesehatan, keuangan, transportasi, dan pendidikan.

Data science adalah bidang ilmu yang menggabungkan statistik, pemrograman, dan pengetahuan domain tertentu.
Data scientist bertugas menganalisis data besar untuk menghasilkan wawasan yang berguna bagi bisnis.
Proses data science meliputi pengumpulan data, pembersihan, eksplorasi, pemodelan, dan komunikasi hasil.

Chatbot adalah program komputer yang dirancang untuk mensimulasikan percakapan dengan pengguna manusia.
Chatbot berbasis aturan bekerja dengan mencocokkan pola teks, sedangkan chatbot AI menggunakan model bahasa.
Chatbot digunakan luas dalam layanan pelanggan, pendidikan, kesehatan, dan berbagai bidang lainnya.

Python Scikit-learn adalah library machine learning yang menyediakan berbagai algoritma klasifikasi dan regresi.
Scikit-learn mudah digunakan dan memiliki dokumentasi yang sangat lengkap untuk berbagai kebutuhan ML.

Basis data atau database adalah kumpulan data yang terorganisasi dan dapat diakses secara elektronik.
Sistem manajemen basis data atau DBMS digunakan untuk membuat, mengelola, dan mengakses database.
Contoh DBMS populer adalah MySQL, PostgreSQL, MongoDB, dan SQLite.
"""

# =============================================
# BUILD KNOWLEDGE BASE
# =============================================
@st.cache_resource
def build_knowledge_base(text):
    sentences = sent_tokenize(text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 15]
    clean = [preprocessing(s) for s in sentences]
    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    X = vectorizer.fit_transform(clean)
    return sentences, vectorizer, X

# =============================================
# FUNGSI RESPONS CHATBOT
# =============================================
def chatbot_response(user_input, sentences, vectorizer, X, threshold=0.10):
    clean_input = preprocessing(user_input)
    if not clean_input.strip():
        return "Pertanyaan terlalu singkat atau tidak dikenali. Coba tanyakan lebih spesifik."
    user_vec = vectorizer.transform([clean_input])
    sim = cosine_similarity(user_vec, X)
    idx = int(sim.argmax())
    score = float(sim[0][idx])
    if score < threshold:
        return "Maaf, saya tidak menemukan informasi yang relevan. Coba gunakan kata kunci yang lebih spesifik."
    return sentences[idx]

# =============================================
# UI UTAMA
# =============================================
st.title("🤖 Chatbot NLP Bahasa Indonesia")
st.caption("Berbasis TF-IDF + Cosine Similarity | Ringan & Bisa Diakses Online")

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=50)
    st.markdown("## ⚙️ Pengaturan")

    st.markdown("### 📄 Upload Dokumen")
    uploaded_file = st.file_uploader(
        "Upload file .txt sebagai sumber pengetahuan",
        type=["txt"],
        help="Chatbot akan menjawab berdasarkan isi dokumen ini"
    )

    st.markdown("### 🎚️ Sensitivitas Jawaban")
    threshold = st.slider(
        "Threshold kecocokan",
        min_value=0.05, max_value=0.50,
        value=0.10, step=0.05,
        help="Rendah = lebih mudah menjawab | Tinggi = lebih selektif"
    )

    st.markdown("### ℹ️ Tentang Aplikasi")
    st.info(
        "**Teknologi:**\n"
        "- NLTK (tokenisasi & stopword)\n"
        "- TF-IDF + N-Gram\n"
        "- Cosine Similarity\n"
        "- Streamlit Cloud"
    )

    if st.button("🗑️ Hapus Riwayat Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# --- LOAD KNOWLEDGE BASE ---
if uploaded_file is not None:
    doc_text = uploaded_file.read().decode("utf-8")
    st.sidebar.success(f"✅ Dokumen dimuat ({len(doc_text.split())} kata)")
else:
    doc_text = DEFAULT_KNOWLEDGE
    st.sidebar.caption("📌 Menggunakan knowledge base default")

sentences, vectorizer, X = build_knowledge_base(doc_text)

# --- SESSION STATE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- STATISTIK ---
col1, col2, col3 = st.columns(3)
col1.metric("📚 Data Kalimat", len(sentences))
col2.metric("💬 Total Pesan", len(st.session_state.messages))
col3.metric("🎯 Threshold", f"{threshold:.2f}")

st.divider()

# --- PESAN SAMBUTAN ---
if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.write(
            "👋 Halo! Saya siap menjawab pertanyaan Anda.\n\n"
            "**Coba tanyakan:**\n"
            "- Apa itu machine learning?\n"
            "- Jelaskan tentang COBIT 2019\n"
            "- Apa fungsi TF-IDF?\n"
            "- Apa itu audit TI?"
        )

# --- RIWAYAT CHAT ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# --- INPUT PENGGUNA ---
user_input = st.chat_input("Ketik pertanyaan Anda di sini...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Mencari jawaban..."):
            response = chatbot_response(user_input, sentences, vectorizer, X, threshold)
        st.write(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
