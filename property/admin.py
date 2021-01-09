from django.contrib import admin

# Register your models here.
from . models import Property , PropertyBook , PropertyImages , PropertyReview , Category , Place



admin.site.register(Property)
admin.site.register(PropertyBook)
admin.site.register(PropertyImages)