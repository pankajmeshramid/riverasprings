import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# 1. REPLACE CSS
# ============================================================
old_css = """/* \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 DISTRIBUTORS \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 */
.distributors{background:#fff;padding:140px 0}
@media(max-width:768px){.distributors{padding:80px 0}}
.distributors .label{display:block;margin-bottom:.5rem}
.distributors .gold-rule{margin-bottom:1.75rem}
.distributors h2{
  font-family:var(--serif);font-size:clamp(32px,6vw,72px);
  font-weight:700;color:var(--heading);line-height:0.95;letter-spacing:-1px;margin-bottom:clamp(2rem,4vw,3rem);
}
.top-seller{
  border:2px solid var(--gold);padding:2rem;margin-bottom:2.5rem;
  position:relative;display:flex;align-items:center;gap:1.5rem;
  background:rgba(201,162,39,.03);
}
.top-seller-badge{
  background:var(--gold);color:var(--dark);
  font-size:.65rem;letter-spacing:.12em;text-transform:uppercase;font-weight:700;
  padding:.4rem .9rem;position:absolute;top:-1px;right:1.5rem;
}
.top-seller h3{font-family:var(--serif);font-size:1.3rem;font-weight:700;color:var(--heading)}
.top-seller p{color:#666;font-size:.9rem}
.dist-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem}
.dist-card{
  border:1px solid rgba(11,74,63,.08);padding:1.8rem 1.5rem;border-radius:4px;
  background:var(--bg);transition:transform .6s cubic-bezier(.16,1,.3,1),box-shadow .3s;
  cursor:pointer;position:relative;overflow:hidden;
}
.dist-card:hover{transform:translateY(-6px) scale(1.02);box-shadow:0 16px 48px rgba(11,74,63,.1)}
.dist-card h3{font-family:var(--serif);font-size:1.1rem;font-weight:700;color:var(--heading);margin-bottom:.3rem}
.dist-card p{color:#666;font-size:.85rem}
@media(max-width:1024px){
  .dist-grid{grid-template-columns:1fr 1fr}
}
@media(max-width:768px){
  .dist-grid{grid-template-columns:1fr}
  .top-seller{flex-direction:column;text-align:center;gap:1rem}
}"""

new_css = """/* \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 DISTRIBUTION \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 */
.section-distribution{padding:120px 0;background:#FAFAF7}
.section-distribution .section-header{text-align:center;max-width:700px;margin:0 auto 48px;padding:0 var(--gutter)}
.section-distribution .section-eyebrow{
  display:block;font-family:var(--sans);font-size:.7rem;letter-spacing:.22em;
  text-transform:uppercase;font-weight:600;color:var(--gold);margin-bottom:.5rem;
}
.section-distribution h2{
  font-family:var(--serif);font-size:clamp(32px,6vw,56px);
  font-weight:700;color:var(--heading);line-height:1.05;letter-spacing:-1px;margin-bottom:1rem;
}
.section-distribution .section-header p{
  font-size:15px;color:rgba(8,33,31,0.6);line-height:1.7;
}
.dist-radius-badge{
  display:flex;align-items:center;justify-content:center;gap:10px;
  margin:0 auto 48px;padding:12px 28px;
  background:rgba(201,162,39,0.08);border:1px solid rgba(201,162,39,0.3);
  border-radius:30px;width:fit-content;
  font-size:13px;letter-spacing:1px;color:#0B4A3F;font-weight:500;
}
.dist-grid{
  display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));
  gap:20px;max-width:1100px;margin:0 auto;padding:0 24px;
}
.dist-card{
  background:#fff;border:1px solid rgba(11,74,63,0.1);border-radius:12px;
  padding:28px 20px;text-align:center;
  transition:transform .3s ease,box-shadow .3s ease,border-color .3s ease;
}
.dist-card:hover{
  transform:translateY(-4px);
  box-shadow:0 12px 32px rgba(11,74,63,0.12);
  border-color:rgba(201,162,39,0.4);
}
.dist-card h3{
  font-family:var(--serif);font-size:20px;color:#08211F;margin-bottom:6px;font-weight:700;
}
.dist-state{
  font-size:11px;letter-spacing:1.5px;text-transform:uppercase;
  color:#C9A227;margin-bottom:10px;font-weight:600;
}
.dist-distance{font-size:13px;color:rgba(8,33,31,0.6)}
.dist-hq{
  background:linear-gradient(145deg,#0B4A3F 0%,#08211F 100%);
  border-color:#C9A227;position:relative;
}
.dist-hq h3,.dist-hq .dist-distance{color:#fff}
.dist-hq .dist-state{color:#F5D583}
.dist-badge-hq{
  position:absolute;top:-12px;left:50%;transform:translateX(-50%);
  background:#C9A227;color:#08211F;
  font-size:10px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;
  padding:5px 16px;border-radius:20px;white-space:nowrap;
}
.dist-note{
  text-align:center;font-size:13px;color:rgba(8,33,31,0.5);
  margin-top:40px;max-width:500px;margin-left:auto;margin-right:auto;padding:0 var(--gutter);
}
@media(max-width:767px){
  .dist-grid{grid-template-columns:repeat(2,1fr);gap:14px}
  .section-distribution{padding:70px 0}
}"""

