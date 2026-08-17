# -*- coding: utf-8 -*-
"""Gera cards de preview SVG para os 4 projetos pinados."""
import os, math, random
random.seed(42)

# Dimensões do card — proporção consistente em todos os previews
W, H = 880, 440

# Paleta centralizada (combina com o tema)
BG0       = "#020617"
BG1       = "#0B1024"
BG2       = "#1E1B4B"
DIM       = "#64748B"
TEXT      = "#E2E8F0"
CYAN      = "#22D3EE"
INDIGO    = "#6366F1"
DEEP      = "#4F46E5"
WHITE     = "#F8FAFC"
GREEN     = "#34D399"
AMBER     = "#FBBF24"
PINK      = "#F472B6"
ORANGE    = "#F97316"
BLUE      = "#3B82F6"
DISCORD   = "#5865F2"

OUT_DIR = "assets/projects"
os.makedirs(OUT_DIR, exist_ok=True)


def common_defs(accent):
    """Devs/patterns réutilizáveis + glow filter."""
    return f'''<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="{BG0}"/>
    <stop offset="55%" stop-color="{BG1}"/>
    <stop offset="100%" stop-color="{BG2}"/>
  </linearGradient>
  <radialGradient id="glow" cx="50%" cy="50%" r="60%">
    <stop offset="0%" stop-color="{accent}" stop-opacity="0.45"/>
    <stop offset="55%" stop-color="{accent}" stop-opacity="0.10"/>
    <stop offset="100%" stop-color="{accent}" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="barGrad" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="{INDIGO}"/>
    <stop offset="50%" stop-color="{accent}"/>
    <stop offset="100%" stop-color="{CYAN}"/>
  </linearGradient>
  <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
    <path d="M32 0H0V32" fill="none" stroke="{accent}" stroke-opacity="0.10" stroke-width="1"/>
  </pattern>
  <filter id="soft" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur stdDeviation="6"/>
  </filter>
  <clipPath id="frame"><rect x="0" y="0" width="{W}" height="{H}" rx="18"/></clipPath>
</defs>'''


