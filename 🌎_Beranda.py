# Beranda isi : Pembuka

import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
import pandas as pd
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from PIL import Image
import numpy as np
import sklearn


# with st.sidebar:
#     selected = option_menu(
#         menu_title="Main Menu",
#         options=["Home", "Projects", "Contact"],
#     )

# if selected=="Home":
#     st.title("Home")
# if selected=="Projects":
#     st.title("Projects")
# if selected=="Contact":
#     st.title("Contact")


st.set_page_config(
    page_title="Beranda",
    page_icon="🌎",
    menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
)

st.write("# Welcome to CyberBook! 👋")

st.caption('“Cyber-Security is much more than a matter of IT.” ― Stephane Nappo.')

components.html(
    """
    <head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>

<div class="container">
  <div id="myCarousel" class="carousel slide" data-ride="carousel">
    <!-- Indicators -->
    <ol class="carousel-indicators">
      <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
      <li data-target="#myCarousel" data-slide-to="1"></li>
      <li data-target="#myCarousel" data-slide-to="2"></li>
    </ol>

    <!-- Wrapper for slides -->
    <div class="carousel-inner">
      <div class="item active">
        <img src="https://commercial.acerid.com/assets/images/medias/20210204093324_Cybersecurity-Banner.jpg" alt="Los Angeles" style="width:100%;">
      </div>

      <div class="item">
        <img src="https://www.dicoding.com/blog/wp-content/uploads/2021/11/Blog-Apa-itu-Phising-Simak-Penjelasan-Lengkapnya.jpg" alt="Chicago" style="width:100%;">
      </div>
    
      <div class="item">
        <img src="https://binus.ac.id/wp-content/uploads/2020/10/43-0-Kupas-Tuntas-Jurusan-Cyber-Security.-Belajar-Apa-Saja-sih-di-Kampus.jpg" alt="New york" style="width:100%;">
      </div>
    </div>

    <!-- Left and right controls -->
    <a class="left carousel-control" href="#myCarousel" data-slide="prev">
      <span class="glyphicon glyphicon-chevron-left"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="right carousel-control" href="#myCarousel" data-slide="next">
      <span class="glyphicon glyphicon-chevron-right"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>
</div>

</body>""",
    height=300,
)

st.sidebar.success("Ayo ketahui dunia Cyber!")

st.header('Apa itu Cyber Security?')
st.write('''
  Cyber security adalah aktivitas yang dilakukan sistem atau seseorang dalam rangka melindungi sistem komputer dari serangan. Biasanya serangan tersebut bersifat ilegal.

  Jika mengacu pada International Telecommunication Unit (ITU), cyber security adalah aktivitas yang meliputi kebijakan dan konsep keamanan dan berfungsi melindungi aset organisasi.

  Perlindungan dapat berupa perangkat lunak (software), aplikasi atau apa pun yang berhubungan dengan sistem komputer. Sehingga, dengan menggunakan keamanan siber, perusahaan dapat menanggulangi ancaman di sistem komputer.

  Konsep Cyber Security
  Ada tiga konsep untuk memahami cyber security yaitu confidentiality (kerahasiaan), integrity (integritas), dan availability (ketersediaan) informasi. Untuk mengetahui lebih lengkap, simak penjelasannya di bawah ini.

  1. Kerahasiaan
  Konsep yang pertama adalah kerahasiaan. Maksudnya adalah membatasi akses dan hanya diperuntukkan orang-orang tertentu. Hal ini penting dilakukan agar di kemudian hari tidak terjadi kebocoran data. Misal, hanya orang-orang tertentu yang bisa mengakses laporan keuangan. Sedangkan lainnya, tidak.

  Satu hal yang penting dari kerahasiaan adalah mengaktifkan two factor authentication (2FA). Jadi, ketika hendak mengakses akun tertentu harus melewati dua proses. Pertama, masuk melalui password. Kedua, masuk melalui kode khusus yang dikirim ke piranti tertentu.

  2. Integritas
  Konsep kedua adalah integritas. Maksudnya, menyampaikan informasi yang benar, tepat, dan akurat kepada publik. Selain menyimpan informasi, perusahaan perlu menjaga data yang dimiliki pengguna. Jangan sampai hal tersebut bocor ke pihak-pihak yang tidak berkepentingan.

  Cara untuk menghindari kebocoran data seperti enkripsi, tanda tangan digital, atau certificate authority (CA).

  3. Ketersediaan
  Konsep ketiga adalah siap sedia. Maksudnya, jangan sampai pelanggan kecewa dengan sistem yang Anda atau perusahaan miliki. Misal, perusahaan Anda berbasis aplikasi keuangan. TIba-tiba, aplikasi keuangan sedang macet dan tidak tertangani dalam kurun waktu tertentu. Hal ini dapat membuat pelanggan berpindah ke kompetitor.
''')



st.sidebar.markdown(
    """
    Ketahui apa saja yang dapat terjadi di dunia Cyber.
    ### Kontak Kami 👈
    - Kirim pertanyaan di [Email kami](aaa@gmail.com)
    - Kunjungi konten kami di [Intagram](https://intagram.com)
    - Kunjungi juga [GitHub kami](https://github.com)
"""
)

st.header('Kerugian yang ditimbulkan Cyber Security Attack')

@st.cache
def get_UN_data():
    AWS_BUCKET_URL = "./src/file"
    df = pd.read_csv(AWS_BUCKET_URL + "/crime.csv")
    return df.set_index("Crime")


try:
    df = get_UN_data()
    countries = st.multiselect(
        "", list(df.index), ["Malware", "Phising", "Serangan Berbasis Web", 
        "Ransomware"]
    )
    if not countries:
        st.error("Please select at least one country.")
    else:
        data = df.loc[countries]
        data /= 1000000.0
        st.write("### Kerugian terhadap Cyber Crime Attack (US$)", data.sort_index())

        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(
            columns={"index": "year", "value": "Kerugian terhadap Cyber Crime Attack (US$)"}
        )
        chart = (
            alt.Chart(data)
            .mark_area(opacity=0.3)
            .encode(
                x="year:T",
                y=alt.Y("Kerugian terhadap Cyber Crime Attack (US$):Q", stack=None),
                color="Crime:N",
            )
        )
        st.altair_chart(chart, use_container_width=True)
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )