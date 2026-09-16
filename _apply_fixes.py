#!/usr/bin/env python3
"""Apply FIX 1, FIX 2, FIX 3 to index.html"""
import base64, re

# Read index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Read base64 images
with open("_waterfall_b64.txt", "r") as f:
    waterfall_b64 = f.read().strip()
with open("_bottle1l_b64.txt", "r") as f:
    bottle1l_b64 = f.read().strip()

# Read logo base64 from the existing nav (extract it)
logo_match = re.search(r'class="nav-logo"[^>]*src="(data:image/png;base64,[^"]+)"', html)
# Actually logo src is before class, let me search differently
logo_match = re.search(r'<img src="(data:image/png;base64,[^"]+)"[^>]*class="nav-logo"', html)
logo_b64 = logo_match.group(1) if logo_match else ""

# ============================================================
# FIX 1: Replace Source section placeholder with waterfall image
# ============================================================

# Replace the source-img CSS
old_source_img_css = """.source-img{
  position:relative;aspect-ratio:3/4;overflow:hidden;
  background:linear-gradient(135deg,var(--teal) 0%,#0d6454 50%,var(--dark) 100%);
  box-shadow:0 20px 60px rgba(11,74,63,.12);
}
.source-img-ph{
  width:100%;height:100%;display:flex;align-items:center;justify-content:center;
  color:rgba(255,255,255,.3);font-size:.75rem;letter-spacing:.1em;text-transform:uppercase;font-weight:600;
}
.source-img::after{content:'';position:absolute;inset:0;border:1px solid rgba(201,162,39,.2);pointer-events:none}"""

new_source_img_css = """.source-img{
  position:relative;aspect-ratio:3/4;overflow:hidden;
  border-radius:8px;
  box-shadow:0 20px 60px rgba(0,0,0,0.3);
}
.source-img img{
  width:100%;
  height:100%;
  object-fit:cover;
  border-radius:8px;
  display:block;
}
.source-img-overlay{
  position:absolute;inset:0;z-index:1;pointer-events:none;
  background:linear-gradient(180deg, rgba(11,74,63,0.15) 0%, transparent 40%, transparent 60%, rgba(11,74,63,0.25) 100%);
  border-radius:8px;
}
.source-img::after{content:'';position:absolute;inset:0;border:1px solid rgba(201,162,39,.2);pointer-events:none;border-radius:8px}"""

html = html.replace(old_source_img_css, new_source_img_css)

# Replace the source-img HTML
old_source_img_html = """<div class="source-img rv rv-d2">
        <div class="source-img-ph" aria-label="Source image placeholder">[SOURCE IMAGE]</div>
      </div>"""

new_source_img_html = f"""<div class="source-img rv rv-d2">
        <img src="data:image/jpeg;base64,{waterfall_b64}" alt="Natural waterfall \u2014 Rivera Springs water source" loading="lazy">
        <div class="source-img-overlay" aria-hidden="true"></div>
      </div>"""

html = html.replace(old_source_img_html, new_source_img_html)

# Update mobile source-img CSS
html = html.replace(
    ".source-img{max-width:420px;aspect-ratio:4/3}",
    ".source-img{max-width:100%;aspect-ratio:4/3;order:-1}"
)

print("FIX 1: Source image replaced")

# ============================================================
# FIX 2: Retailers Coming Soon
# ============================================================

# Add Coming Soon CSS before the DISTRIBUTORS CSS section
old_retailers_end_css = """@media(max-width:768px){
  .loyalty-steps{grid-template-columns:1fr}
}

/* \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 DISTRIBUTORS \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 */"""

new_retailers_end_css = """@media(max-width:768px){
  .loyalty-steps{grid-template-columns:1fr}
}

.program-preview{
  opacity:0.8;
  border:1.5px dashed rgba(201,162,39,0.5);
  border-radius:12px;
  padding:32px;
  position:relative;
  margin-bottom:2rem;
}
.coming-soon-badge{
  position:absolute;
  top:-14px;
  left:50%;
  transform:translateX(-50%);
  background:#C9A227;
  color:#08211F;
  padding:6px 24px;
  border-radius:20px;
  font-size:13px;
  font-weight:700;
  letter-spacing:2px;
  text-transform:uppercase;
  white-space:nowrap;
  z-index:2;
}
.coming-soon-badge .badge-icon{margin-right:6px}
.launch-message{
  color:var(--teal);font-size:.95rem;line-height:1.7;
  font-style:italic;margin-top:1.5rem;max-width:640px;
}

/* \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 DISTRIBUTORS \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 */"""

