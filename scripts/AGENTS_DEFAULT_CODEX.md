# AGENTS - Guia Mestre

Este arquivo serve como índice central para as instruções específicas de cada agente.  
Cada agente possui seu próprio arquivo dedicado, que **não é mesclado** aqui, para permitir edição independente.

---

## Regras Mandatórias

- **LaTeX**: **NUNCA** use a estrutura `\ifdefined\mainfile`. Todos os arquivos `.tex` devem seguir o template padrão com `\documentclass`, `\input{preamble.tex}`, `\input{variables.tex}`, `\begin{document}` e `\end{document}`.
- **Identificadores**: Nomes de funções, variáveis e identificadores devem ser **SEMPRE** em inglês (EUA).

---

## Estrutura

- `docs/AGENTS_git.md` → Instruções e fluxos de trabalho para Git, GitHub e GitLab  
- `docs/AGENTS_latex.md` → Instruções e padrões para documentos LaTeX  
- `docs/AGENTS_python.md` → Instruções para Python, PEP8, Sphinx e formatação de código

---

## Como usar no ChatGPT Codex

No **ChatGPT Codex** (ou outra instância), você pode pedir para o modelo considerar **somente** uma seção ou arquivo específico, por exemplo:

> "Use apenas as instruções do arquivo `docs/AGENTS_python.md`"  
> "Considere as instruções do `docs/AGENTS_git.md` para revisar este commit"

---

## Leitura para Instruções Externas

- [AGENTS_git.md](docs/AGENTS_git.md)  
- [AGENTS_latex.md](docs/AGENTS_latex.md)  
- [AGENTS_python.md](docs/AGENTS_python.md)

---

> **Nota:** Cada arquivo é independente e pode ser atualizado separadamente.  
> O `AGENTS.md` serve apenas como guia/índice mestre.
