import openpyxl

# 새로운 Excel 파일 생성
wb = openpyxl.Workbook()

# 기본 시트 선택
sheet = wb.active

# 데이터 입력
sheet["A1"] = "Hello"
sheet["B1"] = "World!"

# 파일 저장
wb.save("example.xlsx")