import pandas as pd
import os
data = pd.DataFrame()
name = os.listdir('data')
for i  in range(len(name)):
    path1 = 'data/'+name[i]

    name2 = os.listdir(path1)

    for e in range(len(name2)):
        if name2[e] =='Test':
            path2 =path1+'/'+name2[e]
            name3 = os.listdir(path2)
            for f in range(len(name3)):
                path3 = path2+'/'+name3[f]
                print(path3)
                data1 = pd.read_table(path3, header=None, names=['Time', 'data'], sep="]",quoting=3)
                data1['label']=name[i]
                # print(data1)
                data = pd.concat([data,data1],axis=0)
                # print(path3)
                # print(name[i])
print(data)


data.to_csv('test.csv')


