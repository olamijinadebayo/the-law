import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','coolproject.settings')
import django
django.setup()

from django.contrib.gis.geos import Point
import csv 

from lawyer.models import AllLawyer


def main():
    print("am working")

    csv_data = "data/final_data.csv"

    with open(csv_data, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for line in csv_reader:
            name = line['name']
            icon = line['icon']
            lat = line['latitude']
            lng =  line['longitude']
            description = line['vicinity']
            coord = Point(float(lng),float(lat))
            data = AllLawyer(name=name, icon=icon, description=description,geom=coord)
            data.save()

if __name__ == "__main__":
    main()