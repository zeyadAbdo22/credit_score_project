from fastapi import FastAPI, HTTPException
from db_config import get_all_connections
from utils.score_calculator import calculate_credit_score

app = FastAPI()

@app.get("/calculate_score/{user_id}")
def get_credit_score(user_id: int):
    try:
        conns = get_all_connections()
        score_data = calculate_credit_score(user_id, conns)
        
        # Get user info
        cursor = conns['users_db'].cursor()
        cursor.execute("SELECT name, email FROM users WHERE user_id = %s", (user_id,))
        user_record = cursor.fetchone()
        
        if user_record:
            user_name, user_email = user_record
            user_data = {"name": user_name, "email": user_email}
        else:
            user_data = {"name": f"User {user_id}", "email": None}
            
        return {
            "user_id": user_id,
            **user_data,
            **score_data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))