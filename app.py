import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Aditi Gogte | Portfolio",
    page_icon="🚀",
    layout="centered"
)

# ----------------------------------------------------
# HERO HEADER
# ----------------------------------------------------
st.title("Hi, I'm Aditi Gogte 👋")
st.caption("🚀 Associate Analyst & MCA (AI/ML) Student")

st.write(
    "I specialize in bridging the gap between intelligent data-driven solutions, full-stack development, "
    "and complex enterprise environments. With hands-on experience in workflow optimization and a core focus "
    "on computer vision and automated reasoning, I love building technical tools that deliver immediate impact."
)

# Interactive Contact Rows
col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("💼 Connect on LinkedIn", "https://linkedin.com/in/aditi-gogte-375a01288")
with col2:
    st.link_button("💻 View GitHub Profile", "https://github.com/aditigogte")
with col3:
    st.link_button("📧 Email Me", "mailto:aditimanojgogte@gmail.com")

st.divider()

# ----------------------------------------------------
# HIGH-FIDELITY NAVIGATION TABS (Smooth UX Transition)
# ----------------------------------------------------
# This organizes your profile cleanly, loading layouts with smooth native fade animations.
tab_projects, tab_skills, tab_experience, tab_about = st.tabs([
    "🚀 Featured Projects", 
    "🛠️ Technical Arsenal", 
    "💼 Experience & Education",
    "🌱 Impact & Interests"
])

# ----------------------------------------------------
# TAB 1: PROJECTS (Interactive Cards + Expanders)
# ----------------------------------------------------
with tab_projects:
    st.markdown("### Highlighted Engineering Work")
    
    # Project 1 Card
    with st.container(border=True):
        st.subheader("👁️ AI-Based Smart Surveillance System")
        st.caption("**Tech Stack:** Python • OpenCV • YOLOv8 | *Academic Project*")
        st.write(
            "Built a real-time computer vision surveillance platform running advanced tracking algorithms "
            "and object detection modules for automated human presence monitoring."
        )
        # Expander for a clean accordion style interaction
        with st.expander("🔍 View Technical Implementation Details"):
            st.write("• Engineered granular alert generation logic to minimize false-positive anomalies.")
            st.write("• Structured a secure, high-efficiency evidence storage backend to streamline post-event investigation pipelines.")
            st.info("Key Focus: Real-time image matrix manipulation and inference latency minimization.")

    # Project 2 Card
    with st.container(border=True):
        st.subheader("🤖 BobKnows Why - AI Debugger")
        st.caption("**Tech Stack:** Python • Streamlit • IBM watsonx.ai | *IBM Hackathon Winner*")
        st.write(
            "Developed and successfully packaged an AI co-pilot web application within a high-intensity 48-hour hackathon sprint "
            "to completely automate messy software error log analysis."
        )
        with st.expander("🔍 View Technical Implementation Details"):
            st.write("• Seamlessly integrated a dynamic Streamlit frontend interface with LLM endpoints via the IBM watsonx API.")
            st.write("• Enabled development teams to capture system exceptions and receive real-time, plain-English bug documentation along with instant syntax updates.")
            st.success("🏆 Awarded 1st Place during the collaborative enterprise platform sprint.")

# ----------------------------------------------------
# TAB 2: TECHNICAL ARSENAL (Metrics + Split Columns)
# ----------------------------------------------------
with tab_skills:
    st.markdown("### Core Capabilities")
    
    # Interactive Metrics Rows
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    metric_col1.metric(label="Core Languages", value="7+", delta="Fluent")
    metric_col2.metric(label="AI Frameworks", value="YOLO / OpenCV", delta="Vision")
    metric_col3.metric(label="Enterprise Tools", value="Workday ERP", delta="Optimized")
    
    st.markdown("---")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        with st.container(border=True):
            st.markdown("**💻 Languages & Frameworks**")
            st.write("Python • SQL • JavaScript • C • C++ • HTML5 • CSS3")
            
        with st.container(border=True):
            st.markdown("**🤖 AI & Data Analytics**")
            st.write("OpenCV • YOLOv8 • Streamlit • IBM watsonx.ai • Business Analytics")
            
    with col_right:
        with st.container(border=True):
            st.markdown("**☁️ Cloud & Architecture**")
            st.write("AWS Cloud Fundamentals • API Infrastructure • Web Services")
            
        with st.container(border=True):
            st.markdown("**⚙️ ERP & Data Pipelines**")
            st.write("Workday ERP • XSLT Transformations • XPath Queries • Reporting")

# ----------------------------------------------------
# TAB 3: EXPERIENCE & EDUCATION (Timeline Style)
# ----------------------------------------------------
with tab_experience:
    st.markdown("### Career Roadmap")
    
    # Work Experience Segment
    st.markdown("#### 💼 Professional Milestones")
    with st.container(border=True):
        st.markdown("**Associate Analyst** | *Deloitte USI*")
        st.caption("Timeline: Oct 2024 - Mar 2025")
        st.write(
            "• Operated directly within complex Workday ERP system environments executing configuration updates, "
            "automated process flows, and critical data validation pipelines."
        )
        st.write(
            "• Extracted and generated high-impact analytical reports, tracking down software bugs and maintaining "
            "impeccable database accuracy across functional units."
        )

    # Education Segment
    st.markdown("#### 🎓 Academic Profile")
    edu_col1, edu_col2 = st.columns(2)
    with edu_col1:
        with st.container(border=True):
            st.markdown("**MCA (AI / ML)**")
            st.write("Ramdeobaba University, Nagpur")
            st.caption("Expected 2027 | Current Score: 70%")
            
    with edu_col2:
        with st.container(border=True):
            st.markdown("**B.Sc. in Computer Science**")
            st.write("Dr. Ambedkar College, Nagpur")
            st.caption("Graduated 2024 | Final Score: 69%")

# ----------------------------------------------------
# TAB 4: IMPACT & INTERESTS (Personal Highlights)
# ----------------------------------------------------
with tab_about:
    st.markdown("### Beyond the Code")
    
    col_vol, col_hob = st.columns(2)
    
    with col_vol:
        with st.container(border=True):
            st.markdown("#### 🌱 Community Impact")
            st.write("**Volunteer Work**")
            st.write("Dedicated volunteer at *Rise for Tails NGO*, Nagpur since 2020 supporting community animal welfare.")
            
    with col_hob:
        with st.container(border=True):
            st.markdown("#### 🏀 Personal Hobbies")
            st.write("• Competitive Basketball Player")
            st.write("• Long-distance Marathon Runner")
            st.write("• Conversational German Language Learner")