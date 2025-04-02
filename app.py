from flask import Flask, render_template
from traffic_system import TrafficSystem

app = Flask(__name__)
traffic_system = TrafficSystem()

@app.route('/')
def index():
    return render_template('index.html', vehicles=traffic_system.vehicles)

if __name__ == '__main__':
    app.run(debug=True)