from django.core.management.base import BaseCommand
import pandas as pd
from django.db import transaction
from annual.models import QuarterlyProduction, AnnualProduction


class Command(BaseCommand):
    def handle(self, *args, **options):
        path_file = 'data.xls'
        df = pd.read_excel(path_file)
        # df = df.drop_duplicates(subset=['API WELL NUMBER', 'OIL', 'GAS', 'BRINE'])
        records = df.groupby('API WELL  NUMBER').agg(
            total_oil=pd.NamedAgg(column="OIL", aggfunc='sum'),
            total_gas=pd.NamedAgg(column="GAS", aggfunc='sum'),
            total_brine=pd.NamedAgg(column="BRINE", aggfunc='sum'),
        ).reset_index()
        annual_records = [
            AnnualProduction(
                api_well_number=data['API WELL  NUMBER'],
                total_oil=data['total_oil'],
                total_gas=data['total_gas'],
                total_brine=data['total_brine'],
            )
            for size, data in records.iterrows()
        ]

        batch_size = 500
        with transaction.atomic():
            for size in range(0, len(annual_records)):
                AnnualProduction.objects.bulk_create(annual_records[size:size + batch_size], ignore_conflicts=True)
                self.stdout.write(f'{batch_size}data added..')
        return "annual data added successfully"
