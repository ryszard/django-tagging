from django.contrib import admin
from tagging.models import Tag, TaggedItem

admin.site.register(TaggedItem)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Tag, TagAdmin)

