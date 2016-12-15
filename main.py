# -*- coding: utf-8 -*-
from __future__ import unicode_literals #for python2
import codecs
import sys

args = sys.argv
fin  = codecs.open(args[1], 'r', 'utf-8')
doc = fin.readlines()
doc2 = []
for l in doc:
    l = l.replace('、','，')
    l = l.replace('。','．')
    doc2.append(l)
fin.close()
fout = codecs.open(args[1], 'w', 'utf-8')
fout.write(''.join(doc2))
fout.close()
