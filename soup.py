from bs4 import BeautifulSoup
import os
import pandas as pd

all_data=[]
for file in os.listdir('data'):
    with open(f'data/{file}',encoding='utf-8')as f:
         html_doc=f.read()
         soup =BeautifulSoup(html_doc,'html.parser')
         try:
            t = soup.find('h2')
            title = t.get_text() if t else ''
         except Exception as e:
            title = ''

         try:
            r = soup.find('span', class_='a-icon-alt')
            rating = r.get_text() if r else ''
         except Exception as e:
            rating = ''

         try:
            p = soup.find('span', class_='a-price')
            price = p.get_text() if p else ''
         except Exception as e:
            price = ''

         try:
            las_m = soup.find('span', class_='a-size-base a-color-secondary')
            last_monthpurchase = las_m.get_text() if las_m else ''
         except Exception as e:
            last_monthpurchase = ''

      

         try:
          link = 'https://www.amazon.com' + (soup.find('a')['href'] if soup.find('a') else '')
         except Exception as e:
          link = ''
         

         all_data.append({
            'Name': title,
            'Price': price,
         
            'Rating': rating,
            'Last Month Purchase': last_monthpurchase,
            'Website': link
        })
    
         
        




df = pd.DataFrame(all_data)
df.to_csv('output.csv', index=False)

print("Data saved to output.csv")
    # print(soup.prettify())

