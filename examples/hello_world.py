#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
An example showing how to create a "Hello World" class from scratch.
"""
from jawa import ClassFile
from jawa.assemble import assemble

if __name__ == '__main__':
    cf = ClassFile.create('HelloWorld')

    main = cf.methods.create('main', '([Ljava/lang/String;)V', code=True)
    main.access_flags.acc_static = True
    main.code.max_locals = 1
    main.code.max_stack = 2

    main.code.assemble(assemble([
        ('getstatic', cf.constants.field_ref(
            'java/lang/System',
            'out',
            'Ljava/io/PrintStream;'
        )),
        ('ldc', cf.constants.string('Hello World!')),
        ('invokevirtual', cf.constants.method_ref(
            'java/io/PrintStream',
            'println',
            '(Ljava/lang/String;)V'
        )),
        ('return',)
    ]))

    with open('HelloWorld.class', 'wb') as fout:
        cf.save(fout)
