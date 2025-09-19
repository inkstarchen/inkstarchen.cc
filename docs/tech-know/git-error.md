## 网络问题
### GitHub连接超时：Failed to connect to github.com port 443: Connection timed out
**解决方法**：1.关闭代理和梯子---->2.执行以下代码重置代理
```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

### Git克隆仓库报错：HTTP/2 stream 1 was not closed
**解决办法**：执行以下代码将通信协议油http/2改为http/1.1
```bash
git config --global http.version HTTP/1.1
```