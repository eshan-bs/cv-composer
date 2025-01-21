
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_("email address"), blank=True)
    user_type = models.IntegerField(default=0)

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]


    def __str__(self):
        return self.username

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class CurriculumVitae(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_summary = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    work_experience = models.TextField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)
    languages = models.TextField(blank=True, null=True)
    portfolio_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s CV"

class Project(BaseModel):
    curriculum_vitae = models.ForeignKey(CurriculumVitae, on_delete=models.CASCADE)
    technology = models.CharField(max_length=255)  # Field to store technologies used in the project
    responsibility = models.TextField()  # Field for describing the responsibilities in the project
    project_link = models.URLField(blank=True, null=True)  # Optional field for a project link
    project_duration = models.CharField(max_length=100)  # Duration of the project (e.g., "6 months")
    short_description = models.TextField(blank=True, null=True)  # A brief description of the project

    def __str__(self):
        return f"Project by {self.curriculum_vitae.user.username}"

class TechnicalSkill(BaseModel):
    curriculum_vitae = models.ForeignKey(CurriculumVitae, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # Skill name (e.g., Python, Django, etc.)
    proficiency_level = models.CharField(max_length=50, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert')
    ])  # Proficiency level in the skill

    def __str__(self):
        return f"{self.curriculum_vitae}: {self.name} - {self.proficiency_level}"

