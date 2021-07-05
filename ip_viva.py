import pandas as pd

data = {"   " : [500,501,502],
        'Name': ['Ishant Verma', 'Kapil Tyagi', 'Ruhi Sen'],
        'Class':[9,9,9],
        'Sec':['A',"B","B"],
        'Project name':['App development','Machine Learning','Block coding']
        }
project = pd.DataFrame(data,index=[500,' ',502])
project.iloc[::3, : ]
grade = ['D', 'B', 'C']
project['grade'] = grade
project.tail(1)
print(project)