html = html.replace(old_retailers_end_css, new_retailers_end_css)

# Replace retailers section HTML
old_retailers_html = """<section class="retailers" id="retailers" aria-labelledby="retailersH2">
  <div class="container">
    <span class="label rv" data-i18n="retLabel">BECOME A PARTNER</span>
    <span class="gold-rule rv rv-d1"></span>
    <h2 class="rv rv-d1" id="retailersH2" data-i18n="retH2">Retailers \u2014 Earn While You Sell</h2>
    <p class="retailers-intro rv rv-d2" data-i18n="retIntro">Scan the QR code on every box, earn 1 credit point per scan. Collect 30 points and redeem for 1 free box \u2014 available after 30 days.</p>
    <div class="loyalty-steps">
      <div class="loyalty-step rv rv-d2">
        <div class="loyalty-step-num">1</div>
        <h3 data-i18n="retStep1H">Scan QR</h3>
        <p data-i18n="retStep1P">Scan the QR code printed inside every Rivera Springs box using your phone.</p>
      </div>
      <div class="loyalty-step rv rv-d3">
        <div class="loyalty-step-num">2</div>
        <h3 data-i18n="retStep2H">Earn Points</h3>
        <p data-i18n="retStep2P">Each scan earns you 1 credit point. Points accumulate automatically in your account.</p>
      </div>
      <div class="loyalty-step rv rv-d4">
        <div class="loyalty-step-num">3</div>
        <h3 data-i18n="retStep3H">Redeem Rewards</h3>
        <p data-i18n="retStep3P">Collect 30 points and redeem for 1 free box. Redemption available after 30 days.</p>
      </div>
    </div>
    <a href="#contact" class="hero-cta rv rv-d5" data-i18n="retCta">Partner With Us <svg viewBox="0 0 16 16"><path d="M1 8h14M9 2l6 6-6 6"/></svg></a>
  </div>
</section>"""

new_retailers_html = """<section class="retailers" id="retailers" aria-labelledby="retailersH2">
  <div class="container">
    <span class="label rv" data-i18n="retLabel">BECOME A PARTNER</span>
    <span class="gold-rule rv rv-d1"></span>
    <h2 class="rv rv-d1" id="retailersH2" data-i18n="retH2">Retailers \u2014 Earn While You Sell</h2>
    <div class="program-preview rv rv-d2">
      <div class="coming-soon-badge"><span class="badge-icon">\U0001f680</span><span class="badge-text" data-i18n="retComingSoon">Coming Soon</span></div>
      <p class="retailers-intro" data-i18n="retIntro">Scan the QR code on every box, earn 1 credit point per scan. Collect 30 points and redeem for 1 free box \u2014 available after 30 days.</p>
      <div class="loyalty-steps">
        <div class="loyalty-step">
          <div class="loyalty-step-num">1</div>
          <h3 data-i18n="retStep1H">Scan QR</h3>
          <p data-i18n="retStep1P">Scan the QR code printed inside every Rivera Springs box using your phone.</p>
        </div>
        <div class="loyalty-step">
          <div class="loyalty-step-num">2</div>
          <h3 data-i18n="retStep2H">Earn Points</h3>
          <p data-i18n="retStep2P">Each scan earns you 1 credit point. Points accumulate automatically in your account.</p>
        </div>
        <div class="loyalty-step">
          <div class="loyalty-step-num">3</div>
          <h3 data-i18n="retStep3H">Redeem Rewards</h3>
          <p data-i18n="retStep3P">Collect 30 points and redeem for 1 free box. Redemption available after 30 days.</p>
        </div>
      </div>
      <p class="launch-message" data-i18n="retLaunchMsg">Our retailer rewards program is launching soon. Register your interest today and be the first to earn.</p>
    </div>
    <a href="#contact" class="hero-cta rv rv-d5" data-i18n="retCta">Partner With Us <svg viewBox="0 0 16 16"><path d="M1 8h14M9 2l6 6-6 6"/></svg></a>
  </div>
</section>"""

