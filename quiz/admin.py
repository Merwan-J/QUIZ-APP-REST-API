from django.contrib import admin
from .models import Question,Quiz,Choice, Category
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice

    def get_extra(self, request, obj=None, **kwargs):
        extra = 4
        return extra

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline,]

class QuestionInlince(admin.TabularInline):
    model = Question



admin.site.register(Quiz)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Category)