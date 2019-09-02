import requests
from flask import render_template
from app import app

@app.route("/")
def index():
    temp = requests.get("http://192.168.0.87").text.split("temp")[1][:5]

    # html

# >>> html.split("temp")[1]
# ':24.00\r\n</body>\r\n</html>\r\n'
# >>> html.split("temp")[1][5:]
# '0\r\n</body>\r\n</html>\r\n'
# >>> html.split("temp")[1][:5]
    return render_template("index.html", temp=temp)
