import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# 1. CSS — Quality grid from 3 to 4 cols + strength specs + complaint badge
# ============================================================
# Change quality-cols from repeat(3,1fr) to repeat(4,1fr)
content = content.replace(
    ".quality-cols{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(2rem,4vw,3.5rem)}",
    ".quality-cols{display:grid;grid-template-columns:repeat(4,1fr);gap:clamp(2rem,4vw,3.5rem)}"
)
# Update tablet breakpoint from 1fr 1fr to repeat(2,1fr) (same, just verify)
# Update mobile breakpoint - already 1fr, fine

# Add strength CSS before the UPCOMING PRODUCTS or after QUALITY section CSS
strength_css = """
.strength-specs{list-style:none;margin:20px 0}
.strength-specs li{
  display:flex;justify-content:space-between;padding:10px 0;
  border-top:1px solid rgba(11,74,63,0.1);font-size:13px;
}
.strength-specs li:first-child{border-top:none}
.spec-label{color:rgba(8,33,31,0.6);font-weight:500}
.spec-value{color:#08211F;font-weight:600;text-align:right}
.spec-value span{font-weight:400;color:rgba(8,33,31,0.5);font-size:11px;display:block}
.complaint-badge{
  margin-top:24px;padding:20px;background:rgba(11,74,63,0.06);
  border:1px solid rgba(201,162,39,0.3);border-radius:10px;text-align:center;
}
.complaint-number{
  display:block;font-family:var(--serif);font-size:32px;color:#0B4A3F;font-weight:600;
}
.complaint-text{
  display:block;font-size:11px;letter-spacing:1px;text-transform:uppercase;
  color:rgba(8,33,31,0.55);margin-top:4px;
}

"""

# Insert before UPCOMING PRODUCTS CSS
css_anchor = "/* \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 UPCOMING PRODUCTS \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 */"
assert css_anchor in content, "UPCOMING PRODUCTS CSS anchor not found"
content = content.replace(css_anchor, strength_css + css_anchor)
print("1a. Strength CSS added")

# ============================================================
# 2. CSS — Popup styles for product cards
# ============================================================
popup_css = """
/* ═══════════ BOTTLE HOVER POPUP ═══════════ */
.product-card{perspective:1200px}
.bottle-hover-popup{
  position:absolute;bottom:calc(100% + 12px);left:50%;
  transform:translateX(-50%) translateY(10px);
  width:260px;
  background:linear-gradient(145deg,#0E4038 0%,#08211F 100%);
  border:1px solid rgba(201,162,39,0.3);border-radius:14px;padding:20px;
  opacity:0;visibility:hidden;pointer-events:none;
  transition:opacity .35s ease,transform .35s cubic-bezier(.2,.7,.3,1);
  box-shadow:0 20px 50px rgba(0,0,0,0.4);z-index:20;
}
.product-card:hover .bottle-hover-popup{
  opacity:1;visibility:visible;transform:translateX(-50%) translateY(0);
}
.bottle-hover-popup::after{
  content:"";position:absolute;top:100%;left:50%;transform:translateX(-50%);
  border:8px solid transparent;border-top-color:#08211F;
}
.popup-3d-stage{
  height:140px;display:flex;align-items:center;justify-content:center;margin-bottom:14px;
}
.popup-bottle-img{
  height:130px;width:auto;
  filter:drop-shadow(0 12px 20px rgba(0,0,0,0.4));
  transition:transform .4s ease;transform:rotateY(0deg);
}
.product-card:hover .popup-bottle-img{
  animation:popupTilt 3s ease-in-out infinite;
}
@keyframes popupTilt{
  0%,100%{transform:rotateY(-12deg)}
  50%{transform:rotateY(12deg)}
}
.popup-specs h4{
  font-family:var(--serif);font-size:15px;color:#F5D583;
  margin-bottom:10px;text-align:center;
}
.popup-specs ul{list-style:none;margin-bottom:12px}
.popup-specs li{
  font-size:11px;color:rgba(255,255,255,0.75);padding:5px 0;
  display:flex;justify-content:space-between;
}
.popup-specs li strong{color:#fff}
.popup-zero-badge{
  display:block;text-align:center;font-size:11px;
  color:#C9A227;font-weight:600;padding-top:10px;
  border-top:1px solid rgba(255,255,255,0.1);
}
@media(max-width:768px){
  .bottle-hover-popup{display:none}
}
.bottle-hover-popup.mobile-open{
  opacity:1;visibility:visible;
  transform:translateX(-50%) translateY(0);display:block;
}

"""

