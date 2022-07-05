from django.contrib import admin
from .models import *

admin.site.register([Games, Feedback, Gacha, Storylines, Characters, CharType, Equipment])

# Register your models here.
