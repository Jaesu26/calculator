## 파이썬의 tkinter를 통해 계산기를 만들어보자
## tkinter import 하기
'''
버전2 계산기입니다
버전1 계산기에 부족한 기능을 추가했습니다
6×4 크기로 구성했습니다

새로운 기능: 제곱, 제곱근, 자연로그, Backspace, 보류(π, e)
'''
import tkinter as tk
import tkinter.font
from math import pi
from math import e
from math import sqrt
from math import log

## 윈도우창 생성
window = tk.Tk()

## 윈도우 제목 설정
window.title('계산기')

## 윈도우 창 크기 설정
window.geometry('360x560+800+200')

## 창 크기 조절 불가능
window.resizable(False, False)


## 상단 프레임 설정
upper_frame = tk.Frame(window)
upper_frame.pack(pady = 40)


## 하단 프레임 설정
down_frame = tk.Frame(window)
down_frame.pack(padx = 10, pady = 10)


## 계산기 숫자 입력창
entry = tk.Entry(upper_frame, justify = 'right', width = 30, borderwidth = 5)
entry.pack()


## 함수 설정
## 초기화
reset = 0

## 숫자 클릭
def number_button_click(num):
    global reset
    
    current_entry = entry.get()
    new_entry = current_entry + str(num)
    
    if reset == 1 or reset == 2:
        entry.delete(0, 'end')
        entry.insert(0, str(num))
    
    elif len(current_entry) < 1:
        entry.insert(0, str(num))
        
    else:
        last = current_entry[-1]
        
        if last != 'e' and last != 'π':
            entry.delete(0, 'end')
            entry.insert(0, new_entry)
                 
    reset = 0
    
## 등호 클릭
def equal_button_click():
    global reset
    
    if reset == 1 or reset == 2:
        entry.delete(0, 'end')
        
    current_entry = entry.get()
    op = ['÷', '×', 'π', '^', '√', 'ln']
    ch_op = ['/', '*', 'pi', '**', 'sqrt', 'log']
    op_idx = 0
    
    for op_chr in op:
        if current_entry.find(op_chr) != -1:
            current_entry = current_entry.replace(op_chr, ch_op[op_idx])
        op_idx += 1
            
    try:
        rtn = eval(current_entry)
        entry.delete(0, 'end')
        entry.insert(0, rtn)
        reset = 1
        
    except ZeroDivisionError:
        error_message = '0으로 나눌 수 없습니다'
        entry.delete(0, 'end')
        entry.insert(0, error_message)
        reset = 2
        
    except (SyntaxError, TypeError, ValueError):
        error_message = '잘못된 수식입니다'
        entry.delete(0, 'end')
        entry.insert(0, error_message)
        reset = 2
        
    
## 사칙연산 클릭
def operation_button_click(op):
    global reset
    
    if reset == 2:
        entry.delete(0, 'end')  
        
    test_entry = current_entry = entry.get()
    test_entry = test_entry.replace('÷', '+') 
    test_entry = test_entry.replace('×', '+')
    test_entry = test_entry.replace('-', '+')
    test_list = test_entry.split('+')
            
    
    if len(current_entry) > 0:
        last = current_entry[-1]
        test_idx = test_list[-1]
        condition = last != '+' and last != '-' and last != '×' and last != '÷'
    
        if condition and last != '.':
            new_entry = current_entry + op
            entry.delete(0, 'end')
            entry.insert(0, new_entry)
        
        if test_idx == '.':
            entry.delete(0, 'end')
            entry.insert(0, current_entry)
                
        if condition and test_idx != '.':
            new_entry = current_entry + op
            entry.delete(0, 'end')
            entry.insert(0, new_entry)
                
    reset = 0
            
## entry clear
def clear_button_click():
    global reset
    reset = 0
    
    entry.delete(0, 'end')

    
## parentheses operation
def paren_button_click(paren):
    global reset
    
    current_entry = entry.get()
    new_entry = current_entry + paren
    
    if reset == 1 or reset == 2:
        entry.delete(0, 'end')
        entry.insert(0, paren)
        
    else:
        entry.delete(0, 'end')
        entry.insert(0, new_entry)
    
    reset = 0

