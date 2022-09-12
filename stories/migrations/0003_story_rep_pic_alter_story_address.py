# Generated by Django 4.0 on 2022-09-04 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_place_etc_hours_alter_placephoto_place'),
        ('stories', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='rep_pic',
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='story',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.place'),
        ),
    ]