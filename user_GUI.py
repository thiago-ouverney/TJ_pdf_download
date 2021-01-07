import tkinter as tk
from acesso_site import robo_download_email
from pdf_join import consolidando_emails
from send_email import send_email
import time
from tkinter.filedialog import askopenfilename

def robozinho():
    robo_download_email(dir_trabalho.get(),
                         url.get(),
                         1,final_paginas.get()
                        )

    time.sleep(2)

    consolidando_emails(dir_trabalho.get(),
                        processo_cod.get()
                        )



master = tk.Tk()
master.title("Robo Búzios")


#Labels
tk.Label(master, text="url").grid(row=0)
tk.Label(master, text="Número Processo").grid(row=1)
tk.Label(master, text="Número de Páginas").grid(row=2)
tk.Label(master, text="Diretório Trabalho").grid(row=3)


#Criando Entradas
url = tk.Entry(master)
processo_cod = tk.Entry(master)
email_solicitante = tk.Entry(master)
final_paginas = tk.Entry(master)
dir_trabalho = tk.Entry(master)

#Organizando minhas entradas
url.grid(row=0, column=1)
processo_cod.grid(row=1, column=1)
final_paginas.grid(row=2, column=1)
dir_trabalho.grid(row=3, column=1)

#Variáveis já preenchidas
dir_trabalho.insert(10,'C:\\Users\\81018590\\Desktop\\Teste_Trabalho')
#http://www1.tjrj.jus.br/gedvisaweb/frmFramenavegador.aspx?id=33FAC503470D4846

#Botões
tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=5,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)

#
# tk.Button(master,
#           text='Ask Open File',
#           command=askopenfilename).grid(row=6,
#                                     column=0,
#                                     sticky=tk.W,
#                                     pady=4)
tk.Button(master,
          text='Rodar',
          command=robozinho
          ).grid(row=5,
                 column=1,
                 sticky=tk.W,
                 pady=4
                 )



master.mainloop()