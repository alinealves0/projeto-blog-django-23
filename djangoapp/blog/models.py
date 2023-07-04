from django.db import models

class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True, default=None, 
        null=True, blank=True, max_length=255,
    )

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = 'nova_slug'
        return super().save(*args, **kwargs)
