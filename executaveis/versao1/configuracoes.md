### Data da geração do executável

22/02/2023 às 19:26

---

### Configurações para a geração do executável

Utilização do pyinstaller [v4.3] no terminal de um ambiente virtual criado especificamente para isso no PyCharm [v2020.1.5] contendo os mesmos arquivos do ambiente virtual original

---

### Comando utilizado para a geração do executável

pyinstaller --onefile --icon=design/icone/utilizaveis/bug.ico --add-data "bug_invertido.ico;." main.py

---

### Descrição da versão

Utiliza uma interface gráfica estilizada para configurar a exibição de um padrão de caracteres como um desenho em um terminal de comandos

Através de Caixas de Entrada e Botões de Ajustes o usuário pode configurar os seguintes aspectos:
* O tamanho de cada linha
* A quantidade de caracteres em cada linha
* A frequência de alternância entre o caracter padrão e o caracter especial
* O caracter utilizado como caracter padrão
* O caracter utilizado como caracter especial
* A velocidade com a qual as linhas são impressas

Através dos Botões Principais o usuário pode executar as seguintes ações:
* Exibir o desenho resultado dos ajustes escolhidos
* Limpar o terminal para não haver interferência em novos desenhos

Nota: Para estimular a criatividade e apresentar o funcionamento do programa para novos usuários, o código conta com valores padrões que são carregados na inicialização e podem ser utilizados como teste.