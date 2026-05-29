import streamlit as st

# CONFIG
st.set_page_config(
    page_title="Modern Landing",
    layout="wide",
)

# INLINE CSS
st.markdown("""
<style>

body {
    background: #060816;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* NAVBAR */
.navbar {
    display: flex;
    justify-content: space-between;
    padding: 20px 40px;
    align-items: center;
}

.logo {
    font-size: 26px;
    font-weight: bold;
}

.menu a {
    margin: 0 15px;
    opacity: 0.7;
    cursor: pointer;
}

/* HERO */
.hero-left h1 {
    font-size: 60px;
    margin: 20px 0;
}

.tag {
    background: rgba(255,255,255,0.1);
    padding: 8px 14px;
    border-radius: 999px;
    display: inline-block;
}

.desc {
    opacity: 0.7;
    max-width: 500px;
}

.buttons {
    margin-top: 25px;
}

.primary {
    background: #6d5dfc;
    border: none;
    padding: 12px 24px;
    border-radius: 12px;
    color: white;
    margin-right: 10px;
}

.secondary {
    background: transparent;
    border: 1px solid rgba(255,255,255,0.3);
    padding: 12px 24px;
    border-radius: 12px;
    color: white;
}

/* CARD */
.card img {
    width: 100%;
    border-radius: 20px;
}

/* STATS */
.stat {
    background: rgba(255,255,255,0.05);
    padding: 30px;
    border-radius: 20px;
    text-align: center;
}

.stat h2 {
    font-size: 36px;
}

</style>
""", unsafe_allow_html=True)

# NAVBAR
st.markdown("""
<div class="navbar">
    <div class="logo">NABIL.</div>
    <div class="menu">
        <a>Home</a>
        <a>Features</a>
        <a>Pricing</a>
        <a>Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# HERO
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("""
    <div class="hero-left">
        <div class="tag">✨ Modern Streamlit Website</div>

        <h1>Build Beautiful Digital Experiences</h1>

        <p class="desc">
        Website modern dengan tampilan seperti Figma Sites,
        dibuat menggunakan Streamlit.
        </p>

        <div class="buttons">
            <button class="primary">Start Now</button>
            <button class="secondary">Learn More</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=1200&auto=format&fit=crop">
    </div>
    """, unsafe_allow_html=True)

# SPACING
st.markdown("<br><br>", unsafe_allow_html=True)

# STATS
col1, col2, col3 = st.columns(3)

col1.markdown("""
<div class="stat">
    <h2>10K+</h2>
    <p>Users</p>
</div>
""", unsafe_allow_html=True)

col2.markdown("""
<div class="stat">
    <h2>99%</h2>
    <p>Performance</p>
</div>
""", unsafe_allow_html=True)

col3.markdown("""
<div class="stat">
    <h2>24/7</h2>
    <p>Support</p>
</div>
""", unsafe_allow_html=True)
