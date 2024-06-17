from tkinter import *
import time
import tkinter
from pygame import mixer
import BD
from tkinter import messagebox
import tkinter as tk
import sqlite3


#inicio de secion
def login():
    username = entry_username.get()
    password = entry_password.get()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    if result:
        messagebox.showinfo("Login Successful", "Welcome " + username)
        root.destroy()  # Cierra la ventana de login
        open_main_program()  # Abre el programa principal
    else:
        messagebox.showerror("Error", "Invalid Username or Password")


def register():
    register_window = tk.Toplevel(root)
    register_window.title("Register")

    tk.Label(register_window, text="Full Name").grid(row=0, column=0)
    tk.Label(register_window, text="Email").grid(row=1, column=0)
    tk.Label(register_window, text="Phone").grid(row=2, column=0)
    tk.Label(register_window, text="Username").grid(row=3, column=0)
    tk.Label(register_window, text="Password").grid(row=4, column=0)

    entry_fullname = tk.Entry(register_window)
    entry_email = tk.Entry(register_window)
    entry_phone = tk.Entry(register_window)
    entry_reg_username = tk.Entry(register_window)
    entry_reg_password = tk.Entry(register_window)

    entry_fullname.grid(row=0, column=1)
    entry_email.grid(row=1, column=1)
    entry_phone.grid(row=2, column=1)
    entry_reg_username.grid(row=3, column=1)
    entry_reg_password.grid(row=4, column=1)

    def save_user():
        fullname = entry_fullname.get()
        email = entry_email.get()
        phone = entry_phone.get()
        username = entry_reg_username.get()
        password = entry_reg_password.get()
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (fullname, email, phone, username, password) VALUES (?, ?, ?, ?, ?)",
                  (fullname, email, phone, username, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "User Registered Successfully")
        register_window.destroy()

    tk.Button(register_window, text="Register", command=save_user).grid(row=5, column=1)


def open_main_program():
    import tkinter as tk
    from pygame import mixer

    root = tk.Tk()
    root.geometry("900x500")
    root.resizable(height=False, width=False)
    root.title("Reloj")
    root.config(bg="white")
    root.iconbitmap(
        r"Fotos InterfacesGraficas\icono-de-reloj-para-sitios-web-y-aplicaciones-imagen-fondo-turquesa-ilustración-vectorial-línea-plana-eps-179972961.ico")

    # Aquí agrega tu código del archivo Reloj.py para la interfaz del reloj
    # Ejemplo:
    # def main_interface():
    #     # Código para la interfaz del reloj
    # main_interface()

    root.mainloop()


root = tk.Tk()
root.title("Login")

tk.Label(root, text="Username").grid(row=0, column=0)
tk.Label(root, text="Password").grid(row=1, column=0)

entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")

entry_username.grid(row=0, column=1)
entry_password.grid(row=1, column=1)

tk.Button(root, text="Login", command=login).grid(row=2, column=1)
tk.Button(root, text="Register", command=register).grid(row=2, column=0)

root.mainloop()


root = Tk()
root.geometry("900x500")
root.resizable(height=False, width=False)
root.title("Reloj")
root.config(bg="white")
root.iconbitmap(
    r"Fotos InterfacesGraficas\icono-de-reloj-para-sitios-web-y-aplicaciones-imagen-fondo-turquesa-ilustración-vectorial-línea-plana-eps-179972961.ico")

FrameInicio = ""
FrameAlarma = ""
FrameCrono = ""
FrameTemp = ""
FrameActual = ""
Sonar = None
CorriendoTemp = False
CorriendoCrono = False
Var = False
Var_ = False
VarEliminarAlarma = False
AlarmaGuardada = False
Terminado = False
RelojIMGLabel = ""
día = ""
Tiempo = 0
Tiempo_ = 0




# MENU

def Menu_Hamburguesa():
    global CloseIMG
    menu = Frame(root, width=300, height=500, bg="#12c4c0")
    menu.place(x=0, y=0)

    miButton = Button(menu, command=lambda: [Inicio(), menu.destroy()], text=" I N I C I O", width=42, height=2,
                      fg="white", border=0, bg="#12c4c0", activeforeground="#262626", activebackground="#0f9d9a",
                      cursor="hand2")
    miButton.place(x=0, y=80)
    miButton1 = Button(menu, command=lambda: [Alarma(), menu.destroy()], text=" A L A R M A", width=42, height=2,
                       fg="white", border=0, bg="#12c4c0", activeforeground="#262626", activebackground="#0f9d9a",
                       cursor="hand2")
    miButton1.place(x=0, y=117)
    miButton2 = Button(menu, command=lambda: [Cronometro(), menu.destroy()], text=" C R O N Ó M E T R O", width=42,
                       height=2, fg="white", border=0, bg="#12c4c0", activeforeground="#262626",
                       activebackground="#0f9d9a", cursor="hand2")
    miButton2.place(x=0, y=154)
    miButton3 = Button(menu, command=lambda: [Temporizador(), menu.destroy()], text=" T E M P O R I Z A D O R",
                       width=42, height=2, fg="white", border=0, bg="#12c4c0", activeforeground="#262626",
                       activebackground="#0f9d9a", cursor="hand2")
    miButton3.place(x=0, y=191)
    miButton4 = Button(menu, command=lambda: [pomodoro(), menu.destroy()], text=" P O M O D O R O", width=42, height=2,
                       fg="white", border=0, bg="#12c4c0", activeforeground="#262626", activebackground="#0f9d9a",
                       cursor="hand2")
    miButton4.place(x=0, y=228)


    def EncimaInicio(arg):
        miButton.config(bg="#0f9d9a")

    def FueraInicio(arg):
        miButton.config(bg="#12c4c0")

    def EncimaAlarma(arg):
        miButton1.config(bg="#0f9d9a")

    def FueraAlarma(arg):
        miButton1.config(bg="#12c4c0")

    def EncimaCrono(arg):
        miButton2.config(bg="#0f9d9a")

    def FueraCrono(arg):
        miButton2.config(bg="#12c4c0")

    def EncimaTemp(arg):
        miButton3.config(bg="#0f9d9a")

    def FueraTemp(arg):
        miButton3.config(bg="#12c4c0")

    def EncimaPomodoro(arg):
        miButton4.config(bg="#0f9d9a")

    def FueraPomodoro(arg):
        miButton4.config(bg="#12c4c0")

    miButton.bind("<Enter>", EncimaInicio)
    miButton.bind("<Leave>", FueraInicio)
    miButton1.bind("<Enter>", EncimaAlarma)
    miButton1.bind("<Leave>", FueraAlarma)
    miButton2.bind("<Enter>", EncimaCrono)
    miButton2.bind("<Leave>", FueraCrono)
    miButton3.bind("<Enter>", EncimaTemp)
    miButton3.bind("<Leave>", FueraTemp)
    miButton4.bind("<Enter>", EncimaPomodoro)
    miButton4.bind("<Leave>", FueraPomodoro)

    CloseIMG = PhotoImage(file=r"Fotos InterfacesGraficas\close.png")
    Button(menu, image=CloseIMG, border=0, command=lambda: menu.destroy(), bg="#12c4c0", activebackground="#12c4c0",
           cursor="hand2").place(x=5, y=10)



