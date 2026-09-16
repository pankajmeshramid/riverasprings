#!/usr/bin/env python3
"""Apply FIX 1-4 to index.html"""
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

with open("_gif_b64.txt", "r") as f:
    gif_b64 = f.read().strip()

# ============================================================
# FIX 1: Replace hero background with animated waterfall GIF
# ============================================================

# 1a. Replace hero-bg CSS: remove Ken Burns, add responsive object-position, fallback bg
old_hero_bg_css = """.hero{
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
@keyframes kenburns{from{transform:scale(1.0)}to{transform:scale(1.05)}}"""

new_hero_bg_css = """.hero{
  position:relative;width:100%;
  height:100dvh;
  min-height:700px;
  overflow:hidden;background-color:#1a3a20;
}
.hero-bg{
  position:absolute;inset:0;width:100%;height:100%;
  object-fit:cover;object-position:center top;
  z-index:0;
}
@media(min-width:1024px){.hero-bg{object-position:center 20%}}
@media(min-width:768px) and (max-width:1023px){.hero-bg{object-position:center 25%}}
@media(max-width:767px){.hero-bg{object-position:center 15%}}"""

assert old_hero_bg_css in html, "FIX 1: Could not find old hero-bg CSS"
html = html.replace(old_hero_bg_css, new_hero_bg_css)

# 1b. Replace hero-bg img src - find the data:image/jpeg;base64 in the hero-bg img tag
# The hero bg is: <img class="hero-bg" src="data:image/jpeg;base64,..."
hero_bg_pattern = r'(<img class="hero-bg" src=")data:image/jpeg;base64,[^"]+(")'
hero_bg_replacement = r'\g<1>data:image/gif;base64,' + gif_b64 + r'\2'
html, count = re.subn(hero_bg_pattern, hero_bg_replacement, html, count=1)
assert count == 1, f"FIX 1: hero-bg img replacement failed (count={count})"

print("FIX 1: Hero background replaced with animated waterfall GIF")

# ============================================================
# FIX 2: Reduce bottle size in hero section
# ============================================================

# 2a. Change .hero-bottle width from 280px to 160px
html = html.replace(
    ".hero-bottle{\n  position:relative;display:flex;align-items:center;justify-content:center;\n  width:280px;perspective:800px;\n}",
    ".hero-bottle{\n  position:relative;display:flex;align-items:center;justify-content:center;\n  width:160px;perspective:800px;\n}"
)

# 2b. Scale down the glow
html = html.replace(
    "  width:180%;height:180%;border-radius:50%;\n  background:radial-gradient(circle,rgba(245,213,131,0.45)",
    "  width:160%;height:160%;border-radius:50%;\n  background:radial-gradient(circle,rgba(245,213,131,0.35)"
)

# 2c. Reduce drop shadow intensity for smaller bottle
html = html.replace(
    "filter:drop-shadow(0 40px 40px rgba(0,0,0,0.6));",
    "filter:drop-shadow(0 24px 30px rgba(0,0,0,0.5));"
)

# 2d. Reduce ripple ring size
html = html.replace(
    "  width:120px;height:24px;border-radius:50%;\n  border:1px solid rgba(201,162,39,.2);\n  animation:rippleExpand 3s ease-out infinite;z-index:0;",
    "  width:80px;height:16px;border-radius:50%;\n  border:1px solid rgba(201,162,39,.2);\n  animation:rippleExpand 3s ease-out infinite;z-index:0;"
)
html = html.replace(
    "@keyframes rippleExpand{0%{width:80px;height:16px;opacity:.4}100%{width:200px;height:40px;opacity:0}}",
    "@keyframes rippleExpand{0%{width:60px;height:12px;opacity:.4}100%{width:140px;height:28px;opacity:0}}"
)

# 2e. Mobile bottle size: 120px instead of 180px
html = html.replace(
    ".hero-bottle{width:180px;margin:0 auto;order:1}",
    ".hero-bottle{width:120px;margin:0 auto;order:1}"
)

# 2f. Tablet bottle size: reduce from 220px
html = html.replace(
    ".hero-bottle{width:220px}",
    ".hero-bottle{width:140px}"
)

print("FIX 2: Bottle size reduced (160px desktop, 120px mobile)")

