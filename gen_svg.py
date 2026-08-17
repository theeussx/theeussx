# -*- coding: utf-8 -*-
import math

ACCENT   = "#4F46E5"
ACCENT2  = "#6366F1"
CYAN     = "#22D3EE"
GREEN    = "#34D399"
AMBER    = "#FBBF24"
TEXT     = "#CBD5E1"
DIM      = "#64748B"
BG0      = "#020617"
BG1      = "#0B1024"

CYCLE = 15.0  # seconds

def kt(t_start, t_end=None):
    """keyTimes/values for fade-in at t_start, stay, fade out at end of cycle."""
    a = max(t_start - 0.15, 0) / CYCLE
    b = t_start / CYCLE
    c = (CYCLE - 0.9) / CYCLE
    return f'values="0;0;1;1;0" keyTimes="0;{a:.4f};{b:.4f};{c:.4f};1"'

def fade(t_start, extra=""):
    return f'<animate attributeName="opacity" {kt(t_start)} dur="{CYCLE}s" repeatCount="indefinite" {extra}/>'

# ----------------------------------------------------------------------------------
# 1) BOOT SEQUENCE
# ----------------------------------------------------------------------------------
W, H = 900, 330
lines = [
    ("[  OK  ]", GREEN,  "booting", "theeussx.core", "v4.0.1  ::  neural backend runtime"),
    ("[  OK  ]", GREEN,  "mounting", "/dev/termux", "mobile-only development environment"),
    ("[  OK  ]", GREEN,  "loading", "modules", "node · typescript · express · prisma"),
    ("[  OK  ]", GREEN,  "linking", "databases", "mysql://cluster · mongodb://atlas"),
    ("[ WARN ]", AMBER,  "missing", "coffee.service", "fallback: pure willpower engaged"),
    ("[  OK  ]", GREEN,  "deploying", "bots", "wardizitto · uptime 99.9%"),
]

body = []
body.append(f'''<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="{BG0}"/>
    <stop offset="55%" stop-color="{BG1}"/>
    <stop offset="100%" stop-color="#0A0A2E"/>
  </linearGradient>
  <linearGradient id="barGrad" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="{ACCENT}"/>
    <stop offset="60%" stop-color="{ACCENT2}"/>
    <stop offset="100%" stop-color="{CYAN}"/>
  </linearGradient>
  <linearGradient id="scan" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="{CYAN}" stop-opacity="0"/>
    <stop offset="50%" stop-color="{CYAN}" stop-opacity="0.16"/>
    <stop offset="100%" stop-color="{CYAN}" stop-opacity="0"/>
  </linearGradient>
  <pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse">
    <path d="M30 0H0V30" fill="none" stroke="{ACCENT2}" stroke-opacity="0.10" stroke-width="1"/>
  </pattern>
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="3" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <clipPath id="frame"><rect x="0" y="0" width="{W}" height="{H}" rx="14"/></clipPath>
</defs>''')

