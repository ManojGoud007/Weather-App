from flask import Flask, render_template
import requests
app = Flask(__name__)

city = 'Hyderabad'
key = 'XXXXXXXXXXXXXXXXX'
url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid='+key

res = requests.get(url).json()
@app.route("/")
def index():
    return render_template('index.html', res = res)


if __name__ == '__main__':
    app.run(debug=True)

