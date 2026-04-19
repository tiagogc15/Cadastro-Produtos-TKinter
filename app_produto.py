import tkinter as tk
from tkinter import messagebox

produtos = {}

# ================== FUNÇÃO TROCAR TELA ==================
def mostrar_frame(frame):
    for f in (frame_menu, frame_cadastro, frame_busca, frame_lista, frame_atualizar, frame_excluir):
        f.pack_forget()
    frame.pack(fill="both", expand=True)

# ================== SAIR ==================
def sair():
    if messagebox.askyesno("Sair", "Deseja realmente sair?"):
        janela.destroy()

# ================== CADASTRAR ==================
def cadastrar():
    try:
        codigo = int(entry_cod_cad.get())
        produtos[codigo] = {
            "nome": entry_nome_cad.get(),
            "preco": float(entry_preco_cad.get().replace(",", ".")),
            "quantidade": int(entry_qtd_cad.get())
        }
        messagebox.showinfo("Sucesso", "Produto cadastrado!")
    except:
        messagebox.showerror("Erro", "Dados inválidos!")

# ================== LISTAR ==================
def listar():
    lista.delete(0, tk.END)
    for c, p in produtos.items():
        lista.insert(tk.END, f"{c} - {p['nome']} - R$ {p['preco']:.2f}")

# ================== BUSCAR ==================
def buscar():
    nome = entry_nome_busca.get().lower()
    codigo = entry_cod_busca.get()

    lista_busca.delete(0, tk.END)

    if codigo:
        codigo = int(codigo)
        if codigo in produtos:
            p = produtos[codigo]
            lista_busca.insert(tk.END, f"{codigo} - {p['nome']}")
        else:
            messagebox.showwarning("Erro", "Não encontrado")

    elif nome:
        for c, p in produtos.items():
            if nome in p["nome"].lower():
                lista_busca.insert(tk.END, f"{c} - {p['nome']}")

# ================== ATUALIZAR ==================
def carregar_para_edicao(event):
    selecionado = lista_atual.get(tk.ACTIVE)
    if selecionado:
        codigo = int(selecionado.split(" - ")[0])
        p = produtos[codigo]

        entry_cod_atual.delete(0, tk.END)
        entry_nome_atual.delete(0, tk.END)
        entry_preco_atual.delete(0, tk.END)
        entry_qtd_atual.delete(0, tk.END)

        entry_cod_atual.insert(0, codigo)
        entry_nome_atual.insert(0, p["nome"])
        entry_preco_atual.insert(0, p["preco"])
        entry_qtd_atual.insert(0, p["quantidade"])

def atualizar():
    try:
        codigo = int(entry_cod_atual.get())
        produtos[codigo] = {
            "nome": entry_nome_atual.get(),
            "preco": float(entry_preco_atual.get().replace(",", ".")),
            "quantidade": int(entry_qtd_atual.get())
        }
        messagebox.showinfo("Atualizado", "Produto atualizado!")
    except:
        messagebox.showerror("Erro", "Dados inválidos!")

# ================== EXCLUIR ==================
def excluir():
    selecionado = lista_excluir.get(tk.ACTIVE)
    if selecionado:
        codigo = int(selecionado.split(" - ")[0])

        if messagebox.askyesno("Confirmar", "Deseja excluir?"):
            del produtos[codigo]
            messagebox.showinfo("Excluído", "Produto removido!")
            atualizar_lista_excluir()

def atualizar_lista_excluir():
    lista_excluir.delete(0, tk.END)
    for c, p in produtos.items():
        lista_excluir.insert(tk.END, f"{c} - {p['nome']}")

# ================== JANELA ==================
janela = tk.Tk()
janela.title("Sistema de Produtos")
janela.geometry("400x500")

# ================== MENU ==================
frame_menu = tk.Frame(janela)

