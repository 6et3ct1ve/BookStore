from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    biography = models.TextField()
    birth_year = models.IntegerField()
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
