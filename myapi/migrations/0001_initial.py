# Generated by Django 3.0.3 on 2020-02-24 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('mobile', models.CharField(max_length=60)),
                ('vehicle_type', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=60)),
            ],
        ),
    ]