# ============================================================
# FIX 3: Remove brand text from nav, keep only logo
# ============================================================

# 3a. Remove .nav-wordmark CSS (but keep .nav-brand)
# Remove wordmark CSS lines
for old_css, new_css in [
    (".nav-wordmark{display:flex;flex-direction:column;line-height:1}\n.nav-wordmark-rivera{font-family:var(--serif);font-weight:900;font-size:1.35rem;color:#fff;letter-spacing:.08em;text-transform:uppercase}\n.nav-wordmark-springs{font-family:var(--serif);font-weight:400;font-style:italic;font-size:.85rem;color:var(--gold);letter-spacing:.06em}", ""),
    (".nav-wordmark{display:none}", ""),
]:
    html = html.replace(old_css, new_css)

# 3b. Remove the nav-wordmark HTML div
html = html.replace(
    """      <div class="nav-wordmark">
        <span class="nav-wordmark-rivera">RIVERA</span>
        <span class="nav-wordmark-springs">Springs</span>
      </div>""",
    ""
)

# 3c. Update .nav-brand gap since no text now
html = html.replace(
    ".nav-brand{display:flex;align-items:center;gap:1rem}",
    ".nav-brand{display:flex;align-items:center}"
)

print("FIX 3: Nav brand text removed, logo only")

# ============================================================
# FIX 4: Add Upcoming Products section
# ============================================================

# 4a. Add CSS before SOURCE section CSS
upcoming_css = """
/* ═══════════ UPCOMING PRODUCTS ═══════════ */
.section-upcoming{background:#08211F;padding:clamp(5rem,10vw,6.25rem) 0;color:#fff}
.section-upcoming .section-header{text-align:center;max-width:600px;margin:0 auto clamp(2.5rem,5vw,3.75rem)}
.section-eyebrow{
  font-size:12px;letter-spacing:4px;text-transform:uppercase;
  color:#C9A227;margin-bottom:12px;display:block;font-family:var(--sans);font-weight:600;
}
.section-upcoming h2{
  font-family:var(--serif);font-size:clamp(2rem,4vw,2.625rem);
  font-weight:400;color:#fff;margin-bottom:16px;line-height:1.1;
}
.section-upcoming .section-header p{color:rgba(255,255,255,0.7);font-size:15px;line-height:1.6}
.upcoming-grid{
  display:grid;grid-template-columns:1fr 1fr;gap:48px;
  max-width:900px;margin:0 auto;padding:0 24px;
}
@media(max-width:768px){.upcoming-grid{grid-template-columns:1fr;gap:40px}}
.upcoming-card{
  text-align:center;padding:40px 24px;
  border:1px solid rgba(255,255,255,0.08);border-radius:12px;
  background:rgba(255,255,255,0.03);
  transition:border-color .3s,transform .3s;
}
.upcoming-card:hover{border-color:rgba(201,162,39,0.3);transform:translateY(-4px)}
.upcoming-visual{
  position:relative;height:320px;
  display:flex;align-items:center;justify-content:center;margin-bottom:28px;
}
.silhouette-svg{
  width:100px;height:300px;
  filter:drop-shadow(0 20px 40px rgba(0,0,0,0.4));
  animation:silFloat 6s ease-in-out infinite;
}
@keyframes silFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
.silhouette-glow{
  position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
  width:160px;height:280px;border-radius:50%;filter:blur(40px);
}
.sparkling .silhouette-glow{background:radial-gradient(ellipse,rgba(245,213,131,0.15) 0%,transparent 60%)}
.alkaline .silhouette-glow{background:radial-gradient(ellipse,rgba(60,200,180,0.15) 0%,transparent 60%)}
.upcoming-badge{
  position:absolute;top:12px;right:12px;
  background:rgba(201,162,39,0.15);border:1px solid rgba(201,162,39,0.4);
  color:#C9A227;font-size:10px;letter-spacing:2px;text-transform:uppercase;
  padding:5px 14px;border-radius:20px;font-weight:600;font-family:var(--sans);
}
.alkaline-badge{background:rgba(60,200,180,0.12);border-color:rgba(60,200,180,0.4);color:#3CC8B4}
.upcoming-card h3{
  font-family:var(--serif);font-size:clamp(1.25rem,2.5vw,1.5rem);
  font-weight:400;color:#F5D583;margin-bottom:12px;
}
.upcoming-card p{font-size:14px;line-height:1.65;color:rgba(255,255,255,0.65);max-width:320px;margin:0 auto}

"""

