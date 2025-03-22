from tkinter import *

# ! Definindo algumas cores

black_color = "#000000"  # preta
grey_color = "#59656F"  # cinza
light_grey_color = "#cdd1cd"  # cinza claro
white_color = "#feffff"  # branca
blue_color = "#0074eb"  # azul
red_color = "#f04141"  # vermelho
green_color = "#59b356"  # verde

# ! Criando janela principal

janela = Tk()
janela.resizable(width=FALSE, height=FALSE)
janela.geometry('500x255')
janela.title('To-Do App')
janela.configure(background=light_grey_color)

# ! Dividindo a janela em duas partes

# > Frame da esquerda
frame_esquerda = Frame(janela, width=300, height=200, bg=white_color, relief="flat")
frame_esquerda.grid(row=0, column=0, sticky=NSEW)

# > Frame da direita
frame_direita = Frame(janela, width=200, height=250, bg=blue_color, relief="flat")
frame_direita.grid(row=0, column=1, sticky=NSEW)

# ! Dividindo o frame da esquerda em duas partes

frame_e_buttons = Frame(frame_esquerda, width=300, height=40, bg=light_grey_color, relief="flat")
frame_e_buttons.grid(row=0, column=0, sticky=NSEW)

frame_e_baixo = Frame(frame_esquerda, width=300, height=160, bg=black_color, relief="flat")
frame_e_baixo.grid(row=1, column=0, sticky=NSEW)

# ? Dividindo o frame dos botões novo, remover e atualizar

# > Botão de novo
button_new = Button(frame_e_buttons, text="Novo",fg="white", font="5", anchor="center",
                    width=10, height=1, bg=blue_color, relief="flat")
button_new.grid(row=0, column=0, sticky=NSEW)

#> Botão de remover
button_remove = Button(frame_e_buttons, text="Remover",fg="white", font="5", anchor="center",
                    width=10, height=1, bg=red_color, relief="flat")
button_remove.grid(row=0, column=1, sticky=NSEW)

#> Botão de atualizar
button_update = Button(frame_e_buttons, text="Novo",fg="white", font="5", anchor="center",
                    width=10, height=1, bg=green_color, relief="flat")
button_update.grid(row=0, column=2, sticky=NSEW)


janela.mainloop()
