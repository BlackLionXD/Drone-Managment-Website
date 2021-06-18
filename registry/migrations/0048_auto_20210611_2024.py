# Generated by Django 3.2.4 on 2021-06-11 20:24

from django.db import migrations, models
import registry.models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0047_auto_20210611_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='dot_permission_document',
            field=models.URLField(default='https://raw.githubusercontent.com/openskies-sh/aerobridge/master/sample-data/Aerobridge-placeholder-document.pdf', help_text='Link to Purchased RPA has ETA from WPC Wing, DoT for operating in the de-licensed frequency band(s). Such approval shall be valid for a particular make and model', validators=[registry.models.validate_url]),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='operataions_manual_document',
            field=models.URLField(default='https://raw.githubusercontent.com/openskies-sh/aerobridge/master/sample-data/Aerobridge-placeholder-document.pdf', help_text='Link to Operation Manual Document', validators=[registry.models.validate_url]),
        ),
        migrations.AlterField(
            model_name='historicalaircraft',
            name='dot_permission_document',
            field=models.URLField(default='https://raw.githubusercontent.com/openskies-sh/aerobridge/master/sample-data/Aerobridge-placeholder-document.pdf', help_text='Link to Purchased RPA has ETA from WPC Wing, DoT for operating in the de-licensed frequency band(s). Such approval shall be valid for a particular make and model', validators=[registry.models.validate_url]),
        ),
        migrations.AlterField(
            model_name='historicalaircraft',
            name='operataions_manual_document',
            field=models.URLField(default='https://raw.githubusercontent.com/openskies-sh/aerobridge/master/sample-data/Aerobridge-placeholder-document.pdf', help_text='Link to Operation Manual Document', validators=[registry.models.validate_url]),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='eta_document',
            field=models.URLField(default='https://raw.githubusercontent.com/openskies-sh/aerobridge/master/sample-data/Aerobridge-placeholder-document.pdf', help_text='Link to Equipment Type Approval (ETA) from WPC Wing', validators=[registry.models.validate_url]),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='gst_document',
            field=models.URLField(default='https://raw.githubusercontent.com/openskies-sh/aerobridge/master/sample-data/Aerobridge-placeholder-document.pdf', help_text='Link to GST certification document', validators=[registry.models.validate_url]),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='pan_card_document',
            field=models.URLField(default='https://raw.githubusercontent.com/openskies-sh/aerobridge/master/sample-data/Aerobridge-placeholder-document.pdf', help_text='URL of Manufacturers PAN Card scan', validators=[registry.models.validate_url]),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='security_clearance_document',
            field=models.URLField(default='https://raw.githubusercontent.com/openskies-sh/aerobridge/master/sample-data/Aerobridge-placeholder-document.pdf', help_text='Link to Security Clearance from Ministry of Home Affairs', validators=[registry.models.validate_url]),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='identification_photo',
            field=models.URLField(default='https://github.com/openskies-sh/aerobridge/blob/master/sample-data/id-card-sample.jpeg', validators=[registry.models.validate_url]),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='identification_photo_small',
            field=models.URLField(default='https://github.com/openskies-sh/aerobridge/blob/master/sample-data/id-card-sample.jpeg', validators=[registry.models.validate_url]),
        ),
    ]