# Insert before QUALITY CSS section
qual_css_anchor = "/* \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 QUALITY \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 */"
assert qual_css_anchor in content, "QUALITY CSS anchor not found"
content = content.replace(qual_css_anchor, popup_css + qual_css_anchor)
print("1b. Popup CSS added")

# ============================================================
# 3. HTML — Add strength column to Quality section
# ============================================================
quality_col_anchor = """      <div class="quality-col rv rv-d2">
        <div class="quality-icon">
          <svg viewBox="0 0 24 24"><path d="M12 2l3 6h6l-5 4 2 7-6-4-6 4 2-7-5-4h6z"/></svg>
        </div>
        <h3 data-i18n="qualCertH">Certification</h3>"""

# Find the end of the Certification column and add strength after it
# The cert col ends with </div> then </div> (closing quality-cols)
cert_col_end = "        <h3 data-i18n=\"qualCertH\">Certification</h3>\n        <p data-i18n=\"qualCertP\">"
assert cert_col_end in content, "Cert col anchor not found"

# Find the closing </div> of the cert quality-col, then insert strength col
# The pattern: qualCertP paragraph ends with </p>\n      </div>\n    </div>  (closing quality-cols)
old_quality_cols_end = "      </div>\n    </div>\n\n    <div class=\"cert-row"
assert old_quality_cols_end in content, "Quality cols end anchor not found"

strength_html = """      </div>
      <div class="quality-col strength-col rv rv-d3">
        <div class="quality-icon">
          <svg viewBox="0 0 60 60" width="44" height="44">
            <rect x="20" y="8" width="20" height="44" rx="3" fill="none" stroke="#C9A227" stroke-width="1.5"/>
            <path d="M20,20 L40,20" stroke="#C9A227" stroke-width="1"/>
            <path d="M15,30 L45,30" stroke="#C9A227" stroke-width="1" stroke-dasharray="2,2"/>
            <path d="M30,42 L30,52 M25,47 L35,47" stroke="#C9A227" stroke-width="1.5"/>
          </svg>
        </div>
        <h3 data-i18n="strengthTitle">Bottle Strength &amp; Durability</h3>
        <p data-i18n="strengthDesc">Every Rivera Springs bottle is engineered from virgin, food-grade PET (Polyethylene Terephthalate) \u2014 not recycled or reprocessed material \u2014 for maximum structural integrity and safety.</p>
        <ul class="strength-specs">
          <li>
            <span class="spec-label" data-i18n="specWallLabel">Wall Thickness</span>
            <span class="spec-value">[X.XX] mm</span>
          </li>
          <li>
            <span class="spec-label" data-i18n="specTopLoadLabel">Top-Load Strength</span>
            <span class="spec-value">[XX] kg <span data-i18n="specTopLoadNote">(safe palletized stacking)</span></span>
          </li>
          <li>
            <span class="spec-label" data-i18n="specDropLabel">Drop-Test Resistance</span>
            <span class="spec-value">[X.X] m <span data-i18n="specDropNote">(filled bottle, per IS 14543)</span></span>
          </li>
          <li>
            <span class="spec-label" data-i18n="specESCRLabel">ESCR</span>
            <span class="spec-value" data-i18n="specESCRValue">High resistance to environmental stress cracking</span>
          </li>
        </ul>
        <div class="complaint-badge">
          <span class="complaint-number">0.00%</span>
          <span class="complaint-text" data-i18n="complaintText">Leakage complaints received to date</span>
        </div>
      </div>
    </div>

    <div class="cert-row"""

content = content.replace(old_quality_cols_end, strength_html)
print("2. Strength HTML column added")

