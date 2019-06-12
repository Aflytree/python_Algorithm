#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2019 Lynxi Ltd. All rights reserved.
#   
#   @name          ：abstractMethod.py
#   @author        ：Afly
#   @date          ：2019.06.12
#   @description   ：
#
#================================================================
import sys

from abc import ABCMeta,abstractmethod
"""
   METHOND:1
   接口
　 定义:一种特殊的类,声明了若干方法,要求继承该接口的类必须实现这种方法
   作用:限制继承接口的类的方法的名称及调用方式,隐藏了类的内部实现
"""
class Payment(metaclass=ABCMeta):
    @abstractmethod#定义抽象方法的关键字
    def pay(self,money):
        pass

    # @abstractmethod
    # def pay(self,money):
    #     raise NotImplementedError

class AiliPay(Payment):
    #子类继承接口,必须实现接口中定义的抽象方法,否则不能实例化对象
    def pay(self,money):
        print('使用支付宝支付%s元'%money)

class ApplePay(Payment):
    def pay(self,money):
        print('使用苹果支付支付%s元'%money)

hial = AiliPay()
hiap = ApplePay()
hial.pay(100)
hiap.pay(200)

"""
    METHOD:2
    一:单例模式

     定义:保证一个类只有一个实例,并提供一个访问它的全局访问点

     适用场景:当一个类只能有一个实例而客户可以从一个众所周知的访问点访问它时

     优点:对唯一实例的受控访问,相当于全局变量,但是又可以防止此变量被篡改
"""
class Singleton(object):
    #如果该类已经有了一个实例则直接返回,否则创建一个全局唯一的实例
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singleton,cls).__new__(cls)
        return cls._instance

class MyClass(Singleton):
    def __init__(self,name):
        if name:
            self.name = name

a = MyClass('a')
print(a)
print(a.name)

b = MyClass('b')
print(b)
print(b.name)

print(a)
print(a.name)
