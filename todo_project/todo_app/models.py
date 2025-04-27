from django.db import models
class Todo_model(models.Model):
    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    


