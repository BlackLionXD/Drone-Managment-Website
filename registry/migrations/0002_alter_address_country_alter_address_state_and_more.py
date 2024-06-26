# Generated by Django 5.0.1 on 2024-04-16 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(choices=[('ET', 'ETHIOPIA')], default='ET', max_length=2),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(blank=True, choices=[('AN', 'Andaman and Nicobar Islands'), ('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chandigarh'), ('CH', 'Chhattisgarh'), ('DN', 'Dadra and Nagar Haveli'), ('DD', 'Daman and Diu'), ('DL', 'Delhi'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('LA', 'Ladakh'), ('LD', 'Lakshadweep'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Odisha'), ('PY', 'Puducherry'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TS', 'Telangana'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('UK', 'Uttarakhand'), ('WB', 'West Bengal')], help_text='Pick a state', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.CharField(choices=[('ET', 'ETHIOPIA')], default='IN', help_text='At the moment only India is configured, you can setup your own country', max_length=2),
        ),
        migrations.AlterField(
            model_name='person',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text='Assign a date of birth with this person', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(help_text='Associate a email address with the person, this field is required', max_length=254),
        ),
        migrations.AlterField(
            model_name='person',
            name='social_security_number',
            field=models.CharField(blank=True, help_text='If social security / identification number is avaialble associate it with a person', max_length=25, null=True),
        ),
    ]
