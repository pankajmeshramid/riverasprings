with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# 1. CSS — Replace old journey styles with new animated diagram
# ============================================================
old_css = """/* Journey process line */
.journey{margin-top:2.5rem;position:relative;overflow-x:auto;padding-bottom:.5rem}
.journey-track{display:flex;align-items:flex-start;gap:0;min-width:max-content;position:relative}
.journey-track::before{
  content:'';position:absolute;top:20px;left:20px;right:20px;height:2px;
  background:linear-gradient(90deg,var(--teal),var(--gold) 50%,var(--teal));opacity:.2;z-index:0;
}
.journey-step{display:flex;flex-direction:column;align-items:center;gap:.35rem;flex:1;min-width:72px;position:relative;z-index:1}
.journey-icon{
  width:40px;height:40px;border-radius:50%;flex-shrink:0;
  background:var(--mist);display:flex;align-items:center;justify-content:center;
  border:2px solid var(--teal);transition:border-color .3s,background .3s;
}
.journey-icon:hover{border-color:var(--gold);background:rgba(201,162,39,.08)}
.journey-icon svg{width:18px;height:18px;stroke:var(--teal);fill:none;stroke-width:1.8}
.journey-name{font-size:.58rem;letter-spacing:.08em;text-transform:uppercase;color:var(--teal);font-weight:600;text-align:center;line-height:1.3}
.journey-arrow{display:flex;align-items:center;padding-top:10px;color:var(--gold);opacity:.35;font-size:.7rem}"""

new_css = """/* Water journey animated process flow */
.water-journey{max-width:1100px;margin:80px auto 0;padding:0 24px}
.journey-title{
  text-align:center;font-family:var(--serif);
  font-size:clamp(24px,3vw,34px);color:#08211F;margin-bottom:56px;
}
.journey-track{position:relative}
.journey-line{
  position:absolute;top:28px;left:0;width:100%;height:40px;z-index:0;pointer-events:none;
}
#journeyPath{stroke-dashoffset:0;animation:flowDash 20s linear infinite}
@keyframes flowDash{to{stroke-dashoffset:-200}}
.journey-nodes{
  display:flex;justify-content:space-between;align-items:flex-start;position:relative;z-index:1;
}
.journey-node{
  display:flex;flex-direction:column;align-items:center;flex:1;
  opacity:0;transform:translateY(20px);
  transition:opacity .6s cubic-bezier(.16,1,.3,1),transform .6s cubic-bezier(.16,1,.3,1);
}
.journey-node.in-view{opacity:1;transform:translateY(0)}
.node-icon{
  width:56px;height:56px;border-radius:50%;background:#FAFAF7;
  border:1.5px solid rgba(11,74,63,0.2);
  display:flex;align-items:center;justify-content:center;
  padding:12px;margin-bottom:12px;
  transition:transform .3s ease,border-color .3s ease,box-shadow .3s ease;
}
.journey-node:hover .node-icon{
  transform:scale(1.12) translateY(-4px);
  border-color:#C9A227;box-shadow:0 8px 24px rgba(201,162,39,0.25);
}
.node-icon svg{width:100%;height:100%}
.node-icon-final{
  background:linear-gradient(145deg,#0B4A3F,#08211F);border-color:#C9A227;
}
.node-label{
  font-size:11px;letter-spacing:.5px;text-align:center;
  color:rgba(8,33,31,0.7);font-weight:500;max-width:90px;line-height:1.3;
}
.node-label-final{
  color:#C9A227;font-weight:700;font-family:var(--serif);font-size:15px;
}
.journey-node:nth-child(1){transition-delay:0s}
.journey-node:nth-child(2){transition-delay:.08s}
.journey-node:nth-child(3){transition-delay:.16s}
.journey-node:nth-child(4){transition-delay:.24s}
.journey-node:nth-child(5){transition-delay:.32s}
.journey-node:nth-child(6){transition-delay:.40s}
.journey-node:nth-child(7){transition-delay:.48s}
.journey-node:nth-child(8){transition-delay:.56s}"""

assert old_css in content, "Old journey CSS not found"
content = content.replace(old_css, new_css)
print("1. CSS replaced")

# Update mobile breakpoints — old ones reference .journey-track, .journey-name, .journey-icon
content = content.replace(
    "  .journey-track{gap:0;padding:0 0.5rem}\n  .journey-name{font-size:.52rem}\n  .journey-icon{width:34px;height:34px}",
    ""
)
print("1b. Old mobile journey CSS removed")

