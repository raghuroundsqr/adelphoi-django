# Generated by Django 2.2.7 on 2019-12-26 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstMatch', '0008_testmodels_exclusionary_criteria'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeltests',
            name='Exclusionary_Criteria',
            field=models.BooleanField(db_column='Exclusionary_Criteria', default=False),
        ),
    ]
