with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# 1. CSS — insert before DISTRIBUTION comment
# ============================================================
css_block = """/* \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 CUSTOM BRANDING \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 */
.section-custom{padding:120px 0;background:#08211F;color:#fff}
.section-custom .section-header{text-align:center;max-width:640px;margin:0 auto 64px;padding:0 var(--gutter)}
.section-custom .section-eyebrow{
  display:block;font-family:var(--sans);font-size:.7rem;letter-spacing:.22em;
  text-transform:uppercase;font-weight:600;color:var(--gold);margin-bottom:.5rem;
}
.section-custom h2{font-family:var(--serif);font-size:clamp(36px,5vw,56px);color:#fff;margin-bottom:16px}
.section-custom .section-header p{color:rgba(255,255,255,0.7);font-size:15px}
.custom-grid{
  display:grid;grid-template-columns:1fr 1fr;gap:40px;
  max-width:1000px;margin:0 auto;padding:0 24px;
}
@media(max-width:768px){.custom-grid{grid-template-columns:1fr;gap:32px}}
.custom-card{
  background:rgba(255,255,255,0.03);border:1px solid rgba(201,162,39,0.2);
  border-radius:16px;padding:40px 32px;
  transition:border-color .3s,transform .3s;
}
.custom-card:hover{border-color:rgba(201,162,39,0.5);transform:translateY(-4px)}
.custom-icon{margin-bottom:24px}
.custom-card h3{font-family:var(--serif);font-size:24px;color:#F5D583;margin-bottom:14px}
.custom-card>p{font-size:14px;line-height:1.65;color:rgba(255,255,255,0.75);margin-bottom:24px}
.custom-features{list-style:none;margin-bottom:24px}
.custom-features li{
  font-size:13px;color:rgba(255,255,255,0.65);padding:8px 0 8px 22px;
  position:relative;border-top:1px solid rgba(255,255,255,0.08);
}
.custom-features li:first-child{border-top:none}
.custom-features li::before{content:"\\2192";position:absolute;left:0;color:#C9A227}
.custom-moq{
  display:inline-block;font-size:11px;letter-spacing:1px;text-transform:uppercase;
  color:#C9A227;background:rgba(201,162,39,0.1);padding:6px 14px;border-radius:20px;margin-bottom:20px;
}
.custom-cta{
  display:block;text-align:center;padding:14px;
  border:1.5px solid #C9A227;color:#C9A227;text-decoration:none;
  font-size:12px;letter-spacing:2px;text-transform:uppercase;font-weight:600;
  border-radius:6px;transition:all .3s;
}
.custom-cta:hover{background:#C9A227;color:#08211F}
.custom-note{
  text-align:center;font-size:12px;color:rgba(255,255,255,0.45);
  max-width:480px;margin:48px auto 0;padding:0 var(--gutter);
}

"""

anchor = "/* \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 DISTRIBUTION \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 */"
assert anchor in content, "CSS anchor not found"
content = content.replace(anchor, css_block + anchor)
print("1. CSS inserted")

