from django.db import models
from django.contrib.postgres.fields import ArrayField

from apps.core.models import CreatedModifiedDateTimeBase

# Create your models here.


class Tag(CreatedModifiedDateTimeBase):
    # id=None # If you don't want the default id to be created
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(CreatedModifiedDateTimeBase):
    cat = models.CharField(max_length=100)

    def __str__(self):
        return self.cat


class Resources(CreatedModifiedDateTimeBase):
    user_id = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL)
    cat_id = models.ForeignKey(
        "resources.Category", default=1, on_delete=models.SET_DEFAULT
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=500)
    tags = models.ManyToManyField("resources.Tag", through="ResourcesTag")
    rate = ArrayField(base_field=models.IntegerField())  # INT ARRAY

    def __str__(self):
        return f"{self.user_id.username} - {self.title}"


class ResourcesTag(CreatedModifiedDateTimeBase):
    modified_at = None
    resources_id = models.ForeignKey("resources.Resources", on_delete=models.CASCADE)
    tag_id = models.ForeignKey("resources.Tag", on_delete=models.CASCADE)


class Review(CreatedModifiedDateTimeBase):
    user_id = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL)
    resources_id = models.ForeignKey("resources.Resources", on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return f"{self.user_id.username} - {self.resources_id.title}"
