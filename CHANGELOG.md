# Novidades do Jhon (/ojhon)

Mais novo em cima. Cada versão é uma linha `## AAAA.MM.DD-N (DD/MM/AAAA)` seguida do que mudou, em linguagem de usuário.

## 2026.10.29-3 (29/10/2026)
- **ID do Jhon:** mesma família visual do Gab (fundo quase preto, cor neon, Inter Tight 800), com o azul elétrico como assinatura e um símbolo de barras subindo com seta. Arquivos em `assets/id/` e banner novo.
- **Painel com tema escuro:** segue o tema do sistema e tem o botão de sol e lua no topo (a escolha fica salva).
- **Menu do painel reorganizado:** Painel (com contadores), Canais (com ou sem dados) e Pedir ao Jhon (copia o comando já com o cliente). Completo em tela grande, só ícones em tela média, gaveta no celular, e dá para recolher.
- **Preço da X-Trader corrigido** pelo site (X-ACCESS Genesis R$ 997 por ano).

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
