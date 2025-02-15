

## 博弈论简介


> 博弈的第一步，选择你要进行博弈的主题或赛道（选对赛道比选对策略更重要），博弈的基础，判断参与者与你的利益一致性。

## 概述
### 何为博弈

博弈，是指在一定的 ==游戏规则== 约束下，基于 ==直接相互作用== 的环境条件，各参与人依据所掌握的 ==信息== ，选择各自的 ==策略== （行动），以实现 ==利益最大化== 的过程。

- 博弈既有对抗也有合作

世上有两种博弈：

- 一种博弈（有限游戏）以取胜为目的，
- 一种博弈（无限游戏）以共赢为目的。

**用心选合适的，而不是费心去改变不合适的！（人与人之间的关系：只筛选，不改变。改变自己筛选他人。）即成本前移**

>**胜兵先胜而求战，败兵先战而求胜**只有当我有十足的把握是或者超过六成的把握时，我才开始这场竞争。

### 发展简史
!!! info "商业博弈模型"

	=== "古诺模型"

		>参加博弈的双方以各自在同一时间内相互独立的产量作为决策的变量，是一个产量竞争模型。

	=== "伯川德模型"
		>该模型与古诺模型的不同之处在于，企业把其产品的价格而不是产量作为竞争的手段和决策的变量，通过制定一个最优的销售价格来是实现利润的最大化。

		伯川德悖论：寡头竞争，削价到边际成本。

		1、寡头市场的均衡价格为：P=MC（价格等于产品的边际成本）

		2、寡头企业的长期经济利润为0。

		**没有差别，按成本定价。**

		**没有差别，就没有利润。**
	=== "斯塔克尔伯格模型"

		**博弈的魅力就在于每个人在做决策的时候，必须考虑对手的反应（甚至反应的反应的反应），并把该反应（甚至反应的反应的反应）作为决策的依据之一。**
		>一个产量领导模型，厂商之间存在着行动次序的区别。领导厂商所决定的产量将是一个以跟随厂商的反应函数为约束的利润最大化产量。

### 理论的诞生与发展

1、二十世纪四十年代的社会变化。

2、约翰冯诺依曼的卓越贡献。1944年冯诺依曼和摩根斯坦发表《博弈论和经济行为》

3、约翰福布斯纳什的发扬光大

4、发展方向

- 对纳什均衡的弱化（一般化）

- 对纳什均衡的精炼（筛选）

- 对博弈论基本假设的研究

- 对博弈论应用的研究

## 术语解读和基本假设
### 术语解读
#### 博弈的术语
- 参与人（players）：理性选择的主体。

- 信息（information）：参与者有关博弈的知识。

- 行动（action）：参与者能够选择的变量

- 策略（srtategies）：参与者在行动之前所准备好的一套完整的行动方案
（预案）。
	1. 完整性
	2. 多样性
	3. 不可观察性

- 损益（payoff）：参与者的得与失。
- 结局（outcome）：所有参与者选择各自的策略后的结果。
- 均衡（equilibrium）：所有参与者的最优策略组合。
- 弈的规则（rules of the game）：参与者、行动和结果合起来统称为博弈的规则。
#### 均衡的含义
>如果参与人事前达成一个协议，在不存在外部强制的情况下，每个人都有积极性遵守这个协议，这个协议就是纳什均衡。

**改革需要理由，不改革不需要理由**
#### 博弈的分类
<div class="grid" markdown>
!!! note "合作博弈和非合作博弈"

	=== "**合作博弈**"
		指参与者能够达成一种具有约束力的协议，在协议范围内选择有利于双方的策略。

	=== "**非合作博弈**" 
		指参与者无法达成这样一种协议。

!!! note "静态博弈和动态博弈"

	=== "**静态博弈**"
		指在博弈中，参与者同时选择，或虽非同时选择，但是在逻辑时间上是同时的。

	=== "**动态博弈**"
		指在博弈中，参与者的行动有先后顺序，且后行动者能够观察到先行动者的行动。

