from django.contrib import admin
from cashbook.models import Movement


@admin.register(Movement)
class MovementAdmin(admin.ModelAdmin):
    pass