# INICIO
def Inicio():
    global FrameInicio, Var
    try:
        if not AlarmaGuardada:
            FrameAlarma.destroy()
    except AttributeError:
        pass
    try:
        if not CorriendoCrono:
            FrameCrono.destroy()
    except AttributeError:
        pass
    try:
        FrameInicio.destroy()
    except AttributeError:
        pass
    try:
        if not CorriendoTemp:
            FrameTemp.destroy()
    except AttributeError:
        pass

    HoraInicio = ""
    FrameInicio = Frame(root, bg="white", height=500, width=800)
    FrameInicio.place(x=100, y=0)
    LugarLabel = Label(FrameInicio, text="Perú, Huancayo", fg="#12c4c0", font=("Helvetica", 10, "bold"),
                       bg="white")
    LugarLabel.place(x=273, y=0)
    HoraLabelInicio = Label(FrameInicio, text=HoraInicio, font=("Helvetica", 70, "bold"), bg="white", fg="#12c4c0")
    HoraLabelInicio.place(x=93, y=150)

    def HoraActualInicio():
        HoraInicio = time.strftime("%I:%M:%S %p")
        if HoraInicio.startswith("0"):
            HoraInicio = HoraInicio.removeprefix("0")
        HoraLabelInicio.config(text=HoraInicio)
        HoraLabelInicio.after(100, HoraActualInicio)

    HoraActualInicio()


Inicio()


# CRONOMETRO
def Cronometro():
    global PlayIMG, PausaIMG, ReinicioIMG, BotonPausaPlayCron, BotonReiniciarCron, Var, ImagenCrono
    global FrameCrono, CronoLabel, PausaCrono, ReinicioCrono, CronoTexto, CorriendoCrono
    try:
        if not AlarmaGuardada:
            FrameAlarma.destroy()
    except AttributeError:
        pass
    try:
        if not CorriendoCrono:
            FrameCrono.destroy()
    except AttributeError:
        pass
    try:
        FrameInicio.destroy()
    except AttributeError:
        pass
    try:
        if not CorriendoTemp:
            FrameTemp.destroy()
    except AttributeError:
        pass

    PlayIMG = PhotoImage(file=r"Fotos InterfacesGraficas\BotonPlay.png")
    PausaIMG = PhotoImage(file=r"Fotos InterfacesGraficas\BotonPausar.png")
    ReinicioIMG = PhotoImage(file=r"Fotos InterfacesGraficas\ReiniciarBoton.png")

    if not CorriendoCrono:
        FrameCrono = Frame(root, bg="white", height=500, width=800)
        FrameCrono.place(x=100, y=0)
        FrameCrono.pack_propagate(False)
        CronoTexto = "00:00:00,00"
        CronoLabel = Label(FrameCrono, text=CronoTexto, font=("Helvetica", 70), bg="white")
        CronoLabel.place(y=100, x=100)
        BotonPausaPlayCron = Button(FrameCrono, command=PlayCrono, image=PlayIMG, border=0, bg="white",
                                    activebackground="white", cursor="hand2")
        BotonPausaPlayCron.place(x=287, y=250)
        BotonReiniciarCron = Button(FrameCrono, command=ReiniciarCrono, image=ReinicioIMG, border=0, bg="white",
                                    activebackground="white", cursor="hand2")
        BotonReiniciarCron.place(x=353, y=251)
        ImagenCrono = "Play"
        PausaCrono = False
        ReinicioCrono = False
    else:
        FrameCrono.place(x=100, y=0)
        if ImagenCrono == "Pausa":
            BotonPausaPlayCron.config(command=PausarCrono, image=PausaIMG)
        else:
            BotonPausaPlayCron.config(command=PlayCrono, image=PlayIMG)
        BotonPausaPlayCron.place(x=287, y=250)
        BotonReiniciarCron.config(image=ReinicioIMG)
        BotonReiniciarCron.place(x=353, y=251)
        FrameCrono.lift()


def ReiniciarCrono():
    global ReinicioCrono, CronoLabel, CronoTexto, BotonPausaPlayCron, Var
    ReinicioCrono = True
    Var = False
    CronoTexto = "00:00:00,00"
    CronoLabel.config(text=CronoTexto)
    BotonPausaPlaycommand = BotonPausaPlayCron["command"]
    BotonPausaPlaycommand = str(BotonPausaPlaycommand)
    BotonPausaPlaycommand = "".join([i for i in BotonPausaPlaycommand if not i.isdigit()])
    if BotonPausaPlaycommand == "PlayCrono":
        ReinicioCrono = False


def PausarCrono():
    global PlayIMG, PausaCrono
    BotonPausaPlayCron.config(image=PlayIMG, command=PlayCrono)
    PausaCrono = True


def PlayCrono():
    global CronoLabel, PausaIMG, PausaCrono, ReinicioCrono, Tiempo, Var, Var_, Tiempo_, ImagenCrono, CorriendoCrono
    if not ReinicioCrono:
        if not PausaCrono:
            CorriendoCrono = True
            if Var_:
                difTiempos = time.time() - Tiempo_
                Tiempo = Tiempo + difTiempos
                Var_ = False
            if not Var:
                Tiempo = time.time()
                Var = True

            def FuncPLayCrono():
                global Tiempo
                ResTiempo = time.time() - Tiempo
                Horas = int(ResTiempo / 3600)
                Minutos = int(ResTiempo / 60 - Horas * 60)
                Segundos = int(ResTiempo - Horas * 3600 - Minutos * 60)
                Milisegundos = int((ResTiempo - Horas * 3600 - Minutos * 60 - Segundos) * 100)
                Horas = str(Horas)
                Minutos = str(Minutos)
                Segundos = str(Segundos)
                Milisegundos = str(Milisegundos)
                if len(Horas) == 1:
                    Horas = "0" + Horas
                if len(Minutos) == 1:
                    Minutos = "0" + Minutos
                if len(Segundos) == 1:
                    Segundos = "0" + Segundos
                if len(Milisegundos) == 1:
                    Milisegundos = "0" + Milisegundos
                CronoTexto = f"{Horas}:{Minutos}:{Segundos},{Milisegundos}"
                CronoLabel.config(text=CronoTexto)

            FuncPLayCrono()
            CronoLabel.after(1, PlayCrono)

            if ImagenCrono == "Play":
                BotonPausaPlayCron.config(image=PausaIMG, command=PausarCrono)
                ImagenCrono = "Pausa"
        else:
            CronoLabel.after_cancel(CronoLabel)
            Tiempo_ = time.time()
            ImagenCrono = "Play"
            Var_ = True
            PausaCrono = False
    else:
        CronoLabel.after_cancel(CronoLabel)
        BotonPausaPlayCron.config(image=PlayIMG, command=PlayCrono)
        ImagenCrono = "Play"
        CorriendoCrono = False
        ReinicioCrono = False


