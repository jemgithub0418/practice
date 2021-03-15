from django.db import models
from django.utils.translation import ugettext as _


class BlogCategory(models.Model):
    title = models.CharField(
            max_length=256,
            verbose_name = _('Title: '),
            unique=True,
            blank= False,
            null= False
        )

    class Meta:
        verbose_name = _('Blog_Categoty')
        verbose_name_plural = _('Blog_Categories')

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(
            max_length = 256,
            verbose_name = _('Title: '),
            unique=True,
            blank=False,
            null=False,
        )

    slug = models.SlugField(
            max_length=256,
            verbose_name = _('Slug :'),
            unique = True,
            blank = False,
            null = False
        )
