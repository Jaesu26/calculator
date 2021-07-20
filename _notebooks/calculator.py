## 파이썬의 tkinter를 통해 계산기를 만들어보자
## tkinter import 하기
import tkinter as tk

## 윈도우창 생성
window = tk.Tk()

## 윈도우 제목 설정
window.title('계산기')

## 윈도우 창 크기 설정
window.geometry('350x500+800+200')

## 종료할 때까지 윈도우창 띄우기
window.mainloop()