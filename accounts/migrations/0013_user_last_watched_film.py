# Generated by Django 3.0.3 on 2020-03-06 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0012_film_comments'),
        ('accounts', '0012_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_watched_film',
            field=models.ForeignKey(blank=True, default='0304141', on_delete=django.db.models.deletion.CASCADE, related_name='lastWatched', to='films.Film'),
            preserve_default=False,
        ),
    ]