# Add mobile vertical layout in the @media(max-width:820px) or separate block
# Insert before PRODUCTS CSS section
products_css = "/* \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 PRODUCTS \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 */"
mobile_journey_css = """
@media(max-width:767px){
  .journey-line{display:none}
  .journey-nodes{
    flex-direction:column;align-items:flex-start;gap:0;
    position:relative;padding-left:32px;
  }
  .journey-nodes::before{
    content:"";position:absolute;left:27px;top:28px;bottom:28px;width:2px;
    background:repeating-linear-gradient(180deg,#C9A227 0,#C9A227 6px,transparent 6px,transparent 12px);
  }
  .journey-node{
    flex-direction:row;align-items:center;gap:16px;margin-bottom:24px;width:100%;
  }
  .node-icon{width:44px;height:44px;margin-bottom:0;flex-shrink:0}
  .node-label{text-align:left;max-width:none;font-size:13px}
  .water-journey{margin-top:48px}
  .journey-title{margin-bottom:36px}
}

"""
content = content.replace(products_css, mobile_journey_css + products_css)
print("1c. Mobile journey CSS added")

# ============================================================
# 2. HTML — Replace old journey chain with new animated diagram
# ============================================================
old_html = """        <div class="journey rv rv-d3" aria-label="Water purification journey">
          <div class="journey-track">
            <div class="journey-step">
              <div class="journey-icon"><svg viewBox="0 0 24 24"><path d="M12 2L2 22h20L12 2z"/><path d="M8 16c2-3 4-2 4-6"/><path d="M12 10c0 4 2 3 4 6"/></svg></div>
              <span class="journey-name" data-i18n="jWaterfall">Waterfall</span>
            </div>
            <span class="journey-arrow">\u203a</span>"""

# I need to find the full old HTML block. Let me use start/end anchors
old_journey_start = '        <div class="journey rv rv-d3" aria-label="Water purification journey">'
old_journey_end = '        </div>\n\n        <dl class="source-stats'

assert old_journey_start in content, "Old journey HTML start not found"
assert old_journey_end in content, "Old journey HTML end not found"

start_idx = content.index(old_journey_start)
end_idx = content.index(old_journey_end)
old_journey_html = content[start_idx:end_idx]

new_journey_html = """        <div class="water-journey rv rv-d3">
          <h3 class="journey-title" data-i18n="journeyTitle">The Journey of Every Drop</h3>
          <div class="journey-track">
            <svg class="journey-line" viewBox="0 0 1200 40" preserveAspectRatio="none">
              <path id="journeyPath" d="M 20,20 L 1180,20" stroke="url(#flowGrad)" stroke-width="2" fill="none" stroke-dasharray="6,6"/>
              <defs>
                <linearGradient id="flowGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#0B4A3F"/>
                  <stop offset="50%" stop-color="#C9A227"/>
                  <stop offset="100%" stop-color="#0B4A3F"/>
                </linearGradient>
              </defs>
            </svg>
            <div class="journey-nodes">
              <div class="journey-node">
                <div class="node-icon">
                  <svg viewBox="0 0 48 48"><path d="M14,6 L14,20 Q14,26 18,30 L14,44 M24,6 L24,22 Q24,28 28,32 L26,44 M34,6 L34,18 Q34,24 30,28 L32,44" stroke="#0B4A3F" stroke-width="2" fill="none" stroke-linecap="round"/></svg>
                </div>
                <span class="node-label" data-i18n="stepWaterfall">Waterfall</span>
              </div>
              <div class="journey-node">
                <div class="node-icon">
                  <svg viewBox="0 0 48 48"><circle cx="24" cy="30" r="12" fill="none" stroke="#0B4A3F" stroke-width="2"/><path d="M24,6 Q30,16 24,22 Q18,16 24,6Z" fill="#0B4A3F"/></svg>
                </div>
                <span class="node-label" data-i18n="stepSpring">Spring</span>
              </div>
              <div class="journey-node">
                <div class="node-icon">
                  <svg viewBox="0 0 48 48"><rect x="8" y="14" width="32" height="6" rx="2" fill="#C9A227"/><rect x="8" y="22" width="32" height="6" rx="2" fill="#C9A227" opacity="0.7"/><rect x="8" y="30" width="32" height="6" rx="2" fill="#C9A227" opacity="0.45"/></svg>
                </div>
                <span class="node-label" data-i18n="stepSand">Sand Filtration</span>
              </div>
              <div class="journey-node">
                <div class="node-icon">
                  <svg viewBox="0 0 48 48"><polygon points="24,6 40,16 40,32 24,42 8,32 8,16" fill="none" stroke="#0B4A3F" stroke-width="2"/><circle cx="24" cy="24" r="5" fill="#0B4A3F"/></svg>
                </div>
                <span class="node-label" data-i18n="stepCarbon">Carbon Filtration</span>
              </div>
              <div class="journey-node">
                <div class="node-icon">
                  <svg viewBox="0 0 48 48"><circle cx="18" cy="24" r="10" fill="none" stroke="#0B4A3F" stroke-width="2"/><circle cx="30" cy="24" r="10" fill="none" stroke="#C9A227" stroke-width="2"/></svg>
                </div>
                <span class="node-label" data-i18n="stepRO">Reverse Osmosis</span>
              </div>
              <div class="journey-node">
                <div class="node-icon">
                  <svg viewBox="0 0 48 48"><circle cx="24" cy="24" r="8" fill="#C9A227"/><g stroke="#C9A227" stroke-width="2"><line x1="24" y1="4" x2="24" y2="10"/><line x1="24" y1="38" x2="24" y2="44"/><line x1="4" y1="24" x2="10" y2="24"/><line x1="38" y1="24" x2="44" y2="24"/><line x1="9" y1="9" x2="13" y2="13"/><line x1="35" y1="35" x2="39" y2="39"/><line x1="39" y1="9" x2="35" y2="13"/><line x1="13" y1="35" x2="9" y2="39"/></g></svg>
                </div>
                <span class="node-label" data-i18n="stepUV">UV &amp; Ozone</span>
              </div>
              <div class="journey-node">
                <div class="node-icon">
                  <svg viewBox="0 0 48 48"><rect x="17" y="6" width="14" height="8" rx="2" fill="none" stroke="#0B4A3F" stroke-width="2"/><path d="M17,14 L14,20 L14,42 Q14,44 16,44 L32,44 Q34,44 34,42 L34,20 L31,14Z" fill="none" stroke="#0B4A3F" stroke-width="2"/></svg>
                </div>
                <span class="node-label" data-i18n="stepBottling">Bottling</span>
              </div>
              <div class="journey-node journey-node-final">
                <div class="node-icon node-icon-final">
                  <svg viewBox="0 0 48 48"><circle cx="24" cy="16" r="7" fill="#C9A227"/><path d="M12,42 Q12,28 24,28 Q36,28 36,42" fill="none" stroke="#C9A227" stroke-width="2"/></svg>
                </div>
                <span class="node-label node-label-final" data-i18n="stepYou">You</span>
              </div>
            </div>
          </div>
        </div>

"""