# ============================================================
# 2. HTML — insert between Retailers </section> and Distribution comment
# ============================================================
html_block = """
<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 CUSTOM BRANDING \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 -->
<section id="custom-branding" class="section-custom" aria-labelledby="customH2">
  <div class="section-header rv">
    <span class="section-eyebrow" data-i18n="customEyebrow">Bulk &amp; Private Label</span>
    <h2 id="customH2" data-i18n="customTitle">Your Brand. Our Water.</h2>
    <p data-i18n="customSubtitle">Bulk ordering with custom branding options \u2014 for retailers, businesses, and event organizers.</p>
  </div>

  <div class="custom-grid">
    <div class="custom-card rv rv-d1">
      <div class="custom-icon">
        <svg viewBox="0 0 60 60" width="48" height="48">
          <rect x="10" y="8" width="40" height="44" rx="4" fill="none" stroke="#C9A227" stroke-width="1.5"/>
          <line x1="18" y1="20" x2="42" y2="20" stroke="#C9A227" stroke-width="1.5"/>
          <line x1="18" y1="28" x2="42" y2="28" stroke="#C9A227" stroke-width="1.5"/>
          <line x1="18" y1="36" x2="34" y2="36" stroke="#C9A227" stroke-width="1.5"/>
          <circle cx="30" cy="44" r="4" fill="none" stroke="#C9A227" stroke-width="1.5"/>
        </svg>
      </div>
      <h3 data-i18n="whiteLabelTitle">Private Label \u2014 Your Own Brand</h3>
      <p data-i18n="whiteLabelDesc">Building your own water brand? We manufacture and bottle under YOUR name and logo \u2014 full white-label production. Rivera Springs branding does not appear on the bottle. You sell it as your own.</p>
      <ul class="custom-features">
        <li data-i18n="wlFeature1">Custom label design &amp; printing</li>
        <li data-i18n="wlFeature2">Your brand name, your logo, your identity</li>
        <li data-i18n="wlFeature3">Same 7-stage filtration &amp; quality standards</li>
        <li data-i18n="wlFeature4">Minimum order quantity applies</li>
      </ul>
      <span class="custom-moq" data-i18n="wlMOQ">MOQ: [To be confirmed] boxes</span>
      <a href="#contact" class="custom-cta" data-i18n="customCTA">Enquire Now</a>
    </div>

    <div class="custom-card rv rv-d2">
      <div class="custom-icon">
        <svg viewBox="0 0 60 60" width="48" height="48">
          <rect x="14" y="6" width="32" height="48" rx="4" fill="none" stroke="#C9A227" stroke-width="1.5"/>
          <path d="M22,20 L30,14 L38,20 L34,20 L34,30 L26,30 L26,20 Z" fill="none" stroke="#C9A227" stroke-width="1.2"/>
          <line x1="20" y1="40" x2="40" y2="40" stroke="#C9A227" stroke-width="1.2"/>
          <line x1="20" y1="45" x2="34" y2="45" stroke="#C9A227" stroke-width="1.2"/>
        </svg>
      </div>
      <h3 data-i18n="eventLabelTitle">Wedding &amp; Event Bottles</h3>
      <p data-i18n="eventLabelDesc">Celebrating a wedding, engagement, or special event? Add your names, photo, or event details to the label \u2014 alongside Rivera Springs branding \u2014 for a personalized touch your guests will remember.</p>
      <ul class="custom-features">
        <li data-i18n="evFeature1">Your photo or names printed on label</li>
        <li data-i18n="evFeature2">Rivera Springs branding stays on the bottle</li>
        <li data-i18n="evFeature3">Perfect for weddings, engagements, corporate events</li>
        <li data-i18n="evFeature4">Minimum order quantity applies</li>
      </ul>
      <span class="custom-moq" data-i18n="evMOQ">MOQ: [To be confirmed] boxes</span>
      <a href="#contact" class="custom-cta" data-i18n="customCTA">Enquire Now</a>
    </div>
  </div>

  <p class="custom-note rv rv-d3" data-i18n="customNote">Custom orders require advance booking and lead time for label design and approval. Contact us to discuss your requirements, minimum quantities, and pricing.</p>
</section>

"""

html_anchor = "<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 DISTRIBUTION \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 -->"
assert html_anchor in content, "HTML anchor not found"
content = content.replace(html_anchor, html_block + html_anchor)
print("2. HTML inserted")

# ============================================================
# 3. NAV — add "Custom Branding" link after Retailers
# ============================================================
nav_old = '<a href="#retailers" role="menuitem" data-i18n="navRetailers">Retailers</a>\n        <a href="#distributors" role="menuitem" data-i18n="navDistributors">Distribution</a>'
nav_new = '<a href="#retailers" role="menuitem" data-i18n="navRetailers">Retailers</a>\n        <a href="#custom-branding" role="menuitem" data-i18n="navCustom">Custom Branding</a>\n        <a href="#distributors" role="menuitem" data-i18n="navDistributors">Distribution</a>'
assert nav_old in content, "Nav anchor not found"
content = content.replace(nav_old, nav_new)
print("3. Nav link added")

