# Generated by Django 3.2.6 on 2021-11-22 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_alter_user_chucvu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monhoc',
            name='TenMonHoc',
            field=models.CharField(choices=[(0, 'Tiếng Việt cấp 1'), (1, 'Tiếng Anh'), (2, 'Đạo Đức'), (3, 'Tự Nhiên và Xã Hội'), (4, 'Lịch Sử và Địa Lý'), (5, 'Khoa Học'), (6, 'Tin Học'), (7, 'Công Nghệ'), (8, 'Mỹ Thuật'), (9, 'Âm Nhạc'), (10, 'Ngữ Văn'), (11, 'Toán'), (12, 'Vật Lý'), (13, 'Hóa Học'), (14, 'Giáo Dục Công Dân'), (15, 'Khoa Học Tự Nhiên'), (16, 'Sinh Học')], default=0, max_length=100),
        ),
    ]
