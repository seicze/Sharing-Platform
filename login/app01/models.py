# from django.db import models
#
# # Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=50)
#     email = models.CharField(max_length=60)
#     password = models.CharField(max_length=20)
#
#     def __str__(self):
#         print(self.username)
#
#
# class app01(models.Model):
#     user_id = models.IntegerField()
#     type = models.IntegerField()
#     user_name = models.CharField(max_length=22)
#     password = models.CharField(max_length=22)
#     real_name = models.CharField(max_length=22)
#     tel = models.CharField(max_length=22)
#     email = models.CharField(max_length=45)
#     basic_info = models.CharField(max_length=255)
#     money = models.FloatField()





# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Project(models.Model):
    project_id = models.AutoField(db_column='Project_id', primary_key=True)  # Field name made lowercase.
    project_name = models.CharField(db_column='Project_name', max_length=255)  # Field name made lowercase.
    institute = models.CharField(db_column='Institute', max_length=255, blank=True, null=True)  # Field name made lowercase.
    direction = models.CharField(db_column='Direction', max_length=255, blank=True, null=True)  # Field name made lowercase.
    introduction = models.CharField(db_column='Introduction', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    experts = models.CharField(db_column='Experts', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Project'


class TMessage(models.Model):
    index = models.BigAutoField(db_column='Index', primary_key=True)  # Field name made lowercase.
    receive_id = models.IntegerField(db_column='Receive_id')  # Field name made lowercase.
    request_id = models.IntegerField(db_column='Request_id')  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=255, blank=True, null=True)  # Field name made lowercase.
    request_date = models.DateTimeField(db_column='Request_date')  # Field name made lowercase.
    send_date = models.DateTimeField(db_column='Send_date')  # Field name made lowercase.
    state = models.PositiveIntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_message'


class Account(models.Model):
    user_id = models.AutoField(primary_key=True)
    type = models.IntegerField(default=1)
    user_name = models.CharField(unique=True, max_length=22)
    password = models.CharField(max_length=22)
    real_name = models.CharField(max_length=22, blank=True, null=True)
    tel = models.CharField(max_length=22, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    basic_info = models.CharField(max_length=255, blank=True, null=True)
    money = models.FloatField(default=0.0)

    class Meta:
        managed = False
        db_table = 'account'


class Essay(models.Model):
    paper_id = models.AutoField(db_column='Paper_id', primary_key=True)  # Field name made lowercase.
    paper_name = models.CharField(db_column='Paper_name', max_length=255)  # Field name made lowercase.
    author_id = models.IntegerField(db_column='Author_id')  # Field name made lowercase.
    author_name = models.CharField(db_column='Author_name', max_length=255)  # Field name made lowercase.
    research_areas = models.CharField(db_column='Research_areas', max_length=255, blank=True, null=True)  # Field name made lowercase.
    introduction = models.CharField(db_column='Introduction', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    institute = models.CharField(db_column='Institute', max_length=255, blank=True, null=True)  # Field name made lowercase.
    openness = models.PositiveIntegerField(db_column='Openness')  # Field name made lowercase.
    public_content = models.CharField(db_column='Public_content', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    published_time = models.DateField(db_column='Published_time', blank=True, null=True)  # Field name made lowercase.
    times_cited = models.PositiveIntegerField(db_column='Times_cited', blank=True, null=True)  # Field name made lowercase.
    price = models.PositiveIntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=8)  # Field name made lowercase.
    download_link = models.CharField(db_column='Download_link', max_length=255, blank=True, null=True)  # Field name made lowercase.
    download_times = models.PositiveIntegerField(db_column='Download_times', blank=True, null=True)  # Field name made lowercase.
    document_id = models.CharField(db_column='Document_id', max_length=255, blank=True, null=True)  # Field name made lowercase.
    keywords = models.CharField(db_column='keywords', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clicks = models.IntegerField(db_column='clicks')
    db = models.CharField(db_column='db', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cssci = models.CharField(db_column='cssci', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'essay'


class Expert(models.Model):
    expert_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    institute = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    direction = models.CharField(max_length=255, blank=True, null=True)
    introduction = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expert'


class Message(models.Model):
    index = models.BigAutoField(primary_key=True)
    send = models.ForeignKey(Account, related_name='sender', on_delete=models.CASCADE)
    receive = models.ForeignKey(Account, related_name='receiver', on_delete= models.CASCADE)
    text = models.ForeignKey('MessageText', models.DO_NOTHING)
    send_date = models.DateTimeField()
    state = models.PositiveIntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'message'


class MessageText(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=4096, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'message_text'


class Patent(models.Model):
    patent_id = models.AutoField(db_column='Patent_id', primary_key=True)  # Field name made lowercase.
    patent_name = models.CharField(db_column='Patent_name', max_length=255)  # Field name made lowercase.
    author_id = models.IntegerField(db_column='Author_id')  # Field name made lowercase.
    author_name = models.CharField(db_column='Author_name', max_length=255)  # Field name made lowercase.
    research_areas = models.CharField(db_column='Research_areas', max_length=255, blank=True, null=True)  # Field name made lowercase.
    introduction = models.CharField(db_column='Introduction', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    institute = models.CharField(db_column='Institute', max_length=255, blank=True, null=True)  # Field name made lowercase.
    openness = models.PositiveIntegerField(db_column='Openness')  # Field name made lowercase.
    public_content = models.CharField(db_column='Public_content', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    published_time = models.DateField(db_column='Published_time', blank=True, null=True)  # Field name made lowercase.
    owner_id = models.IntegerField(db_column='Owner_id')  # Field name made lowercase.
    owner_name = models.CharField(db_column='Owner_name', max_length=255)  # Field name made lowercase.
    price = models.PositiveIntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=8)  # Field name made lowercase.
    download_link = models.CharField(db_column='Download_link', max_length=255, blank=True, null=True)  # Field name made lowercase.
    download_times = models.PositiveIntegerField(db_column='Download_times', blank=True, null=True)  # Field name made lowercase.
    document_id = models.CharField(db_column='Document_id', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patent'