assert old_css in content, "OLD CSS NOT FOUND"
content = content.replace(old_css, new_css)
print("1. CSS replaced")

# ============================================================
# 2. REPLACE HTML
# ============================================================
old_html = """<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 DISTRIBUTORS \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 -->
<section class="distributors" id="distributors" aria-labelledby="distH2">
  <div class="container">
    <span class="label rv" data-i18n="distLabel">OUR NETWORK</span>
    <span class="gold-rule rv rv-d1"></span>
    <h2 class="rv rv-d1" id="distH2" data-i18n="distH2Text">Our Proud Distributors</h2>
    <div class="top-seller rv rv-d2">
      <div class="top-seller-badge" data-i18n="distTopBadge">&#11088; Top Seller</div>
      <div>
        <h3 data-i18n="distTopName">[TOP DISTRIBUTOR NAME]</h3>
        <p data-i18n="distTopRegion">[Region]</p>
      </div>
    </div>
    <div class="dist-grid">
      <div class="dist-card rv rv-d1"><h3 data-i18n="dist1Name">[Distributor 1]</h3><p data-i18n="dist1City">[City]</p></div>
      <div class="dist-card rv rv-d2"><h3 data-i18n="dist2Name">[Distributor 2]</h3><p data-i18n="dist2City">[City]</p></div>
      <div class="dist-card rv rv-d3"><h3 data-i18n="dist3Name">[Distributor 3]</h3><p data-i18n="dist3City">[City]</p></div>
      <div class="dist-card rv rv-d4"><h3 data-i18n="dist4Name">[Distributor 4]</h3><p data-i18n="dist4City">[City]</p></div>
      <div class="dist-card rv rv-d5"><h3 data-i18n="dist5Name">[Distributor 5]</h3><p data-i18n="dist5City">[City]</p></div>
      <div class="dist-card rv rv-d6"><h3 data-i18n="dist6Name">[Distributor 6]</h3><p data-i18n="dist6City">[City]</p></div>
    </div>
  </div>
</section>"""

