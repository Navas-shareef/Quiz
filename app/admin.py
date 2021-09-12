from django.contrib import admin
from .models import Quiz,Quiz_questions,Quiz_records

# Register your models here.

admin.site.register(Quiz)
admin.site.register(Quiz_questions)
admin.site.register(Quiz_records)
