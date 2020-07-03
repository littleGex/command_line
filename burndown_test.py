import pandas as pd
import datetime
import matplotlib.pyplot as plt
# import seaborn as sns
import sys

def numOfDays(date1, date2): 
    return (date2-date1).days 

def burn(date1, date2, est, toDo):
    # Driver program 
    if date1 == '':
        date1 = datetime.date(2020, 2, 10) 
    elif date1 != '':
        date1 = datetime.date(year=int(date1[0:4]), month=int(date1[5:6]), day=int(date1[6:8]))
    # print(date1)
        
    if date2 == '':
        date2 = datetime.date(2020, 2, 28) 
    elif date2 != '':
        date2 = datetime.date(year=int(date2[0:4]), month=int(date2[5:6]), day=int(date2[6:8]))   
    # print(date2)
        
    print(numOfDays(date1, date2), "days")
    
    days = numOfDays(date1, date2)
    
    if est == '':
        est = int(108)
    elif est != '':
        est = int(est)
    # print(est)
    
    if toDo == '':
        toDo = int(48.5)
    elif toDo != '':
        toDo = int(toDo)
    # print(toDo)
    
    today = numOfDays(date1, datetime.date.today())
    # to =datetime.date(2020,2,15)
    # today = numOfDays(date1,to)
    increment = round(float((est-toDo)/today),2)
    
    # df = pd.DataFrame(columns=('Days','Estimate','To_do'))
    df = pd.DataFrame(columns=('Days','Estimate'))
    
    
    for i in range(days,0,-1):
        # df.loc[i] = [i, int(est/days*i), int(est-(increment*i))]
        df.loc[i] = [i, int(est/days*i)]
    
    df.reset_index(drop=True, inplace=True)
    
    # df['To_do'] = df.apply(lambda row: (est-(increment*row.name)),axis=1)
    df['To_do'] = df.apply(lambda row: (est-(increment*row.name)) if ( row['Days'] >= (days-today)) else toDo,axis=1)
    # print(df)   
     
    # for i in range(days,0,-1):
    #     df.loc[i] = [i, int(est/days*i), df.To_do.rolling(3)-increment]
    
    # b = int(est-((est-toDo)/today))
    # b
    
    plt.plot(df['Estimate'], label='Estimate')
    plt.plot(df['To_do'],label='To do')
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.xticks(df.index.tolist(), rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # if len(sys.argv) == 6:
    #     burn(date1=sys.argv[2],date2=sys.argv[3], est=sys.argv[4], toDo=sys.argv[5]) # python burndown_test.py burn <date1> <date2> <est> <todo>
    # elif len(sys.argv) != 6:
    #     print('number of inputs not correct, please check')
    
    # python burndown_test.py burn 20200505 20200630 40 15 - As an example. Graph will not be correct if today() falls outside this time box
    burn(date1=sys.argv[2],date2=sys.argv[3], est=sys.argv[4], toDo=sys.argv[5]) # python burndown_test.py burn <date1> <date2> <est> <todo> 
