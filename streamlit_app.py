import streamlit as st
import requests
#from fastapi import HTTPException  # Note: This import isn't used in this file

# Page configuration
st.set_page_config(page_title="Credit Score Calculator", page_icon="📊", layout="centered")
st.title("Credit Score Calculator")

# API URL (default runs on localhost)
API_URL = "http://127.0.0.1:8000"  # This assumes FastAPI is running locally on port 8000

# User ID input field
user_id = st.number_input(
    "Enter User ID",
    min_value=1,       # Only positive integers allowed
    step=1,            # Increment by 1
    format="%d",       # Display as integer
    value=None,        # Starts empty
    placeholder="Type your user ID..."  # Hint text
)

# When "Check Score" button is clicked
if st.button("Check Score", type="primary"):
    # Validate input
    if not user_id:
        st.warning("Please enter a valid User ID")
        st.stop()  # Stop execution if no ID provided

    try:
        # Make API request to FastAPI endpoint
        response = requests.get(f"{API_URL}/calculate_score/{user_id}")
        
        # If API returns successful response (status code 200)
        if response.status_code == 200:
            data = response.json()  # Parse JSON response
            
            # Display results section
            st.divider()
            st.subheader("Credit Score Result")
            
            # Show user info
            st.markdown(f"**{data['name']} (ID: {user_id})**")
            st.markdown(f"**Email:** {data['email'] if data['email'] else 'Not available'}")
            
            # Create styled score card using HTML/CSS
            st.markdown(
                f"""
                <div style='
                    border: 1px solid #ddd;
                    border-radius: 8px;
                    padding: 20px;
                    margin-top: 10px;
                '>
                    <h2 style='text-align: center;'>Credit Score: {data['final_score']:.2f}</h2>
                    <hr style='margin: 10px 0;'>
                    <p><b>Payment Score:</b> {data['payment_score']:.1f}</p>
                    <p><b>Debt Score:</b> {data['debt_score']:.2f}</p>
                    <p><b>History Score:</b> {data['history_score']:.1f}</p>
                    <p><b>Credit Mix Score:</b> {data['mix_score']:.1f}</p>
                </div>
                """,
                unsafe_allow_html=True  # Allows raw HTML rendering
            )
    
        else:
            # Handle case where user isn't found (API returns 404)
            st.error(f"User not found in the database")

    # Handle connection errors to API
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to connect to API: {str(e)}")
    
    # Catch any other unexpected errors
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")