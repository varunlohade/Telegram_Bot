import requests
import csv
import time
import pandas as pd
def countdown(t):
    
    while t:
        
        time.sleep(1)
        t -= 1
      
def send_msg(text):
    token = 'token_telegram'
    chat_id = '-1001640811578'
    url_req = f'https://api.telegram.org/bot{token}/sendMessage' +'?chat_id='+chat_id+'&text='+text
    results = requests.get(url_req)
    print(results.json())


file = open('jobs.csv')
# df = pd.read_csv(file)
# print(df)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
for i in range(len(rows)-2):
 
    
    
    print(i)
    stri = f"**{i}) {rows[i][1]}**\n\n{rows[i][2]}\n{rows[i][3]}\n {i+1}){rows[i+1][1]}**\n{rows[i+1][2]}\n{rows[i+1][3]}\n \n{rows[i+2][1]}**\n\n{rows[i+2][2]}\n{rows[i+2][3]}\n"
    # print(f"**{rows[i][1]}**\n\n{rows[i][2]}\n{rows[i][3]}\n \n \n {rows[i+1][1]}**\n\n{rows[i+1][2]}\n{rows[i+1][3]}\n \n \n{rows[i+2][1]}**\n\n{rows[i+2][2]}\n{rows[i+2][3]}\n \n \n ")
    send_msg(stri)
    countdown(600)
    print(" ")
  




