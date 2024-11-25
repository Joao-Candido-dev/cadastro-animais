import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod

# Classes
class Animal(ABC):
    @abstractmethod
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def __str__(self):
        pass

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def __str__(self):
        return f"Cachorro: {self.nome}, Idade: {self.idade}, Raça: {self.raca}"

class Gato(Animal):
    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)
        self.cor = cor

    def __str__(self):
        return f"Gato: {self.nome}, Idade: {self.idade}, Cor: {self.cor}"

# Lista 
animais = []

# Funções
def cadastrar_animal():
    tipo = tipo_var.get()
    nome = nome_entry.get()
    idade = idade_entry.get()
    atributo = atributo_entry.get()

    if not nome or not idade or not atributo:
        resultado_label.config(text="Por favor, preencha todos os campos.")
        return

    try:
        idade = int(idade)
    except ValueError:
        resultado_label.config(text="Idade deve ser um número.")
        return

    if tipo == "Cachorro":
        animal = Cachorro(nome, idade, atributo)
    elif tipo == "Gato":
        animal = Gato(nome, idade, atributo)
    else:
        resultado_label.config(text="Tipo de animal inválido.")
        return

    animais.append(animal)
    resultado_label.config(text=f"{tipo} cadastrado com sucesso!")
    atualizar_lista()

def atualizar_lista():
    lista_text.delete("1.0", tk.END)
    for animal in animais:
        lista_text.insert(tk.END, str(animal) + "\n")


root = tk.Tk()
root.title("Cadastro de Animais")


tabs = ttk.Notebook(root)
tabs.pack(expand=1, fill="both")


cadastro_frame = ttk.Frame(tabs)
tabs.add(cadastro_frame, text="Cadastro")

ttk.Label(cadastro_frame, text="Tipo:").grid(row=0, column=0, padx=5, pady=5)
tipo_var = tk.StringVar(value="Cachorro")
ttk.Combobox(cadastro_frame, textvariable=tipo_var, values=["Cachorro", "Gato"]).grid(row=0, column=1, padx=5, pady=5)

ttk.Label(cadastro_frame, text="Nome:").grid(row=1, column=0, padx=5, pady=5)
nome_entry = ttk.Entry(cadastro_frame)
nome_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(cadastro_frame, text="Idade:").grid(row=2, column=0, padx=5, pady=5)
idade_entry = ttk.Entry(cadastro_frame)
idade_entry.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(cadastro_frame, text="Raça/Cor:").grid(row=3, column=0, padx=5, pady=5)
atributo_entry = ttk.Entry(cadastro_frame)
atributo_entry.grid(row=3, column=1, padx=5, pady=5)

ttk.Button(cadastro_frame, text="Cadastrar", command=cadastrar_animal).grid(row=4, column=0, columnspan=2, pady=10)
resultado_label = ttk.Label(cadastro_frame, text="")
resultado_label.grid(row=5, column=0, columnspan=2)


lista_frame = ttk.Frame(tabs)
tabs.add(lista_frame, text="Lista de Animais")


lista_text = tk.Text(lista_frame, width=50, height=20)
lista_text.pack(padx=10, pady=10)

root.mainloop()
