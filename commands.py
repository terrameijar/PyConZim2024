import csv
from flask import Flask
from flask.cli import with_appcontext
import click
from models import Transformer, db

csv_file_path = 'data/transformers-with-descriptions-cleaned.csv'

@click.command(name='populate_db')
@with_appcontext
def populate_database():
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        
        for row in reader:
            transformer = Transformer(
                name=row["Name"],
                affiliation=row["Affiliation"],
                abilities=row["Abilities"],
                transformation_mode=row["Transformation/Alternate Mode"],
                image_url=row["Image URL"],
                description=row["Description"],
                quote=row["Quote"]
            )
            db.session.add(transformer)
        db.session.commit()

    print("Transformers data populated into database")