# Generated by Django 5.0 on 2023-12-26 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('seat', models.IntegerField()),
                ('duration', models.IntegerField()),
            ],
        ),
    ]
