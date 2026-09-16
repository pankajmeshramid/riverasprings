import importlib.util, os

spec = importlib.util.spec_from_file_location('b64', '_b64_data.py')
b64 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b64)

with open('rivera-springs.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ─── NEW CSS ───
chunk3_css = r'''
/* ═══════════ FACTORY ═══════════ */
.factory{background:#fff;padding:var(--section-pad) 0}
.factory-header{text-align:center;margin-bottom:clamp(2.5rem,5vw,4rem)}
.factory-header .label{display:block;margin-bottom:.5rem}
.factory-header .gold-rule{margin:0 auto 1.75rem}
.factory-header h2{font-family:var(--serif);font-size:clamp(2rem,4vw,3rem);font-weight:700;color:var(--heading);line-height:1.1}

.factory-grid{display:grid;grid-template-columns:1fr 1fr;gap:1.25rem}
.factory-img{
  width:100%;aspect-ratio:16/9;object-fit:cover;
  box-shadow:0 8px 32px rgba(0,0,0,.08);
  transition:transform .4s ease,box-shadow .4s ease;
}
.factory-img:hover{transform:scale(1.015);box-shadow:0 16px 48px rgba(0,0,0,.12)}
.factory-cap{text-align:center;margin-top:clamp(2rem,4vw,3rem);max-width:720px;margin-left:auto;margin-right:auto}
.factory-cap p{color:#666;font-size:.93rem;line-height:1.8;margin-bottom:.8rem}
.factory-cap .stat-line{
  font-family:var(--serif);font-size:clamp(1.1rem,2vw,1.5rem);
  color:var(--heading);font-weight:700;letter-spacing:.02em;
}

@media(max-width:600px){.factory-grid{grid-template-columns:1fr}}

/* ═══════════ RETAILERS ═══════════ */
.retailers{background:var(--mist);padding:var(--section-pad) 0}
.retailers-grid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(3rem,6vw,5rem);align-items:center}
.retailers-text .label{display:block;margin-bottom:.5rem}
.retailers-text .gold-rule{margin-bottom:1.75rem}
.retailers-text h2{font-family:var(--serif);font-size:clamp(2rem,4vw,2.8rem);font-weight:700;color:var(--heading);line-height:1.1;margin-bottom:1.5rem}
.retailers-text p{color:var(--text);font-size:.93rem;line-height:1.82;margin-bottom:1.2rem}
.retailers-text ul{margin-bottom:2rem}
.retailers-text li{
  padding:.5rem 0;font-size:.9rem;color:var(--text);
  padding-left:1.5rem;position:relative;
}
.retailers-text li::before{
  content:'';position:absolute;left:0;top:.85rem;
  width:8px;height:8px;background:var(--gold);border-radius:50%;
}
.qr-highlight{
  background:#fff;border-left:3px solid var(--gold);
  padding:1.25rem 1.5rem;margin-bottom:2rem;
}
.qr-highlight p{font-size:.88rem;color:var(--text);margin:0;line-height:1.7}
.qr-highlight strong{color:var(--teal)}

.retailers-cta-box{
  background:#fff;padding:clamp(2.5rem,5vw,3.5rem);text-align:center;
  border:1px solid rgba(11,74,63,.08);
  box-shadow:0 8px 32px rgba(11,74,63,.04);
}
.retailers-cta-box h3{font-family:var(--serif);font-size:1.4rem;color:var(--heading);margin-bottom:1rem}
.retailers-cta-box p{color:#666;font-size:.9rem;margin-bottom:2rem;line-height:1.7}
.btn-gold{
  display:inline-flex;align-items:center;gap:.8rem;
  background:var(--gold);color:var(--dark);
  padding:1rem 2.2rem;font-size:.75rem;letter-spacing:.15em;text-transform:uppercase;font-weight:700;
  transition:all .25s;box-shadow:0 4px 20px rgba(201,162,39,.2);
}
.btn-gold:hover{background:var(--gold-hi);transform:translateY(-2px);box-shadow:0 8px 32px rgba(201,162,39,.3)}

@media(max-width:820px){.retailers-grid{grid-template-columns:1fr}}

/* ═══════════ DISTRIBUTORS ═══════════ */
.distributors{background:var(--bg);padding:var(--section-pad) 0}
.distributors-header{text-align:center;margin-bottom:clamp(2.5rem,5vw,4rem)}
.distributors-header .label{display:block;margin-bottom:.5rem}
.distributors-header .gold-rule{margin:0 auto 1.75rem}
.distributors-header h2{font-family:var(--serif);font-size:clamp(2rem,4vw,3rem);font-weight:700;color:var(--heading);line-height:1.1}

.top-seller{
  max-width:480px;margin:0 auto 3rem;background:#fff;
  border:2px solid var(--gold);padding:2rem 2.25rem;position:relative;
  box-shadow:0 8px 40px rgba(201,162,39,.1);transition:transform .3s,box-shadow .3s;
}
.top-seller:hover{transform:translateY(-4px);box-shadow:0 16px 56px rgba(201,162,39,.15)}
.top-badge{
  position:absolute;top:-12px;left:50%;transform:translateX(-50%);
  background:var(--gold);color:var(--dark);padding:.35rem 1.25rem;
  font-size:.6rem;letter-spacing:.18em;text-transform:uppercase;font-weight:700;
  white-space:nowrap;
}
.top-seller h3{font-family:var(--serif);font-size:1.3rem;color:var(--teal);font-weight:700;margin-bottom:.3rem;margin-top:.7rem;text-align:center}
.top-seller p{color:#888;font-size:.82rem;letter-spacing:.04em;text-align:center}

.dist-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.25rem}
.dist-card{
  background:#fff;border:1px solid rgba(11,74,63,.06);padding:1.4rem 1.6rem;
  transition:all .3s;
}
.dist-card:hover{border-color:rgba(11,74,63,.15);transform:translateY(-3px);box-shadow:0 8px 28px rgba(11,74,63,.06)}
.dist-card h3{font-family:var(--serif);font-size:.95rem;color:var(--teal);font-weight:700;margin-bottom:.2rem}
.dist-card p{color:#888;font-size:.78rem;letter-spacing:.04em}

@media(max-width:768px){.dist-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:480px){.dist-grid{grid-template-columns:1fr}}

/* ═══════════ CONTACT ═══════════ */
.contact{background:#fff;padding:var(--section-pad) 0}
.contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(3rem,6vw,5rem);align-items:start}
.contact-info .label{display:block;margin-bottom:.5rem}
.contact-info .gold-rule{margin-bottom:1.75rem}
.contact-info h2{font-family:var(--serif);font-size:clamp(1.8rem,3.5vw,2.6rem);font-weight:700;color:var(--heading);line-height:1.15;margin-bottom:1.75rem}
.contact-info address{font-style:normal;color:#666;font-size:.9rem;line-height:2.1}
.contact-info address strong{color:var(--heading);font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;display:block;margin-top:1.25rem;font-family:var(--sans)}
.contact-info address strong:first-child{margin-top:0}
.contact-info address a{border-bottom:1px solid rgba(11,74,63,.15);transition:border-color .25s}
.contact-info address a:hover{border-color:var(--teal)}

.contact-form{display:flex;flex-direction:column;gap:1.2rem}
.form-group{display:flex;flex-direction:column;gap:.35rem}
.form-group label{font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;font-weight:700;color:var(--teal);font-family:var(--sans)}
.form-group input,.form-group textarea{
  font-family:inherit;font-size:.9rem;padding:.85rem 1rem;
  border:1px solid rgba(11,74,63,.1);background:var(--bg);
  color:var(--text);transition:border-color .25s,box-shadow .25s;outline:none;
  min-height:48px;
}
.form-group input:focus,.form-group textarea:focus{border-color:var(--teal);box-shadow:0 0 0 3px rgba(11,74,63,.06)}
.form-group textarea{resize:vertical;min-height:120px}
.form-submit{
  display:inline-flex;align-items:center;gap:.8rem;
  background:var(--teal);color:#fff;
  padding:1rem 2.2rem;font-size:.75rem;letter-spacing:.15em;text-transform:uppercase;font-weight:700;
  transition:background .25s,transform .2s;align-self:flex-start;border:none;cursor:pointer;
  min-height:48px;
}
.form-submit:hover{background:#0d6454;transform:translateY(-2px)}

@media(max-width:820px){.contact-grid{grid-template-columns:1fr}}

/* ═══════════ FOOTER ═══════════ */
.footer{background:var(--dark);color:rgba(255,255,255,.55);padding:clamp(4rem,8vw,6rem) 0 0}
.footer-grid{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:clamp(2rem,4vw,4rem)}
.footer-logo{height:48px;width:auto;mix-blend-mode:screen;margin-bottom:1.25rem;filter:brightness(1.5)}
.footer-brand .gold-rule{margin-bottom:1.25rem}
.footer-brand p{font-size:.85rem;line-height:1.8;max-width:340px;margin-bottom:1.5rem}
.footer-social{display:flex;gap:.8rem}
.footer-social a{
  width:36px;height:36px;display:flex;align-items:center;justify-content:center;
  border:1px solid rgba(255,255,255,.1);color:rgba(255,255,255,.5);transition:all .25s;
  min-width:48px;min-height:48px;
}
.footer-social a:hover{border-color:var(--gold);color:var(--gold);background:rgba(201,162,39,.06)}
.footer-social a svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.8}
.footer-col h4{color:#fff;font-size:.68rem;letter-spacing:.2em;text-transform:uppercase;font-weight:700;margin-bottom:1.2rem;font-family:var(--sans)}
.footer-col address{font-style:normal;font-size:.82rem;line-height:2}
.footer-col a{transition:color .25s}
.footer-col a:hover{color:var(--gold)}
.footer-bottom{
  margin-top:clamp(3rem,5vw,5rem);border-top:1px solid rgba(255,255,255,.06);
  padding:1.75rem 0;display:flex;justify-content:space-between;flex-wrap:wrap;gap:.75rem;
  font-size:.7rem;color:rgba(255,255,255,.3);
}
.footer-pride{color:var(--gold);font-weight:600;letter-spacing:.06em}

@media(max-width:820px){
  .footer-grid{grid-template-columns:1fr}
  .footer-bottom{flex-direction:column;text-align:center}
}

/* Back to top */
.back-top{
  position:fixed;bottom:2rem;right:2rem;z-index:90;
  width:48px;height:48px;display:flex;align-items:center;justify-content:center;
  background:var(--teal);color:#fff;border:1px solid rgba(255,255,255,.1);
  opacity:0;pointer-events:none;transform:translateY(12px);
  transition:opacity .35s,transform .35s,background .25s;
}
.back-top.vis{opacity:1;pointer-events:auto;transform:translateY(0)}
.back-top:hover{background:#0d6454}
.back-top svg{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:2.5}
'''

# ─── NEW HTML ───
chunk3_html = '''
<!-- FACTORY -->
<section class="factory" id="factory" aria-label="Our Factory">
  <div class="container">
    <div class="factory-header rv">
      <span class="label" data-i18n="factLabel">Manufacturing</span>
      <span class="gold-rule"></span>
      <h2 data-i18n="factH2">Our Factory</h2>
    </div>
    <div class="factory-grid">
      <img class="factory-img rv" src="''' + b64.factory1 + '''" alt="Rivera Springs factory exterior, Amgaon Rd, Adashi, Tanda" loading="lazy">
      <img class="factory-img rv rv-d1" src="''' + b64.factory2 + '''" alt="Rivera Springs bottling plant, corrugated steel building" loading="lazy">
    </div>
    <div class="factory-cap rv rv-d2">
      <p data-i18n="factP">Our facility at Tanda, Dist. Gondia operates a fully automated bottling line with no manual handling from water intake to sealed product. The plant follows pharmaceutical-grade hygiene standards \u2014 stainless steel piping, positive-pressure clean rooms, and real-time quality monitoring at every stage.</p>
      <div class="stat-line" data-i18n="factStat">90 bottles per minute. 4\u20135 boxes per minute. Fully automated line.</div>
    </div>
  </div>
</section>

<!-- RETAILERS -->
<section class="retailers" id="retailers" aria-label="Retailers">
  <div class="container">
    <div class="retailers-grid">
      <div class="retailers-text rv">
        <span class="label" data-i18n="retLabel">For Retailers</span>
        <span class="gold-rule"></span>
        <h2 data-i18n="retH2">Stock Rivera Springs in your store</h2>
        <p data-i18n="retP1">We are building a retail network across Maharashtra and neighbouring states. If you run a kirana store, supermarket, restaurant, hotel, or any establishment that serves water to customers, we want to hear from you.</p>
        <ul>
          <li data-i18n="retB1">Loyalty rewards programme with direct brand support</li>
          <li data-i18n="retB2">Point-of-sale marketing materials provided free</li>
          <li data-i18n="retB3">Dedicated territory support \u2014 no overlapping distributors</li>
          <li data-i18n="retB4">Competitive retailer margins on all SKUs</li>
        </ul>
        <div class="qr-highlight">
          <p data-i18n="retQR" data-i18n-html="true"><strong>QR-based credit system:</strong> Scan the QR code on every box to earn 1 credit point. Accumulate 30 points and redeem for 1 free box (redeemable after 30 days). Points tracked digitally \u2014 no paper coupons, no disputes.</p>
        </div>
      </div>
      <div class="retailers-cta-box rv rv-d2">
        <h3 data-i18n="retCtaH">Become a Rivera Springs Retailer</h3>
        <p data-i18n="retCtaP">Fill out the contact form below or call us directly. Our distribution team will reach out within 48 hours with territory details and pricing.</p>
        <a href="#contact" class="btn-gold" data-i18n="retCtaBtn">Partner With Us</a>
      </div>
    </div>
  </div>
</section>

<!-- DISTRIBUTORS -->
<section class="distributors" id="distributors" aria-label="Our Proud Distributors">
  <div class="container">
    <div class="distributors-header rv">
      <span class="label" data-i18n="distLabel">Distribution Network</span>
      <span class="gold-rule"></span>
      <h2 data-i18n="distH2">Our Proud Distributors</h2>
    </div>
    <div class="top-seller rv rv-d1">
      <div class="top-badge" data-i18n="topBadge">\u2b50 Top Seller</div>
      <h3 data-i18n="topName">[TOP DISTRIBUTOR NAME]</h3>
      <p data-i18n="topRegion">[Region \u2014 e.g., Nagpur Division, Maharashtra]</p>
    </div>
    <div class="dist-grid">
      <div class="dist-card rv rv-d1"><h3 data-i18n="d1Name">[Distributor 1]</h3><p data-i18n="d1City">[City/Region]</p></div>
      <div class="dist-card rv rv-d2"><h3 data-i18n="d2Name">[Distributor 2]</h3><p data-i18n="d2City">[City/Region]</p></div>
      <div class="dist-card rv rv-d2"><h3 data-i18n="d3Name">[Distributor 3]</h3><p data-i18n="d3City">[City/Region]</p></div>
      <div class="dist-card rv rv-d3"><h3 data-i18n="d4Name">[Distributor 4]</h3><p data-i18n="d4City">[City/Region]</p></div>
      <div class="dist-card rv rv-d3"><h3 data-i18n="d5Name">[Distributor 5]</h3><p data-i18n="d5City">[City/Region]</p></div>
      <div class="dist-card rv rv-d4"><h3 data-i18n="d6Name">[Distributor 6]</h3><p data-i18n="d6City">[City/Region]</p></div>
    </div>
  </div>
</section>

<!-- CONTACT -->
<section class="contact" id="contact" aria-label="Contact">
  <div class="container">
    <div class="contact-grid">
      <div class="contact-info rv">
        <span class="label" data-i18n="conLabel">Get in Touch</span>
        <span class="gold-rule"></span>
        <h2 data-i18n="conH2">We would love to hear from you</h2>
        <address>
          <strong data-i18n="conCompL">Company</strong>
          <span data-i18n="conComp">Rivera Springs (Brand of Maya International Exports)</span><br>
          <strong data-i18n="conAddrL">Address</strong>
          <span data-i18n="conAddr">Gat No 407/1/B Tanda, Tah &amp; Dist Gondia, Maharashtra-441614</span><br>
          <strong data-i18n="conPhoneL">Phone</strong>
          <a href="tel:+919890640603" data-i18n="conPhone">+91 98906 40603</a><br>
          <strong data-i18n="conEmailL">Email</strong>
          <a href="mailto:mayainternationalexports06@gmail.com" data-i18n="conEmail">mayainternationalexports06@gmail.com</a><br>
          <strong>FSSAI</strong>
          <span>11526999000410</span>
        </address>
      </div>
      <form class="contact-form rv rv-d2" id="contactForm" aria-label="Contact form" onsubmit="return false;">
        <div class="form-group">
          <label for="cName" data-i18n="fName">Name</label>
          <input type="text" id="cName" name="name" autocomplete="name" required>
        </div>
        <div class="form-group">
          <label for="cPhone" data-i18n="fPhone">Phone</label>
          <input type="tel" id="cPhone" name="phone" autocomplete="tel">
        </div>
        <div class="form-group">
          <label for="cMsg" data-i18n="fMsg">Message</label>
          <textarea id="cMsg" name="message" rows="5" required></textarea>
        </div>
        <button type="submit" class="form-submit" data-i18n="fSubmit">Send Message</button>
      </form>
    </div>
  </div>
</section>
'''

# ─── FOOTER + BACK-TO-TOP (after </main>) ───
footer_html = '''
</main>

<!-- FOOTER -->
<footer class="footer" aria-label="Footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="''' + b64.logo_dark + '''" alt="Rivera Springs" class="footer-logo" loading="lazy">
        <span class="gold-rule"></span>
        <p data-i18n="footDesc">Packaged drinking water with added minerals, sourced and bottled at origin in Amgaon, Maharashtra. A brand of Maya International Exports.</p>
        <div class="footer-social">
          <a href="#" aria-label="Facebook"><svg viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg></a>
          <a href="#" aria-label="Instagram"><svg viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="5"/><circle cx="17.5" cy="6.5" r="1.5"/></svg></a>
        </div>
      </div>
      <div class="footer-col">
        <h4 data-i18n="footOffice">Registered Office</h4>
        <address>
          <span data-i18n="footLine1">Maya International Exports</span><br>
          <span data-i18n="footLine2">Gat No 407/1/B Tanda</span><br>
          <span data-i18n="footLine3">Tah &amp; Dist Gondia, Maharashtra-441614</span>
        </address>
      </div>
      <div class="footer-col">
        <h4 data-i18n="footConH">Get in Touch</h4>
        <address>
          <strong style="color:#fff;font-size:.72rem" data-i18n="footTrade">Trade Enquiries</strong><br>
          <a href="tel:+919890640603">+91 98906 40603</a><br>
          <a href="mailto:mayainternationalexports06@gmail.com">mayainternationalexports06@gmail.com</a><br><br>
          <strong style="color:#fff;font-size:.72rem">FSSAI</strong><br>
          11526999000410
        </address>
      </div>
    </div>
    <div class="footer-bottom">
      <span data-i18n="footCopy" data-i18n-html="true">&copy; 2024 Rivera Springs Pvt. Ltd. All rights reserved.</span>
      <span class="footer-pride" data-i18n="footPride">Made with pride in Amgaon, Maharashtra</span>
    </div>
  </div>
</footer>

<a href="#hero" class="back-top" id="backTop" aria-label="Back to top">
  <svg viewBox="0 0 24 24"><polyline points="18 15 12 9 6 15"/></svg>
</a>
'''

# ─── i18n SYSTEM (full JS) ───
i18n_js = r'''
  /* ═══════ Contact form feedback ═══════ */
  document.getElementById('contactForm').addEventListener('submit',function(e){
    e.preventDefault();var b=this.querySelector('.form-submit');var ot=b.textContent;
    var lang=document.documentElement.lang;
    b.textContent=lang==='hi'?'\u092d\u0947\u091c\u093e \u0917\u092f\u093e!':lang==='mr'?'\u092a\u093e\u0920\u0935\u0932\u0947!':'Sent!';
    b.style.background='var(--gold)';b.style.color='var(--dark)';
    setTimeout(function(){b.textContent=ot;b.style.background='';b.style.color=''},2000);
  });

  /* ═══════ i18n ═══════ */
  var T={
en:{
skip:'Skip to main content',
navSource:'The Source',navRange:'Our Range',navQuality:'Quality',navFounder:"Founder\u2019s Journey",navFactory:'Factory',navRetailers:'Retailers',navDistributors:'Distributors',navContact:'Contact',
heroLabel:'Packaged Drinking Water \u00b7 Added Minerals',
heroRivera:'RIVERA',heroSprings:'Springs',
heroWmTag:'Born from Nature. Bottled for You.',
heroH1:'Pure water from the <em>heart of India.</em>',
heroCta:'Discover the Source',
stat1Val:'7 Stage',stat1Label:'Filtration',stat2Label:'Parts Per Million',stat3Label:'BIS Certified',
scrollCue:'Scroll',
srcLabel:'The Source',
srcH2:"Pure water from Satpura\u2019s pristine waterfalls, not a municipal borewell",
srcP1:"Rivera Springs draws from the pure, untouched waterfalls and natural springs near the <strong>Satpura foothills</strong> \u2014 water naturally filtered through ancient rock formations over millennia. Rich in <strong>Magnesium, Potassium &amp; Sodium</strong>, this water carries the balanced mineral profile that only geological filtration can provide.",
srcP2:"This isn\u2019t treated municipal water or borewell supply dressed up with a label. This is nature\u2019s own filtration, bottled at the source. We pipe from spring to plant within a closed circuit \u2014 no tanker transport, no open-air holding. The bottling facility sits at the source, not hundreds of kilometres away in an industrial estate.",
jWaterfall:'Waterfall',jSpring:'Spring',jSandFilt:'Sand Filtration',jCarbFilt:'Carbon Filtration',jUVOzone:'UV & Ozone',jBottle:'Bottling',jYou:'You',
statRegion:'Region',statRegionV:'Satpura Hills',statType:'Source Type',statTypeV:'Natural Spring',
prodLabel:'Our Range',
prodH2:'Every format,<br>one source<span class="gold-rule" style="margin-top:1rem"></span>',
prodDesc:'All bottles use the same spring source and undergo identical multi-stage purification. The only difference is the pack format.',
p250name:'Compact',p250use:'Perfect for on-the-go. Toss it in your bag, keep one at the counter, hand it out at events.',
p500name:'Everyday',p500use:'The everyday essential. For retail counters, restaurants, and daily hydration.',
p1Lname:'Standard',p1Luse:'For home & office. Daily hydration, family dining, and general trade.',
qualLabel:'Quality & Certification',
qualH2:'Tested at source, tested at line, tested before dispatch',
qualIntro:'Every production batch is sampled and tested against parameters mandated by IS 14543:2016. Records are maintained for FSSAI inspection on demand.',
qualSrcH:'Sourcing',qualSrcP:"Natural springs near the Satpura foothills. Water surfaces through ancient rock formations that impart a balanced mineral profile \u2014 Magnesium, Potassium, Sodium and Calcium in naturally occurring proportions. TDS maintained between 50\u2013120 ppm.",
qualProcH:'Processing',qualProcP:"Multi-stage treatment as printed on every label: Sand Filtration, Carbon Filtration, Reverse Osmosis, UV Treatment & Ozonisation. Added minerals: Magnesium, Potassium & Sodium. Fully automated bottling line \u2014 no manual handling from intake to sealed cap.",
qualCertH:'Certification',qualCertP:'FSSAI Licensed (Lic No: 11526999000410). IS 14543 compliant. ISO 22000 food safety management. BIS certification mark on every bottle. Manufactured & marketed by Maya International Exports, Gat No. 407/1/B, Tanda, Tal & Dist Gondia, Maharashtra 441614.',
certBIS:'BIS Certified',certFSSAI:'FSSAI Licensed',
mineralCap:'Typical Mineral Composition (mg/L)',mineralParam:'Parameter',mineralVal:'Value',
mTDS:'Total Dissolved Solids (TDS)',mCa:'Calcium (Ca\u00b2\u207a)',mMg:'Magnesium (Mg\u00b2\u207a)',mK:'Potassium (K\u207a)',mNa:'Sodium (Na\u207a)',mCl:'Chloride (Cl\u207b)',mSO4:'Sulphate (SO\u2084\u00b2\u207b)',mF:'Fluoride (F\u207b)',mNO3:'Nitrate (NO\u2083\u207b)',
fdrPhPh:'[FOUNDER PHOTO \u2014 Saurabh K]',fdrName:'Saurabh K',fdrTitle:'Founder, Rivera Springs',
fdrLabel:"Founder\u2019s Journey",
fdrH2:'Building a water brand that earns the label it prints',
fdrP1:"Saurabh K is a young man from Amgaon, a small town in eastern Maharashtra\u2019s Gondia district. Not born into the water business \u2014 he studied the industry from scratch, learning every link in the chain from natural springs to automated bottling, from BIS compliance paperwork to last-mile distribution logistics.",
fdrP2:"The founding moment came from a simple realisation: his region deserved spring-quality water at the standard of national brands, not just another borewell-and-RO operation printing \u201cmineral water\u201d on a label. He founded Maya International Exports and set up the Rivera Springs bottling line near Amgaon \u2014 deliberately close to the source rather than close to the market.",
fdrP3:"What drives him is an obsession with water quality that goes beyond mere compliance \u2014 every batch tested, every source monitored, every deviation investigated. The ambition is clear: making Rivera Springs the brand that Vidarbha and all of Maharashtra trusts. Not the cheapest option on the shelf, but the cleanest.",
fdrQuote:'\u201c[FOUNDER QUOTE \u2014 will add later]\u201d',fdrCite:'Saurabh K, Founder',
factLabel:'Manufacturing',factH2:'Our Factory',
factP:"Our facility at Tanda, Dist. Gondia operates a fully automated bottling line with no manual handling from water intake to sealed product. The plant follows pharmaceutical-grade hygiene standards \u2014 stainless steel piping, positive-pressure clean rooms, and real-time quality monitoring at every stage.",
factStat:'90 bottles per minute. 4\u20135 boxes per minute. Fully automated line.',
retLabel:'For Retailers',retH2:'Stock Rivera Springs in your store',
retP1:'We are building a retail network across Maharashtra and neighbouring states. If you run a kirana store, supermarket, restaurant, hotel, or any establishment that serves water to customers, we want to hear from you.',
retB1:'Loyalty rewards programme with direct brand support',retB2:'Point-of-sale marketing materials provided free',retB3:'Dedicated territory support \u2014 no overlapping distributors',retB4:'Competitive retailer margins on all SKUs',
retQR:'<strong>QR-based credit system:</strong> Scan the QR code on every box to earn 1 credit point. Accumulate 30 points and redeem for 1 free box (redeemable after 30 days). Points tracked digitally \u2014 no paper coupons, no disputes.',
retCtaH:'Become a Rivera Springs Retailer',retCtaP:'Fill out the contact form below or call us directly. Our distribution team will reach out within 48 hours with territory details and pricing.',retCtaBtn:'Partner With Us',
distLabel:'Distribution Network',distH2:'Our Proud Distributors',
topBadge:'\u2b50 Top Seller',topName:'[TOP DISTRIBUTOR NAME]',topRegion:'[Region \u2014 e.g., Nagpur Division, Maharashtra]',
d1Name:'[Distributor 1]',d1City:'[City/Region]',d2Name:'[Distributor 2]',d2City:'[City/Region]',d3Name:'[Distributor 3]',d3City:'[City/Region]',d4Name:'[Distributor 4]',d4City:'[City/Region]',d5Name:'[Distributor 5]',d5City:'[City/Region]',d6Name:'[Distributor 6]',d6City:'[City/Region]',
conLabel:'Get in Touch',conH2:'We would love to hear from you',
conCompL:'Company',conComp:'Rivera Springs (Brand of Maya International Exports)',conAddrL:'Address',conAddr:'Gat No 407/1/B Tanda, Tah & Dist Gondia, Maharashtra-441614',
conPhoneL:'Phone',conPhone:'+91 98906 40603',conEmailL:'Email',conEmail:'mayainternationalexports06@gmail.com',
fName:'Name',fPhone:'Phone',fMsg:'Message',fSubmit:'Send Message',
footDesc:'Packaged drinking water with added minerals, sourced and bottled at origin in Amgaon, Maharashtra. A brand of Maya International Exports.',
footOffice:'Registered Office',footLine1:'Maya International Exports',footLine2:'Gat No 407/1/B Tanda',footLine3:'Tah & Dist Gondia, Maharashtra-441614',
footConH:'Get in Touch',footTrade:'Trade Enquiries',
footCopy:'&copy; 2024 Rivera Springs Pvt. Ltd. All rights reserved.',footPride:'Made with pride in Amgaon, Maharashtra'
},

hi:{
skip:'\u092e\u0941\u0916\u094d\u092f \u0938\u093e\u092e\u0917\u094d\u0930\u0940 \u092a\u0930 \u091c\u093e\u090f\u0901',
navSource:'\u0938\u094d\u0930\u094b\u0924',navRange:'\u0939\u092e\u093e\u0930\u0940 \u0930\u0947\u0902\u091c',navQuality:'\u0917\u0941\u0923\u0935\u0924\u094d\u0924\u093e',navFounder:'\u0938\u0902\u0938\u094d\u0925\u093e\u092a\u0915 \u0915\u0940 \u0915\u0939\u093e\u0928\u0940',navFactory:'\u0915\u093e\u0930\u0916\u093e\u0928\u093e',navRetailers:'\u0930\u093f\u091f\u0947\u0932\u0930\u094d\u0938',navDistributors:'\u0935\u093f\u0924\u0930\u0915',navContact:'\u0938\u0902\u092a\u0930\u094d\u0915',
heroLabel:'\u092a\u0948\u0915\u094d\u0921 \u092a\u0947\u092f\u091c\u0932 \u00b7 \u0916\u0928\u093f\u091c \u092f\u0941\u0915\u094d\u0924',
heroRivera:'\u0930\u093f\u0935\u0947\u0930\u093e',heroSprings:'\u0938\u094d\u092a\u094d\u0930\u093f\u0902\u0917\u094d\u0938',
heroWmTag:'\u092a\u094d\u0930\u0915\u0943\u0924\u093f \u0938\u0947 \u091c\u0928\u094d\u092e\u093e\u0964 \u0906\u092a\u0915\u0947 \u0932\u093f\u090f \u092c\u094b\u0924\u0932\u092c\u0902\u0926\u0964',
heroH1:'<em>\u092d\u093e\u0930\u0924 \u0915\u0947 \u0926\u093f\u0932</em> \u0938\u0947 \u0936\u0941\u0926\u094d\u0927 \u092a\u093e\u0928\u0940\u0964',
heroCta:'\u0938\u094d\u0930\u094b\u0924 \u091c\u093e\u0928\u0947\u0902',
stat1Val:'7 \u091a\u0930\u0923',stat1Label:'\u092b\u093c\u093f\u0932\u094d\u091f\u094d\u0930\u0947\u0936\u0928',stat2Label:'\u092a\u094d\u0930\u0924\u093f \u0926\u0938 \u0932\u093e\u0916',stat3Label:'BIS \u092a\u094d\u0930\u092e\u093e\u0923\u093f\u0924',
scrollCue:'\u0928\u0940\u091a\u0947 \u0938\u094d\u0915\u094d\u0930\u0949\u0932 \u0915\u0930\u0947\u0902',
srcLabel:'\u0938\u094d\u0930\u094b\u0924',
srcH2:'\u0938\u093e\u0924\u092a\u0941\u0921\u093c\u093e \u0915\u0947 \u091d\u0930\u0928\u094b\u0902 \u0938\u0947 \u0936\u0941\u0926\u094d\u0927 \u092a\u093e\u0928\u0940, \u092e\u094d\u092f\u0941\u0928\u093f\u0938\u093f\u092a\u0932 \u092c\u094b\u0930\u0935\u0947\u0932 \u0928\u0939\u0940\u0902',
srcP1:'\u0930\u093f\u0935\u0947\u0930\u093e \u0938\u094d\u092a\u094d\u0930\u093f\u0902\u0917\u094d\u0938 \u0915\u093e \u092a\u093e\u0928\u0940 <strong>\u0938\u093e\u0924\u092a\u0941\u0921\u093c\u093e \u0915\u0940 \u0924\u0932\u0939\u091f\u0940</strong> \u0915\u0947 \u092a\u093e\u0938 \u092a\u094d\u0930\u093e\u0915\u0943\u0924\u093f\u0915 \u091d\u0930\u0928\u094b\u0902 \u0914\u0930 \u091d\u0930\u0928\u094b\u0902 \u0938\u0947 \u0906\u0924\u093e \u0939\u0948 \u2014 \u092a\u0941\u0930\u093e\u0928\u0940 \u091a\u091f\u094d\u091f\u093e\u0928\u094b\u0902 \u0938\u0947 \u0939\u091c\u093c\u093e\u0930\u094b\u0902 \u0938\u093e\u0932\u094b\u0902 \u0938\u0947 \u091b\u0928\u0915\u0930 \u0906\u092f\u093e \u092a\u093e\u0928\u0940\u0964 <strong>\u092e\u0948\u0917\u094d\u0928\u0940\u0936\u093f\u092f\u092e, \u092a\u094b\u091f\u0948\u0936\u093f\u092f\u092e \u0914\u0930 \u0938\u094b\u0921\u093f\u092f\u092e</strong> \u0938\u0947 \u092d\u0930\u092a\u0942\u0930\u0964',
srcP2:'\u092f\u0939 \u092e\u094d\u092f\u0941\u0928\u093f\u0938\u093f\u092a\u0932 \u0915\u093e \u092a\u093e\u0928\u0940 \u0928\u0939\u0940\u0902 \u0939\u0948\u0964 \u092f\u0939 \u092a\u094d\u0930\u0915\u0943\u0924\u093f \u0915\u093e \u0905\u092a\u0928\u093e \u092b\u093c\u093f\u0932\u094d\u091f\u094d\u0930\u0947\u0936\u0928 \u0939\u0948, \u0938\u094d\u0930\u094b\u0924 \u092a\u0930 \u0939\u0940 \u092c\u094b\u0924\u0932\u092c\u0902\u0926\u0964 \u091d\u0930\u0928\u0947 \u0938\u0947 \u092a\u094d\u0932\u093e\u0902\u091f \u0924\u0915 \u092c\u0902\u0926 \u092a\u093e\u0907\u092a\u0932\u093e\u0907\u0928 \u0938\u0947 \u092a\u0939\u0941\u0901\u091a\u0924\u093e \u0939\u0948 \u2014 \u0928 \u091f\u0948\u0902\u0915\u0930, \u0928 \u0916\u0941\u0932\u0940 \u0939\u0935\u093e \u092e\u0947\u0902 \u0930\u0916\u0928\u093e\u0964',
jWaterfall:'\u091d\u0930\u0928\u093e',jSpring:'\u091d\u0930\u0928\u093e',jSandFilt:'\u0930\u0947\u0924 \u091b\u0928\u0928\u0940',jCarbFilt:'\u0915\u093e\u0930\u094d\u092c\u0928 \u091b\u0928\u0928\u0940',jUVOzone:'UV \u0914\u0930 \u0913\u091c\u093c\u094b\u0928',jBottle:'\u092c\u094b\u0924\u0932\u093f\u0902\u0917',jYou:'\u0906\u092a',
statRegion:'\u0915\u094d\u0937\u0947\u0924\u094d\u0930',statRegionV:'\u0938\u093e\u0924\u092a\u0941\u0921\u093c\u093e \u092a\u0939\u093e\u0921\u093c\u0940',statType:'\u0938\u094d\u0930\u094b\u0924 \u092a\u094d\u0930\u0915\u093e\u0930',statTypeV:'\u092a\u094d\u0930\u093e\u0915\u0943\u0924\u093f\u0915 \u091d\u0930\u0928\u093e',
prodLabel:'\u0939\u092e\u093e\u0930\u0940 \u0930\u0947\u0902\u091c',
prodH2:'\u0939\u0930 \u092b\u0949\u0930\u094d\u092e\u0947\u091f,<br>\u090f\u0915 \u0938\u094d\u0930\u094b\u0924<span class="gold-rule" style="margin-top:1rem"></span>',
prodDesc:'\u0938\u092d\u0940 \u092c\u094b\u0924\u0932\u0947\u0902 \u090f\u0915 \u0939\u0940 \u091d\u0930\u0928\u0947 \u0915\u0947 \u0938\u094d\u0930\u094b\u0924 \u0938\u0947 \u0906\u0924\u0940 \u0939\u0948\u0902\u0964 \u092b\u0930\u094d\u0915 \u0938\u093f\u0930\u094d\u092b\u093c \u092a\u0948\u0915 \u0915\u093e \u0939\u0948\u0964',
p250name:'\u0915\u0949\u092e\u094d\u092a\u0948\u0915\u094d\u091f',p250use:'\u091a\u0932\u0924\u0947-\u092b\u093f\u0930\u0924\u0947 \u0915\u0947 \u0932\u093f\u090f\u0964 \u092c\u0948\u0917 \u092e\u0947\u0902 \u0921\u093e\u0932\u094b, \u0915\u093e\u0909\u0902\u091f\u0930 \u092a\u0930 \u0930\u0916\u094b, \u0907\u0935\u0947\u0902\u091f \u092e\u0947\u0902 \u092c\u093e\u0901\u091f\u094b\u0964',
p500name:'\u0930\u094b\u091c\u093c\u093e\u0928\u093e',p500use:'\u0930\u094b\u091c\u093c\u092e\u0930\u094d\u0930\u093e \u0915\u0940 \u091c\u093c\u0930\u0942\u0930\u0924\u0964 \u0926\u0941\u0915\u093e\u0928, \u0930\u0947\u0938\u094d\u0924\u0930\u093e\u0902 \u0914\u0930 \u0930\u094b\u091c\u093c\u093e\u0928\u093e \u0909\u092a\u092f\u094b\u0917 \u0915\u0947 \u0932\u093f\u090f\u0964',
p1Lname:'\u0938\u094d\u091f\u0948\u0902\u0921\u0930\u094d\u0921',p1Luse:'\u0918\u0930 \u0914\u0930 \u0926\u092b\u093c\u094d\u0924\u0930 \u0915\u0947 \u0932\u093f\u090f\u0964 \u092a\u0930\u093f\u0935\u093e\u0930\u093f\u0915 \u092d\u094b\u091c\u0928 \u0914\u0930 \u0930\u094b\u091c\u093c\u093e\u0928\u093e \u0909\u092a\u092f\u094b\u0917\u0964',
qualLabel:'\u0917\u0941\u0923\u0935\u0924\u094d\u0924\u093e \u0914\u0930 \u092a\u094d\u0930\u092e\u093e\u0923\u0928',
qualH2:'\u0938\u094d\u0930\u094b\u0924 \u092a\u0930 \u092a\u0930\u0940\u0915\u094d\u0937\u0923, \u0932\u093e\u0907\u0928 \u092a\u0930 \u092a\u0930\u0940\u0915\u094d\u0937\u0923, \u092d\u0947\u091c\u0928\u0947 \u0938\u0947 \u092a\u0939\u0932\u0947 \u092a\u0930\u0940\u0915\u094d\u0937\u0923',
qualIntro:'\u0939\u0930 \u092c\u0948\u091a \u0915\u093e \u0928\u092e\u0942\u0928\u093e \u0932\u093f\u092f\u093e \u091c\u093e\u0924\u093e \u0939\u0948 \u0914\u0930 IS 14543:2016 \u0915\u0947 \u092e\u093e\u0928\u0915\u094b\u0902 \u0915\u0947 \u0905\u0928\u0941\u0938\u093e\u0930 \u091c\u093e\u0901\u091a\u093e \u091c\u093e\u0924\u093e \u0939\u0948\u0964',
qualSrcH:'\u0938\u094d\u0930\u094b\u0924',qualSrcP:'\u0938\u093e\u0924\u092a\u0941\u0921\u093c\u093e \u0915\u0940 \u0924\u0932\u0939\u091f\u0940 \u0915\u0947 \u092a\u094d\u0930\u093e\u0915\u0943\u0924\u093f\u0915 \u091d\u0930\u0928\u0947\u0964 TDS 50\u2013120 ppm\u0964 \u092e\u0948\u0917\u094d\u0928\u0940\u0936\u093f\u092f\u092e, \u092a\u094b\u091f\u0948\u0936\u093f\u092f\u092e, \u0938\u094b\u0921\u093f\u092f\u092e \u0914\u0930 \u0915\u0948\u0932\u094d\u0936\u093f\u092f\u092e \u092a\u094d\u0930\u093e\u0915\u0943\u0924\u093f\u0915 \u0905\u0928\u0941\u092a\u093e\u0924 \u092e\u0947\u0902\u0964',
qualProcH:'\u092a\u094d\u0930\u0915\u094d\u0930\u093f\u092f\u093e',qualProcP:'\u0930\u0947\u0924 \u091b\u0928\u0928\u0940, \u0915\u093e\u0930\u094d\u092c\u0928 \u091b\u0928\u0928\u0940, \u0930\u093f\u0935\u0930\u094d\u0938 \u0911\u0938\u094d\u092e\u094b\u0938\u093f\u0938, UV \u0914\u0930 \u0913\u091c\u093c\u094b\u0928\u0947\u0936\u0928\u0964 \u091c\u094b\u0921\u093c\u0947 \u0917\u090f \u0916\u0928\u093f\u091c: \u092e\u0948\u0917\u094d\u0928\u0940\u0936\u093f\u092f\u092e, \u092a\u094b\u091f\u0948\u0936\u093f\u092f\u092e \u0914\u0930 \u0938\u094b\u0921\u093f\u092f\u092e\u0964 \u0907\u0928\u091f\u0947\u0915 \u0938\u0947 \u0938\u0940\u0932 \u0924\u0915 \u092a\u0942\u0930\u0940 \u0924\u0930\u0939 \u0938\u094d\u0935\u091a\u093e\u0932\u093f\u0924\u0964',
qualCertH:'\u092a\u094d\u0930\u092e\u093e\u0923\u0928',qualCertP:'FSSAI \u0932\u093e\u0907\u0938\u0947\u0902\u0938 (11526999000410)\u0964 IS 14543 \u0905\u0928\u0941\u092a\u093e\u0932\u0928\u0964 ISO 22000 \u0916\u093e\u0926\u094d\u092f \u0938\u0941\u0930\u0915\u094d\u0937\u093e\u0964 BIS \u092a\u094d\u0930\u092e\u093e\u0923\u093f\u0924\u0964 \u0928\u093f\u0930\u094d\u092e\u093e\u0924\u093e: \u092e\u093e\u092f\u093e \u0907\u0902\u091f\u0930\u0928\u0947\u0936\u0928\u0932 \u090f\u0915\u094d\u0938\u092a\u094b\u0930\u094d\u091f\u094d\u0938, \u091f\u093e\u0902\u0921\u093e, \u0917\u094b\u0902\u0926\u093f\u092f\u093e\u0964',
certBIS:'BIS \u092a\u094d\u0930\u092e\u093e\u0923\u093f\u0924',certFSSAI:'FSSAI \u0932\u093e\u0907\u0938\u0947\u0902\u0938\u094d\u0921',
mineralCap:'\u0938\u093e\u092e\u093e\u0928\u094d\u092f \u0916\u0928\u093f\u091c \u0938\u0902\u0930\u091a\u0928\u093e (mg/L)',mineralParam:'\u092a\u0948\u0930\u093e\u092e\u0940\u091f\u0930',mineralVal:'\u092e\u093e\u0928',
mTDS:'\u0915\u0941\u0932 \u0918\u0941\u0932\u0928\u0936\u0940\u0932 \u0920\u094b\u0938 (TDS)',mCa:'\u0915\u0948\u0932\u094d\u0936\u093f\u092f\u092e (Ca\u00b2\u207a)',mMg:'\u092e\u0948\u0917\u094d\u0928\u0940\u0936\u093f\u092f\u092e (Mg\u00b2\u207a)',mK:'\u092a\u094b\u091f\u0948\u0936\u093f\u092f\u092e (K\u207a)',mNa:'\u0938\u094b\u0921\u093f\u092f\u092e (Na\u207a)',mCl:'\u0915\u094d\u0932\u094b\u0930\u093e\u0907\u0921 (Cl\u207b)',mSO4:'\u0938\u0932\u094d\u092b\u0947\u091f (SO\u2084\u00b2\u207b)',mF:'\u092b\u094d\u0932\u094b\u0930\u093e\u0907\u0921 (F\u207b)',mNO3:'\u0928\u093e\u0907\u091f\u094d\u0930\u0947\u091f (NO\u2083\u207b)',
fdrPhPh:'[\u0938\u0902\u0938\u094d\u0925\u093e\u092a\u0915 \u0915\u093e \u092b\u094b\u091f\u094b \u2014 \u0938\u094c\u0930\u092d]',fdrName:'\u0938\u094c\u0930\u092d \u0915\u0947.',fdrTitle:'\u0938\u0902\u0938\u094d\u0925\u093e\u092a\u0915, \u0930\u093f\u0935\u0947\u0930\u093e \u0938\u094d\u092a\u094d\u0930\u093f\u0902\u0917\u094d\u0938',
fdrLabel:'\u0938\u0902\u0938\u094d\u0925\u093e\u092a\u0915 \u0915\u0940 \u0915\u0939\u093e\u0928\u0940',
fdrH2:'\u090f\u0915 \u0910\u0938\u093e \u092a\u093e\u0928\u0940 \u092c\u094d\u0930\u093e\u0902\u0921 \u091c\u094b \u0905\u092a\u0928\u0947 \u0932\u0947\u092c\u0932 \u0915\u094b \u0938\u093e\u0930\u094d\u0925\u0915 \u0915\u0930\u0947',
fdrP1:'\u0938\u094c\u0930\u092d \u0915\u0947. \u0917\u094b\u0902\u0926\u093f\u092f\u093e \u091c\u093f\u0932\u0947 \u0915\u0947 \u0905\u092e\u0917\u093e\u0901\u0935 \u0938\u0947 \u0939\u0948\u0902\u0964 \u092a\u093e\u0928\u0940 \u0915\u093e \u0927\u0902\u0927\u093e \u0935\u093f\u0930\u093e\u0938\u0924 \u092e\u0947\u0902 \u0928\u0939\u0940\u0902 \u092e\u093f\u0932\u093e \u2014 \u091d\u0930\u0928\u0947 \u0938\u0947 \u092c\u0949\u091f\u0932\u093f\u0902\u0917 \u0924\u0915, BIS \u0905\u0928\u0941\u092a\u093e\u0932\u0928 \u0938\u0947 \u0935\u093f\u0924\u0930\u0923 \u0924\u0915 \u2014 \u0939\u0930 \u0915\u0921\u093c\u0940 \u0916\u0941\u0926 \u0938\u0940\u0916\u0940\u0964',
fdrP2:'\u0909\u0928\u0915\u0947 \u0915\u094d\u0937\u0947\u0924\u094d\u0930 \u0915\u094b \u0930\u093e\u0937\u094d\u091f\u094d\u0930\u0940\u092f \u092c\u094d\u0930\u093e\u0902\u0921\u094d\u0938 \u091c\u0948\u0938\u0940 \u0917\u0941\u0923\u0935\u0924\u094d\u0924\u093e \u0915\u093e \u092a\u093e\u0928\u0940 \u091a\u093e\u0939\u093f\u090f \u0925\u093e, \u0928 \u0915\u093f \u0938\u093f\u0930\u094d\u092b\u093c \u090f\u0915 \u0914\u0930 \u092c\u094b\u0930\u0935\u0947\u0932 \u0911\u092a\u0930\u0947\u0936\u0928\u0964 \u092e\u093e\u092f\u093e \u0907\u0902\u091f\u0930\u0928\u0947\u0936\u0928\u0932 \u090f\u0915\u094d\u0938\u092a\u094b\u0930\u094d\u091f\u094d\u0938 \u0915\u0940 \u0938\u094d\u0925\u093e\u092a\u0928\u093e \u0915\u0930 \u0905\u092e\u0917\u093e\u0901\u0935 \u092e\u0947\u0902 \u092c\u0949\u091f\u0932\u093f\u0902\u0917 \u0932\u093e\u0907\u0928 \u0932\u0917\u093e\u0908 \u2014 \u092c\u093e\u091c\u093c\u093e\u0930 \u0915\u0947 \u092a\u093e\u0938 \u0928\u0939\u0940\u0902, \u0938\u094d\u0930\u094b\u0924 \u0915\u0947 \u092a\u093e\u0938\u0964',
fdrP3:'\u0939\u0930 \u092c\u0948\u091a \u0915\u093e \u092a\u0930\u0940\u0915\u094d\u0937\u0923, \u0939\u0930 \u0938\u094d\u0930\u094b\u0924 \u0915\u0940 \u0928\u093f\u0917\u0930\u093e\u0928\u0940, \u0939\u0930 \u0935\u093f\u091a\u0932\u0928 \u0915\u0940 \u091c\u093e\u0901\u091a\u0964 \u0932\u0915\u094d\u0937\u094d\u092f \u0938\u094d\u092a\u0937\u094d\u091f \u0939\u0948: \u0930\u093f\u0935\u0947\u0930\u093e \u0938\u094d\u092a\u094d\u0930\u093f\u0902\u0917\u094d\u0938 \u0915\u094b \u0935\u093f\u0926\u0930\u094d\u092d \u0914\u0930 \u092a\u0942\u0930\u0947 \u092e\u0939\u093e\u0930\u093e\u0937\u094d\u091f\u094d\u0930 \u0915\u093e \u092d\u0930\u094b\u0938\u0947\u092e\u0902\u0926 \u092c\u094d\u0930\u093e\u0902\u0921 \u092c\u0928\u093e\u0928\u093e\u0964 \u0938\u092c\u0938\u0947 \u0938\u0938\u094d\u0924\u093e \u0928\u0939\u0940\u0902, \u0938\u092c\u0938\u0947 \u0938\u093e\u092b\u093c\u0964',
fdrQuote:'\u201c[\u0938\u0902\u0938\u094d\u0925\u093e\u092a\u0915 \u0915\u093e \u0909\u0926\u094d\u0927\u0930\u0923 \u2014 \u092c\u093e\u0926 \u092e\u0947\u0902 \u091c\u094b\u0921\u093c\u093e \u091c\u093e\u090f\u0917\u093e]\u201d',fdrCite:'\u0938\u094c\u0930\u092d \u0915\u0947., \u0938\u0902\u0938\u094d\u0925\u093e\u092a\u0915',
factLabel:'\u0909\u0924\u094d\u092a\u093e\u0926\u0928',factH2:'\u0939\u092e\u093e\u0930\u093e \u0915\u093e\u0930\u0916\u093e\u0928\u093e',
factP:'\u091f\u093e\u0902\u0921\u093e, \u091c\u093f\u0932\u093e \u0917\u094b\u0902\u0926\u093f\u092f\u093e \u092e\u0947\u0902 \u0939\u092e\u093e\u0930\u0940 \u0938\u0941\u0935\u093f\u0927\u093e \u092a\u0942\u0930\u0940 \u0924\u0930\u0939 \u0938\u094d\u0935\u091a\u093e\u0932\u093f\u0924 \u092c\u0949\u091f\u0932\u093f\u0902\u0917 \u0932\u093e\u0907\u0928 \u091a\u0932\u093e\u0924\u0940 \u0939\u0948\u0964 \u092a\u093e\u0928\u0940 \u0915\u0947 \u0907\u0928\u091f\u0947\u0915 \u0938\u0947 \u0938\u0940\u0932 \u0924\u0915 \u0915\u094b\u0908 \u0939\u093e\u0925 \u0928\u0939\u0940\u0902 \u0932\u0917\u0924\u093e\u0964 BIS \u0914\u0930 ISO \u092e\u093e\u0928\u0915\u094b\u0902 \u0915\u0947 \u0905\u0928\u0941\u0938\u093e\u0930\u0964',
factStat:'\u092a\u094d\u0930\u0924\u093f \u092e\u093f\u0928\u091f 90 \u092c\u094b\u0924\u0932\u0947\u0902\u0964 \u092a\u094d\u0930\u0924\u093f \u092e\u093f\u0928\u091f 4\u20135 \u092c\u0949\u0915\u094d\u0938\u0964 \u092a\u0942\u0930\u094d\u0923 \u0938\u094d\u0935\u091a\u093e\u0932\u093f\u0924\u0964',
retLabel:'\u0930\u093f\u091f\u0947\u0932\u0930\u094d\u0938 \u0915\u0947 \u0932\u093f\u090f',retH2:'\u0905\u092a\u0928\u0940 \u0926\u0941\u0915\u093e\u0928 \u092e\u0947\u0902 \u0930\u093f\u0935\u0947\u0930\u093e \u0938\u094d\u092a\u094d\u0930\u093f\u0902\u0917\u094d\u0938 \u0930\u0916\u0947\u0902',
retP1:'\u0939\u092e \u092e\u0939\u093e\u0930\u093e\u0937\u094d\u091f\u094d\u0930 \u0914\u0930 \u0906\u0938\u092a\u093e\u0938 \u0915\u0947 \u0930\u093e\u091c\u094d\u092f\u094b\u0902 \u092e\u0947\u0902 \u0930\u093f\u091f\u0947\u0932 \u0928\u0947\u091f\u0935\u0930\u094d\u0915 \u092c\u0928\u093e \u0930\u0939\u0947 \u0939\u0948\u0902\u0964 \u0915\u093f\u0930\u093e\u0928\u093e, \u0938\u0941\u092a\u0930\u092e\u093e\u0930\u094d\u0915\u0947\u091f, \u0930\u0947\u0938\u094d\u0924\u0930\u093e\u0902, \u0939\u094b\u091f\u0932 \u2014 \u0939\u092e\u0938\u0947 \u091c\u0941\u0921\u093c\u093f\u090f\u0964',
retB1:'\u0932\u0949\u092f\u0932\u094d\u091f\u0940 \u0930\u093f\u0935\u0949\u0930\u094d\u0921 \u0915\u093e\u0930\u094d\u092f\u0915\u094d\u0930\u092e \u0914\u0930 \u0938\u0940\u0927\u093e \u092c\u094d\u0930\u093e\u0902\u0921 \u0938\u092a\u094b\u0930\u094d\u091f',
retB2:'\u092a\u0949\u0907\u0902\u091f-\u0911\u092b\u093c-\u0938\u0947\u0932 \u092e\u093e\u0930\u094d\u0915\u0947\u091f\u093f\u0902\u0917 \u0938\u093e\u092e\u0917\u094d\u0930\u0940 \u092e\u0941\u092b\u093c\u094d\u0924',
retB3:'\u0938\u092e\u0930\u094d\u092a\u093f\u0924 \u0915\u094d\u0937\u0947\u0924\u094d\u0930 \u0938\u092e\u0930\u094d\u0925\u0928 \u2014 \u0913\u0935\u0930\u0932\u0948\u092a \u0928\u0939\u0940\u0902',
retB4:'\u0938\u092d\u0940 \u092a\u094d\u0930\u094b\u0921\u0915\u094d\u091f\u094d\u0938 \u092a\u0930 \u0905\u091a\u094d\u091b\u093e \u0930\u093f\u091f\u0947\u0932\u0930 \u092e\u093e\u0930\u094d\u091c\u093f\u0928',
retQR:'<strong>QR \u0915\u094d\u0930\u0947\u0921\u093f\u091f \u092a\u094d\u0930\u0923\u093e\u0932\u0940:</strong> \u0939\u0930 \u092c\u0949\u0915\u094d\u0938 \u092a\u0930 QR \u0915\u094b\u0921 \u0938\u094d\u0915\u0948\u0928 \u0915\u0930\u0947\u0902 \u2014 1 \u092a\u0949\u0907\u0902\u091f \u092e\u093f\u0932\u0947\u0917\u093e\u0964 30 \u092a\u0949\u0907\u0902\u091f \u092a\u0930 1 \u092c\u0949\u0915\u094d\u0938 \u092e\u0941\u092b\u093c\u094d\u0924 (30 \u0926\u093f\u0928 \u092c\u093e\u0926 \u0930\u093f\u0921\u0940\u092e)\u0964 \u0921\u093f\u091c\u093f\u091f\u0932 \u091f\u094d\u0930\u0948\u0915\u093f\u0902\u0917 \u2014 \u0928 \u0915\u093e\u0917\u091c\u093c, \u0928 \u0935\u093f\u0935\u093e\u0926\u0964',
retCtaH:'\u0930\u093f\u0935\u0947\u0930\u093e \u0938\u094d\u092a\u094d\u0930\u093f\u0902\u0917\u094d\u0938 \u0930\u093f\u091f\u0947\u0932\u0930 \u092c\u0928\u0947\u0902',retCtaP:'\u0928\u0940\u091a\u0947 \u0938\u0902\u092a\u0930\u094d\u0915 \u092b\u0949\u0930\u094d\u092e \u092d\u0930\u0947\u0902 \u092f\u093e \u0938\u0940\u0927\u0947 \u0915\u0949\u0932 \u0915\u0930\u0947\u0902\u0964 48 \u0918\u0902\u091f\u0947 \u092e\u0947\u0902 \u0939\u092e\u093e\u0930\u0940 \u091f\u0940\u092e \u0938\u0902\u092a\u0930\u094d\u0915 \u0915\u0930\u0947\u0917\u0940\u0964',retCtaBtn:'\u0939\u092e\u093e\u0930\u0947 \u0938\u093e\u0925 \u091c\u0941\u0921\u093c\u0947\u0902',
distLabel:'\u0935\u093f\u0924\u0930\u0923 \u0928\u0947\u091f\u0935\u0930\u094d\u0915',distH2:'\u0939\u092e\u093e\u0930\u0947 \u0917\u094c\u0930\u0935\u0936\u093e\u0932\u0940 \u0935\u093f\u0924\u0930\u0915',
topBadge:'\u2b50 \u0936\u0940\u0930\u094d\u0937 \u0935\u093f\u0915\u094d\u0930\u0947\u0924\u093e',topName:'[\u0936\u0940\u0930\u094d\u0937 \u0935\u093f\u0924\u0930\u0915]',topRegion:'[\u0915\u094d\u0937\u0947\u0924\u094d\u0930]',
d1Name:'[\u0935\u093f\u0924\u0930\u0915 1]',d1City:'[\u0936\u0939\u0930]',d2Name:'[\u0935\u093f\u0924\u0930\u0915 2]',d2City:'[\u0936\u0939\u0930]',d3Name:'[\u0935\u093f\u0924\u0930\u0915 3]',d3City:'[\u0936\u0939\u0930]',d4Name:'[\u0935\u093f\u0924\u0930\u0915 4]',d4City:'[\u0936\u0939\u0930]',d5Name:'[\u0935\u093f\u0924\u0930\u0915 5]',d5City:'[\u0936\u0939\u0930]',d6Name:'[\u0935\u093f\u0924\u0930\u0915 6]',d6City:'[\u0936\u0939\u0930]',
conLabel:'\u0938\u0902\u092a\u0930\u094d\u0915 \u0915\u0930\u0947\u0902',conH2:'\u0939\u092e\u0947\u0902 \u0906\u092a\u0938\u0947 \u0938\u0941\u0928\u0928\u093e \u0905\u091a\u094d\u091b\u093e \u0932\u0917\u0947\u0917\u093e',
conCompL:'\u0915\u0902\u092a\u0928\u0940',conComp:'\u0930\u093f\u0935\u0947\u0930\u093e \u0938\u094d\u092a\u094d\u0930\u093f\u0902\u0917\u094d\u0938 (\u092e\u093e\u092f\u093e \u0907\u0902\u091f\u0930\u0928\u0947\u0936\u0928\u0932 \u090f\u0915\u094d\u0938\u092a\u094b\u0930\u094d\u091f\u094d\u0938 \u0915\u093e \u092c\u094d\u0930\u093e\u0902\u0921)',conAddrL:'\u092a\u0924\u093e',conAddr:'\u0917\u0948\u091f \u0928\u0902. 407/1/B \u091f\u093e\u0902\u0921\u093e, \u0924\u0939. \u0935 \u091c\u093f. \u0917\u094b\u0902\u0926\u093f\u092f\u093e, \u092e\u0939\u093e\u0930\u093e\u0937\u094d\u091f\u094d\u0930-441614',
conPhoneL:'\u092b\u093c\u094b\u0928',conPhone:'+91 98906 40603',conEmailL:'\u0908\u092e\u0947\u0932',conEmail:'mayainternationalexports06@gmail.com',
fName:'\u0928\u093e\u092e',fPhone:'\u092b\u093c\u094b\u0928',fMsg:'\u0938\u0902\u0926\u0947\u0936',fSubmit:'\u0938\u0902\u0926\u0947\u0936 \u092d\u0947\u091c\u0947\u0902',
footDesc:'\u0916\u0928\u093f\u091c \u092f\u0941\u0915\u094d\u0924 \u092a\u0948\u0915\u094d\u0921 \u092a\u0947\u092f\u091c\u0932, \u0905\u092e\u0917\u093e\u0901\u0935, \u092e\u0939\u093e\u0930\u093e\u0937\u094d\u091f\u094d\u0930 \u092e\u0947\u0902 \u092c\u094b\u0924\u0932\u092c\u0902\u0926\u0964 \u092e\u093e\u092f\u093e \u0907\u0902\u091f\u0930\u0928\u0947\u0936\u0928\u0932 \u090f\u0915\u094d\u0938\u092a\u094b\u0930\u094d\u091f\u094d\u0938 \u0915\u093e \u092c\u094d\u0930\u093e\u0902\u0921\u0964',
footOffice:'\u092a\u0902\u091c\u0940\u0915\u0943\u0924 \u0915\u093e\u0930\u094d\u092f\u093e\u0932\u092f',footLine1:'\u092e\u093e\u092f\u093e \u0907\u0902\u091f\u0930\u0928\u0947\u0936\u0928\u0932 \u090f\u0915\u094d\u0938\u092a\u094b\u0930\u094d\u091f\u094d\u0938',footLine2:'\u0917\u0948\u091f \u0928\u0902. 407/1/B \u091f\u093e\u0902\u0921\u093e',footLine3:'\u0924\u0939. \u0935 \u091c\u093f. \u0917\u094b\u0902\u0926\u093f\u092f\u093e, \u092e\u0939\u093e\u0930\u093e\u0937\u094d\u091f\u094d\u0930-441614',
footConH:'\u0938\u0902\u092a\u0930\u094d\u0915 \u0915\u0930\u0947\u0902',footTrade:'\u0935\u094d\u092f\u093e\u092a\u093e\u0930 \u092a\u0942\u091b\u0924\u093e\u091b',
footCopy:'&copy; 2024 \u0930\u093f\u0935\u0947\u0930\u093e \u0938\u094d\u092a\u094d\u0930\u093f\u0902\u0917\u094d\u0938\u0964 \u0938\u0930\u094d\u0935\u093e\u0927\u093f\u0915\u093e\u0930 \u0938\u0941\u0930\u0915\u094d\u0937\u093f\u0924\u0964',footPride:'\u0905\u092e\u0917\u093e\u0901\u0935, \u092e\u0939\u093e\u0930\u093e\u0937\u094d\u091f\u094d\u0930 \u092e\u0947\u0902 \u0917\u0930\u094d\u0935 \u0938\u0947 \u092c\u0928\u093e\u092f\u093e'
},

mr:{
skip:'\u092e\u0941\u0916\u094d\u092f \u092e\u091c\u0915\u0942\u0930\u093e\u0935\u0930 \u091c\u093e',
navSource:'\u0938\u094d\u0930\u094b\u0924',navRange:'\u0906\u092e\u091a\u0940 \u0930\u0947\u0902\u091c',navQuality:'\u0917\u0941\u0923\u0935\u0924\u094d\u0924\u093e',navFounder:'\u0938\u0902\u0938\u094d\u0925\u093e\u092a\u0915\u093e\u091a\u0940 \u0917\u094b\u0937\u094d\u091f',navFactory:'\u0915\u093e\u0930\u0916\u093e\u0928\u093e',navRetailers:'\u0930\u093f\u091f\u0947\u0932\u0930\u094d\u0938',navDistributors:'\u0935\u093f\u0924\u0930\u0915',navContact:'\u0938\u0902\u092a\u0930\u094d\u0915',
heroLabel:'\u092a\u0948\u0915\u094d\u0921 \u092a\u093f\u0923\u094d\u092f\u093e\u091a\u0947 \u092a\u093e\u0923\u0940 \u00b7 \u0916\u0928\u093f\u091c\u092f\u0941\u0915\u094d\u0924',
heroRivera:'\u0930\u093f\u0935\u094d\u0939\u0947\u0930\u093e',heroSprings:'\u0938\u094d\u092a\u094d\u0930\u093f\u0902\u0917\u094d\u0938',
heroWmTag:'\u0928\u093f\u0938\u0930\u094d\u0917\u093e\u0924\u0942\u0928 \u091c\u0928\u094d\u092e\u0932\u0947\u0932\u0947\u0964 \u0924\u0941\u092e\u091a\u094d\u092f\u093e\u0938\u093e\u0920\u0940 \u092c\u093e\u091f\u0932\u0940\u092c\u0902\u0926\u0964',
heroH1:'<em>\u092d\u093e\u0930\u0924\u093e\u091a\u094d\u092f\u093e \u0939\u0943\u0926\u092f\u093e\u0924\u0942\u0928</em> \u0936\u0941\u0926\u094d\u0927 \u092a\u093e\u0923\u0940\u0964',
heroCta:'\u0938\u094d\u0930\u094b\u0924 \u092a\u0939\u093e',
stat1Val:'7 \u091f\u092a\u094d\u092a\u0947',stat1Label:'\u092b\u093f\u0932\u094d\u091f\u094d\u0930\u0947\u0936\u0928',stat2Label:'\u092a\u094d\u0930\u0924\u093f \u0926\u0936\u0932\u0915\u094d\u0937',stat3Label:'BIS \u092a\u094d\u0930\u092e\u093e\u0923\u093f\u0924',
scrollCue:'\u0916\u093e\u0932\u0940 \u0938\u094d\u0915\u094d\u0930\u094b\u0932 \u0915\u0930\u093e',
srcLabel:'\u0938\u094d\u0930\u094b\u0924',
srcH2:'\u0938\u093e\u0924\u092a\u0941\u0921\u094d\u092f\u093e\u091a\u094d\u092f\u093e \u0927\u092c\u0927\u092c\u094d\u092f\u093e\u0902\u0924\u0942\u0928 \u0936\u0941\u0926\u094d\u0927 \u092a\u093e\u0923\u0940, \u092e\u094d\u092f\u0941\u0928\u093f\u0938\u093f\u092a\u0932 \u092c\u094b\u0930\u0935\u0947\u0932 \u0928\u093e\u0939\u0940',
srcP1:'\u0930\u093f\u0935\u094d\u0939\u0947\u0930\u093e \u0938\u094d\u092a\u094d\u0930\u093f\u0902\u0917\u094d\u0938\u091a\u0947 \u092a\u093e\u0923\u0940 <strong>\u0938\u093e\u0924\u092a\u0941\u0921\u094d\u092f\u093e\u091a\u094d\u092f\u093e \u092a\u093e\u092f\u0925\u094d\u092f\u093e\u091c\u0935\u0933\u091a\u094d\u092f\u093e</strong> \u0928\u0948\u0938\u0930\u094d\u0917\u093f\u0915 \u091d\u0930\u094d\u092f\u093e\u0902\u0924\u0942\u0928 \u092f\u0947\u0924\u0947 \u2014 \u092a\u0941\u0930\u093e\u0924\u0928 \u0916\u0921\u0915\u093e\u0902\u092e\u0927\u0942\u0928 \u0939\u091c\u093e\u0930\u094b \u0935\u0930\u094d\u0937\u0947 \u0917\u093e\u0933\u0942\u0928 \u0906\u0932\u0947\u0932\u0947 \u092a\u093e\u0923\u0940\u0964 <strong>\u092e\u0945\u0917\u094d\u0928\u0947\u0936\u093f\u092f\u092e, \u092a\u094b\u091f\u0945\u0936\u093f\u092f\u092e \u0906\u0923\u093f \u0938\u094b\u0921\u093f\u092f\u092e</strong> \u092f\u093e\u0902\u0928\u0940 \u092d\u0930\u092a\u0942\u0930\u0964',
srcP2:'\u0939\u0947 \u092e\u094d\u092f\u0941\u0928\u093f\u0938\u093f\u092a\u0932 \u092a\u093e\u0923\u0940 \u0928\u093e\u0939\u0940\u0964 \u0939\u0940 \u0928\u093f\u0938\u0930\u094d\u0917\u093e\u091a\u0940 \u0938\u094d\u0935\u0924:\u091a\u0940 \u0917\u093e\u0933\u0923\u0940 \u0906\u0939\u0947, \u0938\u094d\u0930\u094b\u0924\u093e\u0935\u0930\u091a \u092c\u093e\u091f\u0932\u0940\u092c\u0902\u0926\u0964 \u091d\u0930\u094d\u092f\u093e\u092a\u093e\u0938\u0942\u0928 \u092a\u094d\u0932\u093e\u0902\u091f\u092a\u0930\u094d\u092f\u0902\u0924 \u092c\u0902\u0926 \u092a\u093e\u0907\u092a\u0932\u093e\u0907\u0928 \u2014 \u091f\u0945\u0902\u0915\u0930 \u0928\u093e\u0939\u0940, \u0909\u0918\u0921\u094d\u092f\u093e \u0939\u0935\u0947\u0924 \u0920\u0947\u0935\u0923\u0947 \u0928\u093e\u0939\u0940\u0964',
jWaterfall:'\u0927\u092c\u0927\u092c\u093e',jSpring:'\u091d\u0930\u093e',jSandFilt:'\u0935\u093e\u0933\u0942 \u0917\u093e\u0933\u0923\u0940',jCarbFilt:'\u0915\u093e\u0930\u094d\u092c\u0928 \u0917\u093e\u0933\u0923\u0940',jUVOzone:'UV \u0906\u0923\u093f \u0913\u091d\u094b\u0928',jBottle:'\u092c\u093e\u091f\u0932\u0940\u092c\u0902\u0926',jYou:'\u0924\u0941\u092e\u094d\u0939\u0940',
statRegion:'\u092a\u094d\u0930\u0926\u0947\u0936',statRegionV:'\u0938\u093e\u0924\u092a\u0941\u0921\u093e \u0921\u094b\u0902\u0917\u0930',statType:'\u0938\u094d\u0930\u094b\u0924 \u092a\u094d\u0930\u0915\u093e\u0930',statTypeV:'\u0928\u0948\u0938\u0930\u094d\u0917\u093f\u0915 \u091d\u0930\u093e',
prodLabel:'\u0906\u092e\u091a\u0940 \u0930\u0947\u0902\u091c',
prodH2:'\u092a\u094d\u0930\u0924\u094d\u092f\u0947\u0915 \u092b\u0949\u0930\u094d\u092e\u0945\u091f,<br>\u090f\u0915\u091a \u0938\u094d\u0930\u094b\u0924<span class="gold-rule" style="margin-top:1rem"></span>',
prodDesc:'\u0938\u0930\u094d\u0935 \u092c\u093e\u091f\u0932\u094d\u092f\u093e \u090f\u0915\u093e\u091a \u091d\u0930\u094d\u092f\u093e\u091a\u094d\u092f\u093e \u092a\u093e\u0923\u094d\u092f\u093e\u0924\u0942\u0928 \u092f\u0947\u0924\u093e\u0924\u0964 \u092b\u0930\u0915 \u092b\u0915\u094d\u0924 \u092a\u0945\u0915\u091a\u093e\u0964',
p250name:'\u0915\u0949\u092e\u094d\u092a\u0945\u0915\u094d\u091f',p250use:'\u092b\u093f\u0930\u0924\u093e\u0928\u093e \u0938\u094b\u092c\u0924\u0964 \u092c\u0945\u0917\u092e\u0927\u094d\u092f\u0947 \u091f\u093e\u0915\u093e, \u0915\u093e\u0909\u0902\u091f\u0930\u0935\u0930 \u0920\u0947\u0935\u093e, \u0915\u093e\u0930\u094d\u092f\u0915\u094d\u0930\u092e\u093e\u0924 \u0935\u093e\u091f\u093e\u0964',
p500name:'\u0930\u094b\u091c\u091a\u0947',p500use:'\u0930\u094b\u091c\u091a\u0940 \u0917\u0930\u091c\u0964 \u0926\u0941\u0915\u093e\u0928, \u0939\u094b\u091f\u0947\u0932 \u0906\u0923\u093f \u0926\u0948\u0928\u0902\u0926\u093f\u0928 \u0935\u093e\u092a\u0930\u093e\u0938\u093e\u0920\u0940\u0964',
p1Lname:'\u0938\u094d\u091f\u0945\u0902\u0921\u0930\u094d\u0921',p1Luse:'\u0918\u0930 \u0906\u0923\u093f \u0911\u092b\u093f\u0938\u0938\u093e\u0920\u0940\u0964 \u0915\u0941\u091f\u0941\u0902\u092c\u093e\u0938\u094b\u092c\u0924 \u091c\u0947\u0935\u0923 \u0906\u0923\u093f \u0930\u094b\u091c\u091a\u093e \u0935\u093e\u092a\u0930\u0964',
qualLabel:'\u0917\u0941\u0923\u0935\u0924\u094d\u0924\u093e \u0906\u0923\u093f \u092a\u094d\u0930\u092e\u093e\u0923\u0928',
qualH2:'\u0938\u094d\u0930\u094b\u0924\u093e\u0935\u0930 \u0924\u092a\u093e\u0938\u0923\u0940, \u0932\u093e\u0907\u0928\u0935\u0930 \u0924\u092a\u093e\u0938\u0923\u0940, \u092a\u093e\u0920\u0935\u0923\u094d\u092f\u093e\u0906\u0927\u0940 \u0924\u092a\u093e\u0938\u0923\u0940',
qualIntro:'\u092a\u094d\u0930\u0924\u094d\u092f\u0947\u0915 \u092c\u0945\u091a\u091a\u0940 \u0924\u092a\u093e\u0938\u0923\u0940 \u0939\u094b\u0924\u0947 \u0906\u0923\u093f IS 14543:2016 \u091a\u094d\u092f\u093e \u092e\u093e\u0928\u0915\u093e\u0902\u0928\u0941\u0938\u093e\u0930 \u0924\u092a\u093e\u0938\u0932\u0947 \u091c\u093e\u0924\u0947\u0964',
qualSrcH:'\u0938\u094d\u0930\u094b\u0924',qualSrcP:'\u0938\u093e\u0924\u092a\u0941\u0921\u094d\u092f\u093e\u091a\u094d\u092f\u093e \u092a\u093e\u092f\u0925\u094d\u092f\u093e\u091c\u0935\u0933\u091a\u0947 \u0928\u0948\u0938\u0930\u094d\u0917\u093f\u0915 \u091d\u0930\u0947\u0964 TDS 50\u2013120 ppm\u0964 \u092e\u0945\u0917\u094d\u0928\u0947\u0936\u093f\u092f\u092e, \u092a\u094b\u091f\u0945\u0936\u093f\u092f\u092e, \u0938\u094b\u0921\u093f\u092f\u092e \u0906\u0923\u093f \u0915\u0945\u0932\u094d\u0936\u093f\u092f\u092e \u0928\u0948\u0938\u0930\u094d\u0917\u093f\u0915 \u092a\u094d\u0930\u092e\u093e\u0923\u093e\u0924\u0964',
qualProcH:'\u092a\u094d\u0930\u0915\u094d\u0930\u093f\u092f\u093e',qualProcP:'\u0935\u093e\u0933\u0942 \u0917\u093e\u0933\u0923\u0940, \u0915\u093e\u0930\u094d\u092c\u0928 \u0917\u093e\u0933\u0923\u0940, \u0930\u093f\u0935\u094d\u0939\u0930\u094d\u0938 \u0911\u0938\u094d\u092e\u094b\u0938\u093f\u0938, UV \u0906\u0923\u093f \u0913\u091d\u094b\u0928\u0947\u0936\u0928\u0964 \u091c\u094b\u0921\u0932\u0947\u0932\u0947 \u0916\u0928\u093f\u091c: \u092e\u0945\u0917\u094d\u0928\u0947\u0936\u093f\u092f\u092e, \u092a\u094b\u091f\u0945\u0936\u093f\u092f\u092e \u0906\u0923\u093f \u0938\u094b\u0921\u093f\u092f\u092e\u0964 \u0907\u0928\u091f\u0947\u0915\u092a\u093e\u0938\u0942\u0928 \u0938\u0940\u0932\u092a\u0930\u094d\u092f\u0902\u0924 \u092a\u0942\u0930\u094d\u0923 \u0938\u094d\u0935\u092f\u0902\u091a\u0932\u093f\u0924\u0964',
qualCertH:'\u092a\u094d\u0930\u092e\u093e\u0923\u0928',qualCertP:'FSSAI \u0932\u093e\u092f\u0938\u0928\u094d\u0938 (11526999000410)\u0964 IS 14543 \u0905\u0928\u0941\u092a\u093e\u0932\u0928\u0964 ISO 22000 \u0905\u0928\u094d\u0928 \u0938\u0941\u0930\u0915\u094d\u0937\u093e\u0964 BIS \u092a\u094d\u0930\u092e\u093e\u0923\u093f\u0924\u0964 \u0928\u093f\u0930\u094d\u092e\u093e\u0924\u093e: \u092e\u093e\u092f\u093e \u0907\u0902\u091f\u0930\u0928\u0945\u0936\u0928\u0932 \u090f\u0915\u094d\u0938\u092a\u094b\u0930\u094d\u091f\u094d\u0938, \u091f\u093e\u0902\u0921\u093e, \u0917\u094b\u0902\u0926\u093f\u092f\u093e\u0964',
certBIS:'BIS \u092a\u094d\u0930\u092e\u093e\u0923\u093f\u0924',certFSSAI:'FSSAI \u0932\u093e\u092f\u0938\u0928\u094d\u0938\u094d\u0921',
mineralCap:'\u0938\u093e\u092e\u093e\u0928\u094d\u092f \u0916\u0928\u093f\u091c \u0938\u0902\u0930\u091a\u0928\u093e (mg/L)',mineralParam:'\u092a\u0945\u0930\u093e\u092e\u0940\u091f\u0930',mineralVal:'\u092e\u0942\u0932\u094d\u092f',
mTDS:'\u090f\u0915\u0942\u0923 \u0935\u093f\u0930\u0918\u0933\u0923\u0936\u0940\u0932 \u0918\u0928 (TDS)',mCa:'\u0915\u0945\u0932\u094d\u0936\u093f\u092f\u092e (Ca\u00b2\u207a)',mMg:'\u092e\u0945\u0917\u094d\u0928\u0947\u0936\u093f\u092f\u092e (Mg\u00b2\u207a)',mK:'\u092a\u094b\u091f\u0945\u0936\u093f\u092f\u092e (K\u207a)',mNa:'\u0938\u094b\u0921\u093f\u092f\u092e (Na\u207a)',mCl:'\u0915\u094d\u0932\u094b\u0930\u093e\u0907\u0921 (Cl\u207b)',mSO4:'\u0938\u0932\u094d\u092b\u0947\u091f (SO\u2084\u00b2\u207b)',mF:'\u092b\u094d\u0932\u094b\u0930\u093e\u0907\u0921 (F\u207b)',mNO3:'\u0928\u093e\u092f\u091f\u094d\u0930\u0947\u091f (NO\u2083\u207b)',
fdrPhPh:'[\u0938\u0902\u0938\u094d\u0925\u093e\u092a\u0915\u093e\u091a\u093e \u092b\u094b\u091f\u094b \u2014 \u0938\u094c\u0930\u092d]',fdrName:'\u0938\u094c\u0930\u092d \u0915\u0947.',fdrTitle:'\u0938\u0902\u0938\u094d\u0925\u093e\u092a\u0915, \u0930\u093f\u0935\u094d\u0939\u0947\u0930\u093e \u0938\u094d\u092a\u094d\u0930\u093f\u0902\u0917\u094d\u0938',
fdrLabel:'\u0938\u0902\u0938\u094d\u0925\u093e\u092a\u0915\u093e\u091a\u0940 \u0917\u094b\u0937\u094d\u091f',
fdrH2:'\u0906\u092a\u0932\u094d\u092f\u093e \u0932\u0947\u092c\u0932\u0932\u093e \u0938\u093e\u0930\u094d\u0925\u0915 \u0920\u0930\u0935\u0923\u093e\u0930\u093e \u092a\u093e\u0923\u094d\u092f\u093e\u091a\u093e \u092c\u094d\u0930\u0901\u0921',
fdrP1:'\u0938\u094c\u0930\u092d \u0915\u0947. \u0917\u094b\u0902\u0926\u093f\u092f\u093e \u091c\u093f\u0932\u094d\u0939\u094d\u092f\u093e\u0924\u0932\u094d\u092f\u093e \u0905\u092e\u0917\u093e\u0935\u093e\u0924\u0932\u0947\u0964 \u092a\u093e\u0923\u094d\u092f\u093e\u091a\u093e \u0935\u094d\u092f\u0935\u0938\u093e\u092f \u0935\u093e\u0930\u0936\u093e\u0924 \u0928\u093e\u0939\u0940 \u2014 \u091d\u0930\u094d\u092f\u093e\u092a\u093e\u0938\u0942\u0928 \u092c\u093e\u091f\u0932\u0940\u092c\u0902\u0926\u092a\u0930\u094d\u092f\u0902\u0924, BIS \u0905\u0928\u0941\u092a\u093e\u0932\u0928\u093e\u092a\u093e\u0938\u0942\u0928 \u0935\u093f\u0924\u0930\u0923\u093e\u092a\u0930\u094d\u092f\u0902\u0924 \u2014 \u092a\u094d\u0930\u0924\u094d\u092f\u0947\u0915 \u0915\u0921\u0940 \u0938\u094d\u0935\u0924: \u0936\u093f\u0915\u0932\u0947\u0964',
fdrP2:'\u0924\u094d\u092f\u093e\u0902\u091a\u094d\u092f\u093e \u092d\u093e\u0917\u093e\u0932\u093e \u0930\u093e\u0937\u094d\u091f\u094d\u0930\u0940\u092f \u092c\u094d\u0930\u0901\u0921\u094d\u0938\u0938\u093e\u0930\u0916\u094d\u092f\u093e \u0926\u0930\u094d\u091c\u093e\u091a\u0947 \u092a\u093e\u0923\u0940 \u0939\u0935\u0947 \u0939\u094b\u0924\u0947, \u0906\u0923\u0916\u0940 \u090f\u0915 \u092c\u094b\u0930\u0935\u0947\u0932 \u0911\u092a\u0930\u0947\u0936\u0928 \u0928\u093e\u0939\u0940\u0964 \u092e\u093e\u092f\u093e \u0907\u0902\u091f\u0930\u0928\u0945\u0936\u0928\u0932 \u090f\u0915\u094d\u0938\u092a\u094b\u0930\u094d\u091f\u094d\u0938\u091a\u0940 \u0938\u094d\u0925\u093e\u092a\u0928\u093e \u0915\u0930\u0942\u0928 \u0905\u092e\u0917\u093e\u0935\u093e\u0924 \u092c\u093e\u091f\u0932\u0940\u092c\u0902\u0926 \u0932\u093e\u0907\u0928 \u0932\u093e\u0935\u0932\u0940 \u2014 \u092c\u093e\u091c\u093e\u0930\u093e\u091c\u0935\u0933 \u0928\u093e\u0939\u0940, \u0938\u094d\u0930\u094b\u0924\u093e\u091c\u0935\u0933\u0964',
fdrP3:'\u092a\u094d\u0930\u0924\u094d\u092f\u0947\u0915 \u092c\u0945\u091a\u091a\u0940 \u0924\u092a\u093e\u0938\u0923\u0940, \u092a\u094d\u0930\u0924\u094d\u092f\u0947\u0915 \u0938\u094d\u0930\u094b\u0924\u093e\u0935\u0930 \u0932\u0915\u094d\u0937, \u092a\u094d\u0930\u0924\u094d\u092f\u0947\u0915 \u0935\u093f\u091a\u0932\u0928\u093e\u091a\u0940 \u0924\u092a\u093e\u0938\u0923\u0940\u0964 \u0927\u094d\u092f\u0947\u092f \u0938\u094d\u092a\u0937\u094d\u091f: \u0930\u093f\u0935\u094d\u0939\u0947\u0930\u093e \u0938\u094d\u092a\u094d\u0930\u093f\u0902\u0917\u094d\u0938\u0932\u093e \u0935\u093f\u0926\u0930\u094d\u092d \u0906\u0923\u093f \u0938\u092e\u0938\u094d\u0924 \u092e\u0939\u093e\u0930\u093e\u0937\u094d\u091f\u094d\u0930\u093e\u091a\u093e \u0935\u093f\u0936\u094d\u0935\u093e\u0938\u0942 \u092c\u094d\u0930\u0901\u0921 \u092c\u0928\u0935\u0923\u0947\u0964 \u0938\u094d\u0935\u0938\u094d\u0924 \u0928\u093e\u0939\u0940, \u0938\u094d\u0935\u091a\u094d\u091b\u0964',
fdrQuote:'\u201c[\u0938\u0902\u0938\u094d\u0925\u093e\u092a\u0915\u093e\u091a\u0947 \u0935\u093f\u091a\u093e\u0930 \u2014 \u0928\u0902\u0924\u0930 \u091c\u094b\u0921\u0932\u0947 \u091c\u093e\u0924\u0940\u0932]\u201d',fdrCite:'\u0938\u094c\u0930\u092d \u0915\u0947., \u0938\u0902\u0938\u094d\u0925\u093e\u092a\u0915',
factLabel:'\u0909\u0924\u094d\u092a\u093e\u0926\u0928',factH2:'\u0906\u092e\u091a\u093e \u0915\u093e\u0930\u0916\u093e\u0928\u093e',
factP:'\u091f\u093e\u0902\u0921\u093e, \u091c\u093f. \u0917\u094b\u0902\u0926\u093f\u092f\u093e \u092f\u0947\u0925\u0947 \u0906\u092e\u091a\u0940 \u0938\u0941\u0935\u093f\u0927\u093e \u092a\u0942\u0930\u094d\u0923 \u0938\u094d\u0935\u092f\u0902\u091a\u0932\u093f\u0924 \u092c\u093e\u091f\u0932\u0940\u092c\u0902\u0926 \u0932\u093e\u0907\u0928 \u091a\u093e\u0932\u0935\u0924\u0947\u0964 \u092a\u093e\u0923\u094d\u092f\u093e\u091a\u094d\u092f\u093e \u0907\u0928\u091f\u0947\u0915\u092a\u093e\u0938\u0942\u0928 \u0938\u0940\u0932\u092a\u0930\u094d\u092f\u0902\u0924 \u0939\u093e\u0924 \u0932\u093e\u0917\u0924 \u0928\u093e\u0939\u0940\u0964 BIS \u0906\u0923\u093f ISO \u092e\u093e\u0928\u0915\u093e\u0902\u0928\u0941\u0938\u093e\u0930\u0964',
factStat:'\u092a\u094d\u0930\u0924\u093f \u092e\u093f\u0928\u093f\u091f 90 \u092c\u093e\u091f\u0932\u094d\u092f\u093e\u0964 \u092a\u094d\u0930\u0924\u093f \u092e\u093f\u0928\u093f\u091f 4\u20135 \u092c\u0949\u0915\u094d\u0938\u0964 \u092a\u0942\u0930\u094d\u0923 \u0938\u094d\u0935\u092f\u0902\u091a\u0932\u093f\u0924\u0964',
retLabel:'\u0930\u093f\u091f\u0947\u0932\u0930\u094d\u0938\u0938\u093e\u0920\u0940',retH2:'\u0924\u0941\u092e\u091a\u094d\u092f\u093e \u0926\u0941\u0915\u093e\u0928\u093e\u0924 \u0930\u093f\u0935\u094d\u0939\u0947\u0930\u093e \u0938\u094d\u092a\u094d\u0930\u093f\u0902\u0917\u094d\u0938 \u0920\u0947\u0935\u093e',
retP1:'\u0906\u092e\u094d\u0939\u0940 \u092e\u0939\u093e\u0930\u093e\u0937\u094d\u091f\u094d\u0930 \u0906\u0923\u093f \u0936\u0947\u091c\u093e\u0930\u091a\u094d\u092f\u093e \u0930\u093e\u091c\u094d\u092f\u093e\u0902\u092e\u0927\u094d\u092f\u0947 \u0930\u093f\u091f\u0947\u0932 \u0928\u0947\u091f\u0935\u0930\u094d\u0915 \u0924\u092f\u093e\u0930 \u0915\u0930\u0924 \u0906\u0939\u094b\u0924\u0964 \u0915\u093f\u0930\u093e\u0923\u093e, \u0938\u0941\u092a\u0930\u092e\u093e\u0930\u094d\u0915\u0947\u091f, \u0939\u094b\u091f\u0947\u0932, \u0930\u0947\u0938\u094d\u091f\u0949\u0930\u0902\u091f \u2014 \u0906\u092e\u094d\u0939\u093e\u0932\u093e \u0938\u0902\u092a\u0930\u094d\u0915 \u0915\u0930\u093e\u0964',
retB1:'\u0932\u0949\u092f\u0932\u094d\u091f\u0940 \u092c\u0915\u094d\u0937\u0940\u0938 \u0915\u093e\u0930\u094d\u092f\u0915\u094d\u0930\u092e \u0906\u0923\u093f \u0925\u0947\u091f \u092c\u094d\u0930\u0901\u0921 \u0938\u092a\u094b\u0930\u094d\u091f',
retB2:'\u092a\u0949\u0907\u0902\u091f-\u0911\u092b-\u0938\u0947\u0932 \u092e\u093e\u0930\u094d\u0915\u0947\u091f\u093f\u0902\u0917 \u0938\u093e\u0939\u093f\u0924\u094d\u092f \u092e\u094b\u092b\u0924',
retB3:'\u0938\u092e\u0930\u094d\u092a\u093f\u0924 \u0915\u094d\u0937\u0947\u0924\u094d\u0930 \u0938\u092e\u0930\u094d\u0925\u0928 \u2014 \u0913\u0935\u094d\u0939\u0930\u0932\u0945\u092a \u0928\u093e\u0939\u0940',
retB4:'\u0938\u0930\u094d\u0935 \u092a\u094d\u0930\u094b\u0921\u0915\u094d\u091f\u094d\u0938\u0935\u0930 \u091a\u093e\u0902\u0917\u0932\u0947 \u0930\u093f\u091f\u0947\u0932\u0930 \u092e\u093e\u0930\u094d\u091c\u093f\u0928',
retQR:'<strong>QR \u0915\u094d\u0930\u0947\u0921\u093f\u091f \u092a\u094d\u0930\u0923\u093e\u0932\u0940:</strong> \u092a\u094d\u0930\u0924\u094d\u092f\u0947\u0915 \u092c\u0949\u0915\u094d\u0938\u0935\u0930\u091a\u093e QR \u0915\u094b\u0921 \u0938\u094d\u0915\u0945\u0928 \u0915\u0930\u093e \u2014 1 \u092a\u0949\u0907\u0902\u091f \u092e\u093f\u0933\u0947\u0932\u0964 30 \u092a\u0949\u0907\u0902\u091f\u0935\u0930 1 \u092c\u0949\u0915\u094d\u0938 \u092e\u094b\u092b\u0924 (30 \u0926\u093f\u0935\u0938\u093e\u0902\u0928\u0902\u0924\u0930 \u0930\u093f\u0921\u0940\u092e)\u0964 \u0921\u093f\u091c\u093f\u091f\u0932 \u091f\u094d\u0930\u0945\u0915\u093f\u0902\u0917 \u2014 \u0915\u093e\u0917\u0926 \u0928\u093e\u0939\u0940, \u0935\u093e\u0926 \u0928\u093e\u0939\u0940\u0964',
retCtaH:'\u0930\u093f\u0935\u094d\u0939\u0947\u0930\u093e \u0938\u094d\u092a\u094d\u0930\u093f\u0902\u0917\u094d\u0938 \u0930\u093f\u091f\u0947\u0932\u0930 \u092c\u0928\u093e',retCtaP:'\u0916\u093e\u0932\u091a\u093e \u0938\u0902\u092a\u0930\u094d\u0915 \u092b\u0949\u0930\u094d\u092e \u092d\u0930\u093e \u0915\u093f\u0902\u0935\u093e \u0925\u0947\u091f \u0915\u0949\u0932 \u0915\u0930\u093e\u0964 48 \u0924\u093e\u0938\u093e\u0902\u0924 \u0906\u092e\u091a\u0940 \u091f\u0940\u092e \u0938\u0902\u092a\u0930\u094d\u0915 \u0915\u0930\u0947\u0932\u0964',retCtaBtn:'\u0906\u092e\u091a\u094d\u092f\u093e\u0938\u094b\u092c\u0924 \u092f\u093e',
distLabel:'\u0935\u093f\u0924\u0930\u0923 \u0928\u0947\u091f\u0935\u0930\u094d\u0915',distH2:'\u0906\u092e\u091a\u0947 \u0905\u092d\u093f\u092e\u093e\u0928\u0940 \u0935\u093f\u0924\u0930\u0915',
topBadge:'\u2b50 \u0936\u0940\u0930\u094d\u0937 \u0935\u093f\u0915\u094d\u0930\u0947\u0924\u093e',topName:'[\u0936\u0940\u0930\u094d\u0937 \u0935\u093f\u0924\u0930\u0915]',topRegion:'[\u092a\u094d\u0930\u0926\u0947\u0936]',
d1Name:'[\u0935\u093f\u0924\u0930\u0915 1]',d1City:'[\u0936\u0939\u0930]',d2Name:'[\u0935\u093f\u0924\u0930\u0915 2]',d2City:'[\u0936\u0939\u0930]',d3Name:'[\u0935\u093f\u0924\u0930\u0915 3]',d3City:'[\u0936\u0939\u0930]',d4Name:'[\u0935\u093f\u0924\u0930\u0915 4]',d4City:'[\u0936\u0939\u0930]',d5Name:'[\u0935\u093f\u0924\u0930\u0915 5]',d5City:'[\u0936\u0939\u0930]',d6Name:'[\u0935\u093f\u0924\u0930\u0915 6]',d6City:'[\u0936\u0939\u0930]',
conLabel:'\u0938\u0902\u092a\u0930\u094d\u0915 \u0915\u0930\u093e',conH2:'\u0906\u092e\u094d\u0939\u093e\u0932\u093e \u0924\u0941\u092e\u091a\u0947 \u0910\u0915\u093e\u092f\u0932\u093e \u0906\u0935\u0921\u0947\u0932',
conCompL:'\u0915\u0902\u092a\u0928\u0940',conComp:'\u0930\u093f\u0935\u094d\u0939\u0947\u0930\u093e \u0938\u094d\u092a\u094d\u0930\u093f\u0902\u0917\u094d\u0938 (\u092e\u093e\u092f\u093e \u0907\u0902\u091f\u0930\u0928\u0945\u0936\u0928\u0932 \u090f\u0915\u094d\u0938\u092a\u094b\u0930\u094d\u091f\u094d\u0938\u091a\u093e \u092c\u094d\u0930\u0901\u0921)',conAddrL:'\u092a\u0924\u094d\u0924\u093e',conAddr:'\u0917\u0945\u091f \u0928\u0902. 407/1/B \u091f\u093e\u0902\u0921\u093e, \u0924\u0939. \u0935 \u091c\u093f. \u0917\u094b\u0902\u0926\u093f\u092f\u093e, \u092e\u0939\u093e\u0930\u093e\u0937\u094d\u091f\u094d\u0930-441614',
conPhoneL:'\u092b\u094b\u0928',conPhone:'+91 98906 40603',conEmailL:'\u0908\u092e\u0947\u0932',conEmail:'mayainternationalexports06@gmail.com',
fName:'\u0928\u093e\u0935',fPhone:'\u092b\u094b\u0928',fMsg:'\u0938\u0902\u0926\u0947\u0936',fSubmit:'\u0938\u0902\u0926\u0947\u0936 \u092a\u093e\u0920\u0935\u093e',
footDesc:'\u0916\u0928\u093f\u091c\u092f\u0941\u0915\u094d\u0924 \u092a\u0948\u0915\u094d\u0921 \u092a\u093f\u0923\u094d\u092f\u093e\u091a\u0947 \u092a\u093e\u0923\u0940, \u0905\u092e\u0917\u093e\u0935 \u092e\u0939\u093e\u0930\u093e\u0937\u094d\u091f\u094d\u0930\u093e\u0924 \u0938\u094d\u0930\u094b\u0924\u093e\u0935\u0930 \u092c\u093e\u091f\u0932\u0940\u092c\u0902\u0926\u0964 \u092e\u093e\u092f\u093e \u0907\u0902\u091f\u0930\u0928\u0945\u0936\u0928\u0932 \u090f\u0915\u094d\u0938\u092a\u094b\u0930\u094d\u091f\u094d\u0938\u091a\u093e \u092c\u094d\u0930\u0901\u0921\u0964',
footOffice:'\u0928\u094b\u0902\u0926\u0923\u0940\u0915\u0943\u0924 \u0915\u093e\u0930\u094d\u092f\u093e\u0932\u092f',footLine1:'\u092e\u093e\u092f\u093e \u0907\u0902\u091f\u0930\u0928\u0945\u0936\u0928\u0932 \u090f\u0915\u094d\u0938\u092a\u094b\u0930\u094d\u091f\u094d\u0938',footLine2:'\u0917\u0945\u091f \u0928\u0902. 407/1/B \u091f\u093e\u0902\u0921\u093e',footLine3:'\u0924\u0939. \u0935 \u091c\u093f. \u0917\u094b\u0902\u0926\u093f\u092f\u093e, \u092e\u0939\u093e\u0930\u093e\u0937\u094d\u091f\u094d\u0930-441614',
footConH:'\u0938\u0902\u092a\u0930\u094d\u0915 \u0915\u0930\u093e',footTrade:'\u0935\u094d\u092f\u093e\u092a\u093e\u0930 \u091a\u094c\u0915\u0936\u0940',
footCopy:'&copy; 2024 \u0930\u093f\u0935\u094d\u0939\u0947\u0930\u093e \u0938\u094d\u092a\u094d\u0930\u093f\u0902\u0917\u094d\u0938\u0964 \u0938\u0930\u094d\u0935 \u0939\u0915\u094d\u0915 \u0930\u093e\u0916\u0940\u0935\u0964',footPride:'\u0905\u092e\u0917\u093e\u0935, \u092e\u0939\u093e\u0930\u093e\u0937\u094d\u091f\u094d\u0930\u093e\u0924 \u0905\u092d\u093f\u092e\u093e\u0928\u093e\u0928\u0947 \u092c\u0928\u0935\u0932\u0947\u0932\u0947'
}
};

  function setLang(lang){
    document.documentElement.lang=lang;
    if(lang==='hi'||lang==='mr'){document.body.style.fontFamily="var(--deva)"}else{document.body.style.fontFamily=""}
    var dict=T[lang]||T.en;
    document.querySelectorAll('[data-i18n]').forEach(function(el){
      var key=el.getAttribute('data-i18n');
      if(dict[key]!==undefined){
        if(el.hasAttribute('data-i18n-html')){el.innerHTML=dict[key]}
        else{el.textContent=dict[key]}
      }
    });
    document.querySelectorAll('.lang-btn').forEach(function(b){
      b.classList.toggle('active',b.getAttribute('data-lang')===lang);
    });
    try{localStorage.setItem('rs-lang',lang)}catch(e){}
  }
  document.querySelectorAll('.lang-btn').forEach(function(b){
    b.addEventListener('click',function(){setLang(this.getAttribute('data-lang'))});
  });
  var saved;try{saved=localStorage.getItem('rs-lang')}catch(e){}
  if(saved&&T[saved])setLang(saved);
'''

# ─── INJECT ───
# 1. CSS
css_marker = '/* ═══════════ SECTIONS PLACEHOLDER — chunks 3-4 add here ═══════════ */'
html = html.replace(css_marker, chunk3_css)

# 2. HTML sections
html_marker = '<!-- ═══════════ REMAINING SECTIONS — added by chunks 3-4 ═══════════ -->'
html = html.replace(html_marker, chunk3_html)

# 3. Replace </main> with footer
html = html.replace('\n</main>\n', footer_html, 1)

# 4. Insert i18n + contact JS before closing })();
html = html.replace('\n})();\n', i18n_js + '\n})();\n', 1)

with open('rivera-springs.html', 'w', encoding='utf-8') as f:
    f.write(html)

size = os.path.getsize('rivera-springs.html')
lines = html.count('\n') + 1
print(f'Written rivera-springs.html: {size:,} bytes ({size//1024} KB), {lines} lines')
