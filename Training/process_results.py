import pandas as pd

for version in ('v8n', '11n', 'v8s', '11s'):
    txt_file = f'results_yolo{version}.txt'
    print(f'\nFichier <{txt_file}>', end="")
    
    df = pd.read_csv(txt_file, sep='\t', header=0, skiprows=[1])
    
    df = df.sort_values(by=["recall","mAP50-95", ], ascending=False)
    max_mAP50_90 = df['mAP50-95'].values[0]
    max_recall   = df['recall'].values[0]
    print(f' - Valeurs max -> "max_recall": {max_recall}, "max_mAP50-90": {max_mAP50_90}\n')
    
    n = ((df['recall'].values > max_recall - 0.001)*(df['mAP50-95'].values >= max_mAP50_90 - 0.009)).argmin()
    df = df[['#meta-params', 'recall', 'mAP50-95']]
    
    print(df.head(4))
    
