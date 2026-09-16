#!/usr/bin/env python3
"""
Round 3 fixes for Rivera Springs index.html
FIX 1: Replace hero bg GIF with new JPEG + hue-rotate + color wash + pan animation
FIX 2: Fix i18n keys and add Hindi/Marathi translations for Upcoming Products
FIX 3: Replace SVG bottle silhouettes with frosted-glass cards
"""
import re, sys

HTML_FILE = r'C:\Users\PANKAJ\riverasprings\index.html'
HERO_B64_FILE = r'C:\Users\PANKAJ\riverasprings\_hero_b64.txt'

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def fix1_hero_bg(html):
    """Replace GIF hero bg with JPEG, add hue-rotate filter, color wash, pan animation"""
    print("=== FIX 1: Replace hero background ===")

    # Read base64 data
    hero_b64 = read_file(HERO_B64_FILE).strip()
    print(f"  Hero image b64 length: {len(hero_b64)}")

    # 1. Replace the hero-bg CSS to add filter and animation
    old_hero_bg_css = """.hero-bg{
  position:absolute;inset:0;width:100%;height:100%;
  object-fit:cover;object-position:center top;
  z-index:0;
}"""
    new_hero_bg_css = """.hero-bg{
  position:absolute;inset:0;width:100%;height:100%;
  object-fit:cover;object-position:center top;
  z-index:0;
  filter:hue-rotate(140deg) saturate(0.7) brightness(0.85);
  animation:heroPan 30s ease-in-out infinite alternate;
}
@keyframes heroPan{0%{transform:scale(1.08) translate(0,0)}100%{transform:scale(1.08) translate(-2%,-1.5%)}}"""

    count = html.count(old_hero_bg_css)
    print(f"  hero-bg CSS matches: {count}")
    if count == 1:
        html = html.replace(old_hero_bg_css, new_hero_bg_css)
        print("  ✓ hero-bg CSS updated with filter + animation")
    else:
        print(f"  ✗ Expected 1 match, found {count}")
        return html

    # 2. Replace the hero background-color with transparent (since we have image)
    # Keep background-color as fallback but change to dark teal
    old_hero_main = "overflow:hidden;background-color:#1a3a20;"
    new_hero_main = "overflow:hidden;background-color:#040e0c;"
    count = html.count(old_hero_main)
    print(f"  hero bg-color matches: {count}")
    if count == 1:
        html = html.replace(old_hero_main, new_hero_main)
        print("  ✓ hero bg-color updated")

    # 3. Replace the img src from GIF to JPEG
    old_src_pattern = r'<img class="hero-bg" src="data:image/gif;base64,[A-Za-z0-9+/=]+"'
    new_src = f'<img class="hero-bg" src="data:image/jpeg;base64,{hero_b64}"'
    match = re.search(old_src_pattern, html)
    if match:
        html = html[:match.start()] + new_src + html[match.end():]
        print("  ✓ hero-bg img src replaced (GIF → JPEG)")
    else:
        print("  ✗ Could not find hero-bg img tag with GIF src")
        return html

    # 4. Add color wash div right after the hero-bg img tag
    # Find the closing > of the hero-bg img and the hero-overlay div
    old_overlay = '<div class="hero-overlay">'
    new_overlay = '<div class="hero-color-wash"></div>\n  <div class="hero-overlay">'
    count = html.count(old_overlay)
    print(f"  hero-overlay matches: {count}")
    if count == 1:
        html = html.replace(old_overlay, new_overlay)
        print("  ✓ hero-color-wash div added")

    # 5. Add CSS for hero-color-wash (before .hero-overlay CSS)
    old_overlay_css = ".hero-overlay{"
    new_overlay_css = """.hero-color-wash{
  position:absolute;inset:0;z-index:0;pointer-events:none;
  background:rgba(11,74,63,0.45);
  mix-blend-mode:color;
}
.hero-overlay{"""
    count = html.count(old_overlay_css)
    print(f"  .hero-overlay{{ CSS matches: {count}")
    if count >= 1:
        html = html.replace(old_overlay_css, new_overlay_css, 1)
        print("  ✓ hero-color-wash CSS added")

    print("  FIX 1 COMPLETE\n")
    return html


