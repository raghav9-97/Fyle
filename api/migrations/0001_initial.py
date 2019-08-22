# Generated by Django 2.2.4 on 2019-08-20 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('ifsc', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('bank_id', models.IntegerField()),
                ('branch', models.CharField(max_length=75)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=30)),
            ],
        ),
    ]