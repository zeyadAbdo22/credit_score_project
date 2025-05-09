import streamlit as st
from db_config import get_all_connections
from utils.score_calculator import calculate_credit_score

# Set up page configuration
st.set_page_config(page_title="Credit Score Checker", layout="centered")
st.title("Check Credit Score")

# User ID input field - starts empty
user_id = st.number_input(
    "Enter User ID",
    min_value=1,  # Minimum allowed value
    step=1,
    format="%d",  # Integer format
    value=None,  # Starts empty
    placeholder="Type your user ID..."  # Hint text
)

# Check Score button (always enabled in this version)
if st.button("Check Score", type="primary"):
    try:
        # Get database connections
        conns = get_all_connections()
        
        # Check if user exists in database
        cursor = conns['users_db'].cursor()
        cursor.execute("SELECT name, email FROM users WHERE user_id = %s", (user_id,))
        user_record = cursor.fetchone()
        
        if not user_record:
            st.warning("User ID not found in database")
            st.stop()  # Stop execution if user not found
        
        user_name, user_email = user_record
        score_data = calculate_credit_score(user_id, conns)
        
        # Display results
        st.divider()
        st.subheader("Credit Score Result")
        st.markdown(f"**{user_name} (ID: {user_id})**")
        st.markdown(f"**Email:** {user_email}")
        
        # Score card with styling
        st.markdown(
            f"""
            <div style='
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 20px;
                margin-top: 10px;
            '>
                <h2 style='text-align: center;'>Credit Score: {score_data['final_score']:.2f}</h2>
                <hr style='margin: 10px 0;'>
                <p><b>Payment Score:</b> {score_data['payment_score']:.1f}</p>
                <p><b>Debt Score:</b> {score_data['debt_score']:.2f}</p>
                <p><b>History Score:</b> {score_data['history_score']:.1f}</p>
                <p><b>Credit Mix Score:</b> {score_data['mix_score']:.1f}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    except Exception as e:
        st.error(f"Error calculating score: {str(e)}")