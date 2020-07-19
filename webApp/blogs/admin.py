from django.contrib import admin

# Register your models here.
from blogs.models import Blogpost

admin.site.register(Blogpost)