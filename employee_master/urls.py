from django.urls import path
from .views import *

urlpatterns = [

    # ==========================
    # Dashboard
    # ==========================
    path(
        "dashboard/",
        dashboard,
        name="employee_dashboard"
    ),

    # ==========================
    # Employee Management
    # ==========================
    path(
        "employees/",
        employee_list,
        name="employee_list"
    ),

    path(
        "employees/add/",
        add_employee,
        name="add_employee"
    ),

    path(
        "employees/<int:id>/",
        employee_detail,
        name="employee_detail"
    ),

    path(
        "employees/edit/<int:id>/",
        edit_employee,
        name="edit_employee"
    ),

    path(
        "employees/delete/<int:id>/",
        delete_employee,
        name="delete_employee"
    ),

    # ==========================
    # Personal Contact Details
    # ==========================
    path(
        "personal-details/",
        personal_details_list,
        name="personal_details_list"
    ),

    path(
        "personal-details/add/<int:employee_id>/",
        add_personal_details,
        name="add_personal_details"
    ),

    path(
        "personal-details/view/<int:id>/",
        view_personal_details,
        name="view_personal_details"
    ),

    path(
        "personal-details/edit/<int:id>/",
        edit_personal_details,
        name="edit_personal_details"
    ),

    path(
        "personal-details/delete/<int:id>/",
        delete_personal_details,
        name="delete_personal_details"
    ),

    # ==========================
    # Educational Qualification
    # ==========================
    path(
        "education/",
        education_list,
        name="education_list"
    ),

    path(
        "education/add/<int:employee_id>/",
        add_education,
        name="add_education"
    ),

    path(
        "education/view/<int:id>/",
        view_education,
        name="view_education"
    ),

    path(
        "education/edit/<int:id>/",
        edit_education,
        name="edit_education"
    ),

    path(
        "education/delete/<int:id>/",
        delete_education,
        name="delete_education"
    ),

    # ==========================
    # Experience History
    # ==========================
    path(
        "experience/",
        experience_list,
        name="experience_list"
    ),

    path(
        "experience/add/<int:employee_id>/",
        add_experience,
        name="add_experience"
    ),

    path(
        "experience/view/<int:id>/",
        view_experience,
        name="view_experience"
    ),

    path(
        "experience/edit/<int:id>/",
        edit_experience,
        name="edit_experience"
    ),

    path(
        "experience/delete/<int:id>/",
        delete_experience,
        name="delete_experience"
    ),

    # ==========================
    # Employee Documents
    # ==========================
    path(
        "documents/",
        document_list,
        name="document_list"
    ),

    path(
        "documents/add/<int:employee_id>/",
        add_document,
        name="add_document"
    ),

    path(
        "documents/view/<int:id>/",
        view_document,
        name="view_document"
    ),

    path(
        "documents/delete/<int:id>/",
        delete_document,
        name="delete_document"
    ),

]