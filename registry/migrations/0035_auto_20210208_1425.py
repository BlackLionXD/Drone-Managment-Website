# Generated by Django 3.1.6 on 2021-02-08 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0034_auto_20210204_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='company_number',
            field=models.CharField(default='CO-212', max_length=25),
        ),
    ]