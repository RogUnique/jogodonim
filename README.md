# Jogo Do Nim Ultimate

<H2> Apresentação</H2>

Olá Dev me chamo Roger Lemos e seja bem-vindo ao meu primeiro "Grande Projeto" em programação e 100% em Python.

<h4>O que é o Jogo do Nim?</h4>

O jogo do Nim classico é um Jogo de mesa onde dois jogadores escolhem quantas pedras(peças) irão dispor sobre o tabuleiro e quantas delas poderão ser retiradas por jogada.
Vence quem retirar a ultima peça.
Quem começa geralmente leva vantagem pois dita o ritmo do jogo.

<h2>Qual a razão do projeto?</h2>
 
 O projeto nasceu como uma atividade do  curso <a href="https://www.coursera.org/learn/ciencia-computacao-python-conceitos">"Introdução à Ciência da Computação com Python Parte 1"</a> 
 que está presente no Coursera de forma gratuita. O Jogo do Nim é apresentado como um desafio na semana 6 e uma atividade necessaria para proseguir para a próxima semana. O desafio era criar 
 um Jogo do Nim que você jogasse contra a máquina e  ela sempre vencesse.A máquina decide quem começa dependendo do número de peças na mesa e dita suas jogadas seguintes usando a mesma lógica.
 Este era o desafio, realmente cumpriu seu papel e se não fosse os ajudantes do fórum eu não teria conseguido. Então fica aqui meu agradecimento.
 
 <h3>Espremendo o limão até o fim</h3>

Passado o quase trauma do desafio decidi dar uma olhada no código e ir adicionando algumas coisinhas ali, outras aqui...E quando vi tava imerso no projeto colocando todo tempo que eu tinha e o que eu não tinha nele.
Esse fenonemo eu acho que acontece com todos os programadores e eu chamo de "Espremando o limão até a ultima gota" pois você aplica tudo que sabe e aprende novas coisas para elevar um projeto ao seu potencial máximo.
<h4>Dilema do momento certo</h4>
E eu estava 100% dentro desse fenomeno, o que estava adiando a postagem dele aqui no GitHub pois entrei naquela de "Irei postar só quando tiver: isso, aquilo...infinito" então hoje encerro este dilema e mostro ao mundo 
este meu filho.

<H1> Jogo Do Nim Ultimate</h1>
Agora bora explicar como é a versão <strike>esprimida</strike> Ultimate do Jogo do Nim.

<h2> Sobre o Jogo </H2>

<h3>Modos</h3>

O jogo possuí dois modos: Jogador vs Jogador e Jogador vs Máquina.

<h3> Modalidades </h3>

Após escolher o adversário você poderá escolher entre duas modalidades: Partida e Campeonato(3 partidas)

<h3> Jogador Vs Máquina</h3>

O modo Jogador vs Máquina agora conta com 4 opções de dificuldaes: Fácil, Médio, Díficil e Impóssivel.

<h3> Decidindo quem começa </h3>

Para decidir quem começa em ambos modos é realizado um Impar X Par. 

Quem vencer começa e quem perder escolhe o número de peças na mesa e o máximo a ser retirado.

<H2>Um caso de estudo muito divertido </h2>
Este jogo foi muito importante para o meu desenvolvimento como programador pois reforcei vários conceitos chaves. Os quais irei falar abertamente no meu blog em momento oportuno. Agora deixo meu agradecimento final aos responsaveis 
pelo curso <a href="https://www.coursera.org/learn/ciencia-computacao-python-conceitos">"Introdução à Ciência da Computação com Python Parte 1"</a> e minha dica final pra quem tá começando é estude e PRATIQUE faça projetos que te enolva assim você aprenderá muito mais do que pode imaginar agora.
E no final compartilhe com os outros para receber Feedback e inspirar.

<!-- The grid: four columns -->
<div class="row">
  <div class="column">
    <img src="img_nature.jpg" alt="" onclick="myFunction(this);">
  </div>
  <div class="column">
    <img src="img_snow.jpg" alt="" onclick="myFunction(this);">
  </div>
  <div class="column">
    <img src="img_mountains.jpg" alt="" onclick="myFunction(this);">
  </div>
  <div class="column">
    <img src="img_lights.jpg" alt="" onclick="myFunction(this);">
  </div>
</div>

<!-- The expanding image container -->
<div class="container">
  <!-- Close the image -->
  <span onclick="this.parentElement.style.display='none'" class="closebtn">&times;</span>

  <!-- Expanded image -->
  <img id="expandedImg" style="width:100%">

  <!-- Image text -->
  <div id="imgtext"></div>
</div>


 
