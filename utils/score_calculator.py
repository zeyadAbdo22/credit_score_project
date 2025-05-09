def calculate_credit_score(user_id, conns):
    # Define weights for each credit score factor
    weights = {
        "payment": 0.35,  # 35% weight for payment history
        "debt": 0.30,     # 30% for debt usage
        "history": 0.15,  # 15% for credit history length
        "mix": 0.20       # 20% for credit mix variety
    }

    # Helper function to query database and cap scores at 100
    def query_and_cap(conn, sql, max_score=100):
        cursor = conn.cursor()
        cursor.execute(sql, (user_id,))  # Execute SQL with user_id parameter
        result = float(cursor.fetchone()[0])  # Get first result as float
        return min(result, max_score)  # Ensure score doesn't exceed max_score

    # Get payment history score (on-time payments percentage)
    payment_score = query_and_cap(conns['payments_db'], 
                                "SELECT on_time/total * 100 FROM payments WHERE user_id = %s")

    # Get debt utilization score (lower usage = better)
    debt_score = query_and_cap(conns['debt_db'], 
                             "SELECT (1 - used/credit_limit) * 100 FROM debt WHERE user_id = %s")

    # Get credit history length score (max 10 years/120 months)
    history_score = query_and_cap(conns['history_db'], 
                                "SELECT (account_age / 120) * 100 FROM history WHERE user_id = %s")

    # Get credit mix score (variety of credit types)
    mix_score = query_and_cap(conns['mix_db'], 
                            "SELECT (types_used / total_types) * 100 FROM credit_mix WHERE user_id = %s")

    # Calculate weighted raw score (0-100 scale)
    raw_score = (
        weights['payment'] * payment_score +
        weights['debt'] * debt_score +
        weights['history'] * history_score +
        weights['mix'] * mix_score
    )

    # Convert to standard credit score range (300-850)
    scaled_score = 300 + (raw_score / 100) * 550

    # Return all scores for display
    return {
        "payment_score": payment_score,  # Original payment score
        "debt_score": debt_score,       # Original debt score
        "history_score": history_score,  # Original history score
        "mix_score": mix_score,         # Original credit mix score
        "final_score": scaled_score     # Final calculated credit score
    }