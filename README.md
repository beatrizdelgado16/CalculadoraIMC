# Calculadora de IMC

## 📜 Descrição do Projeto
Este projeto é uma calculadora simples de **Índice de Massa Corporal (IMC)** com interface gráfica desenvolvida em **Python** usando a biblioteca **Tkinter**. A aplicação permite que o usuário insira o peso e a altura, calcule o IMC e visualize o resultado em uma interface amigável.

---

## ✅ Funcionalidades
- 💻 Interface gráfica intuitiva para entrada de peso e altura.
- ⚙️ Cálculo automático do IMC com base nos valores fornecidos.
- ⚠️ Mensagem de erro ao tentar calcular com campos vazios ou valores inválidos.

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Tkinter** (para a interface gráfica)
- **Git** (para controle de versão)

---

## 📂 Estrutura do Projeto
```plaintext
CalculadoraIMC/
│
├── README.md             # Documentação do projeto
├── main.py               # Arquivo principal para executar o programa
├── src/                  # Diretório com os arquivos do sistema
│   ├── imc_calculator.py # Lógica para o cálculo do IMC
│   ├── views.py          # Interface gráfica
│
└── .gitignore            # Arquivo para ignorar arquivos no Git
```

---

## ▶️ Como Executar o Projeto

Clone o repositório:

```bash
git clone https://github.com/beatrizdelgado16/CalculadoraIMC.git
cd CalculadoraIMC
```

Instale o Python (se ainda não estiver instalado):

- Certifique-se de ter a versão 3.x.

Execute o programa:

```bash
python main.py
```

---

## 🚧 Dificuldades Encontradas e Soluções
Durante o desenvolvimento do projeto, algumas dificuldades foram encontradas e solucionadas, conforme descrito abaixo:

1. **❌ Erro de Importação**
   - **Descrição**: O erro "ModuleNotFoundError: No module named 'src'" ocorreu ao tentar executar o programa.
   - **Solução**: Garantimos que o terminal estivesse no diretório raiz do projeto antes de executar o código. Também ajustamos os caminhos relativos nos arquivos Python.

2. **❌ Erro de Entradas Válidas**
   - **Descrição**: A interface permitia entradas vazias ou inválidas, como texto ou números negativos.
   - **Solução**: Implementamos validações nos campos de entrada para garantir que apenas números positivos fossem aceitos. Uma mensagem de erro é exibida quando entradas inválidas são detectadas.

3. **❌ Erro no Git (Identidade Não Configurada)**
   - **Descrição**: A identidade do usuário não estava configurada no Git, resultando em erros ao tentar fazer commits.
   - **Solução**: Configuramos o nome e o email do usuário com os comandos:

   ```bash
git config --global user.name "Beatriz Delgado"
git config --global user.email "beatrizdasvdelgado09@gmail.com"
```

4. **❌ Erro ao Configurar o Repositório no GitHub**
   - **Descrição**: O comando `git push` falhou devido à falta de commits iniciais ou problemas com o nome da branch.
   - **Solução**: Realizamos o primeiro commit corretamente e ajustamos a branch com o comando:

   ```bash
git branch -M main
```

5. **❌ Interface Mostrando Valor Padrão 0.00**
   - **Descrição**: O valor do IMC era exibido como 0.00 mesmo após inserir os valores de peso e altura.
   - **Solução**: Ajustamos o método que atualiza o valor na interface para exibir o resultado corretamente.

---

## 🔄 Gerenciamento com Git

### 🚀 Uso de Branches
Foi criada a branch `feature/views` para desenvolver a interface gráfica e posteriormente integrada à branch principal (`main`) após revisão.

### ✏️ Commits
Foram realizados commits frequentes com mensagens claras, como:
- "Adicionando interface gráfica com validações básicas"
- "Corrigindo erros de importação e ajustes no layout"

### 🔀 Merges
Após testar as funcionalidades em branches específicas, elas foram mescladas na branch `main` utilizando:

```bash
git checkout main
git merge feature/views
git push origin main
```

---

## 📌 Conclusão
Este projeto é um exemplo prático de como desenvolver uma aplicação com interface gráfica e usar o Git para gerenciar o controle de versão.

### ✨ Futuras Melhorias
- Adicionar categorias baseadas no valor do IMC (ex.: "Peso normal", "Sobrepeso").
- Melhorar o layout da interface gráfica com bibliotecas adicionais, como `ttk`.