# Insert before SOURCE CSS
source_css_marker = "/* \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 SOURCE \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 */"
assert source_css_marker in html, "FIX 4: Could not find SOURCE CSS marker"
html = html.replace(source_css_marker, upcoming_css + source_css_marker)

# 4b. Add Upcoming Products HTML section between Products and Quality
upcoming_html = """
<!-- ═══════════ UPCOMING PRODUCTS ═══════════ -->
<section id="upcoming" class="section-upcoming" aria-labelledby="upcomingH2">
  <div class="container">
    <div class="section-header rv">
      <span class="section-eyebrow" data-i18n="upEyebrow">What's Next</span>
      <h2 class="rv rv-d1" id="upcomingH2" data-i18n="upH2">Upcoming Products</h2>
      <p class="rv rv-d2" data-i18n="upDesc">Expanding our range with premium hydration \u2014 crafted for those who demand more from their water.</p>
    </div>

    <div class="upcoming-grid">
      <div class="upcoming-card rv rv-d2">
        <div class="upcoming-visual">
          <div class="bottle-silhouette sparkling">
            <div class="silhouette-glow"></div>
            <svg viewBox="0 0 120 380" class="silhouette-svg">
              <defs>
                <linearGradient id="silGrad1" x1="0" y1="0" x2="1" y2="1">
                  <stop offset="0%" stop-color="rgba(245,213,131,0.25)"/>
                  <stop offset="100%" stop-color="rgba(245,213,131,0.05)"/>
                </linearGradient>
              </defs>
              <path d="M48,10 L72,10 L72,45 L82,65 L82,340 C82,360 38,360 38,340 L38,65 L48,45 Z" fill="url(#silGrad1)" stroke="rgba(201,162,39,0.4)" stroke-width="1"/>
              <rect x="45" y="2" width="30" height="12" rx="3" fill="rgba(201,162,39,0.3)" stroke="rgba(201,162,39,0.5)" stroke-width="0.8"/>
              <circle cx="55" cy="200" r="3" fill="rgba(255,255,255,0.15)"/>
              <circle cx="65" cy="240" r="2" fill="rgba(255,255,255,0.12)"/>
              <circle cx="50" cy="280" r="2.5" fill="rgba(255,255,255,0.1)"/>
              <circle cx="70" cy="170" r="1.8" fill="rgba(255,255,255,0.12)"/>
              <circle cx="58" cy="310" r="2" fill="rgba(255,255,255,0.08)"/>
            </svg>
          </div>
          <span class="upcoming-badge" data-i18n="upBadge">Coming Soon</span>
        </div>
        <h3 data-i18n="upSparkH">Premium Sparkling Water</h3>
        <p data-i18n="upSparkP">Naturally carbonated. Fine bubbles. The same pristine Satpura source, now with effervescence \u2014 for those who want their purity with a sparkle.</p>
      </div>

      <div class="upcoming-card rv rv-d3">
        <div class="upcoming-visual">
          <div class="bottle-silhouette alkaline">
            <div class="silhouette-glow"></div>
            <svg viewBox="0 0 120 380" class="silhouette-svg">
              <defs>
                <linearGradient id="silGrad2" x1="0" y1="0" x2="1" y2="1">
                  <stop offset="0%" stop-color="rgba(60,200,180,0.25)"/>
                  <stop offset="100%" stop-color="rgba(60,200,180,0.05)"/>
                </linearGradient>
              </defs>
              <path d="M42,10 L78,10 L78,40 L88,58 L88,320 C88,355 32,355 32,320 L32,58 L42,40 Z" fill="url(#silGrad2)" stroke="rgba(60,200,180,0.4)" stroke-width="1"/>
              <rect x="40" y="2" width="40" height="12" rx="3" fill="rgba(60,200,180,0.3)" stroke="rgba(60,200,180,0.5)" stroke-width="0.8"/>
              <text x="60" y="200" text-anchor="middle" font-family="Bodoni Moda,serif" font-size="28" fill="rgba(60,200,180,0.3)" font-weight="700">pH</text>
              <text x="60" y="235" text-anchor="middle" font-family="Inter,sans-serif" font-size="18" fill="rgba(60,200,180,0.25)">9.5+</text>
            </svg>
          </div>
          <span class="upcoming-badge alkaline-badge" data-i18n="upBadge">Coming Soon</span>
        </div>
        <h3 data-i18n="upAlkH">Alkaline Mineral Water</h3>
        <p data-i18n="upAlkP">Enhanced with added minerals. pH 9.5+. Designed for active lifestyles and health-conscious consumers \u2014 alkaline hydration, sourced from nature, not a lab.</p>
      </div>
    </div>
  </div>
</section>

"""

