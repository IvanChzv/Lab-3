from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)
@app.route('/')
def index():
    current_date = datetime.now().strftime("%Y-%m-%d")
    return render_template('index.html', current_date=current_date)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)