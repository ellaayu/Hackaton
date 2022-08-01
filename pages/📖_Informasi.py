# Oraganisasi yang terlibat di dunia Cyber

import streamlit as st
import streamlit.components.v1 as components
import webbrowser
from streamlit_option_menu import option_menu
from PIL import Image

# 1. as sidebar menu
# with st.sidebar:
#     selected = option_menu("Main Menu", ["Home", 'Settings', "Projects"], 
#         icons=['house', 'gear', 'list-task'], menu_icon="cast", default_index=1)
#     selected

# if selected=="Home":
#     st.title("Home")
# if selected=="Projects":
#     st.title("Projects")
# if selected=="Settings":
#     st.title("Settings")
    
# 2. horizontal menu
selected = option_menu(None, ["Phising", "Linux Password", "SUDO", 'SSH'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected
if selected=="Phising":
    image = Image.open('././src/img/phishing-1.jpg')
    st.image(image, caption='')

    st.title("Phising")

    st.markdown('''

    - [Apa itu Phising](#section-1)
    - [Bagaimana menghindari Phising](#section-2)
    ''', unsafe_allow_html=True)

    st.header('Apa itu Phising')
    st.write('''
    Phising adalah upaya untuk mendapatkan informasi data seseorang dengan teknik pengelabuan. Data yang menjadi sasaran phising adalah data pribadi (nama, usia, alamat), data akun (username dan password), dan data finansial (informasi kartu kredit, rekening).

    Istilah resmi phising adalah phishing, yang berasal dari kata fishing yaitu memancing.

    Kegiatan phising memang bertujuan memancing orang untuk memberikan informasi pribadi secara sukarela tanpa disadari. Padahal informasi yang dibagikan tersebut akan digunakan untuk tujuan kejahatan.

    Kenapa korban mau melakukan hal itu?

    Pelaku phising biasanya menampakkan diri sebagai pihak atau institusi yang berwenang. Dengan menggunakan website atau email palsu yang tampak meyakinkan, banyak orang berhasil dikelabui.
    ''')

    st.header('Bagaimana menghindari Phising')
    st.write('''
    Setelah mengetahui apa itu phising dan ciri-cirinya, kali ini kita akan membahas tips menghindarinya, yaitu antara lain:

    1.         Rutin Memeriksa Keamanan Gadget

    Phising adalah kejahatan yang dapat menyerang seluruh aplikasi dalam gadget, termasuk aplikasi mobile banking. Jika kita suka menyimpan informasi di gadget (dalam aplikasi Note, misalnya), data ini juga akan terancam jika gadget kita terkena phising.

    Oleh karena itu, lakukan pemeriksaan keamanan menyeluruh di gadget secara rutin. Cek riwayat penggunaan aplikasi, file-file aneh, dan suhu gadget setiap kali Anda punya waktu luang.

    2.         Menyimpan Informasi Login dengan Hati-Hati

    Tips menghindari phising selanjutnya adalah menyimpan informasi login dengan hati-hati. Kita seringkali meninggalkan info login kita di sembarang tempat, misalnya di komputer umum atau di ponsel orang lain. Anda sebaiknya menghindari ini jika tidak ingin jadi korban phising.

    Selain menyimpan info login dengan hati-hati, pastikan juga untuk selalu menggunakan kata sandi unik. Jika takut kesulitan mengingat, Anda bisa menulisnya di sebuah catatan pribadi dan tidak meninggalkannya di sembarang tempat.

    3.         Tidak Mengikuti Perintah Email/Pesan Teks Mencurigakan

    Tips berikutnya menghindari phising adalah dengan mengabaikan seluruh email atau pesan teks mencurigakan. Dalam sehari, Anda bisa saja menerima serangan phising lebih dari beberapa kali. Sesering apapun, jangan sampai Anda melakukan perintah dari pengirim mencurigakan. Jika pengirim tersebut mengaku sebagai orang lain, coba hubungi orang aslinya.

    4.         Mengakses Website dengan SSL

    SSL adalah Secure Socket Layer yang dipasang di website agar pengaksesnya terlindung serangan online. Jika ingin perangkat Anda terlindung dari phising dan malware, sebaiknya hanya kunjungi website dengan SSL. Cara membedakan website SSL dengan tanpa SSL adalah dari protokol aksesnya. Website dengan SSL protokol aksesnya adalah “https://”, bukan “https://”

    5.         Waspada Menerima Telpon Tidak Dikenal

    Tips menghindari phising berikutnya adalah tidak menerima telpon orang asing. Kalau pun Anda harus menerima, dengarkan dulu apa kepentingan orang asing tersebut. Jika permintaannya menyangkut hal-hal privasi/meminta uang, sebaiknya Anda abaikan saja telponnya.

    6.         Tidak Mudah Tergiur Hadiah yang Ditawarkan Email/Pesan Teks

    Selain waspada saat menerima telpon, Anda juga sebaiknya tidak mudah tergoda oleh hadiah dari email atau pesan teks. Sebagian besar hadiah semacam itu hanyalah kedok untuk melakukan phising. Jika Anda tergiur, bukannya mendapat hadiah milyaran, Anda malah akan kehilangan banyak data berharga, termasuk data rekening.

    7.         Memasang Aplikasi Pelindung Phising

    Tips menghindari phising yang terakhir adalah memasang aplikasi pelindung phising dan malware. Ada banyak aplikasi semacam ini tersebar di internet, baik aplikasi ponsel atau aplikasi komputer. Oleh karena itu, pastikan aplikasi ini selalu terpasang di gadget Anda, agar gadget awet dari serangan phising maupun malware.

    Nah itulah informasi singkat terkait apa itu phising, ciri-ciri, dan tips menghindarinya. Phising adalah kejahatan online yang harus diwaspadai. Apabila anda merasa mengalami hal ini, segera lakukan tindakan pencegahan dengan mengabaikannya ya! Jika pelaku phising benar-benar mengganggu, laporkan saja ke pihak berwajib di sekitar Anda.
    ''')
if selected=="Linux Password":
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

    st.header('Kompleksitas Password')
    st.write('''
   Semakin rumit sebuah password maka akan lebih sulit dipecahkan, oleh karena itu aturan standar pembuatan password harus dibuat dengan memperhatikan tingkat kerumitan sebuah password. Berikut adalah aturan yang sering digunakan:

    · Panjang password minimal 6 karakter maksimal 64 karakter

    · Terdapat huruf kapital

    · Terdapat huruf kecil

    · Terdapat angka (0–9)

    · Terdapat karakter lain (non-alphanumeric characters: ~!@#$%^&*_-+=`|\(){}[]:;”’<>,.?/)
    ''')

    st.header('Menginstall PAM')
    st.write('''
    PAM atau Pluggable Authentication Modules memungkinkan system administrator untuk menerapkan aturan kekuatan/kompleksitas password pada seluruh user. Sehingga user terpaksa membuat password yang kompleks.

    sudo apt-get install libpam_cracklib
    ''')

    st.header('Membuat Aturan Kompleksitas Password')
    st.write('''
    1. File pengaturan berada pada direktori /etc/pam.d/ dengan nama file common-password, sebelum mengubah script, buat backup file terlebih dahulu.

    sudo cp /etc/pam.d/common-password /root/

    sudo nano /etc/pam.d/common-password

    2. Cari baris berikut

    Password requisite pam_cracklib.so retry=3 minlen=8 difok=3

    Administrator dapat mengubah aturan password sesuai kebutuhan dengan parameter sebagai berikut:

    · retry=3 : Memberikan 3 kali kesempatan memasukkan password sebelum error

    · minlen=16 : Jumlah minimal panjang password

    · difok=3 : Jumlah karakter sama yang diperbolahkan antara password lama dan baru

    · ucredit=-1 : Password harus mengandung minimal 1 huruf kapital

    · lcredit=-1 : Password harus mengandung mminimal 1 huruf kecil

    · dcredit=-1 : Password harus mengandung minimal 1 digit angka

    · ocredit=-1 : Password harus mengandung minimal 1 karakter spesial (non alphanumeric)

    3. Setelah mengubah aturan password, simpan file

    4. Selanjutnya coba untuk membuat password baru
    ''')

    st.header('Mengatur Masa Pakai Password')
    st.write('''
    Salah satu teknik keamanan password adalah dengan rutin mengganti password. Linux menyediakan command khusus untuk mengatur masa pakai atau kadaluarsa password user yaitu chage.

    1. Memeriksa masa pakai password user

    chage -l <username>

    2. Administrator dapat mengatur masa pakai password menggunakan option -M

    chage -M <jumlah-hari-masa-pakai> <username>

    Misalnya user sotya dapat memakai password hanya selama 30 hari, maka perintahnya
    chage -M 30 busotya

    3. Terdapat option lain yang juga dapat diatur sesuai kebutuhan, seperti

    -M = jumlah hari maksimum sebelum diminta mengganti password

    -m = jumlah minimum hari sebelum user diperbolehkan mengganti password

    -E = mengatur kadaluarsa akun
    ''')
if selected=="SUDO":
    image = Image.open('././src/img/sudo.jpg')
    st.image(image, caption='')

    st.title("Hardening Super User DO (SUDO)")

    st.write('''
    Super User adalah user dengan hak akses tertinggi pada sistem linux. Seseorang dengan autentikasi super user dapat mengakses seluruh file dan mengeksekusi seluruh perintah sistem. Untuk dapat mengakses hak akses super user, seseorang dapat menggunakan perintah su, kemudian memasukkan password root. Jika berhasil login, maka ia dapat menggunakan hak akses tertinggi tersebut. Penggunaan perintah su untuk mendapatkan hak akses super user harus dibatasi untuk sysadmin saja. Sementara itu, agar user biasa dapat mengeksekusi perintah administrasi sistem secara terbatas, dapat menggunakan sudo. Penggunaan sudo hanya memerlukan password user saja, sehingga user tidak perlu mengetahui password super user untuk dapat mengeksekusi perintah administrasi sistem. Namun, tentu saja kemudahaan seperti ini harus diperhatikan agar tidak menjadi celah keamanan bagi penyusup.
    ''')

    st.markdown('''

    - [Menambahkan User menjadi Pengguna Sudo (Sudoers)](#section-1)
    - [Menghapus User dari Group Sudo](#section-2)
    - [Membatasi Akses Sudoers](#section-3)
    ''', unsafe_allow_html=True)

    st.header('Menambahkan User menjadi Pengguna Sudo (Sudoers)')
    st.write('''
    Pada dasarnya sudo adalah group, sehingga apabila ingin meningkatkan hak akses seorang user menjadi sudoers, hanya perlu menambahkan user tersebut ke dalam group sudo.

    sudo usermod -aG sudo username

    Jika berhasil, user tersebut akan dapat menggunakan sudo dengan password usernya.
    ''')

    st.header('Menghapus User dari Group Sudo')
    st.write('''
   Apabila memungkinkan, sebaiknya user yang dapat menggunakan perintah sudo hanyalah system administrator saja. Oleh karena itu selalu periksa group seorang user, apakah ia termasuk dalam group sudo atau tidak.

    1. Periksa keanggotaan group sebuah user dengan perintah

    groups <username>

    Apabila user tersebut termasuk dalam group sudo, maka besar kemungkinan ia dapat mengakses atau mengeksekusi perintah administratif sistem.

    2. Menghapus keanggotaan group dengan perintah

    gpasswd -d <username> <group>
    Perlu diperhatikan bahwa perintah tersebut hanya dapat dijalankan oleh super user. Contoh apabila kita ingin menghaous keanggotaan user bambang dari group sudo, maka perintahnya adalah sebagai berikut:
    sudo gpasswd -d bambang sudo
    ''')

    st.header('Membatasi Akses Sudoers')
    st.write('''
    Sudoers dapat dibatasi hak aksesnya hanya pada perintah-perintah yang dibutuhkan saja. Sehingga sudoers tidak dapat dengan leluasa mengakses file atau perintah sistem.

    1. File konfigurasi sudoers dapat diakses dengan perintah

    sudo visudo

    2. Semisal sudoers hanya diperbolehkan mengeksekusi perintah instalasi apt-get saja maka ubah baris %sudo yang awalnya

    %sudo ALL=(ALL:ALL) ALL

    menjadi

    %sudo ALL=(ALL:ALL) PASSWD : /usr/bin/apt-get

    3. Simpan dan keluar

    4. Cobalah untuk mengeksekusi perintah selain apt-get dengan sudo. Apabila tidak berhasil maka konfigurasi benar
    ''')

if selected=="SSH":
    image = Image.open('././src/img/ssh.jpg')
    st.image(image, caption='')

    st.title("Secure Shell (SSH) Hardening")

    st.write('''
    Aplikasi yang digunakan untuk komunikasi dengan SSH adalah ssh, kita harus menginstall aplikasi ssh terlebih dulu dengan perintah

    1. Menginstall aplikasi ssh dengan perintah

    root@debian:/# apt-get install ssh

    Tekan Y apabila ada pertanyaan konfirmasi instalasi.

    Pada latihan ini, kamu akan bertindak sebagai SSH client yang akan meremote SSH server.
    SSH client : PC masing-masing, dengan IP, username, dan password masing-masing
    SSH server: PC server, dengan IP xxx username server dan password server

    Login menggunakan username dan password biasa

    2. Cobalah untuk mengakses PC kelompok lain dengan perintah ssh diikuti username@alamat-ip. MISALNYA, username kelompok lain adalah putri dan alamat ip nya adalah 192.168.1.10, maka perintah yang benar adalah

    root@debian:/# ssh putri@192.168.1.10

    kemudian masukkan password user putri tersebut.

    3. Jika password benar, maka kita dapat mengakses PC kelompok lain.
    ''')

    st.markdown('''

    - [Mengubah Default Port](#section-1)
    - [Login Tanpa Password (menggunakan public dan private key)](#section-2)
    - [Membatasi User yang dapat Mengakses Server](#section-3)
    ''', unsafe_allow_html=True)

    st.header('Mengubah Default Port')
    st.write('''
    Secara default SSH menggunakan port 22, port tersebut termasuk dalam kategori weel-known port (0–1023) yang akan dengan mudah discan dengan aplikasi scanning network seperti nmap. Salah satu cara termudah untuk meningkatkan keamanan layanan SSH adalah dengan mengubah port 22 menjadi yang tidak termasuk well-known port.

    1. Di PC client meremote server: buka file /etc/ssh/sshd_config dengan perintah

    server@debian:/$ nano /etc/ssh/sshd_config

    2. Cari dan beri tanda pagar (#) pada parameter Port 22

    3. Di bawah baris tersebut, tambahkan parameter port baru misalnya Port 34627

    4. Simpan dengan menekan kombinasi tombol Ctrl+X, Y, dan Enter.

    5. Selanjutnya restart SSH pada server

    server@debian:/$ sudo systemctl restart sshd
    ''')

    st.header('Login Tanpa Password (menggunakan public dan private key)')
    st.write('''
    Apabila seorang administrator memiliki banyak server linux yang harus ditangani, maka proses remote access akan lebih mudah dilakukan tanpa password login namun tetap aman. Hal ini dapat dilakukan dengan memanfaatkan fitur keamanan public key pada SSH.

    1. Di PC klien: User harus mengenerate (membentuk) pasangan public key dan private key dengan perintah

    klien@debian:/$ ssh-keygen –t rsa

    Tampilan pada layar

    2. Di PC klien me-remote server: buat sebuah direktori baru bernama .ssh

    klien@debian:/$ ssh server@192.168.1.10 mkdir –p .ssh

    tampilan di layar

    3. Di PC client: Mengupload public key milik client ke server dengan perintah

    klien@debian:/$ ssh-copy-id server@192.168.1.10

    Masukkan password server untuk menyelesaikan proses.

    4. Selanjutnya menonaktifkan autentikasi password pada server.

    server@debian:/$ sudo nano /etc/ssh/sshd_config

    5. Pada file konfigurasi, cari parameter PasswordAuthentication, hilangkan tanda pagar (#) ubah opsi yes menjadi no.

    PasswordAuthentication no

    6. Simpan dengan menekan kombinasi tombol Ctrl+X, Y, dan Enter.

    7. Selanjutnya restart SSH pada server

    server@debian:/$ sudo systemctl restart sshd

    8. Di PC client: Cobalah untuk login ke server, apabila tidak diminta memasukkan password, maka login SSH tanpa menggunakan password telah berhasil.

    9. Di PC client meremote server: Cobalah untuk membuat direktori baru di /home dengan namamu sendiri.
    ''')

    st.header('Membatasi User yang dapat Mengakses Server')
    st.write('''
    Sebaiknya remote access tidak dibuka untuk semua user yang terdaftar pada sistem. Hal ini untuk meminimalisir kemungkinan penyusup yang mendapatkan akun login user biasa dari social engineering atau scanning sederhana.

    1. Di PC client meremote server: buka file /etc/ssh/sshd_config dengan perintah

    server@debian:/$ nano /etc/ssh/sshd_config

    2. Arahkan kursor ke baris paling akhir, tambahkan tulisan AllowUsers diikuti nama user yang diperbolehkan meremote server, setiap nama user dipisahkan dengan spasi. Misal yang diperbolehkan meremote server adalah user bima dan arjuna, maka skripnya adalah

    AllowUsers bima arjuna

    3. Simpan dengan menekan kombinasi tombol Ctrl+X, Y, dan Enter.

    4. Selanjutnya restart SSH pada server

    server@debian:/$ sudo systemctl restart sshd

    5. Cobalah meremote server dengan username yang tidak terdaftar!
    ''')


# url = 'https://www.streamlit.io/'



# components.html("""
#  <head>
#   <meta charset="utf-8">
#   <meta name="viewport" content="width=device-width, initial-scale=1">
#   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
#   <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
#   <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
# </head>
# <body>
# <div class="card mb-3">
#   <img class="card-img-top" src="./src/img/phishing-1.jpg" alt="Card image cap">
#   <div class="card-body">
#     <h5 class="card-title">Card title</h5>
#     <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
#     <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
#   </div>
# </div>
# </body""")
# if st.button('Open browser'):
#     webbrowser.page(url)
