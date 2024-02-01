from django.shortcuts import render, HttpResponse,redirect
from app01.models import Department,UserInfo

# Create your views here.
def show(request):
    return HttpResponse("欢迎使用")


def user_list(request):
    # 优先去项目的根目录的templates中寻找（提前先配置 不配置就是无效）
    # 根据app的注册顺序，在每个app下的templates目录寻找
    return render(request, "user_list.html")


def user_add(request):
    return render(request, "user_add.html")


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
    res = requests.get(url, headers=headers)
    data_list = res.json()

    return render(request, "news.html", {"news_list": data_list})

def somthing(request):
    # request是一个对象封装了用户通过浏览器发送过来的所有请求和相关的数据

    #  1.获取请求方式 GET/POST
    print(request.method)
    # 2. 在url上传递值（获取url上传递的值somthing/?n1=123&n2=999）
    print(request.GET)
    # 3.在请求体中提交数据
    print(request.POST)
    # 4.[响应]HttpResponse("返回内容"),将字符串内容返回给请求者
    # return HttpResponse("返回内容")

    # 5.[响应]读取HTML的内容 + 渲染(替换) => 字符串,返回给用户浏览器
    # 需要在 app01/templates 下新建`something.html`
    # return render(request,"somthing.html",{"title":"来了"})
    # 6.[响应] 让浏览器重定向到其他的页面
    return redirect("http://www.baidu.com")

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


# 或者可以写为from app01 import models，下面使用为models.Department
def orm(request):
    # 1.新建############
    # Department.objects.create(title="销售部")
    # Department.objects.create(title="IT部")
    # UserInfo.objects.create(name="吴佩奇",password="123",age=18)
    # UserInfo.objects.create(name="sugary", password="123", age=18)
    # UserInfo.objects.create(name="wuyangjun", password="123")

    # 2.删除########
    # UserInfo.objects.filter(id=7).delete()
    # Department.objects.all().delete()

    # ### 3.获取数据 ###
    # 3.1 获取符合条件的所数据
    # data_list = [对象，对象，对象]    QuerySet类型
    # data_list = UserInfo.objects.all()
    # for obj in data_list:
    #     print(obj.id, obj.name, obj.password, obj.age)
    #
    # data_list = [对象，]
    # data_list = UserInfo.objects.filter(id=1)
    # print(data_list)
    # 3.1 获取第一条数据【对象】
    # row_obj = UserInfo.objects.filter(id=1).first()
    # print(row_obj.id, row_obj.name, row_obj.password, row_obj.age)
    # ### 3.更新数据 ###
    UserInfo.objects.all().update(password=999)
    UserInfo.objects.filter(name="sugary").update(age=20)

    return HttpResponse("成功")

def info_list(request):
    # 1.获取数据库中所有的用户信息
    # [对象，对象，对象]
    data_list = UserInfo.objects.all()
    # 渲染，返回给用户
    return render(request, "info_list.html",{"data_list":data_list})

def info_add(request):
    if request.method == "GET":
        return render(request, "info_add.html")
    # 获取用户提交的数据
    username = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")
    # 添加到数据库
    UserInfo.objects.create(name=username,password=pwd,age=age)
    return redirect("/info/list")

def info_delete(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/info/list")