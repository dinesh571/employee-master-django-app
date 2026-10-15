from django.contrib import admin
from .models import (
    Employee,
    PersonalContactDetails,
    EducationalQualification,
    ExperienceHistory,
    EmployeeDocument,
)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "employee_id",
        "first_name",
        "department",
        "designation",
        "status",
    )

    search_fields = (
        "employee_id",
        "first_name",
        "last_name",
    )

    list_filter = (
        "department",
        "status",
    )


admin.site.register(PersonalContactDetails)
admin.site.register(EducationalQualification)
admin.site.register(ExperienceHistory)
admin.site.register(EmployeeDocument)