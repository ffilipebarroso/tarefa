# Documentação do Programa de Lista de Tarefas
(programa criado nos fundamentos de programação funcional)

## Introdução

    O programa de lista de tarefas é uma aplicação simples desenvolvida em Python que permite ao usuário gerenciar uma lista de tarefas. Ele foi projetado para ser fácil de usar e possui uma interface gráfica básica para adicionar e remover tarefas da lista.
Funcionalidades Principais

    Adicionar Tarefa: Permite ao usuário adicionar uma nova tarefa à lista.
    Remover Tarefa: Permite ao usuário remover uma tarefa selecionada da lista.
    Visualizar Tarefas: Exibe todas as tarefas atualmente presentes na lista.

## Tecnologias Utilizadas

    O programa de lista de tarefas foi desenvolvido utilizando Python e a biblioteca Tkinter para criar a interface gráfica. Ele também faz uso de conceitos de programação funcional, como funções de ordem superior, imutabilidade e recursão.
Funcionalidades de Programação Funcional

    Funções de Ordem Superior: As funções adicionar_tarefa() e remover_tarefa() são exemplos de funções de ordem superior que aceitam outras funções como argumentos (por meio do parâmetro command dos botões) e operam sobre os dados passados para elas.

    Imutabilidade: A função adicionar_tarefa() utiliza o método delete() do widget entrada_tarefa para limpar a caixa de entrada após adicionar uma nova tarefa à lista, mantendo assim a imutabilidade dos dados.

    Recursão: Embora não seja explicitamente demonstrado neste programa, a recursão é um conceito fundamental da programação funcional. Ela é comumente usada para resolver problemas de forma recursiva, embora não seja necessária nesta aplicação específica.

## Instalação

Para executar o programa de lista de tarefas, siga estas etapas:

    Certifique-se de ter o Python instalado em seu sistema. Você pode baixar e instalar o Python a partir do site oficial.

    Clone ou faça o download deste repositório para o seu computador.

    Navegue até o diretório do projeto em seu terminal ou prompt de comando.

    Execute o seguinte comando para iniciar o programa:

    bash

    python lista_tarefas.py


**Este programa foi desenvolvido por Filipe Barroso**
