# Credit Score Calculation Project

**Using FastAPI, Streamlit, and MySQL**

This project calculates a user's credit score based on data distributed across multiple databases, using a simple algorithm that assigns weights to various financial factors.

---

## Project Components

* **FastAPI** – Backend API for credit score calculation.
* **MySQL** – The database system, split into 5 independent databases to simulate a distributed architecture.
* **Streamlit** – Frontend UI for user interaction.
* **Python Modules** – Organized into folders like `utils/`, `db_config.py`, etc.
* **SQL Files** – For creating databases and tables.
* **Test Data Script** – Script to generate random sample data for testing.

---

## Databases

The data is distributed across 5 independent databases:

- users_db: Contains user data.
- payments_db: Data on timely payments.
- debt_db: Percentage of credit limit used.
- history_db: Account age.
- mix_db: Credit account variety.

---
## Setup Instructions

### 1. Install Dependencies

Make sure you have all required Python packages:

```bash
pip install -r requirements.txt
```

### 2. Create Databases and Tables

Run the following commands to create the databases and tables using the `.sql` files inside the `models/` directory:

```bash
mysql -u root -p < models/create_users.sql
mysql -u root -p < models/create_payments.sql
mysql -u root -p < models/create_debt.sql
mysql -u root -p < models/create_history.sql
mysql -u root -p < models/create_mix.sql
```

### 3. Generate Random Test Data

To populate the databases with random test data, run the following Python script:

```bash
python test_data.py
```

This will insert sample users, payment records, credit usage data, credit history, and credit mix information into the appropriate databases.

**Note**: Ensure your MySQL credentials are correctly configured in `db_config.py`.

### 4. Start FastAPI Backend

Launch the FastAPI server:

```bash
python -m uvicorn main:app --reload 
```

Access the API at:
[http://127.0.0.1:8000](http://127.0.0.1:8000)

### 5. Start Streamlit Frontend

Launch the Streamlit app for a user-friendly interface:

```bash
python -m streamlit run streamlit_app.py 
```

The app will open in your browser at:
[http://localhost:8501](http://localhost:8501)

---