# ============================================================
# 4. HTML — Add hover popups to product cards
# ============================================================
# Each product card needs a popup inserted before its closing </div>
# 250ml card
popup_250 = """      <div class="bottle-hover-popup">
        <div class="popup-3d-stage">
          <div class="popup-bottle-img" style="width:40px;height:120px;background:linear-gradient(180deg,rgba(201,162,39,0.2),rgba(201,162,39,0.05));border-radius:6px 6px 4px 4px;border:1px solid rgba(201,162,39,0.3)"></div>
        </div>
        <div class="popup-specs">
          <h4 data-i18n="popupStrengthTitle">Built to Last</h4>
          <ul>
            <li><span data-i18n="specWallLabel">Wall Thickness</span> <strong>[X.XX] mm</strong></li>
            <li><span data-i18n="specTopLoadLabel">Top-Load</span> <strong>[XX] kg</strong></li>
            <li><span data-i18n="specDropLabel">Drop-Tested</span> <strong>[X.X] m</strong></li>
          </ul>
          <span class="popup-zero-badge">0.00% <span data-i18n="popupZeroText">leakage complaints</span></span>
        </div>
      </div>"""

popup_500 = popup_250  # Same specs placeholder for all sizes
popup_1L = popup_250

# Insert popup before closing </div> of each product-card
# 250ml card ends with product-use div then </div>
old_250_end = '        <div class="product-use" data-i18n="p250use">Perfect for on-the-go. Toss it in your bag, keep one at the counter, hand it out at events.</div>\n      </div>'
new_250_end = '        <div class="product-use" data-i18n="p250use">Perfect for on-the-go. Toss it in your bag, keep one at the counter, hand it out at events.</div>\n' + popup_250 + '\n      </div>'
assert old_250_end in content, "250ml card end not found"
content = content.replace(old_250_end, new_250_end)

old_500_end = '        <div class="product-use" data-i18n="p500use">The everyday essential. For retail counters, restaurants, and daily hydration.</div>\n      </div>'
new_500_end = '        <div class="product-use" data-i18n="p500use">The everyday essential. For retail counters, restaurants, and daily hydration.</div>\n' + popup_500 + '\n      </div>'
assert old_500_end in content, "500ml card end not found"
content = content.replace(old_500_end, new_500_end)

old_1L_end = '        <div class="product-use" data-i18n="p1Luse">For home &amp; office. Daily hydration, family dining, and general trade.</div>\n      </div>'
new_1L_end = '        <div class="product-use" data-i18n="p1Luse">For home &amp; office. Daily hydration, family dining, and general trade.</div>\n' + popup_1L + '\n      </div>'
assert old_1L_end in content, "1L card end not found"
content = content.replace(old_1L_end, new_1L_end)
print("3. Popup HTML added to all 3 product cards")

# ============================================================
# 5. JS — Add mobile tap-to-toggle for popups
# ============================================================
# Find the closing </script> of the main JS block and insert before it
# Let's find a unique JS anchor - the i18n system or scroll handler
js_code = """
// Mobile tap-to-toggle for bottle hover popups
if(window.matchMedia('(hover:none)').matches){
  document.querySelectorAll('.product-card').forEach(function(card){
    var popup=card.querySelector('.bottle-hover-popup');
    if(popup){
      popup.style.display='block';
      card.addEventListener('click',function(e){
        e.stopPropagation();
        var isOpen=popup.classList.contains('mobile-open');
        document.querySelectorAll('.bottle-hover-popup').forEach(function(p){p.classList.remove('mobile-open')});
        if(!isOpen) popup.classList.add('mobile-open');
      });
    }
  });
  document.addEventListener('click',function(){
    document.querySelectorAll('.bottle-hover-popup').forEach(function(p){p.classList.remove('mobile-open')});
  });
}
"""

# Find the last </script> before </body>
# Insert the JS before the closing of the main script
# Let's find the footer/end pattern
js_anchor = "\n</script>\n</body>"
assert js_anchor in content, "JS anchor </script></body> not found"
content = content.replace(js_anchor, js_code + "\n</script>\n</body>")
print("4. Mobile tap JS added")

