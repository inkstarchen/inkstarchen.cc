# Git基础知识

## 如何创建远程仓库
??? info "解决方法"
	1.先在github上创建好一个仓库

	2.在本地选择好存放的文件夹

	3.创建README.md
	```
	echo "# <repository>" >> README.md
	```
	4.初始化git
	```
	git init
	```
	5.向git添加文件信息
	```
	git add README.md
	```
	6.填写提交信息并提交
	```
	git commit -m "first commit"
	```
	7.创建主分支
	```
	git branch -M main
	```
	8.连接远程仓库
	```
	git remote add origin https://github.com/<uesrname>/<repository>.gi
	```
	9.上传本地修改到远程仓库
	```
	git push -u origin main
	```

### 1.如何用mkdocs向GitHub推送网页
使用下列代码

`mkdocs gh-deploy`

### 2.如何忽略文件上传

设置仓库中的.gitignore文件
??? 示例
	如果你想忽略位于根目录下的`text.txt`文件，可以添加：
	```
	def int a 
	/text.txt
	```
	如果想要忽略根目录下的`test`目录中的`text.txt`文件，可以添加：
	```
	/test/text.txt
	or
	test/text.txt
	```
	
	同名同后缀文件忽略
	以`text.txt`为例，你可以添加：
	```
	text.txt
	```
	
	同目录下所有文件
	以`test`为例，你可以添加：
	```
	text/
	```
	
	所有同名文件及目录
	以`test`为例，你可以添加：
	```
	test
	```
	
	相同开头的文件及目录
	示例：
	```
	img*
	```
	
	所有扩展名文件
	示例：
	`*.md`
	排除文件(无法对忽略的目录下的文件做)
	```
	!README.md
	```

## Git 基本语法
??? tip "语法"
	??? note "初始化一个新的 Git 仓库"
		在项目根目录下执行以下命令以创建一个新的 Git 仓库：
		```
			git init
		```
		工作目录状态与变更
		查看状态

	??? tip "检查当前工作目录和暂存区状态" 
		使用以下命令来查看哪些文件已修改、新增、待提交或暂存：

		```
			git status
		```
		添加与暂存

	??? caution "将文件添加到暂存区" 
		要将单个文件添加到暂存区以准备提交，执行：

		```
		git add <文件名>
		```
		若要一次性添加所有修改和新文件到暂存区，可以使用：
		```
		git add .
		```
		取消暂存

	??? important "从暂存区移除文件" 
		如果需要取消对某个文件的暂存（撤销 git add），运行：

		```
			git restore --staged <文件名>
		```
		或者使用旧版语法：
		```
			git reset HEAD <文件名>
		```
		删除文件

	??? warning "删除工作目录中的文件并跟踪该删除操作"
		要从工作目录和暂存区中删除指定文件，并将其删除记录到下次提交，执行：

		```
			git rm <文件名>
		```
		提交变更
		正常提交

	??? success "提交暂存区的更改" 
		使用以下命令将暂存区的所有更改提交到本地仓库，并附带一条简短的提交说明：

		```
			git commit -m "<提交说明>"
		```
		修改最近提交
		??? info "修正最后一次提交" 如果需要修改最后一次提交的信息（如修改提交说明），执行：

		```
			git commit --amend
		```
		若要保留上次提交的说明，仅修改提交内容（例如，将未暂存的改动加入到最近一次提交），使用：
		```
			git commit --amend --no-edit
		```
		快速提交已跟踪文件

	??? abstract "直接提交所有已跟踪文件的现有变更" 
		对于已跟踪文件的现有变更（已修改和已删除的文件），可以省略 git add，直接提交：

		```
			git commit -a -m "<提交说明>"
		```
		分支管理
		查看、创建、切换分支

	??? example "查看、创建、切换分支" 
		查看本地分支:

		```
			git branch
		```
		**创建新分支**:
		```
			git branch <分支名>
		```
		**切换到指定分支**:
		```
			git checkout <分支名>
		```
		或使用新式语法：
		```
			git switch <分支名>
		```
		**创建并切换到新分支**:
		```
			git checkout -b <新分支名>
		```
		或新式语法：
		```
			git switch -c <新分支名>
		```

		合并与删除分支

	??? attention "合并与删除分支" 
		合并分支:

		```
			git merge <分支名>
		```
		**删除已合并到当前分支的本地分支**:
		```
			git branch -d <分支名>
		```
		**删除远程仓库上的分支**:
		```
			git push origin --delete <分支名>
		```
		历史与差异
		查看提交历史与详细信息

	??? details "查看提交历史与详细信息" 
		显示提交历史记录:

		```
			git log
		```
		**查看指定提交的详细信息**:
		```
			git show <commit_id>
		```
		比较差异

	??? quote  "比较文件、暂存区与提交之间的差异" 
		比较工作目录中当前文件与暂存区的差异:

!!! info
    建设中……

