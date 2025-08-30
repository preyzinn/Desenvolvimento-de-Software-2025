from tkinter import *
root = Tk()
root.title("Cadastro de Funcionários")
root.geometry("300x250")

class Funcionario:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id

    def __str__(self):
        return f"{self.id} - {self.nome}"

class Professor(Funcionario):
    pass

class Administracao(Funcionario):
    pass

class Tecno(Funcionario):
    pass


funcionarios = []


def cadastro():
    nome = entry_nome.get()
    id_func = entry_id.get()
    cargo = cargo_var.get()

    if nome.strip() == "" or id_func.strip() == "":
        label_status.config(text="⚠ Preencha todos os campos!", fg="red")
        return

    if cargo == "Professor":
        f = Professor(nome, id_func)
    elif cargo == "Administração":
        f = Administracao(nome, id_func)
    else:
        f = Tecno(nome, id_func)

    funcionarios.append(f)


    listbox_funcionarios.insert(END, str(f))
    label_status.config(text="Funcionário cadastrado", fg="green")


    entry_nome.delete(0, END)
    entry_id.delete(0, END)



Label(root, text="Nome:").pack(pady=2)
entry_nome = Entry(root)
entry_nome.pack(pady=2)

Label(root, text="ID:").pack(pady=2)
entry_id = Entry(root)
entry_id.pack(pady=2)

Label(root, text="Cargo:").pack(pady=2)
cargo_var = StringVar(value="Professor")
OptionMenu(root, cargo_var, "Professor", "Administração", "Tecno").pack(pady=2)

Button(root, text="Cadastrar", command=cadastro).pack(pady=5)

label_status = Label(root, text="")
label_status.pack()

Label(root, text="Funcionários cadastrados:").pack(pady=5)
listbox_funcionarios = Listbox(root, width=30, height=6)
listbox_funcionarios.pack()

root.mainloop()


