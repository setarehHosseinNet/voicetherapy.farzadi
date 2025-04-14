from django.db import models


# Create your models here.
class Article(models.Model):
    ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    Short_description = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    icon_Name = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.title,self.status,self.content


