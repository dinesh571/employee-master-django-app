from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import (
    Employee,
    PersonalContactDetails,
    EducationalQualification,
    ExperienceHistory,
    EmployeeDocument,
    EmployeeCertificate
)


# ==========================================================
# DASHBOARD
# ==========================================================

@login_required(login_url="login")
def dashboard(request):
    return render(request, "dashboard.html")


# ==========================================================
# EMPLOYEE CRUD
# ==========================================================

@login_required(login_url="login")
def employee_list(request):

    employees = Employee.objects.all().order_by("employee_id")

    context = {
        "employees": employees
    }

    return render(
        request,
        "employee_list.html",
        context
    )


@login_required(login_url="login")
def add_employee(request):

    if request.method == "POST":

        Employee.objects.create(

            employee_id=request.POST.get("employee_id"),

            first_name=request.POST.get("first_name"),

            last_name=request.POST.get("last_name"),

            email=request.POST.get("email"),

            phone=request.POST.get("phone"),

            gender=request.POST.get("gender"),

            date_of_birth=request.POST.get("date_of_birth"),

            designation=request.POST.get("designation"),

            department=request.POST.get("department"),

            joining_date=request.POST.get("joining_date"),

        )

        messages.success(
            request,
            "Employee added successfully."
        )

        return redirect("employee_list")

    return render(
        request,
        "add_employee.html"
    )


@login_required(login_url="login")
def employee_detail(request, id):

    employee = get_object_or_404(
        Employee,
        id=id
    )

    context = {
        "employee": employee
    }

    return render(
        request,
        "employee_detail.html",
        context
    )


@login_required(login_url="login")
def edit_employee(request, id):

    employee = get_object_or_404(
        Employee,
        id=id
    )

    if request.method == "POST":

        employee.employee_id = request.POST.get("employee_id")

        employee.first_name = request.POST.get("first_name")

        employee.last_name = request.POST.get("last_name")

        employee.email = request.POST.get("email")

        employee.phone = request.POST.get("phone")

        employee.gender = request.POST.get("gender")

        employee.date_of_birth = request.POST.get("date_of_birth")

        employee.designation = request.POST.get("designation")

        employee.department = request.POST.get("department")

        employee.joining_date = request.POST.get("joining_date")

        employee.save()

        messages.success(
            request,
            "Employee updated successfully."
        )

        return redirect("employee_list")

    context = {
        "employee": employee
    }

    return render(
        request,
        "edit_employee.html",
        context
    )


@login_required(login_url="login")
def delete_employee(request, id):

    employee = get_object_or_404(
        Employee,
        id=id
    )

    employee.delete()

    messages.success(
        request,
        "Employee deleted successfully."
    )

    return redirect("employee_list")
# ==========================================================
# PERSONAL & CONTACT DETAILS CRUD
# ==========================================================

@login_required(login_url="login")
def personal_details_list(request):

    details = PersonalContactDetails.objects.select_related(
        "employee"
    ).all()

    context = {
        "details": details
    }

    return render(
        request,
        "personal_details_list.html",
        context
    )


@login_required(login_url="login")
def add_personal_details(request, employee_id):

    employee = get_object_or_404(
        Employee,
        id=employee_id
    )

    if request.method == "POST":

        PersonalContactDetails.objects.create(

            employee=employee,

            father_name=request.POST.get("father_name"),

            mother_name=request.POST.get("mother_name"),

            marital_status=request.POST.get("marital_status"),

            blood_group=request.POST.get("blood_group"),

            nationality=request.POST.get("nationality"),

            permanent_address=request.POST.get("permanent_address"),

            current_address=request.POST.get("current_address"),

            personal_email=request.POST.get("personal_email"),

            personal_mobile=request.POST.get("personal_mobile"),

            emergency_contact_name=request.POST.get("emergency_contact_name"),

            emergency_contact_number=request.POST.get("emergency_contact_number"),

            emergency_contact_relationship=request.POST.get(
                "emergency_contact_relationship"
            ),
        )

        messages.success(
            request,
            "Personal details added successfully."
        )

        return redirect("personal_details_list")

    context = {
        "employee": employee
    }

    return render(
        request,
        "add_personal_details.html",
        context
    )


