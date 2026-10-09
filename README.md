# Justificativa

## 1.
A rota de leitura deve ficar em leituras.py ao invés de app.py para garantir a modularização da aplicação, separando funcionalidades de acordo com o modelo MVC. Em app.py deve estar apenas os registros dos blueprints.

## 2.
A aplicação identifica o usuário logado por meio do ID do usuário, que agora é verificado em todas as funcionalidades de CRUD e Banco de Dados.

## 3.
Por meio da verificação de ID do usuário da sessão e por meio do bloqueio aplicado em seguranca.py, que igualmente verifica se o ID do usuário está na sessão.