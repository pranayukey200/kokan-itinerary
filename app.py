from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    print('\n  Konkan itinerary running -> http://localhost:5000\n')
    app.run(host='0.0.0.0', port=5000, debug=False)