content = content[:start_idx] + new_journey_html + content[end_idx:]
print("2. HTML replaced")

# ============================================================
# 3. JS — Add IntersectionObserver for journey nodes
# ============================================================
js_code = """
// Journey node reveal on scroll
var jt=document.querySelector('.journey-track');
if(jt){
  var jo=new IntersectionObserver(function(entries){
    entries.forEach(function(entry){
      if(entry.isIntersecting){
        document.querySelectorAll('.journey-node').forEach(function(n){n.classList.add('in-view')});
        jo.disconnect();
      }
    });
  },{threshold:0.2});
  jo.observe(jt);
}
"""

js_anchor = "\n</script>\n</body>"
assert js_anchor in content, "JS anchor not found"
content = content.replace(js_anchor, js_code + "\n</script>\n</body>")
print("3. JS observer added")

# ============================================================
# 4. i18n — EN: replace old jXxx keys with new stepXxx keys + journeyTitle
# ============================================================
old_en_journey = "jWaterfall:'Waterfall',jSpring:'Spring',jSandFilt:'Sand Filtration',jCarbFilt:'Carbon Filtration',\n      jUVOzone:'UV & Ozone',jBottle:'Bottling',jYou:'You',"
new_en_journey = "journeyTitle:'The Journey of Every Drop',\n      stepWaterfall:'Waterfall',stepSpring:'Spring',stepSand:'Sand Filtration',stepCarbon:'Carbon Filtration',\n      stepRO:'Reverse Osmosis',stepUV:'UV & Ozone',stepBottling:'Bottling',stepYou:'You',"
assert old_en_journey in content, "EN journey i18n not found"
content = content.replace(old_en_journey, new_en_journey)
print("4. EN i18n replaced")

