import requests
import time
from datetime import datetime

URL = "http://localhost"
LOG_FILE = "health.log"

while True:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        response = requests.get(URL, timeout=5)
        if response.status_code == 200:
            line = f"[{now}] OK — app répond correctement"
        else:
            line = f"[{now}] WARN — statut HTTP {response.status_code}"
    except Exception as e:
        line = f"[{now}] DOWN — app ne répond pas ({e})"

    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")

    time.sleep(30)