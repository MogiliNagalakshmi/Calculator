import streamlit as st

# Title
st.title("🧮 Simple Calculator")

# Operation selection
option = st.selectbox("Choose an operation:", ("Addition", "Subtraction", "Multiplication", "Division"))

# Input numbers
num1 = st.number_input("Enter the first number:", format="%.2f")
num2 = st.number_input("Enter the second number:", format="%.2f")

# Calculate result
if st.button("Calculate"):
    if option == "Addition":
        result = num1 + num2
        st.success(f"The result is: {result}")
    elif option == "Subtraction":
        result = num1 - num2
        st.success(f"The result is: {result}")
    elif option == "Multiplication":
        result = num1 * num2
        st.success(f"The result is: {result}")
    elif option == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result is: {result}")
        else:
            st.error("Error: Division by zero is not allowed.")
