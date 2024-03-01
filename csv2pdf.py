# Input: A csv file
# Output: A pdf file
# Process: Read the .csv file, and convert it to the html format to draw the table, and then save as a .pdf file
#
# In this file uses wkhtmltopdf, please download and install it: https://wkhtmltopdf.org/downloads.html
#
# Import the required Module
#import pdfplumber
import re
import string
import csv
import pdfkit

# Edit the following four values
csv_path = 'files/test.csv' # Give a .csv file as Input
html_path = 'files/test.html' # Give a .html file as temporary file
output_pdf_path = 'files/test.pdf' #Give a .pdf file as Output
output_path = 'files/output.txt' # The log file of translated data


#regex
zhStr = re.compile(u'[\u4e00-\u9fa5]+') # 中文
enStr = re.compile(u'[\u0041-\u005a|\u0061-\u007a]+') # English

#html
message_start = f"""
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">"""
    
message_style = """
    <style type="text/css" media="screen">
        table {border:1px solid #ccc;}
        th, td {padding:5px 15px;}
        th {background:#66cc00; color:#fff;}		
        tr:nth-child(odd) {background:#E6F5F5;}
    </style>
</head>
<body>
    <table>
		<tr>
			<th>捐款日期</th><th>會員編號</th><th>姓氏</th><th>稱謂</th><th>捐款金額</th>
		</tr>
"""
message_body = """"""
message_end = """</table></body></html>"""


f = open(output_path, 'w', encoding='utf-8')
htmlfile = open(html_path, 'w', encoding='utf-8')

with open(csv_path, newline='', encoding='utf-8') as csvfile:
    rows = csv.reader(csvfile, delimiter=';') # 記得指定 csv 的 delimiter  
    for row in rows:
        #print(', '.join(row))    
        donate_date = row[0] #捐款日期
        donor_id = row[1] #會員編號
        donor_name = row[2] #姓氏
        donor_title = row[3] #稱謂
        donate_amount = row[4] #捐款金額        
        
        if zhStr.search(donor_name): #中文姓氏
            if donor_name != '無名氏' and len(donor_name) > 2: #姓氏不為'無名氏'，且多於2個字
                f.writelines(str(donor_id) + ', ' + donor_name + '\n')
                donor_name = donor_name[:1] #只擷取第一個字
        elif enStr.search(donor_name):
            donor_name_split = donor_name.split() #英文姓氏
            if len(donor_name_split) > 1: #多於2個英文單字
                f.writelines(str(donor_id) + ', ' + donor_name + '\n')
                donor_name = donor_name_split[0] #只擷取第一個單字
        else: #非中文、非英文姓氏
            if len(donor_name) > 2: #多於2個字
                f.writelines(str(donor_id) + ', ' + donor_name + '\n')
                donor_name = donor_name[:1] #只擷取第一個字
                
        if donate_date != '捐款日期' and donate_date.lower() != 'date':
            message_body += string.Template("""<tr>
                                    <td>${donate_date}</td><td>${donor_id}</td><td>${donor_name}</td><td>${donor_title}</td><td>${donate_amount}</td>
                                </tr>""").substitute(locals())

messages = (message_start + message_style + message_body + message_end)
htmlfile.write(messages)

f.close()
csvfile.close()
htmlfile.close()
print('Converted to HTML')

#從 .html 轉為 .pdf
#請指定 wkhtmltopdf 執行檔的位置
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=bytes(path_wkhtmltopdf, 'utf-8'))
pdfkit.from_file(html_path, output_pdf_path, configuration=config)
    
print('Converted to PDF and Done')
