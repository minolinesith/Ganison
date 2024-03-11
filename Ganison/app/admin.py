from django.contrib import admin

# Register your models here.
from . models import School,Class,Assesment_Areas,Student,Answers,Summary,Awards,Subject

from import_export.admin import ImportExportModelAdmin

admin.site.register(School, ImportExportModelAdmin)
admin.site.register(Class, ImportExportModelAdmin)
admin.site.register(Assesment_Areas, ImportExportModelAdmin)
admin.site.register(Student, ImportExportModelAdmin)
admin.site.register(Answers, ImportExportModelAdmin)
admin.site.register(Summary, ImportExportModelAdmin)
admin.site.register(Awards, ImportExportModelAdmin)
admin.site.register(Subject, ImportExportModelAdmin)