# ============================================================
# 5. i18n — HI
# ============================================================
old_hi_journey = (
    "jWaterfall:'\\u091d\\u0930\\u0928\\u093e',jSpring:'\\u091d\\u0930\\u0928\\u093e \\u0938\\u094d\\u0930\\u094b\\u0924',"
    "jSandFilt:'\\u0930\\u0947\\u0924 \\u092b\\u093f\\u0932\\u094d\\u091f\\u094d\\u0930\\u0947\\u0936\\u0928',"
    "jCarbFilt:'\\u0915\\u093e\\u0930\\u094d\\u092c\\u0928 \\u092b\\u093f\\u0932\\u094d\\u091f\\u094d\\u0930\\u0947\\u0936\\u0928',\n"
    "      jUVOzone:'UV \\u0914\\u0930 \\u0913\\u091c\\u093c\\u094b\\u0928',jBottle:'\\u092c\\u0949\\u091f\\u0932\\u093f\\u0902\\u0917',jYou:'\\u0906\\u092a',"
)
new_hi_journey = (
    "journeyTitle:'\\u0939\\u0930 \\u092c\\u0942\\u0901\\u0926 \\u0915\\u0940 \\u092f\\u093e\\u0924\\u094d\\u0930\\u093e',\n"
    "      stepWaterfall:'\\u091d\\u0930\\u0928\\u093e',stepSpring:'\\u0938\\u094d\\u0930\\u094b\\u0924',"
    "stepSand:'\\u0930\\u0947\\u0924 \\u0928\\u093f\\u0938\\u094d\\u092a\\u0902\\u0926\\u0928',"
    "stepCarbon:'\\u0915\\u093e\\u0930\\u094d\\u092c\\u0928 \\u0928\\u093f\\u0938\\u094d\\u092a\\u0902\\u0926\\u0928',\n"
    "      stepRO:'\\u0930\\u093f\\u0935\\u0930\\u094d\\u0938 \\u0911\\u0938\\u094d\\u092e\\u094b\\u0938\\u093f\\u0938',"
    "stepUV:'\\u092f\\u0942\\u0935\\u0940 \\u0914\\u0930 \\u0913\\u091c\\u093c\\u094b\\u0928',"
    "stepBottling:'\\u092c\\u0949\\u091f\\u0932\\u093f\\u0902\\u0917',stepYou:'\\u0906\\u092a',"
)
assert old_hi_journey in content, "HI journey i18n not found"
content = content.replace(old_hi_journey, new_hi_journey)
print("5. HI i18n replaced")

# ============================================================
# 6. i18n — MR
# ============================================================
old_mr_journey = (
    "jWaterfall:'\\u0927\\u092c\\u0927\\u092c\\u093e',jSpring:'\\u091d\\u0930\\u093e',"
    "jSandFilt:'\\u0935\\u093e\\u0933\\u0942 \\u0917\\u093e\\u0933\\u0923\\u0940',"
    "jCarbFilt:'\\u0915\\u093e\\u0930\\u094d\\u092c\\u0928 \\u0917\\u093e\\u0933\\u0923\\u0940',\n"
    "      jUVOzone:'UV \\u0906\\u0923\\u093f \\u0913\\u091d\\u094b\\u0928',jBottle:'\\u092c\\u0949\\u091f\\u0932\\u093f\\u0902\\u0917',jYou:'\\u0924\\u0941\\u092e\\u094d\\u0939\\u0940',"
)
new_mr_journey = (
    "journeyTitle:'\\u092a\\u094d\\u0930\\u0924\\u094d\\u092f\\u0947\\u0915 \\u0925\\u0947\\u0902\\u092c\\u093e\\u091a\\u093e \\u092a\\u094d\\u0930\\u0935\\u093e\\u0938',\n"
    "      stepWaterfall:'\\u0927\\u092c\\u0927\\u092c\\u093e',stepSpring:'\\u091d\\u0930\\u093e',"
    "stepSand:'\\u0935\\u093e\\u0933\\u0942 \\u0917\\u093e\\u0933\\u0923\\u0940',"
    "stepCarbon:'\\u0915\\u093e\\u0930\\u094d\\u092c\\u0928 \\u0917\\u093e\\u0933\\u0923\\u0940',\n"
    "      stepRO:'\\u0930\\u093f\\u0935\\u094d\\u0939\\u0930\\u094d\\u0938 \\u0911\\u0938\\u094d\\u092e\\u094b\\u0938\\u093f\\u0938',"
    "stepUV:'\\u092f\\u0942\\u0935\\u094d\\u0939\\u0940 \\u0906\\u0923\\u093f \\u0913\\u091d\\u094b\\u0928',"
    "stepBottling:'\\u092c\\u093e\\u091f\\u0932\\u0940\\u092c\\u0902\\u0926',stepYou:'\\u0924\\u0941\\u092e\\u094d\\u0939\\u0940',"
)
assert old_mr_journey in content, "MR journey i18n not found"
content = content.replace(old_mr_journey, new_mr_journey)
print("6. MR i18n replaced")

# ============================================================
# WRITE
# ============================================================
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nAll done!")
