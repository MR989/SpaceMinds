from django.db import models

# Create your models here.

class Blogpost(models.Model):
    post_id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    heading = models.CharField(max_length=500,default="")
    content_heading = models.TextField(max_length=500,default="")
    
    sub_head1 = models.CharField(max_length=500,default="")
    content_sub_head1 = models.TextField(max_length=500,default="")
    
    sub_head2 = models.CharField(max_length=500,default="")
    content_sub_head2 = models.TextField(max_length=500,default="")
    
   

    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='blogs/static/imag',default="")

    def __str__(self):
        return self.title