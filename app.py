from flask import Flask, request
import sqlite3

app = Flask(__name__)

# --- Intentional: unused variable (code smell) ---
_unused_counter = 0

# --- Intentional: hardcoded credential (security issue) ---
DB_PASSWORD = "admin123"   # SonarQube should flag hardcoded credentials

@app.route("/")
def home():
    return "Hello from Flask inside Docker on port 6002!...v2"

# --- Intentional: SQL built via string concatenation (SQL injection risk) ---
@app.route("/user")
def get_user():
    # Example: /user?name=alice
    name = request.args.get("name", "guest")
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    # vulnerable query - concatenates user input directly
    query = "SELECT * FROM users WHERE name = '" + name + "';"
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return {"user": rows}

# --- Intentional: no error handling for division (bug) ---
@app.route("/divide")
def divide():
    # Example: /divide?a=10&b=0  -> runtime ZeroDivisionError
    a = float(request.args.get("a", "1"))
    b = float(request.args.get("b", "0"))   # default 0 to trigger error easily
    result = a / b   # unhandled division by zero
    return {"result": result}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6002)


