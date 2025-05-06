from decimal import Decimal

def calculate_credit_score(user_id, conns):
    weights = {
        "payment": Decimal(0.35),
        "debt": Decimal(0.30),
        "history": Decimal(0.15),
        "mix": Decimal(0.20)
    }

    def query_one(conn, sql):
        cursor = conn.cursor()
        cursor.execute(sql, (user_id,))
        result = cursor.fetchone()[0]
        return Decimal(result)  

    payment_score = query_one(conns['payments_db'], "SELECT on_time/total * 100 FROM payments WHERE user_id = %s")
    debt_score = query_one(conns['debt_db'], "SELECT (1 - used/credit_limit) * 100 FROM debt WHERE user_id = %s")
    history_score = query_one(conns['history_db'], "SELECT (account_age / 30) * 100 FROM history WHERE user_id = %s")
    mix_score = query_one(conns['mix_db'], "SELECT (types_used / total_types) * 100 FROM credit_mix WHERE user_id = %s")

    raw_score = (
        weights['payment'] * payment_score +
        weights['debt'] * debt_score +
        weights['history'] * history_score +
        weights['mix'] * mix_score
    )
    scaled_score = int(300 + (raw_score / Decimal(100)) * Decimal(550))

    return {
        "payment_score": round(float(payment_score), 2),
        "debt_score": round(float(debt_score), 2),
        "history_score": round(float(history_score), 2),
        "mix_score": round(float(mix_score), 2),
        "final_score": scaled_score
    }
