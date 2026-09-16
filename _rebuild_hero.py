import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('hero_bottles_b64.txt', 'r') as f:
    b64 = f.read().strip()

# === STEP 1: Replace hero CSS block ===
old_css_start = '/* \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 HERO \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 */'
old_css_end = '/* \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 UPCOMING PRODUCTS \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 */'

i1 = html.index(old_css_start)
i2 = html.index(old_css_end)

new_hero_css = r"""/* ═══════════ HERO ═══════════ */
.hero{
  position:relative;width:100%;
  height:100dvh;
  min-height:700px;
  overflow:hidden;background-color:#04120f;
}
.hero-bg{
  position:absolute;inset:0;width:100%;height:100%;
  object-fit:cover;object-position:center 60%;
  z-index:0;
  animation:heroZoom 32s ease-in-out infinite alternate;
}
@keyframes heroZoom{from{transform:scale(1.0)}to{transform:scale(1.04)}}
@media(min-width:1024px){.hero-bg{object-position:center 55%}}
@media(min-width:768px) and (max-width:1023px){.hero-bg{object-position:center 58%}}
@media(max-width:767px){.hero-bg{object-position:center 62%}}

.hero-overlay{
  position:absolute;inset:0;z-index:1;pointer-events:none;
  background:
    linear-gradient(180deg,rgba(4,18,15,0.85) 0%,rgba(4,18,15,0.15) 20%,transparent 32%),
    linear-gradient(0deg,rgba(4,18,15,0.9) 0%,rgba(4,18,15,0.25) 18%,transparent 32%),
    linear-gradient(90deg,rgba(4,18,15,0.35) 0%,transparent 18%,transparent 82%,rgba(4,18,15,0.35) 100%);
}

.hero-content{
  position:relative;z-index:10;width:100%;max-width:var(--max-w);
  margin:0 auto;padding:0 var(--gutter);
  height:100%;
}

/* Wordmark - top center */
.wordmark{
  position:absolute;top:100px;left:50%;transform:translateX(-50%);
  text-align:center;z-index:10;
}
.wordmark-rivera{
  font-family:var(--serif);font-weight:900;
  font-size:44px;color:#FFFFFF;
  letter-spacing:6px;text-transform:uppercase;
  line-height:1;
  text-shadow:0 4px 20px rgba(0,0,0,0.5);
}
.wordmark-springs{
  display:flex;align-items:center;gap:14px;margin-top:4px;justify-content:center;
}
.wordmark-springs .gold-rule{
  flex:0 0 40px;height:1px;background:#C9A227;width:40px;display:block;
}
.springs-text{
  font-family:var(--serif);font-weight:400;font-style:italic;
  font-size:20px;color:#C9A227;
  letter-spacing:4px;text-transform:uppercase;
}
.wordmark-tagline{
  font-family:var(--serif);font-style:italic;
  font-size:14px;color:rgba(245,213,131,0.85);
  margin-top:10px;letter-spacing:0.5px;
}

/* Hero body block - bottom center */
.hero-body-block{
  position:absolute;bottom:130px;left:50%;transform:translateX(-50%);
  text-align:center;max-width:480px;z-index:10;
}

.hero-body{
  color:rgba(255,255,255,0.78);font-size:1rem;line-height:1.75;
  margin-bottom:1.5rem;
}

.hero-cta-btn{
  display:inline-flex;align-items:center;gap:.8rem;
  background:var(--gold);color:var(--dark);
  padding:1rem 2.4rem;font-size:.75rem;letter-spacing:.15em;
  text-transform:uppercase;font-weight:700;
  transition:background .25s,transform .2s,box-shadow .3s;
  box-shadow:0 4px 20px rgba(201,162,39,.25);
  text-decoration:none;
}
.hero-cta-btn:hover{background:var(--gold-hi);transform:translateY(-2px);box-shadow:0 8px 32px rgba(201,162,39,.35)}
.hero-cta-btn .arrow{font-size:1.1em;transition:transform .2s}
.hero-cta-btn:hover .arrow{transform:translateX(4px)}

/* Hero bottom bar */
.hero-bottom{
  position:absolute;bottom:0;left:0;right:0;z-index:10;
  padding:1.5rem var(--gutter);
  display:flex;align-items:center;justify-content:space-between;
  max-width:var(--max-w);margin:0 auto;
}
.hero-bottom-tagline{
  font-family:var(--serif);font-style:italic;font-size:.85rem;
  color:rgba(245,213,131,0.7);
}
.hero-bottom-certs{display:flex;gap:.6rem}
.hero-bottom-cert{
  font-size:.55rem;letter-spacing:.1em;text-transform:uppercase;font-weight:700;
  color:rgba(255,255,255,.3);padding:.4rem .7rem;
  border:1px solid rgba(255,255,255,.08);
}

/* Rising particles */
.hero-particle{
  position:absolute;z-index:2;
  width:3px;height:3px;border-radius:50%;
  background:rgba(245,213,131,0.5);
  box-shadow:0 0 6px rgba(245,213,131,0.3);
  animation:particleRise linear infinite;
  pointer-events:none;
}
@keyframes particleRise{
  0%{transform:translateY(0) scale(1);opacity:0}
  10%{opacity:1}
  90%{opacity:1}
  100%{transform:translateY(-100vh) scale(0.3);opacity:0}
}

/* Hero scroll cue */
.hero-scroll{
  position:absolute;bottom:2.5rem;left:50%;transform:translateX(-50%);z-index:10;
  color:rgba(255,255,255,.35);font-size:.58rem;letter-spacing:.22em;text-transform:uppercase;text-align:center;
}
.hero-scroll::after{
  content:'';display:block;width:1px;height:40px;
  background:var(--gold);margin:.7rem auto 0;opacity:.4;
  animation:scrollPulse 2.2s ease-in-out infinite;
}
@keyframes scrollPulse{0%,100%{opacity:.15;transform:scaleY(.5)}50%{opacity:.5;transform:scaleY(1)}}

/* Hero mobile */
@media(max-width:768px){
  .hero{min-height:600px}
  .wordmark{top:80px}
  .wordmark-rivera{font-size:32px;letter-spacing:4px}
  .springs-text{font-size:16px;letter-spacing:3px}
  .wordmark-tagline{font-size:12px}
  .hero-body-block{bottom:100px;max-width:320px;padding:0 1rem}
  .hero-body{font-size:.9rem;margin-bottom:1rem}
  .hero-cta-btn{padding:.8rem 1.8rem;font-size:.7rem}
  .hero-bottom{flex-direction:column;gap:.5rem;text-align:center}
  .hero-scroll{display:none}
}
@media(min-width:769px) and (max-width:1024px){
  .wordmark-rivera{font-size:40px;letter-spacing:5px}
  .springs-text{font-size:18px}
}

"""

