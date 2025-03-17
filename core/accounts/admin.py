from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


class CustomUserAmin(UserAdmin):
    model = User
    list_display = ("email", "is_staff", "is_active", "is_verified")
    list_filter = ("email", "is_staff", "is_active", "is_verified")
    search_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        ("Authenticate", {"fields": ("email", "password")}),
        (
            "premition",
            {
                "fields": (
                    "is_active",
                    "is_superuser",
                    "is_staff",
                    "is_verified",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_verified",
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAmin)
admin.site.register(Profile)
