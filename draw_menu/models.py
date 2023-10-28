from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title