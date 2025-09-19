> 为获取清晰的视角，我们需要将理论和实现分离

> 数据结构即，数据的组织形式，提供一定的操作以辅助算法的运行。因此选择适当的数据结构对于算法的实现有极大影响

[数据结构可视化网站](https://www.cs.usfca.edu/galles/visualization/Algorithms.html)

#### 常见的数据结构
- 数组
- 队列
- 哈希表
- 堆积（heap）

## 数组

- 顺序排列，用下标指示位置
- 插入和删除都需要进行大量平移交换，但查询速度快
- 散列表(hash table)

## 队列
- 只在一头做出队，一头做入队

## 哈希表
- 计算哈希函数来存储数据到某个特定位置
- 冲突处理
	- 开放空间：线性探测（+1），二次探测（再次哈希），伪随机数（加上一个随机数）
	- 链式存储：在同一个哈希值位置使用链表存储数据
## 堆积
### Leftist Heaps
- 目标：加速合并到$O(N)$
- 定义: The null path length, $Npl(X)$, of any node $X$ is the length of the shortest path from $X$ to a node without two children. Define $Npl(NULL) = -1$
- 定义: The leftist heap property is that for every node $X$ in the heap, the null path length of the left child is at least as large as that of the right child.
```c
struct TreeNode{
	ElementType Element;
	PriorityQueue Left;
	PriorityQueue Right;
	int Npl;
}

PriorityQueue Merge( PriorityQueue H1, PriorityQueue H2){
	if(H1 == NULL) return H2;
	if(H2 == NULL) return H1;
	if(H1->Element < H2->Element) reutrn Merge1(H1,H2);
	else return Merge1(H2, H1);
}

static PriorityQueue
Merge1(PriorityQueue H1, PriorityQueue H2){
	if(H1->Left == NULL)
		H1->Left = H2;
	else{
		H1->Right = Merge(H1->Right,H2);
		if(H1->Left->Npl < H1->Right->Npl)
			SwapChildren(H1);
		H1->Npl = H1->Right->Npl +1;
	}
	return H1;
}
	Tp = O(logN)
```

### Skew Heaps
- a simple version of the leftist heaps
- 目标: Any M consecutive operations take at most O(MlogN) time.
- Merge: Always swap the left and right children except that the largest of all the nodes on the right paths does not have its children swapped.

均摊分析：
$$T_{amortized} = O(logN),\quad D_i = 结果树的根，\phi(D_i)=heavy节点的数目$$
- heavy node：右子树的节点数超过祖先树的一半
$H_i: l_i + h_i$ 右子树:因为都是在右子树操作
Before merge:$\phi_0 = h_1 + h_2 + h$
After merge:$\phi_N \leq l_1 + l_2 + h$
这是由于左右交换以及插入的影响
$T_{amortized} = T_{worst} + \phi_N - \phi_0 \leq 2(l_1 + l_2)$
$l = O(log N)$

### Binomail Queues
- 定义: A binomial queue is not a heap-ordered tree, but rather a collection of heap-ordered trees, known as a forest.Each heap-ordered tree is binomial tree.
- 操作集
```
FindMin: The minimum key is in one of the roots.
		There are at most [logN] roots, hence Tp = O(logN).
Merge:Tp = O(logN)
Insert: Performing N Inserts on an initially empty binomial queue will take O(N) worst-case time. Hence the average time is constant.
DeleteMin: Step 1:FindMin in B_k
		Step 2: Remove B_k from H
		Step 3: Remove root from B_k
		Step 4: Merge(H',H")

```

- 实现
```c
typedef struct BinNode *Position;
typedef struct Collection *BinQueue;
typedef struct BinNode *BinTree;

struct BinNode{
ElementType Element;
Position LeftChild;
Position NextSibling;
};

struct Collection
{
int CurrentSize; /* total number of nodes */
BinTree The Trees[MaxTrees];
}

BinTree 
CombineTrees( BinTree T1, BinTree T2){
if(T1->Element > T2->Element)
	return CombineTrees(T2, T1);
T2->NextSibling = T1->LeftChild;
T1->LeftChild = T2;
return T1;
}

BinQueue Merge(BinQueue H1, BinQueue H2){
BinTree T1, T2, Carry = NULL;
int i, j;
if(H1->CurrentSize + H2->CurrentSize > Capacity) ErrorMessage();
H1->CurrentSize += H2->CurrentSize;
for(i=0, j=1; j <= H1->CurrentSize; i++, j*=2){
	T1 = H1->TheTrees[i]; T2 = H2->TheTrees[i];
	switch(4*!!Carry + 2*!!T2 + !!T1){
		case 0:
		case 1: break;
		case 2: H1->TheTrees[i] = T2; H2->TheTrees[i] = NULL; break;
		case 4: H1->TheTrees[i] = Carry; Carry = NULL; break;
		case 3: Carry = CombineTrees(T1, T2);H1->TheTrees[i] = H2->TheTrees[i] = NULL; break;
		case 5: Carry = CombineTrees(T1, Carry);H1->TheTrees[i] = NULL; break;
		case 6: Carry = CombineTrees(T2, Carry);H2->TheTrees[i] = NULL;break;
		case 7: H1->TheTrees[i] = Carry;
		Carry = CombineTrees(T1, T2);H2->TheTrees[i] = NULL; break;
	}
}
return H1;
}

ElementType DeleteMin(BinQueue H){
BinQueue DeletedQueue;
Position DeletedTree, OldRootl
ElemetType MinItem = Infinity;
int i, j, MinTree;
if(isEmpty(H)) {PrintErrorMessage(); return -Infinity;}
for(i = 0; i < MaxTrees; i++){
	if(H->TheTrees[i] && H->TheTrees[i]->Element < MinItem){
	MinItem = H->TheTrees[i]->Element; MinTree=i; }
}
DeletedTree = H->TheTrees[MinTree];
H->TheTrees[MinTree] = NULL;
OldRoot = DeletedTree;
DeletedTree = DeletedTree->LeftChild; free(OldRoot);
DeletedQueue = Initialize();
DeletedQueue->CurrentSize = (1<<MinTree)-1;
for(j = MinTree - 1; j >= 0; j--){
	DeletedQueue->TheTrees[j] = DeletedTree;
	DeletedTree = DeletedTree->NextSibling;
	DeletedQueue->TheTrees[j]->NextSibling =NULL;	
}
H->CurrentSize -= DeletedQueue->CurrentSize +1;
H = Merge(H, DeletedQueue);
reutrn MinItem.
}
```
#### 复杂度分析
$C_i = 第i次插入的花费； \phi_i=第i次插入后的树的个数. C_i + (\phi_i-\phi_{i-1})=2$
## 树
### [[树/AVL树|AVL树]]
- 目的：加速搜索
- 要求及定义：高度平衡
	- 左右子树都高度平衡
	- $|h_L - h_R| \leq 1$，其中$h_L$和$h_R$,分别为左右子树的高
- 基本操作：
	- 左右旋转
	- 插入、删除、查找
### Splay Trees
- 目标：从空树开始的连续M次操作，最多达到$O(MlogN)$的时间
- 想法：当一个节点杯访问后，就将其移动到根节点，
- 基本操作：
	- zig-zag、zig-zig
	- 查找、插入、删除、连接

复杂度均摊分析：待看

### Red-Black Trees
- 目的：得到平衡的二叉搜索树，牺牲了部分平衡性以换取插入和删除操作时少量的旋转操作
- 需要满足以下性质：
	- 所有节点要么是黑的要么是红的
	- 根节点是黑的
	- 所有叶子节点是黑的
	- 如果一个节点是红的，那么他的孩子都是黑的
	- 左右子树黑高相同
- 删除的基本思想：在左子树中找最大或在右子树中找最小，交换后，将交换点涂黑准备删除
[删除](https://zh.wikipedia.org/w/index.php?search=%E7%BA%A2%E9%BB%91%E6%A0%91&title=Special%3A%E6%90%9C%E7%B4%A2&wprov=acrw1_-1#:~:text=%E5%88%A0%E9%99%A4)

### B+ Tree
- 定义: A B+ tree of order M is a tree with the following structural properties:
- The root is either a leaf of has between 2 and M children.
- All nonleaf nodes (except the root) have between [M/2] and M children
- All leaves are at the same depth

删除：即逐层退化.
伪代码
```c
Btree Insert ( ElementType X, Btree T){
	Search from root to leaf for X and find the proper leaf node;
	Insert X;
	while( this node has M+1 keys) {
		split it into 2 nodes with [(M+1)/2]  and [(M+1)/2]keys, respectively;
		if(this node is the root)
			create a new root with two children;
		check its parent;
	}
}
T(M,N) = O((M/logM)logN)
```
## 倒排索引(Inverted File Index)
- 定义：index is a mechanism for locating a given term in a text
- 定义:Inerted file cotains a list of potiners to all occurences of that term in teh text.
![[images/Pasted_image_20241228211824.png]]
```c
Index Generator
while (read a document D) {
	while (read a term T in D) {
		if (Find( Dictionary, T ) == false )
			Insert( Dictionary, T );
		Get T's posting list;
		Insert a node to T's posting list;
	}
}
Write the inverted index to disk
```

Stop words: useless words like "a" "the" "it"
Word Stemming: Process a word so that only its stem or root form is left

#### 几个问题
- 存储索引表有两种方法：搜索树、哈希表
```c
without enough space
while ( read a document D ) {
	while ( read a term T in D) {
		if (out of memory ) {
			Write BlockIndex[BlockCnt] to disk;
			BlockCnt ++;
			FreeMemory;
		}
		if (Find( Dictionary, T ) == false)
			Insert( Dictionary , T);
		Get T's posting list;
		Insert a node to T's posting list;
	}
}
for ( i=0; i < BlockCnt; i++)
	Merge( InvertedIndex, BlockIndex[i]);
```

- 分布式索引的两种解决方法：Term-partitioned index\ Document-partitioned index.
- 动态更新索引：插入、更新、删除
- 空间利用：索引压缩：阈值（只返回权值高的文档）

相关性的评估

|               | Relevant | Irrelevant |
| ------------- | -------- | ---------- |
| Retrieved     | $R_R$    | $I_R$      |
| Not Retrieved | $R_N$    | $I_N$      |
$$Precision \quad P=P_R/(R_R+I_R) \qquad Recall\quad R=R_R/(R_R + R_N)$$



## 图

### 抽象数据类型定义
```
类型名称：图(Graph)
数据对象集:G(V,E)由一个非空的有限顶点集合V和一个有限边集合E组成。
操作集：对于任意图G\v\e
---
Graph Create():建立并返回空图
Graph InsertVertex(Graph G, Vertex v):将v插入G
Graph InsertEdge(Graph G, Edge e):将e插入G
void DFS(Graph G, Vertex v):从顶点v出发深度优先遍历图G；
void BFS(Graph G, Vertex v):从顶点v出发宽度优先遍历图G;
void ShortestPath(Graph G, Vertex v, int Dist[]):计算图G中顶点v到任意其他顶点的最短距离;
void MST(Graph G):计算图G的最小生成树
```
### 常见术语
- 网络
	- 无向图
	- 有向图
- 连通：
	- 如果从v到w存在一条（无向）路径 
- 路径：v到w的路径是一系列顶点{$V,v_1,v_2,\cdots,v_n,w$}的集合，其中任一对相邻的顶点间都有图中的边。**路径的长度**是路径中的边数（如果带权，则是所有边的权重和）。如果V到W之间的所有顶点都不同，则称**简单路径**
- 回路：
	- 起点等于终点的路径
- 连通图
	- 图中任意两顶点均连通 
- 连通分量：无向图的极大连通子图
	- 极大顶点数：再加1个顶点就不连通了
	- 极大边数：包含子图中所有顶点相连的所有边
- 强连通：有向图中顶点V和W之间存在双向路径，则称V和W是强连通的
- 强连通图：有向图中任意两顶点均强连通
- 强连通分量：有向图的极大强连通子图

## 链表
### 线性表（Linear List）
- 使用含有指针的结构将内存上不相邻的数据在组织结构上联系起来
- 根据指针的组织形式可以分为：单向链表、双向链表、循环链表

### 广义表（Generalized List）
- 广义表是**线性表的推广**
- 在广义表中，这些元素不仅可以是单元素也可以是**另一个广义表**

```
typedef struct GNode *GList;
struct GNode{
	int Tag;	/*标志域：0表示结点是单元素，1表示结点是广义表*/
	union {		/*子表指针域Sublist与单元素数据域Data复用,即共用
				存储空间*/
		ElementType	Data;
		GList SubList;
	} URegion;
	GList Next;
};
```

### 多重链表
- 链表中的节点可能同时隶属于多个链
- 多重链表中结点的**指针域会有多个**

**应用**：树和图这样相对复杂的数据结构都可以采用多重链表方式实现存储。

#### 十字链表
**示例**：存储稀疏矩阵

- 只存储矩阵非0元素项
	结点的数据域：行坐标Row、列坐标Col、数值Value
- 每个结点通过两个指针域，把同行、同列串起来；
	- 行指针（或称为向右指针）Right
	- 列指针（或称为向下指针）Down
- 用一个标识域Tag来区分头结点和非0元素结点：
- 头节点的标识值为“Head”，矩阵非0元素结点的标识值为“Term”
- 头节点则只有在数据域只有Next

## 队列

### 队列（Queue）
**定义**：具有一定操作约束的线性表
- 插入和删除操作：只能在一端插入，而在另一端删除。
- 数据插入：**入队列(AddQ)**
- 数据删除：**出队列(DeleteQ)**
- 先进先出：FIFO

#### 抽象数据类型描述
```
类型名称：队列(Queue)
数据对象集：一个有0或多个元素的有穷线性表
操作集：长度为MaxSze的队列Q

1.Queue CreateQueue( int MaxSize );生成长度为MaxSize的空队列
2.int IsFullQ( Queue Q, int MaxSize );判断队列Q是否已满
3.void AddQ( Queue , ElementType item);将数据元素item插入队列Q中
4.int Is EmptyQ(Queue Q);判断队列Q是否为空
5.ElementType Delete( Queu Q);将队头数据元素从队列中删除并返回
```

#### 队列的顺序存储实现
```
#define MaxSize <储存数据元素的最大个数>
struct QNode {
		ElementType Data[MaxSize];
		int rear;
		int front;
};
typedef struct QNode *Queue;
```
#### 队列的链式存储实现
```
struct Node{
	ElementType Data;
	struct Node *Next;
};
struct QNode{ /*链队列结构*/
	struct Node *rear;	/*指向队尾结点*/
	struct Node *front; /*指向队头结点*/
};
typedef struct QNode *Queue;
Queue PtrQ;
```

## 堆栈（Stack）

- 只在一端(栈顶，Top)做插入入栈(Push)、删除出栈(Pop)

#### 抽象数据类型描述
```
类型名称：堆栈（Stack）
数据对象集：一个有0个或多个元素的有穷线性表。
操作集：长度为MaxSize的堆栈S

1.Stack CreateStack( int MaxSize ); 生成空堆栈，其最大长度为MaxSize
2.int IsFull(Stack S,int MaxSize ); 判断堆栈S是否已满
3.void Push(Stack S,ElementType item);将元素item压入堆栈
4.int IsEmpty(Stack S);判断堆栈S是否为空
5.ElementType Pop(Stack S);删除并返回栈顶元素
```
#### 栈的顺序存储实现
```
#define MaxSize <存储数据元素的最大个数>
typedef struct SNode *Stack;
struct SNode{
		ElementType Data[MaxSize];
		int Top;
};
```

#### 堆栈的应用
**示例**：中缀表达式求值（将中缀表达式转换成后缀表达式）
- **运算数**：直接输出
- **左括号**：压入堆栈
- **右括号**：将栈顶的运算符弹出并输出，直到遇到左括号（出栈，不输出）
- **运算符**：
	- 若优先级大于栈顶运算符则把它压栈；
	- 若优先级小于等于栈顶运算符时，将栈顶运算符弹出并输出，再比较新的栈顶运算符，直到该运算符大于栈顶运算符优先级为止，然后将该运算符压栈；
- 若各对象处理完毕，则把堆栈中存留的运算符一并输出；
其他用途：函数调用及递归实现、深度优先搜索、回溯算法


## 堆积

### 优先队列（Priority Queue）
**定义**：特殊的“队列”，取出元素的顺序是依照元素的**优先权（关键字）** 大小，而不是元素进入队列的先后顺序。

#### 堆的两个特性
- 结构性：用数组表示的完全二叉树；
- 有序性：任一结点的关键字是其子树所有结点的最大值（或最小值）

#### 堆的抽象数据类型描述
```c
类型名称：最大堆（MaxHeap）

数据对象集：完全二叉树，每个结点的元素不小于其子结点的元素值

操作集：最大堆H
- MaxHeap Create( int MaxSize):创建一个空的最大堆。
- Boolean IsFull(MaxHeap H);判断最大堆H是否已满。
- Insert( MaxHeap H, ElementType item):将元素item插入最大堆H；
- Boolean IsEmpty( MaxHeap h):判断最大堆是否为空.
- ElementType DeleteMax(MaxHeap H):返回H中最大元素（高优先级）
```
#### 最大堆的操作
**创建**:
```c
typedef struct HeapStruct *MaxHeap;
struct HeapStruct}{
		ElementType *Elements; /*存储元素的数组*/
		int Size;				/*堆的当前元素个数*/
		int Capacity;			/*堆的最大容量*/
};

MaxHeap Create( int MaxSize){ /*创建容量为MaxSize的空的最大堆*/
	MaxHeap H = (MaxHeap)malloc(sizeof(struct HeapStruct));
	H->Elements = (*ElementType)malloc((MaxSize+1)*sizeof(ElementType));
	H->Size = 0;
	H->Capacity = MaxSiz;
	H->Elements[0] = MaxData;
	/*定义“哨兵”为大于堆中所有可能元素的值，便于以后更快操作*/
	return H;
	
}
```

**插入**：
```c
void Insert(MaxHeap H, ElementType item){
	int i;
	if (IsFull(H)){
		printf("最大堆已满");
		return;
	}
	i = ++H->Size;
	for( ; H->Elements[i/2] < item; i /=2) H->Elements[i] = H->Elements[i/2];
	H->Elements[i] = item; 
}
```

**删除**:
```c
ElementType DeleteMax(MaxHeap H){
	/*从最大堆H中取出键值为最大的元素，删除一个结点*/
	int Parent,Child;
	ElementType MaxItem, temp;
	if(IsEmpty(H)){
		printf("最大堆已为空");
		return;
	}
	MaxItem = H->Elements[1];/*取出根结点最大值*/
	/*用最大堆中最后一个元素从根结点开始向上过滤下层结点*/
	temp = H->Elements[H->Size--];
	for( Parent = 1; Parent*2<=H->Size;Parent = Child){
		Child = Parent * 2;
		if((Child!=H->Size) && 
			(H->Elements[Child] < H->Elements[Child+1]))
			Child++; /*Child指向左右子结点的较大者*/
		if( temp >= H->Elements[Child]) break;
		else /*移动temp元素到下一层*/
			H->Elements[Parent] = H->Elements[Child];
	}
	H->Elements[Parent] = temp;
	return MaxItem;
	
}
```


## 树

### 树(Tree)
**定义**：n个结点构成的有限集合

??? **基本术语**
	1. **结点的度（Degree）**：结点的子树个数
	2. **树的度**：树的所有结点中最大的度数
	3. **叶结点**：度为0的结点
	4. **父结点**：有子树的结点时其子树的根节点的父节点
	5. **子节点**：若A结点是B结点的父结点，则称B结点是A结点的子系结点
	6. **兄弟结点**：具有同一父结点的各结点彼此是兄弟结点
	7. **路径和路径长度**：路径所包含边的个数为路径长度
	8. **祖先结点**：沿树根到某一结点路径上的所有结点都是这个结点的祖先结点。
	9. **子孙结点**：某一结点的子树中的所有结点
	10. **结点的层次**
	11. **树的深度**：树中所有结点中最大层次

**表示方法**
- 儿子-兄弟表示法（减少空间浪费）

### 二叉树
- 斜二叉树Skewed Binary Trees
- 完美二叉树
#### 抽象数据类型定义
```
类型名称：二叉树
数据对象集：一个有穷的结点集合。
	若不为空，则由根结点和其左、右二叉子树组成

操作集：
	1.Boolean IsEmpty(BinTree BT): 判别BT是否为空；
	2。void Traversal(BinTree BT):遍历，按某顺序访问每个结点；
	3.BinTree CreatBinTree():创建一个二叉树
遍历法：
	- void PreOrderTraversal(BinTree BT):先序---根、左子树、右子树；
	- void InOrderTraversal(BinTree BT):中序---左子树、根、右子树；
	- void PostOrderTraversal(BinTree BT):后序---左子树、右子树、根;
	- void LevelOrderTraversal(BinTree BT):层次遍历,从上到下、从左到右；
```
#### 存储结构
1. **顺序存储结构**（数组形式）：父节点\[i/2\]，左孩子结点2i,右孩子结点2i+1;
2. **链表存储**：
	```
	typedef struct TreeNode *BinTree;
	typedef BinTree Position;
	struct TreeNode{
			ElementType Data;
			BinTree Left;
			BinTree Right;
	}
	```
#### 遍历
1. 前序遍历（preorder traversal）
2. 中序遍历（inorder traversal）
3. 后序遍历（postorder traversal）
- 中序遍历的非递归遍历算法（利用堆栈）
	```
	void InOrderTraversal(BinTree BT){
		BinTree T=BT;
		Stack S = CreatStack(MaxSize);
		while(T || !IsEmpty(S)){
			while(T){
				Push(S,T);
				T = T->left;
			}
			if(!IsEmpty(S)){
				T = Pop(S);
				printf("%5d", T->Data);
				T = T ->Right;
			}
		}	
	}
	```
- 核心问题：**二维结构的线性化**
- 层序遍历（队列实现）
	```
	void LevelOrderTraversal (BinTree BT){
		Queue Q; BinTree T;
		if(!BT) return;
		Q = CreatQueue(MaxSize);
		AddQ(Q,BT);
		while(!IsEmptyQ(Q)){
			T = DeleteQ(Q);\n
			printf("%d",T->Data);
			if(T->Left) AddQ(Q,T->Left);
			if(T->Right) AddQ(Q,T->Right);
		}
	}
	```
### 二叉树搜索
只有在平衡二叉树的情况，可以实现较好的搜索。
### 查找(Searching)
**定义**:根据某个给定关键字K，从集合R中找出关键字与K相同的记录
- **静态查找**：集合中记录是固定的
	- 没有插入和删除操作，只有查找
	- **示例**：顺序查找
- **动态查找**：集合中记录是动态变化的
	- 除查找，还可能发生插入和删除
- **二分查找**：
	- 有序且连续存放于数组.

### 哈夫曼树的定义
**带权路径长度（WPL）**：设二叉树有n个叶子结点，每个叶子结点带有权值$w_k$，从根结点到每个叶子结点的长度为$l_k$,则每个叶子结点的带权路径长度之和就是:$WPL=\sum_{k=1}^nw_kl_k$

**最优二叉树**或**哈夫曼树**：WPL最小的二叉树

#### 哈夫曼树的创建
```
typedef struct TreeNode *HuffmanTree;
struct TreeNode{
	int Weight;
	HuffmanTree Left, Right;
}
HuffmanTree Huffman(MinHeap H)
{
	int i; HuffmanTree T;
	BuildMinHeap(H);
	for(i = 1; i < H->Size; i++){
		T = malloc(sizeof(struct TreeNde));
		T->Left = DeleteMin(H);
		T->Right = DeleteMin(H);
		T->Weight = T->Left->Weight+T->Right->Weight;
		Insert(H,T);
	}
	T = DeleteMin(H);
	return T;
}
```

#### 哈夫曼树的特点
- 没有度为1的结点；
- n个叶子结点的哈夫曼树共有2n-1个结点
- 任意非叶节点的左右子树交换后仍是哈夫曼树；
- 存在同构;

- 避免二义性（使用前缀编码）
### 树的表示
- 二维数组表示(邻接矩阵)
- 链表表示（邻接表）
### 树的遍历
- 深度优先

```c
void DFS(Vertex V)
{
	visited[V] = true;
	for(V的每个邻接点W)
		if(!visited[W])
			DFS(W);
}
```

- 广度优先

```c
void BFS(Vertex V)
{
	visited[V] = true;
	Enqueue(V,Q);
	while(!IsEmpty(Q)){
		V = Dequeue(Q);
		for(V的每个邻接点W)
			if(!visited[W]){
				visited[W] = true;
				Enqueue(W,Q);
			}
	}
}
```

- 每调用一次DFS（V）,就把V所在的连通分量遍历了一遍.BFS也是一样

```c
void ListComponents(Graph G){
	for(each V in G)
		if(!visited[V]){
			DFS(V);
		}
}
```
### 最小生成树
- Prim算法

```c
void Prim()
{
	MST = {s};
	while(1){
		V = 未收录顶点中dist最小者;
		if(这样的V不存在)
			break;
		将V收录进MST :dist[V] = 0;
		for(V的每个邻接点W)
			if(W未被收录)
			 if(E_(V,W) < dist[W]){
			 	dist[W] = E_(V,W);
			 	parent[W] = V;
			 }
	}
}
```
- Kruskal算法

```c
void Kruskal(Graph G)
{
	MST ={};
	while(MST中不到|V|-1条边&&E中还有边){
		从E中取一条权重最小的边E_(V,W);
		将E_（V，W）从E中删除;
		if(E_(V,W)不在MST中构成回路)
			将E_（V，W）加入MST；
		else
			彻底无视E_（V，W）;
	}
	if(MST中不到|V|-1条边)
		Error("生成树不存在");
}
```

### AVL树
- 要求：任一节点对应的两棵子树的最大高度差为1
- 目的：为了避免高度过长，从而提高搜索效率
- 手段：自下而上递归，旋转

| 算法  | 平均      | 最差      |
| --- | ------- | ------- |
| 空间  | O(n)    | O(n)    |
| 搜索  | O(logn) | O(logn) |
| 插入  | O(logn) | O(logn) |
| 删除  | O(logn) | O(logn) |





## Amortized analysis
分类：

- 聚集法(Aggregate method)
- 记账法(Accounting method)
- 势能法(Potential method)
### Aggregate method

计算n个操作的时间复杂度上限$T(n)$,平摊$T(n)$至每一个操作，每一个操作的均摊成本就是$T(n)/n$

### Accounting method

在执行花费较低的operation时先存credot.供花费较高的operation使用.
对每一个操作定义一个合法的均摊成本(amortized cost)，假设$c_i$是第$i$个操作的实际成本，$\hat{c_i}$为第$i$个操作的均摊成本.其合法性需要以以下式子来确定：

$$\sum^n_{k=1}\hat{c_i} \geq \sum^n_{k=1}c_i$$

### Potential method

定义一个势能函数(potential function)$\phi(D)$,将数据结构的状态映射成一个实数.我们做一下定义:

$$D_0:数据结构D的初始状态,\qquad D_i:数据结构D经过i个操作后的状态$$

$$c_i:第i个操作的实际成本，\qquad \hat{c_i}:第i个操作的均摊成本$$

定义$\hat{c_i} = c_i + \phi(D_i) - \phi(D_{i-1})$ 

为了满足$\sum^n_{k=1}\hat{c_i} \geq \sum^n_{k=1}c_i$

我们定义$\phi(D_n)-\phi(D_0)\geq 0$,通常令$\phi(D_0)=0$和$\phi(D_n)\geq 0$
