from openpyxl import Workbook
import requests
import matplotlib.pyplot as plt
import pandas as pd
from openpyxl import Workbook
import openpyxl
from datetime import date

codewars = requests.get("https://www.codewars.com/api/v1/users/felipetega")
today=date.today().strftime("%d/%m/%Y")
codewars = codewars.json()
username = codewars["username"]
rank = codewars["ranks"]["overall"]["name"]
honor = codewars["honor"]
codes = codewars["codeChallenges"]["totalCompleted"]
ranking = codewars["leaderboardPosition"]
print(f"{today}, {username}, {rank}, honor: {honor}, completed challenges: {codes}, ranking: {ranking}")

book = Workbook()
sheet = book.active
rows = (("Class","Honor","Total Completed","Ranking"),
        (4,5,6),
        (7,8,9))
for row in rows:
  sheet.append(row)
book.save("Stats.xlsx")
