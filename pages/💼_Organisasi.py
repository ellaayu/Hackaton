# Oraganisasi yang terlibat di dunia Cyber

import streamlit as st
import streamlit.components.v1 as components
import webbrowser

st.set_page_config(
    page_title="Organisasi",
    page_icon="💼",
    menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
)


url_CISCO = 'https://www.cisco.com/'
url_ITU = 'https://ictfootprint.eu/fr/node/615'
url_GroupIB = 'https://www.group-ib.com/'
url_CDC = 'https://www.cdc.gov/'
url_GCA = 'https://globalcybersecurity.ch/'



components.html("""
 <head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>
<div class="card mb-3">
  <img class="card-img-top" src="https://1000logos.net/wp-content/uploads/2016/11/Cisco-logo.jpg" 
  alt="Card image cap" height="90" width=200">
  <div class="card-body">
    <h4 class="card-title">CISCO</h5>
    <p class="card-text">Cisco mengembangkan, memproduksi, dan menjual perangkat keras jaringan, perangkat lunak jaringan.</p>
  </div>
</div>
</body""")
if st.button('Kunjungi CISCO'):
    webbrowser.open_new_tab(url_CISCO)

components.html("""
 <head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>
<div class="card mb-3">
  <img class="card-img-top" src="data:image/jpeg;base64,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" 
  alt="Card image cap" height="90" width=200">
  <div class="card-body">
    <h4 class="card-title"> International Telecommunication Union (ITU)</h5>
    <p class="card-text">Organisasi internasional yang didirikan untuk membakukan dan meregulasi radio internasional.</p>
    <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
  </div>
</div>
</body""")
if st.button('Kunjungi ITU'):
    webbrowser.open_new_tab(url_ITU)

components.html("""
 <head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>
<div class="card mb-3">
  <img class="card-img-top" src="https://globalcybersecurity.ch/wp-content/uploads/2021/03/GCA_websitelogo-3.png" 
  alt="Card image cap" height="90" width=200">
  <div class="card-body">
    <h4 class="card-title">Global Cybersecurity Association (GCA)</h5>
    <p class="card-text">Not-for-profit cybersecurity association in Zürich, Switzerland.</p>
  </div>
</div>
</body""")
if st.button('Kunjungi GCA'):
    webbrowser.open_new_tab(url_GCA)

components.html("""
 <head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>
<div class="card mb-3">
  <img class="card-img-top" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0JT3eH1Shh0npx2dVBs9NHp4IH9SMmrFjgg&usqp=CAU" 
  alt="Card image cap" height="90" width=200">
  <div class="card-body">
    <h4 class="card-title">Group-IB</h5>
    <p class="card-text">Global leaders in providing high‑fidelity Threat Intelligence and anti‑fraud solutions.</p>
  </div>
</div>
</body""")
if st.button('Kunjungi Group-IB'):
    webbrowser.open_new_tab(url_GroupIB)

components.html("""
 <head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>
<div class="card mb-3">
  <img class="card-img-top" src="https://images.glints.com/unsafe/180x0/glints-dashboard.s3.amazonaws.com/company-logo/a437aa91e6b2f2191ceb0e3bb765c4c2.jpg" 
  alt="Card image cap" height="90" width=200">
  <div class="card-body">
    <h4 class="card-title">Cyber Data Center (cdc) International</h5>
    <p class="card-text">Data center managed by PT Media Nusantara Data Global which provide facilities.</p>
    <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
  </div>
</div>
</body""")
if st.button('Kunjungi CDC'):
    webbrowser.open_new_tab(url_CDC)
    