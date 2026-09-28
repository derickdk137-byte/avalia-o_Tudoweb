"""Pesquisa de atendimento TudoWeb. Execute com: python3 app.py."""

# Tkinter cria a interface; messagebox exibe alertas e ttk fornece a barra de progresso.
import tkinter as tk
from tkinter import messagebox, ttk


# Configuração geral: limite da pesquisa e cores usadas na interface (hexadecimal).
TOTAL_ENTREVISTADOS = 50
LARANJA = "#C74708"
FUNDO = "#FFF5EB"
TEXTO = "#39251B"


class Pesquisa:
    """Armazena e valida as respostas durante a execução do aplicativo."""

    def __init__(self):
        # Cada objeto Pesquisa começa com uma lista vazia de entrevistados.
        # self permite acessar os dados do próprio objeto em seus métodos.
        self.respostas = []

    def registrar(self, nome, idade, opiniao):
        """Valida os dados e adiciona uma resposta; informa erros com ValueError."""
        # Impede que a pesquisa ultrapasse o número exigido de participantes.
        if len(self.respostas) >= TOTAL_ENTREVISTADOS:
            raise ValueError("A pesquisa já possui 50 respostas.")
        # Remove espaços nas extremidades e rejeita nomes vazios.
        nome = nome.strip()
        if not nome:
            raise ValueError("Digite o nome do entrevistado.")
        # Converte o texto da idade em inteiro; except trata falhas de conversão.
        try:
            idade = int(idade)
        except (ValueError, TypeError):
            raise ValueError("Digite a idade em anos inteiros.") from None
        # Confere a faixa de idade e exige uma das três opiniões disponíveis.
        if not 0 <= idade <= 130:
            raise ValueError("Digite uma idade entre 0 e 130 anos.")
        if opiniao not in (1, 2, 3):
            raise ValueError("Selecione uma opinião sobre o atendimento.")
        # Guarda os três dados em um dicionário dentro da lista de respostas.
        self.respostas.append({"nome": nome, "idade": idade, "opiniao": opiniao})

    def resultados(self):
        """Retorna as quantidades de EXCELENTE e RUIM, nessa ordem."""
        # Reinicia os contadores a cada cálculo para não duplicar as quantidades.
        excelentes = 0
        ruins = 0
        # Estrutura de repetição: percorre todos os entrevistados e conta votos.
        for resposta in self.respostas:
            # Cada += 1 acrescenta um voto; a opinião 2 (BOM) não é contabilizada aqui.
            if resposta["opiniao"] == 1:
                excelentes += 1
            elif resposta["opiniao"] == 3:
                ruins += 1
        return excelentes, ruins


