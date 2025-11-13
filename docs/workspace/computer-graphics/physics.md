## 射线检测

### Slab Method

#### 直观理解

**Slab（平板）** 在三维空间中可以理解为两个平行平面之间的无限空间区域。想象一下：

- 在现实生活中：一本书的两页之间的空间、三明治的两片面包之间的区域
    
- 在数学上：由两个平行平面定义的无界空间

#### 代码过程

由于射线与AABB包围盒最多两个交点，则用`t_min`和`t_max`分别代表射线进入Slab的最晚时间，和出Slab的最早时间.

> 射线必须依次先经过三个不同的slab平面，才能与AABB有交，这是因为，三个不同的slab围成了AABB的空间，只有同时存在三个slab空间中时才是在AABB空间中，假如先穿出了其中一个slab平面，而还没进入另一个slab平面，则不存在同时进入三个slab空间的情况.

以 x 轴为例：

- 若射线方向的x分量为0，则代表射线平行于y-z平面，这时需要确定射线是否在y-z平面组成的slab中.
	- 如果在的话，则与y-z平面没有交点，全局的`t_min`和`t_max`不需要更新
	- 如果不在，则与AABB包围盒没有交点，直接返回`false`
    
```ts
if (ray.d.x === 0) {   
  if (ray.o.x <= ab.aabbMin.x || ray.o.x >= ab.aabbMax.x) {  
    return false;  
  }  
}
```
- 若射线方向的x分量不为0，则计算出与两个平面的交点长度,由于不知道射线方向，因此需要进行检测交换.

```ts
let invD = 1.0 / ray.d.x;  
let t1 = (ab.aabbMin.x - ray.o.x) * invD;  
let t2 = (ab.aabbMax.x - ray.o.x) * invD;  
  
if (t1 > t2) {  
  let temp = t1;  
  t1 = t2;  
  t2 = temp;  
}
```

- 更新全局值

```ts
tmin = Math.max(tmin, t1);  
tmax = Math.min(tmax, t2);  
  
if (tmin > tmax) return false;
```

- 如果`tmax`大于等于0，则射线从AABB中穿过或起点在AABB内
- 如果`tmin`小于等于0，则射线起点在AABB内