!!! note "完全信息博弈与不完全信息博弈"
	=== "**完全信息博弈**"
		指在博弈中，每个参与者对其他参与者的类型、策略空间及损益函数都有准确的信息。

	=== "**不完全信息博弈**"
		总有一些信息不是所有参与者都知道的。
	
!!! note "零和博弈与非零和博弈"

	=== "**零和博弈**"
		指博弈前的损益总和与博弈后的损益总和相等。

	=== "**非零和博弈**" 
		指博弈后的损益大于（小于）博弈前的损益总和。（正和或负和）

	=== "**建议**"
		**不玩负和游戏，少玩零和游戏，多玩正和游戏**
</div>
### 基本假设
#### 理性假设
> **在互动关系中，完全理性的选择未必是最好的选择** 
<div class="grid" markdown>
!!! note
	=== "认知理性"

		* 人是自我利益的判断者
		* 偏好具有完备性 （completeness）和传递性 （transitivity）

	=== "行为理性"
		* 自我利益的追求者（行为者）
		* 利益最大化 （两利相权取其重，两害相权取其轻）


	=== "情境理性"
		**理性不能独立于场景而存在**

		**理性必然依场景的改变而改变**

		> 情境理性给出了学校存在的一个重要理由

	=== "共同知识假设"

		**共同知识**：指各参与者在无穷递归意义上均知悉的事实。

		**信息传递不能确保信息的完全接收**

		**达成共识是一件非常困难的事情**

!!! tip "特别提醒"
	* **顾客需要的不是便宜，而是占到了便宜。**
	* **教育与洗脑的根本区别，在于是否屏蔽异见。**
	* **如果不给对方您的两利让其相权，那么对方就很可能会把您的一利和他人的一利相权，从而离您而去。（多做选择题，少做判断题）**
</div>






### 蜈蚣博弈

> 蜈蚣博弈（Centipede game）是一个双人博弈，两人轮流行动，轮到一方时有两种选择：不合作，博弈将直接结束，直接获得收益P；合作，博弈将继续进行，且轮到对方选择。如果对手选择不合作将结束博弈，玩家将会获得一个稍微低于P的收益，但如果对手也选择继续博弈，该玩家将在之后的博弈中获得一个高于P的收益。随着博弈的不断进行，两玩家的收益之和将越来越高。博弈进行有限轮，若两玩家一直选择合作，两人最后的收益相同。

玩到最后的前提是：

* 更看重对方的利益
* 大家都愿意吃眼前亏



### 策略
**策略让我们建立起从信息到行动的快速反应机制，从而能够以最快的速度做出行动选择。**
**中国的立法精神：公民有退让义务**

**出门在外，不清楚对方的行为模式或反应函数之前**

* 尽量避免与他人发生正面冲突是你的占优策略。
* 如果冲突发生了，尽量避免暴力升级是你的占优策略。
* 当面临人身或财产的严重危险时，尽快寻求警方帮助是你的占优策略。

## 最后通牒与讨价还价
### 最后通牒
#### 最后通牒的含义
>一人提出方案，另一人表决。若表决不痛过，则一无所得。

- **人在博弈中，会追求利益以外的价值（不患寡，患不均）**
- **越是成熟的组织，越是使用最后通牒的博弈**
- **决定您出价高低的是：贪婪和恐惧**

>职务提升制度直接影响组织的管理效率。尽可能建立基于绩效和能力的职务提升制度，并坚持公开竞争性原则。

**谁来承担决策的后果就谁来做决策**

#### 独裁者博弈
>第一，人们在决定其行动时，并不会仅仅考虑到其经济利益，虽然这可能时最主要的一个考量，他们也会考虑一些道德和社会规范，比如公平原则，“己所不欲，勿施于人。”

>第二，一个社会如果在制度安排上能够给人民更多可以拒绝（可以说“不”）的权利，那么这个社会就会产生更多的公平性，甚至会带来更多的效率改善。


>第三，一个社会在制度安排上给了机构（官员）更多可以拒绝（可以说“不”）的权力（比如行政审批制度），那么拥有审批权的机构（官员）一定能够从中获利丰厚。（如社会抚养费）

