from django.contrib import admin

# Register your models here

from .models import Comments


class CommentsAdmin(admin.ModelAdmin):
    fields = [
        'content',
        'address_type',
        'address_id',
        'address_object'
    ]
    readonly_fields = ['address_object']

    class Meta:
        model = Comments


admin.site.register(Comments)