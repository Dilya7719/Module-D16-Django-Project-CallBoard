from django.contrib import admin
from .models import Call, Respond

class RespondAdmin(admin.ModelAdmin):
    list_display = ['respond_accept', 'respond_create_date', 'respond_author', 'respond_call', 'respond_text']
    list_filter = ['respond_call']
    search_fields = ['respond_author']

admin.site.register(Call)
admin.site.register(Respond)