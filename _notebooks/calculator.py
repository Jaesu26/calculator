## 파이썬의 tkinter를 통해 계산기를 만들어보자
## tkinter import 하기
import tkinter as tk
import tkinter.font

## 윈도우창 생성
window = tk.Tk()

## 윈도우 제목 설정
window.title('계산기')

## 윈도우 창 크기 설정
window.geometry('350x500+800+200')

## 창 크기 조절 불가능
window.resizable(False, False)


## 상단 프레임 설정
upper_frame = tk.Frame(window, width = 400, height = 70)
upper_frame.pack(pady = 40)


## 하단 프레임 설정
down_frame = tk.Frame(window, width = 400, height = 100)
down_frame.pack(padx = 10, pady = 10)


## 계산기 숫자 입력창
entry = tk.Entry(upper_frame, justify = 'right', width = 30, borderwidth = 5)
entry.pack()

font = tk.font.Font(size = 17)


## 1번재 줄 버튼
b_letf_paren = tk.Button(down_frame, text = '(', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1, bg = 'red')
b_letf_paren.grid(row = 0, column = 0, padx = 5, pady = 5)

b_right_paren = tk.Button(down_frame, text = ')', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2 , height = 1, bg = 'red')
b_right_paren.grid(row = 0, column = 1, padx = 5, pady = 5)

b_C = tk.Button(down_frame, text = 'C', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1, bg = 'red')
b_C.grid(row = 0, column = 2, padx = 5, pady = 5)

b_div = tk.Button(down_frame, text = '÷', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1, bg = 'red')
b_div.grid(row = 0, column = 3, padx = 5, pady = 5)


## 2번재 줄 버튼
b_7 = tk.Button(down_frame, text = '7', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1)
b_7.grid(row = 1, column = 0, padx = 5, pady = 5)

b_8 = tk.Button(down_frame, text = '8', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1)
b_8.grid(row = 1, column = 1, padx = 5, pady = 5)

b_9 = tk.Button(down_frame, text = '9', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1)
b_9.grid(row = 1, column = 2, padx = 5, pady = 5)

b_mul = tk.Button(down_frame, text = '×', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1, bg = 'red')
b_mul.grid(row = 1, column = 3, padx = 5, pady = 5)


## 3번재 줄 버튼
b_4 = tk.Button(down_frame, text = '4', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1)
b_4.grid(row = 2, column = 0, padx = 5, pady = 5)

b_5 = tk.Button(down_frame, text = '5', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1)
b_5.grid(row = 2, column = 1, padx = 5, pady = 5)

b_6 = tk.Button(down_frame, text = '6', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1)
b_6.grid(row = 2, column = 2, padx = 5, pady = 5)

b_sub = tk.Button(down_frame, text = '-', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1, bg = 'red')
b_sub.grid(row = 2, column = 3, padx = 5, pady = 5)


## 4번재 줄 버튼
b_1 = tk.Button(down_frame, text = '1', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1)
b_1.grid(row = 3, column = 0, padx = 5, pady = 5)

b_2 = tk.Button(down_frame, text = '2', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1)
b_2.grid(row = 3, column = 1, padx = 5, pady = 5)

b_3 = tk.Button(down_frame, text = '3', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1)
b_3.grid(row = 3, column = 2, padx = 5, pady = 5)

b_add = tk.Button(down_frame, text = '+', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1 , bg = 'red')
b_add.grid(row = 3, column = 3, padx = 5, pady = 5)


## 5번재 줄 버튼
b_sign = tk.Button(down_frame, text = '+/-', bd = 2.5, padx = 15, pady = 10, font = font, width = 2, height = 1)
b_sign.grid(row = 4, column = 0, padx = 0, pady = 2)

b_0 = tk.Button(down_frame, text = '0', bd = 2.5, padx = 15, pady = 10, font = font, width = 2, height = 1)
b_0.grid(row = 4, column = 1, padx = 5, pady = 2)

b_point = tk.Button(down_frame, text = '.', bd = 2.5, padx = 15, pady = 10, font = font, width = 2, height = 1)
b_point.grid(row = 4, column = 2, padx = 5, pady = 2)

b_equal = tk.Button(down_frame, text = '=', bd = 2.5, padx = 15, pady = 10, font = font, width = 2, height = 1, bg = 'red')
b_equal.grid(row = 4, column = 3, padx = 5, pady = 2)



## 종료할 때까지 윈도우창 띄우기
window.mainloop()