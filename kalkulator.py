import streamlit as st

def main():
    st.title("Kalkulator Sederhana")
    
    # Input angka pertama dan kedua
    num1 = st.number_input("Masukkan angka pertama", value=0.0, format="%.2f")
    num2 = st.number_input("Masukkan angka kedua", value=0.0, format="%.2f")
    
    # Pilihan operasi
    operation = st.selectbox("Pilih operasi", ["Tambah", "Kurang", "Kali", "Bagi"])
    
    # Tombol untuk menghitung
    if st.button("Hitung"):
        if operation == "Tambah":
            result = num1 + num2
        elif operation == "Kurang":
            result = num1 - num2
        elif operation == "Kali":
            result = num1 * num2
        elif operation == "Bagi":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Error: Pembagian dengan nol tidak diperbolehkan")
                return
        
        st.success(f"Hasil: {result:.2f}")

if __name__ == "__main__":
    main()
