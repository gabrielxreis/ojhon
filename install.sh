#!/usr/bin/env bash
# Instalador do Jhon (/ojhon), o gestor de tráfego com IA (macOS).
# Uso:  curl -fsSL https://raw.githubusercontent.com/gabrielxreis/ojhon/main/install.sh | bash
#       bash ~/.claude/skills/ojhon/install.sh --so-ads   (só reinstala/atualiza o motor claude-ads)
# Pode rodar de novo quando quiser: atualiza a skill e o motor.
set -euo pipefail

REPO="https://github.com/gabrielxreis/ojhon"
DEST="$HOME/.claude/skills/ojhon"
SO_ADS=0; [ "${1:-}" = "--so-ads" ] && SO_ADS=1

ok()   { printf "  \033[32m✓\033[0m %s\n" "$1"; }
info() { printf "\n\033[1m%s\033[0m\n" "$1"; }
warn() { printf "  \033[33m!\033[0m %s\n" "$1"; }

if [ "$SO_ADS" = 0 ]; then
  info "1/3 Skill /ojhon"
  command -v git >/dev/null 2>&1 || { echo "  Falta o git (xcode-select --install)."; exit 1; }
  if [ -d "$DEST/.git" ]; then
    git -C "$DEST" pull --ff-only --quiet && ok "atualizada em $DEST"
  elif [ -d "$DEST" ]; then
    ok "já existe em $DEST (sem git; não mexi)"
  else
    git clone --depth 1 --quiet "$REPO" "$DEST" && ok "instalada em $DEST"
  fi
  [ -f "$DEST/config.json" ] || cp "$DEST/config.example.json" "$DEST/config.json" 2>/dev/null || true
fi

info "2/3 Motor claude-ads (auditoria, plano, criativo: 33 sub-skills e 25 agentes)"
# O claude-ads só tem dependências conferidas (com hash) para Python 3.10 a 3.13.
PYDIR=""
for v in 3.13 3.12 3.11 3.10; do
  for b in "/opt/homebrew/bin/python$v" "/usr/local/bin/python$v" "$(command -v python$v 2>/dev/null || true)"; do
    if [ -n "$b" ] && [ -x "$b" ]; then PYDIR="$(mktemp -d)"; ln -s "$b" "$PYDIR/python3"; break 2; fi
  done
done
cd "$HOME"
if [ -n "$PYDIR" ]; then
  if PATH="$PYDIR:$PATH" bash "$DEST/vendor/claude-ads/install.sh" --source=local --repo-dir="$DEST/vendor/claude-ads" >/tmp/ojhon_ads_install.log 2>&1; then
    ok "claude-ads com as dependências Python ($("$PYDIR/python3" --version))"
  else
    warn "dependências falharam; instalando só as skills (log: /tmp/ojhon_ads_install.log)"
    bash "$DEST/vendor/claude-ads/install.sh" --source=local --repo-dir="$DEST/vendor/claude-ads" --no-deps >/dev/null && ok "claude-ads sem dependências"
  fi
  rm -rf "$PYDIR"
else
  bash "$DEST/vendor/claude-ads/install.sh" --source=local --repo-dir="$DEST/vendor/claude-ads" --no-deps >/dev/null && ok "claude-ads (sem dependências Python)"
  warn "sem Python 3.10 a 3.13: print de site, análise de landing, PDF e imagem do claude-ads não rodam. 'brew install python@3.12' e rode de novo."
fi

info "3/3 Conferência"
n=$(ls "$DEST/playbooks" 2>/dev/null | wc -l | tr -d ' '); ok "$n playbooks em $DEST/playbooks"
[ -f "$HOME/.claude/skills/ads/SKILL.md" ] && ok "/ads instalado" || warn "/ads não encontrado"
a=$(ls "$HOME/.claude/agents" 2>/dev/null | grep -c '^audit-' || true); ok "$a agentes de auditoria"
echo
echo "Pronto. Reinicie o Claude Code e peça: /ojhon ajuda"
