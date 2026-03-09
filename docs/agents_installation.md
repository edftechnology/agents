# agents_installation.md

## Missão do Agente

Você é responsável por criar, modificar e manter instruções de instalação de programas no `Linux Ubuntu`, garantindo clareza, reprodutibilidade e segurança no processo.

O agente deve:

- Criar tutoriais passo a passo de instalação via **Terminal Emulator**.

- Usar comandos portáteis e compatíveis com diferentes versões do `Linux Ubuntu`.

- Verificar dependências e pacotes adicionais necessários.

- Documentar _links_ oficiais e fontes de referência.

- Registrar _links_ de consultas ao `ChatGPT` e outras fontes em **Referências**.

- Manter o _template_ do `README.ipynb`

---

## Procedimento de Exploração

### 1. Pesquisar instruções no `ChatGPT`

- Criar uma pergunta no `ChatGPT` do tipo:  
  *"Como instalar o <nome_do_projeto/repositório> (sem os underlines `_`) no `Linux Ubuntu` pelo `Terminal Emulator`?"*  

- Copiar o _link+ da resposta do `ChatGPT` para incluir na seção **Referências** do arquivo `README.ipynb`.

---

### 2. Revisar o Projeto

- Revisar todos os arquivos do projeto e alterar o nome do programa para **<nome_do_projeto/repo>** (sem os underlines `_`) conforme descrito na pesquisa/documentação.

- Não alterar os arquivos `README.md` e `README.py` usando o código em `python` chamado `convert_ipynb_to_md.py`.

- Preservar integralmente a seção: `**"2. Certifique-se de que seu sistema esteja limpo e atualizado."**`

- Revisar também os documentos-padrão do projeto:
  
  - CHANGES.txt
  
  - setup.py

---

### 3. Executar Conversão

- Rodar o _script_ de conversão para sincronizar os arquivos:

    ```bash
    python3 subs/submodules/python_scripts/convert_ipynb_to_md.py
    ```
- Caso você não encontre o arquivo `python3 convert_ipynb_to_md.py`, este converte o `README.ipynb` para `.md`. Sendo assim, se não encontrar o arquivo, faça você mesmo.

- Excluir o arquivo `README.py`, pois este não deve existir, caso ele exista.

---

### 4. Acertar código

- Para os repos que possuírem o `README.ipynb`, onde estiver:
 
    1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
 
    Alterar para:
 
    1. Abrir o `Terminal Emulator`. Você pode fazer isso pressionando:
  
        ```bash
        Ctrl + Alt + T
        ```
