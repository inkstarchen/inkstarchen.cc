# 下推自动机与上下文无关文法笔记

## 1. 下推自动机 (PDA)

### 定义
一个下推自动机 (PDA) $P$ 是一个 6 元组：
$$ P = (K, \Sigma, \Gamma, \Delta, s, F) $$
（根据图片内容，通常简化为关注核心四元组 $(K, \Delta, S, F)$）

- $K$: 有限状态集
- $\Delta$: 转移关系
- $S$: 起始状态 ($s \in K$)
- $F$: 接受状态集 ($F \subseteq K$)

### 转移关系 $\Delta$
$\Delta$ 是一个有限子集，属于：
$$ (K \times (\Sigma \cup \{\epsilon\}) \times \Gamma^*) \times (K \times \Gamma^*) $$

其中：
- $(q, a, \beta) \to (q', \alpha)$ 表示：
  - 在当前状态 $q$
  - 读入输入符号 $a$ (可以是 $0$, $1$ 或 $\epsilon$)
  - 从栈顶弹出字符串 $\beta$
  - 进入新状态 $q'$
  - 将字符串 $\alpha$ 压入栈中

### 配置 (Configuration)
一个**配置**是三元组：
$$ (q, w, \gamma) \in K \times \Sigma^* \times \Gamma^* $$

- $q$: 当前状态
- $w$: 剩余输入字符串
- $\gamma$: 栈内容（通常栈顶在左边）

### 转移关系 ⊢
$(q, w, \gamma) \vdash_P (q', w', \gamma')$ 当且仅当存在转移：
$$ ((q, a, \beta), (q', \alpha)) \in \Delta $$
使得：
- $w = a \cdot w'$
- $\gamma = \beta \cdot \gamma''$
- $\gamma' = \alpha \cdot \gamma''$

$\vdash_P^*$ 表示零步或多步转移的闭包。

### 接受条件
PDA $P$ 接受字符串 $w \in \Sigma^*$ 当且仅当：
$$ (s, w, \epsilon) \vdash_P^* (q, \epsilon, \epsilon) \quad \text{对于某个} \quad q \in F $$

语言 $L(P)$ 是所有被 $P$ 接受的字符串集合：
$$ L(P) = \{ w \in \Sigma^* : P \text{ 接受 } w \} $$

$L(P)$ 是**上下文无关语言**。

---

## 示例 1: $L = \{w \in \{0,1\}^* : \#_0(w) = \#_1(w)\}$

- $K = \{q\}$
- $S = q$
- $F = \{q\}$
- $\Delta = \{ ((q, 0, \epsilon), (q, 0)),\ ((q, 1, 0), (q, \epsilon)) \}$

**转移规则：**
- $(q, 0, \epsilon), (q, 0)$: 读 0 压 0
- $(q, 1, 0), (q, \epsilon)$: 读 1 弹 0

---

## 2. 示例 2: $L = \{ww^R : w \in \{0,1\}^*\}$

- $K = \{l, r\}$
- $S = l$
- $F = \{r\}$
- $\Delta = \{ 
    ((l, 0, \epsilon), (l, 0)),\ 
    ((l, 1, \epsilon), (l, 1)),\ 
    ((l, \epsilon, \epsilon), (r, \epsilon)),\ 
    ((r, 0, 0), (r, \epsilon)),\ 
    ((r, 1, 1), (r, \epsilon))
  \}$

---

## 上下文无关文法 (CFG)

### 语言生成器
上下文无关文法通过产生式规则生成语言。

### 定义
一个上下文无关文法 $G$ 是四元组：
$$ G = (V, \Sigma, R, S) $$

- $V$: 有限符号集（包括终结符和非终结符）
- $\Sigma$: 终结符集（如 $\{0,1\}$）
- $S \in V \setminus \Sigma$: 开始符号
- $R \subseteq (V \setminus \Sigma) \times V^*$: 产生式规则集合

规则写作：$A \to u$，其中 $A \in V \setminus \Sigma$，$u \in V^*$

### 示例文法
产生式规则：
- $S \to 0S1$
- $S \to A$ 
- $A \to 0$
- $A \to \epsilon$

**推导示例：**
$$
S \Rightarrow 0S1 \Rightarrow 0A11 \Rightarrow 0011
$$

### 推导定义
对于 $x, y, u \in V^*$，$A \in V \setminus \Sigma$：
$$ xAy \Rightarrow xuy \quad \text{当且仅当} \quad (A \to u) \in R $$

这表示在一步推导中，将 $A$ 替换为 $u$。

# 下推自动机与上下文无关文法（续）

## 从 CFG 到 PDA 的转换

### 基本思路：
若有一个 CFG，可以构造一个 PDA 来接受同一语言。

**构造方法：**
1. 非确定性地在栈中生成一个字符串（使用文法 $A$）
2. 将其与输入进行比较
3. 如果匹配，则接受该输入

### 构造示例：
- $K = \\{q, p\\}$
- $F = \\{q\\}$
- $\\Delta$ 包含以下转移：
  - $((p, \\epsilon, \\epsilon), (q, S))$：初始化栈为开始符号
  - $((q, \\epsilon, A), (q, w))$，对每个 $(A \\to w) \\in R$：模拟推导过程
  - $((q, 0, 0), (q, \\epsilon))$：匹配输入符号 0
  - $((q, 1, 1), (q, \\epsilon))$：匹配输入符号 1

---

## 简单下推自动机

### 定义：
一个 PDA $P = (K, \\Delta, s, F)$ 是**简单的**，如果满足：
1. $|F| = 1$（只有一个接受状态）
2. 对每个转移 $((p, a, \\alpha), (q, \\beta)) \\in \\Delta$，满足以下情况之一：
   - $\\alpha = \\epsilon$ 且 $|\\beta| = 1$（不弹出，压入一个符号），或
   - $|\\alpha| = 1$ 且 $\\beta = \\epsilon$（弹出一个符号，不压入）

### 任意 PDA 到简单 PDA 的转换方法：

#### (1) 如果 $|F| > 1$：
- 创建一个新的接受状态 $f$
- 对每个 $q \\in F$，创建新转移 $((q, \\epsilon, \\epsilon), (f, \\epsilon))$
- 令 $F := \\{f\\}$

#### (2) 处理复杂转移：
考虑四种需要简化的情况：
- **2.1** $|\\alpha| \\geq 1$ 且 $|\\beta| \\geq 1$
- **2.2** $|\\alpha| > 1$ 且 $\\beta = \\epsilon$
- **2.3** $\\alpha = \\epsilon$ 且 $|\\beta| > 1$
- **2.4** $\\alpha = \\epsilon$ 且 $\\beta = \\epsilon$

##### 转换方法示例（2.1情况）：
将复杂转移：
$$((p, a, \\alpha), (q, \\beta))$$

拆分为两个简单转移：
1. $((p, a, \\alpha), (r, \\epsilon))$
2. $((r, \\epsilon, \\epsilon), (q, \\beta))$

其中 $r$ 是新引入的中间状态。

---

## 从简单 PDA 到 CFG 的转换

### 文法构造：
- $V = \\{0, 1\\} \\cup \\{A_{pq} : \\text{对于所有 } p, q \\in K \\times K\\}$
- 符号 $A_{pq}$ 表示：从状态 $p$ 带着空栈开始，经过一系列操作后到达状态 $q$ 且栈为空

### 关键性质：
$A_{pq} \\Rightarrow^* w$（对于某个 $w \\in \\{0,1\\}^*$）当且仅当 $w \\in \\{u \\in \\{0,1\\}^* : (p, u, \\epsilon) \\vdash_P^* (q, \\epsilon, \\epsilon)\\}$

这意味着非终结符 $A_{pq}$ 生成的所有字符串正好是从状态 $p$ 到状态 $q$ 且保持栈为空的输入字符串。

# 正则语言与泵引理

## 正则语言的代数方法

### 记号定义：
- $L_{ij}^k$：从状态 $i$ 到状态 $j$，仅经过状态 $\\{0,1,...,k\\}$ 的所有路径对应的语言
- $R_{ij}^k$：类似定义

### 递推关系：
$$L_{ij}^k = L_{ij}^{k-1} \cup L_{ik}^{k-1} (L_{kk}^{k-1})^* L_{kj}^{k-1}$$
$$R_{ij}^k = R_{ij}^{k-1} \cup R_{ik}^{k-1} (R_{kk}^{k-1})^* R_{kj}^{k-1}$$

### 最终语言：
$$L(M) = L_{0n}^{n-1}$$

其中 $M$ 是有 $n$ 个状态的 DFA，$0$ 是起始状态，$n$ 是接受状态。

---

## 泵引理 (Pumping Lemma)

### 定理陈述：
设 $L$ 是一个正则语言，则存在一个整数 $p \geq 1$（称为**泵长度**），使得对于任何 $w \in L$ 且 $|w| \geq p$，都可以将 $w$ 分成三部分 $w = xyz$，满足：

1. **可泵性**：对于所有 $i \geq 0$，$xy^iz \in L$
2. **非空性**：$|y| > 0$
3. **有界性**：$|xy| \leq p$

### 证明思路：
- 设 $M$ 是识别 $L$ 的 DFA，状态数为 $p$
- 对于 $w \in L$ 且 $|w| \geq p$，考虑 $M$ 接受 $w$ 时的状态序列
- 根据鸽巢原理，在读取前 $p$ 个字符时必然出现重复状态
- 设 $q_i = q_j$（$0 \leq i < j \leq p$），则：
  - $x$：从开始到第一次进入重复状态的字符串
  - $y$：在重复状态间循环的字符串
  - $z$：剩余的字符串

### 示例应用：

#### 例1：$L = ab^*a$
- $p = 2$
- $w = aa$ 可泵

#### 例2：$L = aba$
- $p = 3$
- $w = aba$ 可泵

---

## 泵引理的应用：证明非正则性

### 证明 $A = \\{0^n1^n : n \geq 0\\}$ 不是正则语言

**证明：**
1. 假设 $A$ 是正则的，设 $p$ 为其泵长度
2. 取 $w = 0^p1^p$，显然 $w \in A$ 且 $|w| = 2p \geq p$
3. 根据泵引理，$w$ 可写为 $w = xyz$，满足：
   - $|y| > 0$
   - $|xy| \leq p$
4. 由条件 (3) 可知 $y$ 完全由 $0$ 组成，设 $y = 0^k$（$k \geq 1$）
5. 考虑 $xy^0z = xz = 0^{p-k}1^p$
6. 由于 $k \geq 1$，$p-k \neq p$，所以 $0^{p-k}1^p \notin A$
7. 这与泵引理矛盾，故假设错误，$A$ 不是正则语言
