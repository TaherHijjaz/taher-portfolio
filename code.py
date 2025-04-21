import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1 {
        font-size: 2.8em;
        font-weight: 700;
        color: #003366;
    }
    h2, h3 {
        color: #004080;
    }
    section[data-testid="stSidebar"] {
        background-color: #f3f6fb;
        color: #000000;
    }
    section[data-testid="stSidebar"] * {
        color: #000000 !important;
    }
    .css-qrbaxs {
        margin-top: -10px !important;
        font-style: italic;
        color: #555;
    }
</style>
""", unsafe_allow_html=True)

# --- Helper function for historical stock display ---
def display_historical_stock(name, ticker_symbol, start_date):
    ticker = yf.Ticker(ticker_symbol)
    hist = ticker.history(start=start_date)

    if hist.empty:
        st.warning(f"No historical data for {name} starting from {start_date}.")
        return

    latest_price = hist["Close"].iloc[-1]
    open_price = hist["Open"].iloc[0]
    pct_change = ((latest_price - open_price) / open_price) * 100

    col1, col2 = st.columns([1, 1], gap="medium")
    with col1:
        st.markdown(f"### {name} Stock Report")
        st.write(f"Market performance since {start_date} and investment thesis.")
        st.caption(f"**{name} Equity Research** | Taher Hijjaz")

        if name == "Nike":
            with open("Taher_Hijjaz_DM_Teaser.pdf", "rb") as file:
                st.download_button("📄 Download Nike Teaser", data=file, file_name="Nike_Teaser.pdf", mime="application/pdf")
        elif name == "Costco":
            with open("COSTCO_Equity_Report_.pdf", "rb") as file:
                st.download_button("📄 Download Costco Report", data=file, file_name="Costco_Report.pdf", mime="application/pdf")
        elif name == "TSMC":
            with open("TSM_Stock_Report_Taher_Hijjaz_copy.pdf", "rb") as file:
                st.download_button("📄 Download TSM Report", data=file, file_name="TSM_Report.pdf", mime="application/pdf")

    with col2:
        st.metric(label=f"{name} Return (since {start_date})", value=f"${latest_price:.2f}", delta=f"{pct_change:+.2f}%")
        fig, ax = plt.subplots(figsize=(4, 2))
        ax.plot(hist.index, hist["Close"], linewidth=1.5)
        ax.set_title(f"{ticker_symbol} – Since {start_date}", fontsize=10)
        ax.tick_params(labelsize=8)
        ax.grid(True, linestyle='--', alpha=0.3)
        ax.xaxis.set_major_locator(plt.MaxNLocator(5))
        fig.autofmt_xdate()
        st.pyplot(fig)

# Pages
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
    st.markdown("### 🌍 My Global Journey")
    map_data = pd.DataFrame({"lat": [31.9522, 25.276987, 35.4676, 37.5407], "lon": [35.2332, 55.296249, -97.5164, -77.4360]})
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
        st.image("images_journey.png", use_container_width=True, caption="Journey from Oklahoma to Richmond")

    with open("Taher Hijjaz resume copy.pdf", "rb") as file:
        st.download_button(label="📄 Download My Resume", data=file, file_name="Taher_Hijjaz_Resume.pdf", mime="application/pdf")

elif page == "Projects":
    st.markdown("## 🧠 Projects + Stock Performance")
    st.caption("Charts and metrics since relevant research dates.")

    display_historical_stock("Nike", "NKE", "2025-02-17")
    display_historical_stock("Costco", "COST", "2025-02-10")
    display_historical_stock("TSMC", "TSM", "2025-02-23")

    # MGMT 225
    st.markdown("### 4. MGMT 225 Final Report")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("Built a business intelligence dashboard and KPI model...")
        with open("MGMT_225_Final_Report_copy.pdf", "rb") as file:
            st.download_button("📄 Download MGMT 225 Report", data=file, file_name="MGMT225_Final.pdf", mime="application/pdf")
    with col2:
        st.image("data_picture.jpeg", caption="BI Dashboard Project", use_container_width=True)

    # Palestine Football
    st.markdown("### 5. Palestine National Team Analysis")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("Collected and visualized match data for the Palestinian team...")
    with col2:
        st.image("pfa.png", caption="Match Data Analysis", use_container_width=True)

    with open("Palestine_Iraq copy.png", "rb") as file:
        st.download_button("📄 Download Palestine Analysis", data=file, file_name="Palestine_Iraq copy.png",
                           mime="application/pdf")

    # Small Business
    st.markdown("### 6. Small Business Financial Analysis")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("Helped a Richmond business understand financials and cash flow...")
    with col2:
        st.image("EPC.png", caption="Financial Planning Presentation", use_container_width=True)

    with open("Project Pep House Deliverable.pptx", "rb") as file:
        st.download_button("📄 Download Analysis", data=file, file_name="Project Pep House Deliverable.pptx",
                           mime="application/pdf")

elif page == "Experiences":
    st.markdown("## 💼 Experiences")

    # 1. Lakeside Consulting Group
    st.markdown("### Lakeside Consulting Group – Consultant")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
As a consultant for Lakeside Consulting Group, I led financial analysis for an elder care startup, helping them evaluate pricing strategies and market entry plans. I collaborated with a cross-functional team to build financial projections and present actionable recommendations to the client.
        """)
    with col2:
        st.image("LCG.png", caption="Startup Consulting Engagement", use_container_width=True)

    # 2. VITA
    st.markdown("### Internal Revenue Service – VITA Volunteer")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
