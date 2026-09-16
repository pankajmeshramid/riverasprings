"""
Step 3: Replace factory images with cropped+base64 versions
Step 4: iOS/mobile compatibility fixes
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('factory_new_1_b64.txt', 'r') as f:
    fac1_b64 = f.read().strip()
with open('factory_new_2_b64.txt', 'r') as f:
    fac2_b64 = f.read().strip()

# === STEP 3: Replace factory images ===
html = html.replace(
    '<img src="factory-0015.jpg" alt="Rivera Springs bottling facility exterior" loading="lazy">',
    '<img src="data:image/jpeg;base64,' + fac1_b64 + '" alt="Loading and dispatch operations at Amgaon Rd, Adashi, Tanda" loading="lazy" width="720" height="367">'
)
html = html.replace(
    '<img src="factory-0016.jpg" alt="Rivera Springs automated bottling line" loading="lazy">',
    '<img src="data:image/jpeg;base64,' + fac2_b64 + '" alt="Warehouse operations with staff in safety gear at Tanda facility" loading="lazy" width="720" height="367">'
)

# === STEP 4: iOS/mobile compatibility ===

# 4a: Add 100vh fallback before 100dvh for hero
# Current: height:100dvh; — need fallback
html = html.replace(
    '.hero{\n  position:relative;width:100%;\n  height:100dvh;',
    '.hero{\n  position:relative;width:100%;\n  height:100vh;height:100dvh;'
)

# 4b: Ensure product-scroll has -webkit-overflow-scrolling (already present, verify)
# Already has it at line 448

# 4c: Factory grid images — add aspect-ratio to prevent layout shift
html = html.replace(
    '.factory-grid img{\n  width:100%;height:100%;object-fit:cover;',
    '.factory-grid img{\n  width:100%;height:auto;aspect-ratio:720/367;object-fit:cover;'
)

# 4d: Source image — ensure aspect-ratio is set
# Already has aspect-ratio:3/4 on .source-img

# 4e: Ensure nav mobile drawer has 100vh fallback (already has it)
# line 131: height:100dvh;height:100vh — already correct order? Let's fix order
html = html.replace(
    'height:100dvh;height:100vh;background:var(--dark);',
    'height:100vh;height:100dvh;background:var(--dark);'
)

# 4f: Contact form - ensure no action URL pointing to third party
# Check if form has action attribute
if 'action=' in html[html.index('id="contactForm"'):html.index('id="contactForm"')+200]:
    print("WARNING: contactForm has action attribute")
else:
    print("OK: contactForm has no action attribute (submit handled by JS)")

# 4g: Verify no external scripts except Google Fonts
import re as re2
scripts = re2.findall(r'<script[^>]*src=["\']([^"\']+)', html)
for s in scripts:
    print(f"External script: {s}")
if not scripts:
    print("OK: No external script tags found")

links = re2.findall(r'<link[^>]*href=["\']([^"\']+)', html)
for l in links:
    if 'fonts.googleapis.com' not in l and 'fonts.gstatic.com' not in l:
        print(f"WARNING: Non-font external link: {l}")
    else:
        print(f"OK: Font link: {l}")

# 4h: Check for eval()
if 'eval(' in html:
    print("WARNING: eval() found in file!")
else:
    print("OK: No eval() found")

# 4i: Check inline event handlers for undefined functions
handlers = re2.findall(r'on\w+="[^"]*"', html)
for h in handlers:
    print(f"Inline handler: {h}")
if not handlers:
    print("OK: No inline event handlers")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nDone! Factory images replaced + iOS fixes applied.")
print(f"File size: {len(html)} chars")