# ============================================================
# 4. i18n — EN
# ============================================================
en_anchor = "      distNote:'Distances are approximate road distances from our Amgaon facility. Expanding coverage \\u2014 contact us to check availability in your area.',\n      ctLabel:'GET IN TOUCH'"
en_insert = """      distNote:'Distances are approximate road distances from our Amgaon facility. Expanding coverage \\u2014 contact us to check availability in your area.',
      navCustom:'Custom Branding',
      customEyebrow:'Bulk & Private Label',customTitle:'Your Brand. Our Water.',
      customSubtitle:'Bulk ordering with custom branding options \\u2014 for retailers, businesses, and event organizers.',
      whiteLabelTitle:'Private Label \\u2014 Your Own Brand',
      whiteLabelDesc:'Building your own water brand? We manufacture and bottle under YOUR name and logo \\u2014 full white-label production. Rivera Springs branding does not appear on the bottle. You sell it as your own.',
      wlFeature1:'Custom label design & printing',wlFeature2:'Your brand name, your logo, your identity',
      wlFeature3:'Same 7-stage filtration & quality standards',wlFeature4:'Minimum order quantity applies',
      wlMOQ:'MOQ: [To be confirmed] boxes',
      eventLabelTitle:'Wedding & Event Bottles',
      eventLabelDesc:'Celebrating a wedding, engagement, or special event? Add your names, photo, or event details to the label \\u2014 alongside Rivera Springs branding \\u2014 for a personalized touch your guests will remember.',
      evFeature1:'Your photo or names printed on label',evFeature2:'Rivera Springs branding stays on the bottle',
      evFeature3:'Perfect for weddings, engagements, corporate events',evFeature4:'Minimum order quantity applies',
      evMOQ:'MOQ: [To be confirmed] boxes',
      customCTA:'Enquire Now',
      customNote:'Custom orders require advance booking and lead time for label design and approval. Contact us to discuss your requirements, minimum quantities, and pricing.',
      ctLabel:'GET IN TOUCH'"""
assert en_anchor in content, "EN i18n anchor not found"
content = content.replace(en_anchor, en_insert)
print("4. EN i18n added")

# ============================================================
# 5. i18n — HI (uses literal \u escapes in file)
# ============================================================
hi_anchor = "      distNote:'\\u0926\\u0942\\u0930\\u093f\\u092f\\u093e\\u0901"
assert hi_anchor in content, "HI i18n anchor not found"

# Find the full distNote line and ctLabel line
hi_dist_end = "\\u0915\\u0930\\u0947\\u0902\\u0964',\n      ctLabel:"
assert hi_dist_end in content, "HI distNote->ctLabel boundary not found"

