from flask import Flask
import os
import datetime
import pytz
import subprocess
import getpass

app = Flask(__name__)

@app.route("/htop")
def htop():
    name = "Achyuth"
    username = getpass.getuser()
    ist = datetime.datetime.now(pytz.timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.getoutput("top -b -n 1 | head -10")

    return f"""
    <h1>System Monitoring - /htop</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist}</p>
    <pre><strong>Top Output:</strong>\n{top_output}</pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
