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
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
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
    depart = models.ForeignKey(to="Department",to_field="id",on_delete=models.CASCADE)
    # ### 3.2 直接将要删除的那个数据置空，这里是将员工所属的部门置空
    # depart = models.Foreignkey(to="Department", to_field="id", null=True,blank=True,on_delete=models.SET_NULL)

    # 在django中做的约束
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)