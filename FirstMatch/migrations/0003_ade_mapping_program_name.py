# Generated by Django 2.2.7 on 2019-12-04 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstMatch', '0002_ade_mapping_location_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='ade_mapping',
            name='program_name',
            field=models.CharField(db_column='program_name', default=1, max_length=100),
            preserve_default=False,
        ),
    ]
