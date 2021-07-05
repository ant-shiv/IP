import pandas as pd
data = {"   " : [500,501,502],
        'Name': ['Ishant Verma', 'Kapil Tyagi', 'Ruhi Sen'],
        'Class':[9,9,9],
        'Sec':['A',"B","B"],
        'Project name':['App development','Machine Learning','Block coding']
        }
project = pd.DataFrame(data,index=['500',' ','502'])
grade = ['D', 'B', 'C']
project['grade'] = grade
new_row = {'phone no':''}
project = project.append(new_row, ignore_index=True)
print(project)