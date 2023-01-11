import tkinter as tk
import tkinter.messagebox as msg
from tkinter import *
import numpy as np
import pyautogui as screen

##FUNCIONES DEL ARCHIVO
def main():
    generate_graphics()

def generate_graphics():
    #Ventana principal
    window = tk.Tk()
    window.title("Proyecto de unidad - Universidad de las Fuerzas Armadas - ESPE")
    window.resizable(0,0)
    window.iconbitmap("ProyectoP2\\favicon.ico")
    window.wm_iconbitmap("ProyectoP2\\favicon.ico")
    window_width = 800
    window_height = 600
    width_screen, height_screen = screen.size()
    window_pos_width = (width_screen/2) - (window_width/2)
    window_pos_heigth = (height_screen/2) - (window_height/2)
    pos = str(int(window_width)) + "x" + str(int(window_height))+"+"+str(int(window_pos_width)) + "+" + str(int(window_pos_heigth))
    window.geometry(pos)
    window.config(bg="black")

    #Frames
    Frm_title = tk.Frame(window)
    Frm_title.configure(width=800, height=100, bg='#2B2823')
    Frm_title.place(x=0, y=0)
    Frm_Menu = tk.Frame(window)
    Frm_Menu.configure(width=800, height=25, bg="#205225")
    Frm_Menu.place(x=0, y=100)
    Frm_Principal = tk.Frame(window)
    Frm_Principal.configure(width=800, height=500, bg='#f9fadc')
    Frm_Principal.place(x=0, y=125)
    Frm_MatrizA = tk.Frame(Frm_Principal)
    Frm_MatrizA.configure(width=300, height=280 , bg='#8fa691')
    Frm_MatrizA.place(x=36, y=100)
    Frm_MatrizX = tk.Frame(Frm_Principal)
    Frm_MatrizX.configure(width=50, height=280 , bg='#d4ceaa')
    Frm_MatrizX.place(x=404, y=100)
    Frm_Resultados = tk.Frame(Frm_Principal)
    Frm_Resultados.configure(width=70, height=190, bg='#cc3917')
    Frm_Resultados.place(x=605, y=174)
    Frm_Parametros = tk.Frame(Frm_Principal)
    Frm_Parametros.configure(width=200, height=80, bg="#FFFFFF")
    Frm_Parametros.place(x=544, y=53)

    #Matriz de coeficientes

    txt_a11 = tk.Entry(Frm_MatrizA)
    txt_a11.configure(font=("Inter",12), fg="black", bg="white")
    txt_a11.place(x=44, y=28, width=32, height=32)
    txt_a11.focus()
    txt_a12 = tk.Entry(Frm_MatrizA)
    txt_a12.configure(font=("Inter",12), fg="black", bg="white")
    txt_a12.place(x=104, y=28, width=32, height=32)
    txt_a13 = tk.Entry(Frm_MatrizA)
    txt_a13.configure(font=("Inter",12), fg="black", bg="white")
    txt_a13.place(x=164, y=28, width=32, height=32)
    txt_a14 = tk.Entry(Frm_MatrizA)
    txt_a14.configure(font=("Inter",12), fg="black", bg="white")
    txt_a14.place(x=224, y=28, width=32, height=32)
    txt_a21 = tk.Entry(Frm_MatrizA)
    txt_a21.configure(font=("Inter",12), fg="black", bg="white")
    txt_a21.place(x=44, y=88, width=32, height=32)
    txt_a22 = tk.Entry(Frm_MatrizA)
    txt_a22.configure(font=("Inter",12), fg="black", bg="white")
    txt_a22.place(x=104, y=88, width=32, height=32)
    txt_a23 = tk.Entry(Frm_MatrizA)
    txt_a23.configure(font=("Inter",12), fg="black", bg="white")
    txt_a23.place(x=164, y=88, width=32, height=32)
    txt_a24 = tk.Entry(Frm_MatrizA)
    txt_a24.configure(font=("Inter",12), fg="black", bg="white")
    txt_a24.place(x=224, y=88, width=32, height=32)
    txt_a31 = tk.Entry(Frm_MatrizA)
    txt_a31.configure(font=("Inter",12), fg="black", bg="white")
    txt_a31.place(x=44, y=148, width=32, height=32)
    txt_a32 = tk.Entry(Frm_MatrizA)
    txt_a32.configure(font=("Inter",12), fg="black", bg="white")
    txt_a32.place(x=104, y=148, width=32, height=32)
    txt_a33 = tk.Entry(Frm_MatrizA)
    txt_a33.configure(font=("Inter",12), fg="black", bg="white")
    txt_a33.place(x=164, y=148, width=32, height=32)
    txt_a34 = tk.Entry(Frm_MatrizA)
    txt_a34.configure(font=("Inter",12), fg="black", bg="white")
    txt_a34.place(x=224, y=148, width=32, height=32)
    txt_a41 = tk.Entry(Frm_MatrizA)
    txt_a41.configure(font=("Inter",12), fg="black", bg="white")
    txt_a41.place(x=44, y=208, width=32, height=32)
    txt_a42 = tk.Entry(Frm_MatrizA)
    txt_a42.configure(font=("Inter",12), fg="black", bg="white")
    txt_a42.place(x=104, y=208, width=32, height=32)
    txt_a43 = tk.Entry(Frm_MatrizA)
    txt_a43.configure(font=("Inter",12), fg="black", bg="white")
    txt_a43.place(x=164, y=208, width=32, height=32)
    txt_a44 = tk.Entry(Frm_MatrizA)
    txt_a44.configure(font=("Inter",12), fg="black", bg="white")
    txt_a44.place(x=224, y=208, width=32, height=32)
    txt_max_iter = tk.Entry(Frm_Parametros)
    txt_max_iter.configure(font=("Inter",10), fg="black", bg="#D9D9D9")
    txt_max_iter.place(x=150, y=13, width=40, height=20)
    txt_max_iter.setvar()
    txt_tolerancia = tk.Entry(Frm_Parametros)
    txt_tolerancia.configure(font=("Inter",10), fg="black", bg="#D9D9D9")
    txt_tolerancia.place(x=150, y=46, width=40, height=20)

    #Terminos independientes
    txt_x1 = tk.Entry(Frm_MatrizX)
    txt_x1.configure(font=("Inter",12), fg="black", bg="white")
    txt_x1.place(x=9, y=28, width=32, height=32)
    txt_x2 = tk.Entry(Frm_MatrizX)
    txt_x2.configure(font=("Inter",12), fg="black", bg="white")
    txt_x2.place(x=9, y=88, width=32, height=32)
    txt_x3 = tk.Entry(Frm_MatrizX)
    txt_x3.configure(font=("Inter",12), fg="black", bg="white")
    txt_x3.place(x=9, y=148, width=32, height=32)
    txt_x4 = tk.Entry(Frm_MatrizX)
    txt_x4.configure(font=("Inter",12), fg="black", bg="white")
    txt_x4.place(x=9, y=208, width=32, height=32)

    #Resultados
    lbl_b1 = tk.Label(Frm_Resultados)
    lbl_b1.configure(font=("Inter",8, "bold"), fg="white", bg="#cc3917", state="disabled")
    lbl_b1.place(x=5, y=15)
    lbl_b2 = tk.Label(Frm_Resultados)
    lbl_b2.configure(font=("Inter",8, "bold"), fg="white", bg="#cc3917", state="disabled")
    lbl_b2.place(x=5, y=61)
    lbl_b3 = tk.Label(Frm_Resultados)
    lbl_b3.configure(font=("Inter",8, "bold"), fg="white", bg="#cc3917", state="disabled")
    lbl_b3.place(x=5, y=106)
    lbl_b4 = tk.Label(Frm_Resultados)
    lbl_b4.configure(font=("Inter",8, "bold"), fg="white", bg="#cc3917", state="disabled")
    lbl_b4.place(x=5, y=152)

    #Labels
    lbl_tittle = tk.Label(Frm_title, bg='#2b2823')
    lbl_tittle.configure(font=("Corinthia",60), text="Métodos Numéricos", fg='white')
    lbl_tittle.place(x=180, y=-10)
    lbl_matrix = tk.Label(Frm_Principal)
    lbl_matrix.configure(text="Matriz de coeficientes 4x4:", font=("Inter",12, "bold"), fg="black", bg='#f9fadc')
    lbl_matrix.place(x=83, y=67)
    lbl_X = tk.Label(Frm_Principal)
    lbl_X.configure(text="X", font=("Inter",12, "bold"), fg="black", bg="#f9fadc")
    lbl_X.place(x=359, y=229)
    lbl_equal = tk.Label(Frm_Principal)
    lbl_equal.configure(text="=", font=("Inter",12, "bold"),fg="black", bg="#f9fadc")
    lbl_equal.place(x=476, y=229)
    lbl_resultado = tk.Label(Frm_Principal)
    lbl_resultado.configure(text="Resultados:", font=("Inter",12, "bold"), fg="black", bg="#f9fadc")
    lbl_resultado.place(x=595, y=141)
    lbl_terminos = tk.Label(Frm_Principal)
    lbl_terminos.configure(text="Términos\nindependientes:", font=("Inter",12, "bold"), fg="black", bg="#f9fadc")
    lbl_terminos.place(x=368, y=44)
    lbl_axb = tk.Label(Frm_Principal)
    lbl_axb.configure(text="A * x = b", font=("Inter",40, "bold"), fg="black", bg="#f9fadc")
    lbl_axb.place(x=317, y=408)
    lbl_parametros = tk.Label(Frm_Principal)
    lbl_parametros.configure(text="Parámetros:",font=("Inter",16, "bold"), fg="black", bg="#F9FADC")
    lbl_parametros.place(x=592, y=20)
    lbl_max_iter = tk.Label(Frm_Parametros)
    lbl_max_iter.configure(text="Máximo iteraciones:",font=("Inter",10, "bold"), fg="black", bg="#FFFFFF")
    lbl_max_iter.place(x=10, y=14)
    lbl_tolerancia = tk.Label(Frm_Parametros)
    lbl_tolerancia.configure(text="Tolerancia:",font=("Inter",10, "bold"), fg="black", bg="#FFFFFF")
    lbl_tolerancia.place(x=10, y=48)

    #Botones
    btn_Calcular = tk.Button(Frm_Principal)
    btn_Calcular.configure(text="Calcular", font=("Inter",10, "bold"), fg="white", bg='#2b2823')
    btn_Calcular.place(x=592, y=383, width=100, height=30)
    btn_Limpiar = tk.Button(Frm_Principal)
    btn_Limpiar.configure(text="Limpiar", font=("Inter",10, "bold"), fg="white", bg='#2b2823')
    btn_Limpiar.place(x=604, y=422, width=75, height=25)
    btn_Gauss = tk.Button(Frm_Menu)
    btn_Gauss.configure(text="Gauss-Seidel", font=("Inter",10, "bold"), fg="white", bg='#205225', relief="ridge", bd=1)
    btn_Gauss.place(x=0, y=0, width=125, height=25)
    btn_Interpolacion = tk.Button(Frm_Menu)
    btn_Interpolacion.configure(text="Interpolacion", font=("Inter",10, "bold"), fg="white", bg='#205225', relief="ridge", bd=1)
    btn_Interpolacion.place(x=125, y=0, width=125, height=25)

    #Iniciar funcionalidades
    tolerancia = 0.000001
    max_iter = 100
    txt_tolerancia.insert(0,str(tolerancia))
    txt_max_iter.insert(0,str(max_iter))
    zero_matrix =np.zeros(4)
    def calcular_clic_event(event):
        try:
            a11 = int(txt_a11.get())
            a12 = int(txt_a12.get())
            a13 = int(txt_a13.get())
            a14 = int(txt_a14.get())
            a21 = int(txt_a21.get())
            a22 = int(txt_a22.get())
            a23 = int(txt_a23.get())
            a24 = int(txt_a24.get())
            a31 = int(txt_a31.get())
            a32 = int(txt_a32.get())
            a33 = int(txt_a33.get())
            a34 = int(txt_a34.get())
            a41 = int(txt_a41.get())
            a42 = int(txt_a42.get())
            a43 = int(txt_a43.get())
            a44 = int(txt_a44.get())
            x1 = int(txt_x1.get())
            x2 = int(txt_x2.get())
            x3 = int(txt_x3.get())
            x4 = int(txt_x4.get())
            tolerancia = float(txt_tolerancia.get())
            max_iter = int(txt_max_iter.get())
            A = np.array([
                [a11, a12, a13, a14],
                [a21, a22, a23, a24],
                [a31, a32, a33, a34],
                [a41, a42, a43, a44]])
            x = np.array([x1, x2, x3, x4])
            b = gauss_seidel(A, x, zero_matrix, max_iter, tolerancia)

            lbl_b1.configure(text=str(round(b[0],7)), state="normal")
            lbl_b2.configure(text=str(round(b[1],7)), state="normal")
            lbl_b3.configure(text=str(round(b[2],7)), state="normal")
            lbl_b4.configure(text=str(round(b[3],7)), state="normal")
            return
        except ValueError as e:
            msg.showerror("Error", f"Error: {e.args[0]}")
            return

    def limpiar_clic_event(event):
        try:
            void_string = StringVar()
            void_string.set("")
            txt_a11.configure(textvariable=void_string)
            txt_a11.focus()
            txt_a12.configure(textvariable=void_string)
            txt_a13.configure(textvariable=void_string)
            txt_a14.configure(textvariable=void_string)
            txt_a21.configure(textvariable=void_string)
            txt_a22.configure(textvariable=void_string)
            txt_a23.configure(textvariable=void_string)
            txt_a24.configure(textvariable=void_string)
            txt_a31.configure(textvariable=void_string)
            txt_a32.configure(textvariable=void_string)
            txt_a33.configure(textvariable=void_string)
            txt_a34.configure(textvariable=void_string)
            txt_a41.configure(textvariable=void_string)
            txt_a42.configure(textvariable=void_string)
            txt_a43.configure(textvariable=void_string)
            txt_a44.configure(textvariable=void_string)
            txt_x1.configure(textvariable=void_string)
            txt_x2.configure(textvariable=void_string)
            txt_x3.configure(textvariable=void_string)
            txt_x4.configure(textvariable=void_string)
            lbl_b1.configure(textvariable=void_string, state="disabled")
            lbl_b2.configure(textvariable=void_string, state="disabled")
            lbl_b3.configure(textvariable=void_string, state="disabled")
            lbl_b4.configure(textvariable=void_string, state="disabled")
        except Exception as e:
            msg.showerror("Error", f"Error: {e.args[0]}")
            return
    
    btn_Calcular.bind('<Button-1>', calcular_clic_event)
    btn_Limpiar.bind('<Button-1>', limpiar_clic_event)
    window.mainloop()

    return window

def gauss_seidel(A, b, x0, max_iter, tol):
    n = len(A)
    x = x0.copy()
    for i in range(max_iter):
        x_new = np.zeros_like(x)
        for j in range(n):
            s1 = sum(-A[j][k] * x_new[k] for k in range(j))
            s2 = sum(-A[j][k] * x[k] for k in range(j+1, n))
            x_new[j] = (b[j] - s1 - s2) / A[j][j]
        if np.allclose(x, x_new, rtol=tol):
            return x_new
        x = x_new
    return x

##MAIN
main()