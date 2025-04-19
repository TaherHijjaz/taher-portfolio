import streamlit as st
import pandas as pd

st.set_page_config(page_title="Taher Hijjaz Portfolio", layout="wide", page_icon="📊")

# Sidebar navigation
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["Home", "My Journey", "Projects", "Experiences", "Skills", "Career Development", "Reflections"])

# ------------------ HEADER ------------------ #
st.markdown("""
<style>
    .big-font {
        font-size:30px !important;
    }
    /* General layout enhancements */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    /* Header styling */
    h1 {
        font-size: 2.8em;
        font-weight: 700;
        color: #003366;
    }
    h2, h3 {
        color: #004080;
    }
    /* Sidebar accent and visibility fix */
    section[data-testid="stSidebar"] {
        background-color: #f3f6fb;
        color: #000000;
    }
    section[data-testid="stSidebar"] * {
        color: #000000 !important;
    }
    /* Improve caption spacing */
    .css-qrbaxs {
        margin-top: -10px !important;
        font-style: italic;
        color: #555;
    }
</style>
""", unsafe_allow_html=True)

if page == "Home":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("Hi, I am Taher 👋")

        st.markdown("""
        ## A Sophomore at the University of Richmond majoring in Business Administration with a concentration in Finance and Business Analytics

        I was born in Palestine 🇵🇸, raised in Dubai for 14 years, and then immigrated to the United States four and a half years ago. I completed high school in Oklahoma, spent my freshman year at the University of Oklahoma, and then transferred to the University of Richmond — where I’m now in my second semester.

        Outside the classroom, I'm passionate about soccer ⚽ — I follow leagues and players from every corner of the world. I’m proud to contribute to the Palestinian national football team by collecting and visualizing performance data.

        Professionally, I’m keeping my doors open across finance — whether that’s investment banking, wealth management, or quant finance. My goal is to gain experience in the U.S. for the next 5–6 years, then return to Palestine and contribute to rebuilding and growing its economy during these difficult times.

        [Learn More by going to my LinkedIn ➤ ](https://www.linkedin.com/in/taher-hijjaz)
        """)
    with col2:
        st.image("Taher_picture.PNG", caption="Taher Hijjaz", use_container_width=True)

    st.markdown("---")

    # Add interactive map of Taher's journey
    st.markdown("### 🌍 My Global Journey")

    map_data = pd.DataFrame(
        {
            "lat": [31.9522, 25.276987, 35.4676, 37.5407],
            "lon": [35.2332, 55.296249, -97.5164, -77.4360],
        }
    )

    st.map(map_data)
    st.caption("Journey path from Palestine → Dubai → Oklahoma → Richmond")

