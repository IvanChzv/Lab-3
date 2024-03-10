from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)
@app.route('/')
def index():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', current_datetime=current_datetime)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
