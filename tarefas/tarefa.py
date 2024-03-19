import tkinter as tk

# Função para adicionar uma tarefa à lista
def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)

# Função para remover uma tarefa da lista
def remover_tarefa():
    indice = lista_tarefas.curselection()
    if indice:
        lista_tarefas.delete(indice)

# Função principal
def main():
    global entrada_tarefa  # Torna a variável entrada_tarefa global

    root = tk.Tk()
    root.title("Lista de Tarefas")

    # Frame para entrada de tarefas
    frame_entrada = tk.Frame(root)
    frame_entrada.pack(pady=10)
    label_tarefa = tk.Label(frame_entrada, text="Tarefa:")
    label_tarefa.pack(side=tk.LEFT)
    entrada_tarefa = tk.Entry(frame_entrada, width=50)
    entrada_tarefa.pack(side=tk.LEFT)

    # Botão para adicionar tarefas
    botao_adicionar = tk.Button(root, text="Adicionar Tarefa", command=adicionar_tarefa)
    botao_adicionar.pack()

    # Lista de tarefas
    global lista_tarefas  # Torna a variável lista_tarefas global
    lista_tarefas = tk.Listbox(root, width=50)
    lista_tarefas.pack()

    # Botão para remover tarefas
    botao_remover = tk.Button(root, text="Remover Tarefa", command=remover_tarefa)
    botao_remover.pack()

    root.mainloop()

if __name__ == "__main__":
    main()

