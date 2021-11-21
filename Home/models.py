from django.db import models

# Create your models here.

class User(models.Model):
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=15)
    Email = models.EmailField()
    SDT = models.CharField(max_length=12)
    NgaySinh = models.DateTimeField()
    NgayTao = models.DateTimeField(auto_now_add=True)
    ChucVuOption = (
        (0, "Phụ Huynh"),
        (1, "Học Sinh"),
        (2, "Sinh Viên"),
        (3, "Giáo Viên - Giảng Viên")
    )
    ChucVu = models.IntegerField(default=0, choices=ChucVuOption)
    GioiThieu = models.TextField(null=True)

class MonHoc(models.Model):
    MonHocOptions = (
        (0, "Tiếng Việt cấp 1"),
        (1, "Tiếng Anh"),
        (2, "Đạo Đức"),
        (3, "Tự Nhiên và Xã Hội"),
        (4, "Lịch Sử và Địa Lý"),
        (5, "Khoa Học"),
        (6, "Tin Học"),
        (7, "Công Nghệ"),
        (8, "Mỹ Thuật"),
        (9, "Âm Nhạc"),
        (10, "Ngữ Văn"),
        (11, "Toán"),
        (12, "Vật Lý"),
        (13, "Hóa Học"),
        (14, "Giáo Dục Công Dân"),
        (15, "Khoa Học Tự Nhiên"),
        (16, "Sinh Học")
    )
    TenMonHoc = models.IntegerField(default=0, choices=MonHocOptions)
    GhiChu = models.TextField(null=True)

class Lop(models.Model):
    LopOptions = (
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
    TenLop = models.IntegerField(default=0, choices=LopOptions)
    
class HinhThucDeThi(models.Model):
    HinhThucDeOptions = (
        (0, "Luyện tập trắc nghiệm"),
        (1, "Đề thi thông minh"),
        (2, "Lý thuyết tương tác"),
        (3, "Hỏi và Đáp"),
        (4, "Đề thi Tự luận, chấm điểm trực tiếp lên bài"),
        (5, "Đề thi tắc nghệm từ file PDF hoặc Word"),
        (6, "Đề thi trắc nghiệm từ ma trận")
    )
    HinhThucDe = models.IntegerField(default=0, choices=HinhThucDeOptions)

class CauHoi(models.Model):
    MaDeThi = models.ForeignKey('DeThi', on_delete=models.CASCADE)
    HinhThucCauHoiOption = (
        (0, "Trắc nghiệm"),
        (1, "Tự luận")
    )
    HinhThucCauHoi = models.IntegerField(default=0, choices=HinhThucCauHoiOption)
    NoiDungCauHoi = models.TextField()
    DoKhoOption = (
        (0, "Dễ"),
        (1, "Trung bình"),
        (2, "Khó"),
    )
    DoKho = models.IntegerField(default=0, choices=DoKhoOption)
    GhiChu = models.TextField(null=True)

class DapAn(models.Model):
    CauHoi = models.ForeignKey(CauHoi, on_delete=models.CASCADE)
    NoiDungDapAn = models.TextField(null=True)
    DungSai = models.TextField(null=True)
    GhiChu = models.TextField(null=True)
 
class DeThi(models.Model):
    MaDeThietLap = models.CharField(max_length=10)
    TieuDeBaiThi = models.CharField(max_length=200)
    TacGia = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    TenLopThi = models.ForeignKey(Lop, on_delete=models.SET_NULL, null=True)
    MonThi = models.ForeignKey(MonHoc, on_delete=models.SET_NULL, null=True)
    HinhThucThi = models.ForeignKey(HinhThucDeThi, on_delete=models.SET_NULL, null=True)
    SoLuongCauHoi = models.IntegerField()
    NgayTao = models.DateTimeField(auto_now_add=True)

# class DeThi(models.Model):
#     TacGia = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     TenMonThi = models.ForeignKey(MonThi, on_delete=models.SET_NULL, null=True)
#     MaDe = models.CharField(max_length=10)
#     TenDe = models.TextField()
#     NgayTao = models.DateTimeField(auto_now_add=True)
#     HinhThucDeThi = (
#         (0, "Luyện tập trắc nghiệm"),
#         (1, "Đề thi thông minh"),
#         (2, "Lý thuyết tương tác"),
#         (3, "Hỏi và Đáp"),
#         (4, "Đề thi Tự luận, chấm điểm trực tiếp lên bài"),
#         (5, "Đề thi tắc nghệm từ file PDF hoặc Word"),
#         (6, "Đề thi trắc nghiệm từ ma trận")
#     )
#     HinhThucDe = models.IntegerField(default=0, choices=HinhThucDeThi)
#     ClassForTest = (
#         (0, "Mẫu giáo"),
#         (1, "Lớp 1"),
#         (2, "Lớp 2"),
#         (3, "Lớp 3"),
#         (4, "Lớp 4"),
#         (5, "Lớp 5"),
#         (6, "Lớp 6"),
#         (7, "Lớp 7"),
#         (8, "Lớp 8"),
#         (9, "Lớp 9"),
#         (10, "Lớp 10"),
#         (11, "Lớp 11"),
#         (12, "Lớp 12"),
#         (13, "Đại học")
#     )
#     Lop = models.IntegerField(default=0, choices=ClassForTest)

# class DeVaDapAn(models.Model):
#     MaDe = models.ForeignKey(DeThi, on_delete=models.CASCADE)
#     CauHoi = models.TextField()
#     DapAn = models.TextField()
#     CauHoiSo = models.IntegerField(default=0)
#     NoiDungCauHoi = models.TextField()
#     NoiDungCacDapAn = models.TextField()
#     DapAn = models.TextField()

