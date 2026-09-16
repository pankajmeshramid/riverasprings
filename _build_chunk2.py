import importlib.util, os

spec = importlib.util.spec_from_file_location('b64', '_b64_data.py')
b64 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b64)

with open('rivera-springs.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ─── NEW CSS ───
chunk2_css = '''
/* ═══════════ SOURCE ═══════════ */
.source{background:var(--bg);padding:var(--section-pad) 0}
.source-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(3rem,6vw,6rem);align-items:start}
.source-text .label{display:block;margin-bottom:.5rem}
.source-text .gold-rule{margin-bottom:1.75rem}
.source-text h2{
  font-family:var(--serif);font-size:clamp(2rem,4vw,3rem);
  font-weight:700;color:var(--heading);line-height:1.1;
  margin-bottom:1.75rem;max-width:560px;
}
.source-text p{color:var(--text);font-size:.95rem;margin-bottom:1.3rem;max-width:540px;line-height:1.82}
.source-text p strong{color:var(--teal);font-weight:600}

.source-img{
  position:relative;aspect-ratio:3/4;overflow:hidden;
  background:linear-gradient(135deg,var(--teal) 0%,#0d6454 50%,var(--dark) 100%);
  box-shadow:0 20px 60px rgba(11,74,63,.12);
}
.source-img-ph{
  width:100%;height:100%;display:flex;align-items:center;justify-content:center;
  color:rgba(255,255,255,.3);font-size:.75rem;letter-spacing:.1em;text-transform:uppercase;font-weight:600;
}
.source-img::after{content:'';position:absolute;inset:0;border:1px solid rgba(201,162,39,.2);pointer-events:none}

/* Journey process line */
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
.journey-arrow{display:flex;align-items:center;padding-top:10px;color:var(--gold);opacity:.35;font-size:.7rem}

.source-stats{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:rgba(11,74,63,.08);margin-top:2.5rem}
.source-stat{background:var(--mist);padding:1.3rem 1.5rem}
.source-stat dt{font-size:.62rem;letter-spacing:.15em;text-transform:uppercase;color:var(--teal);font-weight:700;margin-bottom:.25rem;font-family:var(--sans)}
.source-stat dd{font-family:var(--serif);font-size:1.4rem;color:var(--heading);font-weight:700}

@media(max-width:820px){
  .source-grid{grid-template-columns:1fr}
  .source-img{max-width:420px;aspect-ratio:4/3}
}

/* ═══════════ PRODUCTS ═══════════ */
.products{background:#fff;padding:var(--section-pad) 0;overflow:hidden}
.products-header{
  display:flex;align-items:flex-end;justify-content:space-between;
  flex-wrap:wrap;gap:1.5rem;margin-bottom:clamp(2.5rem,5vw,4rem);
}
.products-header .left .label{display:block;margin-bottom:.5rem}
.products-header h2{
  font-family:var(--serif);font-size:clamp(2rem,4vw,3rem);
  font-weight:700;color:var(--heading);line-height:1.1;
}
.products-header h2 .gold-rule{margin-top:1rem}
.products-header .right{color:#666;font-size:.9rem;max-width:320px;text-align:right;line-height:1.7}

.product-scroll{
  display:flex;gap:2rem;overflow-x:auto;scroll-snap-type:x mandatory;
  -webkit-overflow-scrolling:touch;padding:1rem .5rem 2rem;cursor:grab;
  scroll-padding:0 1rem;
}
.product-scroll:active{cursor:grabbing}
.product-scroll::-webkit-scrollbar{height:4px}
.product-scroll::-webkit-scrollbar-track{background:rgba(11,74,63,.04)}
.product-scroll::-webkit-scrollbar-thumb{background:rgba(201,162,39,.3);border-radius:2px}
.product-card{
  min-width:300px;max-width:340px;flex-shrink:0;scroll-snap-align:start;
  background:var(--bg);border:1px solid rgba(11,74,63,.06);
  padding:2.5rem 2rem 2rem;
  transition:transform .35s,box-shadow .35s,border-color .3s;
  display:flex;flex-direction:column;align-items:center;text-align:center;
}
.product-card:hover{
  transform:translateY(-8px);
  box-shadow:0 20px 56px rgba(11,74,63,.1);
  border-color:rgba(201,162,39,.25);
}
.product-card-img{
  width:auto;height:300px;object-fit:contain;margin-bottom:1.75rem;
  filter:drop-shadow(0 8px 20px rgba(0,0,0,.08));
  transition:transform .4s ease;
}
.product-card:hover .product-card-img{transform:scale(1.04)}
.product-vol{font-family:var(--serif);font-size:2rem;font-weight:700;color:var(--heading);margin-bottom:.3rem}
.product-name{color:var(--gold);font-size:.68rem;letter-spacing:.16em;text-transform:uppercase;font-weight:700;margin-bottom:.6rem}
.product-use{color:#777;font-size:.88rem;line-height:1.6;max-width:260px}
.product-divider{width:32px;height:2px;background:var(--gold);opacity:.3;margin:1.2rem 0}

@media(max-width:480px){
  .product-card{min-width:260px;padding:2rem 1.5rem 1.5rem}
  .product-card-img{height:240px}
}

/* ═══════════ QUALITY ═══════════ */
.quality{background:var(--bg);padding:var(--section-pad) 0}
.quality-header{text-align:center;max-width:640px;margin:0 auto clamp(3rem,6vw,5rem)}
.quality-header .label{display:block;margin-bottom:.5rem}
.quality-header .gold-rule{margin:0 auto 1.75rem}
.quality-header h2{
  font-family:var(--serif);font-size:clamp(2rem,4vw,3rem);
  font-weight:700;color:var(--heading);line-height:1.1;margin-bottom:1rem;
}
.quality-header p{color:#666;font-size:.95rem;line-height:1.8}

.quality-cols{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(2rem,4vw,3.5rem)}
.quality-col{text-align:left}
.quality-icon{
  width:52px;height:52px;border-radius:50%;
  background:var(--mist);display:flex;align-items:center;justify-content:center;
  margin-bottom:1.5rem;border:2px solid var(--teal);
}
.quality-icon svg{width:22px;height:22px;stroke:var(--teal);fill:none;stroke-width:1.8}
.quality-col h3{
  font-family:var(--serif);font-size:1.3rem;font-weight:700;
  color:var(--heading);margin-bottom:.8rem;
}
.quality-col p{color:#666;font-size:.9rem;line-height:1.8}

.mineral-table{width:100%;max-width:700px;margin:clamp(3rem,6vw,5rem) auto 0;border-collapse:collapse;font-size:.88rem}
.mineral-table caption{text-align:left;font-size:.68rem;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);font-weight:700;padding-bottom:.85rem;font-family:var(--sans)}
.mineral-table thead th{text-align:left;font-weight:700;font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;color:var(--teal);padding:.7rem 0;border-bottom:2px solid var(--teal);font-family:var(--sans)}
.mineral-table thead th:last-child{text-align:right}
.mineral-table td{padding:.6rem 0;border-bottom:1px solid rgba(0,0,0,.05);color:var(--text)}
.mineral-table td:last-child{text-align:right;font-weight:700;color:var(--teal);font-variant-numeric:tabular-nums}

.cert-row{display:flex;gap:1rem;flex-wrap:wrap;margin-top:2.5rem;justify-content:center}
.cert-badge{
  display:flex;align-items:center;gap:.6rem;
  background:var(--mist);padding:.7rem 1.1rem;
  border:1px solid rgba(11,74,63,.1);font-size:.74rem;font-weight:600;color:var(--teal);
  transition:box-shadow .3s;
}
.cert-badge:hover{box-shadow:0 4px 16px rgba(11,74,63,.08)}
.cert-icon{
  width:32px;height:32px;border-radius:50%;border:2px solid var(--teal);
  display:flex;align-items:center;justify-content:center;
  font-family:var(--serif);font-size:.6rem;font-weight:700;color:var(--teal);flex-shrink:0;
}

@media(max-width:768px){
  .quality-cols{grid-template-columns:1fr}
  .quality-col{text-align:center}
  .quality-icon{margin:0 auto 1.5rem}
}

/* ═══════════ FOUNDER ═══════════ */
.founder{background:var(--dark);color:#fff;padding:var(--section-pad) 0;position:relative;overflow:hidden}
.founder::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent)}
.founder::after{content:'';position:absolute;bottom:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent)}
.founder-grid{display:grid;grid-template-columns:.42fr .58fr;gap:clamp(3rem,6vw,5rem);align-items:center}

.founder-portrait{
  position:relative;aspect-ratio:3/4;overflow:hidden;
  border:3px solid var(--gold);box-shadow:0 16px 48px rgba(0,0,0,.3);
}
.founder-portrait-ph{
  width:100%;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:.8rem;
  background:linear-gradient(135deg,var(--dark) 0%,#0d3a32 100%);
}
.founder-portrait-ph svg{opacity:.15}
.founder-portrait-ph span{color:rgba(255,255,255,.3);font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;font-weight:600}
.founder-portrait-label{
  position:absolute;bottom:0;left:0;right:0;
  background:linear-gradient(transparent,rgba(8,33,31,.92));
  padding:3rem 1.75rem 1.5rem;
}
.founder-portrait-label strong{display:block;font-family:var(--serif);font-size:1.15rem;margin-bottom:.15rem}
.founder-portrait-label span{font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);font-weight:600}

.founder-text .label{display:block;margin-bottom:.5rem}
.founder-text .gold-rule{margin-bottom:1.75rem}
.founder-text h2{
  font-family:var(--serif);font-size:clamp(1.8rem,3.5vw,2.6rem);
  font-weight:700;line-height:1.15;margin-bottom:1.75rem;
}
.founder-text p{color:rgba(255,255,255,.72);font-size:.93rem;margin-bottom:1.3rem;line-height:1.82}
.founder-quote{border-left:3px solid var(--gold);padding:1.5rem 0 1.5rem 1.75rem;margin:2rem 0}
.founder-quote blockquote{
  font-family:var(--serif);font-style:italic;
  font-size:clamp(1rem,1.8vw,1.2rem);color:var(--gold-hi);line-height:1.6;margin-bottom:.6rem;
}
.founder-quote cite{font-style:normal;font-size:.7rem;letter-spacing:.15em;text-transform:uppercase;color:var(--gold);font-weight:600}

@media(max-width:820px){
  .founder-grid{grid-template-columns:1fr;gap:2.5rem}
  .founder-portrait{max-width:340px;aspect-ratio:4/5;margin:0 auto}
}
'''

# ─── NEW HTML ───
chunk2_html = '''
<!-- SOURCE -->
<section class="source" id="source" aria-label="The Source">
  <div class="container">
    <div class="source-grid">
      <div class="source-text">
        <span class="label rv" data-i18n="srcLabel">The Source</span>
        <span class="gold-rule rv rv-d1"></span>
        <h2 class="rv rv-d1" data-i18n="srcH2">Pure water from Satpura&#8217;s pristine waterfalls, not a municipal borewell</h2>
        <p class="rv rv-d2" data-i18n="srcP1">Rivera Springs draws from the pure, untouched waterfalls and natural springs near the <strong>Satpura foothills</strong> \u2014 water naturally filtered through ancient rock formations over millennia. Rich in <strong>Magnesium, Potassium &amp; Sodium</strong>, this water carries the balanced mineral profile that only geological filtration can provide.</p>
        <p class="rv rv-d2" data-i18n="srcP2">This isn\u2019t treated municipal water or borewell supply dressed up with a label. This is nature\u2019s own filtration, bottled at the source. We pipe from spring to plant within a closed circuit \u2014 no tanker transport, no open-air holding. The bottling facility sits at the source, not hundreds of kilometres away in an industrial estate.</p>

        <div class="journey rv rv-d3" aria-label="Water purification journey">
          <div class="journey-track">
            <div class="journey-step">
              <div class="journey-icon"><svg viewBox="0 0 24 24"><path d="M12 2L2 22h20L12 2z"/><path d="M8 16c2-3 4-2 4-6"/><path d="M12 10c0 4 2 3 4 6"/></svg></div>
              <span class="journey-name" data-i18n="jWaterfall">Waterfall</span>
            </div>
            <span class="journey-arrow">\u203A</span>
            <div class="journey-step">
              <div class="journey-icon"><svg viewBox="0 0 24 24"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2z"/><path d="M8 12c0-2 1.5-4 4-4s4 2 4 4"/></svg></div>
              <span class="journey-name" data-i18n="jSpring">Spring</span>
            </div>
            <span class="journey-arrow">\u203A</span>
            <div class="journey-step">
              <div class="journey-icon"><svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="2"/><path d="M4 10h16"/><circle cx="8" cy="14" r="1"/><circle cx="12" cy="15" r=".8"/><circle cx="16" cy="13.5" r="1.2"/></svg></div>
              <span class="journey-name" data-i18n="jSandFilt">Sand Filtration</span>
            </div>
            <span class="journey-arrow">\u203A</span>
            <div class="journey-step">
              <div class="journey-icon"><svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="2"/><path d="M8 8v8M12 6v12M16 9v6"/></svg></div>
              <span class="journey-name" data-i18n="jCarbFilt">Carbon Filtration</span>
            </div>
            <span class="journey-arrow">\u203A</span>
            <div class="journey-step">
              <div class="journey-icon"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"/><path d="M8 12h8M12 8v8"/><path d="M6 6l2 2M16 6l-2 2M6 18l2-2M16 18l-2-2"/></svg></div>
              <span class="journey-name">RO</span>
            </div>
            <span class="journey-arrow">\u203A</span>
            <div class="journey-step">
              <div class="journey-icon"><svg viewBox="0 0 24 24"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/></svg></div>
              <span class="journey-name" data-i18n="jUVOzone">UV &amp; Ozone</span>
            </div>
            <span class="journey-arrow">\u203A</span>
            <div class="journey-step">
              <div class="journey-icon"><svg viewBox="0 0 24 24"><path d="M8 2h8v4l-2 2v6l2 2v4H8v-4l2-2V8L8 6V2z"/></svg></div>
              <span class="journey-name" data-i18n="jBottle">Bottling</span>
            </div>
            <span class="journey-arrow">\u203A</span>
            <div class="journey-step">
              <div class="journey-icon"><svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21v-1a7 7 0 0114 0v1"/></svg></div>
              <span class="journey-name" data-i18n="jYou">You</span>
            </div>
          </div>
        </div>

        <dl class="source-stats rv rv-d4">
          <div class="source-stat"><dt data-i18n="statRegion">Region</dt><dd data-i18n="statRegionV">Satpura Hills</dd></div>
          <div class="source-stat"><dt data-i18n="statType">Source Type</dt><dd data-i18n="statTypeV">Natural Spring</dd></div>
          <div class="source-stat"><dt>TDS</dt><dd>50\u2013120</dd></div>
          <div class="source-stat"><dt>pH</dt><dd>6.8\u20137.4</dd></div>
        </dl>
      </div>
      <div class="source-img rv rv-d2">
        <div class="source-img-ph" aria-label="Source image placeholder">[SOURCE IMAGE]</div>
      </div>
    </div>
  </div>
</section>

<!-- PRODUCTS -->
<section class="products" id="products" aria-label="Product Range">
  <div class="container">
    <div class="products-header">
      <div class="left">
        <span class="label rv" data-i18n="prodLabel">Our Range</span>
        <h2 class="rv rv-d1" data-i18n="prodH2" data-i18n-html="true">Every format,<br>one source<span class="gold-rule" style="margin-top:1rem"></span></h2>
      </div>
      <p class="right rv rv-d2" data-i18n="prodDesc">All bottles use the same spring source and undergo identical multi-stage purification. The only difference is the pack format.</p>
    </div>
    <div class="product-scroll" id="productScroll">
      <div class="product-card rv">
        <img class="product-card-img" src="''' + b64.bottle_250 + '''" alt="Rivera Springs 250ml bottle" loading="lazy" width="418" height="1310">
        <div class="product-vol">250 ml</div>
        <div class="product-name" data-i18n="p250name">Compact</div>
        <div class="product-divider"></div>
        <div class="product-use" data-i18n="p250use">Perfect for on-the-go. Toss it in your bag, keep one at the counter, hand it out at events.</div>
      </div>
      <div class="product-card rv rv-d1">
        <img class="product-card-img" src="''' + b64.bottle_500 + '''" alt="Rivera Springs 500ml bottle" loading="lazy" width="360" height="1234">
        <div class="product-vol">500 ml</div>
        <div class="product-name" data-i18n="p500name">Everyday</div>
        <div class="product-divider"></div>
        <div class="product-use" data-i18n="p500use">The everyday essential. For retail counters, restaurants, and daily hydration.</div>
      </div>
      <div class="product-card rv rv-d2">
        <img class="product-card-img" src="''' + b64.bottle_1l_card + '''" alt="Rivera Springs 1 Litre bottle" loading="lazy" width="476" height="1584">
        <div class="product-vol">1 Litre</div>
        <div class="product-name" data-i18n="p1Lname">Standard</div>
        <div class="product-divider"></div>
        <div class="product-use" data-i18n="p1Luse">For home &amp; office. Daily hydration, family dining, and general trade.</div>
      </div>
    </div>
  </div>
</section>

<!-- QUALITY -->
<section class="quality" id="quality" aria-label="Quality and Certification">
  <div class="container">
    <div class="quality-header rv">
      <span class="label" data-i18n="qualLabel">Quality &amp; Certification</span>
      <span class="gold-rule"></span>
      <h2 data-i18n="qualH2">Tested at source, tested at line, tested before dispatch</h2>
      <p data-i18n="qualIntro">Every production batch is sampled and tested against parameters mandated by IS 14543:2016. Records are maintained for FSSAI inspection on demand.</p>
    </div>

    <div class="quality-cols">
      <div class="quality-col rv">
        <div class="quality-icon">
          <svg viewBox="0 0 24 24"><path d="M12 2L2 22h20L12 2z"/><path d="M8 14l4-6 4 6"/></svg>
        </div>
        <h3 data-i18n="qualSrcH">Sourcing</h3>
        <p data-i18n="qualSrcP">Natural springs near the Satpura foothills. Water surfaces through ancient rock formations that impart a balanced mineral profile \u2014 Magnesium, Potassium, Sodium and Calcium in naturally occurring proportions. TDS maintained between 50\u2013120 ppm.</p>
      </div>
      <div class="quality-col rv rv-d1">
        <div class="quality-icon">
          <svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="2"/><line x1="4" y1="10" x2="20" y2="10"/><line x1="10" y1="4" x2="10" y2="20"/><line x1="14" y1="4" x2="14" y2="20"/></svg>
        </div>
        <h3 data-i18n="qualProcH">Processing</h3>
        <p data-i18n="qualProcP">Multi-stage treatment as printed on every label: Sand Filtration, Carbon Filtration, Reverse Osmosis, UV Treatment &amp; Ozonisation. Added minerals: Magnesium, Potassium &amp; Sodium. Fully automated bottling line \u2014 no manual handling from intake to sealed cap.</p>
      </div>
      <div class="quality-col rv rv-d2">
        <div class="quality-icon">
          <svg viewBox="0 0 24 24"><path d="M12 2l3 6h6l-5 4 2 7-6-4-6 4 2-7-5-4h6z"/></svg>
        </div>
        <h3 data-i18n="qualCertH">Certification</h3>
        <p data-i18n="qualCertP">FSSAI Licensed (Lic No: 11526999000410). IS 14543 compliant. ISO 22000 food safety management. BIS certification mark on every bottle. Manufactured &amp; marketed by Maya International Exports, Gat No. 407/1/B, Tanda, Tal &amp; Dist Gondia, Maharashtra 441614.</p>
      </div>
    </div>

    <div class="cert-row rv rv-d3">
      <div class="cert-badge"><div class="cert-icon">IS</div><span>IS 14543</span></div>
      <div class="cert-badge"><div class="cert-icon">ISO</div><span>ISO 22000</span></div>
      <div class="cert-badge"><div class="cert-icon">BIS</div><span data-i18n="certBIS">BIS Certified</span></div>
      <div class="cert-badge"><div class="cert-icon"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="var(--teal)" stroke-width="1.5"><path d="M2 7L5.5 10.5 12 3.5"/></svg></div><span data-i18n="certFSSAI">FSSAI Licensed</span></div>
    </div>

    <table class="mineral-table rv rv-d3" aria-label="Mineral composition">
      <caption data-i18n="mineralCap">Typical Mineral Composition (mg/L)</caption>
      <thead><tr><th data-i18n="mineralParam">Parameter</th><th data-i18n="mineralVal">Value</th></tr></thead>
      <tbody>
        <tr><td>pH</td><td>6.8 \u2013 7.4</td></tr>
        <tr><td data-i18n="mTDS">Total Dissolved Solids (TDS)</td><td>50 \u2013 120</td></tr>
        <tr><td data-i18n="mCa">Calcium (Ca\u00b2\u207a)</td><td>10 \u2013 25</td></tr>
        <tr><td data-i18n="mMg">Magnesium (Mg\u00b2\u207a)</td><td>5 \u2013 15</td></tr>
        <tr><td data-i18n="mK">Potassium (K\u207a)</td><td>1.0 \u2013 3.5</td></tr>
        <tr><td data-i18n="mNa">Sodium (Na\u207a)</td><td>8 \u2013 18</td></tr>
        <tr><td data-i18n="mCl">Chloride (Cl\u207b)</td><td>10 \u2013 25</td></tr>
        <tr><td data-i18n="mSO4">Sulphate (SO\u2084\u00b2\u207b)</td><td>5 \u2013 15</td></tr>
        <tr><td data-i18n="mF">Fluoride (F\u207b)</td><td>&lt; 0.5</td></tr>
        <tr><td data-i18n="mNO3">Nitrate (NO\u2083\u207b)</td><td>&lt; 2</td></tr>
      </tbody>
    </table>
  </div>
</section>

<!-- FOUNDER -->
<section class="founder" id="founder" aria-label="Founder&#8217;s Journey">
  <div class="container">
    <div class="founder-grid">
      <div class="founder-portrait rv">
        <div class="founder-portrait-ph">
          <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><circle cx="12" cy="8" r="4"/><path d="M4 21v-1a7 7 0 0114 0v1"/></svg>
          <span data-i18n="fdrPhPh">[FOUNDER PHOTO \u2014 Saurabh K]</span>
        </div>
        <div class="founder-portrait-label">
          <strong data-i18n="fdrName">Saurabh K</strong>
          <span data-i18n="fdrTitle">Founder, Rivera Springs</span>
        </div>
      </div>
      <div class="founder-text rv rv-d2">
        <span class="label" data-i18n="fdrLabel">Founder\u2019s Journey</span>
        <span class="gold-rule"></span>
        <h2 data-i18n="fdrH2">Building a water brand that earns the label it prints</h2>
        <p data-i18n="fdrP1">Saurabh K is a young man from Amgaon, a small town in eastern Maharashtra\u2019s Gondia district. Not born into the water business \u2014 he studied the industry from scratch, learning every link in the chain from natural springs to automated bottling, from BIS compliance paperwork to last-mile distribution logistics.</p>
        <p data-i18n="fdrP2">The founding moment came from a simple realisation: his region deserved spring-quality water at the standard of national brands, not just another borewell-and-RO operation printing \u201cmineral water\u201d on a label. He founded Maya International Exports and set up the Rivera Springs bottling line near Amgaon \u2014 deliberately close to the source rather than close to the market.</p>
        <p data-i18n="fdrP3">What drives him is an obsession with water quality that goes beyond mere compliance \u2014 every batch tested, every source monitored, every deviation investigated. The ambition is clear: making Rivera Springs the brand that Vidarbha and all of Maharashtra trusts. Not the cheapest option on the shelf, but the cleanest.</p>
        <div class="founder-quote">
          <blockquote data-i18n="fdrQuote">\u201c[FOUNDER QUOTE \u2014 will add later]\u201d</blockquote>
          <cite data-i18n="fdrCite">Saurabh K, Founder</cite>
        </div>
      </div>
    </div>
  </div>
</section>
'''

# ─── INJECT CSS ───
css_marker = '/* ═══════════ SECTIONS PLACEHOLDER — chunks 2-4 add here ═══════════ */'
html = html.replace(css_marker, chunk2_css + '\n' + css_marker.replace('chunks 2-4', 'chunks 3-4'))

# ─── INJECT HTML ───
html_marker = '<!-- ═══════════ REMAINING SECTIONS — added by chunks 2-4 ═══════════ -->'
html = html.replace(html_marker, chunk2_html + '\n<!-- ═══════════ REMAINING SECTIONS — added by chunks 3-4 ═══════════ -->')

# ─── ADD PRODUCT GALLERY DRAG JS ───
# Insert before the closing })(); of the IIFE
js_addition = '''
  /* Product gallery drag-to-scroll */
  var gal=document.getElementById('productScroll');
  if(gal){
    var isDown=false,startX,scrollL;
    gal.addEventListener('mousedown',function(e){isDown=true;gal.style.cursor='grabbing';startX=e.pageX-gal.offsetLeft;scrollL=gal.scrollLeft});
    gal.addEventListener('mouseleave',function(){isDown=false;gal.style.cursor=''});
    gal.addEventListener('mouseup',function(){isDown=false;gal.style.cursor=''});
    gal.addEventListener('mousemove',function(e){if(!isDown)return;e.preventDefault();gal.scrollLeft=scrollL-((e.pageX-gal.offsetLeft)-startX)*1.5});
  }
'''
html = html.replace('\n})();\n', js_addition + '\n})();\n')

with open('rivera-springs.html', 'w', encoding='utf-8') as f:
    f.write(html)

size = os.path.getsize('rivera-springs.html')
lines = html.count('\n') + 1
print(f'Written rivera-springs.html: {size:,} bytes ({size//1024} KB), {lines} lines')
