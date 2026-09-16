with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

count = 0

# ============================================================
# ENGLISH — HTML (actual text in the document)
# ============================================================

# 1. Source section h2
content = content.replace(
    "Pure water from Satpura&#8217;s pristine waterfalls, not a municipal borewell",
    "Pure water from the dense forests of Pangdi and Vidarbha&#8217;s pristine waterfalls, not a municipal borewell"
)
count += 1

# 2. Source section p1
content = content.replace(
    "near the <strong>Satpura foothills</strong>",
    "in the <strong>dense forests of Pangdi and Vidarbha</strong>"
)
count += 1

# 3. Stat region value
content = content.replace(
    '<dd data-i18n="statRegionV">Satpura Hills</dd>',
    '<dd data-i18n="statRegionV">Pangdi &amp; Vidarbha</dd>'
)
count += 1

# 4. Sparkling water description (HTML)
content = content.replace(
    "The same pristine Satpura source, now with effervescence",
    "The same pristine Pangdi-Vidarbha source, now with effervescence"
)
count += 1

# 5. Quality sourcing paragraph (HTML)
content = content.replace(
    "Natural springs near the Satpura foothills. Water surfaces through ancient rock formations",
    "Natural springs in the dense forests of Pangdi and Vidarbha. Water surfaces through ancient rock formations"
)
count += 1

# ============================================================
# ENGLISH — i18n strings
# ============================================================

# srcH2
content = content.replace(
    "srcH2:'Pure water from Satpura\\u2019s pristine waterfalls, not a municipal borewell'",
    "srcH2:'Pure water from the dense forests of Pangdi and Vidarbha\\u2019s pristine waterfalls, not a municipal borewell'"
)
count += 1

# srcP1
content = content.replace(
    "near the <strong>Satpura foothills</strong> \\u2014",
    "in the <strong>dense forests of Pangdi and Vidarbha</strong> \\u2014"
)
count += 1

# statRegionV
content = content.replace(
    "statRegionV:'Satpura Hills'",
    "statRegionV:'Pangdi & Vidarbha'"
)
count += 1

# sparklingDesc
content = content.replace(
    "The same pristine Satpura source, now with effervescence \\u2014",
    "The same pristine Pangdi-Vidarbha source, now with effervescence \\u2014"
)
count += 1

# qualSrcP
content = content.replace(
    "qualSrcP:'Natural springs near the Satpura foothills. Water surfaces through ancient rock formations",
    "qualSrcP:'Natural springs in the dense forests of Pangdi and Vidarbha. Water surfaces through ancient rock formations"
)
count += 1

print(f"EN: {count} replacements")

# ============================================================
# HINDI — i18n (escaped unicode)
# Satpura in Hindi = \u0938\u0924\u092a\u0941\u0921\u093c\u093e (सतपुड़ा)
# ============================================================

# HI srcH2: सतपुड़ा के शुद्ध झरनों से → पंगड़ी और विदर्भ के घने जंगलों के शुद्ध झरनों से
content = content.replace(
    "srcH2:'\\u0938\\u0924\\u092a\\u0941\\u0921\\u093c\\u093e \\u0915\\u0947 \\u0936\\u0941\\u0926\\u094d\\u0927 \\u091d\\u0930\\u0928\\u094b\\u0902 \\u0938\\u0947 \\u0938\\u094d\\u0935\\u091a\\u094d\\u091b \\u092a\\u093e\\u0928\\u0940",
    "srcH2:'\\u092a\\u0902\\u0917\\u0921\\u093c\\u0940 \\u0914\\u0930 \\u0935\\u093f\\u0926\\u0930\\u094d\\u092d \\u0915\\u0947 \\u0918\\u0928\\u0947 \\u091c\\u0902\\u0917\\u0932\\u094b\\u0902 \\u0915\\u0947 \\u0936\\u0941\\u0926\\u094d\\u0927 \\u091d\\u0930\\u0928\\u094b\\u0902 \\u0938\\u0947 \\u0938\\u094d\\u0935\\u091a\\u094d\\u091b \\u092a\\u093e\\u0928\\u0940"
)

