from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100, )
    long_description = RichTextField()
    description = RichTextField(
        blank=True, 
        null=True, 
        config_name='special',
        # external_plugin_resources = [
        #     (
        #         'youtube',
        #         '/static/vendor/ckeditor_plugins/youtube/',
        #         'plugin.js'
        #     )
        # ]
    )

    def __str__(self):
        return self.product_name