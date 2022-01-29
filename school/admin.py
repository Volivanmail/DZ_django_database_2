from django.contrib import admin

from .models import Student, Teacher

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']



# admin.site.register(Student, StudentAdmin)
# admin.site.register(Teacher, TeacherAdmin)