body.append(f'<g clip-path="url(#frame)">')
body.append(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')
body.append(f'<rect width="{W}" height="{H}" fill="url(#grid)"/>')
# ambient glows
body.append(f'<circle cx="70" cy="300" r="180" fill="{ACCENT}" opacity="0.10"/>')
body.append(f'<circle cx="840" cy="30" r="150" fill="{CYAN}" opacity="0.07"/>')
# scanline sweep
body.append(f'''<rect x="0" y="-60" width="{W}" height="60" fill="url(#scan)">
  <animate attributeName="y" values="-60;{H}" dur="4.5s" repeatCount="indefinite"/>
</rect>''')

# window chrome
body.append(f'<rect x="0" y="0" width="{W}" height="40" fill="#060B1F" fill-opacity="0.95"/>')
body.append(f'<line x1="0" y1="40" x2="{W}" y2="40" stroke="{ACCENT2}" stroke-opacity="0.35"/>')
for i, c in enumerate(["#FF5F57", "#FEBC2E", "#28C840"]):
    body.append(f'<circle cx="{24 + i*20}" cy="20" r="6" fill="{c}" opacity="0.9"/>')
body.append(f'<text x="100" y="25" font-family="JetBrains Mono,Fira Code,Consolas,monospace" font-size="13" fill="{DIM}">theeussx@core:~/system/boot</text>')
body.append(f'''<g font-family="JetBrains Mono,Fira Code,Consolas,monospace" font-size="12">
  <circle cx="{W-150}" cy="20" r="4" fill="{GREEN}"><animate attributeName="opacity" values="1;0.2;1" dur="1.6s" repeatCount="indefinite"/></circle>
  <text x="{W-138}" y="25" fill="{GREEN}">SECURE SHELL</text>
</g>''')

y = 74
FS = 14.5
for idx, (tag, col, verb, target, rest) in enumerate(lines):
    t = 0.9 + idx * 1.15
    cid = f"clip{idx}"
    full = 820
    body.append(f'''<clipPath id="{cid}"><rect x="30" y="{y-16}" width="0" height="26">
      <animate attributeName="width" values="0;0;{full};{full};0" keyTimes="0;{t/CYCLE:.4f};{(t+0.6)/CYCLE:.4f};0.955;1" dur="{CYCLE}s" repeatCount="indefinite"/>
    </rect></clipPath>''')
    body.append(f'''<g clip-path="url(#{cid})" font-family="JetBrains Mono,Fira Code,Consolas,monospace" font-size="{FS}">
      {fade(t)}
      <text x="30" y="{y}" fill="{col}" font-weight="700">{tag}</text>
      <text x="118" y="{y}" fill="{DIM}">{verb}</text>
      <text x="{118 + len(verb)*8.7 + 10:.0f}" y="{y}" fill="{ACCENT2}" font-weight="700">{target}</text>
      <text x="{118 + len(verb)*8.7 + 20 + len(target)*8.7:.0f}" y="{y}" fill="{TEXT}" opacity="0.75">{rest}</text>
    </g>''')
    y += 27

# progress bar
by = y + 12
body.append(f'''<g {""}>
  {fade(0.9 + len(lines)*1.15)}
  <text x="30" y="{by-8}" font-family="JetBrains Mono,Fira Code,Consolas,monospace" font-size="12" fill="{DIM}">compiling neural interface</text>
  <rect x="30" y="{by}" width="700" height="8" rx="4" fill="#111a3a"/>
  <rect x="30" y="{by}" width="0" height="8" rx="4" fill="url(#barGrad)" filter="url(#glow)">
    <animate attributeName="width" values="0;140;320;520;700;700" keyTimes="0;0.2;0.45;0.7;0.9;1" dur="{CYCLE}s" repeatCount="indefinite"/>
  </rect>
  <text x="750" y="{by+9}" font-family="JetBrains Mono,Fira Code,Consolas,monospace" font-size="12" fill="{CYAN}">
    100%
  </text>
</g>''')

# final status
fy = by + 46
body.append(f'''<g font-family="JetBrains Mono,Fira Code,Consolas,monospace" font-size="17" font-weight="700">
  {fade(0.9 + len(lines)*1.15 + 1.2)}
  <text x="30" y="{fy}" fill="{ACCENT2}">&gt;</text>
  <text x="50" y="{fy}" fill="#F8FAFC" filter="url(#glow)">SYSTEM ONLINE — WELCOME TO THEEUSSX CORE</text>
  <rect x="{50 + 47*10.2:.0f}" y="{fy-14}" width="10" height="18" fill="{CYAN}">
    <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>
  </rect>
</g>''')

body.append('</g>')
body.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="{ACCENT2}" stroke-opacity="0.45"/>')

svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" fill="none" role="img" aria-label="Boot sequence">\n' + "\n".join(body) + "\n</svg>\n"
open("assets/boot-sequence.svg", "w", encoding="utf-8").write(svg)

# ----------------------------------------------------------------------------------
# 2) TERMINAL — OBJETIVOS
# ----------------------------------------------------------------------------------
W2, H2 = 900, 372
goals = [
    ("Dominar arquitetura de APIs REST + GraphQL", 72, ACCENT2),
    ("Escalar o Wardizitto para +1k servidores",   58, CYAN),
    ("Aprofundar em Docker, CI/CD e Cloud",        41, GREEN),
    ("Publicar meu primeiro pacote npm",           30, AMBER),
    ("Portfólio full-stack de nível sênior",       25, "#F472B6"),
]

b = []
b.append(f'''<defs>
  <linearGradient id="bg2" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="{BG0}"/><stop offset="100%" stop-color="{BG1}"/>
  </linearGradient>
  <pattern id="grid2" width="26" height="26" patternUnits="userSpaceOnUse">
    <path d="M26 0H0V26" fill="none" stroke="{ACCENT2}" stroke-opacity="0.08"/>
  </pattern>
  <filter id="glow2" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="2.4" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <clipPath id="frame2"><rect width="{W2}" height="{H2}" rx="14"/></clipPath>
</defs>
<g clip-path="url(#frame2)">
<rect width="{W2}" height="{H2}" fill="url(#bg2)"/>
<rect width="{W2}" height="{H2}" fill="url(#grid2)"/>
<circle cx="860" cy="330" r="170" fill="{ACCENT}" opacity="0.10"/>
<rect x="0" y="0" width="{W2}" height="38" fill="#060B1F" fill-opacity="0.95"/>
<line x1="0" y1="38" x2="{W2}" y2="38" stroke="{ACCENT2}" stroke-opacity="0.35"/>''')
for i, c in enumerate(["#FF5F57", "#FEBC2E", "#28C840"]):
    b.append(f'<circle cx="{24 + i*20}" cy="19" r="6" fill="{c}" opacity="0.9"/>')
b.append(f'<text x="100" y="24" font-family="JetBrains Mono,Fira Code,Consolas,monospace" font-size="13" fill="{DIM}">theeussx@core:~/goals — bash</text>')

# prompt line typed
cmd = "cat objetivos_2026.log --live"
b.append(f'''<clipPath id="cmdclip"><rect x="26" y="52" width="0" height="24">
  <animate attributeName="width" values="0;0;420;420;0" keyTimes="0;0.02;0.20;0.97;1" dur="{CYCLE}s" repeatCount="indefinite"/>
</rect></clipPath>
<g clip-path="url(#cmdclip)" font-family="JetBrains Mono,Fira Code,Consolas,monospace" font-size="15">
  <text x="26" y="70" fill="{GREEN}" font-weight="700">theeussx@core</text>
  <text x="152" y="70" fill="{DIM}">:</text>
  <text x="160" y="70" fill="{CYAN}">~</text>
  <text x="172" y="70" fill="{ACCENT2}">$</text>
  <text x="188" y="70" fill="#F8FAFC">{cmd}</text>
</g>''')

yy = 108
for i, (name, pct, col) in enumerate(goals):
    t = 2.0 + i * 1.05
    w = round(560 * pct / 100)
    b.append(f'''<g font-family="JetBrains Mono,Fira Code,Consolas,monospace" font-size="13.5">
  {fade(t)}
  <text x="26" y="{yy}" fill="{col}" font-weight="700">▸</text>
  <text x="46" y="{yy}" fill="{TEXT}">{name}</text>
  <rect x="26" y="{yy+8}" width="560" height="6" rx="3" fill="#121a3d"/>
  <rect x="26" y="{yy+8}" width="0" height="6" rx="3" fill="{col}" filter="url(#glow2)">
    <animate attributeName="width" values="0;0;{w};{w};0" keyTimes="0;{t/CYCLE:.3f};{(t+1.0)/CYCLE:.3f};0.95;1" dur="{CYCLE}s" repeatCount="indefinite"/>
  </rect>
  <text x="600" y="{yy+14}" fill="{col}" font-size="12" font-weight="700">{pct}%</text>
  <text x="650" y="{yy+14}" fill="{DIM}" font-size="11">{'IN PROGRESS' if pct < 70 else 'ALMOST THERE'}</text>
</g>''')
    yy += 44

b.append(f'''<g font-family="JetBrains Mono,Fira Code,Consolas,monospace" font-size="14">
  {fade(2.0 + len(goals)*1.05 + 0.6)}
  <text x="26" y="{yy+12}" fill="{ACCENT2}">$</text>
  <text x="44" y="{yy+12}" fill="{DIM}">still compiling the future...</text>
  <rect x="{44 + 30*8.45:.0f}" y="{yy}" width="9" height="16" fill="{CYAN}">
    <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>
  </rect>
</g>
</g>
<rect x="0.5" y="0.5" width="{W2-1}" height="{H2-1}" rx="14" fill="none" stroke="{ACCENT2}" stroke-opacity="0.45"/>''')

svg2 = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W2}" height="{H2}" viewBox="0 0 {W2} {H2}" fill="none" role="img" aria-label="Objetivos">\n' + "\n".join(b) + "\n</svg>\n"
open("assets/terminal-goals.svg", "w", encoding="utf-8").write(svg2)

