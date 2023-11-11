x1, y1, r1 = map(int, input("원1의 중심좌표와 반지름의 길이를 입력하세요 :").split())
x2, y2, r2 = map(int, input("원2의 중심좌표와 반지름의 길이를 입력하세요 :").split())
D = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))**0.5
if D > r1 + r2:
  print("만나지 않음")
if D == r1+r2:
  print("한 점에서 만남")
if D < r1+r2:
  print("두 점에서 만남")