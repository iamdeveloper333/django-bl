from django.db import models
from django.utils import timezone

#
# class State(models.Model):
#     state = models.CharField(max_length=200,unique=True)
#
#     def __str__(self):
#         return self.state
#
# class Category(models.Model):
#     category = models.CharField(max_length=200,unique=True)
#
#     def __str__(self):
#         return self.category
#
# class Qualification(models.Model):
#     qualification = models.CharField(max_length=200,unique=True)
#
#     def __str__(self):
#         return self.qualification

class Post(models.Model):
    state =models.CharField(max_length=200,default=None,null=True)
    category = models.CharField(max_length=200,default=None,null=True)
    qualification = models.CharField(max_length=200,default=None,null=True)
    post_title = models.CharField(max_length=200)
    post_by = models.CharField(max_length=200)
    short_description = models.TextField()
    published_date = models.CharField(max_length=200,default=None,null=True)
    last_date = models.CharField(max_length=200,default=None,null=True)
    apply = models.CharField(max_length=200,blank=True,default=None,null=True)
    notification = models.CharField(max_length=200,blank=True,default=None,null=True)
    syllabus = models.CharField(max_length=200,blank=True,default=None,null=True)
    o_website = models.CharField(max_length=200,blank=True,default=None,null=True)
    extra_info = models.CharField(max_length=200,blank=True,default=None,null=True)

    def __str__(self):
        return self.post_title

class Emails(models.Model):
    email = models.EmailField(max_length=70,default=None,blank=True)

    def __str__(self):
        return self.email

class ImportantDates(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200,default=None,null=True)
    content = models.CharField(max_length=200,default=None,null=True)

    def __str__(self):
        return self.text

class ApplicationFee(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200,default=None,null=True)
    content = models.CharField(max_length=200,default=None,null=True)

    def __str__(self):
        return self.text

class Eligibility(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200,default=None,null=True)
    content = models.CharField(max_length=200,default=None,null=True)

    def __str__(self):
        return self.text

class AgeLimit(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200,default=None,null=True)
    content = models.CharField(max_length=200,default=None,null=True)

    def __str__(self):
        return self.text

class VacancyDetail(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200,default=None,null=True)
    content = models.CharField(max_length=200,default=None,null=True)

    def __str__(self):
        return self.text

class AdmitCards(models.Model):
    post_title = models.CharField(max_length=200)
    post_by = models.CharField(max_length=200)
    apply_link = models.CharField(max_length=200,default=None,null=True)
    img_link = models.CharField(max_length=200,default=None,null=True)

    def __str__(self):
        return self.post_title

class Result(models.Model):
    post_title = models.CharField(max_length=200)
    post_by = models.CharField(max_length=200)
    view_link = models.CharField(max_length=200,default=None,null=True)
    img_link = models.CharField(max_length=200,default=None,null=True)

    def __str__(self):
        return self.post_title