Through the Volunteer Income Tax Assistance (VITA) program, I helped prepare over 50 tax returns for low-income individuals and families. I developed strong technical knowledge in tax law, while building communication skills to explain complex forms and credits in a simple way.
        """)
    with col2:
        st.image("IRS.png", caption="VITA Tax Preparation", use_container_width=True)

    # 3. Best Food Company
    st.markdown("### Best Food Company – Intern")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
I interned in the operations department of Best Food Company, a multinational food supplier. I observed the procurement and distribution process while helping streamline order tracking systems to reduce fulfillment delays.
        """)
    with col2:
        st.image("BFC.png", caption="Supply Chain Exposure", use_container_width=True)

    # 4. Arab Student Association
    st.markdown("### Arab Student Association – President")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
As President of the Arab Student Association at the University of Richmond, I led cultural and educational programming. I organized events such as Dabke Night and cultural workshops, while successfully securing $5,800 in student government funding.
        """)
    with col2:
        st.image("ASA.png", caption="Arab Culture Night", use_container_width=True)

    # 5. Afghan Student Association
    st.markdown("### Afghan Student Association – Financial Controller")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
During my time at the University of Oklahoma, I served as Financial Controller for the Afghan Student Association. I managed budgeting, collaborated with event coordinators, and ensured transparent financial reporting to university administrators.
        """)
    with col2:
        st.image("ASAA.png", caption="Cultural Fund Management", use_container_width=True)

    # 6. Sports Interactive
    st.markdown("### Sports Interactive – Assistant Researcher")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
I contribute to the Football Manager video game as an Assistant Researcher for Palestine. I scout and input real-world player data — such as positions, attributes, and club affiliations — to help maintain accuracy and authenticity in the game.
        """)
    with col2:
        st.image("SI.png", caption="Football Data Research", use_container_width=True)


elif page == "Skills":
    st.markdown("## 🛠️ Skills & Certifications")

    # --- Technical Skills ---
    st.markdown("### ⚙️ Technical Skills")

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("#### 💼 Finance & Analytics")
        st.write("""
- **Financial Modeling**: DCF, LBO, Comparable Company Analysis  
- **Market Knowledge**: Derivatives, Fixed Income, Equities  
- **Data Analysis**: Tableau, Excel (Advanced), Power BI
        """)

    with col2:
        st.markdown("#### 🧠 Programming & Tools")
        st.write("""
- **Languages**: Python (Pandas, NumPy, Scikit-learn, Streamlit)  
- **Visualization**: Matplotlib, Seaborn, Plotly  
- **Version Control**: Git & GitHub
        """)

    st.markdown("---")

    # --- Certifications ---
    st.markdown("### 🎓 Certifications")
    cert_cols = st.columns(3)

    certs = {
        "Bloomberg Market Concepts (BMC)": "📊",
        "Citi Investment Banking Virtual Experience": "🏦",
        "JPMorgan Quantitative Research Virtual Experience": "📈"
    }

    for (cert, emoji), col in zip(certs.items(), cert_cols):
        with col:
            st.markdown(f"{emoji} **{cert}**")

    st.markdown("---")

    # --- Soft Skills ---
    st.markdown("### 💬 Interpersonal Skills")
    st.write("""
- Public speaking & presentation delivery  
- Project management and team leadership  
- Cross-cultural collaboration  
- Adaptability and growth mindset
    """)



elif page == "Career Development":
    st.markdown("## 🎯 Career Development Activities")

    # 1. Q-camp
    st.markdown("### Q-Camp (January 24-25)")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
Q-Camp was an intensive two-day professional development bootcamp organized by the Robins School of Business. It included resume and LinkedIn critiques, employer panels, mock networking, and interactive workshops that helped me refine my approach to career planning. I received direct feedback from recruiters and alumni on how to confidently present my experiences in interviews and elevator pitches.

What stood out the most was the opportunity to practice real-time networking with professionals across consulting, banking, and corporate finance. These conversations pushed me to think beyond my resume and focus on the story I’m telling through my goals, body language, and tone. Q-Camp helped me feel more prepared for career fairs, interviews, and informational calls throughout the semester.
        """)
    with col2:
        st.image("Q-camp.png", caption="Q-camp", use_container_width=True)

    # 2. Job, Internship, and Graduate School Fair
    st.markdown("### Job, Internship, and Graduate School Fair (Feb 6)")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
