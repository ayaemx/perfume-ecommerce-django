from django.db import models
from product.models import Product

class Feedback(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='feedbacks')
    name = models.CharField(max_length=100)  # User's name (or you can use Django's User model)
    comment = models.TextField()
    image = models.ImageField(upload_to='feedback/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Feedback by {self.name} on {self.product.name}"