html = html.replace(old_retailers_html, new_retailers_html)

# Add i18n keys for Coming Soon - English
html = html.replace(
    "retCta:'Partner With Us',",
    "retCta:'Partner With Us',retComingSoon:'Coming Soon',retLaunchMsg:'Our retailer rewards program is launching soon. Register your interest today and be the first to earn.',"
)

# Hindi i18n
html = html.replace(
    "retCta:'\u092a\u093e\u0930\u094d\u091f\u0928\u0930 \u092c\u0928\u0947\u0902',\n      distLabel:",
    "retCta:'\u092a\u093e\u0930\u094d\u091f\u0928\u0930 \u092c\u0928\u0947\u0902',retComingSoon:'\u091c\u0932\u094d\u0926 \u0906 \u0930\u0939\u093e \u0939\u0948',retLaunchMsg:'\u0939\u092e\u093e\u0930\u093e \u0930\u093f\u091f\u0947\u0932\u0930 \u0930\u093f\u0935\u0949\u0930\u094d\u0921\u094d\u0938 \u092a\u094d\u0930\u094b\u0917\u094d\u0930\u093e\u092e \u091c\u0932\u094d\u0926 \u0939\u0940 \u0932\u0949\u0928\u094d\u091a \u0939\u094b \u0930\u0939\u093e \u0939\u0948\u0964 \u0906\u091c \u0939\u0940 \u0905\u092a\u0928\u0940 \u0930\u0941\u091a\u093f \u0926\u0930\u094d\u091c \u0915\u0930\u0947\u0902 \u0914\u0930 \u0915\u092e\u093e\u0928\u0947 \u0935\u093e\u0932\u0947 \u092a\u0939\u0932\u0947 \u092c\u0928\u0947\u0902\u0964',\n      distLabel:"
)

# Marathi i18n
html = html.replace(
    "retCta:'\u092d\u093e\u0917\u0940\u0926\u093e\u0930 \u0935\u094d\u0939\u093e',\n      distLabel:",
    "retCta:'\u092d\u093e\u0917\u0940\u0926\u093e\u0930 \u0935\u094d\u0939\u093e',retComingSoon:'\u0932\u0935\u0915\u0930\u091a \u092f\u0947\u0924 \u0906\u0939\u0947',retLaunchMsg:'\u0906\u092e\u091a\u093e \u0930\u093f\u091f\u0947\u0932\u0930 \u0930\u093f\u0935\u0949\u0930\u094d\u0921\u094d\u0938 \u092a\u094d\u0930\u094b\u0917\u094d\u0930\u093e\u092e \u0932\u0935\u0915\u0930\u091a \u0938\u0941\u0930\u0942 \u0939\u094b\u0924 \u0906\u0939\u0947. \u0906\u091c\u091a \u0924\u0941\u092e\u091a\u0940 \u0930\u0941\u091a\u0940 \u0928\u094b\u0902\u0926\u0935\u093e \u0906\u0923\u093f \u0915\u092e\u0935\u093e \u0915\u0930\u0923\u093e\u0930\u0947 \u092a\u0939\u093f\u0932\u0947 \u0935\u094d\u0939\u093e.',\n      distLabel:"
)

print("FIX 2: Retailers Coming Soon applied")

# ============================================================
# FIX 3: Rebuild Hero Section
# ============================================================

# First, replace the entire hero CSS block
# Find from /* HERO */ to just before /* SOURCE */
hero_css_start = "/* \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 HERO \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 */"
hero_css_end = "/* \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 SOURCE \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 */"

hero_css_start_idx = html.index(hero_css_start)
hero_css_end_idx = html.index(hero_css_end)

