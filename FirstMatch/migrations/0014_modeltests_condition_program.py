# Generated by Django 2.2.7 on 2020-01-20 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstMatch', '0013_auto_20200113_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeltests',
            name='condition_program',
            field=models.IntegerField(db_column='condition_program', default=1),
            preserve_default=False,
        ),
    ]