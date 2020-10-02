from openpyxl import Workbook

#Workbook을 하나 만들어서
# 시트제목을 articles로 하고
# 행을 추가한다.
wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사"])

wb.save(filename='articles.xlsx')