### 讨价还价

#### 讨价还价的含义
也称为**议价**或**谈判**，主要时指参与者通过协商方式解决利益的分配问题，称讨价还价时主要强调其动作或过程，称谈判时则强调其状态或结果。
#### 均衡解

均衡解：X*=(1-δ)/(1-δδ)

**先动优势**

δ代表对长期利益的看重程度

**谈判过程中总能找到一个均衡解**

**知识的互补性**

关键在于沟通交流，要建立沟通理性和交流理性

#### 贴现因子
**是指一个份额经过一段时间后，等同的现在份额，其由参与者的耐心所决定**

寿命、财富、未来收益的确定性、知识水平

组织有比人更长的寿命预期，从而提高了贴现因子

**磨刀不误砍柴工（误与不误取决于你要砍多少的柴）**


## 囚徒困境和破解之道
### 囚徒困境及原因
#### 囚徒困境的来源
> **游戏规则决定游戏的结局**

\ | 坦白 | 抗拒
--| ------| ---
坦白 |-3，-3|0，-5
抗拒|-5，0| -0.5，-0.5



#### 囚徒困境的定义及原因分析
\   |  坦白  | 抗拒
----| ------| -------
坦白 |a1，b1 | a2，b2
抗拒 |a3，b3 | a4，b4

>1、双方都有占优策略，即：
>a1>a3，a2>a4，b1>b2，b3>b4
>在a1>a3，a2>a4的条件下，A选择坦白是占优策略；在b1>b2，b3>b4的条件下，B选择坦白是占优策略。

>2、存在一个合作解，使双方的收益都优于其在占优策略均衡下的收益，即：a1<a4，b1<b4如果双方能够选择合作（都抗拒），本可以得到更好的结果。

**对称条件下的囚徒困境**

\   |  坦白  | 抗拒
----| ------| -------
坦白 |P，P   | T，S
抗拒 |S，T   | R，R

>在一个2人双策略 对称博弈中，如果满足以下条件：T>R>P>S，2R>S+T>2P，那么其占有策略均衡（P，P）就构成了囚徒困境。（个人理性与集体非理想）

#### 原因分析
> 表面上看囚犯对自身利益的追求是导致囚犯困境的原因。然而，真正的原因是：囚犯们在追求自身利益的同时，是以更多地损害他人利益为代价。（君子爱财，取之有道）

**囚犯困境的根本原因在于：私人成本与社会成本的差异，即个人行为的负外部性。**

**条件**：T（temptation）R（revolt）>P（punishment）>S（sucker）每个参与者抵挡不了诱惑T，背叛R了对方，让对方成为受骗者S。在（R-S）>（T-R）（等同于2R>T+S）的情况下，每个人都收到了惩罚P。

**损人利己和损己利人本质上是一样的，是一个硬币的正反两面；从一方来看是损己利人行为，在另一方来看是损人利己的行为，问题的关键是所损失的部分和所利得的部分哪个更多。（盗窃与抢劫）**

**让自己获利时尽量减少伤害他人！**

**道德自律：不做害人大于利己的事！**

### 真实世界的囚犯困境
- 价格战、独裁与多数人的懦弱、民主与多数人的暴政。

- **民主必须与法治（不是法制）相辅相成，才能避免多数人的暴政**

### 《国家理论》作者：约拉姆巴泽尔

1. 人类成员散局于不同的生存环境内，具有相似的智力，故而积累了不同的技能与知识。
2. 当具有不同生活技能与生产知识的人类成员偶然相遇时，他们发现了各自的“比较优势”以比他人更低的可比成本提供某种财货的能力（技能与知识）
3. 于是不同的人类成员之间存在着“交易”的潜在可能性。（“交易”（transactions）不同于“贸易”（trages）。后者可以视为“临时性的交易”，前者则指称更长期和多次的互惠交换）

