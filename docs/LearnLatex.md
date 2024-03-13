## 在学习Latex过程中遇到的问题及解决办法
### 如何新建文档
```
\documentclass[a4paper]{report}
\begin{document}
...
\end{document}
```
### 如何在每段中进行首行缩进
#### 加载indentfirst包
```
\usepackage{indentfirst}
```
### 如何进行伪代码书写
#### 加载两个包
```
\usepackage{algorithm}
\usepackage{algorithmic}
```
#### 基本结构
```
\begin{algorithm}
    \caption{算法名} 
    \begin{algorithmic}
        
        \ENDFOR

    \end{algorithmic} 
\end{algorithm}
```
#### 一些语法
??? 声明
    ```
    \STATE statement
    ```
??? FOR循环
    ```
    \FOR{condition}
    ...
    \ENDFOR
    ```
??? IF判断
    ```
    \IF{condition}
    ...
    \ELSIF{condition}
    ...
    \ELSE
    ...
    \ENDIF
    ```
#### 额外
??? 伪代码中自定义提示项
    ```
    \renewcommand{\algorithmicrequire}{\textbf{your text}}
    \REQUIRE your text
    ```
### 如何在表格中合并单元格
```
\usepackage{multirow}
```
??? 语法
### 如何进行代码渲染
\usepackage{minted}
\usepackage{dirtree}
\usepackage{graphicx}
```
!!! info
    建设中……