- `Optional[X]`等价于`Union[X,None]` : 可以是类型X,也可以是None

> 用于区分 **单量子比特门** 与 **多量子比特门（控制门）**

```python linenums="1"
from typing import List, Tuple, Optional

self.circuit: List[Tuple[str, int, Optional[int]]] = []

# 可能的电路操作记录：
self.circuit = [
    ("H", 0, None),      # 在量子比特0上应用Hadamard门，没有控制比特
    ("X", 1, 0),         # 在量子比特1上应用X门，受量子比特0控制（CNOT门）
    ("Y", 2, None),      # 在量子比特2上应用Y门，没有控制比特
    ("Z", 0, 1),         # 在量子比特0上应用Z门，受量子比特1控制（CZ门）
]
```

```python title="带有返回值提示的函数定义" linenums="1"
def measure(self, shots: int = 1, basis: Optional[np.ndarray] = None) -> List[str]:
```


#### Counter

`Counter` 是Python的collections模块中的一个类，用于统计可迭代对象中元素的出现次数。

```python linenums="1"
from collections import Counter

results = ['00', '00', '01', '11', '00', '11', '01']

# 使用Counter统计
counter_obj = Counter(results)
print(counter_obj)
# 输出: Counter({'00': 3, '01': 2, '11': 2})
print(type(counter_obj))  # <class 'collections.Counter'>

# 将Counter对象转换为普通字典
counts_dict = dict(counter_obj)
print(counts_dict)
# 输出: {'00': 3, '01': 2, '11': 2}
print(type(counts_dict))  # <class 'dict'>
```
