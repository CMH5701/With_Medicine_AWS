# Generated by Django 4.2.4 on 2023-08-17 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review_board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='data published')),
                ('body', models.TextField()),
                ('hits', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Review_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_text', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('review_board_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='with_medicine_review.review_board')),
            ],
        ),
    ]
