# Generated by Django 4.0.2 on 2022-04-28 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_alter_auction_bids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='item_watch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='auctions.listing'),
        ),
    ]
