# Painel do Jhon

O Jhon mostra todo insight e resultado aqui: um painel local no navegador (layout de dashboard: barra lateral, seletor de cliente, busca ⌘K, Exportar CSV, abas Visão geral / Campanhas / Criativos / Parecer).

## Como abrir
```
python3 ~/.claude/skills/ojhon/painel/painel.py --cliente <pasta do cliente>
```
Junta `clientes/*/painel.json` em `painel/dados.js` (fora do git) e abre `painel/index.html`. O seletor do topo troca de cliente. A primeira abertura baixa o mapa (precisa de internet; depois fica no navegador).

## clientes/<cliente>/painel.json (fora do git)
Modelo completo: `clientes/_exemplo/painel.json`. Campos:

| Campo | O que é |
|---|---|
| `cliente` | `id, nome, conta, conta_id, handle, iniciais, plataforma` |
| `atualizado`, `fonte` | data da leitura (AAAA-MM-DD) e de onde vieram os números |
| `periodo` | `rotulo, de, ate` |
| `plataformas` | `[{nome, ativo}]`: Meta Ads, Google Ads, TikTok Ads, YouTube... |
| `manchete` | uma frase com a conclusão (faixa azul do topo) |
| `resumo` | `titulo, subtitulo, comparacao, kpis[]`; cada KPI: `rotulo, valor, anterior, formato (brl, brl0, num, pct, comp), melhor (maior, menor, neutro), nota` |
| `serie` | `titulo, subtitulo, nota, linhas[{campo, rotulo}]` (2 linhas), `extra[{campo, rotulo, formato}]` (só no tooltip), `pontos[{mes: "AAAA-MM", ...}]` |
| `geo` | `titulo, subtitulo, nota, pontos[{rotulo, lat, lon, valor (0-1) ou texto}]` |
| `distribuicao` | `titulo, subtitulo, campo` (coluna das campanhas que agrupa o investimento, padrão `grupo`) |
| `campanhas` | `[{id, campanha, grupo, quando, resultado_tipo, resultados, custo_por_resultado, gasto, cpm, cliques_link, alcance, frequencia, orcamento_dia, parecer (bom, atenção, ruim), porque}]` |
| `parecer` | `bom[], ruim[], fazer[], lacunas[]` (frases do Jhon) |
| `oferta` | `produto, preco, fonte, cpa_alvo, vendas_semana, taxa_pct`: valores iniciais da área Verba |
| `testes`, `testes_regra` | `[{nome, angulo, gancho, duracao, status}]` e a regra de pausa e vitória |
| `concorrentes` | `[{anunciante, categoria, id, desde (AAAA-MM-DD), versoes, texto, link}]`: o `link` é `https://www.facebook.com/ads/library/?id=<id>` e o botão ▶ abre o anúncio numa janela de player direto do site do Meta (nada é baixado; o endereço do vídeo do Meta expira e não é guardado) |
| `concorrentes_resumo`, `concorrentes_insights`, `concorrentes_fonte` | uma linha por anunciante (`anunciante, categoria, anuncios_lidos, desde, leitura`), as leituras do Jhon e de onde veio |
| `totais` | `cpm` e outros totais da conta: a ficha da campanha compara com eles |
| `perfil` | `preenchidos, total, rotulo`: quanto do trafego.md está preenchido |

Clicar numa campanha (tabela ou Criativos) abre a ficha dela: números, comparação com as do mesmo tipo e com a média da conta, parecer e o comando para pedir ao Jhon uma análise só dela.

Regras: número só do dado do usuário (regra 3 do SKILL.md); o que não foi lido fica fora ou escrito em `nota`. Sem travessão nas frases.
