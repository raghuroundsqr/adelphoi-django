# Generated by Django 2.2.7 on 2020-01-08 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstMatch', '0003_auto_20200106_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.IntegerField(db_column='program')),
                ('program_name', models.CharField(db_column='program_name', max_length=100)),
                ('gender', models.IntegerField(db_column='gender')),
                ('gender_name', models.CharField(db_column='gender_name', max_length=20)),
                ('level_of_care', models.IntegerField(db_column='level_of_care')),
                ('level_names', models.CharField(db_column='level_names', max_length=100)),
                ('facility_type', models.IntegerField(db_column='facility_type')),
                ('facility_names', models.CharField(db_column='facility_names', max_length=100)),
                ('program_model_suggested', models.CharField(db_column='program_model_suggested', max_length=100)),
                ('program_type', models.CharField(db_column='program_type', max_length=100)),
            ],
        ),
    ]
