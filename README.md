## Configurando VSCode para WSL2

É necessario instalar essa extensão no vscode para que ele reconheça o WSL2:

![Screenshot extension WSL](https://drive.google.com/uc?id=1SztmoZBNTqiGPQUo6-c2TkShNVqJM6wG)

Próximo passo agora é abrir terminal no windows, e efetuar a troca para Ubuntu.

Efetue a clonagem de um repositório na pasta de preferencia e logo após execute o comando:

```sh
code nome_do_repositorio
```
Caso seu VSCode apareça a mensagem no canto inferior direito igual imagem abaixo mostra, apenas clique em "Reopen Folder in WSL"

![Screenshot Vscode](https://drive.google.com/uc?id=1UcVRGK-GwSGgiBeVnDaA_nagMvhTVMDm)

E note que na parte inferior esquerda indica que esta rodando sobre o WSL:


![Screenshot Vscode](https://drive.google.com/uc?id=1lko_Nnw3oIXlKEpMOnIU7VdGN7PTVhST)

### Erros menos comum:

Por default o WSL pode não adicionar os export no arquivo .bashrc
Para solucionar esse problema basta executar os seguintes comandos:

```sh
nano ~/.bashrc
```
Adicione seu export ao final do arquivo no editor de texto. Salve e saia do editor (Ctrl+O, Enter, Ctrl+X).

Execute o comando abaixo para aplicar as mudanças:

```sh
source ~/.bashrc
```