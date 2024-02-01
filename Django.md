# day5 初识Django

- Python知识点：函数、面向对象
- 前端开发：HTML、CSS、JavaScript、jQuery、BootStrap
- MySql数据库
- Python的Web框架
- - Flask,自身短小精悍+第三方组件
  - Django，内部已经集成了很多组件+第三方组件【主要】

## 1.安装Django

```
pip install django
```

```
c:\python39
- python.exe
- Scripts
  - pip.exe
  - django-admin.exe[工具，创建Django项目中的文件和文件夹
 ]
- Lib
  - 内置模块
  - site-packages
    - openpyxl
    - python-docx
    - fdfhvlahvjkfdhgkjfhgkjdhfgkjdfhgkjdfhkjhgjdhgkljjhkdfajh
    - django【框架的源码】
```

C:\Users\17920\AppData\Roaming\Python\Python38\Scripts

## 2.创建项目

### 终端创建

> django中项目会有一些默认的文件和默认的文件夹。

- 打开终端c 

- 进入某个目录（项目放在哪里）

  ```
  D:/PythonReposity/Django_05
  ```

- 执行命令创建项目

  ```
  "C:\Users\17920\AppData\Roaming\Python\Python38\Scripts\diango-admin.exe" startproject 项目名称
  ```

  ```
  # 如果C:\Users\17920\AppData\Roaming\Python\Python38\Scripts已经加入系统环境变量
  创建项目的命令为
  django-admin startproject 项目名称
  ```

### 基于pycharm创建Django

![image-20240129123325992](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240129123325992.png)

特殊说明

- 命令行，创建的项目是标准的。
- pycharm，在标准的基础上默认加了点东西  
  - 创建了一个templates目录（删除）
  - settings.py中，将57行变成空列表

默认项目的文件介绍

```shell
mysite
├── manage.py			# 项目的管理,包括: 启动项目,创建app, 数据管理【默认放着不动】【***常常用***】
└── mysite
    ├── __init__.py
    ├── settings.py		# 项目配置(模板配置,数据库配置,注册app)【***常常修改***】
    ├── urls.py			# url和函数的对应关系 【***常常修改***】
    ├── asgi.py			# 接收网络请求
    └── wsgi.py			# 接收网络请求
```

简单访问

在 `/root/python/web/web`下新增一个 `views.py` 文件

```python
from django.http import HttpResponse
def index(req):
    return HttpResponse('<h1>welcome to Django</h1>')
```

配置`/root/python/web/web` 下的`urls.py` 文件

```python
from django.contrib import admin
from django.urls import path
from . import views    # 导入我们刚刚创建的views.py文件

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),  # 新增这一行,''为空表示默认访问 ip:端口
]
```

启动

```shell
cd /root/python/web/
python3 manage.py runserver 0.0.0.0:5900
```

浏览器访问测试

