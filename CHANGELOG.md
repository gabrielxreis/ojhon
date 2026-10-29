# Novidades do Jhon (/ojhon)

Mais novo em cima. Cada versão é uma linha `## AAAA.MM.DD-N (DD/MM/AAAA)` seguida do que mudou, em linguagem de usuário.

## 2026.10.29-6 (29/10/2026)
- **Concorrentes repaginados:** destaque para o principal concorrente (foto, quantos anúncios ativos, ganchos que usa e criativos campeões), os outros 4 principais em cards com foto, ranking de quem mais anuncia, todos os criativos campeões ordenados pelo tempo no ar e os demais concorrentes em lista. Cada criativo abre no player da Biblioteca do Meta.
- **Miniaturas dos campeões:** cada criativo campeão aparece com a capa do vídeo, sem baixar o vídeo.
- **Botão de baixar:** ícone ⬇ em cada criativo da concorrência; com o vídeo já baixado pelo Jhon, salva direto em Downloads; sem ele, copia o pedido para o Jhon baixar.
- **Corrigido:** o botão Exportar esticava a barra do topo inteira.
- **Baixar de verdade:** o painel agora abre por um servidor local (127.0.0.1) e o ⬇ salva o vídeo em vez de abrir numa janela.

## 2026.10.29-5 (29/10/2026)
- **Painel sempre em dia:** todo comando do /ojhon atualiza o painel no começo e no fim. A aba aberta se atualiza sozinha em poucos segundos (aparece "O Jhon atualizou o painel") e não abre aba nova a cada comando.

## 2026.10.29-4 (29/10/2026)
- **Ficha da campanha:** clique numa campanha e veja tudo só sobre ela: investimento, resultado, custo por resultado comparado com as do mesmo tipo, CPM contra a média da conta, cliques, alcance, frequência, orçamento, posição no ranking e o parecer do Jhon.
- **Concorrentes com player:** a área Concorrentes mostra o que a concorrência anuncia agora, com filtro por anunciante, há quantos dias cada anúncio está no ar e o botão ▶ que abre o vídeo direto da Biblioteca de Anúncios do Meta, sem baixar nada.

## 2026.10.29-3 (29/10/2026)
- **ID do Jhon:** mesma família visual do Gab (fundo quase preto, cor neon, Inter Tight 800), com o azul elétrico como assinatura e um símbolo de barras subindo com seta. Arquivos em `assets/id/` e banner novo.
- **Painel com tema escuro:** segue o tema do sistema e tem o botão de sol e lua no topo (a escolha fica salva).
- **Menu do painel reorganizado:** Painel (com contadores), Canais (com ou sem dados) e Pedir ao Jhon (copia o comando já com o cliente). Completo em tela grande, só ícones em tela média, gaveta no celular, e dá para recolher.
- **Painel com mais áreas:** Plano de verba (calculadora de verba por semana, retorno e ponto de empate), Testes de criativo e Concorrentes.
- **README novo:** conectores, painel, ID e o fluxo completo.

## 2026.10.29-2 (29/10/2026)
- **Painel do Jhon no navegador:** todo insight ou resultado abre um painel local (`/ojhon painel <cliente>`): barra lateral com as plataformas, seletor de cliente, busca ⌘K, Exportar CSV, abas Visão geral, Campanhas, Criativos e Parecer; resumo com variação contra o mês anterior, mapa de entrega, evolução por mês, investimento por tipo, parecer do Jhon e tabela de campanhas.
- **MCP oficial do Meta Ads:** o Jhon sugere conectar `https://mcp.facebook.com/ads` (fonte principal para Meta, mais rápida que ler o Gerenciador pelo navegador). Só leitura.

## 2026.10.29-1 (29/10/2026)
- **claude-ads v2.1.0:** auditoria do Google para de contar palavra-chave negativa como ativa, fonte vencida passa a reprovar, dependências com falha de segurança trocadas (Pillow 12.3.0, urllib3 2.8.0).
- **Instalador:** ignora pacote Python solto em ~/Library/Python, que derrubava as dependências do claude-ads ("installed version mismatch").
- **Concorrentes de verdade:** o Jhon usa a Biblioteca de Anúncios do Meta (MCP opcional, sem token) para puxar os anúncios ativos dos concorrentes no Brasil.
- **Venda real:** com o MCP da Hotmart ligado, ROAS e CAC saem da venda, não do pixel (só leitura).
- **Painel do cliente (`/ojhon painel`):** dashboard com os números da conta, o que está bom e ruim e o parecer do Jhon.
- **update e doctor:** conferem se o claude-ads está na última versão e se o MCP da Ad Library responde.

## 2026.10.13-1 (13/10/2026)
- **Nasce o Jhon:** gestor de tráfego com IA. Auditoria de 12 plataformas, plano de mídia e verba, criativo e copy, concorrentes, rastreamento, landing page, testes, relatório para cliente, SEO e visibilidade em IA.
- **Dois motores:** claude-ads (33 sub-skills e 25 agentes de auditoria) e 49 playbooks de análise (marketing-skills), escolhidos pelo Jhon conforme o pedido.
- **Ponte com o Gab:** anúncio em vídeo sai com brief do Jhon, edição do Gab e auditoria do criativo antes de subir.
- **Nada muda na conta sem o seu "pode":** publicar, pausar, apagar ou mexer em verba só com aprovação, ação por ação.
