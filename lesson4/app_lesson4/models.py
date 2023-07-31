from django.db import models

class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=120)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("торг", help_text='отметьте, если торг возможен')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "advertisements"
    def __str__(self):
        return f"Advertisement(id+{self.id}), (title+{self.title}, (price+{self.title}))"