![img](https://img-blog.csdnimg.cn/aec928edcbad454fab7170171a2786f1.png)

## 3.创建APP

```
- 项目
  - app,用户管理【表结构、函数、HTML模板、CSS】
  - app，订单管理【表结构、函数、HTML模板、CSS】
  - app，后台管理【表结构、函数、HTML模板、CSS】
  - app，网站 【表结构、函数、HTML模板、CSS】
  - app，API    【表结构、函数、HTML模板、CSS】
  
注意：我们开发比较简洁，用不到多app，一般情况下，项目下创建1个app即可。
```

- 创建app目录，在manage.py所在目录下执行

  ```
   python manage.py startapp app01
  ```

![image-20240129150124272](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240129150124272.png)

通过tree /f

```
├─app01
│  │  admin.py     【固定，不要动】django默认提供了admin后台管理。
│  │  apps.py      【固定，不要动】app启动类
│  │  models.py    【重要】，对数据库操作*********
│  │  tests.py     【固定，不要动】单元测试
│  │  views.py      【重要】，url对应的函数定义在这里*************
│  │  __init__.py
│  │
│  └─migrations    【固定，不要动】数据库变更记录
│          __init__.py
|
└─mysite
    │  asgi.py
    │  settings.py
    │  urls.py    【url->函数】
    │  wsgi.py
    │  __init__.py
    │
    └─__pycache__
            settings.cpython-38.pyc
            __init__.cpython-38.pyc


```

## 4.快速上手

- 确保app已注册【settings.py】

  ![image-20240129152613447](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240129152613447.png)

  

- 编写url和视图函数的对应关系【urls.py】

  ![image-20240130112650774](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240130112650774.png)

- 编写视图函数【views.py】

  <img src="https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240129155113844.png" alt="image-20240129155113844" style="zoom:80%;" />

- 启动django项目

  - 通过命令行启动

    ```
    python manage.py runserver
    ```

  - Pycharm启动

    ![image-20240129171726845](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240129171726845.png)

    

### 4.1 再写一个页面

```
- url -> 函数
- 函数
```

![image-20240129174053397](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240129174053397.png)

### 4.2 template模板

![image-20240129201659310](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240129201659310.png)

## 4.3 静态文件

在开发过程中

- 图片
- CSS
- js

都会当做静态文件处理

1. 在app目录下创建static目录

![image-20240129204817628](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240129204817628.png)

2. 引用静态文件

![image-20240129205141417](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240129205141417.png)

## 5. templates模板语法

 本质上：在HTML中写一些占位符，由数据对这些占位符进行替换和处理

创建一个新的模板页面
编辑`mysite2`下的`urls.py`

```python
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('show/', views.show),
    path('user/list/', views.user_list),
    path('user/add/' , views.user_add),
    path('tpl/' , views.tpl),
]

```

编辑app01下的`views.py`

```python
from django.shortcuts import render
from django.http import HttpResponse

def user_list(request):
    # 1.优先去项目的根目录下寻找
    # 2.根据app的注册顺序去app的目录下templates下寻找
    return render(request, "user_list.html")

def index_app(req):
    return HttpResponse('<h1>welcome to Django blog!</h1>')

# 新增下面的内容
def tpl(request):
    return render(request, "tpl.html")
```

在`app01/templates`下新建`tpl.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Title</title>
</head>
<body>
<h1>模板语法的学习</h1>
</body>
</html>
```

![image-20240130114501622](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240130114501622.png)

#### 单一变量

> 如果说我们从数据库中取到了数据,如何在`html`页面中进行展示呢,这里需要用到templates的基本语法

修改`blog`下的`views.py`

```python
def tpl(request):
    name = "sugary"
    return render(request, "tpl.html", {"name":name})
```

修改`app01/templates`下的`tpl.html`

```html
<body>
    <h1>templates模板语法</h1>
    <li>姓名: {{ name }}</li>
</body>
```

![image-20240130114810786](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240130114810786.png)

> 这样,`name`参数就被传到HTML页面中展示了出来

#### 列表

```python
def tpl(request):
    
    name = "poker"
    role_list = ["管理员", "老师", "保安"]
    
    return render(request, "tpl.html", {"name":name, "n2":roles_list})

<body>
<h1>模板语法的学习</h1>
<li>姓名: {{ n1 }}</li>

<div>{{ n2 }}</div>
<div>{{ n2.0 }}</div>
<div>{{ n2.1 }}</div>
<div>{{ n2.2 }}</div>
</body>
```

![image-20240130114941998](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240130114941998.png)

#### 循环(列表)

修改`blog/templates`下的`tpl.html`

```html

<div>列表循环:
	{% for item in n2 %}
		<span>{{ item }}</span>
	{% endfor %}
</div>
<hr/>
```

![image-20240130115214838](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240130115214838.png)

#### 字典以及循环(字典)

修改`blog`下的`views.py`

```python
def tpl(request):
    name = "sugary"
    role_list = ["管理员", "老师", "保安"]
    user_info = {"name": "lily", "salary": 10000, "role": "CTO"}
    return render(request, "tpl.html", {"n1": name, "n2": role_list, "n3": user_info})
```

修改`blog/templates`下的`tpl.html`

```html
<body>
{{ n3 }}
{{ n3.name }}
{{ n3.salary }}
{{ n3.role }}
<ul>字典循序：
	{% for k,v in n3.items %}
		<li>{{ k }} = {{ v }}</li>
	{% endfor %}
</ul>
<hr/>
</body>
```

![image-20240130115456284](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240130115456284.png)

#### 列表套字典

修改`app01`下的`views.py`

```python
def tpl(request):
    name = "sugary"
    role_list = ["管理员", "老师", "保安"]
    user_info = {"name": "lily", "salary": 10000, "role": "CTO"}
    data_list = [
        {"name": "李四", "salary": 10000, "role": "CTO"},
        {"name": "张三", "salary": 10000, "role": "CTO"},
        {"name": "王五", "salary": 10000, "role": "CTO"}
    ]
    return render(request, "tpl.html", {"n1": name, "n2": role_list, "n3": user_info, "n4": data_list})
```

修改`blog/templates`下的`tpl.html`

```html
<body>
   {{ n4 }}
{{ n4.1.name }}
{{ n4.1.salary }}
{% for item in n4 %}
	<div>{{ item.name }} {{ item.salary }}</div>
{% endfor %}

<hr/> 
</body>
```

![image-20240130115923048](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240130115923048.png)

#### 条件判断

修改`app01/templates`下的`tpl.html`

```html
{% if n1 == "xxx" %}
	<h1>匹配成功</h1>
{% elif n1 == "sugary"%}
	<h1>1111</h1>
{% else %}
	<h1>匹配失败</h1>
{% endif %}
```

> 先介绍这些常用的语法,其实还有很多的语法,感兴趣的可自行百度.

![image-20240130121512564](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240130121512564.png)

### 案例：伪联通新闻中心

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Title</title>
</head>
<body>
<h1>联通新闻中心</h1>
<ul>
		{% for item in news_list %}
			<li>{{ item.new_title }} {{ item.post_time }}</li>
		{% endfor %}
</ul>

</body>
</html>
```

```python
from django.shortcuts import render, HttpResponse

def news(request):
    # 1.定义一些新闻（字典或者列表）或者去数据库
    # 网络请求去联通新闻爬取
    # 向地址https://www.chinaunicom.com.cn/43/menu01/1/news?id=0d8c63f7-e11f-4af5-bb5c-80f8dee3b2e1发送请求
    # 第三方模块requests
    import requests

    headers = {
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        # "Accept - Encoding": "gzip, deflate, br",
        # "Accept - Language": "zh-CN,zh;q=0.9,zh-HK;q=0.8",
        # "Cache - Control": "no - cache",
        # "Connection": "keep - alive",
        # "Cookie": "sessionId = 384c06a80c8e43db884e7a2bc6c",
        # "Host": "www.chinaunicom.com.cn",
        # "Pragma": "no-cache",
        # "Referer": "https://www.chinaunicom.com.cn/43/menu01/1/column05",
        # "Sec-Ch-Ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    url = "https://www.chinaunicom.com.cn/43/menu01/1/news?id=0d8c63f7-e11f-4af5-bb5c-80f8dee3b2e1"
    res = requestsnhgnhgn cb gffgfn.get(url, headers=headers)
    data_list = res.json()

    return render(request, "news.html", {"news_list": data_list})
```

![image-20240130151055659](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240130151055659.png)

## 6.请求和响应

**重定向:** 浏览器向某个网站发送请求,网站返回给浏览器一个新的URL,浏览器去访问这个新的URL地址

![image-20240130160722508](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240130160722508.png)修改`app01`下的`views.py`, 根据情况去掉下面代码的注释进行测试

```python
from django.shortcuts import render, HttpResponse,redirect
def somthing(request):
    # request是一个对象封装了用户通过浏览器发送过来的所有请求和相关的数据

    # 1.[请求]获取请求方式 GET/POST
    print(request.method)
    # 2.[请求] 在url上传递值（获取url上传递的值somthing/?n1=123&n2=999）
    print(request.GET)
    # 3.[请求]在请求体中提交数据
    print(request.POST)
    # 4.[响应]HttpResponse("返回内容"),将字符串内容返回给请求者
    # return HttpResponse("返回内容")

    # 5.[响应]读取HTML的内容 + 渲染(替换) => 字符串,返回给用户浏览器
    # 需要在 app01/templates 下新建`something.html`
    # return render(request,"somthing.html",{"title":"来了"})
    # 6.[响应] 让浏览器重定向到其他的页面
    return redirect("http://www.baidu.com")

```

修改`mysite2/mysite2/urls.py`,增加`something`

```python
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('show/', views.show),
    path('user/list/', views.user_list),
    path('user/add/' , views.user_add),
    path('tpl/' , views.tpl),
    # 联通新闻中心
    path('news/', views.news),
    # 请求和相应
    path('somthing/', views.somthing),
]
```

#### 案例: 用户登录

![image-20240130165801380](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240130165801380.png)

修改`app01`下的`views.py`,新增`login`函数

```python
def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        # 如果是post请求，应该是获取用户提交的数据
        username = request.POST.get("user")
        password = request.POST.get("pwd")
        if username == "sugary" and password == "123":
            # return HttpResponse("登录成功")
            return redirect("http://www.baidu.com")
        else:
            # return HttpResponse("登录失败")
            return render(request,"login.html",{"error_msg":"用户名或者密码错误"})
```

上述代码还可以简化为（因为if要是不执行，会自动return）

```python
def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    # 如果是post请求，应该是获取用户提交的数据
    username = request.POST.get("user")
    password = request.POST.get("pwd")
    if username == "sugary" and password == "123":
        # return HttpResponse("登录成功")
        return redirect("http://www.baidu.com")
    # return HttpResponse("登录失败")
    return render(request,"login.html",{"error_msg":"用户名或者密码错误"})
```

修改`mysite/mysite/urls.py`,增加`login`

```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # 请求和相应
    path('somthing/', views.somthing),
    # 用户登录
    path('login/',views.login)
]
```

在`app01/templates`下新建`login.html`

> {% csrf_token %} 必须加上

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Title</title>
</head>
<body>
<h1>用户登录</h1>
<form method="post" action="/login/">
    
	{% csrf_token %}
    
	<input type="text" name="user" placeholder="请输入用户名">
	<input type="password" name="pwd" placeholder="请输入密码">
	<input type="submit" value="提交"/>
	<span style="color:red">{{ error_msg }}</span>
</form>
</body>
</html>
```

