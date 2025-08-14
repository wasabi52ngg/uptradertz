from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify

class MenuItem(models.Model):
    menu_name = models.CharField(verbose_name='Имя меню', max_length=100,
                                 validators=(MinLengthValidator(2, message='Минимум 2 символа'),))
    title = models.CharField(verbose_name='Название пункта', max_length=100,
                             validators=(MinLengthValidator(2, message='Минимум 2 символа'),))
    slug = models.SlugField(max_length=100, editable=False)
    url = models.CharField(verbose_name='URL пункта (опционально, для переопределения)', max_length=255, blank=True, help_text='Явный URL или named URL. Если пусто, используется автоматический иерархический URL.')
    parent = models.ForeignKey('self', verbose_name='Родитель', null=True, blank=True, on_delete=models.CASCADE,
                               related_name='children_set')
    order = models.PositiveIntegerField(verbose_name='Порядок', default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} ({self.menu_name})"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        path = []
        current = self
        while current:
            path.append(current.slug)
            current = current.parent
        path.reverse()
        return f"/menu/{self.menu_name}/{'/'.join(path)}/"