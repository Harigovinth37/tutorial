# Generated by Django 5.0.4 on 2024-05-02 09:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('contact', models.CharField(max_length=10)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_id', models.IntegerField()),
                ('subjectname', models.CharField(max_length=100)),
                ('T_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app9.tregistration')),
            ],
        ),
    ]