# ----------------------------------------------------------------------------------
# 3) DIVIDER
# ----------------------------------------------------------------------------------
W3, H3 = 900, 26
d = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W3}" height="{H3}" viewBox="0 0 {W3} {H3}" fill="none" role="img" aria-label="divider">
<defs>
  <linearGradient id="dg" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="{ACCENT}" stop-opacity="0"/>
    <stop offset="25%" stop-color="{ACCENT}" stop-opacity="0.9"/>
    <stop offset="50%" stop-color="{CYAN}" stop-opacity="1"/>
    <stop offset="75%" stop-color="{ACCENT2}" stop-opacity="0.9"/>
    <stop offset="100%" stop-color="{ACCENT}" stop-opacity="0"/>
  </linearGradient>
  <filter id="dgl" x="-20%" y="-400%" width="140%" height="900%">
    <feGaussianBlur stdDeviation="2.2" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>
<rect x="0" y="12" width="{W3}" height="2" fill="url(#dg)" filter="url(#dgl)"/>
<circle cx="0" cy="13" r="4" fill="{CYAN}" filter="url(#dgl)">
  <animate attributeName="cx" values="60;840;60" dur="6s" repeatCount="indefinite"/>
  <animate attributeName="opacity" values="0;1;1;0" dur="6s" repeatCount="indefinite"/>
</circle>
<polygon points="450,4 458,13 450,22 442,13" fill="{ACCENT2}" opacity="0.9"/>
</svg>
'''
open("assets/divider.svg", "w", encoding="utf-8").write(d)
print("ok")
