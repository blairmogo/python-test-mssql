import pymssql
import yaml


with open("config.yaml", "r") as f:
    CONFIG = yaml.safe_load(f)

try:
    conn = pymssql.connect(
        server=CONFIG["host"],
        port=CONFIG["port"],
        user=CONFIG["username"],
        password=CONFIG["password"],
        database=CONFIG["database"]
    )
    cursor = conn.cursor()
    cursor.execute("SELECT @@VERSION")
    row = cursor.fetchone()
    print(f"\n\nSERVER VERSION:\n\n{row[0]}")
    cursor.close()
    conn.close()
except Exception as e:
    print("Error connecting to server")
    print(f"Error: {e}")
