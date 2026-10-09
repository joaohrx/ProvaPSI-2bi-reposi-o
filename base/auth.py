from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

import database


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]
        senha_hash = generate_password_hash(senha)
        email_ja_existe = database.buscar_usuario_por_email(email) 

        if not email_ja_existe and nome and senha_hash:
            database.criar_usuario(nome, email, senha_hash)
            return redirect(url_for("auth.login"))

        else:
            flash("Cadastro inválido.")
            return redirect(url_for("auth.registro"))

    return render_template("registro.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        usuario = database.buscar_usuario_por_email(email=email)

        if usuario and check_password_hash(usuario.senha_hash, senha):
            session["usuario_id"] = usuario.id
            session["usuario_nome"] = usuario.nome
            return redirect(url_for("leituras.index"))


        flash("Complete o login usando check_password_hash e session.")
        return redirect(url_for("auth.login"))

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Você saiu!")
    return redirect(url_for("auth.login"))
