from tkinter import *
from db import *

# ? Definindo algumas cores

black_color = "#000000"  # preta
grey_color = "#59656F"  # cinza
light_grey_color = "#cdd1cd"  # cinza claro
white_color = "#feffff"  # branca
blue_color = "#0074eb"  # azul
red_color = "#f04141"  # vermelho
green_color = "#59b356"  # verde

# ? Criando janela principal

janela = Tk()
janela.resizable(width=FALSE, height=FALSE)
janela.geometry('500x255')
janela.title('To-Do App')
janela.configure(background=light_grey_color)

# ? Dividindo a janela em duas partes

# > Frame da esquerda
frame_esquerda = Frame(janela, width=300, height=200, bg=white_color, relief="flat")
frame_esquerda.grid(row=0, column=0, sticky=NSEW)

# > Frame da direita
frame_direita = Frame(janela, width=200, height=250, bg=white_color, relief="flat")
frame_direita.grid(row=0, column=1, sticky=NSEW)

# ? Dividindo o frame da esquerda em duas partes

frame_e_buttons = Frame(frame_esquerda, width=300, height=40, bg=light_grey_color, relief="flat")
frame_e_buttons.grid(row=0, column=0, sticky=NSEW)

frame_e_baixo = Frame(frame_esquerda, width=300, height=160, bg=light_grey_color, relief="flat")
frame_e_baixo.grid(row=1, column=0, sticky=NSEW)

def main(event):
    # > Novo
    if event == "novo":
        for widget in frame_e_baixo.winfo_children():
            widget.destroy()
        
        def adicionar():
            tarefa_entry = entry.get()
            inserir([tarefa_entry])
            mostrar()
        
        lb = Label(frame_e_baixo, width=42, height=5, pady=15, anchor=CENTER, text="Insira nova tarefa")
        lb.grid(row=0, column=0, sticky=NSEW)
        
        entry = Entry(frame_e_baixo, width=15)
        entry.grid(row=1, column=0, sticky=NSEW)
        
        button_add = Button(frame_e_baixo, width=9, height=1, bg=blue_color, pady=10,
                        text="Adicionar", fg="white", font="8", anchor="center", relief=RAISED, command=adicionar)
        button_add.grid(row=2, column=0, sticky=NSEW, pady=15)

    # > Atualizar
    if event == "atualizar":
        for widget in frame_e_baixo.winfo_children():
            widget.destroy()
            
        def on():
            lb = Label(frame_e_baixo, width=42, height=5, pady=15, anchor=CENTER, text="Atualizar tarefa")
            lb.grid(row=0, column=0, sticky=NSEW)
            
            entry = Entry(frame_e_baixo, width=15)
            entry.grid(row=1, column=0, sticky=NSEW)
            
            valor_selecionado = listbox.curselection()[0]
            palavra = listbox.get(valor_selecionado)
            entry.insert(0, palavra)
            
            tarefas = selecionar()
            
            def alterar():
                for item in tarefas:
                    if palavra == item[1]:
                        nova = [entry.get(), item[0]]
                        atualizar(nova)
                        entry.delete(0, END)
                mostrar()

            button_update = Button(frame_e_baixo, width=9, height=1, bg=green_color, pady=10,
                            text="Atualizar", fg="white", font="8", anchor="center", relief=RAISED, command=alterar)
            button_update.grid(row=2, column=0, sticky=NSEW, pady=15)
        
        on()
    
    # > Remover
    if event == 'remover':
        ...
        
        
# > Função remover
def remove():
    valor_selecionado = listbox.curselection()[0]
    palavra = listbox.get(valor_selecionado)
    tarefas = selecionar()
    
    for item in tarefas:
        if palavra == item[1]:
            deletar([item[0]])
    mostrar()

# ? Criando os botões novo, remover e atualizar

# > Botão de novo
button_new = Button(frame_e_buttons, width=10, height=1, bg=blue_color,
                    text="Novo", fg="white", font="5", anchor="center", relief=RAISED, command=lambda: main("novo"))
button_new.grid(row=0, column=0, sticky=NSEW, pady=1)

# > Botão de remover
button_remove = Button(frame_e_buttons, width=10, height=1, bg=red_color,
                    text="Remover", fg="white", font="5", anchor="center", relief=RAISED, command=remove)
button_remove.grid(row=0, column=1, sticky=NSEW, pady=1)

#> Botão de atualizar
button_update = Button(frame_e_buttons, width=10, height=1, bg=green_color,
                    text="Atualizar", fg="white", font="5", anchor="center", relief=RAISED, command=lambda: main("atualizar"))
button_update.grid(row=0, column=2, sticky=NSEW, pady=1)

# ? Adicionando Listbox e um Label
label = Label(frame_direita, width=37, height=1, pady=7, padx=10, relief="flat", anchor=W,
            text="Tarefas", font=("Courier 20 bold"), fg=black_color, bg=white_color)
label.grid(row=0, column=0, sticky=NSEW, pady=1)

listbox = Listbox(frame_direita, width=1, font=("Courier 10 bold"), fg=black_color, bg=white_color)
listbox.grid(row=1, column=0, sticky=NSEW, pady=5)

# ? Adicionando as tarefas na listbox

def mostrar():
    listbox.delete(0, END)
    tarefas = selecionar()
    for item in tarefas:
        listbox.insert(END, item[1])


mostrar()

janela.mainloop()
