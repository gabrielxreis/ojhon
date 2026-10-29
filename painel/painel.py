#!/usr/bin/env python3
"""Painel do Jhon: junta clientes/*/painel.json em painel/dados.js e abre o painel no navegador.

Uso:
  python3 ~/.claude/skills/ojhon/painel/painel.py --cliente xtrader      # atualiza; abre só se não abriu nas últimas 6 h
  python3 ~/.claude/skills/ojhon/painel/painel.py --cliente xtrader --abrir   # força abrir uma aba
  python3 ~/.claude/skills/ojhon/painel/painel.py --cliente xtrader --nao-abrir
  python3 ~/.claude/skills/ojhon/painel/painel.py --checar                # só valida os painel.json

O formato do painel.json está em painel/LEIA.md. dados.js e os painel.json ficam fora do git.
"""
import argparse
import hashlib
import json
import time
import os
import subprocess
import sys
import webbrowser

AQUI = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(AQUI)
CLIENTES = os.path.join(SKILL, "clientes")
OBRIGATORIOS = ["cliente", "atualizado", "resumo", "campanhas", "parecer"]


def carregar():
    dados, erros = {}, []
    if not os.path.isdir(CLIENTES):
        return dados, erros
    for nome in sorted(os.listdir(CLIENTES)):
        caminho = os.path.join(CLIENTES, nome, "painel.json")
        if nome.startswith("_") or not os.path.isfile(caminho):
            continue
        try:
            with open(caminho, encoding="utf-8") as f:
                d = json.load(f)
        except Exception as e:  # noqa: BLE001
            erros.append(f"{nome}: painel.json inválido ({e})")
            continue
        falta = [k for k in OBRIGATORIOS if k not in d]
        if falta:
            erros.append(f"{nome}: falta {', '.join(falta)}")
        dados[nome] = d
    return dados, erros


def abrir(arquivo):
    url = "file://" + arquivo
    if sys.platform == "darwin":
        subprocess.run(["open", arquivo], check=False)
    elif os.name == "nt":
        os.startfile(arquivo)  # type: ignore[attr-defined]
    else:
        webbrowser.open(url)
    return url


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cliente", help="pasta do cliente em clientes/ que abre primeiro")
    ap.add_argument("--nao-abrir", action="store_true", help="só gera o dados.js")
    ap.add_argument("--abrir", action="store_true", help="abre uma aba mesmo que já tenha aberto há pouco")
    ap.add_argument("--checar", action="store_true", help="só valida os painel.json")
    a = ap.parse_args()

    dados, erros = carregar()
    for e in erros:
        print("AVISO:", e)
    if a.checar:
        print(f"{len(dados)} painel(is) lido(s)")
        return 1 if erros else 0
    if not dados:
        print("SEM_DADOS: nenhum clientes/<nome>/painel.json. Monte um pelo modelo clientes/_exemplo/painel.json.")
        return 1
    atual = a.cliente if a.cliente in dados else max(dados, key=lambda k: dados[k].get("atualizado", ""))
    if a.cliente and a.cliente not in dados:
        print(f"AVISO: {a.cliente} sem painel.json; abrindo {atual}")

    corpo = json.dumps(dados, ensure_ascii=False, sort_keys=True)
    versao = hashlib.sha1((corpo + atual).encode("utf-8")).hexdigest()[:12]
    js = ("window.JHON_DADOS = " + corpo + ";\nwindow.JHON_ATUAL = " + json.dumps(atual)
          + ";\nwindow.JHON_VERSAO = " + json.dumps(versao) + ";\n")
    with open(os.path.join(AQUI, "dados.js"), "w", encoding="utf-8") as f:
        f.write(js)

    index = os.path.join(AQUI, "index.html")
    marca = os.path.join(AQUI, ".aberto")
    recente = os.path.isfile(marca) and time.time() - os.path.getmtime(marca) < 6 * 3600
    if a.nao_abrir:
        print("PAINEL_PRONTO: file://" + index)
    elif recente and not a.abrir:
        print("PAINEL_ATUALIZADO: a aba aberta recarrega sozinha em poucos segundos (file://" + index + ")")
    else:
        print("PAINEL_ABERTO: " + abrir(index))
        with open(marca, "w") as f:
            f.write(str(time.time()))
    print(f"cliente: {atual} | clientes no painel: {', '.join(dados)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
