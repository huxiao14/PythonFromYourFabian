import os
from sklearn import tree
#前面为年龄，后面为性别0为男性1为女性，下一个变量是喜欢的流派
People = [['55','1'],['14','0'],['14','1'],['6','0'],['81','0'],['35','1'],['42','0'],['62','1'],['28','0'],['4','1']]
Music = ['Jazz','Rock','Chinese Sytle','Children','Jazz','Pop','Pop','Classical Music','Pop','Children']
PanDuan = tree.DecisionTreeClassifier()
PanDuan = PanDuan.fit(People,Music)
A = '1'
while A[0] != 'Exit':
    A = str(input('请输入判断的年龄，输入Exit退出'))
    if A == 'Exit':
        print('Thanks')
        break
    C = str(input('请输入判断的性别，男性为0女性为1'))
    B = PanDuan.predict([[A,C]])
    if C == '0':
        print ('电脑判断他喜欢的流派是:',B)
    if C == '1':
        print ('电脑判断她喜欢的流派是:',B)
os.system('pause')
    
