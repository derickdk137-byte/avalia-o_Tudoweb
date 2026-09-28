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
