import streamlit as st
from send_email import send_email

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    col11, col12, col13 = st.columns([3, 20, 3])
    with col11:
        st.write("")
    with col12:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.image("images/photo.png", use_column_width='auto')
    with col13:
        st.write("")

with col2:
    st.header("Welcome!")
    content = """
    My name is Konstantin and I am delighted to welcome you on my personal web site.\n
    It is my first web project that was created as a part of python education course.\n
    Some projects are still under development, but you are able
    to check first of them and contact me via a special form available in the sidebar.\n
    
    KK
    """
    # st.write(content)
    st.info(content)


with st.expander("Quick Bio"):
    tab1, tab2, tab3, tab4 = st.tabs(["Education", "Experience", "Additional", "Download"])
    with tab1:
        st.subheader('Education')
        col3, col4, col5 = st.columns([1, 4, 1])
        with col3:
            st.write('2021<br><br>', unsafe_allow_html=True)
            st.write('2013 – 2014<br><br>', unsafe_allow_html=True)
            st.write('2010 – 2013<br><br>', unsafe_allow_html=True)
            st.write('2009 – 2013')
        with col4:
            st.write('CFA INSTITUTE<br>'
                     'Chartered Financial Analyst',
                     unsafe_allow_html=True)
            st.write("FORDHAM UNIVERSITY, GRADUATE SCHOOL OF BUSINESS ADMINISTRATION<br>"
                     "MSc program, Business Enterprise", unsafe_allow_html=True)
            st.write('UNIVERSITY OF LONDON, EXTERNAL PROGRAM<br>'
                     'BSc Economics and Finance', unsafe_allow_html=True)
            st.write('HIGHER SCHOOL OF ECONOMICS<br> INTERNATIONAL COLLEGE OF ECONOMICS AND FINANCE<br>'
                     'BSc Economics', unsafe_allow_html=True)
        with col5:
            st.write('Moscow<br><br>', unsafe_allow_html=True)
            st.write('New York<br><br>', unsafe_allow_html=True)
            st.write('Moscow<br><br>', unsafe_allow_html=True)
            st.write('Moscow')
    with tab2:
        st.subheader('Experience')
        col6, col7, col8 = st.columns([1, 4, 1])
        with col6:
            st.write('<br>October 2021<br><br><br>'
                     'May 2019<br> - <br>October 2021<br><br>'
                     'June 2015<br> - <br>May 2019<br><br>',
                     unsafe_allow_html=True)
        with col7:
            st.write('<b>THE CENTRAL BANK OF THE RUSSIAN FEDERATION</b><br>'
                     'MARKET OPERATIONS DEPARTMENT<br>'
                     'Fixed Income Trader<br><br>'
                     'MARKET OPERATIONS DEPARTMENT<br>'
                     'Lead analyst at pledge facility formation division<br><br><br>'
                     f'COLLECTIVE INVESTMENT AND TRUST MANAGEMENT DEPARTMENT<br>'
                     'Lead expert',
                     unsafe_allow_html=True)
        with col8:
            st.write('<br>Moscow<br><br><br>'
                     'Moscow<br><br><br><br>'
                     'Moscow',
                     unsafe_allow_html=True)
    with tab3:
        st.subheader('Additional')
        col9, col10 = st.columns([1, 5])
        with col9:
            st.write('Membership<br><br>'
                     'Certificates<br><br><br><br>',
                     unsafe_allow_html=True)
        with col10:
            st.write('CFA Russia Association Board Member<br><br>'
                     'Python for Finance: Investment Fundamentals & Data Analytics (Udemy - Online Courses)<br>'
                     'The Python Mega Course: Learn Python in 60 Days with 20 Apps (Udemy - Online Courses)<br>',
                     unsafe_allow_html=True)
    with tab4:
        st.subheader('Download resume')
        st.write('You can download full pdf resume by clicking the button below')
        st.write("Please also be informed that you can send me a direct email through a special form "
                 "available in the sidebar.")
        with open('Konstantin_Kostyukov_resume_2023.pdf', 'rb') as resume_file:
            button = st.download_button('Download resume', resume_file,
                               file_name='Konstantin_Kostyukov_resume_2023.pdf',
                               key='download')
        if button:
            st.write("Thanks for downloading, let's be in touch!")
            send_email('Your resume was downloaded')


