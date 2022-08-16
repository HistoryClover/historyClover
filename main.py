from tkinter import*
from tkinter import LabelFrame
def click():
    try:
        gost=bhh.get()
        ro=float(gost)
        go = lll.get()
        r = float(go)
        ttt=round(ro/(r**2),1)
        if (ttt<=18.0):
            la.config(text="результат\n" + str(ttt) + "кг/м^2"+
                      "   -недостаток веса 2 степени")
        if (18.1<=ttt<=20.0):
            la.config(text="результат\n" + str(ttt) + "кг/м^2" +
                           "   -недостаток веса 1 степени")
        if (20.1<=ttt<=25.0):
            la.config(text="результат\n" + str(ttt) + "кг/м^2" +
                           "   -нормальный вес")
        if(25.0<=ttt<=27.0):
            la.config(text="результат\n" + str(ttt) + "кг/м^2" +
                           "   -есть лишний вес")
        if(27.1<=ttt<=30.0):
            la.config(text="результат\n" + str(ttt) + "кг/м^2" +
                           "   -ожирение 1 степени")
        if(30.1<=ttt<=35.0):
            la.config(text="результат\n" + str(ttt) + "кг/м^2" +
                           "   -ожирение 2 степени")
        if(ttt>35.0):
            la.config(text="результат\n" + str(ttt) + "кг/м^2" +
                           "   -ожирение 3 степени")
    except ZeroDivisionError:
        la.config(text="ошибка")
    except NameError:
        la.config(text="ошибка")
    except SyntaxError:
        la.config(text="ошибка")
    except ValueError:
        la.config(text="ошибка")
    except TypeError:
        la.config(text="ошибка")
    except RecursionError:
        la.config(text="ошибка")
    except ArithmeticError:
        la.config(text="ошибка")
    except RuntimeError:
        la.config(text="ошибка")
    except KeyboardInterrupt:
        la.config(text="ошибка")
    except AssertionError:
        la.config(text="ошибка")
    except AttributeError:
        la.config(text="ошибка")
    except ModuleNotFoundError:
        la.config(text="ошибка")
    except KeyError:
        la.config(text="ошибка")
    except LookupError:
        la.config(text="ошибка")
    except MemoryError:
        la.config(text="ошибка")
root=Tk()
root.title("Clover Index mass")
root.config(bg="Cyan")
root.geometry("450x680")
root.resizable(height=False,width=False)
la=Label(root, text="результат\n-",font=30,bg="Cyan",fg="green")
la.pack(side=BOTTOM,pady=40)
km=LabelFrame(root,text="точка(.) вместо запятой(,) для записи дробного числа",height=25,width=450,bg="DarkTurquoise",fg="black")
km.pack(side=TOP)
hh=LabelFrame(root,text="ввод массы тела(кг)",height=25,width=450,bg="DarkTurquoise",fg="black")
hh.pack(pady=(4,0))
bhh = Entry(root,font=20,width=40,bg="DarkTurquoise")
bhh.pack(pady=(5,0))
kkk=LabelFrame(root,text="ввод роста (м)",height=25,width=450,bg="Turquoise",fg="black")
kkk.pack(pady=(6,0))
lll = Entry(root,font=20,width=40,bg="Turquoise")
lll.focus_set()
lll.pack(pady=(7,0))
btn=Button(root,text="старт",font=10,bg="aquamarine",command=click,fg="black",)
btn.pack(side=TOP,pady=(10,0))
root.mainloop()
