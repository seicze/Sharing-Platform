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
    type = models.IntegerField()
    user_name = models.CharField(unique=True, max_length=22)
    password = models.CharField(max_length=22)
    real_name = models.CharField(max_length=22, blank=True, null=True)
    tel = models.CharField(max_length=22, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    basic_info = models.CharField(max_length=255, blank=True, null=True)
    money = models.FloatField()

    class Meta:
        managed = False
        db_table = 'account'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    summary = models.CharField(db_column='Summary', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    document_id = models.CharField(db_column='Document_id', max_length=255, blank=True, null=True)  # Field name made lowercase.

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
    send = models.ForeignKey(Account,related_name='sender',on_delete=models.CASCADE)
    receive = models.ForeignKey(Account,related_name='receiver',on_delete=models.CASCADE)
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
