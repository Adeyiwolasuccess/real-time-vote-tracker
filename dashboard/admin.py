from django.contrib import admin
from .models import Party, PollingUnit, Submission, SubmissionResult


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ("name", "acronym", "created_at")
    search_fields = ("name", "acronym")


@admin.register(PollingUnit)
class PollingUnitAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "state", "lga", "ward", "created_at")
    search_fields = ("name", "code", "state", "lga", "ward")
    list_filter = ("state", "lga", "ward")


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("id", "polling_unit", "submitted_by", "status", "submitted_at")
    search_fields = ("polling_unit__name", "polling_unit__code", "submitted_by__username")
    list_filter = ("status", "submitted_at")


@admin.register(SubmissionResult)
class SubmissionResultAdmin(admin.ModelAdmin):
    list_display = ("submission", "party", "vote_count")
    search_fields = ("party__name", "party__acronym", "submission__polling_unit__code")
    list_filter = ("party",)