def base_layers(accent, label):
    """Camadas comuns (background, glow, grid, scan)."""
    layers = []
    layers.append(f'<g clip-path="url(#frame)">')
    layers.append(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')
    layers.append(f'<rect width="{W}" height="{H}" fill="url(#grid)"/>')
    layers.append(f'<circle cx="760" cy="100" r="280" fill="url(#glow)"/>')
    layers.append(f'<circle cx="120" cy="{H-60}" r="220" fill="url(#glow)" opacity="0.7"/>')
    # scanline
    layers.append(f'''<rect x="0" y="-40" width="{W}" height="36" fill="{accent}" opacity="0.07">
      <animate attributeName="y" values="-40;{H+20}" dur="6s" repeatCount="indefinite"/>
    </rect>''')
    # borda interna
    layers.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="{accent}" stroke-opacity="0.25" stroke-width="1"/>')
    return layers


def hud_top(label):
    """Header tipo HUD com label do projeto + mini indicador."""
    return f'''<g font-family="JetBrains Mono, Fira Code, Consolas, monospace" font-size="12">
  <text x="32" y="42" fill="{DIM}" letter-spacing="2">{label}</text>
  <g transform="translate({W-130},30)">
    <rect x="0" y="0" width="98" height="22" rx="11" fill="{BG0}" stroke="{GREEN}" stroke-opacity="0.45"/>
    <circle cx="14" cy="11" r="4" fill="{GREEN}">
      <animate attributeName="opacity" values="1;0.2;1" dur="1.6s" repeatCount="indefinite"/>
    </circle>
    <text x="26" y="15" fill="{GREEN}" font-weight="700">ONLINE</text>
  </g>
</g>'''


def tag(x, y, label, fg):
    """Pílula de tech tag."""
    pad_x = 14
    pad_y = 9
    char_w = 7.6
    w = pad_x*2 + int(len(label) * char_w)
    return f'''<g font-family="JetBrains Mono, Fira Code, Consolas, monospace" font-size="12" font-weight="600">
  <rect x="{x}" y="{y}" width="{w}" height="26" rx="13" fill="{BG0}" stroke="{fg}" stroke-opacity="0.55"/>
  <text x="{x + pad_x}" y="{y + 17}" fill="{fg}" letter-spacing="0.5">{label}</text>
</g>'''


def tags_row(accent, tags, y):
    """Linha de tags horizontal com quebra automática."""
    x = 32
    items = []
    for i, t in enumerate(tags):
        items.append(tag(x, y, t, accent if i == 0 else DIM))
        x += int(14 * 2 + len(t)*7.6) + 8
    return "\n".join(items)


# ──────────────────────────────────────────────────────────────────────
# 1) WARDIZITTO  — Discord bot
# ──────────────────────────────────────────────────────────────────────
def wardizitto():
    accent = DISCORD
    layers = base_layers(accent, "// SYS:// DISCORD_CORE")
    layers.append(hud_top("discord-bot / multifuncional"))

    # Ícone grande abstrato: hexágono estilizado + linhas
    cx, cy = W - 220, H // 2 + 30
    layers.append(f'<g transform="translate({cx-110},{cy-110})">')
    layers.append(f'<polygon points="110,8 198,55 198,165 110,212 22,165 22,55" fill="none" stroke="{accent}" stroke-opacity="0.55" stroke-width="2.5"/>')
    layers.append(f'<polygon points="110,40 170,75 170,145 110,180 50,145 50,75" fill="{accent}" fill-opacity="0.18" stroke="{accent}" stroke-opacity="0.85" stroke-width="2"/>')
    # "WD" monograma
    layers.append(f'<text x="110" y="125" font-family="JetBrains Mono, monospace" font-size="52" font-weight="800" text-anchor="middle" fill="{WHITE}" letter-spacing="-2">WD</text>')
    layers.append('</g>')

    # Título e subtítulo
    layers.append(f'''<g font-family="JetBrains Mono, Fira Code, Consolas, monospace">
  <text x="32" y="160" font-size="44" font-weight="800" fill="{WHITE}" letter-spacing="-1">Wardizitto</text>
  <text x="32" y="190" font-size="14" fill="{DIM}">// discord.js · node 20 · typescript · prisma · mysql</text>
</g>''')

    # barra de "uptime"
    by = 360
    layers.append(f'''<g font-family="JetBrains Mono, monospace" font-size="11">
  <text x="32" y="{by-14}" fill="{DIM}" letter-spacing="1.5">UPTIME</text>
  <text x="{W-32}" y="{by-14}" fill="{accent}" font-weight="700" text-anchor="end">99.9%</text>
  <rect x="32" y="{by-4}" width="816" height="6" rx="3" fill="{BG2}"/>
  <rect x="32" y="{by-4}" width="816" height="6" rx="3" fill="url(#barGrad)"/>
</g>''')

    layers.append(tags_row(accent, ["TypeScript", "discord.js", "Prisma", "MySQL", "Docker", "Node 20"], y=250))

    layers.append('</g>')  # fecha clip
    return "\n".join(layers)


# ──────────────────────────────────────────────────────────────────────
# 2) TCF — Trabalho de Conclusão Final (apresentação interativa)
# ──────────────────────────────────────────────────────────────────────
def tcf():
    accent = CYAN
    layers = base_layers(accent, "// SYS:// TCF_PRESENTATION")
    layers.append(hud_top("reapresentação interativa"))

    # Visual: book/podium icon
    cx, cy = W - 230, H // 2 + 40
    layers.append(f'<g transform="translate({cx-110},{cy-110})">')
    # Livro aberto
    layers.append(f'<path d="M30,40 Q110,20 190,40 L190,170 Q110,150 30,170 Z" fill="{accent}" fill-opacity="0.16" stroke="{accent}" stroke-opacity="0.7" stroke-width="2"/>')
    layers.append(f'<line x1="110" y1="40" x2="110" y2="170" stroke="{accent}" stroke-opacity="0.6" stroke-width="2"/>')
    layers.append(f'<line x1="50" y1="70" x2="100" y2="65" stroke="{accent}" stroke-opacity="0.5" stroke-width="1.5"/>')
    layers.append(f'<line x1="50" y1="100" x2="100" y2="95" stroke="{accent}" stroke-opacity="0.5" stroke-width="1.5"/>')
    layers.append(f'<line x1="120" y1="65" x2="170" y2="70" stroke="{accent}" stroke-opacity="0.5" stroke-width="1.5"/>')
    layers.append(f'<line x1="120" y1="95" x2="170" y2="100" stroke="{accent}" stroke-opacity="0.5" stroke-width="1.5"/>')
    # Floating charts (mini bar chart)
    layers.append(f'<g transform="translate(60,200)">')
    layers.append(f'<rect x="0" y="14" width="6" height="14" rx="1" fill="{accent}" opacity="0.7"/>')
    layers.append(f'<rect x="10" y="6" width="6" height="22" rx="1" fill="{accent}" opacity="0.85"/>')
    layers.append(f'<rect x="20" y="0" width="6" height="28" rx="1" fill="{accent}"/>')
    layers.append(f'<rect x="30" y="10" width="6" height="18" rx="1" fill="{accent}" opacity="0.85"/>')
    layers.append('</g>')
    layers.append('</g>')

    layers.append(f'''<g font-family="JetBrains Mono, Fira Code, Consolas, monospace">
  <text x="32" y="160" font-size="44" font-weight="800" fill="{WHITE}" letter-spacing="-1">TCF</text>
  <text x="32" y="190" font-size="14" fill="{DIM}">// react · vite · tailwind · typescript · charts interativos</text>
</g>''')

    # progresso de páginas
    by = 360
    layers.append(f'''<g font-family="JetBrains Mono, monospace" font-size="11">
  <text x="32" y="{by-14}" fill="{DIM}" letter-spacing="1.5">CHAPTERS</text>
  <text x="{W-32}" y="{by-14}" fill="{accent}" font-weight="700" text-anchor="end">12 / 12</text>
  <rect x="32" y="{by-4}" width="816" height="6" rx="3" fill="{BG2}"/>
  <rect x="32" y="{by-4}" width="816" height="6" rx="3" fill="url(#barGrad)"/>
</g>''')

    layers.append(tags_row(accent, ["React", "Vite", "Tailwind", "TypeScript", "Recharts", "shadcn"], y=250))
    layers.append('</g>')
    return "\n".join(layers)


# ──────────────────────────────────────────────────────────────────────
# 3) PTERODROID — painel Pterodactyl-like (Termux / Android)
# ──────────────────────────────────────────────────────────────────────
def pterodroid():
    accent = GREEN
    layers = base_layers(accent, "// SYS:// PTERODROID_PANEL")
    layers.append(hud_top("painel · termux · android"))

    # Visual: server racks + dragon-ish silhouette minimal
    cx, cy = W - 220, H // 2 + 30
    layers.append(f'<g transform="translate({cx-110},{cy-110})">')
    # server stack
    for i, ly in enumerate([10, 58, 106, 154]):
        layers.append(f'<rect x="40" y="{ly}" width="140" height="40" rx="6" fill="{BG0}" stroke="{accent}" stroke-opacity="{0.4 if i%2 else 0.75}" stroke-width="1.5"/>')
        layers.append(f'<circle cx="56" cy="{ly+20}" r="4" fill="{accent if i%2 else GREEN}"/>')
        layers.append(f'<rect x="70" y="{ly+14}" width="80" height="4" rx="2" fill="{accent}" opacity="0.65"/>')
        layers.append(f'<rect x="70" y="{ly+24}" width="50" height="4" rx="2" fill="{accent}" opacity="0.35"/>')
    layers.append('</g>')

    layers.append(f'''<g font-family="JetBrains Mono, Fira Code, Consolas, monospace">
  <text x="32" y="160" font-size="44" font-weight="800" fill="{WHITE}" letter-spacing="-1">pterodroid</text>
  <text x="32" y="190" font-size="14" fill="{DIM}">// node · express · docker · proot · termux · android</text>
</g>''')

    by = 360
    layers.append(f'''<g font-family="JetBrains Mono, monospace" font-size="11">
  <text x="32" y="{by-14}" fill="{DIM}" letter-spacing="1.5">NODES · ONLINE</text>
  <text x="{W-32}" y="{by-14}" fill="{accent}" font-weight="700" text-anchor="end">3 / 3</text>
  <rect x="32" y="{by-4}" width="816" height="6" rx="3" fill="{BG2}"/>
  <rect x="32" y="{by-4}" width="816" height="6" rx="3" fill="url(#barGrad)"/>
</g>''')

    layers.append(tags_row(accent, ["JavaScript", "Node.js", "Docker", "Linux", "Termux", "Proot"], y=250))
    layers.append('</g>')
    return "\n".join(layers)


# ──────────────────────────────────────────────────────────────────────
# 4) FEIRA DE MATEMÁTICA — app educativa
# ──────────────────────────────────────────────────────────────────────
def feira_matematica():
    accent = PINK
    layers = base_layers(accent, "// SYS:// FEIRA_MAT")
    layers.append(hud_top("educação · imersão · impacto"))

    # Visual: pi symbol + floating geom
    cx, cy = W - 220, H // 2 + 30
    layers.append(f'<g transform="translate({cx-110},{cy-110})">')
    # Big π
    layers.append(f'<text x="110" y="140" font-family="Times New Roman, serif" font-size="160" font-weight="700" text-anchor="middle" fill="{accent}" fill-opacity="0.18" stroke="{accent}" stroke-opacity="0.85" stroke-width="2">π</text>')
    # small triangles (geometry)
    layers.append(f'<polygon points="190,200 220,250 160,250" fill="none" stroke="{accent}" stroke-opacity="0.6" stroke-width="1.5"/>')
    layers.append(f'<circle cx="40" cy="50" r="16" fill="none" stroke="{accent}" stroke-opacity="0.6" stroke-width="1.5"/>')
    layers.append(f'<line x1="40" y1="34" x2="40" y2="66" stroke="{accent}" stroke-opacity="0.4" stroke-width="1"/>')
    layers.append(f'<line x1="24" y1="50" x2="56" y2="50" stroke="{accent}" stroke-opacity="0.4" stroke-width="1"/>')
    layers.append('</g>')

    layers.append(f'''<g font-family="JetBrains Mono, Fira Code, Consolas, monospace">
  <text x="32" y="160" font-size="44" font-weight="800" fill="{WHITE}" letter-spacing="-1">Feira de Matemática</text>
  <text x="32" y="190" font-size="14" fill="{DIM}">// react · vite · tailwind · typescript · vercel</text>
</g>''')

    by = 360
    layers.append(f'''<g font-family="JetBrains Mono, monospace" font-size="11">
  <text x="32" y="{by-14}" fill="{DIM}" letter-spacing="1.5">DEPLOY</text>
  <text x="{W-32}" y="{by-14}" fill="{accent}" font-weight="700" text-anchor="end">SHIPPED ✓</text>
  <rect x="32" y="{by-4}" width="816" height="6" rx="3" fill="{BG2}"/>
  <rect x="32" y="{by-4}" width="816" height="6" rx="3" fill="url(#barGrad)"/>
</g>''')

    layers.append(tags_row(accent, ["TypeScript", "React", "Vite", "Tailwind", "Vercel", "shadcn"], y=250))
    layers.append('</g>')
    return "\n".join(layers)


# ──────────────────────────────────────────────────────────────────────
# Render
# ──────────────────────────────────────────────────────────────────────
PROJECTS = {
    "wardizitto.svg":      (wardizitto,        DISCORD),
    "tcf.svg":              (tcf,               CYAN),
    "pterodroid.svg":       (pterodroid,        GREEN),
    "feira-matematica.svg": (feira_matematica,  PINK),
}

for filename, (fn, accent) in PROJECTS.items():
    body = common_defs(accent) + "\n" + fn()
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" fill="none" role="img" '
        f'aria-label="{filename.replace(".svg","")} preview">\n'
        f'{body}\n'
        f'</svg>\n'
    )
    out = os.path.join(OUT_DIR, filename)
    with open(out, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"  ok  {out}  ({len(svg)} bytes)")
print("done")
