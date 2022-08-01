import streamlit as st
import streamlit.components.v1 as components
import webbrowser
from streamlit_option_menu import option_menu
from PIL import Image

def caesar_encrypt(plain_text, KEY):
    ALPHABET = ' abcdefghijklmnopqrstuvwxyz'
    cipher_text = ''
    plain_text = plain_text.lower()

    for c in plain_text:
        index = ALPHABET.find(c)
        index = (index + KEY) % len(ALPHABET)
        cipher_text = cipher_text + ALPHABET[index]

    return cipher_text


# 2. horizontal menu
selected = option_menu(None, ["Caesar", "ROT 13", "XOR Cipher", 'Base64'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
#selected
if selected=="Caesar":
    st.header('Caesar Cipher')
    st.write("Caesar Cipher merupakan salah satu algoritma cipher tertua dan paling diketahui dalam perkembangan ilmu kriptografi. Caesar cipher merupakan salah satu jenis cipher substitusi yang membentuk cipher dengan cara melakukan penukaran karakter pada plainteks menjadi tepat satu karakter pada chiperteks. Teknik seperti ini disebut juga sebagai chiper abjad tunggal. Algoritma kriptografi Caesar Cipher sangat mudah untuk digunakan. Inti dari algoritma kriptografi ini adalah melakukan pergeseran terhadap semua karakter pada plainteks dengan nilai pergeseran yang sama. Adapun langkah-langkah yang dilakukan untuk membentuk chiperteks dengan Caesar Cipher adalah:Menentukan besarnya pergeseran karakter yang digunakan dalam membentuk cipherteks ke plainteks, Menukarkan karakter pada plainteks menjadi cipherteks dengan berdasarkan pada pergeseran yang telah ditentukan sebelumnya")
    st.subheader('Coba Enkripsi Caesar Cipher')
    plain_text = st.text_input("Masukkan kata")
    key = st.number_input("Masukkan jumlah pergeseran", 0, 255, 0, 1)
    #st.write("Cipher Text")
    st.text_area(label="Cipher Text",value=caesar_encrypt(plain_text,key))



if selected=="ROT 13":
    image = Image.open('././src/img/linux.jpg')
    st.image(image, caption='')

    st.title("Linux Password Policy")
    st.write('''
    Password adalah sebuah atribut yang sangat penting dalam keamanan sebuah sistem. Tidak hanya password milik system administrator, namun juga password user biasa. Apabila password user sistem dibuat sesuka hati maka besar kemungkinan penyusup akan dapat menjebol sistem melalui akun tersebut. Oleh karena itu system administrator harus dapat membuat aturan standar pembuatan password serta melakukan pengelolaan password sehingga password yang lemah tidak menjadi celah keamanan sistem
    ''')
    st.markdown('''
    - [Kompleksitas Password](#section-1)
    - [Menginstall PAM](#section-2)
    - [Membuat Aturan Kompleksitas Password](#section-3)
    - [Mengatur Masa Pakai Password](#section-4)
    ''', unsafe_allow_html=True)