浏览器访问,输入错误的用户名和密码

![image-20240130202429283](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240130202429283.png)

## 7.数据库操作

Django开发操作数据库更简单,内部提供了ORM框架

![image-20240130213816067](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240130213816067.png)

#### 安装第三方模块

> mysqlclient

```shell
pip3 install mysqlclient
```

#### ORM

ORM可以帮助我们做两件事:

- 创建/修改/删除数据库中的表（不需要我们写SQL语句）(无法创建数据库)
- 操作表中的数据（不需要我们写SQL语句）

##### 创建数据库

- 启动mysql服务

```sql
create database mydb DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```

![image-20240130221511415](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240130221511415.png)

##### Django连接数据库

修改`mysite/mysite/settings.py`
![image-20240131124936681](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240131124936681.png)
增加如下内容

```python
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'dj_05',
        'USER':'root',
        'PASSWORD':'Huawei12#$%',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}
```

##### Django操作表

- 创建表
- 删除表
- 修改表

配置`app01`下的`models.py`

> 会根据自定义的类创建跟app同名的表

```python
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    age = models.IntegerField()

"""
create table UserInfo(
    id bigint auto_increment primary key,
    name varchar(20),
    password varchar(20),
    age int
)
"""
```

在服务器中项目根目录下执行命令

