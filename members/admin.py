from django.contrib import admin
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("firstname", "lastname")}
    list_display = ("firstname", "lastname", "joined_date", "slug")

admin.site.register(Member, MemberAdmin)
