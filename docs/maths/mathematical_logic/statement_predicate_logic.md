> **命题逻辑是数理逻辑的基础**


## 命题逻辑
- 命题逻辑（proposition logic）是应用一套形式化规则对以符号表示的描述性陈述（称为命题）进行推理的系统.

**原子命题**：指不包含其他命题作为其组成部分的命题

通过命题联结词（connectives）对已有命题进行组合，得到新命题，称为**复合命题（compound proposition）**

=== "命题的运算"
	命题的运算有以下几种
	
	- 命题合取 conjunction. $p \land q$
	- 命题析取 disjunction. $p \lor q$
	- 命题否定 negation. $\lnot p$
	- 命题蕴含 implication. $p \to q.\quad p为前件, \quad q为后件$
	- 命题双向蕴含 bi-implication. $p \leftrightarrow q$

=== "逻辑等价"
	在所有情况下都具有相同真假结果

    - 逆否命题：$(\alpha \to \beta) \equiv \lnot \beta \to \lnot \alpha$
	- 蕴含消除：$(\alpha \to \beta) \equiv \lnot \alpha \lor \beta$
	- 双向消除：$(\alpha \leftrightarrow \beta) \equiv (\alpha \to \beta) \land(\beta \to \alpha)$
	- ...

=== "推理规则"
	按照某种策略从前提出发推出结论的过程。常见推理规则：

	- 假言推理 Modus Ponens：$\frac{\alpha \Rightarrow \beta,\quad \alpha}{\beta}$
	- 与消解 And-Elimination：$\frac{\alpha_1 \land \alpha_2 \land \dots \land \alpha_n}{\alpha_i(q \leq i \leq n)}$
	- 与导入 And-Introduction：$\frac{\alpha_1,\alpha_2,\dots,\alpha_n}{\alpha_1 \land \alpha_2, \land \dots, \land \alpha_n}$
	- 双重否定 Double-Negation Elimination：$\frac{\lnot \lnot \alpha}{\alpha}$
	- 单项消解或单项归结 Unit Resolution：$\frac{\alpha \lor \beta, \lnot \beta}{\alpha}$
	- 消解或归结 Resolution：$\frac{\alpha \lor \beta, \lnot \beta \lor \gamma}{\alpha \lor \gamma}，\frac{\alpha_1 \lor \alpha_2 \lor \dots \lor \alpha_m, \lnot \beta}{\alpha_1 \lor \alpha_2 \lor \dots \lor \alpha_{k-1}\lor \alpha_{k+1}\lor \dots \lor \alpha_m}(\lnot \alpha_k = \lnot \beta)$

=== "范式（normal form）"
	是把命题公式化为一种标准的形式，作用是可以进行两个命题的等价判断
	
	- 析取范式 disjunctive normal form (DNF)：有限个简单合取式构成的析取式称为析取范式
	- 合取范式 conjunctive normal form (CNF)：有限个简单析取式构成的合取式称为合取范式
	- 命题公式的 DNF 和 CNF 都是不唯一的

## 谓词逻辑

> 命题逻辑无法表达局部与整体、一般与个别的关系，因此我们需要谓词逻辑来丰富我们的表达.

- 将原子命题进一步细化，分解出三个核心概念：个体、谓词和量词，来表达个体与总体的内在联系和数量关系，就是谓词逻辑（predicate logic）的研究内容

=== "个体"
	个体是指所研究领域中可以独立存在的具体或抽象的概念
	
	- 规定：用小写字母$a$至$w$表示个体常量（$x,y,z$表示个体变量）
	- 个体的取值范围称为个体域

=== "谓词"
	谓词是用来刻画个体属性或者描述个体之间的关系存在性的元素，其值为真或假
	
	- 包含一个参数的谓词称为一元谓词，表示一元关系
	- 包含多个参数的谓词称为多元谓词，表示个体间的多元关系
	- 规定：用$A(\cdots)至Z(\cdots)$表示谓词

=== "量词"
	全称量词和存在量词统称为量词
	
	- 全称量词：符号$\forall$
	- 存在量词：符号$\exists$
	- 全称量词的描述性是可以用相应的存在量词的藐视形式替换
	- 约束变量：在全称量词或存在量词约束条件下的变量符号
	- 自由变量：不受全称量词或存在量词约束的变量符号
	- 定理：自由变元既可以存在于量词的约束范围之内，也可以存在于量词约束范围之外，即：
		- $(\forall x)(A(x) \lor B) \equiv (\forall x)A(x) \lor B$
		- $(\forall x)(A(x) \land B) \equiv (\forall x)A(x)\land B$
		- $(\exists x)(A(x) \lor B) \equiv (\exists x)A(x) \lor B$
		- $(\exists x)(A(x) \land B)\equiv (\exists x)A(x) \land B$
	- 定理：在约束变元相同的条件下，量词的运算满足分配律
	- 定理：当公式中存在多个量词时，若多个量词都是全称量词或者都是存在量词，则量词位置可以互换；若多个量词中既有全称量词又有存在量词，则量词位置不可以随意互换

- **项**：项是描述对象的逻辑表达式，递归定义：
	- 常量符号和变量符号是项
	- 若$f(x_1,x_2,\cdots,x_n )$是n元函数符号，$t_1,t_2,\cdots,t_n$ 是项，则$f(t_1,t_2,\cdots,t_n)$是项
	- 有限次数地使用上述规则产生的符号串是项

- **原子谓词公式**： 若$P(x_1,x_2,\cdots,x_n)$是n元谓词，$t_1,t_2,\cdots,t_n$是项，则称$P(t_1,t_2,\cdots,t_n)$是原子谓词公式，简称原子公式

- **合式公式**：由逻辑联结词和原子公式构成地用于陈述事实地复杂语句，又称谓词公式：
	- 命题常项，命题变项，原子谓词公式都是合式公式
	- 通过逻辑联结词联结合式公式得到的也是合式公式
	- 如果$A$是合式公式，$x$是个体变项,则$(\exists x)A(x),(\forall x) A(x)$也是合式公式
	- 有限次数地使用上述规则

- 推理规则（$A(x)$是谓词公式，$x$和$y$是变元，$a$是常量符号）
	- 全称量词消去 universal instantiation (UI)：$(\forall x) A(x) \Rightarrow A(y)$
	- 全称量词引入 universal generalization (UG)：$A(y) \Rightarrow (\forall x)A(x)$
	- 存在量词小区 existential instantiation (EI)：$(\exists x)A(x) \Rightarrow A(a)$
	- 存在量词引入 existential generalization （EG)：$A(a) \Rightarrow (\exists x)A(x)$