> 如果不想要某个表了,将class类注释后,重新执行下面的命令即可

```shell
python3 manage.py makemigrations
python3 manage.py migrate
```

由于执行上述命令没反应执行下面的命令可以成功创建表

```
py manage.py makemigrations
py manage.py migrate
```

注意: app需要提前注册
![在这里插入图片描述](https://img-blog.csdnimg.cn/d74b70e0aaf346dfa1f606638e15b0aa.png)
查看Mysql数据库
![image-20240131132609380](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240131132609380.png)

在表中新增列时，由于已存在列中已有数据，所以新增列必须要制定新增列对应的数据。

修改表的话,如果原表中存有数据,此时如果增加一个新的列,需要设定一个默认值

- 1.手动输入一个值

  ```
  size = models.IntegerField()
  ```

  然后执行py manage.py makemigrations选择1，为这行添加数据，再执行py manage.py migrate。

  ![image-20240131145856308](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240131145856308.png)

- 2.设置默认值

```python
age = models.IntegerField(default=2)
```

- 3.允许为空

```python
data = models.IntegerField(null=True, blank=True)
```

以后再开发中如果想要对表结构进行调整：

- 在models.py文件中操作类即可

- 命令

  ```
  py manage.py makemigrations
  py manage.py migrate
  ```

### 4.Django操作表数据

- 添加数据

修改`app01`下的`views.py`

```python
from blog.models import UserInfo
...

def orm(request):
    # 新建数据
    UserInfo.objects.create(name="poker", password="123", age=25)
    UserInfo.objects.create(name="roker", password="456", age=30)

    return HttpResponse("成功")
```

修改`mysite/mysite/urls.py`,增加`orm`

```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index_app/', views.index_app),
    path('user_list/', views.user_list),
    path('tpl/', views.tpl),
    path('something/', views.something),
    path('login/', views.login),
    path('orm/', views.orm),
]
```

浏览器访问页面
![image-20240131152022549](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240131152022549.png)
查看Mysql数据库
![在这里插入图片描述](https://img-blog.csdnimg.cn/1c5306636d94469193592ddad18fc4d2.png)

- 删除数据

```python
	# 删除数据
    UserInfo.objects.filter(id=2).delete()
    # 删除表中所有数据
    UserInfo.objects.all().delete()
```

- 获取数据

```python
# ### 3.获取数据 ###
    # 3.1 获取符合条件的所数据
    # data_list = [对象，对象，对象]    QuerySet类型
    data_list = UserInfo.objects.all()
    for obj in data_list:
        print(obj.id, obj.name, obj.password, obj.age)

    data_list = [对象，]
    data_list = UserInfo.objects.filter(id=1)
    print(data_list)
    # 3.1 获取第一条数据【对象】
    row_obj = UserInfo.objects.filter(id=1).first()
    print(row_obj.id, row_obj.name, row_obj.password, row_obj.age)
```

浏览器刷新访问,观察工作台输出
![在这里插入图片描述](https://img-blog.csdnimg.cn/04cc285ab9994510b7458ba3ec0e87a0.png)

- 更新数据

```python
UserInfo.objects.all().update(password=999)
UserInfo.objects.filter(name="sugary").update(age=20)
```

![image-20240131154745796](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240131154745796.png)

#### 案例:用户管理

1.展示用户列表

- url
- 函数
  - 获取所有用户信息
  - HTML渲染

##### 展示用户列表

修改`mysite/mysite/urls.py`,增加`info/list`

```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index_app/', views.index_app),
    path('user_list/', views.user_list),
    path('tpl/', views.tpl),
    path('something/', views.something),
    path('login/', views.login),
    path('orm/', views.orm),
    path('info/list/', views.info_list)
]
```

修改`app01`下的`views.py`

```python
from blog.models import UserInfo
...
def info_list(request):
    # 1.获取数据库中所有的用户信息
    # [对象，对象，对象]
    data_list = UserInfo.objects.all()
    # 渲染，返回给用户
    return render(request, "info_list.html",{"data_list":data_list})
```

在`app01/templates`下新增`info_list.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>姓名</th>
                <th>密码</th>
                <th>年龄</th>
            </tr>
        </thead>
        <tbody>
            {% for obj in data_list %}
                <tr>
                    <td>{{ obj.id }}</td>
                    <td>{{ obj.name }}</td>
                    <td>{{ obj.password }}</td>
                    <td>{{ obj.age }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```

浏览器访问测试![image-20240131161643845](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240131161643845.png)

##### 添加用户

- url
- 函数
  - GET，看到页面，输入内容
  - POST，提交->写入到数据库

修改`mysite2/mysite2/urls.py`,增加`info/list`

```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index_app/', views.index_app),
    path('user_list/', views.user_list),
    path('tpl/', views.tpl),
    path('something/', views.something),
    path('login/', views.login),
    path('orm/', views.orm),
    path('info/list/', views.info_list),
    path('info/add/', views.info_add),
]
```

修改`app01`下的`views.py`

```python
def info_add(request):
    if request.method == "GET":
        return render(request, "info_add.html")
    # 获取用户提交的数据
    username = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")
    # 添加到数据库
    UserInfo.objects.create(name=username,password=pwd,age=age)

    # 自动跳转
    # return        redirect("http://127.0.0.1:8000//info/list/")
    return redirect("/info/list/")
```

在`app01/templates`下新增`info_add.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Title</title>
</head>
<body>
<h1>添加用户</h1>
<form method="post" action="/info/add/">

    {% csrf_token %}

	<input type="text" name="user" placeholder="用户名">
	<input type="text" name="pwd" placeholder="密码">
	<input type="text" name="age" placeholder="年龄">
	<input type="submit" value="提交"/>

</form>
</body>
</html>
```

浏览器访问
![在这里插入图片描述](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/eba6ee3613fa4591827e17f83f19a07d.png)
点击"提交"
![image-20240131171606156](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240131171606156.png)
在`info/list`页面增加"添加"按钮
修改`app01`/templates`下`info_list.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Title</title>
</head>
<body>
<h1>INFO列表</h1>
<a href="/info/add">添加用户</a>
<table border="1 ">
	<thead>
	<tr>
		<td>ID</td>
		<td>姓名</td>
		<td>密码</td>
		<td>年龄</td>
	</tr>
	</thead>
	<tbody>
	{% for obj in data_list %}
	<tr>
		<td>{{ obj.id}}</td>
		<td>{{ obj.name }}</td>
		<td>{{ obj.password }}</td>
		<td>{{ obj.age }}</td>
	</tr>
	{% endfor %}
	</tbody>
</table>
</body>
</html>
```

![image-20240131171955368](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240131171955368.png)
点击"添加"后,即可跳转回添加页面

##### 删除用户

修改`mysite2/mysite2/urls.py`,增加`info/list`

```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index_app/', views.index_app),
    path('user_list/', views.user_list),
    path('tpl/', views.tpl),
    path('something/', views.something),
    path('login/', views.login),
    path('orm/', views.orm),
    path('info/list/', views.info_list),
    path('info/add/', views.info_add),
    path('info/delete/', views.info_delete)
]
```

修改`blog`下的`views.py`

```python
def info_delete(request):
    nid = request.GET.get("nid")
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/info/list/")
```

```html
```



# day 6 Django开发

主题：员工管理系统

### 1.新建项目 

新建Django项目

### 2.创建app

由于在开发中一般不会命名为app，所以这里命名为web

```
python manage.py startapp web
```

或者通过下面方式创建

![image-20240131175556635](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240131175556635.png)

- 设计部门表与员工表结构

### 3.创建表结构

修改`web/models.py`

```python
from django.db import models

# Create your models here.
class Department(models.Model):
    """部门表"""
    # verbose_name='标题'这句是对这句代码进行注解，怕后面不知道这代码是干嘛用的
    title = models.CharField(verbose_name='标题', max_length=32)

class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=32)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额")
    creat_time = models.DateTimeField(verbose_name="入职时间")
    # 无约束
    # depart_id = models.BigIntegerField(verbose_name="部门ID")

    # 有约束
    #  - to,与哪张表关联
    #  - to_field,与表中的哪一列关联
    # 2.Django自动
    # - 写的depart，生成数据列 depart_id
    # 3部门表被删除,员工所属部门也需要被删除
    # ### 3.1 级联删除
    depart = models.ForeignKey(to="Department",to_field="id",on_delete=models. )
    # ### 3.2 直接将要删除的那个数据置空，这里是将员工所属的部门置空
    # depart = models.Foreignkey(to="Department", to_field="id", null=True,blank=True,on_delete=models.SET_NULL)

    # 在django中做的约束
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices="gender_choice")
```



![image-20240131193118142](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240131193118142.png)

### 4.在MySql中生成表

- 工具连接mysql生成数据库

```sql
create database dj_06 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```

- 修改配置文件连接mysql

  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'dj_06',
          'USER':'root',
          'PASSWORD':'Huawei12#$%',
          'HOST':'127.0.0.1',
          'PORT':3306,
      }
  }
  ```

