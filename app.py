import fire
import time
import sys
from loongchain.chain import Chain

class makeList:
    index = {}
    todoes = {}
    order = 1
    def do(self,record):
        '''copyright owned by crillerium'''
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
    chain = Chain(sys.argv[0].replace('app.py','data'))
    todoes = []
    def __init__(self):
        make = makeList()
        self.chain.run(make)
        self.todoes = list(make.todoes.values())
    def home(self):
        '''
        首页
        '''
        print('所有任务列表:')
        print('共',len(self.todoes),'项')
        for i in range(0,len(self.todoes)):
            print('[',str(i+1),']',self.todoes[i]['title'])

    def add(self):
        '''
        添加
        '''
        action = 'new'
        title = input('请输入标题: ')
        detail = input('请输入详情: ')
        current = str(time.time())
        self.chain.apply({'action':action,'title':title,'detail':detail,'time':current})

    def done(self,order:int):
        '''
        完成
        '''
        task = self.todoes[order-1]['time']
        action = 'done'
        current = str(time.time())
        self.chain.apply({'action':action,'time':current,'task':task})
        print('已完成第'+str(order)+'项任务')

    def show(self,order:int):
        '''
        详情
        '''
        title = self.todoes[order-1]['title']
        detail = self.todoes[order-1]['detail']
        timestamp = self.todoes[order-1]['time']
        time_local = time.localtime(float(timestamp))
        when = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
        print('[任务标题]',title)
        print('[创建时间]',when)
        print('[任务详情]',detail)

if __name__ == '__main__':
    try:
        fire.Fire(Todo)
    except Exception as e:
        print(e)