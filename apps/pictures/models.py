from django.db import models
from django.utils.safestring import mark_safe


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя', unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Tag(models.Model):
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)

    name = models.CharField(max_length=200, verbose_name='Имя', unique=True)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return '%s | %s' % (self.category.name, self.name)


class Picture(models.Model):
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(to='Tag', blank=True)

    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    is_visible = models.BooleanField(verbose_name='Опубликована?', default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.image.name

    def image_tag(self):
        return mark_safe('<img src="%s" width="500" height="auto" />' % self.image.url)

    image_tag.short_description = 'Изображение'
    image_tag.allow_tags = True
