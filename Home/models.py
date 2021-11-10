from django.db import models

# Create your models here.

class User(models.Model):
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=15)
    Email = models.EmailField()
    SDT = models.CharField(max_length=12)
    NgaySinh = models.DateTimeField()
    NgayTao = models.DateTimeField(auto_now_add=True)
    DichVuCaNhan = (
        (0, "Phụ Huynh"),
        (1, "Học Sinh"),
        (2, "Sinh Viên"),
        (3, "Giáo Viên - Giảng Viên")
    )
    ChucVuCaNhan = models.IntegerField(default=0, choices=DichVuCaNhan)
    GioiThieu = models.TextField()

class MonThi(models.Model):
    MaMon = models.CharField(max_length=50)
    TenMon = models.TextField()
 
class DeThi(models.Model):
    TacGia = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    TenMonThi = models.ForeignKey(MonThi, on_delete=models.SET_NULL, null=True)
    MaDe = models.CharField(max_length=10)
    TenDe = models.TextField()
    NgayTao = models.DateTimeField(auto_now_add=True)
    HinhThucDeThi = (
        (0, "Luyện tập trắc nghiệm"),
        (1, "Đề thi thông minh"),
        (2, "Lý thuyết tương tác"),
        (3, "Hỏi và Đáp"),
        (4, "Đề thi Tự luận, chấm điểm trực tiếp lên bài"),
        (5, "Đề thi tắc nghệm từ file PDF hoặc Word"),
        (6, "Đề thi trắc nghiệm từ ma trận")
    )
    HinhThucDe = models.IntegerField(default=0, choices=HinhThucDeThi)
    ClassForTest = (
        (0, "Mẫu giáo"),
        (1, "Lớp 1"),
        (2, "Lớp 2"),
        (3, "Lớp 3"),
        (4, "Lớp 4"),
        (5, "Lớp 5"),
        (6, "Lớp 6"),
        (7, "Lớp 7"),
        (8, "Lớp 8"),
        (9, "Lớp 9"),
        (10, "Lớp 10"),
        (11, "Lớp 11"),
        (12, "Lớp 12"),
        (13, "Đại học")
    )
    Lop = models.IntegerField(default=0, choices=ClassForTest)

class De(models.Model):
    MaDe = models.ForeignKey(DeThi, on_delete=models.CASCADE)
    