- django命令生成数据库表

```
py manage.py makemigrations
py manage.py migrate
```

![image-20240131221551674](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240131221551674.png)

- 表结构创建成功

![image-20240131221449086](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240131221449086.png)

### 5.静态文件管理

![image-20240201114737815](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240201114737815.png)

### 6.部门管理

>体验，最原始的方式来做
>
>Django中提供For和ModelForm组件，这个组件非常方便

#### 6.1部门列表

修改`element_manage/element_manage/urls.py`

```python
from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('depart/list/', views.depart_list),
]

```

修改`web/views.py`

```python
from django.shortcuts import render,redirect
from web import models
# Create your views here.
def depart_list(request):
    # 去数据库中获取所有部门信息
    # queryset类型
    data_list = models.Department.objects.all()
```

新建`web/depart/list`

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>员工管理系统</title>

	<link rel="stylesheet" href="{% static "plugins/bootstrap-3.4.1-dist/css/bootstrap.min.css" %}"/>
	<style>
        .navbar {
            border-radius: 0;
        }
	</style>
</head>
<body>
<div class="navbar navbar-default">
	<div class="container">
		<!-- Brand and toggle get grouped for better mobile display -->
		<div class="navbar-header">
			<button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
			        data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
				<span class="sr-only">Toggle navigation</span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
			</button>
			<a class="navbar-brand" href="#">员工管理系统</a>
		</div>

		<!-- Collect the nav links, forms, and other content for toggling -->
		<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
			<ul class="nav navbar-nav">
				<li><a href="/depart/list">部门管理</a></li>
				<li><a href="#">Link</a></li>

			</ul>
			<ul class="nav navbar-nav navbar-right">
				<li><a href="#">登录</a></li>
				<li class="dropdown">
					<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
					   aria-expanded="false">sugary<span class="caret"></span></a>
					<ul class="dropdown-menu">
						<li><a href="#">个人资料</a></li>
						<li><a href="#">我的信息</a></li>
						<li role="separator" class="divider"></li>
						<li><a href="#">注销</a></li>
					</ul>
				</li>
			</ul>
		</div><!-- /.navbar-collapse -->
	</div><!-- /.container-fluid -->
