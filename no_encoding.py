#!/usr/bin/env python2.7

u = u'El Niño'
for codec in ['latin_1', 'utf_8', 'utf_16']:
    print codec + '\t' + u.encode(codec)
