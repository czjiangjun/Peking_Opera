#! /bin/bash    
#/usr/bin/bash

var1=`echo $1 | awk -F "." '{print $1}' `
var2=`echo $1 | awk -F "." '{print $2}' `
var3="_orig."
var4="_mid."
var5="_mod."
file_back=$var1$var3$var2
file_mid=$var1$var4$var2
file_mod=$var1$var5$var2
# echo $1 
# echo $file_back

#if [ ! -f $file_back ]; then
#       cp $1 ./$file_back
#fi


var6="hspace{40pt}~"
var7="hspace{30pt}~"
var8="hspace{20pt}~"
var9="hspace{10pt}~"
 sed 's/^\ //g' $1  | sed 's/footnote{\ \ /footnote{\ /g ' | sed 's/\\textbf//g'| sed 's/：\ /：/g' > $file_back
 awk -F " " '{if(NF>1 && length($1)<6) print ($1"\\" "'"$var6"'" , $2,$3); else if(NF>1 && length($1)>5 && length($1)<=8) print ($1"\\" "'"$var7"'" , $2,$3); else if(NF>1 && length($1)>8 && length($1)<=10) print ($1"\\" "'"$var8"'" , $2,$3); else if(NF>1 && length($1)>11 && length($1)<=14) print ($1"\\" "'"$var9"'" , $2,$3); else print ($0)}'  $file_back |sed 's/：/:\ /g' > $file_mid
 sed  '/^\s*$/d' $file_mid | sed 's/引子/{\\akai 引子}/g'| sed 's/(内/({\\akai 内}/g'| sed 's/(念)/({\\akai 念})/g'| sed 's/(内白)/({\\akai 内白})/g'| sed 's/(内咳)/({\\akai 内嗽})/g'|sed 's/(或:\ /({\\akai 或}:\ /g'|sed 's/正是:\ /(\akai 正是}:\ /g'|sed 's/^【二/【{\\akai\ 二/g' | sed 's/\^【西/【{\\akai\ 西/g' | sed 's/^【反/【{\\akai\ 反/g' | sed 's/\ 【二/\ 【{\\akai\ 二/g' | sed 's/板】/板}】/g' | sed 's/\ 【西/\ 【{\\akai\ 西/g' | sed 's/\ 【反/\ 【{\\akai\ 反/g' |sed 's/眼】/眼}】/g' | sed 's/\二六】/二六}】/g' | sed 's/\ 【四平调】/\ 【{\\akai\ 四平调}】/g' | sed 's/\ 【回龙】/\ 【{\\akai\ 回龙}】/g' | sed 's/\ 【转/\ 【{\\footnotesize 转}{\\akai\ /g' | sed 's/)【二/)【{\\akai\ 二/g' | sed 's/)【西/)【{\\akai\ 西/g' | sed 's/^【二/【{\\akai\ 二/g' | sed 's/^【西/【{\\akai\ 西/g' | sed 's/{}【二/{}【{\\akai\ 二/g' | sed 's/{}【西/{}【{\\akai\ 西/g' | sed 's/【接/【{\\footnotesize\ 接{}\\akai\ /g' | sed 's/less{}{/less{}\\!{\\bfseries\\akai\ /g' | sed 's/}\\textgreater/}\\!\\textgreater/g' |sed 's/【二/【{\\akai\ 二/g' | sed 's/\【西/【{\\akai\ 西/g' | sed 's/【反/【{\\akai\ 反/g' | sed 's/风入松/{\\akai 风入松}/g'| sed 's/^/\\setlength{\\hangindent}{60pt}{/g' | sed 's/$/}/g' |sed 's/\\ldots{}\\ldots{}/$\\cdots{}\\cdots{}$/g' | sed 's/\\hyperlin//g'|sed G > $file_mod
# awk '{tempword="abc&"; gsub("&","\\\\&",tempword); print tempword }'