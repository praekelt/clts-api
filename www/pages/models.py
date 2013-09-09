from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):

        if not self.id:
            print 'pewpewpew'
            self.slug = slugify(unicode(self.name))
        return super(Category, self).save(*args, **kwargs)


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    content = models.TextField()
    
    class Meta:
        pass

    def __unicode__(self):
        return self.title


