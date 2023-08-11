# Generated by Django 4.2.4 on 2023-08-10 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDetails', '0004_alter_studentmarks_admission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmarks',
            name='admission',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='marks', serialize=False, to='StudentDetails.studentdetails'),
        ),
    ]