class Aplicativo:
    """Constrói a tela e conecta as ações do usuário aos dados da pesquisa."""

    def __init__(self, janela):
        """Prepara a janela principal e apresenta o formulário inicial."""
        # Mantém referências à janela e ao objeto responsável pelas respostas.
        self.janela = janela
        self.pesquisa = Pesquisa()
        # Define título, tamanho inicial, tamanho mínimo e cor de fundo.
        janela.title("TudoWeb • Pesquisa de atendimento")
        janela.geometry("620x740")
        janela.minsize(560, 700)
        janela.configure(bg=FUNDO)
        # Encaminha o clique no X da janela ao método que confirma a saída.
        janela.protocol("WM_DELETE_WINDOW", self.fechar)

        # Personaliza o tema e a cor laranja da barra de progresso.
        estilo = ttk.Style(janela)
        estilo.theme_use("clam")
        estilo.configure("TudoWeb.Horizontal.TProgressbar", background=LARANJA,
                         troughcolor="#F5DDC8", borderwidth=0)

        # Frame agrupa elementos; Label mostra textos; pack posiciona os elementos.
        # padx/pady definem espaçamentos; bg/fg definem cores de fundo e de texto.
        cabecalho = tk.Frame(janela, bg=LARANJA, padx=32, pady=24)
        cabecalho.pack(fill="x")
        tk.Label(cabecalho, text="TudoWeb", font=("Arial", 26, "bold"),
                 bg=LARANJA, fg="white").pack(anchor="w")
        tk.Label(cabecalho, text="PESQUISA DE ATENDIMENTO", font=("Arial", 10, "bold"),
                 bg=LARANJA, fg="white").pack(anchor="w", pady=(8, 0))

        # A área central recebe primeiro o formulário e depois os resultados.
        self.corpo = tk.Frame(janela, bg=FUNDO, padx=32, pady=24)
        self.corpo.pack(fill="both", expand=True)
        self.formulario()

    def texto(self, texto, tamanho=12, negrito=False):
        """Cria um rótulo padronizado e o retorna para permitir atualizações."""
        label = tk.Label(self.corpo, text=texto, bg=FUNDO, fg=TEXTO,
                         font=("Arial", tamanho, "bold" if negrito else "normal"),
                         anchor="w", justify="left", wraplength=490)
        label.pack(fill="x", pady=(0, 10))
        return label

    def formulario(self):
        """Monta os campos, as opções de opinião e o botão de registro."""
        # Apresenta as instruções e o progresso inicial, ainda sem respostas.
        self.texto("Sua opinião faz a diferença.", 21, True)
        self.texto("Preencha os dados e selecione como foi o atendimento.")
        self.progresso_texto = self.texto("Entrevistado 1 de 50 • 0 respostas registradas", 11)
        self.barra = ttk.Progressbar(self.corpo, maximum=TOTAL_ENTREVISTADOS,
                                    style="TudoWeb.Horizontal.TProgressbar")
        self.barra.pack(fill="x", pady=(0, 20))

        # Entry é uma caixa de digitação: aqui recebe o nome do participante.
        self.texto("Nome do entrevistado", 11, True)
        self.nome = tk.Entry(self.corpo, font=("Arial", 14), relief="solid", bd=1)
        self.nome.pack(fill="x", ipady=7, pady=(0, 14))
        # A idade é digitada como texto e validada ao registrar a resposta.
        self.texto("Idade (anos)", 11, True)
        self.idade = tk.Entry(self.corpo, font=("Arial", 14), relief="solid", bd=1)
        self.idade.pack(fill="x", ipady=7, pady=(0, 18))
        self.texto("Como você avalia o atendimento?", 12, True)
        # Variável compartilhada pelas opções: 0 significa nenhuma selecionada.
        self.opiniao = tk.IntVar(value=0)
        # Repetição para montar as três opções previstas na pesquisa.
        for numero, descricao, cor, selecionada, texto in (
            (1, "EXCELENTE", "#21833B", "#145526", "white"),
            (2, "BOM", "#2563EB", "#1E40AF", "white"),
            (3, "RUIM", "#DC2626", "#991B1B", "white"),
        ):
            # Uma única opção pode ficar selecionada. indicatoron=False dá
            # aparência de botão; selectcolor destaca a opção escolhida.
            tk.Radiobutton(self.corpo, text=f"{numero}  •  {descricao}",
                           variable=self.opiniao, value=numero, bg=cor, fg=texto,
                           activebackground=selecionada, activeforeground=texto,
                           selectcolor=selecionada, indicatoron=False,
                           relief="raised", offrelief="raised", bd=2,
                           cursor="hand2", font=("Arial", 12, "bold"),
                           anchor="center", pady=5).pack(fill="x", pady=2)

        # command associa o clique ao método registrar, sem executá-lo agora.
        self.botao = tk.Button(self.corpo, text="Registrar resposta →", command=self.registrar,
                               bg=LARANJA, fg="white", activebackground="#A63805",
                               activeforeground="white", relief="flat", cursor="hand2",
                               font=("Arial", 13, "bold"), pady=12)
        self.botao.pack(fill="x", pady=(18, 10))
        # Reserva espaço para confirmar registros e coloca o cursor no nome.
        self.status = self.texto("", 10)
        self.nome.focus_set()

    def registrar(self):
        """Lê o formulário, registra a resposta e avança a pesquisa."""
        # get() lê os campos; se houver erro, mostra o aviso e mantém os dados
        # na tela para correção. return encerra esta tentativa de registro.
        try:
            self.pesquisa.registrar(self.nome.get(), self.idade.get(), self.opiniao.get())
        except ValueError as erro:
            messagebox.showwarning("Confira os dados", str(erro), parent=self.janela)
            return
        # Ao atingir 50 respostas válidas, substitui o formulário pelo resultado.
        quantidade = len(self.pesquisa.respostas)
        if quantidade == TOTAL_ENTREVISTADOS:
            self.exibir_resultados()
            return
        # Atualiza o progresso e indica o número do próximo entrevistado.
        self.barra["value"] = quantidade
        self.progresso_texto.config(text=f"Entrevistado {quantidade + 1} de 50 • {quantidade} respostas registradas")
        # Limpa os campos e a seleção para receber uma nova pessoa.
        self.nome.delete(0, tk.END)
        self.idade.delete(0, tk.END)
        self.opiniao.set(0)
        self.status.config(text=f"Resposta {quantidade} registrada. Próximo entrevistado!")
        # Antes da última resposta, avisa que o próximo registro abre o resultado.
        if quantidade == TOTAL_ENTREVISTADOS - 1:
            self.botao.config(text="Registrar e ver resultado →")
        self.nome.focus_set()

    def exibir_resultados(self):
        """Troca o formulário pelos totais solicitados no enunciado."""
        # Percorre e remove os elementos da área central, preservando o cabeçalho.
        for widget in self.corpo.winfo_children():
            widget.destroy()
        # Obtém os dois contadores calculados a partir das respostas armazenadas.
        excelentes, ruins = self.pesquisa.resultados()
        self.texto("Pesquisa concluída!", 24, True)
        self.texto("As 50 opiniões foram registradas. Confira o resultado do atendimento.")
        # Cria um cartão para cada total, com título, quantidade e legenda.
        for titulo, quantidade in (("EXCELENTE", excelentes), ("RUIM", ruins)):
            cartao = tk.Frame(self.corpo, bg="white", padx=24, pady=20,
                              highlightbackground="#F0D2B9", highlightthickness=1)
            cartao.pack(fill="x", pady=12)
            tk.Label(cartao, text=titulo, bg="white", fg=TEXTO,
                     font=("Arial", 12, "bold")).pack(anchor="w")
            tk.Label(cartao, text=str(quantidade), bg="white", fg=LARANJA,
                     font=("Arial", 42, "bold")).pack(anchor="w")
            tk.Label(cartao, text="respostas", bg="white", fg=TEXTO,
                     font=("Arial", 11)).pack(anchor="w")
        # Complementa os cartões com o total de participantes e a explicação de BOM.
        self.texto("Total de entrevistados: 50", 12, True)
        self.texto("As respostas BOM integram o total de entrevistados, mas não entram nas duas contagens acima.", 11)

    def fechar(self):
        """Confirma a saída quando existem respostas e encerra a janela."""
        # askyesno retorna True para Sim e False para Não.
        # Se houver respostas e a pessoa escolher Não, a janela permanece aberta.
        if self.pesquisa.respostas and not messagebox.askyesno(
            "Fechar pesquisa", "Os dados estão apenas na memória e serão perdidos ao fechar. Deseja sair?",
            parent=self.janela,
        ):
            return
        # Destrói a janela e encerra seu loop de eventos.
        self.janela.destroy()


# Inicia a interface apenas ao executar este arquivo diretamente.
# Importar suas classes em outro arquivo não abre uma janela automaticamente.
if __name__ == "__main__":
    # Cria a janela principal e monta os componentes do aplicativo nela.
    raiz = tk.Tk()
    Aplicativo(raiz)
    # O loop de eventos processa cliques e digitação até a janela ser fechada.
    # Após a 50ª resposta, ele continua ativo para exibir a tela de resultados.
    raiz.mainloop()
