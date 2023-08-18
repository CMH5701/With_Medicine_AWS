# Generated by Django 4.2.4 on 2023-08-17 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('with_medicine_review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review_comment',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r_posts_comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review_board',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='review_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review_board',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