# Insert between products end and quality start
quality_marker = "<!-- QUALITY -->"
assert quality_marker in html, "FIX 4: Could not find QUALITY HTML marker"
html = html.replace(quality_marker, upcoming_html + quality_marker)

# 4c. Add "Upcoming" nav link between "Our Range" and "Quality"
html = html.replace(
    '<a href="#products" role="menuitem" data-i18n="navRange">Our Range</a>\n        <a href="#quality" role="menuitem" data-i18n="navQuality">Quality</a>',
    '<a href="#products" role="menuitem" data-i18n="navRange">Our Range</a>\n        <a href="#upcoming" role="menuitem" data-i18n="navUpcoming">Upcoming</a>\n        <a href="#quality" role="menuitem" data-i18n="navQuality">Quality</a>'
)

# 4d. Add i18n translations for all three languages

# English translations - add after navContact
html = html.replace(
    "navFactory:'Factory',navRetailers:'Retailers',navDistributors:'Distributors',navContact:'Contact',",
    "navFactory:'Factory',navUpcoming:'Upcoming',navRetailers:'Retailers',navDistributors:'Distributors',navContact:'Contact',",
    1  # only first occurrence = English
)

# Add upcoming product translations in English block - find a good insertion point
# Add after the product translations (p1Luse)
en_upcoming = """upEyebrow:"What\\u2019s Next",upH2:'Upcoming Products',upDesc:'Expanding our range with premium hydration \\u2014 crafted for those who demand more from their water.',upBadge:'Coming Soon',upSparkH:'Premium Sparkling Water',upSparkP:'Naturally carbonated. Fine bubbles. The same pristine Satpura source, now with effervescence \\u2014 for those who want their purity with a sparkle.',upAlkH:'Alkaline Mineral Water',upAlkP:'Enhanced with added minerals. pH 9.5+. Designed for active lifestyles and health-conscious consumers \\u2014 alkaline hydration, sourced from nature, not a lab.',"""

# Find English qualLabel and insert before it
html = html.replace(
    "qualLabel:'Quality &amp; Certification'",
    en_upcoming + "\n      qualLabel:'Quality &amp; Certification'",
    1
)

# Hindi translations - add navUpcoming and product translations
# Hindi navUpcoming
html = html.replace(
    "navFactory:'\u092b\u0948\u0915\u094d\u091f\u094d\u0930\u0940',navRetailers:",
    "navFactory:'\u092b\u0948\u0915\u094d\u091f\u094d\u0930\u0940',navUpcoming:'\u0906\u0928\u0947 \u0935\u093e\u0932\u0947',navRetailers:",
    1
)

