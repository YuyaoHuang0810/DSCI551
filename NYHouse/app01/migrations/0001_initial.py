# Generated by Django 5.0.4 on 2024-04-13 11:27

from django.db import migrations, models


class Migration(migrations.Migration):
    # This is the first migration, so set initial to true
    initial = True
    # There are no dependencies, so leave the list empty
    dependencies = [
    ]
    # This is the list of operations to perform
    operations = [
        # Create a model called Property with the specified fields
        migrations.CreateModel(
            name='Property',
            fields=[
                # The primary key for the model is the id
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                # BROKERTITLE is a character field with a max length of 255
                ('BROKERTITLE', models.CharField(max_length=255)),
                # TYPE is a character field with a max length of 50
                ('TYPE', models.CharField(max_length=50)),
                # PRICE is a decimal field with 2 decimal places and 10 digits
                ('PRICE', models.DecimalField(decimal_places=2, max_digits=10)),
                # BEDS is an integer field
                ('BEDS', models.IntegerField()),
                # BATH is a decimal field with 2 decimal places and 5 digits
                ('BATH', models.DecimalField(decimal_places=2, max_digits=5)),
                # PROPERTYSQFT is an integer field
                ('PROPERTYSQFT', models.IntegerField()),
                # ADDRESS is a character field with a max length of 255
                ('ADDRESS', models.CharField(max_length=255)),
                # STATE is a character field with a max length of 50
                ('STATE', models.CharField(max_length=50)),
                # MAIN_ADDRESS is a character field with a max length of 255
                ('MAIN_ADDRESS', models.CharField(max_length=255)),
                # ADMINISTRATIVE_AREA_LEVEL_2 is a character field with a max length of 50
                ('ADMINISTRATIVE_AREA_LEVEL_2', models.CharField(max_length=50)),
                # LOCALITY is a character field with a max length of 50
                ('LOCALITY', models.CharField(max_length=50)),
                # SUBLOCALITY is a character field with a max length of 50
                ('SUBLOCALITY', models.CharField(max_length=50)),
                # STREET_NAME is a character field with a max length of 255
                ('STREET_NAME', models.CharField(max_length=255)),
                # LONG_NAME is a character field with a max length of 255
                ('LONG_NAME', models.CharField(max_length=255)),
                # FORMATTED_ADDRESS is a character field with a max length of 512
                ('FORMATTED_ADDRESS', models.CharField(max_length=512)),
                # LATITUDE is a decimal field with 6 decimal places and 9 digits
                ('LATITUDE', models.DecimalField(decimal_places=6, max_digits=9)),
                # LONGITUDE is a decimal field with 6 decimal places and 9 digits
                ('LONGITUDE', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
    ]