At the fair, I explored opportunities in finance, consulting, and non-profit work. I engaged in meaningful conversations with recruiters from firms like AlphaSights and CapTech, which helped me clarify what I’m seeking in a summer internship.

It also gave me a chance to refine my pitch. I walked away with company contacts and a better understanding of which types of roles align with my goals in finance and data analytics.
        """)
    with col2:
        st.image("CF.png", caption="Meeting Employers at the Fair", use_container_width=True)

    # 3. Career Services Tour
    st.markdown("### Career Services Tour (Feb 13)")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
Touring Career Services helped me discover the range of tools available to students, from resume feedback to mock interviews and one-on-one advising. I learned about drop-in hours and how to schedule targeted coaching sessions.

The space itself made me feel more welcomed and encouraged to return for help throughout the semester. The staff walked us through different ways to build a career plan and make use of Handshake effectively.
        """)
    with col2:
        st.image("HS.png", caption="Touring the Career Center", use_container_width=True)

    # 4. Handshake Event
    st.markdown("### LinkedIn Workshop (Attended via Handshake – Before Spring Break)")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
I attended a LinkedIn strategy workshop promoted on Handshake that focused on building a professional online presence. The facilitator walked us through how to optimize each section of our profiles — from writing a strong headline and summary to showcasing experiences and skills with clarity. I learned how recruiters use LinkedIn filters and how a well-written profile can increase visibility.

During the interactive portion, I refined my summary to better reflect my interests in finance, analytics, and global development. I also received tips on how to connect with alumni and follow up after informational interviews. The workshop helped me view LinkedIn not just as a resume, but as a storytelling and networking tool.
        """)
    with col2:
        st.image("LD.png", caption="Employer Session from Handshake", use_container_width=True)

    # 5. Cover Letter Draft
    st.markdown("### Cover Letter Draft (Feb 25)")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
I submitted a complete draft of my cover letter for feedback. The focus was on personalizing the letter to reflect both my experiences and the company's values, rather than relying on generic templates.

After revisions, I ended up with a template that I could easily adapt to multiple finance roles. The process taught me the power of storytelling and specificity in job applications.
        """)
    with open("CV.pdf", "rb") as file:
        st.download_button(label="📄 Download My Cover Letter", data=file, file_name="CV.pdf",
                           mime="application/pdf")

    # 6. Career Conversation
    st.markdown("### Career Conversation with Alumni or Industry Professional (Mar 20)")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
I spoke with a University of Richmond alum working in investment research. They offered helpful advice on navigating early careers in finance and how to demonstrate curiosity and competence when applying to roles.

