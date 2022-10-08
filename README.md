#### 开发环境

Python 3.9 

MySQL Server 8.0.27

PyMySQL 1.0.2

#### 如何搭建环境

+ 首先在官网上下载Python3.9，然后下载Pycharm，添加GIthub账户
+ 在我的电脑的系统环境变量Path添加python.exe
+ 下载MySQL Sever,在MySQL Sever目录下 sc delete MySql删除Mysql服务
+ 在MySQL Sever目录中新建my.ini配置文件
+ 在MySQL Sever目录下mysqld --initialize-insecure --user=mysql重新生成data文件
+ 在MySQL Sever目录下mysqld --install "MySql80" --defaults-file="my.ini的路径" 重新安装mysql服务，同时绑定my.ini配置文件
+ 启动服务
+ 在Pycharm上下载PyMysql，Numpy，matploib安装包
+ 在Pycharm上添加Python解释器

#### 项目结构

main.py是连接数据库将数据保存在数据库中以及计算E值（可修改table_num的值）

myRandom.py是随机数生成算法

mysqlOperation.py是有关于MySQL的一系列操作，包括创建、新增、更新、查询、删除等等

Test.py是在每门课一学期都点相同次数（160次）的情况下，计算每门课的e值并传递给main.py

Train.py是抽点检测的算法

#### 功能描述

最小化向后端发送的请求次数，最大化抓出缺勤同学的数量

