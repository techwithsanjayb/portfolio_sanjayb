from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator
# Create your models here.

class article_category(models.Model):
    name = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category_status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "article_categories"
        ordering = ['published_date']
    
    def __str__(self):
        return self.name


class article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    article_category_belongs_to = models.ForeignKey(article_category,on_delete=models.CASCADE)
    body = RichTextField()
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = (('Published', 'PUBLISHED'),('Unpublished', 'UNPUBLISHED'))
    article_published_status = models.CharField(max_length=20, choices=status, default="Unpublished")
    article_thumbnail_image = models.ImageField(upload_to="core/article", validators=[FileExtensionValidator(allowed_extensions=["jpg", "png", "JPEG", "svg"])],
    height_field=None, width_field=None, max_length=None, null=True, blank=True)
    article_document_file = models.FileField(upload_to="core/article",validators=[FileExtensionValidator(['pdf', 'zip', 'csv', 'xls', 'ppt', 'html'])], null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "articles"
        ordering = ['published_date']

    def __str__(self):
        return self.title
