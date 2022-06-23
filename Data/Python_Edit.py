#!/usr/bin/python
#-*-coding:utf-8-*-

import os
import sys
import shutil
import argparse
from collections import Counter

def __version__():
    return '0.0.1'

def Filelines(Target_File):

    openFileTEX = open(Target_File,'r') 
    i = 0
    done = 0
    while (not done):
        line = openFileTEX.readline()
        if line =='':
            done = 1
        i = i+1
    return i-1
       
def get_footnote(Lines, Orig_File,dict_foot):

    openFileTEX = open(Orig_File,'r') 
#    line = openFileTEX.readline()
    i = 0
    for l in range(Lines):
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

def point_footnote(Lines, Target_File, dict_foot):

    footnote_mark = '\\footnote{'
    openFileTEX = open(Target_File,'r+') 
#    line = openFileTEX.readline()
    i = 0
    for l in range(Lines):
        line = openFileTEX.readline()
        line_i = line.strip('\r\n')
#        i = i+1
        if (line_i == '\\item'):
            break
        linecomm_orig = line_i.split('}{\\textsuperscript{')
        if len(linecomm_orig) > 1:
            for i in linecomm_orig:
#                print (i[-6:])
                j = i.split('\\protect')
                if (len(j)>1):
                   k = j[-1].split('fn')[-1]
#                   print(dict_foot[int(k)])
                   i = i[:-7]+footnote_mark + dict_foot[int(k)]+'}'
#                   print(i)
       for element 
                  

    return

#   MAIN
if __name__ == "__main__":

#    os.rename('POTCAR', 'POTCAR_orig')
#    os.rename('INCAR', 'INCAR_orig')
#    os.rename('KPOINTS', 'KPOINTS_orig')
     Orig_TEX = '../2022-06-16.tex'

     Footnote_Dict ={}
     Num = 0
     Lines = Filelines(Orig_TEX)
     Num = get_footnote(Lines, Orig_TEX, Footnote_Dict)

     Lines = Filelines(Orig_TEX)
     Tar_TEX = 'chap-02.tex'
     point_footnote(Lines, Tar_TEX, Footnote_Dict)

#     print (Footnote_Dict)
#     print (Num)

     print ("All Done!")