def fix2_i18n(html):
    """Fix i18n keys and add Hindi/Marathi translations for Upcoming Products"""
    print("=== FIX 2: Fix i18n translations ===")

    # 1. Rename data-i18n attributes in HTML
    renames = {
        'data-i18n="upEyebrow"': 'data-i18n="upcomingEyebrow"',
        'data-i18n="upH2"': 'data-i18n="upcomingTitle"',
        'data-i18n="upDesc"': 'data-i18n="upcomingSubtitle"',
        'data-i18n="upSparkH"': 'data-i18n="sparklingTitle"',
        'data-i18n="upSparkP"': 'data-i18n="sparklingDesc"',
        'data-i18n="upAlkH"': 'data-i18n="alkalineTitle"',
        'data-i18n="upAlkP"': 'data-i18n="alkalineDesc"',
    }

    for old, new in renames.items():
        count = html.count(old)
        html = html.replace(old, new)
        print(f"  Renamed {old} → {new} ({count} occurrences)")

    # Handle upBadge specially - there are 2 instances, rename to sparklingBadge and alkalineBadge
    # First one is sparkling, second is alkaline
    # The sparkling one: <span class="upcoming-badge" data-i18n="upBadge">
    old_spark_badge = '<span class="upcoming-badge" data-i18n="upBadge">'
    new_spark_badge = '<span class="upcoming-badge" data-i18n="sparklingBadge">'
    count = html.count(old_spark_badge)
    print(f"  sparkling badge matches: {count}")
    if count >= 1:
        html = html.replace(old_spark_badge, new_spark_badge, 1)
        print("  ✓ sparklingBadge renamed")

    old_alk_badge = '<span class="upcoming-badge alkaline-badge" data-i18n="upBadge">'
    new_alk_badge = '<span class="upcoming-badge alkaline-badge" data-i18n="alkalineBadge">'
    count = html.count(old_alk_badge)
    print(f"  alkaline badge matches: {count}")
    if count >= 1:
        html = html.replace(old_alk_badge, new_alk_badge, 1)
        print("  ✓ alkalineBadge renamed")

    # 2. Add translation keys to EN block
    # Insert after footerText line in EN block
    en_translations = """      upcomingEyebrow:"What\\u2019s Next",upcomingTitle:'Upcoming Products',upcomingSubtitle:'Expanding our range with premium hydration \\u2014 crafted for those who demand more from their water.',
      sparklingBadge:'Coming Soon',sparklingTitle:'Premium Sparkling Water',sparklingDesc:'Naturally carbonated. Fine bubbles. The same pristine Satpura source, now with effervescence \\u2014 for those who want their purity with a sparkle.',
      alkalineBadge:'Coming Soon',alkalineTitle:'Alkaline Mineral Water',alkalineDesc:'Enhanced with added minerals. pH 9.5+. Designed for active lifestyles and health-conscious consumers \\u2014 alkaline hydration, sourced from nature, not a lab.',"""

    # Find EN footerText line and add after it
    en_footer = "footerText:'\\u00a9 2024 Rivera Springs. All rights reserved. | Made with pride in Amgaon, Maharashtra'"
    count = html.count(en_footer)
    print(f"  EN footerText matches: {count}")
    if count == 1:
        html = html.replace(en_footer, en_footer + ",\n" + en_translations)
        print("  ✓ EN translations added")
    else:
        # Try alternate approach - find the closing of EN block
        print("  Trying alternate EN insertion...")
        # Use regex to find footerText in EN block
        en_footer_re = r"(footerText:'[^']*Made with pride in Amgaon, Maharashtra')"
        m = re.search(en_footer_re, html)
        if m:
            html = html[:m.end()] + ",\n" + en_translations + "\n" + html[m.end():]
            print("  ✓ EN translations added (via regex)")

    # 3. Add Hindi translations
    hi_translations = """      upcomingEyebrow:'\\u0906\\u0917\\u0947 \\u0915\\u094d\\u092f\\u093e \\u0939\\u0948',upcomingTitle:'\\u0906\\u0928\\u0947 \\u0935\\u093e\\u0932\\u0947 \\u0909\\u0924\\u094d\\u092a\\u093e\\u0926',upcomingSubtitle:'\\u092a\\u094d\\u0930\\u0940\\u092e\\u093f\\u092f\\u092e \\u0939\\u093e\\u0907\\u0921\\u094d\\u0930\\u0947\\u0936\\u0928 \\u0915\\u0947 \\u0938\\u093e\\u0925 \\u0939\\u092e\\u093e\\u0930\\u0940 \\u0930\\u0947\\u0902\\u091c \\u0915\\u093e \\u0935\\u093f\\u0938\\u094d\\u0924\\u093e\\u0930 \\u2014 \\u0909\\u0928\\u0915\\u0947 \\u0932\\u093f\\u090f \\u091c\\u094b \\u0905\\u092a\\u0928\\u0947 \\u092a\\u093e\\u0928\\u0940 \\u0938\\u0947 \\u0905\\u0927\\u093f\\u0915 \\u0915\\u0940 \\u092e\\u093e\\u0901\\u0917 \\u0915\\u0930\\u0924\\u0947 \\u0939\\u0948\\u0902\\u0964',
      sparklingBadge:'\\u091c\\u0932\\u094d\\u0926 \\u0906 \\u0930\\u0939\\u093e \\u0939\\u0948',sparklingTitle:'\\u092a\\u094d\\u0930\\u0940\\u092e\\u093f\\u092f\\u092e \\u0938\\u094d\\u092a\\u093e\\u0930\\u094d\\u0915\\u0932\\u093f\\u0902\\u0917 \\u0935\\u0949\\u091f\\u0930',sparklingDesc:'\\u092a\\u094d\\u0930\\u093e\\u0915\\u0943\\u0924\\u093f\\u0915 \\u0930\\u0942\\u092a \\u0938\\u0947 \\u0915\\u093e\\u0930\\u094d\\u092c\\u094b\\u0928\\u0947\\u091f\\u0947\\u0921\\u0964 \\u092c\\u093e\\u0930\\u0940\\u0915 \\u092c\\u0941\\u0932\\u092c\\u0941\\u0932\\u0947\\u0964 \\u0935\\u0939\\u0940 \\u0936\\u0941\\u0926\\u094d\\u0927 \\u0938\\u0924\\u092a\\u0941\\u0921\\u093c\\u093e \\u0938\\u094d\\u0930\\u094b\\u0924, \\u0905\\u092c \\u091a\\u092e\\u0915 \\u0915\\u0947 \\u0938\\u093e\\u0925 \\u2014 \\u091c\\u094b \\u0905\\u092a\\u0928\\u0940 \\u0936\\u0941\\u0926\\u094d\\u0927\\u0924\\u093e \\u092e\\u0947\\u0902 \\u091a\\u092e\\u0915 \\u091a\\u093e\\u0939\\u0924\\u0947 \\u0939\\u0948\\u0902\\u0964',
      alkalineBadge:'\\u091c\\u0932\\u094d\\u0926 \\u0906 \\u0930\\u0939\\u093e \\u0939\\u0948',alkalineTitle:'\\u090f\\u0932\\u094d\\u0915\\u0932\\u093e\\u0907\\u0928 \\u092e\\u093f\\u0928\\u0930\\u0932 \\u0935\\u0949\\u091f\\u0930',alkalineDesc:'\\u0905\\u0924\\u093f\\u0930\\u093f\\u0915\\u094d\\u0924 \\u0916\\u0928\\u093f\\u091c\\u094b\\u0902 \\u0938\\u0947 \\u092f\\u0941\\u0915\\u094d\\u0924\\u0964 pH 9.5+\\u0964 \\u0938\\u0915\\u094d\\u0930\\u093f\\u092f \\u091c\\u0940\\u0935\\u0928\\u0936\\u0948\\u0932\\u0940 \\u0914\\u0930 \\u0938\\u094d\\u0935\\u093e\\u0938\\u094d\\u0925\\u094d\\u092f \\u0938\\u091c\\u0917 \\u0909\\u092a\\u092d\\u094b\\u0915\\u094d\\u0924\\u093e\\u0913\\u0902 \\u0915\\u0947 \\u0932\\u093f\\u090f \\u2014 \\u092a\\u094d\\u0930\\u0915\\u0943\\u0924\\u093f \\u0938\\u0947 \\u0915\\u094d\\u0937\\u093e\\u0930\\u0940\\u092f \\u0939\\u093e\\u0907\\u0921\\u094d\\u0930\\u0947\\u0936\\u0928, \\u0932\\u0948\\u092c \\u0938\\u0947 \\u0928\\u0939\\u0940\\u0902\\u0964',"""

    # Find HI footerText
    hi_footer_pattern = r"(footerText:'.{10,80}\\u092e\\u0939\\u093e\\u0930\\u093e\\u0937\\u094d\\u091f\\u094d\\u0930 \\u092e\\u0947\\u0902 \\u0917\\u0930\\u094d\\u0935 \\u0938\\u0947 \\u092c\\u0928\\u093e\\u092f\\u093e')"
    m = re.search(hi_footer_pattern, html)
    if m:
        html = html[:m.end()] + ",\n" + hi_translations + "\n" + html[m.end():]
        print("  ✓ HI translations added")
    else:
        # Simpler approach - find the "    }," between hi and mr blocks
        # The HI block ends with footerText:'...' then newline then "    },"
        print("  Trying alternate HI insertion...")
        # Find the Hindi closing bracket - it should be the second "    }," after translations var
        hi_close = "\u0917\u0930\u094d\u0935 \u0938\u0947 \u092c\u0928\u093e\u092f\u093e'"
        idx = html.find(hi_close)
        if idx != -1:
            # Insert after the closing quote
            insert_pos = idx + len(hi_close)
            html = html[:insert_pos] + ",\n" + hi_translations + "\n" + html[insert_pos:]
            print("  ✓ HI translations added (alternate)")
        else:
            print("  ✗ Could not find HI insertion point")

    # 4. Add Marathi translations
    mr_translations = """      upcomingEyebrow:'\\u092a\\u0941\\u0922\\u0947 \\u0915\\u093e\\u092f',upcomingTitle:'\\u0906\\u0917\\u093e\\u092e\\u0940 \\u0909\\u0924\\u094d\\u092a\\u093e\\u0926\\u0928\\u0947',upcomingSubtitle:'\\u092a\\u094d\\u0930\\u0940\\u092e\\u093f\\u092f\\u092e \\u0939\\u093e\\u092f\\u0921\\u094d\\u0930\\u0947\\u0936\\u0928\\u0938\\u0939 \\u0906\\u092e\\u091a\\u094d\\u092f\\u093e \\u0930\\u0947\\u0902\\u091c\\u091a\\u093e \\u0935\\u093f\\u0938\\u094d\\u0924\\u093e\\u0930 \\u2014 \\u091c\\u094d\\u092f\\u093e\\u0902\\u0928\\u093e \\u0924\\u094d\\u092f\\u093e\\u0902\\u091a\\u094d\\u092f\\u093e \\u092a\\u093e\\u0923\\u094d\\u092f\\u093e\\u0915\\u0921\\u0942\\u0928 \\u0905\\u0927\\u093f\\u0915\\u093e\\u091a\\u0940 \\u0905\\u092a\\u0947\\u0915\\u094d\\u0937\\u093e \\u0906\\u0939\\u0947.',
      sparklingBadge:'\\u0932\\u0935\\u0915\\u0930\\u091a \\u092f\\u0947\\u0924 \\u0906\\u0939\\u0947',sparklingTitle:'\\u092a\\u094d\\u0930\\u0940\\u092e\\u093f\\u092f\\u092e \\u0938\\u094d\\u092a\\u093e\\u0930\\u094d\\u0915\\u0932\\u093f\\u0902\\u0917 \\u0935\\u0949\\u091f\\u0930',sparklingDesc:'\\u0928\\u0948\\u0938\\u0930\\u094d\\u0917\\u093f\\u0915\\u0930\\u093f\\u0924\\u094d\\u092f\\u093e \\u0915\\u093e\\u0930\\u094d\\u092c\\u094b\\u0928\\u0947\\u091f\\u0947\\u0921. \\u0938\\u0942\\u0915\\u094d\\u0937\\u094d\\u092e \\u092c\\u0941\\u0926\\u092c\\u0941\\u0926\\u0947. \\u0924\\u0947\\u091a \\u0936\\u0941\\u0926\\u094d\\u0927 \\u0938\\u0924\\u092a\\u0941\\u0921\\u094d\\u092f\\u093e\\u091a\\u0947 \\u092a\\u093e\\u0923\\u0940, \\u0906\\u0924\\u093e \\u091a\\u092e\\u0915\\u0926\\u093e\\u0930 \\u2014 \\u091c\\u094d\\u092f\\u093e\\u0902\\u0928\\u093e \\u0924\\u094d\\u092f\\u093e\\u0902\\u091a\\u094d\\u092f\\u093e \\u0936\\u0941\\u0926\\u094d\\u0927\\u0924\\u0947\\u0924 \\u091a\\u092e\\u0915 \\u0939\\u0935\\u0940 \\u0906\\u0939\\u0947.',
      alkalineBadge:'\\u0932\\u0935\\u0915\\u0930\\u091a \\u092f\\u0947\\u0924 \\u0906\\u0939\\u0947',alkalineTitle:'\\u0905\\u0932\\u094d\\u0915\\u0932\\u093e\\u0907\\u0928 \\u092e\\u093f\\u0928\\u0930\\u0932 \\u0935\\u0949\\u091f\\u0930',alkalineDesc:'\\u0905\\u0924\\u093f\\u0930\\u093f\\u0915\\u094d\\u0924 \\u0916\\u0928\\u093f\\u091c\\u093e\\u0902\\u0938\\u0939. pH 9.5+. \\u0938\\u0915\\u094d\\u0930\\u093f\\u092f \\u091c\\u0940\\u0935\\u0928\\u0936\\u0948\\u0932\\u0940 \\u0906\\u0923\\u093f \\u0906\\u0930\\u094b\\u0917\\u094d\\u092f\\u0938\\u091c\\u0917 \\u0917\\u094d\\u0930\\u093e\\u0939\\u0915\\u093e\\u0902\\u0938\\u093e\\u0920\\u0940 \\u2014 \\u0928\\u093f\\u0938\\u0930\\u094d\\u0917\\u093e\\u0924\\u0942\\u0928 \\u0915\\u094d\\u0937\\u093e\\u0930\\u0940\\u092f \\u0939\\u093e\\u092f\\u0921\\u094d\\u0930\\u0947\\u0936\\u0928, \\u0932\\u0945\\u092c\\u092e\\u0927\\u0942\\u0928 \\u0928\\u093e\\u0939\\u0940.',"""

    # Find MR footerText
    mr_footer = "\u0905\u092e\u0917\u093e\u0935, \u092e\u0939\u093e\u0930\u093e\u0937\u094d\u091f\u094d\u0930 \u092e\u0927\u094d\u092f\u0947 \u0905\u092d\u093f\u092e\u093e\u0928\u093e\u0928\u0947 \u092c\u0928\u0935\u0932\u0947'"
    idx = html.find(mr_footer)
    if idx != -1:
        insert_pos = idx + len(mr_footer)
        html = html[:insert_pos] + ",\n" + mr_translations + "\n" + html[insert_pos:]
        print("  ✓ MR translations added")
    else:
        print("  Trying alternate MR insertion...")
        # Find the Marathi closing - look for the unique text near MR footerText
        mr_footer2 = "\u0905\u092d\u093f\u092e\u093e\u0928\u093e\u0928\u0947 \u092c\u0928\u0935\u0932\u0947'"
        idx = html.find(mr_footer2)
        if idx != -1:
            insert_pos = idx + len(mr_footer2)
            html = html[:insert_pos] + ",\n" + mr_translations + "\n" + html[insert_pos:]
            print("  ✓ MR translations added (alternate)")
        else:
            print("  ✗ Could not find MR insertion point")

    print("  FIX 2 COMPLETE\n")
    return html


