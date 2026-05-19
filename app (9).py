
import streamlit as st

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="International Marketing AI",
    page_icon="🌍",
    layout="centered"
)

# -----------------------------------
# Product Marketing Data
# -----------------------------------
marketing_data = {

    "Smart Watch": {
        "title": "AeroX Smart Watch",
        "slogan": "Track Time. Track Life.",
        "description": "Stay connected to every heartbeat of your life with AeroX Smart Watch. Designed for fitness, productivity, and style.",
        "advertisement": "Crafted for modern professionals who demand innovation, elegance, and performance in every second.",
        "social": "⌚ Elevate your lifestyle with AeroX Smart Watch! #SmartLiving #AIWearables"
    },

    "Herbal Tea": {
        "title": "NatureSip Herbal Tea",
        "slogan": "Refresh Naturally. Live Peacefully.",
        "description": "Experience the soothing power of natural herbs blended for a healthier and calmer lifestyle.",
        "advertisement": "Luxury wellness in every sip — crafted from premium organic ingredients around the world.",
        "social": "🍃 Taste the purity of nature with NatureSip Herbal Tea! #HealthyLiving #HerbalTea"
    },

    "Gaming Laptop": {
        "title": "ThunderX Gaming Laptop",
        "slogan": "Power Beyond Limits.",
        "description": "Unleash high-speed gaming performance with cutting-edge graphics and ultra-fast processing.",
        "advertisement": "Built for elite gamers who demand speed, style, and next-generation gaming experiences.",
        "social": "🎮 Rule every battle with ThunderX Gaming Laptop! #GamingLife #NextGenPerformance"
    },

    "Wireless Earbuds": {
        "title": "SoundBeat Wireless Earbuds",
        "slogan": "Feel Every Beat.",
        "description": "Enjoy crystal-clear sound, deep bass, and all-day comfort with intelligent wireless connectivity.",
        "advertisement": "Premium sound engineered for music lovers who value style and immersive audio quality.",
        "social": "🎵 Experience music without limits using SoundBeat Earbuds! #WirelessAudio #MusicLifestyle"
    }
}

# -----------------------------------
# App Title
# -----------------------------------
st.title("🌍 International Business Marketing AI")

st.write("Generate AI-Based International Marketing Content")

# -----------------------------------
# Sidebar
# -----------------------------------
with st.sidebar:

    st.header("📦 Available Products")

    st.write("• Smart Watch")
    st.write("• Herbal Tea")
    st.write("• Gaming Laptop")
    st.write("• Wireless Earbuds")

# -----------------------------------
# Product Selection
# -----------------------------------
product_name = st.selectbox(
    "Select Product",
    (
        "Smart Watch",
        "Herbal Tea",
        "Gaming Laptop",
        "Wireless Earbuds"
    )
)

# -----------------------------------
# Generate Button
# -----------------------------------
if st.button("🚀 Generate Marketing Content"):

    data = marketing_data[product_name]

    st.success("Marketing Content Generated Successfully!")

    st.markdown("## ✨ Marketing Output")

    st.markdown(f"""
### Premium Product Title:
**{data['title']}**

### Slogan:
*"{data['slogan']}"*

### Customer Emotional Advertisement:
{data['description']}

### Luxury Brand Advertisement:
{data['advertisement']}

### Social Media Promotion:
{data['social']}
""")

# -----------------------------------
# Footer
# -----------------------------------
st.markdown("---")
st.caption("Built with Streamlit + Prompt Engineering")
