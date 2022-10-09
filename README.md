### 开发环境

+ 所用软件

  Python 3.9 

  MySQL Server 8.0.27

  PyCharm 2022.1.1 (Community Edition）

+ 所需的包：

  PyMySQL 1.0.2

  numpy

  matplotlib

### 如何搭建环境

#### 1. python环境：

+ 首先在官网上下载Python3.9，然后下载Pycharm，添加Github账户
+ 在我的电脑的系统环境变量Path添加python.exe
+ 在pycharm中下载运行软件所需要的包，并添加所需要的python解释器
+ 详细可参见 [(21条消息) PyCharm安装和配置_明之季的博客-CSDN博客_pycharm配置](https://blog.csdn.net/u011125673/article/details/115375359)

#### 2. MySQL环境

+ 下载MySQL Sever,在MySQL Sever目录下 sc delete MySql删除Mysql服务
+ 在MySQL Sever目录中新建my.ini配置文件
+ 在MySQL Sever目录下mysqld --initialize-insecure --user=mysql重新生成data文件
+ 在MySQL Sever目录下mysqld --install "MySql80" --defaults-file="my.ini的路径" 重新安装mysql服务，同时绑定my.ini配置文件
+ 启动服务并修改密码，建议将密码设置为123456，或者修改main文件中的密码
+ 创建一个database：create database attendance;
+ 详细可参见[MySQL的安装与配置——详细教程 - Winton-H - 博客园 (cnblogs.com)](https://www.cnblogs.com/winton-nfs/p/11524007.html)

#### 项目结构

main.py是连接数据库将数据保存在数据库中以及计算E值（可修改table_num的值）

myRandom.py是随机数生成算法

mysqlOperation.py是有关于MySQL的一系列操作，包括创建、新增、更新、查询、删除等等

Test.py是用于计算每门课的e值并传递给main.py

Train.py是抽点检测的算法

#### 功能描述

最小化向后端发送的请求次数，最大化抓出缺勤同学的数量