elif page == "My Journey":
    st.markdown("## 📘 My Journey")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        I began my undergraduate studies at the University of Oklahoma, where I pursued rigorous courses such as Intermediate Financial Accounting and Microeconomic Theory. During my time there, I served as the Financial Controller for the Afghan Student Association, overseeing financial planning for events, collaborating cross-functionally, and forecasting budget allocations.

        However, by the end of my freshman year, I realized that remaining at the University of Oklahoma would not fully support my career aspiration of breaking into Wall Street. As a result, I transferred to the University of Richmond, an institution known for its academic rigor and emphasis on developing both technical and soft skills.

        Since transferring, I have significantly strengthened my technical foundation in finance through courses such as Corporate Finance, Investments, and Fixed Income/Derivatives. I have also enhanced my analytical abilities by taking courses in Data Analysis Software and Machine Learning. Beyond the classroom, I am actively engaged on campus as President of the Arab Student Association and as a consultant for the Lakeside Consulting Group, a student-run organization.

        Outside of academia, I serve as an Assistant Researcher for Sports Interactive, where I analyze and validate player metrics and collaborate with others to ensure accurate data for soccer clubs and players.
        """)
    with col2:
        st.image("images_journey.png", use_container_width=True, caption="Journey from Oklahoma to Richmond",)
    with open("Taher Hijjaz resume copy.pdf", "rb") as file:
        btn = st.download_button(
            label="📄 Download My Resume",
            data=file,
            file_name="Taher Hijjaz resume copy.pdf",
            mime="application/pdf"
        )

elif page == "Projects":
    st.markdown("## 🧠 Projects")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### 1. Nike Investment Teaser")
        st.write("Created a 1-page teaser to raise $100MM in capital for Nike's production & marketing efforts. Included comps, industry analysis, and valuation metrics.")
        st.caption("**Nike Investment Teaser** | Taher Hijjaz | Feb 2025 — Demonstrates skills in corporate finance and equity storytelling.")
        with open("Taher_Hijjaz_DM_Teaser.pdf", "rb") as file:
            st.download_button("📄 Download The Teaser", data=file, file_name="Nike_Teaser.pdf", mime="application/pdf")

        st.markdown("### 2. Costco Stock Report")
        st.write("Analyzed Costco's valuation, financials, and growth drivers using top-down and bottom-up frameworks.")
        st.caption("**Costco Equity Research** | Taher Hijjaz | Feb 2025 — Used macro/industry/company analysis to justify a buy recommendation.")
        with open("COSTCO_Equity_Report_.pdf", "rb") as file:
            st.download_button("📄 Download Costco Report", data=file, file_name="Costco_Report.pdf", mime="application/pdf")

        st.markdown("### 3. TSMC Stock Report")
        st.write("Performed equity research on Taiwan Semiconductor Manufacturing Company. Focused on semiconductor cycles and AI trends.")
        st.caption("**TSMC Equity Research** | Taher Hijjaz | Jan 2025 — Analyzed semiconductor sector, AI chip growth, and financial forecasts.")
        with open("TSM_Stock_Report_Taher_Hijjaz_copy.pdf", "rb") as file:
            st.download_button("📄 Download TSM Report", data=file, file_name="TSM_Report.pdf", mime="application/pdf")

        st.markdown("### 4. MGMT 225 Final Report")
        st.write("Built a business intelligence dashboard and KPI model for a hypothetical e-commerce company using Excel and Tableau.")
        st.caption("**Final Project – Business Analytics** | Taher Hijjaz | May 2024 — Demonstrated data storytelling and dashboard design skills.")
        with open("MGMT_225_Final_Report_copy.pdf", "rb") as file:
            st.download_button("📄 Download MGMT 225 Report", data=file, file_name="MGMT225_Final.pdf", mime="application/pdf")

        st.markdown("### 5. Palestine National Team Analysis")
        st.write("Collected, cleaned, and visualized match data for the Palestinian national football team. Built pass maps and positional plots.")
        st.caption("**Soccer Analytics Project** | Taher Hijjaz | 2024–2025 — Applied Python to help track tactical improvements for Palestine.")
        with open("Palestine_Iraq copy.png", "rb") as file:
            st.download_button("📄 Download Palestine Analysis", data=file, file_name="Palestine_Team_Analysis.pdf", mime="application/pdf")

        st.markdown("### 6. Small Business Financial Analysis")
        st.write("Helped a small business owner in Richmond understand their income statement and cash flow to improve financial planning.")
        st.caption("**Financial Literacy Support** | Taher Hijjaz | Fall 2024 — Provided practical financial statement insights to a local entrepreneur.")
        with open("Project Pep House Deliverable.pptx", "rb") as file:
            st.download_button("📄 Download Business Analysis", data=file, file_name="Small_Business_Analysis.pdf", mime="application/pdf")
        st.image("images_projects.png", caption="Equity & Consulting Work", use_container_width=True)

elif page == "Experiences":
    st.markdown("## 💼 Experiences")
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("### 1. Lakeside Consulting Group – Consultant")
        st.markdown("- Supported an elder care service provider with $30,000 on revenue relocation, profitability, and marketing.")
        st.markdown("- Built an Excel model to capture revenue and costs and presented findings to stakeholders.")
        st.markdown("- Conducted sensitivity analysis to compare base, upside, and downside projections.")

        st.markdown("### 2. Internal Revenue Service – Volunteer Income Tax")
        st.markdown("- Prepared and filed federal and state tax returns for low-income individuals under the IRS VITA program.")
        st.markdown("- Ensured accuracy and compliance with tax laws while maintaining client confidentiality.")
        st.markdown("- Completed IRS certification training on tax law, ethics, and software systems.")

        st.markdown("### 3. Best Food Company – Summer Intern")
        st.markdown("- Shadowed accounting and procurement teams, gaining insight into financial operations and supplier management.")
        st.markdown("- Gained exposure to financial operations with insights into capital markets and supply chain financing.")

    with col_right:
        st.markdown("### 4. Arab Student Association – President")
        st.markdown("- Secured $5,800 in student government funding through formal proposal and presentation.")
        st.markdown("- Fostered cross-cultural dialogue and campus engagement through collaborative initiatives.")

        st.markdown("### 5. Afghan Student Association – Financial Controller")
        st.markdown("- Oversaw financial planning for five events, collaborating cross-functionally and forecasting budget allocations.")
        st.markdown("- Supervised logistics, coordinated events, and fostered community engagement.")

        st.markdown("### 6. Assistant Researcher – Sports Interactive")
        st.markdown("- Validated player stats across 20+ clubs for accuracy and realism.")
        st.markdown("- ➜ Delivered insights that improved game mechanics and tactical depth.")

        st.markdown("### 7. Volunteer Income Tax (Prior Semester)")
        st.markdown("- Delivered personalized tax assistance, prepared returns, and explained IRS compliance.")
        st.markdown("- ➜ Strengthened communication and financial literacy by explaining complex forms to clients.")

        st.markdown("### 8. Potential Internship – Summer 2025")
        st.markdown("- Planning to intern at a real estate investment firm in Houston or a wealth management firm in Switzerland.")

elif page == "Skills":
    st.markdown("## 🛠️ Skills & Certifications")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### Financial and Software Skills")
        st.markdown("""
        - Financial modeling (DCF, LBO, comps), Excel (pivot tables, macros), PowerPoint  
        - Tableau, Python, and R  
        - Knowledgeable in market trends, pricing models, and trading strategies  
        """)

        st.markdown("### Certifications")
        st.markdown("""
        - Bloomberg Market Concepts Certificate  
        - JPMorgan Chase & Co. Quantitative Research Virtual Experience Program Certificate  
        - Citi Investment Banking Virtual Experience Program Certificate  
        """)
    with col2:
        st.image("images_skills_graphic.png", use_container_width=True)
        st.image("images_skills_graphic.png", use_container_width=True)

elif page == "Career Development":
    st.markdown("## 🎯 Career Development Activities")

    st.markdown("### Q-Camp (Jan 24 – 25)")
    st.write("Participated in intensive workshops to develop career readiness, improve networking skills, and understand recruiting timelines.")

    st.markdown("### Job, Internship & Grad School Fair (Feb 6)")
    st.write("Talked with a couple of accounting firms and research groups to explore internship opportunities and learn about their expectations.")

    st.markdown("### Career Services Tour (Feb 13)")
    st.write("Learned about the various career resources available at Richmond, including resume reviews, mock interviews, and employer connections.")

    st.markdown("### LinkedIn Workshop (Pre-Spring Break)")
    st.write("Attended a LinkedIn workshop advertised on Handshake that helped me improve my profile, build a personal brand, and network more effectively.")

    st.markdown("### Cover Letter Draft (Feb 25)")
    st.write("I had already written a cover letter prior to this class, so I didn’t revise it much, but I still found the session valuable as a refresher.")

    st.markdown("### Career Conversations (Mar 20)")
    st.write("Had a couple of conversations with alumni who gave me valuable insights into roles in private equity and investment research.")

    st.markdown("### Resume Ready Approval (Mar 25)")
    st.write("Received Resume Ready approval without any edits. My resume is polished and employer-ready.")

    st.markdown("### Mock Interview (Apr 1)")
    st.write("This was a challenging but necessary experience. I realized mock interviews are one of my weaknesses, and I plan to practice more over the summer.")

    st.markdown("### Career Advising Appointment (Apr 15)")
    st.write("Met with multiple advisors this semester, including Professor Soady and Keith Webb, to discuss goals and next steps.")

elif page == "Reflections":
    st.markdown("## 🔁 Reflections")
    st.write("""
    Each of these experiences and projects has helped shape my path. Through volunteering, consulting, and research, I've built confidence in both client interaction and technical problem-solving. My short-term goal is to gain internship experience in investment banking or equity research. Long-term, I aim to pursue a Master’s in Financial Engineering and work in quantitative finance.

    I’ve also learned how to critique and revise my work more constructively – especially in projects like the Nike teaser or the tax assistance program. These have taught me the value of feedback, iteration, and clarity.
    """)

# ------------------ FOOTER ------------------ #
st.markdown("Made with ❤️ by Taher Hijjaz | Powered by Streamlit")
