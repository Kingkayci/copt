from django.contrib import admin
from .models import UploadedImage, UploadKYC

# Register your models here.
admin.site.register(UploadedImage)
admin.site.register(UploadKYC)