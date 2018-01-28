#kendi kullanıcı modelimizi yazdık

from django.db import models

class Survey(models.Model):
    name = models.CharField('Araştırma Adı', max_length=100)
    active = models.BooleanField('Aktif mi?', null=False, blank=False, default=False)
    created_at = models.DateTimeField('Oluşturulma Tarihi', null=True, blank=True, auto_now=True)
    updated_at = models.DateTimeField('Güncellenme Tarihi', null=True, blank=True, auto_now_add=True)

    class Meta:
        verbose_name = 'Araştırma'
        verbose_name_plural = 'Araştırmalar'

    def __str__(self):
        return str(self.name)


class Question (models.Model):
    survey = models.ForeignKey(Survey,verbose_name='Arastirma',null=False,blank=False)
    question_title = models.CharField("Sorunuz",max_length=150)
    choice_one = models.CharField("A-",max_length=50)
    choice_two = models.CharField("B-",max_length=50)
    choice_three = models.CharField("C-",max_length=50)
    choice_four=models.CharField("D-",max_length=50)

    class Meta:
         verbose_name = 'Soru'
         verbose_name_plural='Sorular'


    def __str__(self):
         return str(self.question_title)

#bu kısmı hazırladıktan sonra konsoldan
#python manage.py makemigrations election
#python manage.py migrate
#bu sekilde Question class'ı DB'de bir tabloya dönüştürdük


