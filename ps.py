import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")
st.title("🔒Password Strength Checker")
st.markdown("""
Welcome to the **Password Strength Checker**!  
This tool helps you analyze the strength of your password based on:

- ✅ Length of the password  
- ✅ Use of uppercase and lowercase letters  
- ✅ Use of numbers and special characters  
- ✅ Avoiding common or predictable words  
        
### 🔎 How it works:
1. Enter your password in the input box below.  
2. The app will instantly evaluate its strength.  
3. Get tips on how to improve weak passwords.
4. Stay safe and secure online!""")

password = st.text_input("Enter your password:", type="password")

feedback = []
score = 0

if password:
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase letters.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")

    if re.search(r'[!@#$%*&]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (e.g., !@#$%*&).")

    if score == 4:
        feedback.append("✅ Your password is strong!")
    elif score == 3:
        feedback.append("⚠️ Your password is moderate. Consider adding more complexity.")
    else:
        feedback.append("❌ Your password is weak. Please make it stronger.")

    st.markdown("## Improvement Suggestions:")
    for tip in feedback:
        st.write(tip)
else:
    st.info("Please enter a password to check its strength.")