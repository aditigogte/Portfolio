import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Aditi Gogte | Portfolio",
    page_icon="🚀",
    layout="centered"
)

# ----------------------------------------------------
# ADVANCED STYLING LAYER (ISOLATED VARIABLE FIX)
# ----------------------------------------------------
css_style = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght=400;500;600;700&display=swap');

.stApp {
    font-family: 'Inter', sans-serif;
}

.header-container {
    background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%);
    padding: 40px 30px;
    border-radius: 16px;
    color: #FFFFFF;
    margin-bottom: 30px;
}
.main-title { 
    font-size: 40px; 
    font-weight: 700; 
    color: #FFFFFF; 
    margin: 0;
}
.subtitle { 
    font-size: 20px; 
    color: #BFDBFE; 
    margin-top: 8px;
    font-weight: 500;
}

.section-head { 
    font-size: 24px; 
    font-weight: 700; 
    color: #0F172A; 
    margin-top: 40px; 
    margin-bottom: 20px;
    padding-bottom: 8px;
    border-bottom: 2px solid #E2E8F0;
}

.html-card { 
    background-color: #F8FAFC; 
    padding: 24px; 
    border-radius: 12px; 
    border: 1px solid #E2E8F0;
    margin-bottom: 24px;
}

.card-title {
    font-size: 20px;
    font-weight: 600;
    color: #1E3A8A;
    margin-bottom: 6px;
}

.badge-container {
    margin-top: 8px;
    margin-bottom: 12px;
}
.html-badge { 
    display: inline-block; 
    background-color: #EFF6FF; 
    color: #1E40AF; 
    padding: 4px 12px; 
    border-radius: 9999px; 
    margin-right: 6px; 
    margin-bottom: 6px;
    font-size: 13px; 
    font-weight: 600; 
    border: 1px solid #BFDBFE;
}
.tag-title {
    font-size: 14px;
    font-weight: 600;
    color: #475569;
    margin-top: 10px;
}
</style>
"""

# Render the isolated styling variable safely
st.markdown(css_style, unsafe_allowed_html=True)

# ----------------------------------------------------
# HERO BANNER
# ----------------------------------------------------
st.markdown("""
    <div class="header-container">
        <div class="main-title">Hi, I'm Aditi Gogte 👋</div>
        <div class="subtitle">Associate Analyst & MCA (AI/ML) Student</div>
    </div>
""", unsafe_allowed_html=True)

st.write(
    "I specialize in bridging the gap between intelligent data-driven solutions, full-stack development, "
    "and complex enterprise environments. With hands-on experience in workflow optimization and a core focus "
    "on computer vision and automated reasoning, I love building technical tools that deliver immediate impact."
)

# Navigation CTA Buttons
col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("💼 Connect on LinkedIn", "https://linkedin.com/in/aditi-gogte-375a01288")
with col2:
    st.link_button("💻 View GitHub Profile", "https://github.com/aditigogte")
with col3:
    st.link_button("📧 Email Me", "mailto:aditimanojgogte@gmail.com")

# ----------------------------------------------------
# SKILLS SECTION
# ----------------------------------------------------
st.markdown('<div class="section-head">🛠️ Technical Arsenal</div>', unsafe_allowed_html=True)

st.markdown('<div class="tag-title">Languages & Frameworks</div>', unsafe_allowed_html=True)
st.markdown("""
    <div class="badge-container">
        <span class="html-badge">Python</span>
        <span class="html-badge">SQL</span>
        <span class="html-badge">JavaScript</span>
        <span class="html-badge">C</span>
        <span class="html-badge">C++</span>
        <span class="html-badge">HTML5</span>
        <span class="html-badge">CSS3</span>
    </div>
""", unsafe_allowed_html=True)

st.markdown('<div class="tag-title">AI, ML & Data Analytics</div>', unsafe_allowed_html=True)
st.markdown("""
    <div class="badge-container">
        <span class="html-badge">OpenCV</span>
        <span class="html-badge">YOLOv8</span>
        <span class="html-badge">Streamlit</span>
        <span class="html-badge">IBM watsonx.ai</span>
        <span class="html-badge">Business Analytics</span>
        <span class="html-badge">Data Reporting</span>
    </div>
