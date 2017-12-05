# price = 10000.0
# for i in range(5):
#     price = price + (price*0.1)
#
# print(price)

score = [90, 100, 86, 92, 77]
sum = 0
ave = 0
score.sort(reverse=True)
print(score)

for n in score:
    sum += n

print("총점:",sum)
print("평균:",sum / len(score))