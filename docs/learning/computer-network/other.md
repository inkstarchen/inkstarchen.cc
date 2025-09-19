-  什么是公网
	- 公网IP是可以通过Internet直接访问的IP地址.(IP与主机或服务区一对一唯一)
- 什么是私网
	- 在局域网中每台连接到互联网的设备都有一个私有IP，以供路由器来识别.
- 什么是端口
	- 端口是用于提供不同的服务所使用的(应用程序的标识)

- 什么是传输协议
	- 即对数据传输的规定规则.
	- TCP协议：安全协议，三次握手，速度慢
	- UDP协议：不安全协议，速度快
	- 应用层的传输协议，如HTTP,IMAP等，都是基于上述协议
- "What is the FTP"
	- **FTP**:File Transfer Protocol is a TCP protocol for downloading files between computers.

- "How to use FTP"
	- **First**:install vsftpd with`sudo apt install vsftpd`
	
	- **Second**:set up User Authenticated FTP Configuration 
		
	- edit `/etc/vsftpd.conf`
	- ``write_enable=YES``
	- Now restart the service with `sudo systemctl restart vsftpd.service`

- "What is the SFTP"
	- **SFTP**: Secure File Transfer Protocol is a protocol for transferring files between computers over an encrypted connection.

- "How to use SFTP"
	- **First**:install ssh with`sudo apt install ssh`
	
	- **Second**:Creating a new user group for SFTP with `sudo addgroup [group-name]`
	
	- **Third**:Creating a new user for SFTP with `sudo adduser [user-name] `
	
	- and add a password for the user with `sudo passwd [user-name]` 
	
	- then add the user to the group with `sudo usermod -a -G [group-name] [user-name]`

	- **Fourth**:Create and configure a directory for SFTP
	- So first,create a new directory with `sudo mkdir `sudo mkdir -p /var/sftp/[directory-name]`
	- then change the ownership of the directory with `sudo chown root:root /var/sftp`
	- Next, change the permissions for the same directory by giving all rights to the root and others can only read and execute
	`sudo chmod 755 /var/sftp`
	- And finally, change the ownership of the directory you've created for SFTP for the recently created user:
	- `sudo chown inkstar:inkstar /var/sftp/inkstar`

	- **Fifth**:Make changes to the SSHD config file
	- edit `/etc/ssh/sshd_config` with `sudo vim /etc/ssh/sshd_config`
	- add the following lines to the file:
	- ``Match group sftp
	ChrootDirectory /var/sftp
	X11Forwarding no
	AllowTcpForwarding no
	AllowAgentForwarding no
	ForceCommand internal-sftp``

	Match group sftp allows you to specify settings for the specific group.
	ChrootDirectory /home: It ensures that the user won't be able to access anything apart from /var/sftp.
	X11Forwarding no: By disabling the X11 port forwarding, you can save yourself from the vulnerabilities of the X11.
	AllowTcpForwarding no: Ensures that the user can not create arbitrary network connections from the SFTP server.
	AllowAgentForwarding no: It is a security measure and ensures that any compromised server cannot misuse the client's SSH keys.
	ForceCommand internal-sftp: It forces the connection to run upon the login and disables the shell.

	**Sixth**:Restart the SSH service with `sudo systemctl restart ssh`
	**Seventh**:Verigying the SFTP configuration


??? "What is the SSH"
	**SSH**: Secure Shell Protocol is a protocol for securely connecting to a remote computer over an unsecured network.

	??? "The difference between SSH and openSSH"
		ssh depends on openSSH,which means that if you install the ssh package, you will also install openSSH first.

## npm解决Cannot find module 'semver'的问题
执行以下命令
``
sudo apt remove nodejs

sudo apt remove npm

sudo apt remove autoremove
``
进入/usr/local/lib删除所有node和node_modules文件夹
进入/usr/local/include删除所有node和node_modules文件夹
进入/usr/local/bin删除node的可执行文件

**安装最新版nodejs**

先安装curl和git包
``sudo apt install git curl``

然后安装nodejs
``
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -

sudo apt-get install nodejs -y

sudo apt-get install npm
``

## 图床构建
什么是图床：一个用于存储图片的第三方在线静态资源库，其返回一个图片的URL.