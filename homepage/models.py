from django.db import models


# Create your models here.
class Photo(models.Model):
    image_file = models.ImageField(upload_to='original/%Y/%m/%d')
    filtered_image_file = models.ImageField(upload_to='filtered/%Y/%m/%d')
    description = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', '-pk', )

    def delete(self, *args, **kwargs):
        self.image_file.delete()
        self.filtered_image_file.delete()
        super(Photo, self).delete(*args, **kwargs)
