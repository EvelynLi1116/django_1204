from django.core.management.base import BaseCommand
import csv
from adopt.models import Pet

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('csv_file')

    def handle(self,*args,**options):
        with open(options['csv_file'])as fp:
            reader =csv.DictReader(fp)
            data = list(reader)

        for item in data:
            p=Pet(
                birth_date = item['birthdate'],
                species=item['species'],
                sex = item['sex'],
                )
            p.save()
