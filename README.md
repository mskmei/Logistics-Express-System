# 快递物流系统
## <div align="center">部署说明</div>
下载全部后，将文件名改为“物流快递系统”，项目名不宜轻易修改。

环境需求：需要安装 Python 与 MySQL 的最新版本。（此处使用：python==3.9.2, Mysql==8.0.28）。Python 需要安装 Django(4.0.4),folium(0.12.1),pandas(1.3.0)宏包。

数据库搭建：**在 MySQL 平台运行数据库文件夹中的 sql 文件**，创建数据库‘express’的表结构，通过 csv 导入模拟数据（optional）。也可直接将 express 表复制到本地 MySQL 数据文件夹中并重
启 MySQL 服务。

预设调整：在路径“/物流公司系统/物流公司系统”下的 setting.py 文件中，将
DATABASES 下的’USER’、’PASSWORD’、’HOST’ 及’PORT’改为运行主机的 MySQL 实例配
置（账户要有 express 表的所有权限）。TIME_ZONE 的属性改为公司当前所在地。在路径“/物
流公司系统/app01”下的 views.py 文件中，将视图 depaheatmap 和 destheatmap 下的 file_path
改为运行主机该项目的 templates 路径。 服务器启动：在 Python 平台运行 Django 项目‘物流
公司系统’，或在物流公司系统项目下输入指令’python manage.py runserver‘，便可部署系统。默
认的 IP 地址为 127.0.0.1，端口为 8000。

另外，如果要使用热力图需要修改 views.py 中第 135 行
与 147 行处两个文件的位置。
