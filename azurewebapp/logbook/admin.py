
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post

admin.site.site_header = 'Team 36 User Login'
admin.site.index_title = 'My Team Blog'

class PostAdmin(admin.ModelAdmin):
    #list_display = ('title','created','updated',)
    search_fields = ['title','text']
    #list_filter = ('Date Created','Date Updated',)


"""
class LogEntryAdmin(admin.ModelAdmin):
 
    search_fields = ['title','text']
    list_display = (
        'author',
        'title', 'text', 'published_date')



    def __init__(self, *args, **kwargs):
        super(LogEntryAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ()
"""

admin.site.register(Post, PostAdmin)
admin.site.unregister(Group)

