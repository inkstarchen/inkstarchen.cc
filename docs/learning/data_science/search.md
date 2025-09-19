## 二分查找
- 只针对有序数组有效
## 回溯法
- 基本思想: Suppose we have a partial solution $(x_1, \cdots, x_i)$ where each $x_k \in S_k$ for $1 \leq k \leq i < n$. First we add $x_{i+1} \in S_{i+1}$ and check if $(x_1, \cdots, x_i,x_{i+1})$ satisfies the constrains. If the answer is "yes" we continue to add the next $x$, else we delete $x_i$ and backtrack to the previous partial solution $(x_i, \cdots,x_{i-1})$

- 模板
```c
bool Backtracking(int i){
	Found = false;
	if(i > N)
		return true;
	for(each x_i in S_i){
		OK = Check((x_1,...,x_i), R);
		if(OK){
			Count x_i in;
			Found = Backtracking(i+1);
			if(!Found)
				Undo(i);	
		}
		if(Found) break;
	}
	return Found;
}
```

