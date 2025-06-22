import streamlit as st

st.title("🧴 Rekomendasi Skincare Berdasarkan Masalah Kulit")

# Input dari pengguna
keluhan = st.selectbox(
    "Apa masalah kulit kamu saat ini?",
    ["Jerawat", "Kulit Kering", "Kulit Kusam", "Kulit Sensitif", "Kulit Berminyak"]
)

# Fungsi rekomendasi
def rekomendasi_skincare(keluhan):
    if keluhan == "Jerawat":
        return {
            "kandungan": "Salicylic Acid, Niacinamide",
            "produk": [
                "Some By Mi AHA BHA PHA Toner",
                "The Ordinary Niacinamide 10% + Zinc 1%"
            ]
        }
    elif keluhan == "Kulit Kering":
        return {
            "kandungan": "Hyaluronic Acid, Ceramide",
            "produk": [
                "Cetaphil Moisturizing Cream",
                "Hada Labo Gokujyun Lotion"
            ]
        }
    elif keluhan == "Kulit Kusam":
        return {
            "kandungan": "Vitamin C, Alpha Arbutin",
            "produk": [
                "Wardah C-Defense Serum",
                "The Ordinary Alpha Arbutin 2% + HA"
            ]
        }
    elif keluhan == "Kulit Sensitif":
        return {
            "kandungan": "Centella Asiatica, Madecassoside",
            "produk": [
                "Skin1004 Madagascar Centella Ampoule",
                "La Roche-Posay Toleriane Sensitive"
            ]
        }
    elif keluhan == "Kulit Berminyak":
        return {
            "kandungan": "Zinc PCA, Clay, Niacinamide",
            "produk": [
                "Innisfree Super Volcanic Clay Mask",
                "The Ordinary Niacinamide 10% + Zinc 1%"
            ]
        }

# Tombol & output
if st.button("Dapatkan Rekomendasi"):
    hasil = rekomendasi_skincare(keluhan)
    st.subheader("✨ Kandungan yang Direkomendasikan:")
    st.write(hasil["kandungan"])
    st.subheader("📦 Produk Skincare:")
    for p in hasil["produk"]:
        st.write("- " + p)