# ALARMA
def Alarma():
    global ArribaIMG, FrameAlarma, CrearAlarmaButton, AgregarIMG, RelojIMG, AbajoIMG, día, LabelAlarma, RelojIMGLabel, Var
    ArribaIMG = PhotoImage(file=r"Fotos InterfacesGraficas\Arriba.png")
    AgregarIMG = PhotoImage(file=r"Fotos InterfacesGraficas\Agregar.png")
    RelojIMG = PhotoImage(file=r"Fotos InterfacesGraficas\Reloj.png")
    AbajoIMG = PhotoImage(file=r"Fotos InterfacesGraficas\Abajo.png")
    try:
        if not AlarmaGuardada:
            FrameAlarma.destroy()
    except AttributeError:
        pass
    try:
        if not CorriendoCrono:
            FrameCrono.destroy()
    except AttributeError:
        pass
    try:
        FrameInicio.destroy()
    except AttributeError:
        pass
    try:
        if not CorriendoTemp:
            FrameTemp.destroy()
    except AttributeError:
        pass

    if not AlarmaGuardada:
        FrameAlarma = Frame(root, bg="white", height=500, width=800)
        FrameAlarma.place(x=100, y=0)
        FrameAlarma.pack_propagate(False)

        CrearAlarmaButton = Button(FrameAlarma, image=AgregarIMG, command=CrearAlarma, border=0, bg="white",
                                   activebackground="white", cursor="hand2")
        CrearAlarmaButton.place(x=700, y=420)

        RelojIMGLabel = Label(FrameAlarma, image=RelojIMG, bg="white")
        RelojIMGLabel.place(x=284, y=25)

        LabelAlarma = Label(FrameAlarma, text="No tienes ninguna alarma.", font=("Helvetica", 20), bg="white",
                            fg="#12c4c0")
        LabelAlarma.place(x=185, y=175)
    else:
        FrameAlarma.place(x=100, y=0)
        RelojIMGLabel.config(image=RelojIMG)
        RelojIMGLabel.place(x=284, y=225)
        try:
            EliminarAlarmaButton.config(image=CerrarIMG)
            EliminarAlarmaButton.place(x=730, y=10)
        except tkinter.TclError:
            pass
        FrameAlarma.lift()


def CrearAlarma():
    global FrameAlarma, CrearAlarmaButton, FrameCrearAlarma, HoraLabelAlarma, MinutosLabelAlarma, AMPMLabelAlarma, HoraVar, MinutosVar, AMPMVar
    FrameCrearAlarma = Frame(FrameAlarma, width=500, height=300, bg="white", highlightbackground="grey",
                             highlightthickness=3)
    FrameCrearAlarma.place(x=105, y=20)
    HoraVar = time.strftime("%I" + " :")
    MinutosVar = time.strftime("%M")
    AMPMVar = time.strftime("%p")
    HoraLabelAlarma = Label(FrameCrearAlarma, text=HoraVar, font=("Helvetica", 50), bg="white")
    HoraLabelAlarma.place(x=60, y=50)
    MinutosLabelAlarma = Label(FrameCrearAlarma, text=MinutosVar, font=("Helvetica", 50), bg="white")
    MinutosLabelAlarma.place(x=200, y=50)
    AMPMLabelAlarma = Label(FrameCrearAlarma, text=AMPMVar, font=("Helvetica", 50), bg="white")
    AMPMLabelAlarma.place(x=330, y=50)
    CrearAlarmaButton.config(state="disabled")
    Button(FrameCrearAlarma, command=lambda: AlarmaArriba("HoraVar"), image=ArribaIMG, bg="white",
           activebackground="white", border=0).place(x=80, y=20)
    Button(FrameCrearAlarma, command=lambda: AlarmaArriba("MinutosVar"), image=ArribaIMG, bg="white",
           activebackground="white", border=0).place(x=220, y=20)
    Button(FrameCrearAlarma, command=lambda: AlarmaArriba("AMPMVar"), image=ArribaIMG, bg="white",
           activebackground="white", border=0).place(x=360, y=20)
    Button(FrameCrearAlarma, command=lambda: AlarmaAbajo("HoraVar"), image=AbajoIMG, bg="white",
           activebackground="white", border=0).place(x=80, y=120)
    Button(FrameCrearAlarma, command=lambda: AlarmaAbajo("MinutosVar"), image=AbajoIMG, bg="white",
           activebackground="white", border=0).place(x=220, y=120)
    Button(FrameCrearAlarma, command=lambda: AlarmaAbajo("AMPMVar"), image=AbajoIMG, bg="white",
           activebackground="white", border=0).place(x=360, y=120)
    Guardar = Button(FrameCrearAlarma, command=GuardarAlarma, text="Guardar", font=("Helvetica", 20), justify="center",
                     bg="#12c4c0", fg="white", border=0, cursor="hand2")
    Guardar.place(x=50, y=230)
    Cancelar = Button(FrameCrearAlarma,
                      command=lambda: [FrameCrearAlarma.destroy(), CrearAlarmaButton.config(state="normal")],
                      text="Cancelar", font=("Helvetica", 20), justify="center", fg="#12c4c0", border=0, cursor="hand2")
    Cancelar.place(x=310, y=230)
    Guardar.config(state="disabled")
    Lunes = Button(FrameCrearAlarma, command=lambda: Días("Lunes"), text="L", font=("Helvetica", 15), bg="white",
                   border=0)
    Lunes.place(x=55, y=180)
    Martes = Button(FrameCrearAlarma, command=lambda: Días("Martes"), text="M", font=("Helvetica", 15), bg="white",
                    border=0)
    Martes.place(x=115, y=180)
    Miercoles = Button(FrameCrearAlarma, command=lambda: Días("Miercoles"), text="X", font=("Helvetica", 15),
                       bg="white", border=0)
    Miercoles.place(x=175, y=180)
    Jueves = Button(FrameCrearAlarma, command=lambda: Días("Jueves"), text="J", font=("Helvetica", 15), bg="white",
                    border=0)
    Jueves.place(x=235, y=180)
    Viernes = Button(FrameCrearAlarma, command=lambda: Días("Viernes"), text="V", font=("Helvetica", 15), bg="white",
                     border=0)
    Viernes.place(x=295, y=180)
    Sabado = Button(FrameCrearAlarma, command=lambda: Días("Sabado"), text="S", font=("Helvetica", 15), bg="white",
                    border=0)
    Sabado.place(x=355, y=180)
    Domingo = Button(FrameCrearAlarma, command=lambda: Días("Domingo"), text="D", font=("Helvetica", 15), bg="white",
                     border=0)
    Domingo.place(x=415, y=180)

    def Días(DíaArg):
        global día, díaEsp
        if DíaArg == "Lunes":
            Lunes.config(fg="#12c4c0")
            Martes.config(fg="black")
            Miercoles.config(fg="black")
            Jueves.config(fg="black")
            Viernes.config(fg="black")
            Sabado.config(fg="black")
            Domingo.config(fg="black")
            día = "1"
            díaEsp = "Lunes"
        elif DíaArg == "Martes":
            Lunes.config(fg="black")
            Martes.config(fg="#12c4c0")
            Miercoles.config(fg="black")
            Jueves.config(fg="black")
            Viernes.config(fg="black")
            Sabado.config(fg="black")
            Domingo.config(fg="black")
            día = "2"
            díaEsp = "Martes"
        elif DíaArg == "Miercoles":
            Lunes.config(fg="black")
            Martes.config(fg="black")
            Miercoles.config(fg="#12c4c0")
            Jueves.config(fg="black")
            Viernes.config(fg="black")
            Sabado.config(fg="black")
            Domingo.config(fg="black")
            día = "3"
            díaEsp = "Miércoles"
        elif DíaArg == "Jueves":
            Lunes.config(fg="black")
            Martes.config(fg="black")
            Miercoles.config(fg="black")
            Jueves.config(fg="#12c4c0")
            Viernes.config(fg="black")
            Sabado.config(fg="black")
            Domingo.config(fg="black")
            día = "4"
            díaEsp = "Jueves"
        elif DíaArg == "Viernes":
            Lunes.config(fg="black")
            Martes.config(fg="black")
            Miercoles.config(fg="black")
            Jueves.config(fg="black")
            Viernes.config(fg="#12c4c0")
            Sabado.config(fg="black")
            Domingo.config(fg="black")
            día = "5"
            díaEsp = "Viernes"
        elif DíaArg == "Sabado":
            Lunes.config(fg="black")
            Martes.config(fg="black")
            Miercoles.config(fg="black")
            Jueves.config(fg="black")
            Viernes.config(fg="black")
            Sabado.config(fg="#12c4c0")
            Domingo.config(fg="black")
            día = "6"
            díaEsp = "Sábado"
        elif DíaArg == "Domingo":
            Lunes.config(fg="black")
            Martes.config(fg="black")
            Miercoles.config(fg="black")
            Jueves.config(fg="black")
            Viernes.config(fg="black")
            Sabado.config(fg="black")
            Domingo.config(fg="#12c4c0")
            día = "0"
            díaEsp = "Domingo"
        Guardar.config(state="normal")