hi_upcoming = """upEyebrow:'\u0906\u0917\u0947 \u0915\u094d\u092f\u093e',upH2:'\u0906\u0928\u0947 \u0935\u093e\u0932\u0947 \u0909\u0924\u094d\u092a\u093e\u0926',upDesc:'\u092a\u094d\u0930\u0940\u092e\u093f\u092f\u092e \u0939\u093e\u0907\u0921\u094d\u0930\u0947\u0936\u0928 \u0915\u0947 \u0938\u093e\u0925 \u0939\u092e\u093e\u0930\u0940 \u0930\u0947\u0902\u091c \u0915\u093e \u0935\u093f\u0938\u094d\u0924\u093e\u0930 \\u2014 \u0909\u0928\u0915\u0947 \u0932\u093f\u090f \u091c\u094b \u0905\u092a\u0928\u0947 \u092a\u093e\u0928\u0940 \u0938\u0947 \u0905\u0927\u093f\u0915 \u0915\u0940 \u092e\u093e\u0902\u0917 \u0915\u0930\u0924\u0947 \u0939\u0948\u0902\u0964',upBadge:'\u091c\u0932\u094d\u0926 \u0906 \u0930\u0939\u093e \u0939\u0948',upSparkH:'\u092a\u094d\u0930\u0940\u092e\u093f\u092f\u092e \u0938\u094d\u092a\u093e\u0930\u094d\u0915\u0932\u093f\u0902\u0917 \u0935\u0949\u091f\u0930',upSparkP:'\u092a\u094d\u0930\u093e\u0915\u0943\u0924\u093f\u0915 \u0930\u0942\u092a \u0938\u0947 \u0915\u093e\u0930\u094d\u092c\u094b\u0928\u0947\u091f\u0947\u0921\u0964 \u092c\u0930\u0940\u0915 \u092c\u0941\u0932\u092c\u0941\u0932\u0947\u0964 \u0935\u0939\u0940 \u0936\u0941\u0926\u094d\u0927 \u0938\u0924\u092a\u0941\u0921\u093c\u093e \u0938\u094d\u0930\u094b\u0924, \u0905\u092c \u091a\u092e\u0915 \u0915\u0947 \u0938\u093e\u0925 \\u2014 \u0909\u0928\u0915\u0947 \u0932\u093f\u090f \u091c\u094b \u0905\u092a\u0928\u0940 \u0936\u0941\u0926\u094d\u0927\u0924\u093e \u092e\u0947\u0902 \u091a\u092e\u0915 \u091a\u093e\u0939\u0924\u0947 \u0939\u0948\u0902\u0964',upAlkH:'\u090f\u0932\u094d\u0915\u0932\u093e\u0907\u0928 \u092e\u093f\u0928\u0930\u0932 \u0935\u0949\u091f\u0930',upAlkP:'\u0905\u0924\u093f\u0930\u093f\u0915\u094d\u0924 \u0916\u0928\u093f\u091c\u094b\u0902 \u0915\u0947 \u0938\u093e\u0925\u0964 pH 9.5+\\u0964 \u0938\u0915\u094d\u0930\u093f\u092f \u091c\u0940\u0935\u0928\u0936\u0948\u0932\u0940 \u0914\u0930 \u0938\u094d\u0935\u093e\u0938\u094d\u0925\u094d\u092f \u0915\u0947 \u092a\u094d\u0930\u0924\u093f \u0938\u091c\u0917 \u0909\u092a\u092d\u094b\u0915\u094d\u0924\u093e\u0913\u0902 \u0915\u0947 \u0932\u093f\u090f \\u2014 \u092a\u094d\u0930\u0915\u0943\u0924\u093f \u0938\u0947, \u0932\u0948\u092c \u0938\u0947 \u0928\u0939\u0940\u0902\u0964',"""

# Insert before Hindi qualLabel
html = html.replace(
    "qualLabel:'\u0917\u0941\u0923\u0935\u0924\u094d\u0924\u093e \u0914\u0930 \u092a\u094d\u0930\u092e\u093e\u0923\u0928'",
    hi_upcoming + "\n      qualLabel:'\u0917\u0941\u0923\u0935\u0924\u094d\u0924\u093e \u0914\u0930 \u092a\u094d\u0930\u092e\u093e\u0923\u0928'",
    1
)

# Marathi translations
html = html.replace(
    "navFactory:'\u092b\u0945\u0915\u094d\u091f\u094d\u0930\u0940',navRetailers:",
    "navFactory:'\u092b\u0945\u0915\u094d\u091f\u094d\u0930\u0940',navUpcoming:'\u092a\u0941\u0922\u0947 \u0915\u093e\u092f',navRetailers:",
    1
)

