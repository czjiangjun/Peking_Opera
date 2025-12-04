#!/bin/bash
# 关于 texlive/xelatex 的中文输入
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%只要有相应的字体文档，不需要使用CJKutf8，直接由 xelatex 产生pdf文档	%
#%检索安装字体用命令 fc-list | grep'字体名' 即可知道可用字体		%
#%									%
#\usepackage{fontspec}							%
#\setmainfont[Mapping=tex-text]{LiSu}					%
#%\setmainfont[Mapping=tex-text]{Adobe 宋体 Std}	%article用字体	%
#%\setsansfont[Mapping=tex-text]{Adobe 黑体 Std}	 %Beamer用字体	%
#%									%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

MAIN = main
# Temp_DIr = Beamer_Template
RM = rm -f

FIGURES = Figures/
CUR_PWD = $(shell pwd)

find:
	@echo $(CUR_PWD)

# PATHFIG=`pwd`

evince:
	evince $(MAIN).pdf
main:
	xelatex -shell-escape $(MAIN)
	bibtex  $(MAIN) 
	xelatex -shell-escape $(MAIN)
	xelatex -shell-escape $(MAIN)

all: main evince clean

clean:   
	-@$(RM) Data/chap-*.aux Data/.*~ Data/.*.swp Data/*.*~ Data/chap-*.bbl Data/chap-*.blg~
	-@$(RM) *.aux *.bak *.bbl *.blg *.log *.nav *.out *.snm *.sta .*.swp *.toc *.*~ *~

cleanall: clean
	-@$(RM) $(MAIN).pdf
