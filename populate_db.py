import csv

from app import app, db
from models import Transformer

csv_file_path = 'data/transformers-with-descriptions-cleaned.csv'

def populate_database():
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csvfile)
        for row in reader:
            transformer = Transformer(
                name=row["Name"],
                affiliation=row["Abilities"],
                transformation_mode=row["Transformation/Alternate Mode"],
                image_url=row["Image URL"],
                description=row["Description"],
                quote=row["Quote"]
            )
            db.session.add(transformer)
        db.session.commit()

with app.app_context():
    db.create_all()
    populate_database()
    print("Transformers data populated into database")