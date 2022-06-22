#!/usr/bin/python
#-*-coding:utf-8-*-

import os
import sys
import shutil
import argparse
from collections import Counter

def __version__():
    return '0.0.1'

def get_poscar(NUM, REMOVE_I):
    move=[]
    i=0
    j=0
    k=0 
    openFileCON=open('../CONTCAR','r') 
    openFilePOS=open('../POSCAR','r') 
    writeFileHandle=open('Temp','w') 
#    execu1="sed -n 6p POSCAR | wc -w > "
#    NUM_ATOM=os.system(execu1)
#    print NUM_ATOM

    while 1:
        line=openFileCON.readline()
        line=line.strip('\r\n')
        lineapp=openFilePOS.readline()
        lineapp=lineapp.strip('\r\n')
        atom_mov=lineapp.split()
        if lineapp:
            i=i+1
            linewrite=True
            rem1=0
            line=line+' '+atom_mov[-3]+' '+atom_mov[-2]+' '+atom_mov[-1]

            for DELLINE in NUM:
                if i==(DELLINE+8):
                    linewrite=False
                    j=j+1
#                    print (j)
#                    print "%d:%s"%(DELLINE,line)
                    move.append(line)
                else:
                    if i < 9:
                        continue
#                    continue
#                    print (i)
#                   i=i+1
            writeLine='%s\n'%line
            if i==7:
#                line=line.strip('\r\n')
                Num_Atom=line.split()
                print "%s %s" %(Num_Atom[0], Num_Atom[1])
                Num_Atom[0]=int(Num_Atom[0])-int(REMOVE_I[1])
                Num_Atom[1]=int(Num_Atom[1])-int(REMOVE_I[2])
                writeLine='%s %s %s \n' %(Num_Atom[0], Num_Atom[1],len(NUM))
            if linewrite: 
                writeFileHandle.write(writeLine) 
#               writeFileHandle.write(line)

        else:
#            writeLine='\n'
#            writeFileHandle.write(writeLine)
            break
    while k < j:
        k=k+1
        writebottom='%s\n'%move[k-1]
        writeFileHandle.write(writebottom)
#        print "%d,"%DELLINE

    openFileCON.close()
    openFilePOS.close()
    writeFileHandle.close()

    return 

def replace_position(NUM, REMOVE_I, ADD_ELEMENT):
    move=[]
    i=0
    j=0
    k=0 
    openFileCON=open('../../CONTCAR','r') 
    openFilePOS=open('POSCAR','r') 
    writeFileHandle=open('Temp','w') 
#    execu1="sed -n 6p POSCAR | wc -w > "
#    NUM_ATOM=os.system(execu1)
#    print NUM_ATOM

    while 1:
        line=openFileCON.readline()
        line=line.strip('\r\n')
        lineapp=openFilePOS.readline()
        lineapp=lineapp.strip('\r\n')
        if lineapp:
            i=i+1
            linewrite=True
            rem1=0
            line=line+lineapp[43:]

            for DELLINE in NUM:
                if i==(DELLINE+8):
                    linewrite=False
                    j=j+1
#                    print (j)
#                    print "%d:%s"%(DELLINE,line)
                    move.append(line)
#                    print (move[j-1])
                else:
                    if i < 9:
                        continue
#                    print (i)
#                   i=i+1
            writeLine='%s\n'%line
            if i==1:
                writeLine='%s:%s\n' %(line, ADD_ELEMENT)
            if i==6:
                writeLine='%s %s\n' %(line, ADD_ELEMENT)
                ELEMENTS=writeLine
            if i==7:
#                line=line.strip('\r\n')
                Num_Atom=line.split()
                print "%s %s" %(Num_Atom[0], Num_Atom[1])
                Num_Atom[0]=int(Num_Atom[0])-int(REMOVE_I[1])
                Num_Atom[1]=int(Num_Atom[1])-int(REMOVE_I[2])
                writeLine='%s %s %s \n' %(Num_Atom[0], Num_Atom[1],len(NUM))
            if linewrite: 
                writeFileHandle.write(writeLine) 
#               writeFileHandle.write(line)

        else:
#            writeLine='\n'
#            writeFileHandle.write(writeLine)
            break
    while k < j:
        k=k+1
        writebottom='%s\n'%move[k-1]
        writeFileHandle.write(writebottom)
#        print "%d,"%DELLINE

    openFileCON.close()
    openFilePOS.close()
    writeFileHandle.close()

    return ELEMENTS