hi_custom_block = (
    "\\u0915\\u0930\\u0947\\u0902\\u0964',\n"
    "      navCustom:'\\u0915\\u0938\\u094d\\u091f\\u092e \\u092c\\u094d\\u0930\\u093e\\u0902\\u0921\\u093f\\u0902\\u0917',\n"
    "      customEyebrow:'\\u092c\\u0932\\u094d\\u0915 \\u0914\\u0930 \\u092a\\u094d\\u0930\\u093e\\u0907\\u0935\\u0947\\u091f \\u0932\\u0947\\u092c\\u0932',customTitle:'\\u0906\\u092a\\u0915\\u093e \\u092c\\u094d\\u0930\\u093e\\u0902\\u0921\\u0964 \\u0939\\u092e\\u093e\\u0930\\u093e \\u092a\\u093e\\u0928\\u0940\\u0964',\n"
    "      customSubtitle:'\\u0915\\u0938\\u094d\\u091f\\u092e \\u092c\\u094d\\u0930\\u093e\\u0902\\u0921\\u093f\\u0902\\u0917 \\u0935\\u093f\\u0915\\u0932\\u094d\\u092a\\u094b\\u0902 \\u0915\\u0947 \\u0938\\u093e\\u0925 \\u092c\\u0932\\u094d\\u0915 \\u0911\\u0930\\u094d\\u0921\\u0930\\u093f\\u0902\\u0917 \\u2014 \\u0930\\u093f\\u091f\\u0947\\u0932\\u0930\\u094d\\u0938, \\u0935\\u094d\\u092f\\u0935\\u0938\\u093e\\u092f\\u094b\\u0902 \\u0914\\u0930 \\u0907\\u0935\\u0947\\u0902\\u091f \\u0906\\u092f\\u094b\\u091c\\u0915\\u094b\\u0902 \\u0915\\u0947 \\u0932\\u093f\\u090f\\u0964',\n"
    "      whiteLabelTitle:'\\u092a\\u094d\\u0930\\u093e\\u0907\\u0935\\u0947\\u091f \\u0932\\u0947\\u092c\\u0932 \\u2014 \\u0906\\u092a\\u0915\\u093e \\u0905\\u092a\\u0928\\u093e \\u092c\\u094d\\u0930\\u093e\\u0902\\u0921',\n"
    "      whiteLabelDesc:'\\u0905\\u092a\\u0928\\u093e \\u0935\\u0949\\u091f\\u0930 \\u092c\\u094d\\u0930\\u093e\\u0902\\u0921 \\u092c\\u0928\\u093e \\u0930\\u0939\\u0947 \\u0939\\u0948\\u0902? \\u0939\\u092e \\u0906\\u092a\\u0915\\u0947 \\u0928\\u093e\\u092e \\u0914\\u0930 \\u0932\\u094b\\u0917\\u094b \\u0915\\u0947 \\u0924\\u0939\\u0924 \\u092e\\u0948\\u0928\\u094d\\u092f\\u0942\\u092b\\u0948\\u0915\\u094d\\u091a\\u0930 \\u0914\\u0930 \\u092c\\u0949\\u091f\\u0932 \\u0915\\u0930\\u0924\\u0947 \\u0939\\u0948\\u0902 \\u2014 \\u092a\\u0942\\u0930\\u094d\\u0923 \\u0935\\u094d\\u0939\\u093e\\u0907\\u091f-\\u0932\\u0947\\u092c\\u0932 \\u0909\\u0924\\u094d\\u092a\\u093e\\u0926\\u0928\\u0964 \\u092c\\u094b\\u0924\\u0932 \\u092a\\u0930 \\u0930\\u093f\\u0935\\u0947\\u0930\\u093e \\u0938\\u094d\\u092a\\u094d\\u0930\\u093f\\u0902\\u0917\\u094d\\u0938 \\u0915\\u0940 \\u092c\\u094d\\u0930\\u093e\\u0902\\u0921\\u093f\\u0902\\u0917 \\u0928\\u0939\\u0940\\u0902 \\u0906\\u0924\\u0940\\u0964 \\u0906\\u092a \\u0907\\u0938\\u0947 \\u0905\\u092a\\u0928\\u0947 \\u092c\\u094d\\u0930\\u093e\\u0902\\u0921 \\u0915\\u0947 \\u0930\\u0942\\u092a \\u092e\\u0947\\u0902 \\u092c\\u0947\\u091a\\u0947\\u0902\\u0964',\n"
    "      wlFeature1:'\\u0915\\u0938\\u094d\\u091f\\u092e \\u0932\\u0947\\u092c\\u0932 \\u0921\\u093f\\u091c\\u093c\\u093e\\u0907\\u0928 \\u0914\\u0930 \\u092a\\u094d\\u0930\\u093f\\u0902\\u091f\\u093f\\u0902\\u0917',wlFeature2:'\\u0906\\u092a\\u0915\\u093e \\u092c\\u094d\\u0930\\u093e\\u0902\\u0921 \\u0928\\u093e\\u092e, \\u0906\\u092a\\u0915\\u093e \\u0932\\u094b\\u0917\\u094b, \\u0906\\u092a\\u0915\\u0940 \\u092a\\u0939\\u091a\\u093e\\u0928',\n"
    "      wlFeature3:'\\u0935\\u0939\\u0940 7-\\u091a\\u0930\\u0923 \\u092b\\u093f\\u0932\\u094d\\u091f\\u094d\\u0930\\u0947\\u0936\\u0928 \\u0914\\u0930 \\u0917\\u0941\\u0923\\u0935\\u0924\\u094d\\u0924\\u093e \\u092e\\u093e\\u0928\\u0915',wlFeature4:'\\u0928\\u094d\\u092f\\u0942\\u0928\\u0924\\u092e \\u0911\\u0930\\u094d\\u0921\\u0930 \\u092e\\u093e\\u0924\\u094d\\u0930\\u093e \\u0932\\u093e\\u0917\\u0942',\n"
    "      wlMOQ:'MOQ: [To be confirmed] \\u092c\\u0949\\u0915\\u094d\\u0938',\n"
    "      eventLabelTitle:'\\u0936\\u093e\\u0926\\u0940 \\u0914\\u0930 \\u0907\\u0935\\u0947\\u0902\\u091f \\u092c\\u0949\\u091f\\u0932\\u094d\\u0938',\n"
    "      eventLabelDesc:'\\u0936\\u093e\\u0926\\u0940, \\u0938\\u0917\\u093e\\u0908 \\u092f\\u093e \\u0915\\u093f\\u0938\\u0940 \\u0916\\u093e\\u0938 \\u092e\\u094c\\u0915\\u0947 \\u0915\\u0940 \\u0924\\u0948\\u092f\\u093e\\u0930\\u0940? \\u0932\\u0947\\u092c\\u0932 \\u092a\\u0930 \\u0905\\u092a\\u0928\\u0947 \\u0928\\u093e\\u092e, \\u092b\\u094b\\u091f\\u094b \\u092f\\u093e \\u0907\\u0935\\u0947\\u0902\\u091f \\u0935\\u093f\\u0935\\u0930\\u0923 \\u091c\\u094b\\u0921\\u093c\\u0947\\u0902 \\u2014 \\u0930\\u093f\\u0935\\u0947\\u0930\\u093e \\u0938\\u094d\\u092a\\u094d\\u0930\\u093f\\u0902\\u0917\\u094d\\u0938 \\u092c\\u094d\\u0930\\u093e\\u0902\\u0921\\u093f\\u0902\\u0917 \\u0915\\u0947 \\u0938\\u093e\\u0925 \\u2014 \\u090f\\u0915 \\u092f\\u093e\\u0926\\u0917\\u093e\\u0930 \\u0935\\u094d\\u092f\\u0915\\u094d\\u0924\\u093f\\u0917\\u0924 \\u0938\\u094d\\u092a\\u0930\\u094d\\u0936\\u0964',\n"
    "      evFeature1:'\\u0906\\u092a\\u0915\\u093e \\u092b\\u094b\\u091f\\u094b \\u092f\\u093e \\u0928\\u093e\\u092e \\u0932\\u0947\\u092c\\u0932 \\u092a\\u0930 \\u092a\\u094d\\u0930\\u093f\\u0902\\u091f',evFeature2:'\\u0930\\u093f\\u0935\\u0947\\u0930\\u093e \\u0938\\u094d\\u092a\\u094d\\u0930\\u093f\\u0902\\u0917\\u094d\\u0938 \\u092c\\u094d\\u0930\\u093e\\u0902\\u0921\\u093f\\u0902\\u0917 \\u092c\\u094b\\u0924\\u0932 \\u092a\\u0930 \\u0930\\u0939\\u0924\\u0940 \\u0939\\u0948',\n"
    "      evFeature3:'\\u0936\\u093e\\u0926\\u0940, \\u0938\\u0917\\u093e\\u0908, \\u0915\\u0949\\u0930\\u094d\\u092a\\u094b\\u0930\\u0947\\u091f \\u0907\\u0935\\u0947\\u0902\\u091f\\u094d\\u0938 \\u0915\\u0947 \\u0932\\u093f\\u090f \\u0906\\u0926\\u0930\\u094d\\u0936',evFeature4:'\\u0928\\u094d\\u092f\\u0942\\u0928\\u0924\\u092e \\u0911\\u0930\\u094d\\u0921\\u0930 \\u092e\\u093e\\u0924\\u094d\\u0930\\u093e \\u0932\\u093e\\u0917\\u0942',\n"
    "      evMOQ:'MOQ: [To be confirmed] \\u092c\\u0949\\u0915\\u094d\\u0938',\n"
    "      customCTA:'\\u0905\\u092d\\u0940 \\u092a\\u0942\\u091b\\u0947\\u0902',\n"
    "      customNote:'\\u0915\\u0938\\u094d\\u091f\\u092e \\u0911\\u0930\\u094d\\u0921\\u0930 \\u0915\\u0947 \\u0932\\u093f\\u090f \\u0905\\u0917\\u094d\\u0930\\u093f\\u092e \\u092c\\u0941\\u0915\\u093f\\u0902\\u0917 \\u0914\\u0930 \\u0932\\u0947\\u092c\\u0932 \\u0921\\u093f\\u091c\\u093c\\u093e\\u0907\\u0928 \\u0935 \\u0905\\u0928\\u0941\\u092e\\u094b\\u0926\\u0928 \\u0915\\u0947 \\u0932\\u093f\\u090f \\u0938\\u092e\\u092f \\u091a\\u093e\\u0939\\u093f\\u090f\\u0964 \\u0905\\u092a\\u0928\\u0940 \\u0906\\u0935\\u0936\\u094d\\u092f\\u0915\\u0924\\u093e\\u090f\\u0901, \\u0928\\u094d\\u092f\\u0942\\u0928\\u0924\\u092e \\u092e\\u093e\\u0924\\u094d\\u0930\\u093e \\u0914\\u0930 \\u092e\\u0942\\u0932\\u094d\\u092f \\u091c\\u093e\\u0928\\u0928\\u0947 \\u0915\\u0947 \\u0932\\u093f\\u090f \\u0939\\u092e\\u0938\\u0947 \\u0938\\u0902\\u092a\\u0930\\u094d\\u0915 \\u0915\\u0930\\u0947\\u0902\\u0964',\n"
    "      ctLabel:"
)

