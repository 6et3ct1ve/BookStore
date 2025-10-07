from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField()
    established = models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