def fix3_upcoming_cards(html):
    """Replace SVG bottle silhouettes with frosted-glass cards"""
    print("=== FIX 3: Replace upcoming product cards ===")

    # 1. Replace CSS - remove old silhouette CSS, add new card CSS
    old_css = """.upcoming-visual{
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
.alkaline-badge{background:rgba(60,200,180,0.12);border-color:rgba(60,200,180,0.4);color:#3CC8B4}"""

    new_css = """.product-preview{
  position:relative;height:260px;margin-bottom:32px;
  display:flex;align-items:center;justify-content:center;
  border-radius:16px;overflow:hidden;
  background:rgba(255,255,255,0.04);
  backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
  border:1px solid rgba(255,255,255,0.08);
  transition:border-color .4s,box-shadow .4s;
}
.upcoming-card:hover .product-preview{border-color:rgba(201,162,39,0.25);box-shadow:0 8px 40px rgba(0,0,0,0.3)}
.sparkling-preview{background:linear-gradient(135deg,rgba(201,162,39,0.06) 0%,rgba(245,213,131,0.02) 100%)}
.alkaline-preview{background:linear-gradient(135deg,rgba(60,200,180,0.06) 0%,rgba(60,200,180,0.02) 100%)}
.preview-glow{
  position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
  width:180px;height:180px;border-radius:50%;filter:blur(50px);
  animation:previewPulse 4s ease-in-out infinite;
}
.sparkling-preview .preview-glow{background:radial-gradient(circle,rgba(245,213,131,0.2) 0%,transparent 70%)}
.alkaline-preview .preview-glow{background:radial-gradient(circle,rgba(60,200,180,0.2) 0%,transparent 70%)}
@keyframes previewPulse{0%,100%{opacity:.6;transform:translate(-50%,-50%) scale(1)}50%{opacity:1;transform:translate(-50%,-50%) scale(1.1)}}
.preview-icon{position:relative;z-index:2}
.preview-icon svg{width:100px;height:100px}
.preview-label{
  position:absolute;top:16px;right:16px;
  font-size:10px;letter-spacing:2px;text-transform:uppercase;
  padding:5px 14px;border-radius:20px;font-weight:600;font-family:var(--sans);
}
.sparkling-preview .preview-label{background:rgba(201,162,39,0.15);border:1px solid rgba(201,162,39,0.4);color:#C9A227}
.alkaline-preview .preview-label{background:rgba(60,200,180,0.12);border:1px solid rgba(60,200,180,0.4);color:#3CC8B4}
@keyframes bubbleRise{0%{transform:translateY(0);opacity:.6}100%{transform:translateY(-20px);opacity:0}}
@keyframes ringPulse{0%{r:8;opacity:.5;stroke-width:1.5}100%{r:30;opacity:0;stroke-width:0.3}}"""

    count = html.count(old_css)
    print(f"  Old silhouette CSS matches: {count}")
    if count == 1:
        html = html.replace(old_css, new_css)
        print("  ✓ CSS replaced")
    else:
        print(f"  ✗ Expected 1 match, found {count}")
        return html

    # 2. Replace HTML - sparkling card visual
    old_sparkling_html = """        <div class="upcoming-visual">
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
          <span class="upcoming-badge" data-i18n="sparklingBadge">Coming Soon</span>
        </div>"""

    new_sparkling_html = """        <div class="product-preview sparkling-preview">
          <div class="preview-glow"></div>
          <div class="preview-icon">
            <svg viewBox="0 0 100 100" fill="none">
              <circle cx="35" cy="55" r="4" fill="rgba(245,213,131,0.4)"><animate attributeName="cy" values="55;35;55" dur="3s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.6;0;0.6" dur="3s" repeatCount="indefinite"/></circle>
              <circle cx="55" cy="60" r="3" fill="rgba(245,213,131,0.3)"><animate attributeName="cy" values="60;38;60" dur="3.5s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.5;0;0.5" dur="3.5s" repeatCount="indefinite"/></circle>
              <circle cx="50" cy="45" r="5" fill="rgba(245,213,131,0.35)"><animate attributeName="cy" values="45;22;45" dur="2.8s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.6;0;0.6" dur="2.8s" repeatCount="indefinite"/></circle>
              <circle cx="65" cy="50" r="2.5" fill="rgba(245,213,131,0.25)"><animate attributeName="cy" values="50;30;50" dur="4s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.4;0;0.4" dur="4s" repeatCount="indefinite"/></circle>
              <circle cx="42" cy="65" r="3.5" fill="rgba(245,213,131,0.3)"><animate attributeName="cy" values="65;40;65" dur="3.2s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.5;0;0.5" dur="3.2s" repeatCount="indefinite"/></circle>
              <text x="50" y="85" text-anchor="middle" font-family="Bodoni Moda,serif" font-size="11" fill="rgba(245,213,131,0.5)" letter-spacing="3">SPARKLING</text>
            </svg>
          </div>
          <span class="preview-label" data-i18n="sparklingBadge">Coming Soon</span>
        </div>"""

    count = html.count(old_sparkling_html)
    print(f"  Sparkling HTML matches: {count}")
    if count == 1:
        html = html.replace(old_sparkling_html, new_sparkling_html)
        print("  ✓ Sparkling card HTML replaced")
    else:
        print(f"  ✗ Expected 1 match, found {count}")

    # 3. Replace HTML - alkaline card visual
    old_alkaline_html = """        <div class="upcoming-visual">
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
          <span class="upcoming-badge alkaline-badge" data-i18n="alkalineBadge">Coming Soon</span>
        </div>"""

    new_alkaline_html = """        <div class="product-preview alkaline-preview">
          <div class="preview-glow"></div>
          <div class="preview-icon">
            <svg viewBox="0 0 100 100" fill="none">
              <circle cx="50" cy="50" r="8" stroke="rgba(60,200,180,0.5)" stroke-width="1.5" fill="none"><animate attributeName="r" values="8;30;8" dur="3s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.5;0;0.5" dur="3s" repeatCount="indefinite"/></circle>
              <circle cx="50" cy="50" r="8" stroke="rgba(60,200,180,0.4)" stroke-width="1.2" fill="none"><animate attributeName="r" values="8;30;8" dur="3s" begin="0.8s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.4;0;0.4" dur="3s" begin="0.8s" repeatCount="indefinite"/></circle>
              <circle cx="50" cy="50" r="8" stroke="rgba(60,200,180,0.3)" stroke-width="1" fill="none"><animate attributeName="r" values="8;30;8" dur="3s" begin="1.6s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.3;0;0.3" dur="3s" begin="1.6s" repeatCount="indefinite"/></circle>
              <text x="50" y="48" text-anchor="middle" font-family="Bodoni Moda,serif" font-size="20" fill="rgba(60,200,180,0.6)" font-weight="700">pH</text>
              <text x="50" y="63" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" fill="rgba(60,200,180,0.45)">9.5+</text>
              <text x="50" y="88" text-anchor="middle" font-family="Bodoni Moda,serif" font-size="11" fill="rgba(60,200,180,0.5)" letter-spacing="3">ALKALINE</text>
            </svg>
          </div>
          <span class="preview-label" data-i18n="alkalineBadge">Coming Soon</span>
        </div>"""

    count = html.count(old_alkaline_html)
    print(f"  Alkaline HTML matches: {count}")
    if count == 1:
        html = html.replace(old_alkaline_html, new_alkaline_html)
        print("  ✓ Alkaline card HTML replaced")
    else:
        print(f"  ✗ Expected 1 match, found {count}")

    print("  FIX 3 COMPLETE\n")
    return html


# Main
print("Reading index.html...")
html = read_file(HTML_FILE)
original_len = len(html)
print(f"Original size: {original_len} chars\n")

html = fix1_hero_bg(html)
write_file(HTML_FILE, html)
print(f"Saved after FIX 1 ({len(html)} chars)\n")

# Re-read to be safe
html = read_file(HTML_FILE)
html = fix2_i18n(html)
write_file(HTML_FILE, html)
print(f"Saved after FIX 2 ({len(html)} chars)\n")

# Re-read to be safe
html = read_file(HTML_FILE)
html = fix3_upcoming_cards(html)
write_file(HTML_FILE, html)
print(f"Saved after FIX 3 ({len(html)} chars)\n")

print("=" * 50)
print("ALL 3 FIXES APPLIED SUCCESSFULLY")
print(f"Final size: {len(html)} chars")
