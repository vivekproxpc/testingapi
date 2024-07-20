from django.contrib import admin
from .models import Layout, Section, SectionDetail

class SectionDetailInline(admin.StackedInline):
    model = SectionDetail
    extra = 1

class SectionInline(admin.StackedInline):
    model = Section
    extra = 1
    inlines = [SectionDetailInline]

class LayoutAdmin(admin.ModelAdmin):
    inlines = [SectionInline]
    list_display = ['id', 'layout_name', 'slug']
    search_fields = ['layout_name', 'slug']
    prepopulated_fields = {"slug": ("layout_name",)}

admin.site.register(Layout, LayoutAdmin)
admin.site.register(Section)
admin.site.register(SectionDetail)
