import gspread
from oauth2client.service_account import ServiceAccountCredentials

# authentication of logs #
def key_log_read():
    scope = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\Administrator\\Desktop\\service\\sheetData\\api\\sheet_credentials.json", scopes = scope)
    file = gspread.authorize(creds).open("Students").get_worksheet(0).get_all_values()
    # print(file)
    # workbook = file.open("Students")
    # sheet = file.get_worksheet(0)
    # sheet_data = sheet.get_all_values()
    return file


print(key_log_read())

    # print(len(sheet))