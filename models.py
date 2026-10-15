from django.db import models

class Employee(models.Model):

    employee_id = models.CharField(max_length=20, unique=True)

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    gender = models.CharField(max_length=10)

    date_of_birth = models.DateField()

    designation = models.CharField(max_length=100)

    department = models.CharField(max_length=100)

    joining_date = models.DateField()

    status = models.CharField(
        max_length=20,
        default="Active"
    )

    def __str__(self):
        return f"{self.employee_id} - {self.first_name}"

class PersonalContactDetails(models.Model):

    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name="personal_details"
    )

    father_name = models.CharField(max_length=100)

    mother_name = models.CharField(max_length=100)

    marital_status = models.CharField(
        max_length=20,
        choices=[
            ("Single", "Single"),
            ("Married", "Married"),
            ("Divorced", "Divorced"),
        ]
    )

    blood_group = models.CharField(
        max_length=5,
        choices=[
            ("A+", "A+"),
            ("A-", "A-"),
            ("B+", "B+"),
            ("B-", "B-"),
            ("AB+", "AB+"),
            ("AB-", "AB-"),
            ("O+", "O+"),
            ("O-", "O-"),
        ]
    )

    nationality = models.CharField(max_length=50)

    permanent_address = models.TextField()

    current_address = models.TextField()

    personal_email = models.EmailField()

    personal_mobile = models.CharField(max_length=15)

    emergency_contact_name = models.CharField(max_length=100)

    emergency_contact_number = models.CharField(max_length=15)

    emergency_contact_relationship = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.employee.employee_id} - Personal Details"
    
class EducationalQualification(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="educational_qualifications"
    )

    degree = models.CharField(max_length=100)

    specialization = models.CharField(max_length=100)

    institution = models.CharField(max_length=200)

    university = models.CharField(max_length=200)

    year_of_passing = models.PositiveIntegerField()

    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.employee.employee_id} - {self.degree}"

class ExperienceHistory(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="experience_history"
    )

    company_name = models.CharField(max_length=200)

    designation = models.CharField(max_length=100)

    employment_type = models.CharField(
        max_length=30,
        choices=[
            ("Full Time", "Full Time"),
            ("Part Time", "Part Time"),
            ("Contract", "Contract"),
            ("Internship", "Internship"),
            ("Freelance", "Freelance"),
        ]
    )

    start_date = models.DateField()

    end_date = models.DateField()

    currently_working = models.BooleanField(default=False)

    responsibilities = models.TextField()

    skills_used = models.TextField()

    reason_for_leaving = models.TextField()

    def __str__(self):
        return f"{self.employee.employee_id} - {self.company_name}"

class EmployeeDocument(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="documents"
    )

    aadhaar = models.FileField(
        upload_to="documents/aadhaar/",
        blank=True,
        null=True
    )

    pan = models.FileField(
        upload_to="documents/pan/",
        blank=True,
        null=True
    )

    passport = models.FileField(
        upload_to="documents/passport/",
        blank=True,
        null=True
    )

    resume = models.FileField(
        upload_to="documents/resume/",
        blank=True,
        null=True
    )

    profile_photo = models.ImageField(
        upload_to="documents/profile_photo/",
        blank=True,
        null=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.employee.employee_id


class EmployeeCertificate(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="certificates"
    )

    certificate_name = models.CharField(
        max_length=200
    )

    certificate_file = models.FileField(
        upload_to="documents/certificates/"
    )

    issued_by = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    issue_date = models.DateField(
        blank=True,
        null=True
    )

    expiry_date = models.DateField(
        blank=True,
        null=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.employee.employee_id} - {self.certificate_name}"