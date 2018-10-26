from rest_framework import serializers
from .models import Post
# from .models import State
# from .models import Category
# from .models import Qualification
from .models import ImportantDates
from .models import ApplicationFee
from .models import Eligibility
from .models import AgeLimit
from .models import VacancyDetail
from .models import AdmitCards
from .models import Result
from .models import Emails

#
# class StateSerialiazers(serializers.ModelSerializer):
#     class  Meta:
#         model = State
#         fields = ('id','state')
#
#
#
# class StateMiniSerialiazers(serializers.ModelSerializer):
#     class  Meta:
#         model = State
#         fields = ('id','state')
#         extra_kwargs = {
#             'id': {
#                 'read_only': False
#             },
#             'state': {
#                 'validators': [],
#                 'required': False
#             }
#         }



# class CategorySerialiazers(serializers.ModelSerializer):
#     class  Meta:
#         model = Category
#         fields = ('id','category')
#
# class CategoryMiniSerialiazers(serializers.ModelSerializer):
#     class  Meta:
#         model = Category
#         fields = ('id','category')
#         extra_kwargs = {
#             'id': {
#                 'read_only': False
#             },
#             'category': {
#                 'validators': [],
#                 'required': False
#             }
#         }
#
# class QualificationSerialiazers(serializers.ModelSerializer):
#     class  Meta:
#         model = Qualification
#         fields = ('id','qualification')
#
# class QualificationMiniSerialiazers(serializers.ModelSerializer):
#     class  Meta:
#         model = Qualification
#         fields = ('id','qualification')
#         extra_kwargs = {
#             'id': {
#                 'read_only': False
#             },
#             'qualification': {
#                 'validators': [],
#                 'required': False
#             }
#         }

class ImportantDatesSerialiazers(serializers.ModelSerializer):
    class  Meta:
        model = ImportantDates
        fields = ('id','text','content')


class ApplicationFeeSerialiazers(serializers.ModelSerializer):
    class  Meta:
        model = ApplicationFee
        fields = ('id','text','content')

class EligibilitySerialiazers(serializers.ModelSerializer):
    class  Meta:
        model = Eligibility
        fields = ('id','text','content')

class AgeLimitSerialiazers(serializers.ModelSerializer):
    class  Meta:
        model = AgeLimit
        fields = ('id','text','content')

class VacancyDetailSerialiazers(serializers.ModelSerializer):
    class  Meta:
        model = VacancyDetail
        fields = ('id','text','content')