""", unsafe_allowed_html=True)

st.markdown('<div class="tag-title">Cloud Infrastructure & ERP</div>', unsafe_allowed_html=True)
st.markdown("""
    <div class="badge-container">
        <span class="html-badge">AWS Cloud Fundamentals</span>
        <span class="html-badge">API & Web Services</span>
        <span class="html-badge">Workday ERP</span>
        <span class="html-badge">XSLT</span>
        <span class="html-badge">XPath</span>
    </div>
""", unsafe_allowed_html=True)

# ----------------------------------------------------
# PROJECTS SECTION
# ----------------------------------------------------
st.markdown('<div class="section-head">🚀 Featured Projects</div>', unsafe_allowed_html=True)

st.markdown("""
    <div class="html-card">
        <div class="card-title">👁️ AI-Based Smart Surveillance System</div>
        <div style="color: #64748B; font-size: 14px; font-weight: 500; margin-bottom: 12px;">
            Tech Stack: Python, OpenCV, YOLOv8 | Academic Project
        </div>
        <p style="color: #334155; font-size: 15px; line-height: 1.6;">
            Built a real-time computer vision surveillance platform running advanced tracking algorithms and YOLOv8 models for automated human presence monitoring.
        </p>
        <p style="color: #334155; font-size: 15px; line-height: 1.6;">
            • Engineered granular alert generation logic to minimize false-positive anomalies.<br>
            • Structured a secure, high-efficiency evidence storage backend to streamline post-event investigation pipelines.
        </p>
    </div>
""", unsafe_allowed_html=True)

st.markdown("""
    <div class="html-card">
        <div class="card-title">🤖 BobKnows Why - AI Debugger</div>
        <div style="color: #64748B; font-size: 14px; font-weight: 500; margin-bottom: 12px;">
            Tech Stack: Python, Streamlit, IBM watsonx.ai | IBM Hackathon Winner
        </div>
        <p style="color: #334155; font-size: 15px; line-height: 1.6;">
            Developed and successfully packaged an AI co-pilot web application within a high-intensity 48-hour hackathon sprint to completely automate messy software error log analysis.
        </p>
        <p style="color: #334155; font-size: 15px; line-height: 1.6;">
            • Seamlessly integrated a dynamic Streamlit frontend interface with LLM endpoints via the IBM watsonx API.<br>
            • Enabled development teams to capture system exceptions and receive real-time, plain-English bug documentation along with instant syntax updates.
        </p>
    </div>
""", unsafe_allowed_html=True)

# ----------------------------------------------------
# PROFESSIONAL EXPERIENCE
# ----------------------------------------------------
st.markdown('<div class="section-head">💼 Professional Experience</div>', unsafe_allowed_html=True)

st.markdown("**Associate Analyst** | **Deloitte USI** *(Oct 2024 - Mar 2025)*")
st.write(
    "- Operated directly within complex Workday ERP system environments executing configuration updates, "
    "automated process flows, and critical data validation pipelines.\n"
    "- Extracted and generated high-impact analytical reports, tracking down software bugs and maintaining "
    "database accuracy across functional units."
)

st.markdown("---")

# ----------------------------------------------------
# EDUCATION & COMMUNITY (SIDE-BY-SIDE COLUMNS)
# ----------------------------------------------------
col_edu, col_vol = st.columns(2)

with col_edu:
    st.markdown('<div class="section-head" style="margin-top:10px;">🎓 Education</div>', unsafe_allowed_html=True)
    st.markdown("**MCA (AI / ML)**")
    st.write("Ramdeobaba University, Nagpur (Expected 2027) | Score: 70%")
    st.markdown("**B.Sc. in Computer Science**")
    st.write("Dr. Ambedkar College, Nagpur (Graduated 2024) | Score: 69%")

with col_vol:
    st.markdown('<div class="section-head" style="margin-top:10px;">🌱 Impact & Interests</div>', unsafe_allowed_html=True)
    st.markdown("**Volunteer Work**")
    st.write("Dedicated volunteer at *Rise for Tails NGO*, Nagpur since 2020 supporting community animal welfare.")
    st.markdown("**Athletics & Hobbies**")
    st.write("Competitive basketball player, long-distance marathon runner, and basic German language explorer.")