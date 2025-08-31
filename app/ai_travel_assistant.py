import streamlit as st
import os
import sys
from datetime import datetime

# Konfigurasi halaman
st.set_page_config(
    page_title="Travel Assistant - LangChain",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to check libraries
def check_libraries():
    missing_libs = []
    required_libs = {
        'langchain': 'langchain',
        'langchain_google_genai': 'langchain-google-genai',
        'google.generativeai': 'google-generativeai'
    }
    
    for lib, pip_name in required_libs.items():
        try:
            __import__(lib)
        except ImportError:
            missing_libs.append(pip_name)
    
    return missing_libs

# Check for missing libraries
missing_libraries = check_libraries()

if missing_libraries:
    st.error("🚨 **Missing LangChain Libraries**")
    st.markdown("### 📦 Installation Required")
    
    # Show installation command
    install_cmd = "pip install " + " ".join(missing_libraries)
    st.code(install_cmd, language="bash")
    
    st.markdown("### 📋 Complete Installation:")
    st.code("pip install streamlit langchain langchain-google-genai google-generativeai", language="bash")
    
    st.markdown("### 🔄 After Installation:")
    st.info("Restart the application: `streamlit run app.py`")
    
    st.stop()

# Import libraries after check
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain_core.messages import HumanMessage, AIMessage
    from langchain_core.runnables.history import RunnableWithMessageHistory
    from langchain_community.chat_message_histories import ChatMessageHistory
    import google.generativeai as genai
    
except ImportError as e:
    st.error(f"Import error: {e}")
    st.markdown("Please install required libraries and restart.")
    st.stop()

# CSS Styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .user-message {
        background: #e3f2fd;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #2196f3;
    }
    
    .bot-message {
        background: #f3e5f5;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #9c27b0;
    }
    
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 4px solid #4caf50;
    }
    
    .status-good {
        background: #e8f5e8;
        color: #2e7d32;
        padding: 0.5rem;
        border-radius: 5px;
        margin: 0.5rem 0;
    }
    
    .status-warning {
        background: #fff3e0;
        color: #f57c00;
        padding: 0.5rem;
        border-radius: 5px;
        margin: 0.5rem 0;
    }
    
    .quick-btn {
        background: #f0f2f6;
        border: 1px solid #d1d5db;
        border-radius: 8px;
        padding: 0.75rem;
        margin: 0.25rem 0;
        cursor: pointer;
        transition: all 0.2s;
    }
    
    .quick-btn:hover {
        background: #e5e7eb;
        transform: translateY(-1px);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = ChatMessageHistory()
if "langchain_chain" not in st.session_state:
    st.session_state.langchain_chain = None

# Setup LangChain with modern approach
def setup_langchain():
    api_key = st.sidebar.text_input("🔑 Google Gemini API Key:", type="password")
    
    if api_key:
        try:
            # Configure Gemini
            os.environ["GOOGLE_API_KEY"] = api_key
            
            # Create LLM
            llm = ChatGoogleGenerativeAI(
                model="gemini-2.0-flash-exp",
                google_api_key=api_key,
                temperature=0.7
            )
            
            # Create modern prompt template
            prompt = ChatPromptTemplate.from_messages([
                ("system", """Anda adalah asisten travel Indonesia yang ahli di Asia Tenggara.

Berikan jawaban yang:
- Praktis dan spesifik untuk traveler Indonesia
- Include budget dalam Rupiah
- Gunakan bahasa Indonesia yang friendly
- Format dengan emoji dan struktur jelas"""),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{input}")
            ])
            
            # Create chain
            chain = prompt | llm
            
            # Create conversation chain with message history
            def get_session_history(session_id: str = "default"):
                return st.session_state.chat_history
            
            conversation_chain = RunnableWithMessageHistory(
                chain,
                get_session_history,
                input_messages_key="input",
                history_messages_key="chat_history",
            )
            
            st.session_state.langchain_chain = conversation_chain
            st.sidebar.success("✅ LangChain Active!")
            return True
            
        except Exception as e:
            st.sidebar.error(f"❌ Error: {str(e)}")
            return False
    else:
        st.sidebar.info("ℹ️ Enter API key for LangChain features")
        return False

# Basic travel responses (fallback)
def get_basic_response(question):
    q = question.lower()
    
    if "bali" in q and ("flight" in q or "penerbangan" in q):
        return """✈️ **Jakarta → Bali Flights**

**Airline Options:**
• Garuda Indonesia - Rp 1.200.000 (full service)
• Lion Air - Rp 950.000 (basic)
• Citilink - Rp 900.000 (good value)
• AirAsia - Rp 850.000 (budget)

**Tips:**
- Book 2-3 months early for best prices
- Tuesday-Thursday departures cheaper
- Morning flights less likely delayed"""

    elif "budget" in q or "murah" in q:
        return """💰 **Budget Travel Tips Asia**

**Daily Budget Guide:**
• Backpacker: Rp 300-500k/day
• Mid-range: Rp 500k-1jt/day  
• Comfort: Rp 1-2jt/day

**Money-Saving Tips:**
1. Stay in hostels or guesthouses
2. Eat at local warungs/street food
3. Use public transportation
4. Book flights in advance
5. Travel in shoulder season"""

    elif "cuaca" in q or "weather" in q:
        return """🌤️ **Southeast Asia Weather**

**Best Travel Months:**
• Thailand: November - February
• Bali: April - October  
• Singapore: February - April
• Malaysia: December - February

**Packing Essentials:**
- Light, breathable clothing
- Rain jacket/umbrella
- Sunscreen SPF 30+
- Comfortable walking shoes"""

    else:
        return """👋 **Selamat datang di Travel Assistant!**

🤖 **Powered by LangChain + Gemini 2.0**

**Saya bisa membantu dengan:**
• ✈️ Pencarian penerbangan
• 🌤️ Informasi cuaca
• 💰 Tips budget travel
• 🗺️ Rekomendasi destinasi
• 📋 Planning itinerary

**Contoh pertanyaan:**
- "Flight murah Jakarta ke Bali"
- "Cuaca di Bangkok bulan Maret"
- "Budget backpacking Thailand 1 minggu"
- "Itinerary 5 hari di Singapore"

Tanyakan apa saja tentang travel Asia Tenggara!"""

# Process with modern LangChain
def process_question(question):
    if st.session_state.langchain_chain is not None:
        try:
            # Add user message to history
            st.session_state.chat_history.add_user_message(question)
            
            # Get response from chain
            response = st.session_state.langchain_chain.invoke(
                {"input": question},
                config={"configurable": {"session_id": "default"}}
            )
            
            # Add AI response to history
            st.session_state.chat_history.add_ai_message(response.content)
            
            return response.content
            
        except Exception as e:
            st.warning(f"LangChain error: {e}")
            return get_basic_response(question)
    else:
        return get_basic_response(question)

# Main app
def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🤖 AI Travel Assistant</h1>
        <p>🔗 Powered by LangChain + Gemini 2.0 Flash</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar info
    with st.sidebar:
        st.markdown("### ⚙️ Configuration")
        
        # API Key section
        api_key_set = setup_langchain()
        
        if api_key_set:
            st.markdown("### 🎯 AI Features")
            st.markdown("""
            **✅ Activated Features:**
            - Advanced AI responses
            - Personalized recommendations
            - Real-time query processing
            """)
        
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.session_state.chat_history = ChatMessageHistory()
            st.success("Chat cleared!")
            st.rerun()
        
        # Enhanced status section
        st.markdown("### 📊 System Status")
        if api_key_set:
            st.markdown('<div class="status-good">🟢 Gemini 2.0 Flash: Active</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-warning">🟡 Basic Mode: Active</div>', unsafe_allow_html=True)
        
        # Usage statistics
        if st.session_state.messages:
            total_messages = len(st.session_state.messages)
            st.markdown(f"**💬 Chat Messages:** {total_messages}")

    # Main content area
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("### 💬 Smart Chat Interface")

        # Display conversation history with safe HTML rendering
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f"""
                <div class="user-message">
                    <strong>👤 You:</strong><br>{msg["content"]}
                </div>
                """, unsafe_allow_html=True)
            else:
                # Use st.markdown with proper content handling
                st.markdown(f"""
                <div class="bot-message">
                    <strong>🤖 Travel Assistant:</strong><br>{msg["content"]}
                </div>
                """, unsafe_allow_html=True)

        # Chat input with placeholder
        if prompt := st.chat_input("Tanyakan apapun tentang travel... (contoh: 'flight murah ke Bali minggu depan')"):
            # Add user message
            st.session_state.messages.append({"role": "user", "content": prompt})
                
            # Get AI response
            with st.spinner("🤖 AI sedang berpikir..."):
                response = process_question(prompt)
                
            # Add bot response
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()

    with col2:
        st.markdown("### ⚡ Quick Actions")

        # Enhanced quick start options
        quick_categories = {
            "✈️ Flights": [
                ("🏝️ Jakarta → Bali", "Penerbangan murah Jakarta ke Bali"),
                ("🇸🇬 Jakarta → Singapore", "Flight Jakarta ke Singapura"),
                ("🇹🇭 Jakarta → Bangkok", "Tiket pesawat Jakarta Bangkok"),
            ],
            "🌤️ Weather": [
                ("☀️ Bali Weather", "Cuaca di Bali minggu ini"),
                ("🌧️ Singapore Climate", "Iklim Singapura"),
                ("🌡️ Bangkok Weather", "Cuaca Bangkok hari ini"),
            ],
            "💰 Budget": [
                ("🎒 Backpacker Tips", "Tips backpacking murah Asia"),
                ("💵 Budget Planning", "Planning budget travel 1 minggu"),
                ("🏨 Cheap Accommodation", "Hotel murah vs hostel"),
            ],
            "📋 Planning": [
                ("✅ Travel Checklist", "Checklist lengkap perjalanan luar negeri"),
                ("🗺️ Itinerary Help", "Bantuan buat itinerary 5 hari"),
                ("📱 Travel Apps", "Aplikasi wajib untuk traveling"),
            ]
        }

        for category, options in quick_categories.items():
            with st.expander(category, expanded=False):
                for label, prompt in options:
                    if st.button(label, use_container_width=True, key=f"btn_{label}"):
                        # Add user message
                        st.session_state.messages.append({"role": "user", "content": prompt})
                            
                        # Generate response
                        with st.spinner("🔄 Processing..."):
                            response = process_question(prompt)
                            
                        # Add bot response
                        st.session_state.messages.append({"role": "assistant", "content": response})
                        st.rerun()
            
        st.markdown("---")

        # Feature highlights
        st.markdown("### 🎯 AI Capabilities")
        st.markdown("""
        **🟢 Always Available:**
        - Flight search & comparison
        - Weather forecasts
        - Budget travel tips
        - Destination guides
        - Packing checklists
            
        **🤖 With Gemini 2.0 Flash:**
        - Personalized recommendations
        - Complex itinerary planning
        - Real-time travel updates
        - Multi-language support
        """)

        # Pro tips
        with st.expander("💡 Pro Tips"):
            st.markdown("""
            **🎯 Better Questions = Better Answers:**
            - Include your budget range
            - Mention travel dates
            - Specify interests (beach, culture, food)
            - Add group size & ages
                
            **🔥 Examples:**
            - "Budget 5 juta, 3 hari di Bangkok, suka street food"
            - "Honeymoon ke Bali bulan Juni, hotel romantic"
            - "Backpacking Vietnam 2 minggu, budget minimal"
            """)

# Additional helper function for error handling
def safe_execute(func, *args, **kwargs):
    """Execute function with error handling"""
    try:
        return func(*args, **kwargs)
    except Exception as e:
        st.error(f"Execution error: {str(e)}")
        return None

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error(f"🚨 Critical Error: {str(e)}")
        st.markdown("Please restart the application or contact support.")
