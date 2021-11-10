# Generated by Django 3.2.6 on 2021-11-10 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=254)),
                ('SDT', models.CharField(max_length=12)),
                ('NgaySinh', models.DateTimeField()),
                ('NgayTao', models.DateTimeField(auto_now_add=True)),
                ('ChucVuCaNhan', models.CharField(max_length=100)),
                ('GioiThieu', models.TextField()),
            ],
        ),
    ]
