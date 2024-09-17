import streamlit as st

# Function to process the input string and generate the All_Key columns
def generate_all_key(input_string):
    # Split the input string into left and right parts based on '='
    conditions = input_string.split(' AND ')
    
    left_parts = []
    right_parts = []
    
    for condition in conditions:
        if '=' in condition:
            left, right = condition.split('=')
            left = left.strip()
            right = right.strip()
            
            # Extracting the table and column names from the left and right parts
            left_table_col = left.split('.')[-2:]
            right_table_col = right.split('.')[-2:]
            
            # Creating the formatted strings
            left_key = f"{left_table_col[0]}[{left_table_col[1]}]"
            right_key = f"{right_table_col[0]}[{right_table_col[1]}]"
            
            left_parts.append(left_key)
            right_parts.append(right_key)
    
    # Joining all the parts with ' & ' for the final All_Key
    left_all_key = ' & '.join(left_parts)
    right_all_key = ' & '.join(right_parts)
    
    return left_all_key, right_all_key

# Streamlit UI
st.title("Composite Key Generator")
input_string = st.text_area("Enter the string:", "")

# Add a button to see results
if st.button("Generate All_Key"):
    if input_string:
        left_all_key, right_all_key = generate_all_key(input_string)
        
        st.subheader("Generated All_Key for the Left Side:")
        st.write(left_all_key)
        
        st.subheader("Generated All_Key for the Right Side:")
        st.write(right_all_key)
    else:
        st.write("Please enter a valid string to process.")
