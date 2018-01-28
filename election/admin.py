from django.contrib import admin
from election.models import Survey
from election.models import Question

#django-import-export paketini kullanmaya başladık
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin


class SurveyResource (resources.ModelResource):

    class Meta:
        model = Survey
        fields = ('id','name','created_at','active' ,)

class SurveyAdmin(ImportExportActionModelAdmin):
    resource_class = SurveyResource
    list_display = ('name' , 'active' , 'created_at' , 'updated_at',)
    list_filter = ('active',)
    search_fields = ('name',)

admin.site.register(Survey,SurveyAdmin)


class QuestionResorce (resources.ModelResource):

    class Meta:
        model = Question
        fields = ("id","survey","question_title","choice_one","choice_two","choice_three","choice_four")

class QuestionAdmin(ImportExportActionModelAdmin):
    resources_class = QuestionResorce
    list_display = ("id","survey","question_title" ,"choice_one","choice_two","choice_three","choice_four" ,)
    list_filter = ("question_title",)
    search_fields = ("question_title",)

admin.site.register(Question,QuestionAdmin)


