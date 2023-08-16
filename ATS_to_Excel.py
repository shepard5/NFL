import pandas as pd
from ATS_Streak import NFL_ATS

def NFL_ATS_to_Excel():

    streak_data = []
    
    for x in range(1,35):
        if x in [31,32]:
            continue
        
        ATS_streak = NFL_ATS(str(x))
        streak_data.append([x, ATS_streak])
            
    print(streak_data)
    
    df = pd.DataFrame(streak_data, columns=['Variable1', 'Variable2'])

    with pd.ExcelWriter('ATS_Streak_output.xlsx', engine='openpyxl') as writer:
        df.to_excel(writer, index = False) 
    

