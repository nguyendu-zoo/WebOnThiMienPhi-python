# Generated by Django 3.2.6 on 2021-11-10 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeThi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MaDe', models.CharField(max_length=10)),
                ('TenDe', models.TextField()),
                ('NgayTao', models.DateTimeField(auto_now_add=True)),
                ('HinhThucDe', models.IntegerField(choices=[(0, 'Luyen tap trac Nghiem'), (1, 'De thong minh'), (2, 'Ly thuyet tuong tac'), (3, 'Hoi va dap'), (4, 'De thi Tu luan, cham truc tiep tren bai'), (5, 'De thi trac nghiem tu file PDF hoac Word'), (6, 'De thi trac nghiem tu ma tran')], default=0)),
                ('Lop', models.IntegerField(choices=[(0, 'Mau giao'), (1, 'Lop 1'), (2, 'Lop 2'), (3, 'Lop 3'), (4, 'Lop 4'), (5, 'Lop 5'), (6, 'Lop 6'), (7, 'Lop 7'), (8, 'Lop 8'), (9, 'Lop 9'), (10, 'Lop 10'), (11, 'Lop 11'), (12, 'Lop 12'), (13, 'Dai hoc')], default=0)),
                ('TacGia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home.user')),
            ],
        ),
    ]
