# Generated by Django 3.0.5 on 2020-05-04 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_delivery', models.DateTimeField()),
                ('address', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