html = html[:i1] + new_hero_css + html[i2:]

# === STEP 2: Replace hero HTML section ===
hero_tag = '<section class="hero" id="hero" aria-label="Hero">'
hero_start = html.index(hero_tag)

# Find the next </section> after hero start
rest = html[hero_start:]
# The hero section ends at the first </section>
section_end_match = re.search(r'</section>', rest)
hero_end = hero_start + section_end_match.end()

new_hero_html = '<section class="hero" id="hero" aria-label="Hero">\n'
new_hero_html += '  <img class="hero-bg" src="data:image/jpeg;base64,' + b64 + '" alt="Rivera Springs \u2014 1L, 500ml, 250ml bottles">\n'
new_hero_html += """  <div class="hero-overlay" aria-hidden="true"></div>

  <div class="hero-particle" style="left:83%;bottom:-10px;width:2.7px;height:2.7px;animation-duration:9.1s;animation-delay:11.1s" aria-hidden="true"></div>
  <div class="hero-particle" style="left:19%;bottom:-10px;width:4.7px;height:4.7px;animation-duration:15.4s;animation-delay:10.2s" aria-hidden="true"></div>
  <div class="hero-particle" style="left:13%;bottom:-10px;width:2.3px;height:2.3px;animation-duration:13.9s;animation-delay:0.5s" aria-hidden="true"></div>
  <div class="hero-particle" style="left:31%;bottom:-10px;width:2.6px;height:2.6px;animation-duration:13.1s;animation-delay:0.4s" aria-hidden="true"></div>
  <div class="hero-particle" style="left:85%;bottom:-10px;width:3.3px;height:3.3px;animation-duration:15.0s;animation-delay:6.3s" aria-hidden="true"></div>
  <div class="hero-particle" style="left:37%;bottom:-10px;width:4.4px;height:4.4px;animation-duration:16.1s;animation-delay:0.1s" aria-hidden="true"></div>
  <div class="hero-particle" style="left:91%;bottom:-10px;width:2.6px;height:2.6px;animation-duration:12.2s;animation-delay:4.2s" aria-hidden="true"></div>
  <div class="hero-particle" style="left:45%;bottom:-10px;width:3.1px;height:3.1px;animation-duration:9.0s;animation-delay:5.7s" aria-hidden="true"></div>
  <div class="hero-particle" style="left:70%;bottom:-10px;width:2.2px;height:2.2px;animation-duration:9.2s;animation-delay:13.8s" aria-hidden="true"></div>
  <div class="hero-particle" style="left:75%;bottom:-10px;width:4.0px;height:4.0px;animation-duration:9.9s;animation-delay:1.0s" aria-hidden="true"></div>
  <div class="hero-particle" style="left:50%;bottom:-10px;width:3.1px;height:3.1px;animation-duration:10.8s;animation-delay:9.5s" aria-hidden="true"></div>
  <div class="hero-particle" style="left:89%;bottom:-10px;width:2.5px;height:2.5px;animation-duration:14.5s;animation-delay:9.1s" aria-hidden="true"></div>

  <div class="hero-content">
    <div class="wordmark">
      <div class="wordmark-rivera" data-i18n="heroRivera">RIVERA</div>
      <div class="wordmark-springs">
        <span class="gold-rule"></span>
        <span class="springs-text" data-i18n="heroSprings">Springs</span>
        <span class="gold-rule"></span>
      </div>
      <div class="wordmark-tagline" data-i18n="heroWmTag">"Born from Nature. Bottled for You."</div>
    </div>

    <div class="hero-body-block">
      <p class="hero-body">Pure water from Satpura\u2019s pristine waterfalls, not a municipal borewell.</p>
      <a href="#source" class="hero-cta-btn" data-i18n="heroCta">
        Discover the Source <span class="arrow">\u2192</span>
      </a>
    </div>
  </div>

  <div class="hero-bottom">
    <span class="hero-bottom-tagline">"Born from Nature. Bottled for You."</span>
    <div class="hero-bottom-certs">
      <span class="hero-bottom-cert">ISO 22000</span>
      <span class="hero-bottom-cert">BIS 14543</span>
      <span class="hero-bottom-cert">FSSAI</span>
    </div>
  </div>

  <div class="hero-scroll" data-i18n="scrollCue">Scroll Down</div>
</section>"""

html = html[:hero_start] + new_hero_html + html[hero_end:]

# === STEP 3: Remove old bottle-related JS ===
# Remove the first mouse tilt block
html = re.sub(
    r'  /\* Mouse tilt bottle \*/\n.*?addEventListener\(\'mouseleave\',function\(\)\{bottle\.style\.transform=\'\'\}\);\n  \}\n',
    '',
    html,
    flags=re.DOTALL
)

# Remove the second mouse-tilt block
html = re.sub(
    r'  /\* Mouse-tilt 3D for bottle \*/\n.*?bottleWrapEl\.style\.transform=\'\';\n    \}\);\n  \}\n',
    '',
    html,
    flags=re.DOTALL
)

# Remove parallax hero bg JS
html = re.sub(
    r'  /\* Parallax hero bg \*/\n.*?\{passive:true\}\);\n  \}\n',
    '',
    html,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done! Hero section rebuilt.')
print('File size:', len(html), 'chars')
