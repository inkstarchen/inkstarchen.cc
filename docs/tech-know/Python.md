## Python

### seaborn：可视化库

```python title="heatmap" linenums="1"
sns.heatmap(df.corr(), cmap='coolwarm', annot=True);
```

### super: 调用父类函数

```python title="super" linenums="1"
class A():
	def add(x);

class B(A):

super(B,self).add(x)
```

### 累加器

```python title="累加器" linenums="1"
# 假设我们有3个累积量，比如损失、准确率和梯度。
accumulator = Accumulator(3)

# 在每个训练步骤中，我们可以调用 add 方法
for epoch in range(epochs):
    for X, y in data_loader:
        loss = model(X, y)  # 假设这是计算损失的函数
        accuracy = compute_accuracy(model, X, y)
        # 将损失、准确率和梯度累加
        accumulator.add(loss.item(), accuracy, model.parameters())
        
    # 在每个epoch结束时，获取平均值
    avg_loss, avg_accuracy, avg_gradient = accumulator.avg()
    print(f"Epoch {epoch}: loss = {avg_loss}, accuracy = {avg_accuracy}")

```

### torch.no_grad()不计算梯度，因为不用反向传播
```python title="torch.no_grad()" linenums="1"
    animator = d2l.Animator(xlabel='epoch', xlim=[1, num_epochs],legend=['train loss', 'train acc', 'test acc'])
```

- nn.Dense 即 nn.Linear

