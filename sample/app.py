from flask import Flask, render_template
from models import db, Hospital, Service
from utils import load_data_from_csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hospital/<hospital_id>')
def hospital(hospital_id):
    hospital = Hospital.query.get(hospital_id)
    return render_template('hospital.html', hospital=hospital)

@app.route('/service/<service_id>')
def service(service_id):
    service = Service.query.get(service_id)
    return render_template('service.html', service=service)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        load_data_from_csv()
    app.run(host='0.0.0.0', port=5000)

