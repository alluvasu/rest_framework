from django.contrib import admin

# Register your models here.
from a1.models import Snippet
class SnippetAdmin(admin.ModelAdmin):
    list_display=['created','owner','title','code','linenos','highlighted']
admin.site.register(Snippet,SnippetAdmin)
#
# created = models.DateTimeField ( auto_now_add=True )
# title = models.CharField ( max_length=100 , blank=True , default='' )
# code = models.TextField ( )
# linenos = models.BooleanField ( default=False )
# owner = models.ForeignKey ( 'auth.User' , related_name='snippets' , null=True , blank=True , on_delete=models.CASCADE )
# highlighted = models.TextField ( )