4. 交易的执行方式可以划分为I三类：
	1. 基于道德自律的
	2. 基于交易各方相互制约的
	3. 基于与交易无关的“第三方”监督的

5. 威慑而不当真使用暴力，使得“第三方”的威慑具有一种“规模效益”。
1把枪，哪怕只有1颗子弹，也足够让100次交易通过第三方得以执行。（囚犯困境二）

6. 当交易的执行成本（道德或相互制约）低于交易所实现的“比较优势”时，交易各方就会自愿订立交易合约。当购买“第三方执行”服务的成本低于采取“相互制约”方式的成本时，交易各方就会自愿订立购买“第三方执行”服务的合约。


7. 国家一旦确立，就很难被瓦解。如霍布斯所描述的，交易各方自愿购买的“第三方执行”服务，最终将成为他们不得不“购买”的“利维坦”（Leviathan）怪兽（囚犯困境四，与囚犯困境二类似）。
由于国家的规模收益递增性质，人类社会的“财富创造”过程很可能因为“第三方执行”服务提供者的横征暴敛而被“锁入”一个“财富毁灭的过程内”。

9. 如果能找到某种集体行动机制，人类社会就能从传统的“自然国家”过渡到现代的“法治国家”。如果找不到这样一种集体行动机制，人类社会要么停留在自然国家状态，要么长期处于“利维坦”的独裁通知。这就是“独裁政权”与“臣民控制的政权”之间的差异，也是代表强权利益的“法制国”（Rule by law）与代表大众利益的“法治国”（Rule of law）之间的差异。

#### 特别提醒
**政府既要有能力制止老百姓乱来，又要确保自己不能乱来（让老百姓有能力制止政府的乱来）。**

>“人类千万年的历史，最珍贵的不是令人炫目的科技，不是浩瀚的大师们的经典著作，不是政客天花乱坠的演讲，而是实现了对统治者的驯服，实现了把他们关在笼子里的梦想。因为只有驯服了他们，把他们关起来，才不会害人。我现在就是站在笼子里向你们讲话。”--布什
### 如何破解囚徒困境
#### 一、如何利用(两个例子)
1、上帝与魔鬼
2、如何购车

#### 二、如何破解
=== "**道德教化（文化建设）**"

	社会学基本定理：

	> “如果一个社会都是由自利主义者构成的，那么，长期而言，这个社会将消亡。而如果一个社会，通过“说服教育”以及其他说教机构的努力，长期保持一定比例的利他主义者，它就能够稳定地繁衍下去” ————金迪斯

=== "**2、制度建设**"

	- 圈地运动（减少负外部性）
	- 人民公社（自由退社权）

=== "**3、温故知新**"

	- 让历史告诉未来（重复博弈）
	- 学习《博弈论基础》课程

## 万元陷阱和智猪博弈
### 万元陷阱
=== "**陷阱特征**"
	>1. 有一个明显的诱饵
	>2. 通往诱饵之路是单向的，可进不可出
	>3. 越想挣脱、就越陷越深

	**存量绑架、目标偏移**

=== "典型的万元陷阱"
	- 序列竞争（排名赛）
	- 竞技体育

=== "动机"
	1. 是经济（理性）的
	>渴望赢得钞票、赢回他的损失、想避免更多的损失

	2. 是非经济（感性）的
	>渴望挽回面子、证明自己是最好的玩家及处罚对手等。（鼓掌）

#### 应对万元陷阱的建议（鲁宾）
1. 确立你投入的极限及预先的约定：譬如投资多少钱或多少时间？
2. 极限一经确立，就要坚持到底。（止损）
3. 自己打定主意，不必看别人

> **既然事情已经发生，请坦然接受！**

> **更正错误的最好时机，是当你知道了错误的时候**

> **每个人呢都有犯错的时候，请把注意力放在以后如何避免犯同样的错误！**

***
### 智猪博弈
> **智猪博弈是一个搭便车的博弈一方付出了相应的代价，双方共享了所得到的收益。**
=== "原模型"
	\   |  按 |  等
	--- |----| ----
	按  |5，1 | 4，4
	等  | 9，-1|0，0



