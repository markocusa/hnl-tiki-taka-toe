# Generated manually - join code za "play with a friend"

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_online_match_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='join_code',
            field=models.CharField(blank=True, max_length=8, null=True, unique=True),
        ),
    ]