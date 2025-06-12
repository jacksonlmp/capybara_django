from django.db import models
from django.conf import settings

class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name="título")
    body = models.TextField(verbose_name="corpo")
    is_premium = models.BooleanField(default=False, verbose_name="é premium")
    created_at = models.DateTimeField(verbose_name="criado em")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        null=True,
        blank=True,
        on_delete=models.SET_NULL, 
        related_name="created_posts",
        verbose_name="criado por"
    )
    
    published_at = models.DateTimeField(
        null=True, 
        blank=True,
        verbose_name="publicado em"
    )
    published_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name="published_posts",
        verbose_name="publicado por"
    )
        
    updated_at = models.DateTimeField(auto_now=True, verbose_name="criado por")

    class Meta:
        verbose_name = "Postagem do Blog"
        verbose_name_plural = "Postagens do Blog"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
