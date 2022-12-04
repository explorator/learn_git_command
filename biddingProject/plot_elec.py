import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
path=os.path.realpath(os.curdir)
pycharm_project_path=os.path.dirname(path)
cur_path=os.path.join(pycharm_project_path,'biddingProject')

np.random.seed(1024)
random_index=np.random.randint(0,53504,10)
x_axis=np.array([i for i in range(24)])

target_file='datasets/after_convert_target.csv'
p50_file='datasets/after_convert_p50_forecast.csv'
df_target=pd.read_csv(os.path.join(cur_path,target_file),index_col=0)
df_target_filter=df_target.iloc[random_index]

df_p50=pd.read_csv(os.path.join(cur_path,p50_file),index_col=0)
df_p50_filter=df_p50.iloc[random_index]

print(df_target_filter)
print('*'*30)
print(df_p50_filter)
# refect_dic={0:'6075',1:'9105',2:'47713',3:'35308',4:'19045',5:'601',6:'4961',7:'14669',8:'10784',9:'1347'}
#
# plt.figure(figsize=(30,30),dpi=200)
# for i in range(10):
#     single_target=df_target_filter.iloc[i,2:].values
#     single_p50=df_p50_filter.iloc[i,2:].values
#     plt.plot(x_axis,single_target,color='blue',linewidth=3,linestyle='-',label='target')
#     plt.plot(x_axis,single_p50,color='green',linewidth=3,linestyle='-.',label='p50')
#     plt.xlim(0,24)
#     plt.xticks(np.linspace(0,24,25,endpoint=True))
#     plt.xlabel('hour')
#     plt.ylabel('use_power')
#     plt.title('The index of the sample is '+refect_dic[i])
#     plt.legend()
#     number_str='plt_picture/'+refect_dic[i]+'.jpg'
#     plt.savefig(os.path.join(cur_path,number_str))
    # plt.show()
