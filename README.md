# 🧡 Sistema de Pesquisa de Atendimento TudoWeb

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Interface-Tkinter-C74708?style=for-the-badge)
![GitHub](https://img.shields.io/badge/GitHub-Reposit%C3%B3rio-181717?style=for-the-badge&logo=github&logoColor=white)
![Atendimento](https://img.shields.io/badge/Pesquisa-Satisfa%C3%A7%C3%A3o-orange?style=for-the-badge)

## 🎯 Objetivo do sistema

O **Sistema de Pesquisa de Atendimento TudoWeb** coleta a opinião de **50 clientes** para avaliar o grau de satisfação com o atendimento prestado pela empresa de marketing TudoWeb.

Para cada entrevistado, o usuário informa:

- **Nome** do cliente.
- **Idade** em anos.
- **Opinião** sobre o atendimento: EXCELENTE, BOM ou RUIM.

A interface utiliza a cor laranja como identidade visual e apresenta uma barra de progresso. Após o registro da 50ª resposta, o sistema exibe as quantidades de avaliações **EXCELENTE** e **RUIM**.

## 🛠️ Tecnologias utilizadas

- **Python 3**: linguagem utilizada para desenvolver o programa.
- **Tkinter**: biblioteca usada para criar a interface gráfica.
- **ttk e messagebox**: componentes do Tkinter usados para a barra de progresso e as caixas de diálogo.
- **Git e GitHub**: ferramentas para versionamento e armazenamento do projeto.

## ▶️ Como executar

### 1. Verifique se o Python está instalado

No terminal, execute:

```bash
python3 --version
```

O aplicativo requer Python 3, Tkinter e um ambiente com interface gráfica. Não é necessário instalar pacotes com `pip`.

Se o Tkinter não estiver instalado no Ubuntu ou Debian, execute:

```bash
sudo apt install python3-tk
```

### 2. Execute o programa

Abra o terminal na pasta em que o arquivo do programa está salvo e execute:

```bash
python3 app.py
```

No Windows, também é possível utilizar:

```bash
python app.py
```

### 3. Responda à pesquisa

1. Digite o nome e a idade do entrevistado.
2. Selecione uma das três opções de atendimento.
3. Clique em **Registrar resposta**.
4. Repita o processo até completar os **50 entrevistados**.
5. Confira os totais apresentados na tela final.

## 📋 Regras da pesquisa

| Código | Opinião | Cor do botão | Resultado |
|---|---|---|---|
| 1 | EXCELENTE | 🟢 Verde | Contabilizada no total de respostas EXCELENTE |
| 2 | BOM | 🔵 Azul | Registrada na pesquisa, sem contagem própria na tela final |
| 3 | RUIM | 🔴 Vermelho | Contabilizada no total de respostas RUIM |

O sistema também aplica as seguintes validações:

- O nome não pode ficar vazio.
- A idade deve ser um número inteiro entre **0 e 130 anos**.
- Uma opinião deve ser selecionada antes de registrar a resposta.
- A pesquisa aceita exatamente **50 respostas** e apresenta o resultado ao concluir esse total.

As respostas ficam apenas na memória durante a execução e são perdidas ao fechar o aplicativo.

## 🔁 Estruturas de repetição

O laço **`for`** percorre as respostas armazenadas para contar as opiniões EXCELENTE e RUIM. Outros laços `for` criam os botões de opinião e os cartões de resultado.

O **`mainloop()`** do Tkinter mantém a interface ativa, processando cliques e digitação até a janela ser fechada.

## 🤝 Qualidade no atendimento

O projeto ajuda a TudoWeb a conhecer a percepção de seus clientes e identificar oportunidades de melhoria no atendimento, valorizando a opinião de cada entrevistado.

## 👤 Autor

Desenvolvido por **Derick Prado**.
