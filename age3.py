#!/usr/bin/python3

driving = input('請問你沒有開過車')
if driving != '有' and driving != '沒有':
    print('請好好回答')
    raise SystemExit

age = input('請問你的年齡')
age = int(age)
if driving == '有':
    if age >= 18:
        print('你通過測驗')
    else:
        print('幹犯法哦')
elif driving == '沒有':
    if age >= 18:
        print('可以考駕照了啊')
    else:
        print('嘖嘖，年輕人')