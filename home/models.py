from django.db import models
from django.urls import reverse
from accounts.models import User
# Create your models here.
class post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField()
    slug = models.SlugField()
    title = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-created']
    def __str__(self):
        
        return f'{self.slug} - {self.updated}'
    
    def get_absoulot_url(self):
        return reverse('',args=(self.id,self.slug))