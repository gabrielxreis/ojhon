<div align="center">

[![/ojhon](.github/banner.svg)](#readme)

[![Último commit](https://img.shields.io/github/last-commit/gabrielxreis/ojhon?color=2F6BFF&label=atualizado&style=for-the-badge)](https://github.com/gabrielxreis/ojhon/commits/main "Histórico")
[![Claude Code](https://img.shields.io/badge/Claude_Code-skill-D97757.svg?style=for-the-badge&logo=anthropic&logoColor=white)](https://claude.com/claude-code "Claude Code")
[![Painel](https://img.shields.io/badge/-painel_no_navegador-2F6BFF.svg?style=for-the-badge)](#painel "Painel")
[![Meta Ads](https://img.shields.io/badge/Meta_Ads-MCP_oficial-0467DF.svg?style=for-the-badge&logo=meta&logoColor=white)](#conectores "Conectores")
[![Google Ads](https://img.shields.io/badge/Google_Ads-auditoria-4285F4.svg?style=for-the-badge&logo=googleads&logoColor=white)](#o-que-o-jhon-faz "O que o Jhon faz")
[![12 plataformas](https://img.shields.io/badge/-12_plataformas-1E3FD8.svg?style=for-the-badge)](#o-que-o-jhon-faz "Plataformas")
[![/ogab](https://img.shields.io/badge/-ponte_com_o_/ogab-2BFF88.svg?style=for-the-badge&logoColor=black)](#ponte-com-o-gab "Ponte com o Gab")
[![macOS](https://img.shields.io/badge/-macOS-lightblue.svg?style=for-the-badge&logo=apple&logoColor=black)](#instalacao "Instalação")
[![Licença: MIT](https://img.shields.io/badge/-MIT-red.svg?style=for-the-badge)](LICENSE "Licença")

</div>

**/ojhon** (o Jhon) é uma skill do Claude Code que faz o trabalho de **gestor de tráfego**: lê a sua conta de anúncio, audita 12 plataformas, monta plano de mídia e verba, calcula CPA, ROAS e MER, cria e audita criativo e copy, olha os anúncios dos concorrentes, acha verba jogada fora, confere rastreamento (Pixel, CAPI, GA4, UTM) e landing page, desenha teste A/B e escreve o relatório para o cliente. **Todo resultado abre num painel no navegador.** Quando o anúncio é em **vídeo**, o Jhon faz o brief, o **Gab ([/ogab](https://github.com/gabrielxreis/ogab))** edita e o Jhon audita o vídeo antes de subir.

> **Nada muda na sua conta de anúncio sem o seu "pode".** Publicar, pausar, apagar, trocar verba, lance ou público: o Jhon monta a proposta e para. Cada aprovação vale para uma ação só.

> **Cada pessoa usa as PRÓPRIAS contas.** A skill não traz conta, chave nem login. Os dados entram pelos conectores que você mesmo liga no seu Claude (como o MCP oficial do Meta Ads) ou por export (CSV, print, planilha).

* [NOVIDADES](#novidades)
* [INSTALAÇÃO](#instalacao)
    * [Primeiro uso](#primeiro-uso-leia-isto)
    * [Um comando](#um-comando)
    * [Passo a passo manual](#passo-a-passo-manual)
    * [Atualizar](#atualizar)
    * [Requisitos](#requisitos)
* [CONECTORES](#conectores)
* [PAINEL](#painel)
* [USO E COMANDOS](#uso-e-comandos)
    * [Comandos](#comandos)
    * [O que o Jhon faz](#o-que-o-jhon-faz)
    * [O fluxo](#o-fluxo)
* [PONTE COM O GAB](#ponte-com-o-gab)
* [CLIENTES](#clientes)
* [ID DO JHON](#id-do-jhon)
* [SEGURANÇA](#seguranca)
* [MOTORES](#motores)
* [ESTRUTURA DO REPOSITÓRIO](#estrutura-do-repositorio)
* [LICENÇA](#licenca)


# NOVIDADES

O Jhon se atualiza sozinho toda vez que você usa e **mostra o que mudou** logo no começo da conversa. Histórico completo em [`CHANGELOG.md`](CHANGELOG.md). Últimas:

- **Ficha da campanha e player de concorrentes:** clique numa campanha para ver tudo só sobre ela; assista os anúncios da concorrência direto da Biblioteca do Meta.
- **Painel no navegador:** todo insight ou resultado abre um painel local com resumo, evolução da conta, mapa de entrega, investimento por tipo, parecer do Jhon, tabela de campanhas, plano de verba, testes de criativo e concorrentes. Tema claro e escuro, e funciona em qualquer tamanho de tela.
- **MCP oficial do Meta Ads:** conecte `https://mcp.facebook.com/ads` e o Jhon lê a conta direto, sem export.
- **ID própria:** azul elétrico, na mesma família visual do /ogab.
- **claude-ads v2.1.0:** auditoria do Google sem contar palavra-chave negativa como ativa, fonte vencida reprovada, dependências seguras.
- **Concorrentes de verdade:** a Biblioteca de Anúncios do Meta pelo MCP opcional (sem token).
- **Ponte com o Gab:** brief do anúncio, edição no /ogab e auditoria do criativo antes de subir.

# INSTALAÇÃO

[![Instalar no macOS](https://img.shields.io/badge/-Instalar_no_macOS-lightblue.svg?style=for-the-badge&logo=apple&logoColor=black)](#um-comando)
[![install.sh](https://img.shields.io/badge/-install.sh-grey.svg?style=for-the-badge&logo=gnubash&logoColor=white)](install.sh)
[![claude-ads](https://img.shields.io/badge/-claude--ads_v2.1.0-6E40C9.svg?style=for-the-badge)](https://github.com/AgriciDaniel/claude-ads)
[![marketing-skills](https://img.shields.io/badge/-marketing--skills-orange.svg?style=for-the-badge)](https://github.com/irinabuht12-oss/marketing-skills)

## Primeiro uso (leia isto)

Depois de instalar, abra o Claude Code e digite **`/ojhon ajuda`**. Depois:
- **Conecte a conta (recomendado):** no Claude, **Configurações > Conectores > Adicionar conector personalizado**, cole `https://mcp.facebook.com/ads`, entre com a conta dona dos anúncios e reinicie o Claude Code. Sem conector, tudo funciona com export.
- **Cadastre o cliente:** `/ojhon cliente <nome>`. O Jhon pergunta plataformas, objetivo, meta (CPA, ROAS, CPL), verba e ticket, e guarda em `clientes/<nome>/trafego.md`. A marca (tom, público, o que não dizer) vem do mesmo perfil do Gab.
- **Peça:** `/ojhon auditoria`, `/ojhon por que o CPA subiu?`, `/ojhon plano de mídia de R$ 5 mil`, `/ojhon 4 ganchos para o anúncio X`.
- **O que você recebe:** o painel aberto no navegador e, na conversa, o que foi feito, as 1 a 3 ações de maior impacto (com o valor em jogo) e o que depende de você.

## Um comando

Cole no **Terminal** do Mac:

```bash
curl -fsSL https://raw.githubusercontent.com/gabrielxreis/ojhon/main/install.sh | bash
```

O [install.sh](install.sh) pode ser rodado de novo para atualizar. Ele:
- baixa a skill em `~/.claude/skills/ojhon` e cria o seu `config.json`;
- instala o motor **claude-ads** a partir da cópia em `vendor/claude-ads` (skill `/ads`, sub-skills `ads-*` e os agentes `audit-*` em `~/.claude/agents`);
- usa um **Python de 3.10 a 3.13** para as dependências do claude-ads (fixadas por hash, num ambiente isolado, sem misturar com pacotes soltos do seu Python). Sem esse Python, instala só as skills e avisa;
- confere os 49 playbooks, o `/ads` e os agentes.

## Passo a passo manual

1. **Clonar na pasta de skills do Claude:**
   ```bash
   git clone https://github.com/gabrielxreis/ojhon ~/.claude/skills/ojhon
   ```
2. **Criar a sua configuração** (fica só na sua máquina):
   ```bash
   cp ~/.claude/skills/ojhon/config.example.json ~/.claude/skills/ojhon/config.json
   ```
3. **Instalar o motor claude-ads:**
   ```bash
   bash ~/.claude/skills/ojhon/install.sh --so-ads
   ```
4. **(Opcional) Python 3.12** para as partes com script do claude-ads (print de site, análise de landing, PDF, imagem):
   ```bash
   brew install python@3.12
   ```
5. **(Recomendado) Conectores:** veja [CONECTORES](#conectores).

## Atualizar

A skill faz `git pull` sozinha toda vez que é usada (sem tocar no seu `config.json` nem em `clientes/`) e mostra as novidades. Para forçar:

```
/ojhon update
```

## Requisitos

| | Mínimo | Observação |
|---|---|---|
| Sistema | macOS | O claude-ads também roda no Windows (`vendor/claude-ads/install.ps1`) |
| Claude Code | qualquer recente | |
| Navegador | qualquer | O painel abre como arquivo local; o mapa baixa uma vez da internet |
| Python | 3.10 a 3.13 (opcional) | Só para print de site, análise de landing, PDF e imagem do claude-ads |
| Dados | conector ou export | MCP do Meta Ads, CSV, print ou planilha; o Jhon nunca digita senha |
| /ogab | opcional | Para os anúncios em vídeo (ponte com o Gab) |


# CONECTORES

Todos só de leitura: o Jhon lê e propõe, nunca muda a conta sem o seu "pode".

| Conector | O que dá ao Jhon | Como ligar |
|---|---|---|
| **Meta Ads (oficial)** `https://mcp.facebook.com/ads` | gasto, resultado, CPM, CTR, frequência, públicos e criativos, com detalhe por dia, mês, idade, região e posicionamento | **Recomendado.** Configurações > Conectores > Adicionar conector personalizado, colar o endereço, entrar com a conta dona dos anúncios e reiniciar o Claude Code |
| **Biblioteca de Anúncios** ([facebook-ads-library-mcp](https://github.com/RamsesAguirre777/facebook-ads-library-mcp)) | anúncios ativos dos concorrentes no Facebook e Instagram, em qualquer país, sem token | opcional, instalado à parte (`claude mcp add facebook-ads ...`); o Jhon busca sempre com `country="BR"` |
| **Hotmart** | venda real, reembolso e assinatura, para ROAS e CAC de verdade | o conector da Hotmart no Claude; o Jhon usa só as consultas, nunca reembolso, cancelamento ou cupom |
| **Sem conector** | o Gerenciador pelo seu navegador, ou export | CSV, print ou planilha |


# PAINEL

Todo insight ou resultado do Jhon (leitura de conta, auditoria, relatório, teste) abre um **painel local no navegador**:

```bash
python3 ~/.claude/skills/ojhon/painel/painel.py --cliente <cliente>
```

| Área | O que mostra |
|---|---|
| **Visão geral** | conclusão do Jhon numa frase, resumo com variação contra o período anterior (verde quando melhora, vermelho quando piora), mapa de entrega, evolução da conta por mês com tooltip e investimento por tipo de campanha |
| **Campanhas** | tabela que ordena e busca (⌘K), com o selo bom, atenção ou ruim e o motivo; **clique numa campanha** e abre a ficha só dela (números, comparação com as do mesmo tipo e com a média da conta, parecer); **Exportar** baixa o CSV |
| **Criativos** | custo por resultado de cada criativo, do mais barato ao mais caro |
| **Parecer** | o que está bom, o que está ruim, o que fazer primeiro e o que falta você responder |
| **Verba** | calculadora: preço, custo por venda alvo, vendas por semana e taxa viram verba por semana e por mês, retorno, sobra e ponto de empate, com cenários |
| **Testes** | os criativos em teste, com gancho, ângulo e status |
| **Concorrentes** | o que a concorrência anuncia agora, resumo por anunciante, há quantos dias cada anúncio está no ar e o **player**: o botão ▶ abre o vídeo direto da Biblioteca de Anúncios do Meta, sem baixar nada |

- **Sempre em dia:** todo comando do /ojhon atualiza o painel; a aba aberta se atualiza sozinha em poucos segundos, sem abrir aba nova.
- **Vários clientes:** o seletor do topo troca de cliente.
- **Menu lateral:** fica completo em tela grande, vira trilho de ícones em tela média e gaveta no celular. Também dá para recolher manualmente.
- **Tema claro e escuro:** segue o sistema, e o botão de sol e lua no topo guarda a sua escolha.
- **Seus dados:** cada cliente tem um `clientes/<cliente>/painel.json` (formato em [`painel/LEIA.md`](painel/LEIA.md), modelo em [`clientes/_exemplo/painel.json`](clientes/_exemplo/painel.json)). Os dados ficam só na sua máquina, fora do git.


# USO E COMANDOS

## Comandos

No Claude Code, chame com `/ojhon` seguido do pedido, ou só peça em linguagem normal:

| Comando | O que faz |
|---|---|
| `/ojhon <pedido>` | Qualquer trabalho de tráfego; o Jhon escolhe o motor |
| `/ojhon painel [cliente]` | Abre o painel do cliente no navegador |
| `/ojhon cliente <nome>` | Cria ou atualiza o perfil de tráfego do cliente |
| `/ojhon auditoria [cliente] [plataforma]` | Auditoria completa ou de uma plataforma |
| `/ojhon plano [cliente]` | Plano de mídia: objetivo, verba, estrutura, criativo, medição, testes |
| `/ojhon criativo [cliente]` | Ganchos, copy e brief; anúncio em vídeo vai para o Gab |
| `/ojhon concorrente [cliente]` | Biblioteca de anúncios, mensagens, formatos e brechas dos concorrentes |
| `/ojhon relatorio [cliente]` | Resumo da semana e a narrativa do relatório para o cliente |
| `/ojhon ajuda` | O que está instalado e os clientes cadastrados |
| `/ojhon doctor` | Confere o claude-ads, os agentes, as dependências, os playbooks, os conectores e o painel |
| `/ojhon update` | Atualiza a skill |

## O que o Jhon faz

| Área | Exemplos de pedido |
|---|---|
| **Leitura da conta** | gasto por mês, o que vendeu, o que só gerou seguidor, CPM subindo, campanhas paradas |
| **Auditoria** | Google, Meta, YouTube, TikTok, LinkedIn, Microsoft, Amazon, Apple, Reddit, Pinterest, Snapchat e X: achados com evidência e riscos |
| **Diagnóstico** | "o CPA subiu", anomalias, verba jogada fora, termos de busca, canibalização de palavra-chave, fadiga de criativo |
| **Plano e verba** | plano de mídia, verba para bater a meta de vendas por semana, divisão entre canais, previsão de ROAS, contas de CPA, MER, LTV:CAC |
| **Criativo** | ganchos e variações de copy para teste, brief de campanha, auditoria de criativo, reaproveitar um conteúdo em vários formatos |
| **Concorrentes** | Biblioteca de Anúncios do Meta e transparência do Google, posicionamento, landing pages deles |
| **Público** | sobreposição de públicos, frequência, janela de retargeting, perfil de cliente ideal |
| **Rastreamento** | Pixel, CAPI, GA4, atribuição, rastreamento server-side, UTM |
| **Landing page** | coerência entre anúncio e página, conversão, celular, formulário |
| **Testes** | desenho do teste A/B, tamanho de amostra, quando declarar vencedor |
| **Relatório** | resumo da semana e o texto executivo do relatório |
| **SEO e IA** | SEO completo, SEO programático, visibilidade da marca nas respostas do ChatGPT, Claude, Gemini e Perplexity |

## O fluxo

1. **Cliente:** lê a marca (perfil do Gab) e o `trafego.md` (meta, verba, preço, histórico).
2. **Dados:** pelo conector (MCP do Meta Ads), pelo Gerenciador no seu navegador ou pelo export que você manda.
3. **Motor:** o Jhon escolhe o claude-ads (diagnóstico amplo, com agentes por plataforma) ou o playbook da tarefa (entrega pontual).
4. **Painel:** os números e o parecer abrem no navegador.
5. **Proposta:** ações por impacto e o que mudar na conta (em rascunho).
6. **Seu "pode":** só então qualquer mudança na conta, uma por vez.
7. **Histórico:** a decisão entra no `trafego.md` do cliente.


# PONTE COM O GAB

Anúncio em vídeo é trabalho dos dois:

| Etapa | Quem | O quê |
|---|---|---|
| 1. Brief | **Jhon** | objetivo, público, oferta e preço, o que já funcionou na conta, ganchos dos concorrentes, 3 a 4 ganchos para teste, formato e duração por plataforma, CTA, o que a política não deixa dizer e a conta da verba. Sai um `brief_anuncio.md` na pasta do vídeo |
| 2. Roteiro e edição | **Gab** (`/ogab`) | roteiro a partir do brief (com a sua aprovação), voz, música, motions, legenda e export; uma versão por gancho |
| 3. Auditoria do criativo | **Jhon** | gancho nos 3 primeiros segundos, encaixe na plataforma, zona segura, legenda, política e acessibilidade; o que corrigir antes de subir |
| 4. Teste e subida | **Jhon** | plano do teste (o que muda, verba, critério de pausa e de vitória) na área **Testes** do painel, e a subida só com o seu "pode" |


# CLIENTES

O Jhon usa o **mesmo cliente do Gab** e acrescenta só a parte de tráfego:

| Arquivo | O que guarda |
|---|---|
| `~/.claude/skills/ogab/clientes/<empresa>/empresa.md` | marca, público, tom, o que não dizer (do Gab) |
| `clientes/<empresa>/trafego.md` | contas e plataformas, produto e preço, objetivo, KPI e meta, verba, margem, janela de atribuição, criativos testados, histórico de decisões |
| `clientes/<empresa>/painel.json` | os números e o parecer que o painel mostra |

Modelos em [`clientes/_exemplo/`](clientes/_exemplo/). A pasta `clientes/` fica fora do git.


# ID DO JHON

Mesma família visual do /ogab: fundo quase preto, uma cor neon de assinatura com degradê e a marca em Inter Tight 800. O Gab é verde; o Jhon é **azul elétrico**, e o símbolo são barras subindo com uma seta de tendência.

| Token | Valor |
|---|---|
| Azul do Jhon | `#2F6BFF` |
| Degradê da marca | `#9DBBFF` > `#2F6BFF` |
| Fundo | `#060A14` / `#111A2E` |
| Fonte da marca | Inter Tight 800 (OFL, em `assets/fontes/`) |

Arquivos em [`assets/id/`](assets/id/): símbolo, logo e o guia [`ID.md`](assets/id/ID.md). O painel e o banner usam a mesma ID.


# SEGURANÇA

- **Rascunho por padrão:** `ads-launch` e `ads-optimize` só aplicam mudança com o seu "pode", ação por ação.
- **Conectores só de leitura:** o Jhon consulta; reembolso, cancelamento, cupom e qualquer escrita na conta ficam de fora.
- **Sem senha:** o Jhon nunca digita senha, token ou cartão.
- **Número com fonte:** CPA, ROAS, verba e benchmark vêm do seu dado ou de fonte citada com data; o que não foi lido fica escrito como lacuna, inclusive no painel.
- **Nichos regulados:** saúde, finanças, imigração, jurídico e promessa de resultado passam pela checagem de política antes de virar anúncio.
- **Terceiros revisados:** o código em `vendor/` e o MCP da Biblioteca de Anúncios foram lidos antes de entrar (sem envio de dados nem comando escondido); as dependências do claude-ads são fixadas por hash.
- **Seus dados ficam com você:** `clientes/`, `config.json` e os dados do painel ficam fora do git.


# MOTORES

| Motor | Autor | O que traz | Onde |
|---|---|---|---|
| [claude-ads](https://github.com/AgriciDaniel/claude-ads) v2.1.0 | AgriciDaniel (MIT) | skill `/ads`, 33 sub-skills `ads-*` (plataformas, plano, verba, criativo, landing, rastreamento, testes, relatório), 25 agentes, referências e evidências com data | `vendor/claude-ads`; instalado em `~/.claude/skills/ads*` e `~/.claude/agents` |
| [marketing-skills](https://github.com/irinabuht12-oss/marketing-skills) | irinabuht12-oss (MIT) | 49 playbooks de uma tarefa (Google, Meta, LinkedIn, Reddit, SEO, visibilidade em IA, e-mail) | `playbooks/` (índice em [`docs/PLAYBOOKS.md`](docs/PLAYBOOKS.md)); original em `vendor/marketing-skills` |
| [facebook-ads-library-mcp](https://github.com/RamsesAguirre777/facebook-ads-library-mcp) | RamsesAguirre777 (MIT) | MCP opcional que lê a Biblioteca de Anúncios pública do Meta | instalado à parte pelo usuário; não vai no repositório |
| [d3](https://d3js.org) e [world-atlas](https://github.com/topojson/world-atlas) | Mike Bostock (ISC) | gráficos e mapa do painel | carregados pelo painel na hora de abrir |


# ESTRUTURA DO REPOSITÓRIO

```
SKILL.md                 o mapa do Jhon: regras, fontes de dados, motores, pedido > o que usar, ponte com o Gab
README.md                este arquivo
CHANGELOG.md             novidades (mostradas ao usar)
install.sh               instala a skill e o motor claude-ads
config.example.json      modelo do config.json (fica fora do git)
painel/                  painel no navegador: index.html, painel.py (gera os dados e abre), LEIA.md (formato)
assets/id/               ID do Jhon: símbolo, logo e guia
assets/fontes/           Inter Tight (OFL)
playbooks/               49 playbooks (marketing-skills), lidos só quando o pedido cai neles
docs/PLAYBOOKS.md        índice dos playbooks
clientes/_exemplo/       modelos do trafego.md e do painel.json
vendor/claude-ads/       motor claude-ads v2.1.0 (fonte, para instalar e atualizar)
vendor/marketing-skills/ fonte original dos playbooks
.github/banner.svg       banner na ID do Jhon
```


# LICENÇA

Código: [MIT](LICENSE). Terceiros mantêm a licença original: [claude-ads](https://github.com/AgriciDaniel/claude-ads) de AgriciDaniel e [marketing-skills](https://github.com/irinabuht12-oss/marketing-skills) de irinabuht12-oss (MIT, em `vendor/` e `playbooks/`), Inter Tight (OFL, em `assets/fontes/`). Dados e contas de anúncio pertencem aos seus donos.