new_html = '<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 DISTRIBUTION \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 -->\n' \
'<section id="distributors" class="section-distribution" aria-labelledby="distH2">\n' \
'  <div class="section-header rv">\n' \
'    <span class="section-eyebrow" data-i18n="distEyebrow">Where We Deliver</span>\n' \
'    <h2 id="distH2" data-i18n="distTitle">Area of Operation &amp; Distribution</h2>\n' \
'    <p data-i18n="distSubtitle">Serving the tri-state belt of Maharashtra, Madhya Pradesh and Chhattisgarh \u2014 within a 100 km radius of our Amgaon facility.</p>\n' \
'  </div>\n' \
'\n' \
'  <div class="dist-radius-badge rv rv-d1">\n' \
'    <span class="radius-icon">\U0001F4CD</span>\n' \
'    <span data-i18n="distRadiusText">100 km distribution radius from Amgaon, Maharashtra</span>\n' \
'  </div>\n' \
'\n' \
'  <div class="dist-grid">\n' \
'    <div class="dist-card dist-hq rv rv-d1">\n' \
'      <span class="dist-badge dist-badge-hq" data-i18n="distHQBadge">Headquarters</span>\n' \
'      <h3>Amgaon</h3>\n' \
'      <p class="dist-state">Maharashtra</p>\n' \
'      <p class="dist-distance" data-i18n="distDistanceHQ">Manufacturing &amp; Dispatch</p>\n' \
'    </div>\n' \
'    <div class="dist-card rv rv-d1">\n' \
'      <h3>Salekasa</h3>\n' \
'      <p class="dist-state">Maharashtra</p>\n' \
'      <p class="dist-distance">17 km</p>\n' \
'    </div>\n' \
'    <div class="dist-card rv rv-d2">\n' \
'      <h3>Goregaon</h3>\n' \
'      <p class="dist-state">Maharashtra</p>\n' \
'      <p class="dist-distance">~20 km</p>\n' \
'    </div>\n' \
'    <div class="dist-card rv rv-d2">\n' \
'      <h3>Gondia</h3>\n' \
'      <p class="dist-state">Maharashtra</p>\n' \
'      <p class="dist-distance">24 km</p>\n' \
'    </div>\n' \
'    <div class="dist-card rv rv-d3">\n' \
'      <h3>Tirora</h3>\n' \
'      <p class="dist-state">Maharashtra</p>\n' \
'      <p class="dist-distance">~35 km</p>\n' \
'    </div>\n' \
'    <div class="dist-card rv rv-d3">\n' \
'      <h3>Dongargarh</h3>\n' \
'      <p class="dist-state">Chhattisgarh</p>\n' \
'      <p class="dist-distance">~45 km</p>\n' \
'    </div>\n' \
'    <div class="dist-card rv rv-d4">\n' \
'      <h3>Balaghat</h3>\n' \
'      <p class="dist-state">Madhya Pradesh</p>\n' \
'      <p class="dist-distance">~60 km</p>\n' \
'    </div>\n' \
'    <div class="dist-card rv rv-d4">\n' \
'      <h3>Rajnandgaon</h3>\n' \
'      <p class="dist-state">Chhattisgarh</p>\n' \
'      <p class="dist-distance">~75 km</p>\n' \
'    </div>\n' \
'    <div class="dist-card rv rv-d5">\n' \
'      <h3>Bhandara</h3>\n' \
'      <p class="dist-state">Maharashtra</p>\n' \
'      <p class="dist-distance">~85 km</p>\n' \
'    </div>\n' \
'    <div class="dist-card rv rv-d5">\n' \
'      <h3>Lanji</h3>\n' \
'      <p class="dist-state">Madhya Pradesh</p>\n' \
'      <p class="dist-distance">~95 km</p>\n' \
'    </div>\n' \
'  </div>\n' \
'\n' \
'  <p class="dist-note rv rv-d6" data-i18n="distNote">Distances are approximate road distances from our Amgaon facility. Expanding coverage \u2014 contact us to check availability in your area.</p>\n' \
'</section>'

assert old_html in content, "OLD HTML NOT FOUND"
content = content.replace(old_html, new_html)
print("2. HTML replaced")

# ============================================================
# 3. NAV LINK
# ============================================================
content = content.replace(
    '<a href="#distributors" role="menuitem" data-i18n="navDistributors">Distributors</a>',
    '<a href="#distributors" role="menuitem" data-i18n="navDistributors">Distribution</a>'
)
print("3. Nav link updated")

