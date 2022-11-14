list1 = {
"0": 1,
"1": 0,
"2": 0,
"3": 0,
"4": 0,
"5": 0,
"6": 1,
"7": 0,
"8": 2,
"9": 1
}
n = input()
summ = 0

for i in n:
  summ += list1[i]
print(summ)