new_hero_css = """/* \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 HERO \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 */
.hero{
  position:relative;width:100%;
  height:100dvh;
  min-height:700px;
  overflow:hidden;background:var(--dark);
}
.hero-bg{
  position:absolute;inset:0;width:100%;height:100%;
  object-fit:cover;object-position:center 30%;
  z-index:0;
  animation:kenburns 28s ease-in-out infinite alternate;
}
@keyframes kenburns{from{transform:scale(1.0)}to{transform:scale(1.05)}}

.hero-overlay{
  position:absolute;inset:0;z-index:1;pointer-events:none;
  background:
    linear-gradient(180deg,rgba(4,14,12,0.88) 0%,rgba(4,14,12,0.2) 22%,transparent 35%),
    linear-gradient(0deg,rgba(4,14,12,0.92) 0%,rgba(4,14,12,0.3) 20%,transparent 35%),
    linear-gradient(90deg,rgba(4,14,12,0.45) 0%,transparent 22%,transparent 78%,rgba(4,14,12,0.45) 100%),
    radial-gradient(ellipse 40% 50% at 50% 50%,rgba(11,74,63,0.2) 0%,transparent 55%);
}

.hero-content{
  position:relative;z-index:10;width:100%;max-width:var(--max-w);
  margin:0 auto;padding:0 var(--gutter);
  display:grid;grid-template-columns:1fr auto 1fr;gap:clamp(2rem,4vw,4rem);
  align-items:center;height:100%;
}

/* Hero left - wordmark + text */
.hero-left{max-width:480px;padding:2rem 0}

.wordmark{text-align:left;margin-bottom:28px}
.wordmark-rivera{
  font-family:var(--serif);font-weight:900;
  font-size:72px;color:#FFFFFF;
  letter-spacing:8px;text-transform:uppercase;
  line-height:1;
  text-shadow:0 4px 20px rgba(0,0,0,0.5);
}
.wordmark-springs{
  display:flex;align-items:center;gap:14px;margin-top:4px;
}
.wordmark-springs .gold-rule{
  flex:0 0 40px;height:1px;background:#C9A227;width:40px;display:block;
}
.springs-text{
  font-family:var(--serif);font-weight:400;font-style:italic;
  font-size:32px;color:#C9A227;
  letter-spacing:6px;text-transform:uppercase;
}
.wordmark-tagline{
  font-family:var(--serif);font-style:italic;
  font-size:15px;color:rgba(245,213,131,0.85);
  margin-top:14px;letter-spacing:0.5px;
}

.hero-body{
  color:rgba(255,255,255,0.78);font-size:1rem;line-height:1.75;
  max-width:420px;margin-bottom:2rem;
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

/* Hero center - bottle */
.hero-bottle{
  position:relative;display:flex;align-items:center;justify-content:center;
  width:280px;perspective:800px;
}
.bottle-wrap{
  position:relative;transition:transform .15s ease-out;
  animation:bottleFloat 6s ease-in-out infinite;
}
@keyframes bottleFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-16px)}}
.bottle-wrap img{
  width:100%;height:auto;position:relative;z-index:2;
  filter:drop-shadow(0 40px 40px rgba(0,0,0,0.6));
}
.bottle-glow{
  position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
  width:180%;height:180%;border-radius:50%;
  background:radial-gradient(circle,rgba(245,213,131,0.45) 0%,rgba(245,213,131,0.15) 30%,transparent 55%);
  z-index:1;animation:glowPulse 3s ease-in-out infinite;
}
@keyframes glowPulse{0%,100%{opacity:.6;transform:translate(-50%,-50%) scale(1)}50%{opacity:1;transform:translate(-50%,-50%) scale(1.08)}}
.bottle-sweep{
  position:absolute;top:0;left:-30%;width:40%;height:100%;z-index:3;
  background:linear-gradient(105deg,transparent 30%,rgba(255,255,255,.1) 48%,rgba(255,255,255,.18) 50%,rgba(255,255,255,.1) 52%,transparent 70%);
  animation:sweep 5.5s ease-in-out infinite;pointer-events:none;
}
@keyframes sweep{0%,100%{left:-30%;opacity:0}40%{opacity:1}60%{opacity:1}100%{left:130%;opacity:0}}
.ripple-ring{
  position:absolute;bottom:-20px;left:50%;transform:translateX(-50%);
  width:120px;height:24px;border-radius:50%;
  border:1px solid rgba(201,162,39,.2);
  animation:rippleExpand 3s ease-out infinite;z-index:0;
}
.ripple-ring:nth-child(5){animation-delay:.8s}
.ripple-ring:nth-child(6){animation-delay:1.6s}
@keyframes rippleExpand{0%{width:80px;height:16px;opacity:.4}100%{width:200px;height:40px;opacity:0}}

/* Hero right - stat cards */
.hero-stats{
  display:flex;flex-direction:column;gap:0;max-width:200px;justify-self:end;
}
.hero-stat{
  padding:1.2rem 1.4rem;position:relative;
}
.hero-stat+.hero-stat{border-top:1px solid rgba(201,162,39,0.2)}
.hero-stat-val{
  font-family:var(--serif);font-size:36px;font-weight:700;
  color:#F5D583;line-height:1.1;margin-bottom:.25rem;
}
.hero-stat-label{
  font-family:var(--sans);font-size:10px;letter-spacing:.12em;
  text-transform:uppercase;color:rgba(255,255,255,0.85);font-weight:600;
}

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
  .hero{min-height:auto;height:auto;padding:6rem 0 3rem}
  .hero-content{
    grid-template-columns:1fr;gap:2rem;text-align:center;
  }
  .hero-left{max-width:100%;margin:0 auto;padding:0}
  .wordmark{text-align:center}
  .wordmark-rivera{font-size:38px;letter-spacing:4px}
  .wordmark-springs{justify-content:center}
  .springs-text{font-size:18px;letter-spacing:3px}
  .wordmark-tagline{font-size:13px}
  .hero-body{margin:0 auto 1.5rem;text-align:center}
  .hero-cta-btn{margin:0 auto}
  .hero-bottle{width:180px;margin:0 auto;order:1}
  .hero-stats{display:none}
  .hero-bottom{flex-direction:column;gap:.5rem;text-align:center}
  .hero-scroll{display:none}
}
@media(min-width:769px) and (max-width:1024px){
  .wordmark-rivera{font-size:52px;letter-spacing:5px}
  .springs-text{font-size:24px}
  .hero-bottle{width:220px}
  .hero-stat-val{font-size:28px}
}

"""

