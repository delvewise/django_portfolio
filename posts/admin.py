from django.contrib import admin

from .models import Author, Category, Post, Comment, PostView, Resume, Skill

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(Post)
admin.site.register(Resume)
admin.site.register(Comment)
admin.site.register(PostView)
