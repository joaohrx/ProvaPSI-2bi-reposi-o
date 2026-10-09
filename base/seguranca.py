from flask import flash, redirect, session, url_for


def exigir_login():
  if 'usuario_id' not in session:
    flash('Não está logado')
    return redirect(url_for('auth.login'))

  else:
    return None

    # Complete esta função durante a avaliação.
    # Ela deve verificar se existe session["usuario_id"].
    # Caso não exista, redirecione para auth.login.
