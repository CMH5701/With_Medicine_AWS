# Generated by Django 4.2.4 on 2023-08-18 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Med_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_name', models.CharField(max_length=50)),
                ('med_type', models.CharField(max_length=50)),
                ('med_content', models.TextField()),
                ('take_medicine', models.TextField()),
            ],
        ),
    ]
