# Generated manually - potvrda remija (draw request/response)

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_match_join_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='draw_requested_by',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]