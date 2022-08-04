import streamlit as st
import streamlit.components.v1 as components
import webbrowser
import streamlit_option_menu
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

def rot13_encrypt(plain_text):
    ALPHABET = ' abcdefghijklmnopqrstuvwxyz'
    KEY=13
    cipher_text = ''
    plain_text = plain_text.lower()

    for c in plain_text:
        index = ALPHABET.find(c)
        index = (index + KEY) % len(ALPHABET)
        cipher_text = cipher_text + ALPHABET[index]

    return cipher_text

def xor_encrypt(plain_text,key):
    a=[ord(i)^ord(key) for i in plain_text]
    for i in a:
        print(chr(i),end="")
    return a


# 2. horizontal menu
selected = option_menu(None, ["Caesar", "ROT 13", "XOR Cipher", 'Base64'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
#selected
if selected=="Caesar":
    st.header('Caesar Cipher')
    st.write("Caesar Cipher merupakan salah satu algoritma cipher tertua dan paling diketahui dalam perkembangan ilmu kriptografi. Caesar cipher merupakan salah satu jenis cipher substitusi yang membentuk cipher dengan cara melakukan penukaran karakter pada plainteks menjadi tepat satu karakter pada chiperteks. Teknik seperti ini disebut juga sebagai chiper abjad tunggal. Algoritma kriptografi Caesar Cipher sangat mudah untuk digunakan. Inti dari algoritma kriptografi ini adalah melakukan pergeseran terhadap semua karakter pada plainteks dengan nilai pergeseran yang sama. Adapun langkah-langkah yang dilakukan untuk membentuk chiperteks dengan Caesar Cipher adalah:Menentukan besarnya pergeseran karakter yang digunakan dalam membentuk cipherteks ke plainteks, Menukarkan karakter pada plainteks menjadi cipherteks dengan berdasarkan pada pergeseran yang telah ditentukan sebelumnya")
    image = Image.open('././src/img/caesar.png')
    st.image(image, caption='Cipher yang digambarkan di sini menggunakan shift kiri tiga, sehingga (misalnya) setiap kemunculan E pada plaintext menjadi B pada ciphertext.')
    st.subheader('Coba Enkripsi Caesar Cipher')
    plain_text = st.text_input("Masukkan kata")
    key = st.number_input("Masukkan jumlah pergeseran", 0, 255, 0, 1)
    st.text_area(label="Cipher Text",value=caesar_encrypt(plain_text,key))


if selected=="ROT 13":
    st.title("ROT 13")
    st.write('''
    Salah satu contoh dari "substitution cipher" adalah Rot13. Metode rot13 merupakan metode enkripsi yang mengubah suatu huruf menjadi huruf yang letaknya 13 posisi dari huruf semula. Misalnya 'A' akan berubah menjadi 'N' , 'B' berubah menjadi 'O', dst. Rumusnya seperti dibawah ini :
    ''')
    image = Image.open('././src/img/rot13.jpg')
    st.image(image, caption='')
    st.write('''C = ROT13(input)''')
    st.write('''Jika kita ingin merubahnya ke huruf semula, yang harus dilakukan adalah melakukan proses ROT13 sebanyak 2 kali dari huruf awalnya.''')
    st.write('''M = ROT13(ROT13(input))''')
    st.write('''Misal : Plaintext : ZAENAL''')
    st.write('''Ciphertextnya : MNRANY''')
    st.subheader("Coba Enkripsi ROT 13")
    plain_text = st.text_input("Masukkan kata")
    st.text_area(label="Cipher Text",value=rot13_encrypt(plain_text))


if selected=="XOR Cipher":
    st.title("XOR Cipher")
    st.write('''
    Dalam kriptografi, pembuatan chiper (teks hasil enkripsi) melalui operasi XOR merupakan suatu algoritma enskripsi yang relatif sederhana. Teknik ini beroperasi sesuai dengan prinsip:
    ''')
    st.write('''A XOR 0 = A''')
    st.write(''' A XOR A = 0''')
    st.write('''(B XOR A) XOR A = B XOR 0 = B''')
    st.write('''Dengan logika ini, suatu string teks dapat diekripsi dengan menerapkan operasi XOR berbasis bit (binary digit) terhadap setiap karakter menggunakan key tertentu. Bagaimana mendekripsi outputnya untuk mendapatkan plaintext kembali? Dengan menerapkan operasi XOR terhadap chiper.''')
    st.write('''Sebagai contoh, string “Wiki” jika ditulis dalam format ASCII 8 bit menjadi 01010111 01101001 01101011 01101001 dapat dienkripsi dengan suatu key misalnya 11110011 sebagai berikut:''')
    image = Image.open('././src/img/xor.png')
    st.image(image, caption='')
    st.write('''Operator XOR sering dijadikan sebagai salah satu komponen dalam pembentukan chiper yang lebih kompleks. Namun, penggunaan suatu key yang berulang secara konstan menyebabkan suatu chiper dapat dengan mudah dipecahkan menggunakan analisis frekuensi (seperti dibahas pada huruf yang paling sering muncul dalam suatu bahasa). Keutamaan dari teknik ini adalah mudah diimplementasikan dan operasi XOR tidak mahal secara komputasional. Karena itu, chiper XOR masih sering kali digunakan untuk menyembunyikan informasi dalam kasus dan kemudian dilengkapi dengan suatu mekanisme keamanan tambahan. Akan tetapi, jika key dibuat sepanjang message (pesan), tidak berulang dan bit-bitnya bersifat random, maka akan menghadirkan efek one-time-pad (dikenal pula sebagai chiper Vernam) yang tidak dapat dipecahkan, bahkan dalam teori sekalipun.''')
    st.write('''Chiper XOR benar-benar lemah terhadap serangan plaintext umum, karena plaintext XOR ciphertext = key.''')
    st.subheader("Coba Enkripsi ROT 13")
    plain_text = st.text_input("Masukkan kata")
    key = st.text_input("Kunci (1 huruf)")
    st.text_area(label="Cipher Text",value=xor_encrypt(plain_text,key)
)
