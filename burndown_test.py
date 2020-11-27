import pandas as pd
import datetime
import matplotlib.pyplot as plt
# import seaborn as sns
import sys
import argparse


def numOfDays(date1, date2): 
    return (date2-date1).days 

def burn(date1, date2, est, toDo):
    # Driver program 
    if date1 == '':
        date1 = datetime.date(2020, 2, 10) 
    elif date1 != '':
        date1 = datetime.date(year=int(date1[0:4]), month=int(date1[4:6]), day=int(date1[6:8]))
    # print(date1)
        
    if date2 == '':
        date2 = datetime.date(2020, 2, 28) 
    elif date2 != '':
        date2 = datetime.date(year=int(date2[0:4]), month=int(date2[4:6]), day=int(date2[6:8]))   
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
    
    today = datetime.date.today()
    
    if today > date2:
        print ('Todays date exceeds timebox')
        return
    else:
        delta = numOfDays(date1, datetime.date.today())
        print (delta)
        
    increment = round(float((est-toDo)/delta),2)
        
    df = pd.DataFrame(columns=('Days','Estimate'))
    for i in range(days,0,-1):
        df.loc[i] = [i, int(est/days*i)]
    
    df.reset_index(drop=True, inplace=True)
    
    df['To_do'] = df.apply(lambda row: (est-(increment*row.name)) if (row['Days'] >= (days-delta)) else toDo,axis=1)
    
    plt.plot(df['Estimate'], label='Estimate')
    plt.plot(df['To_do'],label='To do')
    plt.axvline(x=delta, color='red', linestyle='--', label='Today')
    
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.xticks(df.index.tolist(), rotation=45)
    plt.title('Sprint burndown')
    plt.xlabel('Days')
    plt.ylabel('Effort')
    
    text = f"Remaining 'to do' effort: {toDo} \n in {days - delta} days"
    plt.gcf().text(0.02, 0.5, text, fontsize=8, fontfamily='Comic Sans MS')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-s', '--start', action="store", dest="date1", help="Start date of time box - YYYMMDD", required=True)
    parser.add_argument('-e', '--end', action="store", dest="date2", help="End date of time box - YYYYMMDD", required=True)
    parser.add_argument('-p', '--predict', action="store", dest="est", help="Estimate of work to do - XX", required=True)
    parser.add_argument('-r', '--remain', action="store", dest="toDo", help="Remaining work to do - XX", required=True)
    
    args = parser.parse_args()

    date1 = args.date1
    date2 = args.date2
    est = args.est
    toDo = args.toDo
    # burn(date1=sys.argv[2],date2=sys.argv[3], est=sys.argv[4], toDo=sys.argv[5]) # python burndown_test.py burn <date1> <date2> <est> <todo> 
    burn(date1, date2, est, toDo)

