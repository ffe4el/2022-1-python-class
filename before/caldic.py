eat_orange = int(input("한라봉의 섭취량을 입력하세요. => "))
eat_strawberry = int(input("딸기의 섭취량을 입력하세요. => "))
eat_banana = int(input("바나나의 섭취량을 입력하세요. => "))

calories = {"한라봉": 49, "딸기":35, "바나나":80}
total_calories = calories["한라봉"]*eat_orange + calories["딸기"]*eat_strawberry + calories["바나나"]*eat_banana

print("총 섭취 칼로리량은 {} 입니다." .format(total_calories))