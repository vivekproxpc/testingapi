from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

class Layout(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    layout_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.layout_name)
        super(Layout, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)


class Section(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    layout = models.ForeignKey(Layout, related_name='layouts', on_delete=models.SET_NULL, null=True)
    banner_image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    header = models.TextField(null=True, blank=True)
    content = RichTextUploadingField(null=True, blank=True)
    n_content=models.TextField(null=True, blank=True)
    image= models.ImageField(upload_to='uploads/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return str(self.id)
    
class SectionDetail(models.Model):
    section = models.ForeignKey(Section, related_name='details', on_delete=models.CASCADE)
    heading = models.CharField(max_length=200, null=True, blank=True)
    description = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return f'{self.heading} - {self.section}'    


