#!/usr/bin/env python3
"""
buscamercadolivre.py

Busca produtos no Mercado Livre (Brasil) via API pública e exibe
título, preço e link direto de cada resultado no terminal.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass

API_URL = "https://api.mercadolibre.com/sites/MLB/search"
USER_AGENT = "busca_ml/2.0 (+https://github.com/vdonoladev)"
TIMEOUT = 10  # segundos


@dataclass
class Produto:
    titulo: str
    preco: float
    link: str

    def formatado(self) -> str:
        preco_fmt = f"R$ {self.preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        return f"{self.titulo:<70}{preco_fmt}\n{self.link}\n"


def buscar_produtos(termo: str, limite: int) -> list[Produto]:
    """Consulta a API do Mercado Livre e retorna os produtos encontrados."""
    query = urllib.parse.urlencode({"q": termo, "limit": limite})
    url = f"{API_URL}?{query}"

    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            charset = resp.headers.get_content_charset() or "utf-8"
            dados = json.loads(resp.read().decode(charset))
    except urllib.error.HTTPError as e:
        sys.exit(f"Erro HTTP {e.code} ao consultar a API: {e.reason}")
    except urllib.error.URLError as e:
        sys.exit(f"Erro de conexão: {e.reason}")
    except json.JSONDecodeError:
        sys.exit("Erro: resposta da API não é um JSON válido.")

    resultados = dados.get("results", [])
    return [Produto(r["title"], r["price"], r["permalink"]) for r in resultados]


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="busca_ml",
        description="Busca produtos no Mercado Livre (Brasil) pelo terminal.",
    )
    parser.add_argument("produto", nargs="+", help="nome do produto a buscar")
    parser.add_argument(
        "-n", "--limit", type=int, default=10,
        help="número máximo de resultados (padrão: 10)",
    )
    parser.add_argument(
        "-o", "--ordenar", choices=["preco", "relevancia"], default="relevancia",
        help="critério de ordenação dos resultados",
    )
    args = parser.parse_args()

    termo = " ".join(args.produto)
    produtos = buscar_produtos(termo, args.limit)

    if not produtos:
        print(f'Nenhum resultado encontrado para "{termo}".')
        return

    if args.ordenar == "preco":
        produtos.sort(key=lambda p: p.preco)

    for produto in produtos:
        print(produto.formatado())


if __name__ == "__main__":
    main()