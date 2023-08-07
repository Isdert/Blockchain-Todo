import fire
import time
import sys
import os
from loongchain.chain import Chain

class makeList:
    index = {}
    todoes = {}
    order = 1
    def do(self,record):
        '''Copyright Owned By Crillerium'''
        if record['action'] == 'new':
            self.index[self.order] = record['time']
            self.todoes[self.order] = record
            self.order+=1
        elif record['action'] == 'done':
            for key,value in self.index.items():
                if value == record['task']:
                    target = key
            self.index.pop(target)
            self.todoes.pop(target)

class Todo:
    chain = Chain(sys.path[0]+os.sep+'blockchain_todo_data')
    todoes = []
    def __init__(self):
        make = makeList()
        self.chain.run(make)
        self.todoes = list(make.todoes.values())
    def home(self):
        '''
        查看所有任务
        '''
        print('所有任务列表:')
        print('共',len(self.todoes),'项')
        for i in range(0,len(self.todoes)):
            print('[',str(i+1),']',self.todoes[i]['title'])

    def add(self):
        '''
        添加新的任务
        '''
        action = 'new'
        title = input('请输入标题: ')
        detail = input('请输入详情: ')
        current = str(time.time())
        if (title == '') or (detail == ''):
            print('添加失败,标题和详情不能为空!')
        else:
            self.chain.apply({'action':action,'title':title,'detail':detail,'time':current})
            print('添加成功!')

    def done(self,order:int):
        '''
        标记指定任务已完成
        '''
        task = self.todoes[order-1]['time']
        action = 'done'
        current = str(time.time())
        self.chain.apply({'action':action,'time':current,'task':task})
        print('已完成第'+str(order)+'项任务')

    def show(self,order:int):
        '''
        查看指定任务详细信息
        '''
        title = self.todoes[order-1]['title']
        detail = self.todoes[order-1]['detail']
        timestamp = self.todoes[order-1]['time']
        time_local = time.localtime(float(timestamp))
        when = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
        print('[任务标题]',title)
        print('[创建时间]',when)
        print('[任务详情]',detail)
    def check(self):
        '''
        审查数据安全性和完整性
        '''
        if self.chain.check():
            print('审查完成,当前Blockchain_Todo数据安全')
            print('建议定期审查,确保数据完整和安全')
        else:
            print('当前Blockchain_Todo数据疑似遭到修改! 建议提交反馈给Crillerium')
            print('提交地址: https://github.com/crillerium/blockchain-todo/issues')

def main():
    try:
        fire.Fire(Todo)
    except Exception as e:
        print(e)
