import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from Computador.Montador import Montador
from Computador.Processador import Processador
from Computador.Registradores import Registradores
class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.processador = Processador()

        self.nome = tk.Text(master, width=95, height=25, )
        self.nome.grid(row=1, column=0, sticky=tk.W+tk.E+tk.N+tk.S, padx=5)

        self.input = tk.Text(master, width=95, height=12)
        self.input.grid(row=2, column=0, sticky=tk.W+tk.E+tk.N+tk.S, pady=10, padx=5)

        self.registradores = self.processador.getRegistradores()

        self.grid(row=1, column=1, sticky=tk.N+tk.S)
        self.menuBar()
        self.set_widgets()

    def set_widgets(self):
        # Inicia o Treeview com as seguintes colunas:
        self.dataCols = ('nome', 'numero', 'valor')
        self.tree = ttk.Treeview(columns=self.dataCols, show='headings')
        self.tree.column('nome', width=70)
        self.tree.column('numero', width=70)
        self.tree.column('valor', width=70)
        self.tree.grid(row=1, column=2 , sticky=tk.N + tk.S)

        # Barras de rolagem
        ysb = ttk.Scrollbar(orient=tk.VERTICAL, command=self.tree.yview)
        self.tree['yscroll'] = ysb.set
        ysb.grid(row=1, column=3, sticky=tk.N + tk.S)

        # Define o textos do cabeçalho (nome em maiúsculas)
        for c in self.dataCols:
            self.tree.heading(c, text=c.title())

        # Dados:
        self.data = self.processador.getRegistradores()

        # Insere cada item dos dados
        for item in self.data:
            self.tree.insert('', 'end', values=item)

    def menuBar(self):
        self.menubar = tk.Menu(self)
        menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=menu)
        menu.add_command(label="Abrir" , command=self.Open)
        menu.add_command(label="Salvar" , command=self.Salvar)

        menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Run", menu=menu)
        menu.add_command(label="Assemble", command=self.verificaSenha)

        self.master.config(menu=self.menubar)

        try:
            self.master.config(menu=self.menubar)
        except AttributeError:
            # master is a toplevel window (Python 1.4/Tkinter 1.63)
            self.master.tk.call(tk.master, "config", "-menu", self.menubar)

    def verificaSenha(self):
        self.processador.setPalavra(Montador(self.nome.get('0.0', tk.END), self.processador.getRegistradores()).getPalavrasMontadas())
        self.processador.setLabel(Montador(self.nome.get('0.0', tk.END), self.processador.getRegistradores()).getLabels())
        self.processador.nextStep()
        self.set_widgets()

    def Open(self):
        arquivo = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Assembler Files","*.asm;*.s"),("all files","*.*")))
        try:
            file = open(arquivo, 'r')
            contents = file.read()

            self.nome.delete(0.0, END)
            self.nome.insert(0.0, contents)
        except:
            pass

    def Salvar(self):
        fileName = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("Assembler Files","*.asm;*.s"),("all files","*.*")))
        try:
            file = open(fileName + '.asm', 'w')
            textoutput = self.text.get(0.0, END)
            file.write(textoutput)
        except:
            pass
        finally:
            file.close()

if __name__ == '__main__':
    root = tk.Tk()

    app = Application(master=root)
    app.master.title("AA Arquitetura")
    app.master.geometry("1000x620+100+100")
    app.mainloop()