# ============================================================
# 6. i18n — EN
# ============================================================
en_quality_anchor = "      certBIS:'BIS Certified',certFSSAI:'FSSAI Licensed',"
assert en_quality_anchor in content, "EN quality i18n anchor not found"
en_strength_i18n = (
    "      certBIS:'BIS Certified',certFSSAI:'FSSAI Licensed',\n"
    "      strengthTitle:'Bottle Strength & Durability',\n"
    "      strengthDesc:'Every Rivera Springs bottle is engineered from virgin, food-grade PET (Polyethylene Terephthalate) \\u2014 not recycled or reprocessed material \\u2014 for maximum structural integrity and safety.',\n"
    "      specWallLabel:'Wall Thickness',specTopLoadLabel:'Top-Load Strength',specTopLoadNote:'(safe palletized stacking)',\n"
    "      specDropLabel:'Drop-Test Resistance',specDropNote:'(filled bottle, per IS 14543)',\n"
    "      specESCRLabel:'ESCR',specESCRValue:'High resistance to environmental stress cracking',\n"
    "      complaintText:'Leakage complaints received to date',\n"
    "      popupStrengthTitle:'Built to Last',popupZeroText:'leakage complaints',"
)
content = content.replace(en_quality_anchor, en_strength_i18n)
print("5. EN i18n added")

# ============================================================
# 7. i18n — HI (escaped unicode)
# ============================================================
hi_quality_anchor = "      certBIS:'BIS \\u092a\\u094d\\u0930\\u092e\\u093e\\u0923\\u093f\\u0924',certFSSAI:'FSSAI \\u0932\\u093e\\u0907\\u0938\\u0947\\u0902\\u0938\\u094d\\u0921',"
assert hi_quality_anchor in content, "HI quality i18n anchor not found"
hi_strength_i18n = (
    "      certBIS:'BIS \\u092a\\u094d\\u0930\\u092e\\u093e\\u0923\\u093f\\u0924',certFSSAI:'FSSAI \\u0932\\u093e\\u0907\\u0938\\u0947\\u0902\\u0938\\u094d\\u0921',\n"
    "      strengthTitle:'\\u092c\\u094b\\u0924\\u0932 \\u092e\\u091c\\u093c\\u092c\\u0942\\u0924\\u0940 \\u0914\\u0930 \\u091f\\u093f\\u0915\\u093e\\u090a\\u092a\\u0928',\n"
    "      strengthDesc:'\\u0939\\u0930 \\u0930\\u093f\\u0935\\u0947\\u0930\\u093e \\u0938\\u094d\\u092a\\u094d\\u0930\\u093f\\u0902\\u0917\\u094d\\u0938 \\u092c\\u094b\\u0924\\u0932 \\u0935\\u0930\\u094d\\u091c\\u093f\\u0928, \\u092b\\u0942\\u0921-\\u0917\\u094d\\u0930\\u0947\\u0921 PET (\\u092a\\u0949\\u0932\\u0940\\u0907\\u0925\\u093f\\u0932\\u0940\\u0928 \\u091f\\u0947\\u0930\\u0947\\u092b\\u094d\\u0925\\u0932\\u0947\\u091f) \\u0938\\u0947 \\u092c\\u0928\\u0940 \\u0939\\u0948 \\u2014 \\u0930\\u0940\\u0938\\u093e\\u0907\\u0915\\u094d\\u0932\\u094d\\u0921 \\u092f\\u093e \\u0930\\u0940\\u092a\\u094d\\u0930\\u094b\\u0938\\u0947\\u0938\\u094d\\u0921 \\u0938\\u093e\\u092e\\u0917\\u094d\\u0930\\u0940 \\u0928\\u0939\\u0940\\u0902 \\u2014 \\u0905\\u0927\\u093f\\u0915\\u0924\\u092e \\u0938\\u0902\\u0930\\u091a\\u0928\\u093e\\u0924\\u094d\\u092e\\u0915 \\u092e\\u091c\\u093c\\u092c\\u0942\\u0924\\u0940 \\u0914\\u0930 \\u0938\\u0941\\u0930\\u0915\\u094d\\u0937\\u093e \\u0915\\u0947 \\u0932\\u093f\\u090f\\u0964',\n"
    "      specWallLabel:'\\u0926\\u0940\\u0935\\u093e\\u0930 \\u092e\\u094b\\u091f\\u093e\\u0908',specTopLoadLabel:'\\u091f\\u0949\\u092a-\\u0932\\u094b\\u0921 \\u0915\\u094d\\u0937\\u092e\\u0924\\u093e',specTopLoadNote:'(\\u0938\\u0941\\u0930\\u0915\\u094d\\u0937\\u093f\\u0924 \\u092a\\u0948\\u0932\\u0947\\u091f \\u0938\\u094d\\u091f\\u0948\\u0915\\u093f\\u0902\\u0917)',\n"
    "      specDropLabel:'\\u0921\\u094d\\u0930\\u0949\\u092a-\\u091f\\u0947\\u0938\\u094d\\u091f \\u092a\\u094d\\u0930\\u0924\\u093f\\u0930\\u094b\\u0927',specDropNote:'(\\u092d\\u0930\\u0940 \\u092c\\u094b\\u0924\\u0932, IS 14543 \\u0905\\u0928\\u0941\\u0938\\u093e\\u0930)',\n"
    "      specESCRLabel:'ESCR',specESCRValue:'\\u092a\\u0930\\u094d\\u092f\\u093e\\u0935\\u0930\\u0923\\u0940\\u092f \\u0924\\u0928\\u093e\\u0935 \\u0926\\u0930\\u093e\\u0930 \\u0915\\u0947 \\u092a\\u094d\\u0930\\u0924\\u093f \\u0909\\u091a\\u094d\\u091a \\u092a\\u094d\\u0930\\u0924\\u093f\\u0930\\u094b\\u0927',\n"
    "      complaintText:'\\u0906\\u091c \\u0924\\u0915 \\u0930\\u093f\\u0938\\u093e\\u0935 \\u0915\\u0940 \\u0936\\u093f\\u0915\\u093e\\u092f\\u0924\\u0947\\u0902 \\u092a\\u094d\\u0930\\u093e\\u092a\\u094d\\u0924',\n"
    "      popupStrengthTitle:'\\u092e\\u091c\\u093c\\u092c\\u0942\\u0924 \\u092c\\u0928\\u093e\\u0935\\u091f',popupZeroText:'\\u0930\\u093f\\u0938\\u093e\\u0935 \\u0936\\u093f\\u0915\\u093e\\u092f\\u0924\\u0947\\u0902',"
)
content = content.replace(hi_quality_anchor, hi_strength_i18n)
print("6. HI i18n added")

