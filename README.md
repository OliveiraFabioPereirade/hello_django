# hello_django

App desenvolvido durante o curso:

### Desenvolvimento para Internet e Banco de Dados com Python e Django

![](https://i.imgur.com/fpUQOLd.png?1)

Oferecido por: 

### Digital Innovation One

Ministrado por:

### Rafael Galleani

---

## Fases do projeto:

#### Primeira fase:
- Criação de uma virtual env;
- Instalação do django nesta virtual env
- Configuração do PyCharm para rodar página padrão do django.

Procedimento descrito no arquivo: ___Cria virtual env, instala django, e configura PyCharm para rodar pagina.txt___

Ao final desta fase, é possivel ver a página http://127.0.0.1:8000/ no navegador:

![](https://i.imgur.com/QhvH6qx.png)

#### Segunda fase:
- Cria estrutura de diretório e arquivos que conterão nossa app (procedimento em ___Cria aplicacao que sera o coracao do projeto.txt___);
- Cria rota '\hello' que retornará a mensagem: "Hello World!" (procedimento em ___Cria rota hello para pagina.txt___).

Ao final desta fase, a página http://127.0.0.1:8000/ retornará erro, pois não foi criado uma rota para ela:

![](https://i.imgur.com/s2j7MHr.png)

Mas a página http://127.0.0.1:8000/hello/ retornará a mensagem esperada:

![](https://i.imgur.com/6PovUKA.png)

#### Terceira fase:
- Permite a passagem de parâmetros junto com a requisição da rota /hello/ .

Alteração identificada pelo commit  ___Permite passagem de parametros___ .

Ao final desta fase, a página http://127.0.0.1:8000/hello/ retornará erro, pois não foi criado uma rota sem parâmetros para ela:

![](https://i.imgur.com/P21npKx.png)

Mas com a passagem de parâmetro Fabio e 43, a página retornará uma mensagem personalizada:

![](https://i.imgur.com/Ij6M2LE.png)

#### Quarta fase:
- Cria rota /add/ que permite a passagem de dois números e retorna o resultado da soma deles.
- Cria rota /sub/ que permite a passagem de dois números e retorna o resultado do primeiro subtraído do segundo.
- Cria rota /mul/ que permite a passagem de dois números e retorna o resultado da multiplicação deles.
- Cria rota /div/ que permite a passagem de dois números e retorna o resultado da divisão do primeiro pelo segundo.

Alteraçao indicada pelo commit  ___Cria rotas para somar, subtrair, multiplicar ou dividir 2 numeros passados como parametro___ .

Ao final desta fase:

A página http://127.0.0.1:8000/add/ com a passagem de parâmetro 15 e 5 retornará a mensagem:

![](https://i.imgur.com/0Rd9CI5.png)

A página http://127.0.0.1:8000/sub/ com a passagem de parâmetro 15 e 5 retornará a mensagem:

![](https://i.imgur.com/ZP4MaJS.png)

A página http://127.0.0.1:8000/mul/ com a passagem de parâmetro 15 e 5 retornará a mensagem:

![](https://i.imgur.com/xeippUE.png)

A página http://127.0.0.1:8000/div/ com a passagem de parâmetro 15 e 5 retornará a mensagem:

![](https://i.imgur.com/qfSTrzi.png)
