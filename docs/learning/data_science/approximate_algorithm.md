为了接近NP完全问题
最好的选择便是,找到一个接近最佳的多项式时间算法
- 定义: An lgorithm has an approximation ratio of $\rho(n)$if, for any input of size $n$, the cost $C$ of the solution produced by the algorithm is within a factor of $\rho(n)$ of the cost $C*$ of an optimal solution.
$$max(\frac{C}{C*}, \frac{C*}{C})\leq \rho(n)$$
If an algorithm achieves an approximation ratio of $\rho(n)$, we call it a $\rho(n)-$approximation algorithm

We say that approximation scheme is a polynomial-time approximation scheme(PTAS) if for any fixed $\varepsilon > 0$, the scheme runs in time polynomial in the size $n$ of its input instance.
$O(n^{2/\varepsilon}),\qquad O((1/\varepsilon)^2n^3)$-fully polynomial-time approximation scheme(FPTAS)

### Approximate Bin Packing
- Given $N$ items of sizes $S_1,S_2,\cdots, S_N,$such that $0<S_i \leq 1$ for all $1\leq i \leq N$. Pack these items in the fewest number of bins, each of which has unit capacity.

#### Next Fit
能装则装，最后一个装不下就新开一个
```c
void NextFit()
{ read item1;
 while(read item2){
	if(item2 can be packed in the same bin as item1)
		place item2 in the bin;
	else
		create a new bin for item2;
	item1 = item2;	
}
}
```

#### First Fit
找到第一个能装下的
- 定理：如果M为最佳数量，first fit 不会用超过17M/10个箱子
- 若物体降序排列则不超过(11M/9+6/9)个箱子
```c
void FirstFit(){
	while(read item){
		scan for the first bin that is large enough for item;
		if(found)
			place item in that bin;
		else
			create a new bin for item;
	}
}
```
#### Best Fit
- 装到一个装得最紧得箱子里.

动态规划：input size包括Pmax的二进制编码长度d，所以Pmax=O(2^d)是指数级的复杂度

## 局部搜索
Local
- Define neighborhoods in teh feasible set
- A local optimum is a best solution in a neighborhood

Search
- Start with a feasible solution and search a better one within the neighborhood
- A local optimum is achieved if no improvement is possible.

Neighbor Relation
- $S'$ is a neighboring soluion of $S-S'$ can be obtained by a small modification of $S$.

但是有局部最优的问题
```c
SolutionType Metropolis(){
	Define constants k and T;
	Start from a feasible solution S in FS;
	MinCost = cost(S);
	while(1){
		S'=Randomly chosen from N(S);
		CurrentCost = cost(S');
		if(CurrentCost < MinCost){
			MinCost = CurrentCost; S=S';
		}
		else {
			With a probability e-{Δcost/(kT)}, let S=S';
			else break;
		}
	}
	return S;
}
```

State-flipping Algorithm
```c
ConfigType State_flipping(){
	Start from an arbitrary configuration S;
	while(!IsStable(S)){
		u = GetUnsatisfied(S);
		S_u = - S_u;
	}
	return S;
}
```

- Claim: The state-flipping algorithm terminates at a stable configuration after at most W=$\sum_e|w_e|$iterations.
- Proof:
	$$\Phi(S) = \sum_{e\quad is \quad good} |w_e|,\quad \Phi(S')=\Phi(S)-\sum_{bad}|w_e|+\sum_{good}|w_e|$$

How good is this local optimum?

- Claim : Let$(A,B)$ be a local optimal partition and let $(A*,B*)$ be a global optimal partition. Then $w(A,B)\geq 1/2 w(A*,B*)$.
- Proof: Since$(A,B)$is a local optimal partition, for any $u \in A$$$\sum_{v\in A}w_{uv}\leq \sum_{v\in B}w_{uv}$$Summing up for all $u \in A$$$2\sum_{\{u,v\}\subseteq A}w_{uv} = \sum_{u\in A}\sum_{v \in A}w_{uv} \leq\sum_{u\in A}\sum_{v\in B}w_{uv} = w(A,B) $$$$2\sum_{\{u,v\}\subseteq B}w_{uv} \leq w(A,B)$$$$w(A*,B*)\leq \sum_{\{u,v\}\subseteq A}w_{uv} + \sum_{\{u,v\}\subseteq B}w_{uv} + w(A,B)\leq 2w(A,B)$$

当算法无法在多项式时间内结束时
stop the algorithm when there are no "big enough" improvements
- Big-improvement-flip: Only choose a node which, when flipped, increases the cut value by at least
	$$\frac{2\varepsilon}{|V|}w(A,B)$$
- Claim: Upon termination, the bit-improvement-flip algorithm returns a cut $(A,B)$ so that
$$(2+\varepsilon)w(A,B) \geq w(A*,B*)$$
- Claim: The big-**improvement**-flip algorithm terminates after at most $O(n/\varepsilon logW)$flips


## A Greedy Solution
- Put the first center at the best possible location for a single center, and then keep adding centers so as to reduce the covering radius each time by as much as possible.
- Fault:

- try again: if we know that $r(C*)\leq r$ where $C*$ is the optimal solution set.

```c
Centers Greedy-2r (Sites S[], int n, int K, double r){
	Sites S'[] = S[];
	Centers C[] = emptyset;
	while(S'[] != emptyset){
		Select any s from S' and add it to C;
		Delete all s' from S' that are at dist(s',s) <= 2r;
	}
	if(|C| <= K) return C;
	else ERROR(No set of K centers with covering radius at most r);
}
```

- A smarter solution-be far away
```c
Centers Greedy-Kcenter(Site S[],int n, int K){
	Centers C[]= emptyset;
	Select any s from S and add it to C;
	while(|C|<K){
		Select s from S with maximum dist(s,C);
		Add s it to C;
	}
	return C;
}
```

DOMINATING-SET -> Kcenters