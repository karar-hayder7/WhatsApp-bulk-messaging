import pywhatkit as kit
import pandas as pd
import time
import openpyxl

# Read the CSV file
df = pd.read_excel('list.xlsx')

# Print the column names to verify
print(df.columns)
count = 0
for index, row in df.iterrows():
    # Get the phone number and name
    number = row["Phone number"]
    name = row["Name"]
    name = str(name).strip()
    #print(phone, name)
    


    message = ""

    with open("message.txt", "r", encoding="utf-8") as file:
        lines = file.read()

       

        print(f"Total lines: {len(lines)}")
  
    message =  lines.format(name=name)
    


    
    phone = f"+{number}"
    kit.sendwhatmsg_instantly(phone, message,wait_time= 10,tab_close=True,close_time=10)
    count +=1 
    print(count)

    time.sleep(10)
    
    #kit.sendwhatmsg(phone, message, time_hour, time_minute)





    