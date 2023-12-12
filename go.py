import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import uuid
from datetime import datetime
import random
import pytz
def update_google_sheet(sheet_url, sheet_name):
    # 使用 Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)
    client = gspread.authorize(creds)

    # 打開 Google Sheets
    sheet = client.open_by_url(sheet_url)
    worksheet = sheet.worksheet(sheet_name)

    #UTC+8 (台北)
    tz = pytz.timezone('Asia/Taipei')

    while True:
        # 生成 UUID
        unique_id = str(uuid.uuid4())

        # 生成日期和時間
        current_datetime = datetime.now(tz).strftime("%Y-%m-%d %H:%M")

        # 生成隨機 (0 到 3)
        random_number = random.randint(0, 3)

        # 更新儲存格
        worksheet.update('A2', unique_id)
        worksheet.update('B2', current_datetime)
        worksheet.update('C2', random_number)

        # log
        print("unique_id: " + str(unique_id) + " current_datetime: " + str(current_datetime) + " value " + str(random_number))

        # 每 60 秒一次
        time.sleep(60)

sheet_url = 'https://docs.google.com/spreadsheets/d/124mJvQXQOuk9eRBTbCtFmr20suHCwcZ2Ykh45N80BSk/edit?usp=sharing'
update_google_sheet(sheet_url, 'test')
