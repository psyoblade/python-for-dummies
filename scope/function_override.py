#!/usr/bin/env python
# -*- coding:utf-8 -*-
import function_original


# 스프링 AOP 같이, 주입 방식은 아니고, 함수 자체를 덮어 써 가능 하다
def override_logging():
    original = function_original.logging

    def custom(*pargs, **kargs):
        import datetime
        started = datetime.datetime.now()
        original(*pargs, **kargs)
        ended = datetime.datetime.now()
        print("Elapsed {}".format(ended - started))

    function_original.logging = custom


function_original.logging("하나", "둘")

override_logging()
function_original.logging("하나", "둘")
