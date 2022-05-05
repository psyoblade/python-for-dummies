#!/usr/bin/env python
# -*- coning:utf-8 -*-


def nonlocal_closure(start):
    # state = start

    def nested(label):
        nonlocal start
        start += 1
        print("this is {} of state {}".format(label, start))

    return nested


# 함수를 여러개 찍어 내고 싶다면 단순 클로저 사용

started = nonlocal_closure(0)
started('suhyuk')

started = nonlocal_closure(1)
started('kiki')


def method_state_closure(start):
    def nested(label):
        nested.state += 1
        print("this is {} of state {}".format(label, start))

    # 함수 속성의 경우는 함수 선언 이후에 수정이 가능함
    nested.state = start
    return nested


started = method_state_closure(0)
started('suhyuk')

started = method_state_closure(1)
started('kiki')


def tester(start):
    def nested(label):
        print(label, state[0])
        state[0] += 1

    state = [start]
    return nested


started = tester(0)
started('suhyuk')

started = tester(1)
started('kiki')
