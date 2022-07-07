#!/usr/bin/python
#-*-coding:utf-8-*-

import os
import sys
import shutil
import argparse
from collections import Counter

def __version__():
    return '0.0.1'

def Exec_shell(Shell_command, Target_File):
    Shell_Exe = Shell_command+' '+ Target_File

    print (Shell_Exe)
    os.system(Shell_Exe)
    return

#   MAIN
if __name__ == "__main__":

#    os.rename('POTCAR', 'POTCAR_orig')
#    os.rename('INCAR', 'INCAR_orig')
#    os.rename('KPOINTS', 'KPOINTS_orig')

     Shell_com = './Edit_Manual_Script.sh'
     for i in range(1, 10):
         part = '0' + str(i)
#         print (part)
         for j in range(1, 26):
             if j < 10 :
                 sect = '0' + str(j)
             else:
                 sect = str(j)
             
             file_name = 'chap-'+ part+'-'+ sect +'.tex'
             file_back = 'chap-'+ part+'-'+ sect +'back.tex'
#             print (file_name)
             if os.path.exists(file_name):
             
#                 print(file_name)
                 shutil.copyfile(file_name, file_back)
                 Exec_shell(Shell_com, file_name)

                 os.remove(file_back)
     print ("All Done!")