html = html[:hero_css_start_idx] + new_hero_css + html[hero_css_end_idx:]

# Now replace the hero HTML section
# Find <!-- HERO --> section to <!-- PRODUCTS --> or next section
hero_html_start = "<!-- HERO -->"
hero_html_end = "\n<!-- SOURCE -->"

# Actually let me look for the actual section markers
hero_html_start = '<!-- HERO -->\n<section class="hero"'
# Find the end of hero section - it ends before the Source section
hero_section_end = '\n\n<!-- SOURCE -->'
# If that doesn't exist, try other pattern
if hero_section_end not in html:
    hero_section_end = '\n<section class="source"'

hero_start_idx = html.index('<!-- HERO -->')
hero_end_idx = html.index('<section class="source"')

# Generate particle elements
particles_html = ""
import random
random.seed(42)
for i in range(24):
    left = random.randint(2, 98)
    duration = random.uniform(8, 18)
    delay = random.uniform(0, 15)
    size = random.uniform(2, 5)
    particles_html += f'  <div class="hero-particle" style="left:{left}%;bottom:-10px;width:{size:.1f}px;height:{size:.1f}px;animation-duration:{duration:.1f}s;animation-delay:{delay:.1f}s" aria-hidden="true"></div>\n'

new_hero_html = f"""<!-- HERO -->
<section class="hero" id="hero" aria-label="Hero">
  <img class="hero-bg" src="data:image/jpeg;base64,{waterfall_b64}" alt="" aria-hidden="true" loading="eager">
  <div class="hero-overlay" aria-hidden="true"></div>

{particles_html}
  <div class="hero-content">
    <div class="hero-left">
      <div class="wordmark">
        <div class="wordmark-rivera" data-i18n="heroRivera">RIVERA</div>
        <div class="wordmark-springs">
          <span class="gold-rule"></span>
          <span class="springs-text" data-i18n="heroSprings">Springs</span>
          <span class="gold-rule"></span>
        </div>
        <div class="wordmark-tagline" data-i18n="heroWmTag">\u201cBorn from Nature. Bottled for You.\u201d</div>
      </div>

      <p class="hero-body">Pure water from Satpura\u2019s pristine waterfalls, not a municipal borewell.</p>

      <a href="#source" class="hero-cta-btn" data-i18n="heroCta">
        Discover the Source <span class="arrow">\u2192</span>
      </a>
    </div>

    <div class="hero-bottle" id="heroBottle">
      <div class="bottle-wrap" id="bottleWrap">
        <div class="bottle-glow" aria-hidden="true"></div>
        <img src="data:image/png;base64,{bottle1l_b64}" alt="Rivera Springs 1L bottle" loading="eager">
        <div class="bottle-sweep" aria-hidden="true"></div>
        <div class="ripple-ring" aria-hidden="true"></div>
        <div class="ripple-ring" aria-hidden="true"></div>
        <div class="ripple-ring" aria-hidden="true"></div>
      </div>
    </div>

    <div class="hero-stats">
      <div class="hero-stat">
        <div class="hero-stat-val" data-i18n="stat1Val">7</div>
        <div class="hero-stat-label" data-i18n="stat1Label">Stage Filtration</div>
      </div>
      <div class="hero-stat">
        <div class="hero-stat-val">TDS &lt;80</div>
        <div class="hero-stat-label" data-i18n="stat2Label">Balanced Minerals</div>
      </div>
      <div class="hero-stat">
        <div class="hero-stat-val">100%</div>
        <div class="hero-stat-label" data-i18n="stat3Label">BIS Certified</div>
      </div>
    </div>
  </div>

  <div class="hero-bottom">
    <span class="hero-bottom-tagline">\u201cBorn from Nature. Bottled for You.\u201d</span>
    <div class="hero-bottom-certs">
      <span class="hero-bottom-cert">ISO 22000</span>
      <span class="hero-bottom-cert">BIS 14543</span>
      <span class="hero-bottom-cert">FSSAI</span>
    </div>
  </div>

  <div class="hero-scroll" data-i18n="scrollCue">Scroll Down</div>
</section>

"""

