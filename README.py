#!/usr/bin/env python
# coding: utf-8
# # Como instalar o `kolourpaint` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Este documento apresenta os passos necessários para instalar o utilitário `kolourpaint` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document shows the steps required to install the `kolourpaint` utility on `Linux Ubuntu`._
# 
# ## Descrição
# 
# ### `kolourpaint`
# 
# O `kolourpaint` é um editor de imagens simples para ambientes `Linux`. Ele oferece ferramentas básicas de desenho, como linhas, formas e preenchimentos, sendo uma alternativa leve ao `Microsoft Paint`.
# 
# ## 1. Instalar o `kolourpaint` no `Linux Ubuntu`
# 
# Para instalar o `kolourpaint`, siga os passos abaixo:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
#     ```bash
#     sudo apt clean
#     ```
# 
#     2.2 Remover pacotes `.deb` antigos ou duplicados do `cache` local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando:
#     ```bash
#     sudo apt autoclean
#     ```
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando:
#     ```bash
#     sudo apt autoremove -y
#     ```
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`:
#     ```bash
#     sudo apt update
#     ```
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes:
#     ```bash
#     sudo apt --fix-broken install
#     ```
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt` novamente:
#     ```bash
#     sudo apt clean
#     ```
# 
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:
#     ```bash
#     sudo apt list --upgradable
#     ```
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`:
#     ```bash
#     sudo apt full-upgrade -y
#     ```
# 
# 3. Instale o `kolourpaint` e verifique a instalação:
#     ```bash
#     sudo apt update
#     sudo apt install kolourpaint
#     kolourpaint --version
#     ```
# 
# ## 2. Abrir uma imagem existente
# 
# Você pode abrir o `kolourpaint` informando um arquivo de imagem:
# ```bash
# kolourpaint ~/Imagens/exemplo.png
# ```
# Esse comando abre a interface do programa carregando a imagem `exemplo.png`.
# 
# ## 3. Usar uma variável de terminal para definir a imagem
# 
# Também é possível definir o caminho em uma variável antes de chamar o `kolourpaint`:
# ```bash
# img_path="~/Imagens/exemplo.png"
# kolourpaint "$img_path"
# ```
# 
# ## Referências
# 
# [1] OPENAI. ***Instalar kolourpaint no Linux Ubuntu***. Disponível em: <https://chatgpt.com/c/68942e26-b7a0-832f-9c96-7c57044cb43a>. ChatGPT. Acessado em: 07/08/2025 05:21.
# 