This conversation also gave me reassurance about the non-linear path to success. The alum shared how experiences outside of Wall Street also led to skill-building and career growth.
        """)
        with col2:
            st.image("convo.png", caption="1-on-1 Career Coaching", use_container_width=True)

    # 7. Resume Ready Approval
    st.markdown("### Resume Ready Certification (Mar 25)")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
Receiving Resume Ready approval using VMOCK meant my resume met the standard expected by employers. I revised my bullet points using action verbs, quantifiable results, and clear formatting.

The experience made me much more confident when submitting applications because I knew my materials were polished and recruiter-friendly.
        """)
    with col2:
        st.image("Vmock.png", caption="Certified Resume!", use_container_width=True)

    # 8. Mock Interview
    st.markdown("### Mock Interview (Apr 1)")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
    I completed my mock interview using an online tool provided by Career Services. The platform simulated a real interview experience with timed questions and webcam recording. I practiced responding to common behavioral and situational prompts, which helped improve my delivery, posture, and verbal organization.

    Afterward, I reviewed my recording and self-assessed areas for improvement, such as filler words and eye contact. The experience built my confidence for real interviews and gave me tangible insights into how I present myself virtually — a skill that’s becoming increasingly important.
        """)
    with col2:
        st.image("MI.png", caption="Mock Interview", use_container_width=True)

    # 9. Career Advising Appointment
    st.markdown("### Career Advising Appointment (Apr 15)")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
I met with a career advisor to strategize internship applications and review my LinkedIn profile. We discussed possible roles aligned with my finance and analytics background.

The session helped me develop a timeline for applications and better understand how to network with intent — not just apply blindly.
        """)
    with col2:
        st.image("CA.png", caption="1-on-1 Career Coaching", use_container_width=True)

    # 10. Designing Your Life Reflections
    st.markdown("### Class Reflections: Designing Your Life, You Majored in What?")
    col1, col2 = st.columns([2, 1])
    # ------------------- Class Reflection Section ------------------- #
    st.markdown("## 📚 5 Reflections from Class")

    # 1. Odyssey Planning & Career Prototyping
    st.markdown("### 🔹 Odyssey Planning & Career Prototypes")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
    This exercise helped me visualize three potential career paths: one rooted in traditional finance, another in advocacy for Palestine, and a third that builds on sports analytics. Laying out each plan made me realize how diverse my interests are and how different scenarios could all lead to fulfillment depending on the opportunities I pursue.

    I also developed prototype conversations and experiences, such as shadowing a sports analytics team, speaking with lobbyists, and pursuing international exposure. This activity made me more intentional about aligning short-term steps (like internships) with long-term visions.
        """)
    with col2:
        st.image("od.png", caption="3 Versions of My Future", use_container_width=True)

    # 2. Workview + Lifeview Integration
    st.markdown("### 🔹 Workview & Lifeview Integration")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
    In my reflections, I connected how my view of work—creating wealth to make change—and my life view as a Palestinian Muslim tie together. I see career success not just as personal achievement but as a mission to serve others and rebuild communities affected by injustice.

    This deeper purpose guides my decision-making. I seek ethical work that honors my values, and I aspire to return to Palestine one day to use finance as a tool for systemic impact. The alignment between work and life gives me clarity and drive in all that I pursue.
        """)
    with col2:
        st.image("lv.png", caption="Purpose Through Faith & Impact", use_container_width=True)

    # 3. Cryptocurrency Market Reflection
    st.markdown("### 🔹 Cryptocurrency Market Reflection")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
    When I witnessed a cryptocurrency created by Trump surge from $7 to $70 in a few hours, it caught my attention as both a finance student and someone curious about market behavior. This real-world event pushed me to research how policy and perception can instantly affect markets.

    I now follow developments in crypto and AI more seriously because they challenge traditional finance logic and offer new opportunities. These reflections help sharpen my analytical thinking and push me to think beyond textbooks.
        """)
    with col2:
        st.image("cc.png", caption="Watching Crypto Markets Move", use_container_width=True)

    # 4. Career Conversation with Dodo Stavrev
    st.markdown("### 🔹 Networking Call with Dodo Stavrev (Trader at Citadel)")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
    I had a 30-minute career conversation with Dodo Stavrev, a former J.P. Morgan investment banker and current trader at Citadel. I was inspired by how he transitioned from banking to trading, and he gave me actionable tips and referrals to follow up on.

    We also bonded over our shared love for soccer and discussed the Bulgarian national team. This conversation taught me that building rapport beyond career talk matters and that staying curious and personable can open doors.
        """)
    with col2:
        st.image("nc.png", caption="Conversation with a Citadel Trader", use_container_width=True)

    # 5. Wisdom Builder – Jack-of-All-Trades Reflection
    st.markdown("### 🔹 Wisdom Builder: Jack of All Trades Reflection")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
    Through our reflection activities, I realized that I naturally lean toward being a "jack of all trades" — comfortable across finance, data analytics, communication, and cultural programming. This doesn’t mean a lack of depth, but rather a flexible toolkit I can apply in dynamic roles.

    In a world driven by change, I see this adaptability as an advantage, especially early in my career. It allows me to approach problems from multiple angles, work across disciplines, and eventually specialize where it counts most.
        """)
    with col2:
        st.image("ja.png", caption="Skills Across Fields", use_container_width=True)

elif page == "Reflections":
    st.markdown("## 🔁 Reflections")
    st.markdown("### 🌍 Integrating Work & Life Purpose")

    st.write("""
My view of work is inseparable from my identity as a Muslim and a Palestinian. I see my career not simply as a way to earn a living, but as a vehicle to serve a larger purpose. To me, work is about maximizing opportunities — acquiring skills, building wealth, and gaining influence — so that I can reinvest those resources in rebuilding and supporting my community back home in Palestine.

Faith and career aren't in conflict; in fact, my faith gives my career direction. Islam teaches that actions must serve humanity, uphold justice, and preserve dignity — values that guide every career decision I make. Whether I'm conducting financial analysis or leading a student organization, I’m always asking: *Will this contribute to something bigger than myself? Will it help others?* That sense of mission pushes me to work harder and with more intentionality every day.
    """)

    st.markdown("---")

    st.markdown("### ✍️ Final Thought")
    st.write("""
I don’t view my goals in finance as separate from my identity or values — they are intertwined. I want to be the kind of professional who succeeds without compromising principles, and the kind of person who uses that success to uplift others. That’s what fulfillment looks like for me — not just a career, but a calling.
    """)


# ------------------ FOOTER ------------------ #
st.markdown("Made with ❤️ by Taher Hijjaz | Powered by Streamlit")
