import csv
from models import db, Hospital, Service

def load_data_from_csv():
    with open('database/hospitals.csv', 'r') as file:
        hospitals = list(csv.reader(file))
        for row in hospitals[1:]:  # Skip the header row
            hospital = Hospital(name=row[1].strip(), location=row[2].strip())
            db.session.add(hospital)
            
    with open('database/services.csv', 'r') as file:
        services = list(csv.reader(file))
        for row in services[1:]:  # Skip the header row
            service = Service(name=row[1].strip(), description=row[2].strip())
            db.session.add(service)
            
    db.session.commit()
