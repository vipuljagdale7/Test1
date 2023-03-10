# Generated by Django 3.0 on 2022-07-15 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField()),
                ('qty', models.IntegerField()),
                ('is_available', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'fruit',
            },
        ),
    ]
