from openpyxl import load_workbook
import requests
from datetime import date

# Data from api
codewars = requests.get("https://www.codewars.com/api/v1/users/felipetega")
today = date.today().strftime("%d/%m/%Y")
codewars = codewars.json()
username = codewars["username"]
rank = -codewars["ranks"]["overall"]["rank"]
honor = codewars["honor"]
codes = codewars["codeChallenges"]["totalCompleted"]
ranking = codewars["leaderboardPosition"]
print(f"{today}, {username}, {rank}, honor: {honor}, completed challenges: {codes}, ranking: {ranking}")

# Load wb
workbook_name = 'Stats.xlsx'
wb = load_workbook(workbook_name)
page = wb.active

# New data to write:
new_dataset = [[today, rank, honor, codes, ranking]]
for data in new_dataset:
    page.append(data)

# Save data
wb.save(filename=workbook_name)
