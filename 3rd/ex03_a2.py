# 試験の成績結果の配列の値をグレードに変換して出力するプログラムを
# if 文を使って作りなさい。

def grading(score):
  if(score >= 90):
    return 'S'
  elif(score >= 80):
    return 'A'
  elif(score >= 70):
    return 'B'
  elif(score >= 60):
    return 'C'
  else:
    return 'F'

scores = [76, 98, 80, 69, 49, 88, 71, 66, 82, 100]
grades = []
for i in range(10):
  grades.append(grading(scores[i]))
print(grades)