# ============================================================
# 4. i18n — EN (ASCII, straightforward)
# ============================================================
old_en_block = (
    "distLabel:'OUR NETWORK',distH2Text:'Our Proud Distributors',\n"
    "      distTopBadge:'\\u2b50 Top Seller',distTopName:'[TOP DISTRIBUTOR NAME]',distTopRegion:'[Region]',\n"
    "      dist1Name:'[Distributor 1]',dist1City:'[City]',dist2Name:'[Distributor 2]',dist2City:'[City]',\n"
    "      dist3Name:'[Distributor 3]',dist3City:'[City]',dist4Name:'[Distributor 4]',dist4City:'[City]',\n"
    "      dist5Name:'[Distributor 5]',dist5City:'[City]',dist6Name:'[Distributor 6]',dist6City:'[City]',"
)
new_en_block = (
    "distEyebrow:'Where We Deliver',distTitle:'Area of Operation & Distribution',\n"
    "      distSubtitle:'Serving the tri-state belt of Maharashtra, Madhya Pradesh and Chhattisgarh \\u2014 within a 100 km radius of our Amgaon facility.',\n"
    "      distRadiusText:'100 km distribution radius from Amgaon, Maharashtra',\n"
    "      distHQBadge:'Headquarters',distDistanceHQ:'Manufacturing & Dispatch',\n"
    "      distNote:'Distances are approximate road distances from our Amgaon facility. Expanding coverage \\u2014 contact us to check availability in your area.',"
)
assert old_en_block in content, "EN i18n block not found"
content = content.replace(old_en_block, new_en_block)
content = content.replace("navDistributors:'Distributors'", "navDistributors:'Distribution'")
print("4. EN i18n replaced")

# ============================================================
# 5. i18n — HI (stored as literal \uXXXX in file, use regex to find)
# ============================================================
# Find the HI dist block by searching for the pattern between distLabel and the next key (ctLabel)
# The file has literal \u escapes, so we need to match them as-is
hi_pattern = re.compile(
    r"distLabel:'[^']*',distH2Text:'[^']*',\n"
    r"      distTopBadge:'[^']*',distTopName:'[^']*',distTopRegion:'[^']*',\n"
    r"      dist1Name:'[^']*',dist1City:'[^']*',dist2Name:'[^']*',dist2City:'[^']*',\n"
    r"      dist3Name:'[^']*',dist3City:'[^']*',dist4Name:'[^']*',dist4City:'[^']*',\n"
    r"      dist5Name:'[^']*',dist5City:'[^']*',dist6Name:'[^']*',dist6City:'[^']*',"
)

matches = list(hi_pattern.finditer(content))
print(f"   Found {len(matches)} i18n dist blocks to replace (expect 2: HI + MR)")