def AlarmaArriba(Var):
    global HoraVar, MinutosVar, AMPMVar
    if Var == "HoraVar":
        HoraVar = HoraVar.replace(":", "")
        HoraVar = int(HoraVar)
        if HoraVar == 12:
            HoraVar = 0
        HoraVar += 1
        HoraVar = str(HoraVar)
        if len(HoraVar) == 1:
            HoraVar = "0" + HoraVar
        HoraVar = HoraVar + " :"
        HoraLabelAlarma.config(text=HoraVar)
    elif Var == "MinutosVar":
        MinutosVar = int(MinutosVar)
        if MinutosVar == 59:
            MinutosVar = 0
        else:
            MinutosVar += 1
        MinutosVar = str(MinutosVar)
        if len(MinutosVar) == 1:
            MinutosVar = "0" + MinutosVar
        MinutosLabelAlarma.config(text=MinutosVar)
    elif Var == "AMPMVar":
        if AMPMVar == "PM":
            AMPMLabelAlarma.config(text="AM")
            AMPMVar = "AM"
        else:
            AMPMLabelAlarma.config(text="PM")
            AMPMVar = "PM"
    HoraVar = HoraVar.replace(":", "")
    HoraVar = HoraVar.replace(" ", "")


def AlarmaAbajo(Var):
    global HoraVar, MinutosVar, AMPMVar
    if Var == "HoraVar":
        HoraVar = HoraVar.replace(":", "")
        HoraVar = int(HoraVar)
        if HoraVar == 1:
            HoraVar = 12
        else:
            HoraVar -= 1
        HoraVar = str(HoraVar)
        if len(HoraVar) == 1:
            HoraVar = "0" + HoraVar
        HoraVar = HoraVar + " :"
        HoraLabelAlarma.config(text=HoraVar)
    elif Var == "MinutosVar":
        MinutosVar = int(MinutosVar)
        if MinutosVar == 0:
            MinutosVar = 59
        else:
            MinutosVar -= 1
        MinutosVar = str(MinutosVar)
        if len(MinutosVar) == 1:
            MinutosVar = "0" + MinutosVar
        MinutosLabelAlarma.config(text=MinutosVar)
    elif Var == "AMPMVar":
        if AMPMVar == "PM":
            AMPMLabelAlarma.config(text="AM")
            AMPMVar = "AM"
        else:
            AMPMLabelAlarma.config(text="PM")
            AMPMVar = "PM"
    HoraVar = HoraVar.replace(":", "")
    HoraVar = HoraVar.replace(" ", "")