@login_required(login_url="login")
def view_personal_details(request, id):

    detail = get_object_or_404(
        PersonalContactDetails,
        id=id
    )

    return render(
        request,
        "view_personal_details.html",
        {
            "detail": detail
        }
    )


@login_required(login_url="login")
def edit_personal_details(request, id):

    detail = get_object_or_404(
        PersonalContactDetails,
        id=id
    )

    if request.method == "POST":

        detail.father_name = request.POST.get("father_name")

        detail.mother_name = request.POST.get("mother_name")

        detail.marital_status = request.POST.get("marital_status")

        detail.blood_group = request.POST.get("blood_group")

        detail.nationality = request.POST.get("nationality")

        detail.permanent_address = request.POST.get(
            "permanent_address"
        )

        detail.current_address = request.POST.get(
            "current_address"
        )

        detail.personal_email = request.POST.get(
            "personal_email"
        )

        detail.personal_mobile = request.POST.get(
            "personal_mobile"
        )

        detail.emergency_contact_name = request.POST.get(
            "emergency_contact_name"
        )

        detail.emergency_contact_number = request.POST.get(
            "emergency_contact_number"
        )

        detail.emergency_contact_relationship = request.POST.get(
            "emergency_contact_relationship"
        )

        detail.save()

        messages.success(
            request,
            "Personal details updated successfully."
        )

        return redirect("personal_details_list")

    return render(
        request,
        "edit_personal_details.html",
        {
            "detail": detail
        }
    )


@login_required(login_url="login")
def delete_personal_details(request, id):

    detail = get_object_or_404(
        PersonalContactDetails,
        id=id
    )

    detail.delete()

    messages.success(
        request,
        "Personal details deleted successfully."
    )

    return redirect("personal_details_list")

# ==========================================================
# EDUCATIONAL QUALIFICATION CRUD
# ==========================================================

@login_required(login_url="login")
def education_list(request):

    educations = EducationalQualification.objects.select_related(
        "employee"
    ).all()

    context = {
        "educations": educations
    }

    return render(
        request,
        "education_list.html",
        context
    )


@login_required(login_url="login")
def add_education(request, employee_id):

    employee = get_object_or_404(
        Employee,
        id=employee_id
    )

    if request.method == "POST":

        EducationalQualification.objects.create(

            employee=employee,

            degree=request.POST.get("degree"),

            specialization=request.POST.get("specialization"),

            institution=request.POST.get("institution"),

            university=request.POST.get("university"),

            year_of_passing=request.POST.get("year_of_passing"),

            percentage=request.POST.get("percentage"),

        )

        messages.success(
            request,
            "Educational Qualification Added Successfully."
        )

        return redirect("education_list")

    return render(
        request,
        "add_education.html",
        {
            "employee": employee
        }
    )


@login_required(login_url="login")
def view_education(request, id):

    education = get_object_or_404(
        EducationalQualification,
        id=id
    )

    return render(
        request,
        "view_education.html",
        {
            "education": education
        }
    )


@login_required(login_url="login")
def edit_education(request, id):

    education = get_object_or_404(
        EducationalQualification,
        id=id
    )

    if request.method == "POST":

        education.degree = request.POST.get("degree")

        education.specialization = request.POST.get("specialization")

        education.institution = request.POST.get("institution")

        education.university = request.POST.get("university")

        education.year_of_passing = request.POST.get("year_of_passing")

        education.percentage = request.POST.get("percentage")

        education.save()

        messages.success(
            request,
            "Educational Qualification Updated Successfully."
        )

        return redirect("education_list")

    return render(
        request,
        "edit_education.html",
        {
            "education": education
        }
    )


@login_required(login_url="login")
def delete_education(request, id):

    education = get_object_or_404(
        EducationalQualification,
        id=id
    )

    education.delete()

    messages.success(
        request,
        "Educational Qualification Deleted Successfully."
    )

    return redirect("education_list")
# ==========================================================
# EXPERIENCE HISTORY CRUD
# ==========================================================

