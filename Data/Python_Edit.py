#!/usr/bin/python
#-*-coding:utf-8-*-

import os
import sys
import shutil
import argparse
from collections import Counter

def __version__():
    return '0.0.1'

def get_footnote(Orig_File,dict_foot):

    openFileTEX = open(Orig_File,'r') 
    line = openFileTEX.readline()
    i = 0
    while line:
        line = openFileTEX.readline()
        linecontent = line.strip()
        linefoot = linecontent.strip('\r\n').split('\\')
#        dict_foot = {}
        if (len(linefoot) > 2 and linefoot[1] == 'leavevmode'):
            i = i+1
#            print (linefoot, end = '')
#            footnote = [] 
            footnote_i = ''
#            print (i)
            line = openFileTEX.readline()
            footitem = line.strip('\r\n')
            footnote_i = footnote_i + footitem
            while (footitem !='\\item'):
                  line = openFileTEX.readline()
                  footitem = line.strip('\r\n')
                  if (footitem !='\\item'):
                     footnote_i = footnote_i + footitem
#            j = j+1
#            print(i, footnote_i)
            dict_foot.update({i:footnote_i})
#
#    print (dict_foot[222])
    return i

       


#   MAIN
if __name__ == "__main__":

#    os.rename('POTCAR', 'POTCAR_orig')
#    os.rename('INCAR', 'INCAR_orig')
#    os.rename('KPOINTS', 'KPOINTS_orig')
     Orig_TEX = '../2022-06-16.tex'

     Footnote_Dict ={}
     Num = 0
     Num = get_footnote(Orig_TEX, Footnote_Dict)

     Tar_Tex = 'chap-02.tex'
#     point_footnote(Tar_TEX)

#     print (Footnote_Dict)
#     print (Num)

     print ("All Done!")
