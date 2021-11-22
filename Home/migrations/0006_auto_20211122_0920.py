# Generated by Django 3.2.6 on 2021-11-22 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_auto_20211110_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='CauHoi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HinhThucCauHoi', models.IntegerField(choices=[(0, 'Trắc nghiệm'), (1, 'Tự luận')], default=0)),
                ('NoiDungCauHoi', models.TextField()),
                ('DoKho', models.IntegerField(choices=[(0, 'Dễ'), (1, 'Trung bình'), (2, 'Khó')], default=0)),
                ('GhiChu', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DapAn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NoiDungDapAn', models.TextField(null=True)),
                ('DungSai', models.TextField(null=True)),
                ('GhiChu', models.TextField(null=True)),
                ('CauHoi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.cauhoi')),
            ],
        ),
        migrations.CreateModel(
            name='HinhThucDeThi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HinhThucDe', models.IntegerField(choices=[(0, 'Luyện tập trắc nghiệm'), (1, 'Đề thi thông minh'), (2, 'Lý thuyết tương tác'), (3, 'Hỏi và Đáp'), (4, 'Đề thi Tự luận, chấm điểm trực tiếp lên bài'), (5, 'Đề thi tắc nghệm từ file PDF hoặc Word'), (6, 'Đề thi trắc nghiệm từ ma trận')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Lop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenLop', models.IntegerField(choices=[(0, 'Mẫu giáo'), (1, 'Lớp 1'), (2, 'Lớp 2'), (3, 'Lớp 3'), (4, 'Lớp 4'), (5, 'Lớp 5'), (6, 'Lớp 6'), (7, 'Lớp 7'), (8, 'Lớp 8'), (9, 'Lớp 9'), (10, 'Lớp 10'), (11, 'Lớp 11'), (12, 'Lớp 12'), (13, 'Đại học')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MonHoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenMonHoc', models.IntegerField(choices=[(0, 'Tiếng Việt cấp 1'), (1, 'Tiếng Anh'), (2, 'Đạo Đức'), (3, 'Tự Nhiên và Xã Hội'), (4, 'Lịch Sử và Địa Lý'), (5, 'Khoa Học'), (6, 'Tin Học'), (7, 'Công Nghệ'), (8, 'Mỹ Thuật'), (9, 'Âm Nhạc'), (10, 'Ngữ Văn'), (11, 'Toán'), (12, 'Vật Lý'), (13, 'Hóa Học'), (14, 'Giáo Dục Công Dân'), (15, 'Khoa Học Tự Nhiên'), (16, 'Sinh Học')], default=0)),
                ('GhiChu', models.TextField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='dethi',
            name='HinhThucDe',
        ),
        migrations.RemoveField(
            model_name='dethi',
            name='Lop',
        ),
        migrations.RemoveField(
            model_name='dethi',
            name='MaDe',
        ),
        migrations.RemoveField(
            model_name='dethi',
            name='TenDe',
        ),
        migrations.RemoveField(
            model_name='dethi',
            name='TenMonThi',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ChucVuCaNhan',
        ),
        migrations.AddField(
            model_name='dethi',
            name='SoLuongCauHoi',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='dethi',
            name='TieuDeBaiThi',
            field=models.CharField(default='Bài Kiểm Tra Chất Lượng', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='ChucVu',
            field=models.TextField(choices=[('a', 'Phụ Huynh'), ('b', 'Học Sinh'), ('c', 'Sinh Viên'), ('d', 'Giáo Viên - Giảng Viên')], default='a'),
        ),
        migrations.AlterField(
            model_name='user',
            name='GioiThieu',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='De',
        ),
        migrations.DeleteModel(
            name='MonThi',
        ),
        migrations.AddField(
            model_name='cauhoi',
            name='MaDeThi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.dethi'),
        ),
        migrations.AddField(
            model_name='dethi',
            name='HinhThucThi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home.hinhthucdethi'),
        ),
        migrations.AddField(
            model_name='dethi',
            name='MonThi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home.monhoc'),
        ),
        migrations.AddField(
            model_name='dethi',
            name='TenLopThi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home.lop'),
        ),
    ]
