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

if [ ! -f $file_back ]; then
       cp $1 ./$file_back
fi


var6="hspace{40pt}~"
var7="hspace{30pt}~"
var8="hspace{20pt}~"
var9="hspace{10pt}~"
awk -F " " '{if(NF>1 && length($1)<2) print ($1"\\" "'"$var6"'" , $2,$3); else if(NF>1 && length($1)>1 && length($1)<3) print ($1"\\" "'"$var7"'" , $2,$3); else if(NF>1 && length($1)>2 && length($1)<4) print ($1"\\" "'"$var8"'" , $2,$3); else if(NF>1 && length($1)>3 && length($1)<5) print ($1"\\" "'"$var9"'" , $2,$3); else print $0}'   $file_back | sed  '/^\s*$/d' | sed 's/\\textbf//g'| sed 's/\ 【二/\ 【{\\akai\ 二/g' | sed 's/板】/板}】/g' | sed 's/\ 【西/\ 【{\\akai\ 西/g' | sed 's/眼】/眼}】/g' | sed 's/\二六】/二六}】/g' | sed 's/\ 【四平调】/\ 【{\\akai\ 四平调}】/g' | sed 's/\ 【回龙】/\ 【{\\akai\ 回龙}】/g' | sed 's/\ 【转/\ 【{\\footnotesize 转}{\\akai\ /g' | sed 's/)【二/)【{\\akai\ 二/g' | sed 's/)【西/)【{\\akai\ 西/g' | sed 's/^【二/【{\\akai\ 二/g' | sed 's/^【西/【{\\akai\ 西/g' | sed 's/{}【二/{}【{\\akai\ 二/g' | sed 's/{}【西/{}【{\\akai\ 西/g' | sed 's/less{}{/less{}\\!{\\bfseries\\akai\ /g' | sed 's/}\\textgreater/}\!\\textgreater/g' | sed 's/^/\\setlength{\\hangindent}{60pt}{/g' | sed 's/$/}/g' |sed 's/\\ldots{}\\ldots{}/$\\cdots{}\\cdots{}$/g' | sed G > $file_mod
# awk '{tempword="abc&"; gsub("&","\\\\&",tempword); print tempword }'
