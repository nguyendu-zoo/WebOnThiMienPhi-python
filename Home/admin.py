from django.contrib import admin
from .models import User, MonHoc, Lop, HinhThucDeThi, CauHoi,DapAn, DeThi

# # Register your models here.

admin.site.register(User)
admin.site.register(MonHoc)
admin.site.register(Lop)
admin.site.register(HinhThucDeThi)
admin.site.register(CauHoi)
admin.site.register(DapAn)
admin.site.register(DeThi)