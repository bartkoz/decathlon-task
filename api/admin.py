from django.contrib import admin
from .models import Movie, Comment


class MovieAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in
                    Movie._meta.fields if field.attname != "id"]


admin.site.register(Movie, MovieAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in
                    Comment._meta.fields if field.attname != "id"]


admin.site.register(Comment, CommentAdmin)
