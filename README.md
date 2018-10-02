# Aula Introdutória

Boa noite. O objetivo da aula de hoje é treinar a programação em time
com controle de versão por meio do git. Leia atentamente as instruções
antes de iniciar, pois a atividade só é descrita ao final, e algumas das
instruções abaixo fazem parte do trabalho; nem todas são realizadas
antes de iniciar suas atividades.

Sempre antes de iniciar realize a configuração abaixo:

$ git config --global user.name "Seu Nome"

$ git config --global user.email "seu@email.com"

Seu objetivo hoje é baixar o repositório, criar um branch de nome
seuprimeironome-2212 e finalmente realizar alguns testes
de programação descritos no final destas instruções.

Lembre-se: para baixar o repositório:

$ git init

$ git remote add repo https://github.com/felipebastos/aulaintrodutoria

$ git pull repo master

No ponto acima você precisa lembrar seu nome de usuário e senha.


Você pode criar e editar seu arquivos normalmente na pasta, mas precisa dizer
ao git que eles farão parte do seu trabalho. Primeiro crie seu galho:

$ git branch seuprimeironome-2212

$ git checkout seuprimeironome2212

Sempre que modificar um arquivo ou adicionar um novo adicione a modificação:

$ git add nomesdosarquivos

Dê commit ao final de um trabalho:

$ git commit -m "Uma mensagem significante sobre o que você fez."

Volte ao branch master, como você está trabalhando em equipe,
pode ser necessário checar se você estava realmente modificando a
última versão do código.

$ git checkout master

$ git pull repo master

Agora que você baixou a última versão do master, faça um merge das
suas modificações. Como cada um trabalhará basicamente em um arquivo
separado, poucos conflitos são aguardados. Isso vai fazer com que
os arquivos em que você trabalhou estejam disponíveis no master também.

$ git merge seuprimeironome-2212

Agora envie as modificações ao servidor:

$ git push repo seuprimeironome-2212

Aqui também é necessário usar usuário e senha.

## Mas qual o outro objetivo da atividade?

Uma empresa contratou vocês para desenvolver uma proposta de layout para
que eles possam usar como portifólio. A empresa vende cabras. Criem um
site em conjunto que utilize as tecnologias web (HTML, CSS e JS) como
proposta de um site. Lembre-se: O site não deve conter apenas uma página,
pois além de uma página inicial, faz-se necessário uma página com a
história da empresa, outra com relatos de clientes que já compraram
cabras com eles, uma com a descrição das cabras que a empresa vende,
uma página de informações para contato, bem como uma em que é alistada
e apresentada a equipe de funcionários da empresa. O nome da empresa
é Cabras da Véia Chica.

Lembrem-se de dividir a equipe, de modo que o verdadeiro poder da
programação por meio de versões se demonstre. Talvez duas ou três
pessoas possam trabalhar em cada tarefa. Mas lembre-se: o estilo
visual deve ser pautado em um arquivo de estilos central, bem como
qualquer código javascript.