</div>

<div class="container">
	<div style="margin-bottom:10px">
		<a class="btn btn-success" href="/depart/add/" target="blank">
			<span class="glyphicon glyphicon-plus" aria-hidden="true"></span>
			新建部门
		</a>
	</div>

	<div class="panel panel-default">
		<!-- Default panel contents -->
		<div class="panel-heading">
			<span class="glyphicon glyphicon-th-list" aria-hidden="true"></span>部门列表
		</div>

		<!-- Table -->
		<table class="table">
			<thead>
			<tr>
				<th>ID</th>
				<th>部门名称</th>
				<th>操作</th>
			</tr>
			</thead>
			<tbody>
			{% for obj in data_list %}
			<tr>
				<th scope="row">{{ obj.id }}</th>
				<td>{{ obj.title }}</td>
				<td>
					<a class="btn btn-primary btn-xs">编辑</a>
					<a class="btn btn-danger btn-xs">删除</a>
				</td>
			</tr>
			{% endfor %}
			</tbody>
		</table>
	</div>
</div>

<script src="{% static "js/jquery-3.7.1.min.js" %}"></script>
<script src="{% static "plugins/bootstrap-3.4.1-dist/js/bootstrap.js" %}"></script>
</body>
</html>
```

![image-20240201214434324](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240201214434324.png)

#### 6.2部门添加

修改`element_manage/element_manage/urls.py`

```python
from django.contrib import admin
from django.urls import path
from employee_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add),
]
```

修改`element_manage/web/views.py`

```python
def depart_add(request):
    """部门添加"""
    if request.method == "GET":
        return render(request, "depart_add.html")

    # 获取用户提交的部门数据
    title = request.POST.get("title")

    # 保存到数据库
    Department.objects.create(title=depart_title)

    return redirect("/depart/list/")
