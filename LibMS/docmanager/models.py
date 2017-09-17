from django.db import models

# Create your models here.
class Author(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)

    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)

class Document(models.Model):
    TYPE_CHOICE = [(0, "Book"), (1, "Thesis")]
    author = models.ForeignKey(Author, null=False)
    ISBN = models.CharField(max_length=13, null=False)
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=256, null=True, blank=True)
    doc_type = models.IntegerField(choices=TYPE_CHOICE, null=False)
    release_date = models.DateField(null=True, blank=True)
    
    class Meta:
        unique_together = ('ISBN', )
