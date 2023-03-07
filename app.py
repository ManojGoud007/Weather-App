from flask import Flask, render_template, request
import requests
app = Flask(__name__)

key = 'your-api-key'
@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=' + key
        res = requests.get(url).json()
        return render_template('index.html', res = res)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