@login_required(login_url="login")
def experience_list(request):

    experiences = ExperienceHistory.objects.select_related(
        "employee"
    ).all()

    context = {
        "experiences": experiences
    }

    return render(
        request,
        "experience_list.html",
        context
    )


@login_required(login_url="login")
def add_experience(request, employee_id):

    employee = get_object_or_404(
        Employee,
        id=employee_id
    )

    if request.method == "POST":

        ExperienceHistory.objects.create(

            employee=employee,

            company_name=request.POST.get("company_name"),

            designation=request.POST.get("designation"),

            employment_type=request.POST.get("employment_type"),

            start_date=request.POST.get("start_date"),

            end_date=request.POST.get("end_date"),

            currently_working=(
                "currently_working" in request.POST
            ),

            responsibilities=request.POST.get("responsibilities"),

            skills_used=request.POST.get("skills_used"),

            reason_for_leaving=request.POST.get("reason_for_leaving")

        )

        messages.success(
            request,
            "Experience Added Successfully."
        )

        return redirect("experience_list")

    return render(
        request,
        "add_experience.html",
        {
            "employee": employee
        }
    )


@login_required(login_url="login")
def view_experience(request, id):

    experience = get_object_or_404(
        ExperienceHistory,
        id=id
    )

    return render(
        request,
        "view_experience.html",
        {
            "experience": experience
        }
    )


@login_required(login_url="login")
def edit_experience(request, id):

    experience = get_object_or_404(
        ExperienceHistory,
        id=id
    )

    if request.method == "POST":

        experience.company_name = request.POST.get("company_name")

        experience.designation = request.POST.get("designation")

        experience.employment_type = request.POST.get("employment_type")

        experience.start_date = request.POST.get("start_date")

        experience.end_date = request.POST.get("end_date")

        experience.currently_working = (
            "currently_working" in request.POST
        )

        experience.responsibilities = request.POST.get(
            "responsibilities"
        )

        experience.skills_used = request.POST.get(
            "skills_used"
        )

        experience.reason_for_leaving = request.POST.get(
            "reason_for_leaving"
        )

        experience.save()

        messages.success(
            request,
            "Experience Updated Successfully."
        )

        return redirect("experience_list")

    return render(
        request,
        "edit_experience.html",
        {
            "experience": experience
        }
    )


@login_required(login_url="login")
def delete_experience(request, id):

    experience = get_object_or_404(
        ExperienceHistory,
        id=id
    )

    experience.delete()

    messages.success(
        request,
        "Experience Deleted Successfully."
    )

    return redirect("experience_list")

@login_required(login_url="login")
def document_list(request):

    documents = EmployeeDocument.objects.select_related(
        "employee"
    ).all()

    return render(
        request,
        "document_list.html",
        {
            "documents": documents
        }
    )

@login_required(login_url="login")
def add_document(request, employee_id):

    employee = get_object_or_404(
        Employee,
        id=employee_id
    )

    if request.method == "POST":

        EmployeeDocument.objects.create(

            employee=employee,

            aadhaar=request.FILES.get("aadhaar"),

            pan=request.FILES.get("pan"),

            passport=request.FILES.get("passport"),

            resume=request.FILES.get("resume"),

            profile_photo=request.FILES.get("profile_photo")

        )

        certificates = request.FILES.getlist("certificate")

        for certificate in certificates:
            EmployeeCertificate.objects.create(
                employee=employee,
                certificate_name=certificate.name,
                certificate_file=certificate
            )

        messages.success(
            request,
            "Documents Uploaded Successfully."
        )

        return redirect("document_list")

    return render(
        request,
        "add_document.html",
        {
            "employee": employee
        }
    )

@login_required(login_url="login")
def view_document(request, id):

    document = get_object_or_404(
        EmployeeDocument,
        id=id
    )

    certificates = EmployeeCertificate.objects.filter(
        employee=document.employee
    )

    return render(
        request,
        "view_document.html",
        {
            "document": document,
            "certificates": certificates,
        }
    )

@login_required(login_url="login")
def delete_document(request, id):

    document = get_object_or_404(
        EmployeeDocument,
        id=id
    )

    document.delete()

    messages.success(
        request,
        "Document Deleted Successfully."
    )

    return redirect("document_list")