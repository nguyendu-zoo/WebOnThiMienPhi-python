from django.contrib import admin
from .models import User, MonHoc, Lop, HinhThucDeThi, CauHoi,DapAn, DeThi

# Register your models here.
class PostUser(admin.ModelAdmin):
    list_display = ['Username', 'ChucVu', 'GioiThieu']
admin.site.register(User, PostUser)

class PostMonHoc(admin.ModelAdmin):
    list_display = ['TenMonHoc']
admin.site.register(MonHoc, PostMonHoc)

class PostLop(admin.ModelAdmin):
    list_display = ['TenLop']
admin.site.register(Lop, PostLop)

class PostHinhThucDeThi(admin.ModelAdmin):
    list_display = ['HinhThucDe']
admin.site.register(HinhThucDeThi, PostHinhThucDeThi)

class PostCauHoi(admin.ModelAdmin):
    list_display = ['NoiDungCauHoi']
admin.site.register(CauHoi, PostCauHoi)

class PostDapAn(admin.ModelAdmin):
    list_display = ['CauHoi']
admin.site.register(DapAn, PostDapAn)

class PostDeThi(admin.ModelAdmin):
    list_display = ['TieuDeBaiThi', 'NgayTao']
admin.site.register(DeThi, PostDeThi)
