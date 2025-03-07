import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")
    
    # Check uppercase and lowercase
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters")
        
    # Check digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Include at least one number")
        
    # Check special characters
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*)")
        
    # Check complexity
    if len(set(password)) >= 6:  # At least 6 unique characters
        score += 1
    else:
        feedback.append("Use more unique characters")
        
    return score, feedback

def main():
    st.title("Password Strength Meter")
    st.write("Check how strong your password is!")
    
    password = st.text_input("Enter your password:", type="password")
    
    if password:
        score, feedback = check_password_strength(password)
        
        # Display strength meter
        if score <= 2:
            st.error("Weak Password")
            strength = "Weak"
        elif score <= 4:
            st.warning("Moderate Password")
            strength = "Moderate"
        else:
            st.success("Strong Password")
            strength = "Strong"
            
        # Display score and progress bar
        st.write(f"Strength Score: {score}/5")
        st.progress(score/5)
        
        # Display feedback for improvement
        if strength != "Strong":
            st.write("Suggestions for improvement:")
            for suggestion in feedback:
                st.write("• " + suggestion)
        else:
            st.write("Great job! Your password meets all security criteria.")

if __name__ == "__main__":
    main()

