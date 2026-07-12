# busca-mercado-livre

Script em Python para buscar produtos no **Mercado Livre (Brasil)** diretamente pelo terminal, usando a API pública do Mercado Livre. Sem dependências externas — só biblioteca padrão.

## Funcionalidades

- Busca por qualquer termo de produto
- Exibe título, preço formatado em R$ e link direto do anúncio
- Limite de resultados configurável
- Ordenação por relevância ou por preço
- Tratamento de erros de rede e de resposta da API

## Requisitos

- Python 3.10+ (usa `list[Produto]` de tipagem nativa)

Nenhuma dependência de terceiros é necessária.

## Instalação

```bash
git clone https://github.com/vdonoladev/busca-mercado-livre.git
cd busca-mercado-livre
chmod +x buscamercadolivre.py
```

## Uso

```bash
python3 buscamercadolivre.py "PRODUTO"
```

### Exemplos

```bash
# Busca simples
python3 buscamercadolivre.py teclado mecânico

# Limitar a 5 resultados
python3 buscamercadolivre.py -n 5 "notebook gamer"

# Ordenar por menor preço
python3 buscamercadolivre.py -o preco "mouse sem fio"
```

### Opções

| Opção            | Descrição                                          | Padrão       |
|------------------|-----------------------------------------------------|--------------|
| `-n`, `--limit`  | Número máximo de resultados                          | `10`         |
| `-o`, `--ordenar`| Critério de ordenação (`relevancia` ou `preco`)      | `relevancia` |
| `-h`, `--help`   | Exibe a ajuda                                         | —            |

## Exemplo de saída

```
Teclado Mecânico Gamer RGB Switch Blue                              R$ 189,90
https://produto.mercadolivre.com.br/MLB-...

Teclado Mecânico Sem Fio Bluetooth                                  R$ 249,00
https://produto.mercadolivre.com.br/MLB-...
```

## Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.