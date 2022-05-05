#!/usr/bin/env python
# -*- coding:utf-8 -*-


class MethodClosure:

    def __init__(self, state):
        self.state = state

    def nested(self, label):
        print("this is {} of state {}".format(label, self.state))


# 객체를 통해서 다양한 행위를 하고 싶다면 클래스 객체

started = MethodClosure(0)
started.nested('suhyuk')

started = MethodClosure(1)
started.nested('kiki')


class ConstructorClosure:

    def __init__(self, state):
        self.state = state

    def __call__(self, label):
        print("this is {} of state {}".format(label, self.state))


started = ConstructorClosure(0)
started('suhyuk')
started = ConstructorClosure(1)
started('kiki')


