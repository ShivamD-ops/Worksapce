# Generated by Django 5.1.3 on 2024-12-04 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemodel',
            name='emp_sallary',
            field=models.CharField(default='0', max_length=100),
        ),
    ]