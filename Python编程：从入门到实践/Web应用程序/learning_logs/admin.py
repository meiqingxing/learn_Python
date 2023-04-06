from django.contrib import admin

# Register your models here.

from learning_logs.models import Topic, Entry  # 导入要注册的模型Topic


admin.site.register(Topic)  # 让Django通过管理网站管理我们的模型
admin.site.register(Entry)  # 注册模型Entry

