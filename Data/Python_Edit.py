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
       
def Get_footnote(Lines, Orig_File,dict_foot):

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
            footnote_i=footnote_i.split('\\protect\\hyperlink{fnref')[-2]
#            print(i, footnote_i)
            dict_foot.update({i:footnote_i})
#
#    print (dict_foot[222])
    return i

def Point_footnote(Lines, Target_File, Target_File_mod, dict_foot):

    footnote_mark = '\\footnote{'
    openFileTEX = open(Target_File,'r') 
    openTarTEX = open(Target_File_mod,'w') 
#    line = openFileTEX.readline()
    i = 0
    for l in range(Lines):
        line = openFileTEX.readline()
        line_i = line.strip('\r\n')
#        i = i+1
        if (line_i == '\\item'):
            break
        linecomm_orig = line_i.split('}{\\textsuperscript')
        if len(linecomm_orig) > 1:
            test = ''
            for i in linecomm_orig:
#                print (i[-6:])
                j = i.split('\\protect')
                if (len(j)>1):
                   k = j[-1].split('fn')[-1]
#                   print(dict_foot[int(k)])
                   i = i[:-7]+footnote_mark+dict_foot[int(k)]
#                   print(i)
                test = test + i   
#       for element 
            line = test +'\n'
#            print(line)
        openTarTEX.write(line)
                  
    return

def Exec_shell(Shell_command, Target_File):
    Shell_Exe = Shell_command+' '+ Target_File

    print (Shell_Exe)
    os.system(Shell_Exe)
    return

def Setseper(Lines, Target_File, Target_File_mod):
    Seper1 ='\\hspace{40pt}~'
    Seper2 ='\\hspace{30pt}~'
    Seper3 ='\\hspace{20pt}~'
    Seper4 ='\\hspace{10pt}~'

    openFileTEX = open(Target_File,'r') 
    openTarTEX = open(Target_File_mod,'w') 
    for l in range(Lines):
        line = openFileTEX.readline()
        line_i = line.strip('\r\n')
        linecomm_orig = line_i.split('\\ ')
        linecomm_orig[0] = linecomm_orig[0]+Seper1
        test = ''
        for i in linecomm_orig:
            test = test+i
        line =test+'\n'
        openTarTEX.write(line)
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
     Num = Get_footnote(Lines, Orig_TEX, Footnote_Dict)

     Lines = Filelines(Orig_TEX)

     state = sys.argv[1]
     if (state == '1'):
         Shell_com = './Script_Single.sh'
         mod_state = '_Single.'
     else:
         Shell_com = './Script_Multi.sh'
         mod_state = '_Multi.'

     for i in range(1,10):

         Tar_TEX = 'chap-0'+str(i) +'.tex'
         File_name = Tar_TEX.split('.')
         Tar_mod_TEX = File_name[0]+ mod_state + File_name[1]
         Point_footnote(Lines, Tar_TEX, Tar_mod_TEX, Footnote_Dict)


         Exec_shell(Shell_com, Tar_mod_TEX)

   #  Setseper(Lines, Tar_TEX, Tar_mod_TEX)

     
#     print (Footnote_Dict)
#     print (Num)

     print ("All Done!")
