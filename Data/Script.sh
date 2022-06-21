#! /usr/bin/bash

var1=`echo $1 | awk -F "." '{print $1}' `
var2=`echo $1 | awk -F "." '{print $2}' `
var3="_orig."
var4="_mid."
var5="_mod."
file_back=$var1$var3$var2
file_mid=$var1$var4$var2
file_mod=$var1$var5$var2
echo $1 
echo $file_back

cp $1 ./$file_back


sed 's/\ 【二/\ 【{\\akai\ 二/g' $file_back | sed 's/板】/板}】/g' > $file_mid
sed 's/\ 【西/\ 【{\\akai\ 西/g' $file_mid | sed 's/眼】/眼}】/g' > $file_mod
sed 's/\ 【四平调】/\ 【{\\akai\ 四平调}】/g' $file_mod > $file_mid
sed 's/\ 【转/\ 【{\\small 转}{\\akai\ /g' $file_mid > $file_mod
