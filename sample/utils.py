
import csv
from models import db, Hospital, Service

def load_data_from_csv():
    with open('database/hospitals.csv', 'r') as file:
        hospitals = list(csv.DictReader(file))
        for row in hospitals:
            hospital = Hospital(name=row['name'], location=row['location'])
            db.session.add(hospital)

    with open('database/services.csv', 'r') as file:
        services = list(csv.DictReader(file))
        for row in services:
            service = Service(name=row['name'], description=row['description'])
            db.session.add(service)

    db.session.commit()