def GuardarAlarma():
    global HoraVar, MinutosVar, AMPMVar, díaEsp, día, ProximaFecha, FechaDía
    global LabelAlarma, AlarmaMomentoSonar, AlarmaGuardada, CerrarIMG, EliminarAlarmaButton
    AlarmaGuardada = True
    CerrarIMG = PhotoImage(file=r"Fotos InterfacesGraficas\Cerrar.png")

    def EliminarAlarma():
        global AlarmaGuardada, VarEliminarAlarma
        AlarmaGuardada = False
        VarEliminarAlarma = True
        Alarma()

    EliminarAlarmaButton = Button(FrameAlarma, command=EliminarAlarma, image=CerrarIMG, border=0, bg="white",
                                  cursor="hand2", activebackground="white")
    EliminarAlarmaButton.place(x=730, y=10)
    FrameCrearAlarma.destroy()
    CrearAlarmaButton.place_forget()
    RelojIMGLabel.place(x=284, y=225)
    LabelAlarma = Label(FrameAlarma, text="Tu alarma sonará\n muy pronto...", font=("Helvetica", 50, "bold"),
                        bg="white", fg="#12c4c0")
    LabelAlarma.place(x=80, y=50)
    AlarmaMomentoSonar = Label(FrameAlarma, font=("Helvetica", 15), bg="white", fg="grey")
    AlarmaMomentoSonar.place(x=130, y=325)
    HoraVar = HoraVar.replace(":", "")
    HoraVar = HoraVar.replace(" ", "")
    FechaDía = int(time.strftime("%d")) + int(día) - int(time.strftime("%w"))
    if FechaDía <= 0:
        FechaDía += 7
    MarcaExcedida = False
    MarcaExcedida_ = False
    MesProximaFecha = time.strftime("%b") + "."
    MesFecha = time.strftime("%b") + "."
    if MesFecha == "Jan.":
        MesFecha = "Ene."
    elif MesFecha == "Apr.":
        MesProximaFecha = "Abr."
    elif MesFecha == "Aug.":
        MesFecha = "Agt."
    if MesProximaFecha == "Jan.":
        MesProximaFecha = "Ene."
    elif MesProximaFecha == "Apr.":
        MesProximaFecha = "Abr."
    elif MesProximaFecha == "Aug.":
        MesProximaFecha = "Agt."
    if time.strftime("%b") == "Jan":
        ProximaFecha = int(time.strftime("%d")) + 7
        if ProximaFecha > 31:
            MarcaExcedida = True
            ProximaFecha = ProximaFecha - 31
        if FechaDía > 31:
            MarcaExcedida_ = True
            FechaDía = FechaDía - 31
    elif time.strftime("%b") == "Feb":
        ProximaFecha = int(time.strftime("%d")) + 7
        if ProximaFecha > 28:
            MarcaExcedida = True
            ProximaFecha = ProximaFecha - 28
        if FechaDía > 28:
            MarcaExcedida_ = True
            FechaDía = FechaDía - 28
    elif time.strftime("%b") == "Mar":
        ProximaFecha = int(time.strftime("%d")) + 7
        if ProximaFecha > 31:
            MarcaExcedida = True
            ProximaFecha = ProximaFecha - 31
        if FechaDía > 31:
            MarcaExcedida_ = True
            FechaDía = FechaDía - 31
    elif time.strftime("%b") == "Apr":
        ProximaFecha = int(time.strftime("%d")) + 7
        if ProximaFecha > 30:
            MarcaExcedida = True
            ProximaFecha = ProximaFecha - 30
        if FechaDía > 30:
            MarcaExcedida_ = True
            FechaDía = FechaDía - 30
    elif time.strftime("%b") == "May":
        ProximaFecha = int(time.strftime("%d")) + 7
        if ProximaFecha > 31:
            MarcaExcedida = True
            ProximaFecha = ProximaFecha - 31
        if FechaDía > 31:
            MarcaExcedida_ = True
            FechaDía = FechaDía - 31
    elif time.strftime("%b") == "Jun":
        ProximaFecha = int(time.strftime("%d")) + 7
        if ProximaFecha > 30:
            MarcaExcedida = True
            ProximaFecha = ProximaFecha - 30
        if FechaDía > 30:
            MarcaExcedida_ = True
            FechaDía = FechaDía - 30
    elif time.strftime("%b") == "Jul":
        ProximaFecha = int(time.strftime("%d")) + 7
        if ProximaFecha > 31:
            MarcaExcedida = True
            ProximaFecha = ProximaFecha - 31
        if FechaDía > 31:
            MarcaExcedida_ = True
            FechaDía = FechaDía - 31
    elif time.strftime("%b") == "Aug":
        ProximaFecha = int(time.strftime("%d")) + 7
        if ProximaFecha > 31:
            MarcaExcedida = True
            ProximaFecha = ProximaFecha - 31
        if FechaDía > 31:
            MarcaExcedida_ = True
            FechaDía = FechaDía - 31
    elif time.strftime("%b") == "Sep":
        ProximaFecha = int(time.strftime("%d")) + 7
        if ProximaFecha > 30:
            MarcaExcedida = True
            ProximaFecha = ProximaFecha - 30
        if FechaDía > 30:
            MarcaExcedida_ = True
            FechaDía = FechaDía - 30
    elif time.strftime("%b") == "Oct":
        ProximaFecha = int(time.strftime("%d")) + 7
        if ProximaFecha > 31:
            MarcaExcedida = True
            ProximaFecha = ProximaFecha - 31
        if FechaDía > 31:
            MarcaExcedida_ = True
            FechaDía = FechaDía - 31
    elif time.strftime("%b") == "Nov":
        ProximaFecha = int(time.strftime("%d")) + 7
        if ProximaFecha > 30:
            MarcaExcedida = True
            ProximaFecha = ProximaFecha - 30
        if FechaDía > 30:
            MarcaExcedida_ = True
            FechaDía = FechaDía - 30
    elif time.strftime("%b") == "Dec":
        ProximaFecha = int(time.strftime("%d")) + 7
        if ProximaFecha > 31:
            MarcaExcedida = True
            ProximaFecha = ProximaFecha - 31
        if FechaDía > 31:
            MarcaExcedida_ = True
            FechaDía = FechaDía - 31
    if MarcaExcedida:
        if MesProximaFecha == "Ene.":
            MesProximaFecha = "Feb."
        elif MesProximaFecha == "Feb.":
            MesProximaFecha = "Mar."
        elif MesProximaFecha == "Mar.":
            MesProximaFecha = "Abr."
        elif MesProximaFecha == "Abr.":
            MesProximaFecha = "May."
        elif MesProximaFecha == "May.":
            MesProximaFecha = "Jun."
        elif MesProximaFecha == "Jun.":
            MesProximaFecha = "Jul."
        elif MesProximaFecha == "Jul.":
            MesProximaFecha = "Agt."
        elif MesProximaFecha == "Agt.":
            MesProximaFecha = "Sep."
        elif MesProximaFecha == "Sep.":
            MesProximaFecha = "Oct."
        elif MesProximaFecha == "Oct.":
            MesProximaFecha = "Nov."
        elif MesProximaFecha == "Nov.":
            MesProximaFecha = "Dec."
        elif MesProximaFecha == "Dec.":
            MesProximaFecha = "Ene."
    if MarcaExcedida_:
        if MesFecha == "Ene.":
            MesFecha = "Feb."
        elif MesFecha == "Feb.":
            MesFecha = "Mar."
        elif MesFecha == "Mar.":
            MesFecha = "Abr."
        elif MesFecha == "Abr.":
            MesFecha = "May."
        elif MesFecha == "May.":
            MesFecha = "Jun."
        elif MesFecha == "Jun.":
            MesFecha = "Jul."
        elif MesFecha == "Jul.":
            MesFecha = "Agt."
        elif MesFecha == "Agt.":
            MesFecha = "Sep."
        elif MesFecha == "Sep.":
            MesFecha = "Oct."
        elif MesFecha == "Oct.":
            MesFecha = "Nov."
        elif MesFecha == "Nov.":
            MesFecha = "Dec."
        elif MesFecha == "Dec.":
            MesFecha = "Ene."

    if ((time.strftime("%w") == día and
         time.strftime("%I") == HoraVar and
         time.strftime("%M") == MinutosVar and
         time.strftime("%p") == AMPMVar)
            or (
                    time.strftime("%w") == día and
                    int(time.strftime("%I")) > int(HoraVar) and
                    time.strftime("%p") == AMPMVar)
            or (
                    int(time.strftime("%I")) == int(HoraVar) and
                    int(time.strftime("%M")) > int(MinutosVar) and
                    time.strftime("%w") == día and
                    time.strftime("%p") == AMPMVar
                    or (
                            int(time.strftime("%w")) == int(día) and
                            time.strftime("%p") == "PM" and
                            AMPMVar == "AM"))
            or (
                    int(time.strftime("%w")) == int(día) and
                    int(time.strftime("%I")) < 12 and
                    time.strftime("%p") == "PM" and
                    int(HoraVar) == 12 and
                    AMPMVar == "PM")):
        AlarmaMomentoSonar.config(
            text=f"Alarma programada para {díaEsp} {ProximaFecha} {MesProximaFecha} a las {HoraVar}:{MinutosVar} {AMPMVar}")
        AlarmaMomentoSonar.place(x=100, y=325)
        AlarmaSonar(1)
    else:
        if ((time.strftime("%w") == día and
             int(HoraVar) > int(time.strftime("%I")))
                or (
                        time.strftime("%w") == día and
                        time.strftime("%I") == HoraVar and
                        int(MinutosVar) > int(time.strftime("%M")))
                or (
                        time.strftime("%w") == día and
                        time.strftime("%p") == "AM" and
                        AMPMVar == "PM")):
            AlarmaMomentoSonar.config(text=f"Alarma programada para Hoy a las {HoraVar}:{MinutosVar} {AMPMVar}")
            AlarmaMomentoSonar.place(x=145, y=325)
            AlarmaSonar(2)
        else:
            AlarmaMomentoSonar.config(
                text=f"Alarma programada para el {díaEsp} {FechaDía} {MesFecha} a las {HoraVar}:{MinutosVar} {AMPMVar}")
            AlarmaMomentoSonar.place(x=100, y=325)
            AlarmaSonar(3)

        if (int(día) == int(time.strftime("%w")) + 1
                or (
                        int(día) == 0 and
                        int(time.strftime("%w")) == 6)):
            AlarmaMomentoSonar.config(text=f"Alarma programada para Mañana a las {HoraVar}:{MinutosVar} {AMPMVar}")
            AlarmaMomentoSonar.place(x=130, y=325)
            AlarmaSonar(4)

    if (int(time.strftime("%w")) > int(día)
            or (
                    int(día) == 0 and not
            int(time.strftime("%w")) == 6) and not
            int(time.strftime("%w")) == 0):
        ProximaFecha = ProximaFecha - (int(time.strftime("%w")) - int(día))
        AlarmaMomentoSonar.config(
            text=f"Alarma programada para {díaEsp} {ProximaFecha} {MesProximaFecha} a las {HoraVar}:{MinutosVar} {AMPMVar}")
        AlarmaMomentoSonar.place(x=100, y=325)
        AlarmaSonar(5)