html = html[:hero_start_idx] + new_hero_html + html[hero_end_idx:]

# Now fix the JS - remove old hero-related JS that references removed elements
# The mouse-tilt for the bottle - let's add it. Find the script section
# Add mouse-tilt JS before the closing </script>
mouse_tilt_js = """
  /* Mouse-tilt 3D for bottle */
  var heroEl=document.getElementById('hero');
  var bottleWrapEl=document.getElementById('bottleWrap');
  if(heroEl&&bottleWrapEl&&window.innerWidth>768){
    heroEl.addEventListener('mousemove',function(e){
      var rect=heroEl.getBoundingClientRect();
      var x=(e.clientX-rect.left)/rect.width-.5;
      var y=(e.clientY-rect.top)/rect.height-.5;
      bottleWrapEl.style.transform='rotateY('+x*28+'deg) rotateX('+(-y*16)+'deg) translateY('+(Math.sin(Date.now()/1000)*16)+'px)';
    });
    heroEl.addEventListener('mouseleave',function(){
      bottleWrapEl.style.transform='';
    });
  }
"""

# Insert before the closing })(); of the script
html = html.replace("\n})();\n</script>", mouse_tilt_js + "\n})();\n</script>")

print("FIX 3: Hero section rebuilt")

# Remove any old stat-card references in JS that might error
# (the old hero used .stat-card class, new uses .hero-stat)
# Check if there are JS refs to stat-card
if 'stat-card' in html.split('</style>')[1]:
    # Find and note - likely in reveal observer, should be fine since class doesn't exist anymore
    pass

# Write the output
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("All fixes applied and saved to index.html")
print(f"File size: {len(html)} bytes")
