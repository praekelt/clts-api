from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    content = models.TextField()
    
    class Meta:
        pass

    def __unicode__(self):
        return self.title
