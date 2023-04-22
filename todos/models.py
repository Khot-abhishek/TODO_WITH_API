from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['completed']
    
    # def save(self, *args, **kwargs):
    # #    kwargs['commit']=False
    #    obj = super(Task, self).save(*args, **kwargs)
    #    if self.request:
    #        obj.user = self.request.user.id
    #    obj.save()
    #    return obj
        