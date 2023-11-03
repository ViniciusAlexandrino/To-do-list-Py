import tkinter as tk

def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)

def remover_tarefa():
    try:
        selecao = lista_tarefas.curselection()
        if selecao:
            lista_tarefas.delete(selecao)
    except:
        pass

# Configuração da janela
janela = tk.Tk()
janela.title("Tarefa App")

# Entrada de tarefa
entrada_tarefa = tk.Entry(janela)
entrada_tarefa.pack(pady=10)

# Botões
botao_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa)
botao_remover = tk.Button(janela, text="Remover Tarefa Selecionada", command=remover_tarefa)
botao_adicionar.pack()
botao_remover.pack()

# Lista de tarefas
lista_tarefas = tk.Listbox(janela)
lista_tarefas.pack()

# Iniciar a janela
janela.mainloop()
