from tkinter import *

win = Tk()
win.geometry("450x550")
win.title("계산기")

#버튼 클릭 이벤트 함수
def button_click(value):
    current = ent.get()
    ent.delete(0,END)
    ent.insert(0,current+value)
#=버튼 클릭시 계산수행 입력창의 수식(eval을 사용) 결과를 계산하는 함수
def culculate():
    try:
        result = eval(ent.get())
        ent.delete(0,END)
        ent.insert(0,str(result))
    except Exception as e:
        ent.delete(0,END)
        ent.insert(0,"수식을 입력해주세요")
        
#"c"버튼 클릭 시 입력 초기화
def clear():
    ent.delete(0,END)
#"<-"버튼 클릭시 하나 삭제
def backspace():
    back = ent.get()
    ent.delete(len(back)-1,END)
    


ent = Entry(win,width=20,font=("돋움",20),borderwidth=5,justify="right",relief="sunken")
ent.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

buttons = [
    'c', '<-', '%', '/',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '+/-','0', '.', '='
]
c=0
r=1
for i in buttons:
    if c==4 :
        r+=1
        c=0
    if i == "=":
        btn = Button(win, text=i,width=5,height=2,command=culculate,font=("돋움",20), relief='solid')
    elif i == "c":
        btn = Button(win, text=i,width=5,height=2,command=clear,font=("돋움",20),relief="raised", bg='#FE2E2E')
    elif i == "<-":
            btn = Button(win, text=i,width=5,height=2,command=backspace,font=("돋움",20),relief='raised',bg= '#000000',fg='#FF0000')
    else:
        btn = Button(win, text=i,width=5,height=2,command=lambda b = i:button_click(b),font=("돋움",20))
    btn.grid(column=c,row=r,padx=10,pady=10)
    c+=1



win.mainloop()