## decimal point
def point_button_click():
    global reset
    
    if reset == 1 or reset == 2:
        entry.delete(0, 'end')
        entry.insert(0, '.')
    
    test_entry = current_entry = entry.get()
    new_entry = current_entry + '.'
        
    if current_entry.find('.') == -1:
        entry.delete(0, 'end')
        entry.insert(0, new_entry)
        
    else:
        test_entry = test_entry.replace('÷', '+') 
        test_entry = test_entry.replace('×', '+')
        test_entry = test_entry.replace('-', '+')
        
        if len(test_entry) < 1:
            entry.insert(0, '.')
        
        else:
            test_list = test_entry.split('+')
            test_idx = test_list[-1]
            
            if test_idx.find('.') == -1:
                entry.delete(0, 'end')
                entry.insert(0, new_entry)
                 
    reset = 0

## plus, minus sign  
def plus_minus_button_click():
    global reset
    
    current_entry = entry.get()
    new_entry = current_entry + '-'
    
    if reset == 1 or reset == 2:
        entry.delete(0, 'end')
        entry.insert(0, '-')
    
    elif current_entry == '':
        entry.delete(0, 'end')
        entry.insert(0, '-')
        
    elif len(current_entry) > 0:
        last = current_entry[-1]
        
        if last == '+' or last == '-' or last == '×' or last == '÷' or last == '(' or last == ')':
            entry.delete(0, 'end')
            entry.insert(0, new_entry)
        
    reset = 0    


## Backspace 
def backspace_button_click():
    global reset
    
    if reset == 1 or reset == 2:
        entry.delete(0, 'end')
        
    else:
        current_entry = entry.get()[:-1]
        entry.delete(0, 'end')
        entry.insert(0, current_entry)
    
    reset = 0


## Transcendental number(pi and e)
def transcendental_number_button_click(tran_num):
    global reset

    if reset == 1 or reset == 2:
        entry.delete(0, 'end')
        entry.insert(0, tran_num)
    
    current_entry = entry.get()
    new_entry = current_entry + tran_num
    
    if len(current_entry) < 1:
        entry.insert(0, tran_num)
        
    else:
        last = current_entry[-1]
        
        if last == '+' or last == '-' or last == '×' or last == '÷' or last == '(':
            entry.delete(0, 'end')
            entry.insert(0, new_entry)
                 
    reset = 0

    
## 제곱
def square_button_click():
    global reset
    
    current_entry = entry.get()
    new_entry = current_entry + '^2'
    
    if reset == 1 or current_entry == '':
        entry.delete(0, 'end')
        
    if reset == 2:
        entry.delete(0, 'end')
        entry.insert(0, new_entry)
        
    else:
        last = current_entry[-1]
        
        if last != '+' and last != '-' and last != '×' and last != '÷' and last != '(':
            entry.delete(0, 'end')
            entry.insert(0, new_entry)
                 
    reset = 0    
    
## 제곱근(√)
def square_root_button_click():
    global reset
    
    current_entry = entry.get()
    new_entry = current_entry + '√('
    
    if reset == 1 or reset == 2 or current_entry == '':
        entry.delete(0, 'end')
        entry.insert(0, '√(')
        
    else:
        last = current_entry[-1]
        
        if last == '+' or last == '-' or last == '×' or last == '÷' or last == '(':
            entry.delete(0, 'end')
            entry.insert(0, new_entry)
    
    reset = 0
    
## 자연로그
def log_e_button_click():
    global reset
    
    current_entry = entry.get()
    new_entry = current_entry + 'ln('
    
    if reset == 1 or reset == 2 or current_entry == '':
        entry.delete(0, 'end')
        entry.insert(0, 'ln(')
        
    else:
        last = current_entry[-1]
        
        if last == '+' or last == '-' or last == '×' or last == '÷' or last == '(':
            entry.delete(0, 'end')
            entry.insert(0, new_entry)
    
    reset = 0

    
## 버튼 폰트 설정

font = tk.font.Font(size = 17)

## 1번재 줄 버튼(제곱, 제곱근, 자연로그, Backspace)
b_power = tk.Button(down_frame, text = 'x²', bd = 2.5, padx = 15, pady = 10, font = font, width = 2, height = 1, bg = 'Magenta', command = square_button_click)
b_power.grid(row = 0, column = 0, padx = 0, pady = 2)

b_root = tk.Button(down_frame, text = '√', bd = 2.5, padx = 15, pady = 10, font = font, width = 2, height = 1, bg = 'Magenta', command = square_root_button_click)
b_root.grid(row = 0, column = 1, padx = 5, pady = 2)

b_log_e = tk.Button(down_frame, text = 'ln', bd = 2.5, padx = 15, pady = 10, font = font, width = 2, height = 1, bg = 'Magenta', command = log_e_button_click)
b_log_e.grid(row = 0, column = 2, padx = 5, pady = 2)