# ============================================================
# 8. i18n — MR (escaped unicode)
# ============================================================
mr_quality_anchor = "      certBIS:'BIS \\u092a\\u094d\\u0930\\u092e\\u093e\\u0923\\u093f\\u0924',certFSSAI:'FSSAI \\u0932\\u093e\\u092f\\u0938\\u0928\\u094d\\u0938',"
assert mr_quality_anchor in content, "MR quality i18n anchor not found"
mr_strength_i18n = (
    "      certBIS:'BIS \\u092a\\u094d\\u0930\\u092e\\u093e\\u0923\\u093f\\u0924',certFSSAI:'FSSAI \\u0932\\u093e\\u092f\\u0938\\u0928\\u094d\\u0938',\n"
    "      strengthTitle:'\\u092c\\u094b\\u091f\\u0932 \\u092e\\u091c\\u092c\\u0942\\u0924\\u0940 \\u0906\\u0923\\u093f \\u091f\\u093f\\u0915\\u093e\\u090a\\u092a\\u0923\\u093e',\n"
    "      strengthDesc:'\\u092a\\u094d\\u0930\\u0924\\u094d\\u092f\\u0947\\u0915 \\u0930\\u093f\\u0935\\u0947\\u0930\\u093e \\u0938\\u094d\\u092a\\u094d\\u0930\\u093f\\u0902\\u0917\\u094d\\u0938 \\u092c\\u094b\\u091f\\u0932 \\u0935\\u094d\\u0939\\u0930\\u094d\\u091c\\u093f\\u0928, \\u092b\\u0942\\u0921-\\u0917\\u094d\\u0930\\u0947\\u0921 PET (\\u092a\\u0949\\u0932\\u0940\\u0907\\u0925\\u093f\\u0932\\u0940\\u0928 \\u091f\\u0947\\u0930\\u0947\\u092b\\u094d\\u0925\\u0932\\u0947\\u091f) \\u092a\\u093e\\u0938\\u0942\\u0928 \\u0924\\u092f\\u093e\\u0930 \\u0915\\u0947\\u0932\\u0940 \\u0906\\u0939\\u0947 \\u2014 \\u0930\\u093f\\u0938\\u093e\\u092f\\u0915\\u0932 \\u0915\\u093f\\u0902\\u0935\\u093e \\u0930\\u093f\\u092a\\u094d\\u0930\\u094b\\u0938\\u0947\\u0938\\u094d\\u0921 \\u0938\\u093e\\u092e\\u0917\\u094d\\u0930\\u0940 \\u0928\\u0935\\u094d\\u0939\\u0947 \\u2014 \\u091c\\u093e\\u0938\\u094d\\u0924\\u0940\\u0924 \\u091c\\u093e\\u0938\\u094d\\u0924 \\u0938\\u0902\\u0930\\u091a\\u0928\\u093e\\u0924\\u094d\\u092e\\u0915 \\u092e\\u091c\\u092c\\u0942\\u0924\\u0940 \\u0906\\u0923\\u093f \\u0938\\u0941\\u0930\\u0915\\u094d\\u0937\\u093f\\u0924\\u0924\\u0947\\u0938\\u093e\\u0920\\u0940.',\n"
    "      specWallLabel:'\\u092d\\u093f\\u0902\\u0924\\u0940\\u091a\\u0940 \\u091c\\u093e\\u0921\\u0940',specTopLoadLabel:'\\u091f\\u0949\\u092a-\\u0932\\u094b\\u0921 \\u0915\\u094d\\u0937\\u092e\\u0924\\u093e',specTopLoadNote:'(\\u0938\\u0941\\u0930\\u0915\\u094d\\u0937\\u093f\\u0924 \\u092a\\u0945\\u0932\\u0947\\u091f \\u0938\\u094d\\u091f\\u0945\\u0915\\u093f\\u0902\\u0917)',\n"
    "      specDropLabel:'\\u0921\\u094d\\u0930\\u0949\\u092a-\\u091f\\u0947\\u0938\\u094d\\u091f \\u092a\\u094d\\u0930\\u0924\\u093f\\u0930\\u094b\\u0927',specDropNote:'(\\u092d\\u0930\\u0932\\u0947\\u0932\\u0940 \\u092c\\u094b\\u091f\\u0932, IS 14543 \\u0905\\u0928\\u0941\\u0938\\u093e\\u0930)',\n"
    "      specESCRLabel:'ESCR',specESCRValue:'\\u092a\\u0930\\u094d\\u092f\\u093e\\u0935\\u0930\\u0923\\u0940\\u092f \\u0924\\u093e\\u0923 \\u092d\\u0947\\u0917\\u093e\\u0902\\u0936\\u0940 \\u0909\\u091a\\u094d\\u091a \\u092a\\u094d\\u0930\\u0924\\u093f\\u0930\\u094b\\u0927',\n"
    "      complaintText:'\\u0906\\u091c\\u092a\\u0930\\u094d\\u092f\\u0902\\u0924 \\u0917\\u0933\\u0924\\u0940\\u091a\\u094d\\u092f\\u093e \\u0924\\u0915\\u094d\\u0930\\u093e\\u0930\\u0940 \\u092a\\u094d\\u0930\\u093e\\u092a\\u094d\\u0924',\n"
    "      popupStrengthTitle:'\\u092e\\u091c\\u092c\\u0942\\u0924 \\u092c\\u093e\\u0902\\u0927\\u0923\\u0940',popupZeroText:'\\u0917\\u0933\\u0924\\u0940 \\u0924\\u0915\\u094d\\u0930\\u093e\\u0930\\u0940',"
)
content = content.replace(mr_quality_anchor, mr_strength_i18n)
print("7. MR i18n added")

# ============================================================
# WRITE
# ============================================================
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nAll done!")
