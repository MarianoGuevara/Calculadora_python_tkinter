from os import system 
system("cls")

import tkinter
import customtkinter
import re

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CALCULADORA")
        self.minsize(200, 200)

        # state='disabled'
        self.txt_screen = customtkinter.CTkEntry(master=self)
        self.txt_screen.grid(row=1, column=2, pady=10, padx=10)

        self.signos = ['+', '-', 'x', '/', '=']

        self.sign_rows = [2, 3, 4, 5, 6]

        self.sign_columns = [3, 3, 3, 3, 3]

        self.numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        self.number_rows = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6]

        self.number_columns = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]

        for i in range(len(self.number_rows)):
            self.btn_numerico = customtkinter.CTkButton(master=self,
                            text=self.numeros[i], command=lambda 
                            contenido=self.numeros[i]: 
                            self.boton_numerico(contenido))
            self.btn_numerico.grid(row=self.number_rows[i], 
                                    column=self.number_columns[i]
                                    , pady=10, padx=10)

        for i in range(len(self.sign_rows)):
            self.btn_signo = customtkinter.CTkButton(master=self,
                            text=self.signos[i], command=lambda 
                            contenido=self.signos[i]: 
                            self.boton_signo(contenido))
            self.btn_signo.grid(row=self.sign_rows[i], 
                                    column=self.sign_columns[i]
                                    , pady=10, padx=10)

        self.label_title = customtkinter.CTkLabel(master=self, 
                        text="Calculadora", font=("Arial", 15, "bold"))
        self.label_title.grid(row=1, column=1, padx=10, pady=10)

        self.btn_reset = customtkinter.CTkButton(master=self,
                            text='Reset', command=lambda 
                            contenido=self.signos[i]: 
                            self.borrar_screen(contenido, self.txt_screen))
        self.btn_reset.grid(row=1, column=3, padx=10, pady=10)

    def borrar_screen(self, contenido, box):
        box.delete(0, tkinter.END)

    def obtener_txt_box(self, box):
        return box.get()

    def insertar_en_txt_box(self, box, dato, indice_inicio):
        box.insert(indice_inicio, dato)

    def boton_numerico(self, contenido):
        actual_ancho_pantalla = len(self.obtener_txt_box(self.txt_screen))

        for i in range(len(self.numeros)):
            if contenido == self.numeros[i]:
                self.insertar_en_txt_box(self.txt_screen,
                                    self.numeros[i], actual_ancho_pantalla)

    def boton_signo(self, contenido):
        signo_actual = ''
        actual_ancho_pantalla = len(self.obtener_txt_box(self.txt_screen))
        caracteres_en_pantalla = self.obtener_txt_box(self.txt_screen)

        lista_partes_screen = re.split('[+|\-|x|/]', caracteres_en_pantalla)

        if actual_ancho_pantalla != 0:
            for i in range(len(self.signos)):
                if (contenido == self.signos[i] and contenido != '=' and 
                    (len(lista_partes_screen) == 1 or 
                    caracteres_en_pantalla[0] == "-")):
                    self.insertar_en_txt_box(self.txt_screen,
                                        f' {self.signos[i]} ', 
                                        actual_ancho_pantalla)

            if contenido == '=' and len(lista_partes_screen) > 1:
                decimal = 0
                for partes in lista_partes_screen:
                    for caracter in partes:
                        if caracter == '.':
                            decimal += 1

                if lista_partes_screen[0] == '':
                    if decimal == 1:
                        num_1 = float(lista_partes_screen[1]) 
                        - (float(lista_partes_screen[1]) * 2)
                    else:
                        num_1 = int(lista_partes_screen[1]) 
                        - (int(lista_partes_screen[1]) * 2)

                    if lista_partes_screen[2][0] == '-':
                        if decimal == 2:
                            num_2 = float(lista_partes_screen[2])
                            - (float(lista_partes_screen[2]) * 2)
                        else:
                            num_2 = int(lista_partes_screen[2])
                            - (int(lista_partes_screen[2]) * 2)
                    else:
                        num_2 = int(lista_partes_screen[2])
                else:
                    if decimal == 1:
                        num_1 = float(lista_partes_screen[0])
                        num_2 = int(lista_partes_screen[1])
                    elif decimal == 2:
                        num_1 = int(lista_partes_screen[0])
                        num_2 = float(lista_partes_screen[1])
                    else:
                        num_1 = int(lista_partes_screen[0])
                        num_2 = int(lista_partes_screen[1])

                for caracter in caracteres_en_pantalla:
                    if caracter == '+':
                        signo_actual = '+'
                    elif caracter == '-':
                        signo_actual = '-'
                    elif caracter == 'x':
                        signo_actual = 'x'
                    elif caracter == '/':
                        signo_actual = '/'

                resultado = f'{self.realizar_operacion(num_1, num_2, signo_actual):.2f}'

                self.borrar_screen(contenido, self.txt_screen)
                self.insertar_en_txt_box(self.txt_screen, 
                                        resultado, actual_ancho_pantalla)

    def realizar_operacion(self, a, b, signo):
        match signo:
            case '+':
                return a + b
            case '-':
                return a - b
            case 'x':
                return a * b
            case '/':
                return a / b


if __name__ == "__main__":
    app = App()
    app.mainloop()