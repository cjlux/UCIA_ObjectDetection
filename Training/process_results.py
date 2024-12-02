######################################
#   Jean-Luc.Charles@mailo.com
#   2024/11/14 - v1.0
######################################

import pandas as pd

print(50*'*', "\n* Sort by 'recall' & 'mAP50-95'\n", 50*'*', sep='')   

for version in ('v8n', '11n', 'v8s', '11s'):
    txt_file = f'results_yolo{version}.txt'
    print(f'\nFile <{txt_file}>', end="")
    
    # read CSV file with panda:
    df = pd.read_csv(txt_file, sep='\t', header=0, skiprows=[1])
    
    # sort rows by descending order of columns "recall","mAP50-95":
    df = df.sort_values(by=["recall","mAP50-95", ], ascending=False)
    
    # the first values in columns "recall" and "mAP50-95  are the max values:
    max_mAP50_90 = df['mAP50-95'].values[0]
    max_recall   = df['recall'].values[0]
    print(f'\n\tMax values -> "max_recall": {max_recall}, "max_mAP50-90": {max_mAP50_90}')
    
    # selected  significant columns
    df1 = df[['#meta-params', 'recall', 'mAP50-95', 'fitness']]
    
    # print the first 4 rows:
    print(df1.head(4))
    

print(50*'*', "\n\n* Sort by 'fitness'\n", 50*'*', sep='')   

for version in ('v8n', '11n', 'v8s', '11s'):
    txt_file = f'results_yolo{version}.txt'
    print(f'\nFile <{txt_file}>', end="")
    
    # read CSV file with panda:
    df = pd.read_csv(txt_file, sep='\t', header=0, skiprows=[1])
    
    # now sort rows by descending order of column "fitnes":
    df = df.sort_values(by=["fitness"], ascending=False)
    
    # the first values in column "fitness" is the max values:
    max_fitness = df['fitness'].values[0]
    print(f'\n\tMax values -> "fitness": {max_fitness}')
    
    # selected  significant columns
    df2 = df[['#meta-params', 'recall', 'mAP50-95', 'fitness']]
    
    # print the first 4 rows:
    print(df2.head(4))