# HI srcP1: <strong>सतपुड़ा की तलहटी</strong> → <strong>पंगड़ी और विदर्भ के घने जंगलों</strong>
content = content.replace(
    "<strong>\\u0938\\u0924\\u092a\\u0941\\u0921\\u093c\\u093e \\u0915\\u0940 \\u0924\\u0932\\u0939\\u091f\\u0940</strong>",
    "<strong>\\u092a\\u0902\\u0917\\u0921\\u093c\\u0940 \\u0914\\u0930 \\u0935\\u093f\\u0926\\u0930\\u094d\\u092d \\u0915\\u0947 \\u0918\\u0928\\u0947 \\u091c\\u0902\\u0917\\u0932</strong>"
)

# HI statRegionV: सतपुड़ा पहाड़ियाँ → पंगड़ी और विदर्भ
content = content.replace(
    "statRegionV:'\\u0938\\u0924\\u092a\\u0941\\u0921\\u093c\\u093e \\u092a\\u0939\\u093e\\u0921\\u093c\\u093f\\u092f\\u093e\\u0901'",
    "statRegionV:'\\u092a\\u0902\\u0917\\u0921\\u093c\\u0940 \\u0914\\u0930 \\u0935\\u093f\\u0926\\u0930\\u094d\\u092d'"
)

# HI qualSrcP: सतपुड़ा तलहटी के पास → पंगड़ी और विदर्भ के घने जंगलों में
content = content.replace(
    "qualSrcP:'\\u0938\\u0924\\u092a\\u0941\\u0921\\u093c\\u093e \\u0924\\u0932\\u0939\\u091f\\u0940 \\u0915\\u0947 \\u092a\\u093e\\u0938 \\u092a\\u094d\\u0930\\u093e\\u0915\\u0943\\u0924\\u093f\\u0915 \\u091d\\u0930\\u0928\\u0947",
    "qualSrcP:'\\u092a\\u0902\\u0917\\u0921\\u093c\\u0940 \\u0914\\u0930 \\u0935\\u093f\\u0926\\u0930\\u094d\\u092d \\u0915\\u0947 \\u0918\\u0928\\u0947 \\u091c\\u0902\\u0917\\u0932\\u094b\\u0902 \\u092e\\u0947\\u0902 \\u092a\\u094d\\u0930\\u093e\\u0915\\u0943\\u0924\\u093f\\u0915 \\u091d\\u0930\\u0928\\u0947"
)

# HI sparklingDesc: सतपुड़ा → पंगड़ी-विदर्भ
# Find the HI sparkling line - it has सतपुड़ा in it
content = content.replace(
    "\\u0938\\u0924\\u092a\\u0941\\u0921\\u093c\\u093e \\u0938\\u094d\\u0930\\u094b\\u0924",
    "\\u092a\\u0902\\u0917\\u0921\\u093c\\u0940-\\u0935\\u093f\\u0926\\u0930\\u094d\\u092d \\u0938\\u094d\\u0930\\u094b\\u0924"
)

print("HI: replacements done")

# ============================================================
# MARATHI — i18n (escaped unicode)
# Satpura in Marathi = \u0938\u0924\u092a\u0941\u0921\u094d\u092f\u093e (सतपुड्या)
# ============================================================

# MR srcH2: सतपुड्याच्या → पांगडी आणि विदर्भाच्या घनदाट जंगलांतील
content = content.replace(
    "srcH2:'\\u0938\\u0924\\u092a\\u0941\\u0921\\u094d\\u092f\\u093e\\u091a\\u094d\\u092f\\u093e \\u0928\\u093f\\u0930\\u094d\\u092e\\u0933 \\u0927\\u092c\\u0927\\u092c\\u094d\\u092f\\u093e\\u0902\\u091a\\u0947 \\u0936\\u0941\\u0926\\u094d\\u0927 \\u092a\\u093e\\u0923\\u0940",
    "srcH2:'\\u092a\\u093e\\u0902\\u0917\\u0921\\u0940 \\u0906\\u0923\\u093f \\u0935\\u093f\\u0926\\u0930\\u094d\\u092d\\u093e\\u091a\\u094d\\u092f\\u093e \\u0918\\u0928\\u0926\\u093e\\u091f \\u091c\\u0902\\u0917\\u0932\\u093e\\u0902\\u0924\\u0940\\u0932 \\u0928\\u093f\\u0930\\u094d\\u092e\\u0933 \\u0927\\u092c\\u0927\\u092c\\u094d\\u092f\\u093e\\u0902\\u091a\\u0947 \\u0936\\u0941\\u0926\\u094d\\u0927 \\u092a\\u093e\\u0923\\u0940"
)

