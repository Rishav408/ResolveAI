import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# --- Configuration ---
OLLAMA_MODEL = "llama3.2"
DOMAIN = "restaurant"

def load_data():
    try:
        with open("complaint.txt", "r", encoding='utf-8') as f:
            complaints = f.read()
        with open("response.txt", "r", encoding='utf-8') as f:
            responses = f.read()
        with open("policies.txt", "r", encoding='utf-8') as f:
            policies = f.read()
        with open("veera_dhabha_profile.txt", "r", encoding='utf-8') as f:
            profile = f.read()
        return complaints, responses, policies, profile
    except FileNotFoundError as e:
        st.error(f"Missing required file: {e.filename}")
        st.stop()
    except UnicodeDecodeError:
        st.error("Failed to read files. Please ensure they use UTF-8 encoding.")
        st.stop()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def main():
    st.title("🍽️ Veera Dhabha ResolvAI")
    complaints, responses, policies, profile = load_data()
    
    with st.sidebar:
        st.subheader("About Veera Dhabha")
        st.write(profile)
    
    for role, message in st.session_state.chat_history:
        with st.chat_message(role):
            st.write(message)
    
    if query := st.chat_input("Type your complaint/question..."):
        st.session_state.chat_history.append(("user", query))
        
        llm = OllamaLLM(model=OLLAMA_MODEL, temperature=0.5)
        prompt = ChatPromptTemplate.from_template("""
        [Restaurant Profile]
        {profile}
        
        [Policies]
        {policies}
        
        [Chat History]
        {history}
        
        [New Query]
        {query}
        
        Respond helpfully in English:
        """)
        
        response = (prompt | llm).invoke({
            "profile": profile,
            "policies": policies,
            "history": "\n".join(f"{role}: {msg}" for role, msg in st.session_state.chat_history),
            "query": query
        })
        
        st.session_state.chat_history.append(("assistant", response))
        st.rerun()

if __name__ == "__main__":
    main()

# To run this file type, "streamlit run main.py" in the terminal.
