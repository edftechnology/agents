# agents_installation.md

## Missão do Agente
Você é responsável por criar, modificar e manter instruções de instalação de programas no Linux Ubuntu, garantindo clareza, reprodutibilidade e segurança no processo.

O agente deve:
- Criar tutoriais passo a passo de instalação via **Terminal Emulator**.
- Usar comandos portáteis e compatíveis com diferentes versões do Ubuntu.
- Verificar dependências e pacotes adicionais necessários.
- Documentar links oficiais e fontes de referência.
- Registrar links de consultas ao ChatGPT e outras fontes em **Referências**.

---

## Procedimento de Exploração

### 1. Pesquisar instruções no ChatGPT
- Criar uma pergunta no ChatGPT do tipo:  
  *"Como instalar o <nome_do_projeto/repositório> (sem os underlines `_`) no Linux Ubuntu?"*  
- Copiar o link da resposta do ChatGPT para incluir na seção **Referências** do arquivo `README.ipynb`.

---

### 2. Revisar o Projeto
- Revisar todos os arquivos do projeto e alterar o nome do programa para **<nome_do_projeto/repo>** (sem os underlines `_`) conforme descrito na pesquisa/documentação.
- Não alterar os arquivos `README.md` e `README.py`.
- Preservar integralmente a seção:  
  **"2. Certifique-se de que seu sistema esteja limpo e atualizado."**

---

### 3. Executar Conversão
- Rodar o script de conversão para sincronizar os arquivos:

```bash
python3 convert_ipynb_to_md_and_py.py
```
- Caso você não encontre o arquivo `python3 convert_ipynb_to_md_and_py.py`, este converte o `README.ipynb` para `.md`. Sendo assim, se não encontrar o arquivo, faça você mesmo.