class PostSerialiazers(serializers.ModelSerializer):
    # state = StateMiniSerialiazers()
    # qualification = QualificationMiniSerialiazers()
    # category = CategoryMiniSerialiazers()
    importantdates_set = ImportantDatesSerialiazers(many=True)
    applicationfee_set =  ApplicationFeeSerialiazers(many=True)
    eligibility_set =  EligibilitySerialiazers(many=True)
    agelimit_set =  AgeLimitSerialiazers(many=True)
    vacancydetail_set =  VacancyDetailSerialiazers(many=True)
    def create(self,validated_data):
        post_title = validated_data.get("post_title")
        post_by = validated_data.get("post_by")
        published_date = validated_data.get("published_date")
        last_date = validated_data.get("last_date")
        apply = validated_data.get("apply")
        notification = validated_data.get("notification")
        syllabus = validated_data.get("syllabus")
        o_website = validated_data.get("o_website")
        extra_info = validated_data.get("extra_info")
        short_description = validated_data.get("short_description")
        state = validated_data.get("state")
        qualification = validated_data.get("qualification")
        category = validated_data.get("category")
        new_obj = Post.objects.create(post_title=post_title,post_by=post_by,published_date=published_date,last_date=last_date,
        short_description=short_description,state=state,qualification=qualification,
        category=category,apply=apply,notification=notification,
        syllabus=syllabus,o_website=o_website,extra_info=extra_info
        )
        all_importantdates = validated_data.get('importantdates_set')
        if all_importantdates:
            for each_importantdates in all_importantdates:
                text = each_importantdates.get('text')
                content = each_importantdates.get('content')
                new_obj.importantdates_set.create(text=text, content=content)
        all_applicationfee = validated_data.get('applicationfee_set')
        if all_applicationfee:
            for each_applicationfee in all_applicationfee:
                text = each_applicationfee.get('text')
                content = each_applicationfee.get('content')
                new_obj.applicationfee_set.create(text=text, content=content)
        all_eligibility = validated_data.get('eligibility_set')
        if all_eligibility:
            for each_eligibility in all_eligibility:
                text = each_eligibility.get('text')
                content = each_eligibility.get('content')
                new_obj.eligibility_set.create(text=text, content=content)

        all_agelimit = validated_data.get('agelimit_set')
        if all_agelimit:
            for each_agelimit in all_agelimit:
                text = each_agelimit.get('text')
                content = each_agelimit.get('content')
                new_obj.agelimit_set.create(text=text, content=content)
        all_vacancydetail = validated_data.get('vacancydetail_set')
        if all_vacancydetail:
            for each_vacancydetail in all_vacancydetail:
                text = each_vacancydetail.get('text')
                content = each_vacancydetail.get('content')
                new_obj.vacancydetail_set.create(text=text, content=content)
        return new_obj

    def update(self,instance,validated_data):
        instance.post_title = validated_data.get("post_title",instance.post_title)
        instance.post_by = validated_data.get("post_by",instance.post_by)
        instance.published_date = validated_data.get("published_date",instance.published_date)
        instance.last_date = validated_data.get("last_date",instance.last_date)
        instance.short_description = validated_data.get("short_description",instance.short_description)
        instance.apply = validated_data.get("apply",instance.apply)
        instance.notification = validated_data.get("notification",instance.notification)
        instance.syllabus = validated_data.get("syllabus",instance.syllabus)
        instance.extra_info = validated_data.get("extra_info",instance.extra_info)
        instance.o_website = validated_data.get("o_website",instance.o_website)
        instance.state = validated_data.get("state",instance.state)
        instance.qualification = validated_data.get("qualification",instance.qualification)
        instance.category = validated_data.get("category",instance.category)
        all_importantdates = validated_data.get("importantdates_set")
        if all_importantdates:
            instance.importantdates_set.all().delete()
            for each_importantdates in all_importantdates:
                instance.importantdates_set.create(text=each_importantdates.get('text'),
                                          content=each_importantdates.get('content')
                                          )

        all_applicationfee = validated_data.get("applicationfee_set")
        if all_applicationfee:
            instance.applicationfee_set.all().delete()
            for each_applicationfee in all_applicationfee:
                instance.applicationfee_set.create(text=each_applicationfee.get('text'),
                                          content=each_applicationfee.get('content')
                                          )
        all_eligibility = validated_data.get("eligibility_set")
        if all_eligibility:
            instance.eligibility_set.all().delete()
            for each_eligibility in all_eligibility:
                instance.eligibility_set.create(text=each_eligibility.get('text'),
                                          content=each_eligibility.get('content')
                                          )
        all_agelimit = validated_data.get("agelimit_set")
        if all_agelimit:
            instance.agelimit_set.all().delete()
            for each_agelimit in all_agelimit:
                instance.agelimit_set.create(text=each_agelimit.get('text'),
                                          content=each_agelimit.get('content')
                                          )
        all_vacancydetail = validated_data.get("vacancydetail_set")
        if all_vacancydetail:
            instance.vacancydetail_set.all().delete()
            for each_vacancydetail in all_vacancydetail:
                instance.vacancydetail_set.create(text=each_vacancydetail.get('text'),
                                          content=each_vacancydetail.get('content')
                                          )

        instance.save()
        return instance

    class  Meta:
        model = Post
        fields = ('id', 'post_title', 'post_by' ,'short_description', 'published_date','last_date','importantdates_set','state','qualification','category','applicationfee_set','eligibility_set','agelimit_set','vacancydetail_set','apply','notification','extra_info','o_website','syllabus')

class AdmitCardsSerialiazers(serializers.ModelSerializer):

    def update(self,instance,validated_data):
        instance.post_title = validated_data.get("post_title",instance.post_title)
        instance.post_by = validated_data.get("post_by",instance.post_by)
        instance.apply_link = validated_data.get("apply_link",instance.apply_link)
        instance.img_link = validated_data.get("img_link",instance.img_link)

        instance.save()
        return instance


    class  Meta:
        model = AdmitCards
        fields = ('id','post_title','post_by','apply_link','img_link')

class ResultSerialiazers(serializers.ModelSerializer):

    def update(self,instance,validated_data):
        instance.post_title = validated_data.get("post_title",instance.post_title)
        instance.post_by = validated_data.get("post_by",instance.post_by)
        instance.view_link = validated_data.get("view_link",instance.view_link)
        instance.img_link = validated_data.get("img_link",instance.img_link)

        instance.save()
        return instance


    class  Meta:
        model = Result
        fields = ('id','post_title','post_by','view_link','img_link')

class EmailsSerialiazers(serializers.ModelSerializer):

    def update(self,instance,validated_data):
        instance.email = validated_data.get("email",instance.email)

        instance.save()
        return instance


    class  Meta:
        model = Emails
        fields = ('id','email')
