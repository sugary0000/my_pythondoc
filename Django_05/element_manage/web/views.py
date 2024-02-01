from django.shortcuts import render,redirect
from web import models
# Create your views here.
def depart_list(request):
    # 去数据库中获取所有部门信息
    # queryset类型
    data_list = models.Department.objects.all()

    return render(request, "depart_list.html",{"data_list":data_list})
def depart_add(request):
    """添加用户"""
    if request.method == "GET":
        return render(request, "depart_add.html")
    # 拿到的用户填写的title
    title = request.POST.get("title")
    # 将用户填写的title放数据库
    models.Department.objects.create(title=title)
    return redirect("/depart/list/")

def depart_delete(request):
    """删除部门"""
    # 获取ID
    nid = request.GET.get("nid")
    # 删除
    models.Department.objects.filter(id=nid).delete()
    # 跳转回部门列表
    return redirect("/depart/list")

# http://127.0.0.1:8000/depart/4/edit/
def depart_edit(request, nid):
    if request.method == "GET":
    # 根据nid，获取他的数据
        row_obj = models.Department.objects.filter(id=nid).first()
        print(row_obj.id, row_obj.title)
        return render(request, "depart_edit.html",{"title":row_obj.title})
    # 获取用户提交的标题
    new_title = request.GET.get("title")
    # 根据id找到数据库中的数据并进行更新
    models.Department.objects.filter(id=nid).update(title=new_title)
    # 重定向回部门列表
    return redirect("/depart/list/")