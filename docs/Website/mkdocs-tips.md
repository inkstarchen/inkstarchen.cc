### 超链接插入
#### 代码
```
[我是一个链接] #在需要的位置放置
[我是一个链接]:https://squidfunk.github.io/mkdocs-material/ #在任意位置放置

```
#### 效果
[我是一个链接] 

[我是一个链接]:https://squidfunk.github.io/mkdocs-material/

### 跨文档连接

```markdown title="doc1.md"
test {#custom-id}
```

```markdown title="doc2.md"
[link](pathto/doc1.md#custom-id)
```
