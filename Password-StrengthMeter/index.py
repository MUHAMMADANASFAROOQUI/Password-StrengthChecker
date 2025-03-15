import re
import streamlit as st


#page_styling
st.set_page_config(page_title= "Password Strength Checker", page_icon="🔒")

#custom CSS
st.markdown(
    """
    <style>
        .stButton>button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 5px;
            cursor: pointer;
        }

        .stButton>button:hover {
            background-color: #2980b9;
            color: white 
        }

        
        .stApp {
            background-color: #f7f7f7;
            color: #2c3e50;
            font-family: 'Segoe UI'
        }
    </style>
    """,
    unsafe_allow_html=True
)

#Title and page description
st.title("🔐 Password Strength Checker")
st.subheader("Welcome! Test and Improve Your Password Strength!")
st.write("Use this simple tool to check your password's strength and get suggestions to make it more stronger.")

#function
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be **atleast 8 characters**.")
    
    if re.search(r"[A-Z]", password ) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should include **both uppercase(A-Z) and lowercase(a-z) letters**.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should include **atleast one number(0-9)**.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include **atleast one special character (!@#$%^&*)**.")

    #display password strength results
    if score == 4:
        st.success("**Strong Password** Your password is secure.")
    elif score == 3:
        st.info("**Moderate Password** Improve security by adding more feature.")
    else:
        st.error("**Weak Password** Follow the suggestions below:")


    #feedback
    if feedback:
        with st.expander("**Improve your password**"):
            for item in feedback:
                st.write(item)

password = st.text_input("Enter Your Password:", type="password", help="Ensure Ypur Password is strong")

#button
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please enter a password first!")


