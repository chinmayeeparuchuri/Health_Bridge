import streamlit as st
import requests

st.title("🩺 Accessible Healthcare Information Bot")
st.write("Ask any question related to health in English or Hindi.")

query = st.text_input("💬 Your question:")

if st.button("Get Advice") and query:
    with st.spinner("🔍 Searching for health advice..."):
        try:
            response = requests.post(
                "http://127.0.0.1:5000/query",
                json={"query": query}
            )
            data = response.json()

            # ✅ Since the response is a list, loop directly over it
            if isinstance(data, list) and data:
                for i, result in enumerate(data, 1):
                    st.markdown(f"### 🔹 Result {i}")
                    st.write(f"**🩺 Topic:** {result['topic']}")
                    st.write(f"**📂 Category:** {result['category']}")
                    st.write("**🔸 English:**")
                    st.write(f"• Description: {result['description_en']}")
                    st.write(f"• Advice: {result['advice_en']}")
                    st.write("**🔸 Hindi:**")
                    st.write(f"• विवरण: {result['description_hi']}")
                    st.write(f"• सलाह: {result['advice_hi']}")
                    st.markdown("---")
            else:
                st.warning("⚠️ No relevant results found.")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