b_backspace = tk.Button(down_frame, text = '⌫', bd = 2.5, padx = 15, pady = 10, font = font, width = 2, height = 1, bg = 'Magenta', command = backspace_button_click)
b_backspace.grid(row = 0, column = 3, padx = 5, pady = 2)


## 2번재 줄 버튼
b_letf_paren = tk.Button(down_frame, text = '(', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1, bg = 'red', command = lambda: paren_button_click('('))
b_letf_paren.grid(row = 1, column = 0, padx = 5, pady = 5)

b_right_paren = tk.Button(down_frame, text = ')', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2 , height = 1, bg = 'red', command = lambda: paren_button_click(')'))
b_right_paren.grid(row = 1, column = 1, padx = 5, pady = 5)

b_C = tk.Button(down_frame, text = 'C', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1, bg = 'red', command = clear_button_click)
b_C.grid(row = 1, column = 2, padx = 5, pady = 5)

b_div = tk.Button(down_frame, text = '÷', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1, bg = 'red', command = lambda: operation_button_click('÷'))
b_div.grid(row = 1, column = 3, padx = 5, pady = 5)


## 3번재 줄 버튼
b_7 = tk.Button(down_frame, text = '7', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1, command = lambda: number_button_click(7))
b_7.grid(row = 2, column = 0, padx = 5, pady = 5)

b_8 = tk.Button(down_frame, text = '8', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1, command = lambda: number_button_click(8))
b_8.grid(row = 2, column = 1, padx = 5, pady = 5)

b_9 = tk.Button(down_frame, text = '9', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1, command = lambda: number_button_click(9))
b_9.grid(row = 2, column = 2, padx = 5, pady = 5)

b_mul = tk.Button(down_frame, text = '×', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1, bg = 'red', command = lambda: operation_button_click('×'))
b_mul.grid(row = 2, column = 3, padx = 5, pady = 5)


## 4번재 줄 버튼
b_4 = tk.Button(down_frame, text = '4', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1, command = lambda: number_button_click(4))
b_4.grid(row = 3, column = 0, padx = 5, pady = 5)

b_5 = tk.Button(down_frame, text = '5', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1, command = lambda: number_button_click(5))
b_5.grid(row = 3, column = 1, padx = 5, pady = 5)

b_6 = tk.Button(down_frame, text = '6', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1, command = lambda: number_button_click(6))
b_6.grid(row = 3, column = 2, padx = 5, pady = 5)

b_sub = tk.Button(down_frame, text = '-', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1, bg = 'red', command = lambda: operation_button_click('-'))
b_sub.grid(row = 3, column = 3, padx = 5, pady = 5)


## 5번재 줄 버튼
b_1 = tk.Button(down_frame, text = '1', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1, command = lambda: number_button_click(1))
b_1.grid(row = 4, column = 0, padx = 5, pady = 5)

b_2 = tk.Button(down_frame, text = '2', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1, command = lambda: number_button_click(2))
b_2.grid(row = 4, column = 1, padx = 5, pady = 5)

b_3 = tk.Button(down_frame, text = '3', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1, command = lambda: number_button_click(3))
b_3.grid(row = 4, column = 2, padx = 5, pady = 5)

b_add = tk.Button(down_frame, text = '+', bd = 2.5,  padx = 15, pady = 10, font = font, width = 2, height = 1 , bg = 'red', command = lambda: operation_button_click('+'))
b_add.grid(row = 4, column = 3, padx = 5, pady = 5)


## 6번재 줄 버튼
b_sign = tk.Button(down_frame, text = '+/-', bd = 2.5, padx = 15, pady = 10, font = font, width = 2, height = 1, command = plus_minus_button_click)
b_sign.grid(row = 5, column = 0, padx = 0, pady = 2)

b_0 = tk.Button(down_frame, text = '0', bd = 2.5, padx = 15, pady = 10, font = font, width = 2, height = 1, command = lambda: number_button_click(0))
b_0.grid(row = 5, column = 1, padx = 5, pady = 2)

b_point = tk.Button(down_frame, text = '.', bd = 2.5, padx = 15, pady = 10, font = font, width = 2, height = 1, command = point_button_click)
b_point.grid(row = 5, column = 2, padx = 5, pady = 2)

b_equal = tk.Button(down_frame, text = '=', bd = 2.5, padx = 15, pady = 10, font = font, width = 2, height = 1, bg = 'red', command = equal_button_click, activebackground = 'blue')
b_equal.grid(row = 5, column = 3, padx = 5, pady = 2)



## 종료할 때까지 윈도우창 띄우기
window.mainloop()