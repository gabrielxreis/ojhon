#!/usr/bin/env python3
"""Servidor local do painel do Jhon: serve a pasta da skill só em 127.0.0.1.

Existe porque, aberto como arquivo (file://), o Chrome ignora o "baixar" dos links e abre o vídeo.
Pelo servidor, `?baixar=<nome>` responde com Content-Disposition: attachment e o arquivo vai para Downloads.

  python3 ~/.claude/skills/ojhon/painel/servidor.py [--porta 47830]
O painel.py sobe este servidor sozinho em segundo plano quando ele não está rodando.
"""
import argparse
import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, quote, urlparse

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORTA = 47830


class Painel(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=SKILL, **k)

    def end_headers(self):
        q = parse_qs(urlparse(self.path).query)
        nome = (q.get("baixar") or [None])[0]
        if nome:
            seguro = "".join(c for c in nome if c not in '\\/:*?"<>|').strip() or "video.mp4"
            self.send_header("Content-Disposition", "attachment; filename*=UTF-8''" + quote(seguro))
        if self.path.split("?")[0].endswith((".js", ".html", ".json")):
            self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *a):
        try:
            with open(os.path.join(SKILL, "painel", ".servidor.log"), "a", encoding="utf-8") as f:
                f.write(self.log_date_time_string() + " " + (fmt % a) + "\n")
        except OSError:
            pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--porta", type=int, default=PORTA)
    a = ap.parse_args()
    try:
        srv = ThreadingHTTPServer(("127.0.0.1", a.porta), Painel)
    except OSError:
        print(f"porta {a.porta} ocupada (o servidor provavelmente já está rodando)")
        return 1
    print(f"painel em http://127.0.0.1:{a.porta}/painel/index.html")
    sys.stdout.flush()
    srv.serve_forever()


if __name__ == "__main__":
    sys.exit(main())
