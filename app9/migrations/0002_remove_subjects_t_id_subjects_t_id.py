# Generated by Django 5.0.4 on 2024-05-02 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app9', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='T_id',
        ),
        migrations.AddField(
            model_name='subjects',
            name='T_id',
            field=models.ManyToManyField(to='app9.tregistration'),
        ),
    ]
