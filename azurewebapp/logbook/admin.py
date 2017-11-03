
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post

admin.site.site_header = 'Team 36 User Login'

class PostAdmin(admin.ModelAdmin):
    #list_display = ('title','created','updated',)
    search_fields = ['title','text']
    #list_filter = ('Date Created','Date Updated',)


admin.site.register(Post, PostAdmin)
admin.site.unregister(Group)