def get_exe_file(exe_file='standard.lsf'):
    file_exe=open(exe_file,'w')
    MPIRUN_CONTENTS="""#可执行脚本的基本格式：
nohup mpirun -np 2 /home/jun_jiang/Softs/VASP/vasp.5.4.1/bin/vasp_std > vasp.log & """
#    MPIRUN_CONTENTS="""#lsf脚本的基本格式：
##队列名,有系统管理员分配，一般不需要修改
#APP_NAME=scinormal
##该参数不建议修改
#NP_PER_NODE=16
##mpi 的类型，该参数不建议修改
#MY_MPI_TYPE=openmpi
##mpi 的路径，在系统下，可以通过which mpicc查看
#MY_MPI_HOME=/share/software/openmpi/icc-12.1.4/openmpi-1.6.3-icc
##任务调用的核心数，为NP_PER_NODE的整数倍将获得更好的计算效率，该参数根据任务计算量大小常调整
#NP=32
##命令行参数
#RUN="~/Softs/VASP/vasp.5.4.1/bin/vasp_std > vasp.log"
##vasp：RUN="vasp"
##lammps:RUN="lmp_openmpi < relax.in > relax.log"
## nohup mpirun -np 2 /home/jun_jiang/Softs/VASP/vasp.5.4.1/bin/vasp > vasp.log &
## nohup /home/jun_jiang/Softs/VASP/vasp.5.4.1/bin/vasp > vasp.log &
##gaussian09:RUN="g09 in.gjf"
##GMX:RUN="mdrun input.file"
##fortan:RUN="run.file" """
    file_exe.write(MPIRUN_CONTENTS)
    file_exe.close
    get_exe='chmod +x standard.lsf'
    os.system(get_exe)
    return exe_file


def print_Kpoint():
    file_Kpoint=open('KPOINTS', 'w')
    KPOINTS_content="""Automatic mesh
0           # number of k-points = 0 ->automatic generation scheme
Monkhorst-Pack       # generate a Monkhors-Pack grid
1 4 1       # subdivisions N_1, N_2 and N_3 along recipr. l. vectors
0. 0. 0.    # optional shift of the mesh (s_1, s_2, s_3)"""
    file_Kpoint.write(KPOINTS_content)
    file_Kpoint.close()
    return

def print_Incar(ELEMENTS):
    file_Incar=open('INCAR', 'w')
    INCAR_COMMON='The alloy: '+str(ELEMENTS)
#    print INCAR_COMMON
    file_Incar.write(INCAR_COMMON)
    INCAR_content ="""NWRITE=0
ISTART=0
SIGMA=0.2
ISMEAR=1
ICHARG=2
ISIF=3
GGA=PE
ENCUT=300 eV
ALGO= F 
LREAL=Auto
NELM=500
NELMIN=5
LWAVE = .FALSE.
LCHARG = .FALSE.
LVTOT = .FALSE.
NSW=300
EDIFF=1.0E-05
EDIFFG=-0.05
IBRION=2
LMAXMIX=4
AMIX=0.2
AMIN=0.01
NSIM=4
POTIM=0.2
NPAR = 8 
PREC=Accurate """
    file_Incar.write(INCAR_content)
    file_Incar.close()
    return


def get_Potential(ELEMENTS):
    DFT_XC=raw_input (' The XC of POTCAR generate by: ')
    if DFT_XC == '':
        DFT_XC='PBE'
    x=raw_input (' The model of POTCAR for this ELEMENT (sv/pv/h...) : ')
    if x=='':
        ELEMENTS=ELEMENTS.strip('\r\n')
    else:
        ELEMENTS=ELEMENTS.strip('\r\n')+'_'+str(x)
    exec1='pmg generate -f '+str(DFT_XC)+' -p '+str(ELEMENTS)
#    print "%s" %exec1
    os.system(exec1)
    return

def get_Index(NUM):
    i=0
    test_Num=[]
    if (os.path.isfile('Replace_Position')):
        file_index=open('Replace_Position', 'r')
        x=file_index.readline()
        x=x.strip('\r\n')
    else: 
        Comment=" The Index of the Replace-Position" 
        print "%s" %Comment
        x=raw_input (' Index=')

        x=x.split()
    while i<int(NUM):
#       print '%s' %(x[i])
        test_Num.append(int(x[i]))
        i=i+1
 #      print i, NUM
    for k,v in dict(Counter(test_Num)).items():
        if v>1:
            sys.stderr.write("[ERROR]:!!! THE POSITION IS Conflcited: !!! \n")
            os._exit(-1)
