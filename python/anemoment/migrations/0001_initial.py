# Generated by Django 2.0.1 on 2018-01-07 09:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RawInputError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[(0, 'Invalid Data'), (1, 'Incomplete Data')], max_length=1)),
                ('raw_input', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WindData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wind_speed_3d', models.FloatField()),
                ('horizontal_wind_direction', models.FloatField()),
                ('u_vector', models.FloatField()),
                ('v_vector', models.FloatField()),
                ('w_vector', models.FloatField()),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('pressure', models.FloatField()),
                ('compass_heading', models.FloatField()),
                ('timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
