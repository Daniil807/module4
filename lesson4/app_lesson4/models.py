from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=120)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("торг", help_text='отметьте, если торг возможен')
    create_at = models.DateTimeField("создано в",auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='изображение', upload_to='advertisements/', blank=True)

    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.create_at.date() == timezone.now().date():
            created_time = self.create_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;"> Сегодня в {}</span>', created_time
            )
        return self.create_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description='дата обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: blue; font-weight: bold;"> Сегодня в {}</span>', updated_time
            )
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description='изображение')
    def image_img(self):
        if self.image:
            return format_html('<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>', self.image.url)
        
    def __str__(self):
        return f"Advertisement(id+{self.id}, title+{self.title}, price+{self.price})"
    class Meta:
        db_table = "advertisements"

    def get_absolute_url(self):
        return reverse('adv-detail', kwargs={'pk':self.pk})