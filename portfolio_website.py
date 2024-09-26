import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyAaiFrAzbrRV22AK2MACwGbefmKonqS7NU")
model = genai.GenerativeModel("gemini-1.5-flash")

col1,col2=st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Swetha Mathu")
with col2:
    st.image("images/img.jpeg")
st.title(" ")
persona="""You are Swetha AI Bot. You help people to know about Swetha.Just Answer 
as if you are responding as me. Here is more info about Swetha:I’m a 3rd-year student at RMK Engineering College, working hard to become an expert in web development with a focus on computer vision. I’m currently learning Python, C++, and web development, while also practicing design skills using Figma. Web development is my main area of focus right now, and I’m building a strong foundation by studying responsive web design on FreeCodeCamp. Alongside that, I’m strengthening my knowledge of programming languages like Python and C++ to eventually integrate artificial intelligence, specifically computer vision, into web applications.

My interest lies in creating innovative web solutions that merge AI-driven capabilities with user-friendly designs. I’m fascinated by how computer vision can transform web experiences, and my goal is to develop web applications that not only look good but can also process and interpret visual data. I believe in project-based learning and constantly push myself to take on new challenges that help me grow both technically and creatively. I'm passionate about continuously improving my coding skills and design thinking and am excited to see how I can contribute to the tech world by combining these two fields.

For me, learning is a journey of consistent effort and curiosity. I enjoy breaking down complex problems and finding smart, efficient solutions. I look forward to deepening my expertise in both web development and AI as I progress and take on new, exciting projects.Currently I do started to learn and explore the world of technology specifically Web Development and Computer Vision technology."""
st.title("Swetha's AI Bot")

user_question=st.text_input("Ask anything about me")
if st.button("ASK",use_container_width=400):
    prompt=persona+"Here is the question that the user asked: "+user_question
    response=model.generate_content(prompt)
    st.write(response.text)

st.title(" ")
col1,col2=st.columns(2)
with col1:
    st.subheader("Exploring Web Dev")
    st.write("Cat Photo App")
    st.write("Cafe Menu")
    st.write("Registration Form")
    st.write("Survey Form")
with col2:
    st.video("https://youtu.be/pVEEy3g82tQ?si=pBgbHnEDUH90IUij")

st.title(" ")
st.title("Glimpse of Learning")
c1,c2,c3,c4=st.columns(4)
with c1:
    st.image("images/m2.jpg")
with c2:
    st.image("images/a3.jpg")
with c3:
    st.image("images/d.jpg")
with c4:
    st.image("images/f.jpg")

st.title(" ")
st.title("My Skills")

st.slider("Programming",0,100,57)
st.slider("HTML",0,100,75)
st.slider("CSS",0,100,60)
st.slider("JavaScript",0,100,30)
st.slider("Figma",0,100,55)

st.title(" ")
st.title("Gallery")
c1,c2,c3=st.columns(3)
with c1:
    st.image("images/g1.jpg")
    st.image("images/g2.jpg")
    st.image("images/g3.jpg")

with c2:
    st.image("images/g4.jpg")
    st.image("images/g5.jpg")
    st.image("images/g6.jpg")
with c3:
    st.image("images/g7.jpg")
    st.image("images/g8.jpg")
    st.image("images/ipo.jpg")
st.write(" ")
st.write("Contact")
st.title("Finally yeah!! I am done with my work of exploring streamlit little bit🎊")
st.write("swet22151.cs@rmkec.ac.in")