#           sys.exit()
#           print test_Num
    return test_Num

def get_Element():
    if (os.path.isfile('Replace_Elements')):
        file_index=open('Replace_Elements', 'r')
        file_index=file_index.readline()
	x=file_index.strip('\r\n')
    else: 
        Comment=" The Name(s) of The Add_Element " 
        print "%s" %Comment
        x=raw_input (' Element (Such as Fe Cu Ag)=')
    x=x.split()
    num=len(x)
    return x, num

def get_Position_Info():
    Comment=" Give The Num. of Added_Element(s) AND Relapce_Num : \n"
    print "%s" %Comment
    x=raw_input (' Num_tot=Num1+Num2+Num3 ... \n')
    x=x.split()
    return x

#def __run_list():
#def __run_list():
#    list = ['create', 'check', 'relax', 'static',
#            'dos', 'results', 'clean', 'clear']
#    return list

def parse_argument():

#    RUN_LIST = __run_list()
    parser = argparse.ArgumentParser(
        description=" Script to do some POSCAR generation")
    parser.add_argument('-N', '--Position_Num', type=int, nargs=1,
                        default=[0],
                        help='The Position of the Replace Atoms, i_atom')
#    parser.add_argument('-I', '--Atom_Num', type=int, nargs= 1,
#                        default=[0],
#                        help='The Number of the Replace Atoms')
    parser.add_argument(
        '-v', '--version', action='version', version='%(prog)s ' + __version__())

    args = parser.parse_args()
    return(args)

#   MAIN
if __name__ == "__main__":

#    os.rename('POTCAR', 'POTCAR_orig')
#    os.rename('INCAR', 'INCAR_orig')
#    os.rename('KPOINTS', 'KPOINTS_orig')
    j=0
    args = parse_argument()
    NUM1 = args.Position_Num
#    NUM2 = args.Atom_Num

    if j>=int(NUM1[0]):
        sys.stderr.write("[ERROR]:!!! THE NUMBER OF ADDED_ALLOY IS NOT GIVEN: !!! \n") 
        os._exit(-1)

    ADD_ELEMENT, NUM2 = get_Element()
    while (j< int(NUM1[0])):
        DIR_ALLOY="ALLOY_"+str(int(j)+1)
        DIRTEST=os.path.isdir(DIR_ALLOY)
        if (not DIRTEST):
            os.mkdir(DIR_ALLOY)
        os.chdir(DIR_ALLOY)

        j=j+1
        NUM3=get_Position_Info() 
#        print NUM3

        i=0
        REPLACE_ATOM = get_Index(NUM3[0])
#        print "%d" %REPLACE_ATOM[0]

        if NUM2 > 0:
#           if ADD_ELEMENTS in ELEMENTS
#           print "%s" %ADD_ELEMENT

           while i< NUM2: 
               DIR_REPLACE="Alloy_"+str(ADD_ELEMENT[i])
               DIRTEST=os.path.isdir(DIR_REPLACE)
               if (not DIRTEST):
                   os.mkdir(DIR_REPLACE) 
               print DIR_REPLACE
               shutil.copy('../POSCAR',DIR_REPLACE)
#              shutil.copy ('KPOINTS', DIR_REPLACE)
#              shutil.copy ('INCAR', DIR_REPLACE)

               os.chdir(DIR_REPLACE)
#              execu1="sed -i 's/ISTART=1/ISTART=0/' INCAR"
#              os.system(execu1)

               ELEMENTS=replace_position(REPLACE_ATOM, NUM3, ADD_ELEMENT[i])
               print_Incar(ELEMENTS)
               print_Kpoint()
#       print "%s" %ELEMENTS
               if (j==1): 
                   get_Potential(ELEMENTS)
               else:
                   poten_exist="../../ALLOY_1/Alloy_"+str(ADD_ELEMENT[i])+"/POTCAR"
                   shutil.copy(poten_exist, ".")


               os.remove('POSCAR')
               os.rename('Temp','POSCAR')

               bjob_bash=get_exe_file()
               mpirun_command="bsub "+bjob_bash
##           print mpirun_command
#               os.system(mpirun_command)

               i=i+1

               os.chdir('../')
        else:
           get_poscar(REPLACE_ATOM, NUM3)
#           sys.stderr.write("[ERROR]:!!! THE ELEMENTS IS NOT Given: !!! \n")
#           os._exit(-1)
#           os.remove('POSCAR')
           os.rename('Temp','POSCAR_NEW')

        os.chdir('../')

print "All Done!"
