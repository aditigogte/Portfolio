import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Aditi Gogte | Portfolio",
    page_icon="🚀",
    layout="centered"
)

# ----------------------------------------------------
# HERO SECTION (NATIVE STREAMLIT)
# ----------------------------------------------------
st.title("Hi, I'm Aditi Gogte 👋")
st.subheader("Associate Analyst & MCA (AI/ML) Student")

st.write(
    "I specialize in bridging the gap between intelligent data-driven solutions, full-stack development, "
    "and complex enterprise environments. With hands-on experience in workflow optimization and a core focus "
    "on computer vision and automated reasoning, I love building technical tools that deliver immediate impact."
)

# Connect Buttons (Clean Layout)
col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("💼 Connect on LinkedIn", "https://linkedin.com/in/aditi-gogte-375a01288")
with col2:
    st.link_button("💻 View GitHub Profile", "https://github.com/aditigogte")
with col3:
    st.link_button("📧 Email Me", "mailto:aditimanojgogte@gmail.com")

st.divider()

# ----------------------------------------------------
# TECHNICAL SKILLS
# ----------------------------------------------------
st.header("🛠️ Technical Arsenal")

with st.container(border=True):
    st.markdown("**Languages & Frameworks:**")
    st.caption("Python • SQL • JavaScript • C • C++ • HTML5 • CSS3")

with st.container(border=True):
    st.markdown("**AI, ML & Data Analytics:**")
    st.caption("OpenCV • YOLOv8 • Streamlit • IBM watsonx.ai • Business Analytics • Data Reporting")

with st.container(border=True):
    st.markdown("**Cloud Infrastructure & ERP:**")
    st.caption("AWS Cloud Fundamentals • API & Web Services • Workday ERP • XSLT • XPath")

st.divider()

# ----------------------------------------------------
# FEATURED PROJECTS
# ----------------------------------------------------
st.header("🚀 Featured Projects")

# Project 1
with st.container(border=True):
    st.subheader("👁️ AI-Based Smart Surveillance System")
    st.markdown("*Tech Stack: Python, OpenCV, YOLOv8 | Academic Project*")
    st.write(
        "Built a real-time computer vision surveillance platform running advanced tracking algorithms "
        "and object detection modules for automated human presence monitoring."
    )
    st.write("• Engineered granular alert generation logic to minimize false-positive anomalies.")
    st.write("• Structured a secure, high-efficiency evidence storage backend to streamline post-event investigation pipelines.")

# Project 2
with st.container(border=True):
    st.subheader("🤖 BobKnows Why - AI Debugger")
    st.markdown("*Tech Stack: Python, Streamlit, IBM watsonx.ai | IBM Hackathon Winner*")
    st.write(
        "Developed and successfully packaged an AI co-pilot web application within a high-intensity 48-hour hackathon sprint "
        "to completely automate messy software error log analysis."
    )
    st.write("• Seamlessly integrated a dynamic Streamlit frontend interface with LLM endpoints via the IBM watsonx API.")
    st.write("• Enabled development teams to capture system exceptions and receive real-time, plain-English bug documentation along with instant syntax updates.")

st.divider()

# ----------------------------------------------------
# PROFESSIONAL EXPERIENCE
# ----------------------------------------------------
st.header("💼 Professional Experience")

with st.container(border=True):
    st.markdown("**Associate Analyst** | *Deloitte USI* (Oct 2024 - Mar 2025)")
    st.write(
        "• Operated directly within complex Workday ERP system environments executing configuration updates, "
        "automated process flows, and critical data validation pipelines."
    )
    st.write(
        "• Extracted and generated high-impact analytical reports, tracking down software bugs and maintaining "
        "impeccable database accuracy across functional units."
    )

st.divider()

# ----------------------------------------------------
# EDUCATION & COMMUNITY (SIDE-BY-SIDE COLUMNS)
# ----------------------------------------------------
col_edu, col_vol = st.columns(2)

with col_edu:
    st.header("🎓 Education")
    with st.container(border=True):
        st.markdown("**MCA (AI / ML)**")
        st.write("Ramdeobaba University, Nagpur")
        st.caption("Expected 2027 | Score: 70%")
    
    with st.container(border=True):
        st.markdown("**B.Sc. in Computer Science**")
        st.write("Dr. Ambedkar College, Nagpur")
        st.caption("Graduated 2024 | Score: 69%")

with col_vol:
    st.header("🌱 Impact & Interests")
    with st.container(border=True):
        st.markdown("**Volunteer Work**")
        st.write("Dedicated volunteer at *Rise for Tails NGO*, Nagpur since 2020 supporting community animal welfare.")
        
    with st.container(border=True):
        st.markdown("**Athletics & Hobbies**")
        st.write("Competitive basketball player, long-distance marathon runner, and basic German language explorer.")