# HI replacement (escaped unicode)
new_hi_block = (
    "distEyebrow:'\\u0939\\u092e \\u0915\\u0939\\u093e\\u0901 \\u092a\\u0939\\u0941\\u0901\\u091a\\u093e\\u0924\\u0947 \\u0939\\u0948\\u0902',"
    "distTitle:'\\u092a\\u0930\\u093f\\u091a\\u093e\\u0932\\u0928 \\u0915\\u094d\\u0937\\u0947\\u0924\\u094d\\u0930 \\u0914\\u0930 \\u0935\\u093f\\u0924\\u0930\\u0923',\n"
    "      distSubtitle:'\\u092e\\u0939\\u093e\\u0930\\u093e\\u0937\\u094d\\u091f\\u094d\\u0930, \\u092e\\u0927\\u094d\\u092f \\u092a\\u094d\\u0930\\u0926\\u0947\\u0936 \\u0914\\u0930 \\u091b\\u0924\\u094d\\u0924\\u0940\\u0938\\u0917\\u0922\\u093c \\u0915\\u0947 \\u0924\\u094d\\u0930\\u093f-\\u0930\\u093e\\u091c\\u094d\\u092f \\u0915\\u094d\\u0937\\u0947\\u0924\\u094d\\u0930 \\u092e\\u0947\\u0902 \\u0938\\u0947\\u0935\\u093e \\u2014 \\u0939\\u092e\\u093e\\u0930\\u0940 \\u0906\\u092e\\u0917\\u093e\\u0901\\u0935 \\u0938\\u0941\\u0935\\u093f\\u0927\\u093e \\u0938\\u0947 100 \\u0915\\u093f\\u092e\\u0940 \\u0915\\u0947 \\u0926\\u093e\\u092f\\u0930\\u0947 \\u092e\\u0947\\u0902\\u0964',\n"
    "      distRadiusText:'\\u0906\\u092e\\u0917\\u093e\\u0901\\u0935, \\u092e\\u0939\\u093e\\u0930\\u093e\\u0937\\u094d\\u091f\\u094d\\u0930 \\u0938\\u0947 100 \\u0915\\u093f\\u092e\\u0940 \\u0935\\u093f\\u0924\\u0930\\u0923 \\u0926\\u093e\\u092f\\u0930\\u093e',\n"
    "      distHQBadge:'\\u092e\\u0941\\u0916\\u094d\\u092f\\u093e\\u0932\\u092f',distDistanceHQ:'\\u0909\\u0924\\u094d\\u092a\\u093e\\u0926\\u0928 \\u0914\\u0930 \\u092a\\u094d\\u0930\\u0947\\u0937\\u0923',\n"
    "      distNote:'\\u0926\\u0942\\u0930\\u093f\\u092f\\u093e\\u0901 \\u0939\\u092e\\u093e\\u0930\\u0940 \\u0906\\u092e\\u0917\\u093e\\u0901\\u0935 \\u0938\\u0941\\u0935\\u093f\\u0927\\u093e \\u0938\\u0947 \\u0905\\u0928\\u0941\\u092e\\u093e\\u0928\\u093f\\u0924 \\u0938\\u0921\\u093c\\u0915 \\u0926\\u0942\\u0930\\u093f\\u092f\\u093e\\u0901 \\u0939\\u0948\\u0902\\u0964 \\u0915\\u0935\\u0930\\u0947\\u091c \\u092c\\u0922\\u093c \\u0930\\u0939\\u093e \\u0939\\u0948 \\u2014 \\u0905\\u092a\\u0928\\u0947 \\u0915\\u094d\\u0937\\u0947\\u0924\\u094d\\u0930 \\u092e\\u0947\\u0902 \\u0909\\u092a\\u0932\\u092c\\u094d\\u0927\\u0924\\u093e \\u091c\\u093e\\u0928\\u0928\\u0947 \\u0915\\u0947 \\u0932\\u093f\\u090f \\u0939\\u092e\\u0938\\u0947 \\u0938\\u0902\\u092a\\u0930\\u094d\\u0915 \\u0915\\u0930\\u0947\\u0902\\u0964',"
)