def AlarmaSonar(arg):
    global HoraVar, MinutosVar, AMPMVar, día, ProximaFecha, LabelAlarma, AlarmaGuardada
    global FrameAlarmaSonando, RelojImage, VarEliminarAlarma, EliminarAlarmaButton
    Sonar = False
    if not VarEliminarAlarma:
        if arg == 1:
            if (int(time.strftime("%d")) == ProximaFecha and
                    time.strftime("%I") == HoraVar and
                    time.strftime("%M") == MinutosVar and
                    time.strftime("%p") == AMPMVar):
                mixer.init()
                mixer.music.load(r"Fotos InterfacesGraficas\Ringtones.mp3")
                mixer.music.play()
                Sonar = True
            if not Sonar:
                FrameAlarma.after(10, lambda: AlarmaSonar(1))
        if arg == 2:
            if (time.strftime("%w") == día and
                    time.strftime("%I") == HoraVar and
                    time.strftime("%M") == MinutosVar and
                    time.strftime("%p") == AMPMVar):
                mixer.init()
                mixer.music.load(r"Fotos InterfacesGraficas\Ringtones.mp3")
                mixer.music.play()
                Sonar = True
            if not Sonar:
                FrameAlarma.after(10, lambda: AlarmaSonar(2))
        if arg == 3:
            if (int(time.strftime("%d")) == FechaDía and
                    time.strftime("%I") == HoraVar and
                    time.strftime("%M") == MinutosVar and
                    time.strftime("%p") == AMPMVar):
                mixer.init()
                mixer.music.load(r"Fotos InterfacesGraficas\Ringtones.mp3")
                mixer.music.play()
                Sonar = True
            if not Sonar:
                FrameAlarma.after(10, lambda: AlarmaSonar(3))
        if arg == 4:
            if (int(time.strftime("%d")) + int(día) - int(time.strftime("%w")) == int(time.strftime("%d")) and
                    time.strftime("%I") == HoraVar and
                    time.strftime("%M") == MinutosVar and
                    time.strftime("%p") == AMPMVar):
                mixer.init()
                mixer.music.load(r"Fotos InterfacesGraficas\Ringtones.mp3")
                mixer.music.play()
                Sonar = True
            if not Sonar:
                FrameAlarma.after(10, lambda: AlarmaSonar(4))
        if arg == 5:
            if (int(time.strftime("%d")) == ProximaFecha and
                    time.strftime("%I") == HoraVar and
                    time.strftime("%M") == MinutosVar and
                    time.strftime("%p") == AMPMVar):
                mixer.init()
                mixer.music.load(r"Fotos InterfacesGraficas\Ringtones.mp3")
                mixer.music.play()
                Sonar = True
            if not Sonar:
                FrameAlarma.after(10, lambda: AlarmaSonar(5))
        if Sonar:
            RelojImage = PhotoImage(file=r"Fotos InterfacesGraficas\Reloj.png")
            FrameAlarmaSonando = Frame(FrameAlarma, width=400, height=300, bg="white", highlightbackground="grey",
                                       highlightthickness=3)
            FrameAlarmaSonando.place(x=150, y=20)
            FrameAlarmaSonando.pack_propagate(False)
            Label(FrameAlarmaSonando, text="Ring\nRing!!!", font=("Helvetica", 40, "bold"), bg="white",
                  fg="#12c4c0").pack()
            Label(FrameAlarmaSonando, image=RelojImage, bg="white").pack()
            Button(FrameAlarmaSonando, text="C A N C E L A R", font=("Helvetica", 15, "bold"), bg="#12c4c0", fg="white",
                   border=0, cursor="hand2",
                   width=31, command=CancelarAlarma).place(x=8, y=250)
            LabelAlarma.destroy()
            EliminarAlarmaButton.destroy()
    else:
        VarEliminarAlarma = False


def CancelarAlarma():
    global AlarmaGuardada
    mixer.music.stop()
    AlarmaGuardada = False
    Alarma()
    FrameAlarmaSonando.destroy()
    AlarmaMomentoSonar.destroy()
    RelojIMGLabel.place(x=284, y=25)


# TEMPORIZADOR
def Temporizador():
    global FrameTemp, Var, ArribaIMG, AbajoIMG, HorasTemp, PausaTemp, MilisegundosTemp
    global SegundosTemp, TempLabel, MinutosTemp, IniciarBoton, PlayIMG, ReinicioIMG, Terminado
    global CorriendoTemp, PausaIMG, CerrarIMG, ImagenTemp, ReinicioTemp
    try:
        if not AlarmaGuardada:
            FrameAlarma.destroy()
    except AttributeError:
        pass
    try:
        if not CorriendoCrono:
            FrameCrono.destroy()
    except AttributeError:
        pass
    try:
        FrameInicio.destroy()
    except AttributeError:
        pass
    try:
        if not CorriendoTemp:
            FrameTemp.destroy()
    except AttributeError:
        pass

    ArribaIMG = PhotoImage(file=r"Fotos InterfacesGraficas\Arriba.png")
    AbajoIMG = PhotoImage(file=r"Fotos InterfacesGraficas\Abajo.png")
    PlayIMG = PhotoImage(file=r"Fotos InterfacesGraficas\BotonPlay.png")
    PausaIMG = PhotoImage(file=r"Fotos InterfacesGraficas\BotonPausar.png")
    ReinicioIMG = PhotoImage(file=r"Fotos InterfacesGraficas\ReiniciarBoton.png")
    CerrarIMG = PhotoImage(file=r"Fotos InterfacesGraficas\Cerrar.png")

    if not CorriendoTemp:
        FrameTemp = Frame(root, bg="white", height=500, width=800)
        FrameTemp.place(x=100, y=0)
        FrameTemp.pack_propagate(False)
        HorasTemp = "00"
        MinutosTemp = "00"
        SegundosTemp = "00"
        MilisegundosTemp = "00"
        TempLabel = Label(FrameTemp, text="00:00:00", font=("Helvetica", 100), bg="white")
        TempLabel.place(x=90, y=100)

        Label(FrameTemp, text="Horas" + " " * 20 + "Minutos" + " " * 18 + "Segundos", font=("Helvetica", 15),
              fg="#12c4c0", bg="white").place(x=140, y=10)
        Button(FrameTemp, command=lambda: TempArriba("HorasTemp"), image=ArribaIMG, bg="white",
               activebackground="white", border=0).place(x=148, y=75)
        Button(FrameTemp, command=lambda: TempArriba("MinutosTemp"), image=ArribaIMG, bg="white",
               activebackground="white", border=0).place(x=332, y=75)
        Button(FrameTemp, command=lambda: TempArriba("SegundosTemp"), image=ArribaIMG, bg="white",
               activebackground="white", border=0).place(x=516, y=75)
        Button(FrameTemp, command=lambda: TempAbajo("HorasTemp"), image=AbajoIMG, bg="white", activebackground="white",
               border=0).place(x=148, y=240)
        Button(FrameTemp, command=lambda: TempAbajo("MinutosTemp"), image=AbajoIMG, bg="white",
               activebackground="white", border=0).place(x=332, y=240)
        Button(FrameTemp, command=lambda: TempAbajo("SegundosTemp"), image=AbajoIMG, bg="white",
               activebackground="white", border=0).place(x=516, y=240)
        IniciarBoton = Button(FrameTemp, command=PlayTemp, font=("Helvetica", 20, "bold"), text="Iniciar",
                              justify="center", fg="white", bg="#12c4c0", border=0, cursor="hand2", width=20,
                              state="disabled")
        IniciarBoton.place(x=180, y=350)
        PausaTemp = False
        ReinicioTemp = False
    else:
        FrameTemp.place(x=100, y=0)
        try:
            EliminarTempButton.config(image=CerrarIMG)
            EliminarTempButton.place(x=730, y=10)
            if ImagenTemp == "Pausa":
                BotonPausaPlayTemp.config(image=PausaIMG)
            else:
                BotonPausaPlayTemp.config(image=PlayIMG)
            BotonReiniciarTemp.config(image=ReinicioIMG)
            BotonReiniciarTemp.place(x=360, y=275)
            BotonPausaPlayTemp.place(x=290, y=275)
        except tkinter.TclError:
            pass
        FrameTemp.lift()