```

在`element_manage/web/templates`下新建`depart_add.html`

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>员工管理系统</title>

	<link rel="stylesheet" href="{% static "plugins/bootstrap-3.4.1-dist/css/bootstrap.min.css" %}"/>
	<style>
        .navbar {
            border-radius: 0;
        }
	</style>
</head>
<body>
<div class="navbar navbar-default">
	<div class="container">
		<!-- Brand and toggle get grouped for better mobile display -->
		<div class="navbar-header">
			<button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
			        data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
				<span class="sr-only">Toggle navigation</span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
			</button>
			<a class="navbar-brand" href="#">员工管理系统</a>
		</div>

		<!-- Collect the nav links, forms, and other content for toggling -->
		<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
			<ul class="nav navbar-nav">
				<li><a href="/depart/list">部门管理</a></li>
				<li><a href="#">Link</a></li>

			</ul>
			<ul class="nav navbar-nav navbar-right">
				<li><a href="#">登录</a></li>
				<li class="dropdown">
					<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
					   aria-expanded="false">sugary<span class="caret"></span></a>
					<ul class="dropdown-menu">
						<li><a href="#">个人资料</a></li>
						<li><a href="#">我的信息</a></li>
						<li role="separator" class="divider"></li>
						<li><a href="#">注销</a></li>
					</ul>
				</li>
			</ul>
		</div><!-- /.navbar-collapse -->
	</div><!-- /.container-fluid -->
</div>

<div>
	<div class="container">
		<div class="panel panel-default">
			<div class="panel-heading">
				<h3 class="panel-title">新建部门</h3>
			</div>
			<div class="panel-body">
				<form method="post">
{% csrf_token %}
					<div class="form-group">
						<label>标题</label>
						<input type="text" class="form-control" name="title" placeholder="标题"/>
					</div>

					<button type="submit" class="btn btn-primary">保存</button>
				</form>
			</div>
		</div>
	</div>
</div>

<script src="{% static "js/jquery-3.7.1.min.js" %}"></script>
<script src="{% static "plugins/bootstrap-3.4.1-dist/js/bootstrap.js" %}"></script>
</body>
</html>
```

![image-20240201214551055](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240201214551055.png)
![image-20240201214529900](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240201214529900.png)

#### 6.3部门删除

这里删除之后id不连续是因为id是主键，如果从表中删除某一行，其主键值不分配给新行。

修改`element_manage/element_manage/urls.py`

```python
from django.contrib import admin
from django.urls import path
from employee_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add),
    path('depart/delete/', views.depart_delete),
]
```

修改`element_manage/web/views.py`

