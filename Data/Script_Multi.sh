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
  sed 's/^\ //g' $1  | sed 's/footnote{\ \ /footnote{/g '|  sed 's/texorpdfstring/hei\ /g'|  sed 's/subsection/subsubsection{\\large\\hei\ /g'| sed 's/\\textbf//g'| sed 's/：\ /：/g' |sed 's/\\protect\\hyberli//g'  |sed 's/\\protect\ \\hyberli//g' | sed 's/fnref//g'> $file_back

 awk -F " " '{if(NF>=1 && length($1)<6) {print ($1"\\" "'"$var6"'"); for (i=2; i<=NF; ++i) print $i} else if(NF>=1 && length($1)>5 && length($1)<=8) {print ($1"\\" "'"$var7"'"); for (i=2; i<=NF; ++i) print $i} else if(NF>=1 && length($1)>8 && length($1)<=10) {print ($1"\\" "'"$var8"'"); for (i=2; i<=NF; ++i) print $i} else if(NF>=1 && length($1)>11 && length($1)<=14) {print ($1"\\" "'"$var9"'"); for (i=2; i<=NF; ++i) print $i} else print ($0)}' $file_back |sed 's/：/:\~/g' | sed 's/^$/}\n\\setlength{\\hangindent}{56pt}{/g' > $file_mid

 sed  '/^\s*$/d' $file_mid | sed 's/引子/{\\akai 引子}/g'| sed 's/引/{\\akai 引}/g'| sed 's/(内/({\\akai 内}/g'| sed 's/(念)/({\\akai 念})/g'| sed 's/^(接唱)/({\\akai 接唱})/g'| sed 's/(接唱)/({\\akai 接唱})/g'| sed 's/(内白)/({\\akai 内白})/g'| sed 's/(内咳)/({\\akai 内嗽})/g'|sed 's/(或:\ /({\\akai 或}:\ /g'|sed 's/{二黄/二黄/g' | sed 's/{西皮/西皮/g' |sed 's/^【二/【{\\akai\ 二/g' | sed 's/\^【西/【{\\akai\ 西/g' | sed 's/^【反/【{\\akai\ 反/g' | sed 's/\ 【二/\ 【{\\akai\ 二/g' | sed 's/板\\protect/板}\\protect/g' | sed 's/板】/板}】/g' | sed 's/\ 【西/\ 【{\\akai\ 西/g' | sed 's/\ 【反/\ 【{\\akai\ 反/g' |sed 's/眼】/眼}】/g' | sed 's/【大/【{\\akai 大/g' | sed 's/【导/【{\\akai 导/g' | sed 's/【散/【{\\akai 散/g' | sed 's/黄】/黄}】/g' | sed 's/皮】/皮}】/g' | sed 's/二六】/二六}】/g' | sed 's/\ 【四平调】/\ 【{\\akai\ 四平调}】/g' | sed 's/\【回龙】/\【{\\akai\ 回龙}】/g'| sed 's/\^【回龙】/\ 【{\\akai\ 回龙}】/g'| sed 's/\ 【回龙】/\ 【{\\akai\ 回龙}】/g' | sed 's/【转/【{\\footnotesize 转}{\\akai\ /g' | sed 's/\ 【转/\ 【{\\footnotesize 转}{\\akai\ /g' | sed 's/)【二/)【{\\akai\ 二/g' | sed 's/)【西/)【{\\akai\ 西/g' | sed 's/^【二/【{\\akai\ 二/g' | sed 's/^【西/【{\\akai\ 西/g' | sed 's/{}【二/{}【{\\akai\ 二/g' | sed 's/{}【西/{}【{\\akai\ 西/g' | sed 's/【接/【{\\footnotesize\ 接}{\\akai\ /g' | sed 's/less{}{/less{}\\!{\\bfseries\\akai\ /g' | sed 's/}\\textgreater/}\\!\\textgreater/g' |sed 's/【二/【{\\akai\ 二/g' | sed 's/\【西/【{\\akai\ 西/g' | sed 's/【反/【{\\akai\ 反/g' | sed 's/}三叫头\\/}{\\!\\bfseries\\akai\ 三叫头}\\!\\/g'| sed 's/}仓仓仓仓仓才仓\\/}{\\!\\bfseries\\akai\ 仓仓仓仓仓才仓}\\!\\/g'| sed 's/}凤点头\\/}{\\!\\bfseries\\akai\ 凤点头}\\!\\/g'| sed 's/}撕边\\/}{\\!\\bfseries\\akai\ 撕边}\\!\\/g'| sed 's/}哆啰\\/}{\\!\\bfseries\\akai\ 哆啰}\\!\\/g'| sed 's/}扭丝\\/}{\\!\\bfseries\\akai\ 扭丝}\\!\\/g'| sed 's/}撕边一锣\\/}{\\!\\bfseries\\akai\ 撕边一锣}\\!\\/g'| sed 's/}顷仓\\/}{\\!\\bfseries\\akai\ 顷仓}\\!\\/g'| sed 's/}乱锤\\/}{\\!\\bfseries\\akai\ 乱锤}\\!\\/g'| sed 's/{唢呐}/{\\bfseries\\akai\ 唢呐}/g'| sed 's/}吹打{/}{\\bfseries\\akai\ 吹打}{/g'| sed 's/(铙钹\\/}{(\\bfseries\\akai\ 铙钹}/g'| sed 's/}帽子头\\/}{\\!\\bfseries\\akai\ 帽子头}\\!\\/g'| sed 's/}小锣抽头\\/}{\\!\\bfseries\\akai\ 小锣抽头}\\!\\/g'| sed 's/}铙钹夺头\\/}{\\!\\bfseries\\akai\ 铙钹夺头}\\!\\/g'| sed 's/}搓锤\\/}{\\!\\bfseries\\akai\ 搓锤}\\!\\/g'| sed 's/}撤锣\\/}{\\!\\bfseries\\akai\ 撤锣}\\!\\/g'| sed 's/}扫头\\/}{\\!\\bfseries\\akai\ 扫头}\\!\\/g'| sed 's/}叫头\\/}{\\!\\bfseries\\akai\ 叫头}\\!\\/g'| sed 's/}大锣扭丝\\/}\\!{\\bfseries\\akai\ 大锣扭丝}\\!\\/g'| sed 's/}大锣长锤\\/}\\!{\\bfseries\\akai\ 大锣长锤}\\!\\/g'| sed 's/}小锣归位\\/}\\!{\\bfseries\\akai\ 小锣归位}\\!\\/g'| sed 's/}小锣打上\\/}\\!{\\bfseries\\akai\ 小锣打上}\\!\\/g'| sed 's/}冲头\\/}\\!{\\bfseries\\akai\ 冲头}\\!\\/g'| sed 's/}快冲头\\/}\\!{\\bfseries\\akai\ 快冲头}\\!\\/g'| sed 's/}快扭丝\\/}\\!{\\bfseries\\akai\ 快扭丝}\\!\\/g'| sed 's/}台\\/}\\!{\\bfseries\\akai\ 台}\\!\\/g'| sed 's/}嘟仓\\/}\\!{\\bfseries\\akai\ 嘟仓}\\!\\/g'| sed 's/}大锣打下\\/}\\!{\\bfseries\\akai\ 大锣打下}\\!\\/g'| sed 's/}大锣抽头\\/}\\!{\\bfseries\\akai\ 大锣抽头}\\!\\/g'| sed 's/}点绛唇\\/}\\!{\\bfseries\\akai\ 点绛唇}\\!\\/g'| sed 's/}小锣五击头\\/}\\!{\\bfseries\\akai\ 小锣五击头}\\!\\/g'| sed 's/}小锣打上\\/}\\!{\\bfseries\\akai\ 小锣打上}\\!\\/g'| sed 's/}小锣叫头\\/}\\!{\\bfseries\\akai\ 小锣叫头}\\!\\/g'| sed 's/}小锣打下\\/}\\!{\\bfseries\\akai\ 小锣打下}\\!\\/g'| sed 's/}住头\\/}\\!{\\bfseries\\akai\ 住头}\\!\\/g'| sed 's/}抽头\\/}\\!{\\bfseries\\akai\ 抽头}\\!\\/g'| sed 's/}反带锣\\/}\\!{\\bfseries\\akai\ 反带锣}\\!\\/g'| sed 's/}夺头\\/}\\!{\\bfseries\\akai\ 夺头}\\!\\/g'| sed 's/}硬四击\\/}\\!{\\bfseries\\akai\ 硬四击}\\!\\/g'| sed 's/}小锣四反正\\/}\\!{\\bfseries\\akai\ 小锣四反正}\\!\\/g'| sed 's/}合龙\\/}\\!{\\bfseries\\akai\ 合龙}\\!\\/g'| sed 's/}合头\\/}\\!{\\bfseries\\akai\ 合头}\\!\\/g'| sed 's/}清江引\\/}\\!{\\bfseries\\akai\ 清江引}\\!\\/g'| sed 's/}仓\\/}\\!{\\bfseries\\akai\ 仓}\\!\\/g'| sed 's/}才\\/}\\!{\\bfseries\\akai\ 才}\\!\\/g'| sed 's/}哭头\\/}\\!{\\bfseries\\akai\ 哭头}\\!\\/g'| sed 's/【急急风】/\\textless{}\\!{\\bfseries\\akai\ 急急风}\\!\\textgreater{}/g'| sed 's/扫一句/\\!{\\bfseries\\akai\ 扫一句}\\!/g'| sed 's/风入松/{\\akai\ 风入松}/g'|sed 's/\\ldots{}\\ldots{}/$\\cdots{}\\cdots{}$/g' | sed 's/\\protect\\hyperli//g' | sed 's/\\protect\\hyperlink//g' | sed 's/\\protect\\hyperlin//g'| sed 's/^\\hyperlin//g'| sed 's/\\hypertarget{*.*}//g'| sed 's/\\hyperlin//g'| sed 's/}\\label{*.*}/}}/g'| sed 's/\\hypertarget{*.*}//g'|sed G | sed 's/protect\\foot/foot/g' | sed 's/{[0-9]}//g'| sed 's/{[0-9][0-9]}//g' | sed 's/{[0-9][0-9][0-9]}//g'| sed 's/集\ \ /集\~/g' | sed 's/藏本/\~藏本/g' | sed 's/{\[}第/\\vspace{3pt}{\\centerline{{\[}{\\hei\ 第/g' | sed 's/^{\[}第/\\vspace{3pt}{\\centerline{{\[}{\\hei\ 第/g' |sed 's/场{\]}/场}{\]}}}\\vspace{5pt}/g' |sed 's/场\\/场}}\\vspace{5pt}\\/g' |sed 's/(哭/({\\hwfs 哭}/g'|sed 's/(笑/({\\hwfs 笑}/g'|sed 's/介)/{\\hwfs 介})/g' |sed 's/n\\footnote/\\footnote/g' |sed '/^$/d' |sed 's/^}$/}\n/g'> $file_mod 

# var10=`echo | grep "subsubsection{\\\\large" $file_mod | awk -F "subsubsection{\\\\" '{print $2}' | awk -F "large" '{print $2}'`
# sed -i '2 i '\\\\addcontentlines{toc}"'"$10"'"' ' $file_mod 
# awk '{tempword="abc&"; gsub("&","\\\\&",tempword); print tempword }'
