import csv
from datetime import datetime
class User:
    def __init__(self,name='unknown',birth_year=0,height_cm=0,weight_kg=0,nationality='unknown',id="unknown"):
        if id == "unknown":
            current_time = datetime.now()
            id = current_time.strftime("%Y%m%d%H%M%S%f")
        self.id = id
        self.name = name
        self.birth_year = birth_year
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.nationality = nationality