```python
def depart_delete(request):
    """部门删除"""

    nid = request.GET.get('nid')
    Department.objects.filter(id=nid).delete()

    # 重定向回部门列表
    return redirect("/depart/list/")
```

在`element_manage/web/templates`的`depart_add.html`修改如下内容

```html
<tbody>
{% for obj in data_list %}
	<tr>
		<th scope="row">{{ obj.id }}</th>
		<td>{{ obj.title }}</td>
		<td>
			<a class="btn btn-primary btn-xs">编辑</a>
			<a class="btn btn-danger btn-xs" href="/depart/delete/?nid={{ obj.id }}">
				删除
			</a>
		</td>
	</tr>
{% endfor %}
</tbody>
```

![image-20240201214907884](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240201214907884.png)

#### 6.4部门编辑

修改`element_manage/element_manage/urls.py`

```python
from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add),
    path('depart/delete/', views.depart_delete),
    path('depart/<int:nid>/edit/', views.depart_edit),
]
```

修改`element_manage/web/views.py`

```python
def depart_edit(request, nid):
    """部门编辑"""

    if request.method == "GET":
        # 根据nid,获取数据
        row_object = Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html', {"row_object": row_object})
    
    # 如果是POST请求,保存修改
    depart_title = request.POST.get('depart_title')
    Department.objects.filter(id=nid).update(title=depart_title)

    # 重定向回部门列表
    return redirect('/depart/list/')
```


修改`element_manage/web/templates/depart_list.html`

`<a class="btn btn-primary btn-xs" href="/depart/{{ obj.id}}/edit/">编辑</a>`

```html
<tbody>
{% for obj in data_list %}
	<tr>
		<th scope="row">{{ obj.id }}</th>
		<td>{{ obj.title }}</td>
		<td>
			<a class="btn btn-primary btn-xs" href="/depart/{{ obj.id}}/edit/">编辑</a>
			<a class="btn btn-danger btn-xs" href="/depart/delete/?nid={{ obj.id }}">
				删除
			</a>
		</td>
	</tr>
{% endfor %}
</tbody>
```

![image-20240201223029778](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240201223029778.png)

新增`element_manage/web/templates/depart_edit.html`

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>员工管理系统</title>

	<link rel="stylesheet" href="{% static "plugins/bootstrap-3.4.1-dist/css/bootstrap.min.css" %}"/>
	<style>
        .navbar {
            border-radius: 0;
        }
	</style>
</head>
<body>
<div class="navbar navbar-default">
	<div class="container">
		<!-- Brand and toggle get grouped for better mobile display -->
		<div class="navbar-header">
			<button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
			        data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
				<span class="sr-only">Toggle navigation</span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
			</button>
			<a class="navbar-brand" href="#">员工管理系统</a>
		</div>

		<!-- Collect the nav links, forms, and other content for toggling -->
		<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
			<ul class="nav navbar-nav">
				<li><a href="/depart/list">部门管理</a></li>
				<li><a href="#">Link</a></li>

			</ul>
			<ul class="nav navbar-nav navbar-right">
				<li><a href="#">登录</a></li>
				<li class="dropdown">
					<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
					   aria-expanded="false">sugary<span class="caret"></span></a>
					<ul class="dropdown-menu">
						<li><a href="#">个人资料</a></li>
						<li><a href="#">我的信息</a></li>
						<li role="separator" class="divider"></li>
						<li><a href="#">注销</a></li>
					</ul>
				</li>
			</ul>
		</div><!-- /.navbar-collapse -->
	</div><!-- /.container-fluid -->
</div>

<div>
	<div class="container">
		<div class="panel panel-default">
			<div class="panel-heading">
				<h3 class="panel-title">新建部门</h3>
			</div>
			<div class="panel-body">
				<form method="post">
{% csrf_token %}
					<div class="form-group">
						<label>修改部门</label>
						<input type="text" class="form-control" name="title" value="{{ title }}" placeholder="标题"/>
					</div>

					<button type="submit" class="btn btn-primary">保存</button>
				</form>
			</div>
		</div>
	</div>
</div>

<script src="{% static "js/jquery-3.7.1.min.js" %}"></script>
<script src="{% static "plugins/bootstrap-3.4.1-dist/js/bootstrap.js" %}"></script>
</body>
</html>
```

![image-20240201223636953](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240201223636953.png)

浏览器访问`/depart/list/`,点击"编辑"
![image-20240201224008063](https://gitee.com/sugary0000/typora_image_store/raw/master/typora_images/image-20240201224008063.png)
修改后"保存"观察数据变化

11