tk.Button(frame_menu, text="Cadastrar", command=lambda: mostrar_frame(frame_cadastro)).pack(pady=10)
tk.Button(frame_menu, text="Buscar", command=lambda: mostrar_frame(frame_busca)).pack(pady=10)
tk.Button(frame_menu, text="Listar", command=lambda: [mostrar_frame(frame_lista), listar()]).pack(pady=10)
tk.Button(frame_menu, text="Atualizar", command=lambda: [mostrar_frame(frame_atualizar), listar_atual()]).pack(pady=10)
tk.Button(frame_menu, text="Excluir", command=lambda: [mostrar_frame(frame_excluir), atualizar_lista_excluir()]).pack(pady=10)
tk.Button(frame_menu, text="Sair", command=sair).pack(pady=10)

# ================== CADASTRO ==================
frame_cadastro = tk.Frame(janela)

entry_cod_cad = tk.Entry(frame_cadastro)
entry_nome_cad = tk.Entry(frame_cadastro)
entry_preco_cad = tk.Entry(frame_cadastro)
entry_qtd_cad = tk.Entry(frame_cadastro)

for txt, entry in [("Código", entry_cod_cad), ("Nome", entry_nome_cad), ("Preço", entry_preco_cad), ("Qtd", entry_qtd_cad)]:
    tk.Label(frame_cadastro, text=txt).pack()
    entry.pack()

tk.Button(frame_cadastro, text="Salvar", command=cadastrar).pack()
tk.Button(frame_cadastro, text="Voltar", command=lambda: mostrar_frame(frame_menu)).pack()

# ================== LISTA ==================
frame_lista = tk.Frame(janela)
lista = tk.Listbox(frame_lista)
lista.pack(fill="both", expand=True)

tk.Button(frame_lista, text="Voltar", command=lambda: mostrar_frame(frame_menu)).pack()

# ================== BUSCA ==================
frame_busca = tk.Frame(janela)

entry_cod_busca = tk.Entry(frame_busca)
entry_nome_busca = tk.Entry(frame_busca)
lista_busca = tk.Listbox(frame_busca)

tk.Label(frame_busca, text="Código").pack()
entry_cod_busca.pack()
tk.Label(frame_busca, text="Nome").pack()
entry_nome_busca.pack()

tk.Button(frame_busca, text="Buscar", command=buscar).pack()
lista_busca.pack(fill="both", expand=True)

tk.Button(frame_busca, text="Voltar", command=lambda: mostrar_frame(frame_menu)).pack()

# ================== ATUALIZAR ==================
frame_atualizar = tk.Frame(janela)

lista_atual = tk.Listbox(frame_atualizar)
lista_atual.pack(fill="both", expand=True)
lista_atual.bind("<<ListboxSelect>>", carregar_para_edicao)

entry_cod_atual = tk.Entry(frame_atualizar)
entry_nome_atual = tk.Entry(frame_atualizar)
entry_preco_atual = tk.Entry(frame_atualizar)
entry_qtd_atual = tk.Entry(frame_atualizar)

for e in [entry_cod_atual, entry_nome_atual, entry_preco_atual, entry_qtd_atual]:
    e.pack()

tk.Button(frame_atualizar, text="Salvar Alteração", command=atualizar).pack()
tk.Button(frame_atualizar, text="Voltar", command=lambda: mostrar_frame(frame_menu)).pack()

def listar_atual():
    lista_atual.delete(0, tk.END)
    for c, p in produtos.items():
        lista_atual.insert(tk.END, f"{c} - {p['nome']}")

# ================== EXCLUIR ==================
frame_excluir = tk.Frame(janela)

lista_excluir = tk.Listbox(frame_excluir)
lista_excluir.pack(fill="both", expand=True)

tk.Button(frame_excluir, text="Excluir", command=excluir).pack()
tk.Button(frame_excluir, text="Voltar", command=lambda: mostrar_frame(frame_menu)).pack()

# ================== INICIAR ==================
mostrar_frame(frame_menu)
janela.mainloop()