content = content.replace(hi_dist_end, hi_custom_block, 1)
print("5. HI i18n added")

# ============================================================
# 6. i18n — MR (find the MR distNote->ctLabel boundary)
# ============================================================
# MR distNote ends with \u0915\u0930\u093e.' then ctLabel
mr_dist_end = "\\u0915\\u0930\\u093e.',\n      ctLabel:"
assert mr_dist_end in content, "MR distNote->ctLabel boundary not found"

mr_custom_block = (
    "\\u0915\\u0930\\u093e.',\n"
    "      navCustom:'\\u0915\\u0938\\u094d\\u091f\\u092e \\u092c\\u094d\\u0930\\u093e\\u0902\\u0921\\u093f\\u0902\\u0917',\n"
    "      customEyebrow:'\\u092c\\u0932\\u094d\\u0915 \\u0906\\u0923\\u093f \\u092a\\u094d\\u0930\\u093e\\u092f\\u0935\\u094d\\u0939\\u0947\\u091f \\u0932\\u0947\\u092c\\u0932',customTitle:'\\u0924\\u0941\\u092e\\u091a\\u093e \\u092c\\u094d\\u0930\\u093e\\u0902\\u0921. \\u0906\\u092e\\u091a\\u0947 \\u092a\\u093e\\u0923\\u0940.',\n"
    "      customSubtitle:'\\u0915\\u0938\\u094d\\u091f\\u092e \\u092c\\u094d\\u0930\\u093e\\u0902\\u0921\\u093f\\u0902\\u0917 \\u092a\\u0930\\u094d\\u092f\\u093e\\u092f\\u093e\\u0902\\u0938\\u0939 \\u092c\\u0932\\u094d\\u0915 \\u0911\\u0930\\u094d\\u0921\\u0930\\u093f\\u0902\\u0917 \\u2014 \\u0930\\u093f\\u091f\\u0947\\u0932\\u0930\\u094d\\u0938, \\u0935\\u094d\\u092f\\u093e\\u092a\\u093e\\u0930\\u0940 \\u0906\\u0923\\u093f \\u0907\\u0935\\u094d\\u0939\\u0947\\u0902\\u091f \\u0906\\u092f\\u094b\\u091c\\u0915\\u093e\\u0902\\u0938\\u093e\\u0920\\u0940.',\n"
    "      whiteLabelTitle:'\\u092a\\u094d\\u0930\\u093e\\u092f\\u0935\\u094d\\u0939\\u0947\\u091f \\u0932\\u0947\\u092c\\u0932 \\u2014 \\u0924\\u0941\\u092e\\u091a\\u093e \\u0938\\u094d\\u0935\\u0924:\\u091a\\u093e \\u092c\\u094d\\u0930\\u093e\\u0902\\u0921',\n"
    "      whiteLabelDesc:'\\u0924\\u0941\\u092e\\u091a\\u093e \\u0938\\u094d\\u0935\\u0924:\\u091a\\u093e \\u0935\\u0949\\u091f\\u0930 \\u092c\\u094d\\u0930\\u093e\\u0902\\u0921 \\u0924\\u092f\\u093e\\u0930 \\u0915\\u0930\\u0924 \\u0906\\u0939\\u093e\\u0924? \\u0906\\u092e\\u094d\\u0939\\u0940 \\u0924\\u0941\\u092e\\u091a\\u094d\\u092f\\u093e \\u0928\\u093e\\u0935\\u093e\\u0928\\u0947 \\u0906\\u0923\\u093f \\u0932\\u094b\\u0917\\u094b\\u0905\\u0902\\u0924\\u0930\\u094d\\u0917\\u0924 \\u0909\\u0924\\u094d\\u092a\\u093e\\u0926\\u0928 \\u0906\\u0923\\u093f \\u092c\\u0949\\u091f\\u0932\\u093f\\u0902\\u0917 \\u0915\\u0930\\u0924\\u094b \\u2014 \\u092a\\u0942\\u0930\\u094d\\u0923 \\u0935\\u094d\\u0939\\u093e\\u0907\\u091f-\\u0932\\u0947\\u092c\\u0932 \\u0909\\u0924\\u094d\\u092a\\u093e\\u0926\\u0928. \\u092c\\u094b\\u0924\\u0932\\u0940\\u0935\\u0930 \\u0930\\u093f\\u0935\\u0947\\u0930\\u093e \\u0938\\u094d\\u092a\\u094d\\u0930\\u093f\\u0902\\u0917\\u094d\\u0938\\u091a\\u0940 \\u092c\\u094d\\u0930\\u093e\\u0902\\u0921\\u093f\\u0902\\u0917 \\u0928\\u0938\\u0924\\u0947. \\u0924\\u0941\\u092e\\u094d\\u0939\\u0940 \\u0924\\u0947 \\u0924\\u0941\\u092e\\u091a\\u094d\\u092f\\u093e \\u092c\\u094d\\u0930\\u093e\\u0902\\u0921\\u092e\\u094d\\u0939\\u0923\\u0942\\u0928 \\u0935\\u093f\\u0915\\u093e.',\n"
    "      wlFeature1:'\\u0915\\u0938\\u094d\\u091f\\u092e \\u0932\\u0947\\u092c\\u0932 \\u0921\\u093f\\u091d\\u093e\\u0907\\u0928 \\u0906\\u0923\\u093f \\u092a\\u094d\\u0930\\u093f\\u0902\\u091f\\u093f\\u0902\\u0917',wlFeature2:'\\u0924\\u0941\\u092e\\u091a\\u0947 \\u092c\\u094d\\u0930\\u093e\\u0902\\u0921 \\u0928\\u093e\\u0935, \\u0924\\u0941\\u092e\\u091a\\u093e \\u0932\\u094b\\u0917\\u094b, \\u0924\\u0941\\u092e\\u091a\\u0940 \\u0913\\u0933\\u0916',\n"
    "      wlFeature3:'\\u0924\\u0947\\u091a 7-\\u091a\\u0930\\u0923 \\u092b\\u093f\\u0932\\u094d\\u091f\\u094d\\u0930\\u0947\\u0936\\u0928 \\u0906\\u0923\\u093f \\u0917\\u0941\\u0923\\u0935\\u0924\\u094d\\u0924\\u093e \\u092e\\u093e\\u0928\\u0915\\u0947',wlFeature4:'\\u0928\\u094d\\u092f\\u0942\\u0928\\u0924\\u092e \\u0911\\u0930\\u094d\\u0921\\u0930 \\u092e\\u093e\\u0924\\u094d\\u0930\\u093e \\u0932\\u093e\\u0917\\u0942',\n"
    "      wlMOQ:'MOQ: [To be confirmed] \\u092c\\u0949\\u0915\\u094d\\u0938',\n"
    "      eventLabelTitle:'\\u0932\\u0917\\u094d\\u0928 \\u0906\\u0923\\u093f \\u0907\\u0935\\u094d\\u0939\\u0947\\u0902\\u091f \\u092c\\u0949\\u091f\\u0932\\u094d\\u0938',\n"
    "      eventLabelDesc:'\\u0932\\u0917\\u094d\\u0928, \\u0938\\u093e\\u0916\\u0930\\u092a\\u0941\\u0921\\u093e \\u0915\\u093f\\u0902\\u0935\\u093e \\u0916\\u093e\\u0938 \\u0915\\u093e\\u0930\\u094d\\u092f\\u0915\\u094d\\u0930\\u092e\\u093e\\u091a\\u0940 \\u0924\\u092f\\u093e\\u0930\\u0940? \\u0932\\u0947\\u092c\\u0932\\u0935\\u0930 \\u0924\\u0941\\u092e\\u091a\\u0947 \\u0928\\u093e\\u0935, \\u092b\\u094b\\u091f\\u094b \\u0915\\u093f\\u0902\\u0935\\u093e \\u0915\\u093e\\u0930\\u094d\\u092f\\u0915\\u094d\\u0930\\u092e \\u0924\\u092a\\u0936\\u0940\\u0932 \\u091c\\u094b\\u0921\\u093e \\u2014 \\u0930\\u093f\\u0935\\u0947\\u0930\\u093e \\u0938\\u094d\\u092a\\u094d\\u0930\\u093f\\u0902\\u0917\\u094d\\u0938 \\u092c\\u094d\\u0930\\u093e\\u0902\\u0921\\u093f\\u0902\\u0917\\u0938\\u0939 \\u2014 \\u0924\\u0941\\u092e\\u091a\\u094d\\u092f\\u093e \\u092a\\u093e\\u0939\\u0941\\u0923\\u094d\\u092f\\u093e\\u0902\\u0928\\u093e \\u0932\\u0915\\u094d\\u0937\\u093e\\u0924 \\u0930\\u093e\\u0939\\u0923\\u093e\\u0930\\u093e \\u0935\\u094d\\u092f\\u0915\\u094d\\u0924\\u093f\\u0917\\u0924 \\u0938\\u094d\\u092a\\u0930\\u094d\\u0936.',\n"
    "      evFeature1:'\\u0924\\u0941\\u092e\\u091a\\u093e \\u092b\\u094b\\u091f\\u094b \\u0915\\u093f\\u0902\\u0935\\u093e \\u0928\\u093e\\u0935 \\u0932\\u0947\\u092c\\u0932\\u0935\\u0930 \\u092a\\u094d\\u0930\\u093f\\u0902\\u091f',evFeature2:'\\u0930\\u093f\\u0935\\u0947\\u0930\\u093e \\u0938\\u094d\\u092a\\u094d\\u0930\\u093f\\u0902\\u0917\\u094d\\u0938 \\u092c\\u094d\\u0930\\u093e\\u0902\\u0921\\u093f\\u0902\\u0917 \\u092c\\u094b\\u0924\\u0932\\u0940\\u0935\\u0930 \\u0930\\u093e\\u0939\\u0924\\u0947',\n"
    "      evFeature3:'\\u0932\\u0917\\u094d\\u0928, \\u0938\\u093e\\u0916\\u0930\\u092a\\u0941\\u0921\\u093e, \\u0915\\u0949\\u0930\\u094d\\u092a\\u094b\\u0930\\u0947\\u091f \\u0907\\u0935\\u094d\\u0939\\u0947\\u0902\\u091f\\u094d\\u0938\\u0938\\u093e\\u0920\\u0940 \\u0906\\u0926\\u0930\\u094d\\u0936',evFeature4:'\\u0928\\u094d\\u092f\\u0942\\u0928\\u0924\\u092e \\u0911\\u0930\\u094d\\u0921\\u0930 \\u092e\\u093e\\u0924\\u094d\\u0930\\u093e \\u0932\\u093e\\u0917\\u0942',\n"
    "      evMOQ:'MOQ: [To be confirmed] \\u092c\\u0949\\u0915\\u094d\\u0938',\n"
    "      customCTA:'\\u0906\\u0924\\u093e \\u0935\\u093f\\u091a\\u093e\\u0930\\u093e',\n"
    "      customNote:'\\u0915\\u0938\\u094d\\u091f\\u092e \\u0911\\u0930\\u094d\\u0921\\u0930\\u0938\\u093e\\u0920\\u0940 \\u0906\\u0917\\u093e\\u0909 \\u092c\\u0941\\u0915\\u093f\\u0902\\u0917 \\u0906\\u0923\\u093f \\u0932\\u0947\\u092c\\u0932 \\u0921\\u093f\\u091d\\u093e\\u0907\\u0928 \\u0935 \\u092e\\u093e\\u0928\\u094d\\u092f\\u0924\\u0947\\u0938\\u093e\\u0920\\u0940 \\u0935\\u0947\\u0933 \\u0932\\u093e\\u0917\\u0924\\u094b. \\u0924\\u0941\\u092e\\u091a\\u094d\\u092f\\u093e \\u0917\\u0930\\u091c\\u093e, \\u0928\\u094d\\u092f\\u0942\\u0928\\u0924\\u092e \\u092e\\u093e\\u0924\\u094d\\u0930\\u093e \\u0906\\u0923\\u093f \\u0915\\u093f\\u0902\\u092e\\u0924\\u0940 \\u091c\\u093e\\u0923\\u0942\\u0928 \\u0918\\u0947\\u0923\\u094d\\u092f\\u093e\\u0938\\u093e\\u0920\\u0940 \\u0906\\u092e\\u091a\\u094d\\u092f\\u093e\\u0936\\u0940 \\u0938\\u0902\\u092a\\u0930\\u094d\\u0915 \\u0915\\u0930\\u093e.',\n"
    "      ctLabel:"
)

content = content.replace(mr_dist_end, mr_custom_block, 1)
print("6. MR i18n added")

# ============================================================
# WRITE
# ============================================================
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nAll done!")
