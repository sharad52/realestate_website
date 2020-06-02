# Generated by Django 3.0.3 on 2020-04-09 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listings',
            options={'verbose_name': 'Listing', 'verbose_name_plural': 'Listings'},
        ),
        migrations.AlterField(
            model_name='listings',
            name='photo_1',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='photo_2',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='photo_3',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='photo_4',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='photo_5',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='photo_6',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]
