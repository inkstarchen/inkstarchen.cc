## 在学习Git过程中的问题及解决方案

### 1.如何用mkdocs向GitHub推送网页
使用下列代码

`mkdocs gh-deploy`

### 2.如何忽略文件上传

设置仓库中的.gitignore文件
??? 示例
	如果你想忽略位于根目录下的`text.txt`文件，可以添加：
	```
	/text.txt
	```
	如果想要忽略根目录下的`test`目录中的`text.txt`文件，可以添加：
	```
	/test/text.txt
	or
	test/text.txt
	```
	
??? 同名同后缀文件忽略
	以`text.txt`为例，你可以添加：
	```
	text.txt
	```
	
??? 同目录下所有文件
	以`test`为例，你可以添加：
	```
	text/
	```
	
??? 所有同名文件及目录
	以`test`为例，你可以添加：
	```
	test
	```
	
??? 相同开头的文件及目录
	示例：
	```
	img*
	```
	
??? 所有扩展名文件
	示例：
	`*.md`
	排除文件(无法对忽略的目录下的文件做)
	```
	!README.md
	```
!!! info
    建设中……