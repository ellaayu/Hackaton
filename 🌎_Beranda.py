# Beranda isi : Pembuka

import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from PIL import Image


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
        <img src="https://media.suara.com/pictures/970x544/2020/05/12/29597-phising.jpg" alt="Los Angeles" style="width:100%;">
      </div>

      <div class="item">
        <img src="https://www.dicoding.com/blog/wp-content/uploads/2021/11/Blog-Apa-itu-Phising-Simak-Penjelasan-Lengkapnya.jpg" alt="Chicago" style="width:100%;">
      </div>
    
      <div class="item">
        <img src="https://media.suara.com/pictures/970x544/2020/05/12/29597-phising.jpg" alt="New york" style="width:100%;">
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
    height=400,
)

st.sidebar.success("Ayo ketahui dunia Cyber!")
image = Image.open('./src/img/phishing-1.jpg')
with st.sidebar:
    hello = st.image(image, caption='')

st.markdown('''
# Sections
- [Apa itu Cyber](#section-1)
- [Apa itu Security](#section-2)
''', unsafe_allow_html=True)

st.header('Apa itu Cyber')
st.write('''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet volutpat consequat mauris nunc congue nisi vitae suscipit tellus. Amet mauris commodo quis imperdiet. In metus vulputate eu scelerisque. Facilisis gravida neque convallis a cras semper. Quis vel eros donec ac odio. Posuere urna nec tincidunt praesent semper feugiat nibh sed. Vitae et leo duis ut. Consectetur lorem donec massa sapien faucibus et molestie ac feugiat. Scelerisque varius morbi enim nunc faucibus a. Eget velit aliquet sagittis id consectetur purus ut. Massa eget egestas purus viverra. Libero justo laoreet sit amet cursus sit. Nibh nisl condimentum id venenatis a condimentum vitae sapien.
Dictumst vestibulum rhoncus est pellentesque. Egestas sed tempus urna et pharetra pharetra. Eget est lorem ipsum dolor sit amet consectetur. Tortor pretium viverra suspendisse potenti. Diam maecenas ultricies mi eget mauris pharetra. Ultrices mi tempus imperdiet nulla. Volutpat ac tincidunt vitae semper quis. Viverra accumsan in nisl nisi scelerisque eu. Ut aliquam purus sit amet luctus venenatis lectus magna fringilla. Velit ut tortor pretium viverra suspendisse potenti nullam ac.
Commodo sed egestas egestas fringilla phasellus faucibus scelerisque. Pulvinar mattis nunc sed blandit libero volutpat sed cras. Fringilla est ullamcorper eget nulla. Egestas sed tempus urna et pharetra pharetra massa massa. Nunc vel risus commodo viverra maecenas accumsan lacus. Justo donec enim diam vulputate ut pharetra. Metus aliquam eleifend mi in nulla posuere sollicitudin. Lobortis mattis aliquam faucibus purus. Massa tincidunt dui ut ornare lectus sit amet. Et molestie ac feugiat sed lectus vestibulum. Mattis ullamcorper velit sed ullamcorper. Quam adipiscing vitae proin sagittis nisl rhoncus mattis rhoncus. Pulvinar sapien et ligula ullamcorper malesuada. Orci phasellus egestas tellus rutrum tellus pellentesque. Ut venenatis tellus in metus vulputate eu scelerisque felis imperdiet. Etiam erat velit scelerisque in dictum non consectetur.
''')

st.header('Apa itu Security')
st.write('''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet volutpat consequat mauris nunc congue nisi vitae suscipit tellus. Amet mauris commodo quis imperdiet. In metus vulputate eu scelerisque. Facilisis gravida neque convallis a cras semper. Quis vel eros donec ac odio. Posuere urna nec tincidunt praesent semper feugiat nibh sed. Vitae et leo duis ut. Consectetur lorem donec massa sapien faucibus et molestie ac feugiat. Scelerisque varius morbi enim nunc faucibus a. Eget velit aliquet sagittis id consectetur purus ut. Massa eget egestas purus viverra. Libero justo laoreet sit amet cursus sit. Nibh nisl condimentum id venenatis a condimentum vitae sapien.
Dictumst vestibulum rhoncus est pellentesque. Egestas sed tempus urna et pharetra pharetra. Eget est lorem ipsum dolor sit amet consectetur. Tortor pretium viverra suspendisse potenti. Diam maecenas ultricies mi eget mauris pharetra. Ultrices mi tempus imperdiet nulla. Volutpat ac tincidunt vitae semper quis. Viverra accumsan in nisl nisi scelerisque eu. Ut aliquam purus sit amet luctus venenatis lectus magna fringilla. Velit ut tortor pretium viverra suspendisse potenti nullam ac.
Commodo sed egestas egestas fringilla phasellus faucibus scelerisque. Pulvinar mattis nunc sed blandit libero volutpat sed cras. Fringilla est ullamcorper eget nulla. Egestas sed tempus urna et pharetra pharetra massa massa. Nunc vel risus commodo viverra maecenas accumsan lacus. Justo donec enim diam vulputate ut pharetra. Metus aliquam eleifend mi in nulla posuere sollicitudin. Lobortis mattis aliquam faucibus purus. Massa tincidunt dui ut ornare lectus sit amet. Et molestie ac feugiat sed lectus vestibulum. Mattis ullamcorper velit sed ullamcorper. Quam adipiscing vitae proin sagittis nisl rhoncus mattis rhoncus. Pulvinar sapien et ligula ullamcorper malesuada. Orci phasellus egestas tellus rutrum tellus pellentesque. Ut venenatis tellus in metus vulputate eu scelerisque felis imperdiet. Etiam erat velit scelerisque in dictum non consectetur.
''')

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Kontak Kami
    - Kirim pertanyaan di [Email kami](aaa@gmail.com)
    - Kunjungi konten kami di [Intagram](https://intagram.com)
    - Kunjungi juga [GitHub kami](https://github.com)
"""
)