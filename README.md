# Blockchain-Todo
## 区块链任务清单
一个由区块链数据结构强力支持的任务清单

# Features
## 特性
1. 使用命令行
2. 采用区块链数据库
3. 显示所有任务
4. 显示指定任务详情
5. 完成指定任务

# Installation
## 安装
1.下载源码或Releases并解压
(有需要的可以自行修改文件权限)
2.Blockchain-Todo采用的区块链数据库为Loongchain  
(https://github.com/Crillerium/Loongchain)  
而Loongchain已经受到软件著作权保护  
安装方法:  
`pip3 install loongchain-0.6-py3-none-any.whl`  
3. Loongchain安装完成后请执行:
`pip install fire`  

至此依赖以安装完成
# Usage
## 使用方法
1.帮助文档  
执行命令 `py app.py` 可查看由fire生成的标准文档  
2.快捷用法:  
`py app.py home`查看所有任务  
`py app.py add`添加一个任务  
`py app.py show <序号>` 展示序号对应的任务详情  
`py app.py done <序号>` 完成序号对应的任务  
