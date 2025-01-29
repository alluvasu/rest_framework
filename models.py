from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
# Create your models here.
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    owner = models.ForeignKey ( 'auth.User' , related_name='snippets' ,null=True,blank=True, on_delete=models.CASCADE)
    highlighted = models.TextField ( )

    def save(self , *args , **kwargs) :
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """

        linenos = 'table' if self.linenos else False
        options = {'title' : self.title} if self.title else {}

        super ( ).save ( *args , **kwargs )






