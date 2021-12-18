import csv
import re
import requests
import time
import calendar
url = 'https://finance.yahoo.com/quote/TSLA/history?p=TSLA'

headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
}

response = requests.get(url,headers=headers)
# Extract data text content
responses = re.findall('"HistoricalPriceStore":{"prices":\[(.*?)]',response.text)
# Extract specific data values
datas = re.findall('"date":(.*?),',responses[0])
opens = re.findall('"open":(.*?),',responses[0])
highs = re.findall('"high":(.*?),',responses[0])
lows = re.findall('"low":(.*?),',responses[0])
closes = re.findall('"close":(.*?),',responses[0])
adjcloses = re.findall('"adjclose":(.*?)}',responses[0])
volumes = re.findall('"volume":(.*?),',responses[0])
# Construct an empty list Add formatted data
data_num = []
for i in range(len(datas)):
    # Convert the obtained timestamp to a specific date month-year-day
    time_time = time.strftime('%m%Y%d',time.localtime(int(datas[i])))
    # Extract specific month
    month = int(time_time[:2])
    # Format date information
    data = str(calendar.month_abbr[month]) + ' ' +time_time[6:]+','+time_time[2:6]
    # Add specific data into the empty list after formatting
    data_num.append(data)
    data_num.append(format(int(str('%.2f'%float(opens[i]))[:-3]),',')+str('%.2f'%float(opens[i]))[-3:])
    data_num.append(format(int(str('%.2f'%float(highs[i]))[:-3]),',')+str('%.2f'%float(highs[i]))[-3:])
    data_num.append(format(int(str('%.2f'%float(lows[i]))[:-3]),',')+str('%.2f'%float(lows[i]))[-3:])
    data_num.append(format(int(str('%.2f'%float(closes[i]))[:-3]),',')+str('%.2f'%float(closes[i]))[-3:])
    data_num.append(format(int(str('%.2f'%float(adjcloses[i]))[:-3]),',')+str('%.2f'%float(adjcloses[i]))[-3:])
    data_num.append(format(int(volumes[i]),','))

# Set the format of the list saved to csv - construct an empty list, and then add the original list to the save list according to special data
myList = []
n = 7
for i in range(0, len(data_num), n):
    myList.append(data_num[i:i+n])
# print(myList)

# Save csv data - save multiple rows
with open("保存的csv数据.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Date", "Open", "High","Low","Close*","Adj Close**","Volume"])   # 先写入columns_name
    writer.writerows(myList)



# Read web page source code and assign value to content
    with open('Yahoo data.text','r',encoding='utf-8')as read_file:
        content = read_file.read()


# Preliminary cleaning and analysis of web data
title1 = re.findall('">(.*?)</span></td><td class=',content)
print(title1)

## Clean the data list after the first analysis and save it into the original list data
title2 = re.findall('data-reactid="52">(.*)',title1[0])
print(title2)
title1[0] = title2[0]

## Extract other data with different appearance data <span data-reactid="1535">16,006,600</span></td></tr><tr class="BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)" data-reactid="1536"><td class="Py(10px) Ta(start) Pend(10px)" data-reactid="1537"><span data-reactid="1538">Jul 27, 2021'
title3 = title1[6:-1:6]

# Clean the data and save the original list <span data-reactid="1546">644.78 <span>标签后的数据提取
for i in range(len(title1)):
     title1[i] = re.findall('>[A-Za-z\d,\. ]+',title1[i])[0].replace('>','')
print(title1)

## Empty list to save cleaned data data：Dec 13, 2021
title9 = []
for i in range(len(title3)):
## Clean the data in title3 and save it to title4 17,002,600, Aug 03, 2021
    title5 = re.findall('>[A-Za-z\d,\. ]+',title3[i])
    title4 = title5[0].replace('>','')+', '+title5[1].replace('>','')
    print(title4)

## Split the data in the list by','       '18,524,900','Sep 13','2021'
title4 = title4.split(', ')
#
## Combine "Sep 13", "2021" and save as "Sep 13, 2021"
title6 = title4[1]+', '+title4[2]

## Extract the first data in the list title4 and save it to title7  18,524,900
title7 = title4[0]
#
## Set list title8 save title6 title7
title8 = ['','']
title8[0]= title7
title8[1]= title6

## Replace the first saved data with the cleaning data title3 - save the extracted 18,524,900
title3[i] = title8[0]
## Save the second data in title8 Sep 13, 2021 to the title9 list
title9.append(title8[1])
print(title9)
#
# # Save the cleaned data to the original list - save the extracted 18,524,900
title1[6:-1:6] = title3

# # Set the index number inserted into the original list
a = 7
# # Insert the data in title9 into the specified position of the original list cyclically Reconstruct the original list
for i in range(len(title9)):
    title1.insert(a,title9[i])
    a += 7
#
# # Set the format of the list saved to csv - construct an empty list, and then add the original list to the save list according to special data
myList = []
n = 7
for i in range(0, len(title1), n):
    myList.append(title1[i:i+n])
    print(myList)
#
# # save as csv file
with open("Tesla.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Date", "Open", "High","Low","Close*","Adj Close**","Volume"])   # 先写入columns_name
    writer.writerows(myList)








