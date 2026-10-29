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
| `perfil` | `preenchidos, total, rotulo`: quanto do trafego.md está preenchido |

Regras: número só do dado do usuário (regra 3 do SKILL.md); o que não foi lido fica fora ou escrito em `nota`. Sem travessão nas frases.