def PausarTemp():
    global PausaTemp
    PausaTemp = True


def ReiniciarTemp():
    global ReinicioTemp, ReinicioHoras, ReinicioMinutos, ReinicioSegundos, HorasTemp, MinutosTemp, SegundosTemp, MilisegundosTemp
    ReinicioTemp = True
    HorasTemp = True
    HorasTemp = ReinicioHoras
    MinutosTemp = ReinicioMinutos
    SegundosTemp = ReinicioSegundos
    MilisegundosTemp = 0
    TempLabel.config(text=f"{HorasTemp}:{MinutosTemp}:{SegundosTemp}")
    BotonPausaPlaycommand = BotonPausaPlayTemp["command"]
    BotonPausaPlaycommand = str(BotonPausaPlaycommand)
    BotonPausaPlaycommand = "".join([i for i in BotonPausaPlaycommand if not i.isdigit()]) 
    if BotonPausaPlaycommand == "PlayTemp":
        ReinicioTemp = False

def PlayTemp():
    global FrameTemp,SegundosTemp,MinutosTemp,BotonPausaPlayTemp,ImagenTemp,ReinicioTemp,Terminado,RelojImage
    global HorasTemp,PausaTemp,CorriendoTemp,EliminarTempButton,BotonReiniciarTemp,MilisegundosTemp,FrameTempTerminado
    def EliminarTemp():
        global PausaTemp,CorriendoTemp,ReinicioTemp
        PausaTemp = False
        ReinicioTemp = False
        CorriendoTemp = False
        Temporizador()
    if len(FrameTemp.winfo_children()) == 9:
        for i in FrameTemp.winfo_children()[1:]:
            i.destroy()
    if len(FrameTemp.winfo_children()) == 1:
        EliminarTempButton = Button(FrameTemp,command=EliminarTemp,image=CerrarIMG,border=0,bg="white",cursor="hand2",activebackground="white")
        EliminarTempButton.place(x=730,y=10)
        BotonPausaPlayTemp = Button(FrameTemp,command=PausarTemp,image=PausaIMG,border=0,bg="white",activebackground="white",cursor="hand2")
        BotonPausaPlayTemp.place(x=290,y=275)
        BotonReiniciarTemp = Button(FrameTemp,command=ReiniciarTemp,image=ReinicioIMG,border=0,bg="white",activebackground="white",cursor="hand2")
        BotonReiniciarTemp.place(x=360,y=275)
        ImagenTemp = "Pausa"
    if ImagenTemp == "Play":
        ImagenTemp = "Pausa"
        BotonPausaPlayTemp.config(image=PausaIMG,command=PausarTemp)
    if not ReinicioTemp:
        if not PausaTemp:
            CorriendoTemp = True
            SegundosTemp = int(SegundosTemp)
            MinutosTemp = int(MinutosTemp)
            HorasTemp = int(HorasTemp)
            MilisegundosTemp = int(MilisegundosTemp)
            if not MilisegundosTemp == 0:
                MilisegundosTemp -= 1
            else:
                if not SegundosTemp == 0:
                    MilisegundosTemp = 9
                    SegundosTemp -= 1
                else:
                    if not MinutosTemp == 0:
                        SegundosTemp = 59
                        MilisegundosTemp = 9
                        MinutosTemp -= 1
                    else:
                        if not HorasTemp == 0:
                            MilisegundosTemp = 9
                            MinutosTemp = 59
                            SegundosTemp = 59
                            HorasTemp -= 1
            SegundosTemp = str(SegundosTemp)
            MinutosTemp = str(MinutosTemp)
            HorasTemp = str(HorasTemp)
            if len(SegundosTemp) == 1:
                SegundosTemp = "0" + SegundosTemp
            if len(MinutosTemp) == 1:
                MinutosTemp = "0" + MinutosTemp
            if len(HorasTemp) == 1:
                HorasTemp = "0" + HorasTemp    
            TempLabel.config(text=f"{HorasTemp}:{MinutosTemp}:{SegundosTemp}")
            if not Terminado:
                FrameTemp.after(100,PlayTemp)
            if Terminado:
                mixer.init()
                mixer.music.load("Fotos InterfacesGraficas\\Ringtones.mp3")
                mixer.music.play()  
                Terminado = False
                HorasTemp = 0
                MinutosTemp = 0
                SegundosTemp = 0
                BotonPausaPlayTemp.destroy()
                BotonReiniciarTemp.destroy()
                EliminarTempButton.destroy()
                TempLabel.destroy()
                FrameTempTerminado = Frame(FrameTemp,width=400,height=300,bg="white",highlightbackground="grey",highlightthickness=3)
                FrameTempTerminado.place(x=150,y=20)
                FrameTempTerminado.pack_propagate(False)
                RelojImage = PhotoImage(file="Fotos InterfacesGraficas\\Reloj.png")
                Label(FrameTempTerminado,text="Ring\nRing!!!",font=("Helvetica",40,"bold"),bg="white",fg="#12c4c0").pack()
                Label(FrameTempTerminado,image=RelojImage,bg="white").pack()
                Button(FrameTempTerminado,text="C A N C E L A R",font=("Helvetica",15,"bold"),bg="#12c4c0",fg="white",border=0,cursor="hand2",
                width=31,command=CancelarTemp).place(x=8,y=250)
            if (HorasTemp == "00" and
                MinutosTemp == "00" and
                SegundosTemp == "00"):
                Terminado = True
        else:
            FrameTemp.after_cancel(FrameTemp)
            BotonPausaPlayTemp.config(image=PlayIMG,command=PlayTemp)
            ImagenTemp = "Play"
            PausaTemp = False
    else:
        FrameTemp.after_cancel(FrameTemp)
        BotonPausaPlayTemp.config(image=PlayIMG,command=PlayTemp)
        ImagenTemp = "Play"
        ReinicioTemp = False

