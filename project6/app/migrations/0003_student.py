# Generated by Django 5.1.4 on 2024-12-27 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_department_employee_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField()),
                ('name', models.TextField()),
                ('mark', models.IntegerField()),
            ],
        ),
    ]