# MR replacement (escaped unicode)
new_mr_block = (
    "distEyebrow:'\\u0906\\u092e\\u094d\\u0939\\u0940 \\u0915\\u0941\\u0920\\u0947 \\u092a\\u094b\\u0939\\u094b\\u091a\\u0924\\u094b',"
    "distTitle:'\\u0915\\u093e\\u0930\\u094d\\u092f\\u0915\\u094d\\u0937\\u0947\\u0924\\u094d\\u0930 \\u0906\\u0923\\u093f \\u0935\\u093f\\u0924\\u0930\\u0923',\n"
    "      distSubtitle:'\\u092e\\u0939\\u093e\\u0930\\u093e\\u0937\\u094d\\u091f\\u094d\\u0930, \\u092e\\u0927\\u094d\\u092f \\u092a\\u094d\\u0930\\u0926\\u0947\\u0936 \\u0906\\u0923\\u093f \\u091b\\u0924\\u094d\\u0924\\u0940\\u0938\\u0917\\u0921 \\u092f\\u093e \\u0924\\u094d\\u0930\\u093f-\\u0930\\u093e\\u091c\\u094d\\u092f \\u092a\\u091f\\u094d\\u091f\\u094d\\u092f\\u093e\\u0924 \\u0938\\u0947\\u0935\\u093e \\u2014 \\u0906\\u092e\\u091a\\u094d\\u092f\\u093e \\u0906\\u092e\\u0917\\u093e\\u0935 \\u0938\\u0941\\u0935\\u093f\\u0927\\u0947\\u092a\\u093e\\u0938\\u0942\\u0928 100 \\u0915\\u093f\\u092e\\u0940 \\u092a\\u0930\\u093f\\u0918\\u093e\\u0924.',\n"
    "      distRadiusText:'\\u0906\\u092e\\u0917\\u093e\\u0935, \\u092e\\u0939\\u093e\\u0930\\u093e\\u0937\\u094d\\u091f\\u094d\\u0930 \\u092a\\u093e\\u0938\\u0942\\u0928 100 \\u0915\\u093f\\u092e\\u0940 \\u0935\\u093f\\u0924\\u0930\\u0923 \\u092a\\u0930\\u093f\\u0918',\n"
    "      distHQBadge:'\\u092e\\u0941\\u0916\\u094d\\u092f\\u093e\\u0932\\u092f',distDistanceHQ:'\\u0909\\u0924\\u094d\\u092a\\u093e\\u0926\\u0928 \\u0906\\u0923\\u093f \\u092a\\u094d\\u0930\\u0947\\u0937\\u0923',\n"
    "      distNote:'\\u0905\\u0902\\u0924\\u0930\\u0947 \\u0906\\u092e\\u091a\\u094d\\u092f\\u093e \\u0906\\u092e\\u0917\\u093e\\u0935 \\u0938\\u0941\\u0935\\u093f\\u0927\\u0947\\u092a\\u093e\\u0938\\u0942\\u0928 \\u0905\\u0902\\u0926\\u093e\\u091c\\u0947 \\u0930\\u0938\\u094d\\u0924\\u094d\\u092f\\u093e\\u091a\\u0947 \\u0905\\u0902\\u0924\\u0930 \\u0906\\u0939\\u0947\\u0924. \\u0915\\u0935\\u094d\\u0939\\u0930\\u0947\\u091c \\u0935\\u093e\\u0922\\u0924 \\u0906\\u0939\\u0947 \\u2014 \\u0924\\u0941\\u092e\\u091a\\u094d\\u092f\\u093e \\u092d\\u093e\\u0917\\u093e\\u0924 \\u0909\\u092a\\u0932\\u092c\\u094d\\u0927\\u0924\\u093e \\u0924\\u092a\\u093e\\u0938\\u0923\\u094d\\u092f\\u093e\\u0938\\u093e\\u0920\\u0940 \\u0906\\u092e\\u091a\\u094d\\u092f\\u093e\\u0936\\u0940 \\u0938\\u0902\\u092a\\u0930\\u094d\\u0915 \\u0915\\u0930\\u093e.',"
)

# Replace HI (first match after EN was already replaced) and MR (second match)
if len(matches) >= 2:
    # Replace from end to preserve indices
    # Second match = MR
    mr_match = matches[1]
    content = content[:mr_match.start()] + new_mr_block + content[mr_match.end():]
    # First match = HI
    hi_match = matches[0]
    content = content[:hi_match.start()] + new_hi_block + content[hi_match.end():]
    print("5. HI i18n replaced")
    print("6. MR i18n replaced")
else:
    print(f"WARNING: Expected 2 HI/MR blocks, found {len(matches)}")

# HI nav - literal escaped unicode in file
content = content.replace(
    "navDistributors:'\\u0935\\u093f\\u0924\\u0930\\u0915'",
    "navDistributors:'\\u0935\\u093f\\u0924\\u0930\\u0923'"
)
print("7. Nav i18n (HI/MR) updated")

# ============================================================
# WRITE
# ============================================================
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nAll done!")
