from django.db import models

class Section8(models.Model):
    client_name = models.CharField(max_length=100)
    client_role = models.CharField(max_length=100)
    client_image = models.ImageField(upload_to='Section8/', blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=5)
    message = models.TextField()
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.client_name} - {self.client_role}"