=== "扩展模型"
	\    | 按  |等
	--   |---- |--
	按   | 7-A，3-A|6-A，4
	等   |9 ， 1-A|0，0

=== "若干启发"
	- 个人理性与集体理性相冲突，还是相一致，取决于制度安排（游戏规则）。

	- 解决个体理性与集体理性之间的冲突不是靠否定个体理性，而是靠修改制度（游戏规则），从而在满足个体理性的基础上实现集体理性。
	- 从智猪博弈中还可以发现，在A<10时，任一方去按都是集体理性的选择，而收入分配的不均将有助于减少个体理性与集体理性的冲突。

=== "实例分析"
	1. 山寨现象（盗版）
	2. 网络购物
	3. 抄（复印）笔记
	4. 汽车定位系统
	5. 好货不便宜，便宜没好货

***

## 懦夫博弈和夫妻博弈
### 懦夫博弈
\  | 进    |退
---|-------|---
进  |-5，-5 |10，0
退  |0，10  | 0，0

> **先下手为强，后下手遭殃**

>**赢者通吃的行业，容易出现过度竞争**

#### 竞争博弈的核心问题

1. 比什么？（规则）
2. 和谁比？（对手）
3. 怎么比？（策略）

**游戏规则决定了你的能力发展方向。**

>如果你有极大的力量，制定游戏规则；

>如果你有较大的力量，挑选游戏规则；

>如果你缺乏足够的力量，适应游戏规则！

**公共物品的供给**

1. 囚犯困境
2. 智猪博弈
3. 懦夫博弈

### 夫妻博弈

\ |球赛|韩剧
--|-----|--
球赛|2，1|0，0
韩剧|-1，-1|1，2

### 猎鹿博弈

\ |猎鹿|猎兔
--|----|---
猎鹿|4，4|0，2
猎兔|2，0|2，2

> **合作需要沟通与协调，沟通与协调的成本过高，合作很难成功。**

> **人类社会制度和技术的演进方向：不断减低人与人之间的沟通（协调）成本。**

#### 合作博弈的核心问题

1. 合作剩余（新增收益）怎么分配？
2. 合作风险怎么分担？

#### 基本分配方式：

第一种，A拿剩余、B拿固定，如雇主和雇员之间。

第二种，A拿固定，B拿剩余，如银行和企业之间。

第三种，AB约定一个分配比例，如分成制，股份制，以及婚姻关系中平分婚后收入的制度安排。（农民和地主）

> **资本雇佣劳动还是劳动雇佣资本，只是一个合作效率的比较问题。**

**农业经济**：劳动雇佣土地
**工业经济**：资本雇佣劳动
**知识经济**：合伙人时代

1. 劳动监督成本
2. 规模经济效应
3. 资本抵押功能
4. 企业家才能定价

#### 如何在合作博弈中实现利益最大化
贡献越大、机会越多、沟通越易、做事越稳、收益越大。

**竞争博弈：出其不意、攻其不备（难预期）**
**合作博弈：言而有信、行而可期（可预期）**
**一般情况下，请不要相信阴谋论**
>竞争博弈中阴谋的成本在上升，作用在下降
>合作博弈中阴谋不但没好处，而且往往有害

**在博弈中，如果您希望得到对方的信任，关键是让其相信，双方的利益是一致的！**
**执政党（政府）的利益和老百姓的利益相一致，是一个国家政权稳定、长治久安最根本的保障和最坚实的基础。

**共同的价值观（目标）是合作的基石**
**要事优先**
>管理者只做最重要的事情，不做第二重要的事情。

**我们为了一些不重要的事情疲于奔命，
却忘了在真正重要的事情上多下功夫。**

#### 判断一件事的重要性
1、需要做吗？
2、需要你来做吗？
3、你该怎么做？

**每个人可以有和别人不一样的价值观,每个组织需要一个相对统一的价值观。**

**充分沟通必能达成共同认知**

**要想达成共同认知，需要每个人都能畅所欲言。**
