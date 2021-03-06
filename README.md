# coodesh-q-a-challenge-20211029

# Automação Plataforma Coodesh
Scripts para a criação de um novo cadastro no site da Coodesh, realização de login e busca de vagas abertas de uma empresa. Foram utilizadas as soluções Selenium, Python e Behave (Cucumber).

## Instalação & Uso (Windows)
- **Necessário o uso do Python3 para execução do teste**

- Faça o download e instale  a última versão do [Python3](https://www.python.org/downloads/)
- Configure o Python3 no Path do sistema operacional (https://medium.com/@victorromariopazdejesus/python-3-configurando-vari%C3%A1veis-de-ambiente-no-windows-10-63059c7192e6)
- Instale o [Selenium Webdriver](https://tecnoguia.istocks.club/como-instalar-o-selenium-webdriver-em-qualquer-computador-com-python/2021-03-08/) executanto o comando no terminal `pip install -U selenium`.
- Instale o Behave(Cucumber) no terminal `pip install behave`.
- Instale o Nose `pip install nose`
- Faça download do [Chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=89.0.4389.23/) e configure ele no Path do sistema operacional (https://tecnoguia.istocks.club/como-instalar-o-selenium-webdriver-em-qualquer-computador-com-python/2021-03-08/) 
- Faça download e instale o [Google Chrome]( https://www.google.com/chrome/browser/desktop/index.html).

## Estrutura do projeto 

```bash
   |-- feature/                                      
   |    |-- page/                                # Pasta com as funções que interagem com as páginas da plataforma                                
   |    |-- steps/                               # Ordem de execução dos cenários de testes e chamadas das funções que se encontram na pasta 'page'
   |    |-- tests/                               # Diretório com os cenários escritos em Gherkin
   |    |-- support/                             # Diretório com arquivos adicionais que suportam as avaliação
        |-- browser.py                           # Comandos para utilização do browser(Chrome)
        |-- environment.py                       # Realiza a execução dos comandos definidos no arquivo browser.py
   |-- ************************************************************************
```

<br />
