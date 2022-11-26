## 문제 정의하기


문제 상황: 설계할 때 시간을 안 보게됨 
- Q: 왜 내가 설계할 때 시간을 안 보게 될까?
- A: 설계할 땐 화면이 안 보여서 작업 표시줄 숨기기를 했기 때문
- Q: 왜 작업 표시줄을 숨기면 시간을 안 보게 되는가?
- A: 작업 표시줄에 마우스 커서를 올리면 시간이 보이는데, 뭔가 귀찮고 굳이? 시간을 확인 안하게 됨.

<br/>

- Q: 어떻게 하면 작업 표시줄을 숨기고도 시간을 자주 확인하게 할 수 있을까?
- ✔️: 항상 윈도우 창 위에 시간을 표시하는 앱을 띄우면 됨.



<br/>
<br/>
<br/>

## 요구사항 도출하기
- 시간을 표시하는 앱을 만들어야 함
- 앱은 항상 윈도우 창 위에 표시되어야 함
- 마우스 왼쪽 버튼을 누르고 드래그하면 윈도우 창을 이동할 수 있어야 함
- 마우스 오른쪽 버튼을 누르면 프로그램이 종료되어야 함
- 마우스 가운데 버튼을 누르면 Dark/Date 모드가 전환되어야 함


<br/>
<br/>
<br/>





## 코드


```python
# Path: main.py
# GUI clock
# This program displays a digital clock with a GUI

from tkinter import *
from time import strftime

win = Tk()
win.attributes("-topmost", 1)
win.overrideredirect(1)


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(win, font=("ds-digital", 10), background="black", foreground="white")


def drag_start(event):
    win.x = event.x
    win.y = event.y


def drag_motion(event):
    x = (event.x_root - win.x - win.winfo_rootx() + win.winfo_rootx())
    y = (event.y_root - win.y - win.winfo_rooty() + win.winfo_rooty())
    win.geometry("+%s+%s" % (x, y))


def change_color(event):
    if label.cget("foreground") == "white":
        label.config(foreground="black")
        label.config(background="white")
    else:
        label.config(foreground="white")
        label.config(background="black")


label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_motion)
label.bind("<Button-2>", change_color)
label.bind('<Button-3>', lambda e: win.destroy())
label.pack(anchor='center')

time()

mainloop()
```

#### 코드 설명

- ``Tk()``: Tkinter의 메인 윈도우를 생성합니다.
- ``win.attributes("-topmost", 1)``: 윈도우를 최상위로 설정합니다.
- ``win.overrideredirect(1)``: 윈도우의 테두리를 없앱니다.

<br/>

- ``def time():``: 시간을 표시하는 함수입니다.
- ``strftime('%H:%M:%S %p')``: 현재 시간을 문자열로 반환합니다.
- ``label.config(text=string)``: 라벨의 텍스트를 설정합니다.
- ``label.after(1000, time)``: 1초 후에 ``time()`` 함수를 실행합니다.

<br/>

- ``Label(win, font=("ds-digital", 10), background="black", foreground="white")``: 라벨을 생성합니다. ``win``은 라벨이 위치할 윈도우를 지정합니다. ``font``는 라벨의 폰트를 지정합니다. ``background``는 라벨의 배경색을 지정합니다. ``foreground``는 라벨의 글자색을 지정합니다.

<br/>

- ``def drag_start(event):``: 윈도우를 드래그하기 위한 함수입니다.
- ``win.x = event.x``: 윈도우의 x좌표를 저장합니다.
- ``win.y = event.y``: 윈도우의 y좌표를 저장합니다.

<br/>

- ``def drag_motion(event):``: 마우스를 드래그할 때 윈도우의 위치를 변경하기 위한 함수입니다.
- ``x = (event.x_root - win.x - win.winfo_rootx() + win.winfo_rootx())``: 윈도우의 x좌표를 계산합니다.
- ``y = (event.y_root - win.y - win.winfo_rooty() + win.winfo_rooty())``: 윈도우의 y좌표를 계산합니다.
- ``win.geometry("+%s+%s" % (x, y))``: 윈도우의 위치를 변경합니다.

<br/>

- ``def change_color(event):``: 라벨의 색을 변경하는 함수입니다.
- ``if label.cget("foreground") == "white":``: 라벨의 글자색이 흰색이면
- ``label.config(foreground="black")``: 라벨의 글자색을 검은색으로 변경합니다.
- ``label.config(background="white")``: 라벨의 배경색을 흰색으로 변경합니다.
- ``else:``: 라벨의 글자색이 검은색이면
- ``label.config(foreground="white")``: 라벨의 글자색을 흰색으로 변경합니다.
- ``label.config(background="black")``: 라벨의 배경색을 검은색으로 변경합니다.
- ``label.bind("<Button-1>", drag_start)``: 라벨을 클릭했을 때 ``drag_start()`` 함수를 실행합니다.
- ``label.bind("<B1-Motion>", drag_motion)``: 라벨을 드래그할 때 ``drag_motion()`` 함수를 실행합니다.
- ``label.bind("<Button-2>", change_color)``: 라벨의 위에서 마우스 가운데 클릭했을 때 ``change_color()`` 함수를 실행합니다.
- ``label.bind("<Button-3>", lambda e: win.destroy()))``: 라벨을 오른쪽 클릭했을 때 윈도우를 종료합니다.

<br/>

- ``time()``: time() 함수를 실행합니다.
- ``mainloop()``: 윈도우를 실행합니다.