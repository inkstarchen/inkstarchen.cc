- 环境：
	- 服务器：Ubuntu-20.4
	- 笔记本：Windows 11 

在使用RealVNC viewer尝试连接云服务器的时候黑屏，无法连接，下方提示`unencrypted connection`

在网上查询解决方案后，采用以下方案后能够正常启动桌面：

在`.vnc/xstartup`中加入

```sh
sesion-manager &       # 应该是 xfce4-session (会话管理器)
xfdesktop &            # 桌面管理器
xfce4-panel &          # 顶部/底部面板
xfce4-menu-plugin &    # 应用程序菜单插件
xfsettingsd &          # 设置守护进程
xfconfd &              # 配置守护进程
xfwm4 &                # 窗口管理器
```

### 原因解析

- 推测是没有正常启动桌面显示的功能
- 经查询以上指令组合能够启动一个完整的Xfce4 桌面环境