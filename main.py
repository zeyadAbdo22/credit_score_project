# main.py
from fastapi import FastAPI, HTTPException
from db_config import get_all_connections
from utils.score_calculator import calculate_credit_score

app = FastAPI()

@app.get("/calculate_score/{user_id}")
def get_credit_score(user_id: int):
    try:
        conns = get_all_connections()
        score_data = calculate_credit_score(user_id, conns)
        return {"user_id": user_id, **score_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))