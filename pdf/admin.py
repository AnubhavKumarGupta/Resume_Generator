# In the database, I registerd the schema created in the models.py file here so that we can view its schema by going to /admin panel.


from django.contrib import admin
from .models import Profile
# Register your models here.

admin.site.register(Profile)