mr_upcoming = """upEyebrow:'\u092a\u0941\u0922\u0947 \u0915\u093e\u092f',upH2:'\u092f\u0947\u0923\u093e\u0930\u0940 \u0909\u0924\u094d\u092a\u093e\u0926\u0928\u0947',upDesc:'\u092a\u094d\u0930\u0940\u092e\u093f\u092f\u092e \u0939\u093e\u092f\u0921\u094d\u0930\u0947\u0936\u0928\u0938\u0939 \u0906\u092e\u091a\u094d\u092f\u093e \u0930\u0947\u0902\u091c\u091a\u093e \u0935\u093f\u0938\u094d\u0924\u093e\u0930 \\u2014 \u091c\u094d\u092f\u093e\u0902\u0928\u093e \u0906\u092a\u0932\u094d\u092f\u093e \u092a\u093e\u0923\u094d\u092f\u093e\u0915\u0921\u0942\u0928 \u0905\u0927\u093f\u0915\u091a\u0940 \u0905\u092a\u0947\u0915\u094d\u0937\u093e \u0906\u0939\u0947.',upBadge:'\u0932\u0935\u0915\u0930\u091a \u092f\u0947\u0924 \u0906\u0939\u0947',upSparkH:'\u092a\u094d\u0930\u0940\u092e\u093f\u092f\u092e \u0938\u094d\u092a\u093e\u0930\u094d\u0915\u0932\u093f\u0902\u0917 \u0935\u0949\u091f\u0930',upSparkP:'\u0928\u0948\u0938\u0930\u094d\u0917\u093f\u0915\u0930\u093f\u0924\u094d\u092f\u093e \u0915\u093e\u0930\u094d\u092c\u094b\u0928\u0947\u091f\u0947\u0921. \u0938\u0942\u0915\u094d\u0937\u094d\u092e \u092c\u0941\u0926\u092c\u0941\u0926\u0947. \u0924\u0947\u091a \u0936\u0941\u0926\u094d\u0927 \u0938\u0924\u092a\u0941\u0921\u094d\u092f\u093e\u091a\u0947 \u092a\u093e\u0923\u0940, \u0906\u0924\u093e \u091a\u092e\u0915\u0938\u0939 \\u2014 \u091c\u094d\u092f\u093e\u0902\u0928\u093e \u0906\u092a\u0932\u094d\u092f\u093e \u0936\u0941\u0926\u094d\u0927\u0924\u0947\u0924 \u091a\u092e\u0915 \u0939\u0935\u0940 \u0906\u0939\u0947.',upAlkH:'\u0905\u0932\u094d\u0915\u0932\u093e\u0907\u0928 \u092e\u093f\u0928\u0930\u0932 \u0935\u0949\u091f\u0930',upAlkP:'\u0905\u0924\u093f\u0930\u093f\u0915\u094d\u0924 \u0916\u0928\u093f\u091c\u093e\u0902\u0938\u0939. pH 9.5+. \u0938\u0915\u094d\u0930\u093f\u092f \u091c\u0940\u0935\u0928\u0936\u0948\u0932\u0940 \u0906\u0923\u093f \u0906\u0930\u094b\u0917\u094d\u092f\u0938\u091c\u0917 \u0917\u094d\u0930\u093e\u0939\u0915\u093e\u0902\u0938\u093e\u0920\u0940 \\u2014 \u0928\u093f\u0938\u0930\u094d\u0917\u093e\u0924\u0942\u0928, \u0932\u0945\u092c\u092e\u0927\u0942\u0928 \u0928\u093e\u0939\u0940.',"""

html = html.replace(
    "qualLabel:'\u0917\u0941\u0923\u0935\u0924\u094d\u0924\u093e \u0906\u0923\u093f \u092a\u094d\u0930\u092e\u093e\u0923\u0928'",
    mr_upcoming + "\n      qualLabel:'\u0917\u0941\u0923\u0935\u0924\u094d\u0924\u093e \u0906\u0923\u093f \u092a\u094d\u0930\u092e\u093e\u0923\u0928'",
    1
)

# 4e. Fix mobile nav stagger delays - there's now one more link
# The nav-links.open a:nth-child delays need updating for the extra link
# Current: 8 links (source, range, quality, founder, factory, retailers, distributors, contact)
# New: 9 links (source, range, upcoming, quality, founder, factory, retailers, distributors, contact)
# Add 9th child delay
html = html.replace(
    ".nav-links.open a:nth-child(8){transition-delay:.4s}",
    ".nav-links.open a:nth-child(8){transition-delay:.4s}\n  .nav-links.open a:nth-child(9){transition-delay:.45s}"
)

print("FIX 4: Upcoming Products section added with i18n")

# ============================================================
# Write output
# ============================================================
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"\nAll 4 fixes applied. File size: {len(html):,} bytes")
