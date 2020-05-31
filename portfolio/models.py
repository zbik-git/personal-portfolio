from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    descripton = models.CharField(max_length=200)
    img = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