def CancelarTemp():
    global CorriendoTemp,FrameTempTerminado
    CorriendoTemp = False
    mixer.music.stop()
    FrameTempTerminado.destroy()
    Temporizador()

def TempArriba(arg):
    global HorasTemp,MinutosTemp,SegundosTemp
    global ReinicioHoras,ReinicioMinutos,ReinicioSegundos,TempLabel,IniciarBoton
    if arg == "HorasTemp":
        HorasTemp = int(HorasTemp)
        if HorasTemp < 99:
            HorasTemp += 1
        else:
            HorasTemp = 0
        HorasTemp = str(HorasTemp)
        if len(HorasTemp) == 1:
            HorasTemp = "0" + HorasTemp
    if arg == "MinutosTemp":
        MinutosTemp = int(MinutosTemp)
        if MinutosTemp == 59:
            MinutosTemp = 0
        else:
            MinutosTemp += 1
        MinutosTemp = str(MinutosTemp)
        if len(MinutosTemp) == 1:
            MinutosTemp = "0" + MinutosTemp
    if arg == "SegundosTemp":
        SegundosTemp = int(SegundosTemp)
        if SegundosTemp == 59:
            SegundosTemp = 0
        else:
            SegundosTemp += 1
        SegundosTemp = str(SegundosTemp)
        if len(SegundosTemp) == 1:
            SegundosTemp = "0" + SegundosTemp  
    TempLabel.config(text=f"{HorasTemp}:{MinutosTemp}:{SegundosTemp}")
    if (HorasTemp == "00" and
        MinutosTemp == "00" and
        SegundosTemp == "00"):
        IniciarBoton.config(state="disabled")
    else:
        IniciarBoton.config(state="normal")
    ReinicioHoras = HorasTemp
    ReinicioMinutos = MinutosTemp
    ReinicioSegundos = SegundosTemp

def TempAbajo(arg):
    global HorasTemp,MinutosTemp,SegundosTemp
    global ReinicioHoras,ReinicioMinutos,ReinicioSegundos,TempLabel
    if arg == "HorasTemp":
        HorasTemp = int(HorasTemp)
        if HorasTemp <= 0:
            HorasTemp = 99
        else:
            HorasTemp -= 1
        HorasTemp = str(HorasTemp)
        if len(HorasTemp) == 1:
            HorasTemp = "0" + HorasTemp
    if arg == "MinutosTemp":
        MinutosTemp = int(MinutosTemp)
        if MinutosTemp == 0:
            MinutosTemp = 59
        else:
            MinutosTemp -= 1
        MinutosTemp = str(MinutosTemp)
        if len(MinutosTemp) == 1:
            MinutosTemp = "0" + MinutosTemp
    if arg == "SegundosTemp":
        SegundosTemp = int(SegundosTemp)
        if SegundosTemp == 0:
            SegundosTemp = 59
        else:
            SegundosTemp -= 1
        SegundosTemp = str(SegundosTemp)
        if len(SegundosTemp) == 1:
            SegundosTemp = "0" + SegundosTemp  
    TempLabel.config(text=f"{HorasTemp}:{MinutosTemp}:{SegundosTemp}")
    if (HorasTemp == "00" and
        MinutosTemp == "00" and
        SegundosTemp == "00"):
        IniciarBoton.config(state="disabled")
    else:
        IniciarBoton.config(state="normal")
    ReinicioHoras = HorasTemp
    ReinicioMinutos = MinutosTemp
    ReinicioSegundos = SegundosTemp


    
OpenIMG = PhotoImage(file="Fotos InterfacesGraficas\\open.png")
Button(root,image=OpenIMG,command=Menu_Hamburguesa,border=0,bg="white",activebackground="white",cursor="hand2").place(x=5,y=10)

root.mainloop() 


# Pomodoro
def pomodoro():
    global FramePomodoro, CorriendoTemp, PausaTemp, ReinicioTemp, Terminado, ImagenTemp
    global PlayIMG, PausaIMG, ReinicioIMG, CerrarIMG, TempLabel, BotonPausaPlayTemp, BotonReiniciarTemp
    global tiempo_actual, estado  # Variables para el estado del temporizador

    # ... (código para destruir frames existentes) ...

    FramePomodoro = Frame(root, bg="white", height=500, width=800)
    FramePomodoro.place(x=100, y=0)

    tiempo_pomodoro = 25 * 60  # 25 minutos en segundos
    tiempo_descanso = 5 * 60   # 5 minutos en segundos
    tiempo_actual = tiempo_pomodoro  # Comienza en modo Pomodoro
    estado = "Pomodoro"

    # ... (Widgets: TempLabel, BotonPausaPlayTemp, BotonReiniciarTemp) ...

    def actualizar_etiqueta():
        global tiempo_actual
        minutos, segundos = divmod(tiempo_actual, 60)
        TempLabel.config(text=f"{minutos:02d}:{segundos:02d}")
        if tiempo_actual > 0 and CorriendoTemp:
            tiempo_actual -= 1
            FramePomodoro.after(1000, actualizar_etiqueta)
        else:
            reproducir_alarma()
            if estado == "Pomodoro":
                messagebox.showinfo("Descanso", "Es hora de un descanso de 5 minutos.")
                iniciar_descanso()
            else:
                messagebox.showinfo("Pomodoro", "Es hora de un nuevo Pomodoro.")
                iniciar_pomodoro()

    def iniciar_pomodoro():
        global tiempo_actual, estado
        tiempo_actual = tiempo_pomodoro
        estado = "Pomodoro"
        actualizar_etiqueta()

    def iniciar_descanso():
        global tiempo_actual, estado
        tiempo_actual = tiempo_descanso
        estado = "Descanso"
        actualizar_etiqueta()

    def PlayTemp():
        global CorriendoTemp, PausaTemp
        if not CorriendoTemp:
            CorriendoTemp = True
            BotonPausaPlayTemp.config(image=PausaIMG, command=PausarTemp)
            actualizar_etiqueta()
        else:
            if PausaTemp:
                PausaTemp = False
                BotonPausaPlayTemp.config(image=PausaIMG, command=PausarTemp)
                actualizar_etiqueta()

    def PausarTemp():
        global PausaTemp
        if CorriendoTemp:
            PausaTemp = True
            BotonPausaPlayTemp.config(image=PlayIMG, command=PlayTemp)

    def ReiniciarTemp():
        global tiempo_actual, CorriendoTemp, PausaTemp
        CorriendoTemp = False
        PausaTemp = False
        BotonPausaPlayTemp.config(image=PlayIMG, command=PlayTemp)
        if estado == "Pomodoro":
            tiempo_actual = tiempo_pomodoro
        else:
            tiempo_actual = tiempo_descanso
        actualizar_etiqueta()

    def reproducir_alarma():
        mixer.music.load("Fotos InterfacesGraficas\\Ringtones.mp3")
        mixer.music.play()

root.mainloop()
