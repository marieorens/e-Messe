# Generated by Django 5.0.6 on 2024-07-08 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messe', '0003_messe_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='messe',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