# MR srcP1: <strong>सतपुड्याच्या पायथ्याजवळ</strong> → <strong>पांगडी आणि विदर्भाच्या घनदाट जंगलांत</strong>
content = content.replace(
    "<strong>\\u0938\\u0924\\u092a\\u0941\\u0921\\u094d\\u092f\\u093e\\u091a\\u094d\\u092f\\u093e \\u092a\\u093e\\u092f\\u0925\\u094d\\u092f\\u093e\\u091c\\u0935\\u0933</strong>",
    "<strong>\\u092a\\u093e\\u0902\\u0917\\u0921\\u0940 \\u0906\\u0923\\u093f \\u0935\\u093f\\u0926\\u0930\\u094d\\u092d\\u093e\\u091a\\u094d\\u092f\\u093e \\u0918\\u0928\\u0926\\u093e\\u091f \\u091c\\u0902\\u0917\\u0932\\u093e\\u0902\\u0924</strong>"
)

# MR statRegionV: सतपुड्याचे डोंगर → पांगडी आणि विदर्भ
content = content.replace(
    "statRegionV:'\\u0938\\u0924\\u092a\\u0941\\u0921\\u094d\\u092f\\u093e\\u091a\\u0947 \\u0921\\u094b\\u0902\\u0917\\u0930'",
    "statRegionV:'\\u092a\\u093e\\u0902\\u0917\\u0921\\u0940 \\u0906\\u0923\\u093f \\u0935\\u093f\\u0926\\u0930\\u094d\\u092d'"
)

# MR qualSrcP: सतपुड्याच्या पायथ्याजवळचे → पांगडी आणि विदर्भाच्या घनदाट जंगलांतील
content = content.replace(
    "qualSrcP:'\\u0938\\u0924\\u092a\\u0941\\u0921\\u094d\\u092f\\u093e\\u091a\\u094d\\u092f\\u093e \\u092a\\u093e\\u092f\\u0925\\u094d\\u092f\\u093e\\u091c\\u0935\\u0933\\u091a\\u0947 \\u0928\\u0948\\u0938\\u0930\\u094d\\u0917\\u093f\\u0915 \\u091d\\u0930\\u0947",
    "qualSrcP:'\\u092a\\u093e\\u0902\\u0917\\u0921\\u0940 \\u0906\\u0923\\u093f \\u0935\\u093f\\u0926\\u0930\\u094d\\u092d\\u093e\\u091a\\u094d\\u092f\\u093e \\u0918\\u0928\\u0926\\u093e\\u091f \\u091c\\u0902\\u0917\\u0932\\u093e\\u0902\\u0924\\u0940\\u0932 \\u0928\\u0948\\u0938\\u0930\\u094d\\u0917\\u093f\\u0915 \\u091d\\u0930\\u0947"
)

# MR sparklingDesc: सतपुड्या → पांगडी-विदर्भ
content = content.replace(
    "\\u0938\\u0924\\u092a\\u0941\\u0921\\u094d\\u092f\\u093e\\u091a\\u094d\\u092f\\u093e \\u0938\\u094d\\u0930\\u094b\\u0924",
    "\\u092a\\u093e\\u0902\\u0917\\u0921\\u0940-\\u0935\\u093f\\u0926\\u0930\\u094d\\u092d \\u0938\\u094d\\u0930\\u094b\\u0924"
)

print("MR: replacements done")

# ============================================================
# WRITE
# ============================================================
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# ============================================================
# VERIFY — count remaining Satpura references
# ============================================================
remaining_en = content.lower().count('satpura')
# Check for Hindi सतपुड़ा escaped
remaining_hi = content.count('\\u0938\\u0924\\u092a\\u0941\\u0921\\u093c\\u093e')
# Check for Marathi सतपुड्या escaped
remaining_mr = content.count('\\u0938\\u0924\\u092a\\u0941\\u0921\\u094d\\u092f\\u093e')

print(f"\nRemaining 'Satpura' (EN): {remaining_en}")
print(f"Remaining Hindi Satpura: {remaining_hi}")
print(f"Remaining Marathi Satpura: {remaining_mr}")

if remaining_en == 0 and remaining_hi == 0 and remaining_mr == 0:
    print("\nALL CLEAR - zero Satpura references remain!")
else:
    print("\nWARNING - some references remain, check manually")
