#! /bin/bash    
#/usr/bin/bash

git checkout $1
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
 mkdir ../Back_up
 cp $1 ../Back_up/$file_back

var9="hspace{10pt}~"
  sed 's/subsubsection/section*/g' $1  | sed 's/subsection/section/g' | sed 's/\\small{之/{\\small\ 之/g' > $file_mid
#  sed -i '2d' $file_mid
  sed  -i '/phantom/d' $file_mid
  sed -i '/newpage/a\\\phantomsection\ %实现目录的正确跳转'  $file_mid

  mv $file_mid $1 #&& rm -f $fille_back


 #| sed '\\hspace{[0-9][0-9]pt}\~$//g ' 
 # |sed '\\hspace{[0-9][0-9]pt}\~ //g '
 #|sed '/^$/d' |sed 's/^}$/}\n/g'> $file_mod 

# var10=`echo | grep "subsubsection{\\\\large" $file_mod | awk -F "subsubsection{\\\\" '{print $2}' | awk -F "large" '{print $2}'`
# sed -i '2 i '\\\\addcontentlines{toc}"'"$10"'"' ' $file_mod 
# awk '{tempword="abc&"; gsub("&","\\\\&",tempword); print tempword }'
