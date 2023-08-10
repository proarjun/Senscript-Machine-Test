# Generated by Django 4.2.4 on 2023-08-10 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('student_id', models.CharField(default='STD_', max_length=20, primary_key=True, serialize=False)),
                ('branch', models.CharField(choices=[('CS', 'CS'), ('EC', 'EC'), ('MECH', 'MECH')], max_length=20)),
                ('name', models.CharField(max_length=60)),
                ('phone', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(max_length=254)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
