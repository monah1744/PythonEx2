from django.contrib import admin
from . import models

# Register your models here.


class CommentsInline(admin.TabularInline):
    model = models.Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'is_deleted', 'author']
    list_display_link = ['title', ]
    # list_editable = ['title']
    inlines = [CommentsInline]
    raw_id_fields = ['author']


admin.site.register(models.PortalUser)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment)
admin.site.register(models.Like)
admin.site.register(models.Source)
admin.site.register(models.Tag)
