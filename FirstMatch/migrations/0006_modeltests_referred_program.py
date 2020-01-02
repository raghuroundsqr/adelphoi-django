# Generated by Django 2.2.7 on 2020-01-02 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstMatch', '0005_adelphoi_mapping_program_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeltests',
            name='referred_program',
            field=models.CharField(choices=[('ISM', 'ISM'), ('ISF', 'ISF'), ('MHFO', 'MHFO'), ('SUBAB', 'SUBAB'), ('DIAGNOSTIC', 'DIAGNOSTIC'), ('SEXOF-MH', 'SEXOF-MH'), ('SEXOF-SECURE', 'SEXOF-SECURE'), ('SEXOF', 'SEXOF'), ('ENHANCED', 'ENHANCED'), ('SECURE-MALE', 'SECURE-MALE'), ('SECURE-FEMALE', 'SECURE-FEMALE'), ('INDEPENDENT LIVING', 'INDEPENDENT LIVING')], db_column='program_type', default=1, max_length=100),
            preserve_default=False,
        ),
    ]
