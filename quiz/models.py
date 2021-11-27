from django.db import models

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Quiz(models.Model):
    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'
        ordering = ['id']
    
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='question')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='choice')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.choice_text
    
