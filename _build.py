import importlib.util, os

spec = importlib.util.spec_from_file_location('b64', '_b64_data.py')
b64 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b64)

html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Rivera Springs — Born from Nature. Bottled for You.</title>
<meta name="description" content="Rivera Springs Pvt. Ltd. — Premium packaged drinking water with added minerals, sourced and bottled at origin in Amgaon, Maharashtra, India.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,700;0,6..96,900;1,6..96,400;1,6..96,700;1,6..96,900&family=Inter:wght@300;400;500;600;700&family=Noto+Sans+Devanagari:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
/* ═══════════ RESET & VARIABLES ═══════════ */
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}

:root{
  --teal:#0B4A3F;
  --dark:#08211F;
  --gold:#C9A227;
  --gold-hi:#F5D583;
  --mist:#E8F3EE;
  --bg:#FAFAF7;
  --text:#1A1A1A;
  --heading:#08211F;
  --serif:'Bodoni Moda','Georgia','Times New Roman',serif;
  --sans:'Inter',-apple-system,BlinkMacSystemFont,system-ui,sans-serif;
  --deva:'Noto Sans Devanagari','Inter',sans-serif;
  --max-w:1260px;
  --gutter:clamp(1.25rem,4vw,2.5rem);
  --section-pad:clamp(5rem,10vw,9rem);
}

html{scroll-behavior:smooth;font-size:16px}

@media(prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  *,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important;scroll-behavior:auto!important}
}

body{
  font-family:var(--sans);color:var(--text);line-height:1.72;
  background:var(--bg);-webkit-font-smoothing:antialiased;
  -moz-osx-font-smoothing:grayscale;overflow-x:hidden;
}
html[lang="hi"] body,html[lang="mr"] body{font-family:var(--deva)}

img{max-width:100%;display:block;height:auto}
a{color:inherit;text-decoration:none}
button{font-family:inherit;cursor:pointer;border:none;background:none}
ul,ol{list-style:none}

:focus-visible{outline:2.5px solid var(--gold);outline-offset:4px;border-radius:2px}

/* Skip link */
.skip{position:absolute;top:-100%;left:1rem;z-index:9999;background:var(--gold);color:var(--dark);padding:.75rem 1.5rem;font-weight:700;font-size:.85rem;letter-spacing:.08em;transition:top .2s}
.skip:focus{top:1rem}

/* Utility */
.container{width:100%;max-width:var(--max-w);margin:0 auto;padding:0 var(--gutter)}
.label{font-family:var(--sans);font-size:.7rem;letter-spacing:.22em;text-transform:uppercase;font-weight:600;color:var(--gold)}
.gold-rule{width:52px;height:2px;background:var(--gold);display:block}

/* Reveal animation */
.rv{opacity:0;transform:translateY(30px);transition:opacity .7s ease,transform .7s ease}
.rv.vis{opacity:1;transform:translateY(0)}
.rv-d1{transition-delay:.1s}.rv-d2{transition-delay:.2s}.rv-d3{transition-delay:.3s}
.rv-d4{transition-delay:.4s}.rv-d5{transition-delay:.5s}.rv-d6{transition-delay:.6s}

/* ═══════════ NAV ═══════════ */
.nav{
  position:fixed;top:0;left:0;right:0;z-index:100;
  padding:1.1rem 0;transition:background .45s,padding .35s,box-shadow .4s;
}
.nav.scrolled{
  background:rgba(8,33,31,.97);
  -webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px);
  padding:.55rem 0;box-shadow:0 2px 28px rgba(0,0,0,.3);
}
.nav-inner{
  display:flex;align-items:center;justify-content:space-between;
  max-width:var(--max-w);margin:0 auto;padding:0 var(--gutter);
}
.nav-brand{display:flex;align-items:center;gap:1rem}
.nav-logo{height:72px;width:auto;transition:height .3s;flex-shrink:0}
.nav.scrolled .nav-logo{height:52px}
.nav-wordmark{display:flex;flex-direction:column;line-height:1}
.nav-wordmark-rivera{font-family:var(--serif);font-weight:900;font-size:1.35rem;color:#fff;letter-spacing:.08em;text-transform:uppercase}
.nav-wordmark-springs{font-family:var(--serif);font-weight:400;font-style:italic;font-size:.85rem;color:var(--gold);letter-spacing:.06em}

.nav-right{display:flex;align-items:center;gap:1.5rem}
.nav-links{display:flex;gap:1.8rem}
.nav-links a{
  color:rgba(255,255,255,.72);font-size:.68rem;letter-spacing:.13em;
  text-transform:uppercase;font-weight:600;padding:.25rem 0;
  position:relative;transition:color .25s;white-space:nowrap;
}
.nav-links a::after{
  content:'';position:absolute;bottom:-3px;left:0;right:0;
  height:1.5px;background:var(--gold);transform:scaleX(0);
  transform-origin:right;transition:transform .3s ease;
}
.nav-links a:hover{color:#fff}
.nav-links a:hover::after{transform:scaleX(1);transform-origin:left}

.lang-sw{display:flex;gap:.3rem}
.lang-btn{
  background:rgba(255,255,255,.07);color:rgba(255,255,255,.5);
  font-size:.62rem;letter-spacing:.06em;font-weight:600;
  padding:.35rem .6rem;border:1px solid rgba(255,255,255,.1);
  transition:all .25s;border-radius:2px;
}
.lang-btn:hover{background:rgba(255,255,255,.14);color:#fff}
.lang-btn.active{background:var(--gold-hi);color:var(--dark);border-color:var(--gold-hi)}

/* Hamburger */
.nav-toggle{display:none;color:#fff;padding:.5rem;z-index:201;width:44px;height:44px;position:relative}
.nav-toggle .ham{display:block;width:22px;height:2px;background:#fff;position:absolute;left:11px;transition:all .35s cubic-bezier(.4,0,.2,1)}
.nav-toggle .ham:nth-child(1){top:14px}
.nav-toggle .ham:nth-child(2){top:21px}
.nav-toggle .ham:nth-child(3){top:28px}
.nav-toggle.open .ham:nth-child(1){top:21px;transform:rotate(45deg)}
.nav-toggle.open .ham:nth-child(2){opacity:0;transform:translateX(-8px)}
.nav-toggle.open .ham:nth-child(3){top:21px;transform:rotate(-45deg)}

.nav-overlay{position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:199;opacity:0;pointer-events:none;transition:opacity .35s}
.nav-overlay.open{opacity:1;pointer-events:auto}

@media(max-width:768px){
  .nav-logo{height:52px}
  .nav.scrolled .nav-logo{height:44px}
  .nav-wordmark{display:none}
  .nav-links{
    position:fixed;top:0;right:-100%;width:82vw;max-width:340px;
    height:100dvh;height:100vh;background:var(--dark);flex-direction:column;
    padding:6rem 2.5rem 2rem;gap:0;z-index:200;
    transition:right .4s cubic-bezier(.4,0,.2,1);
    box-shadow:-8px 0 40px rgba(0,0,0,.35);
    overflow-y:auto;
  }
  .nav-links.open{right:0}
  .nav-links a{
    font-size:.95rem;letter-spacing:.1em;padding:1rem 0;
    border-bottom:1px solid rgba(255,255,255,.06);
    opacity:0;transform:translateX(20px);
    transition:opacity .3s ease,transform .3s ease,color .25s;
  }
  .nav-links.open a{opacity:1;transform:translateX(0)}
  .nav-links.open a:nth-child(1){transition-delay:.05s}
  .nav-links.open a:nth-child(2){transition-delay:.1s}
  .nav-links.open a:nth-child(3){transition-delay:.15s}
  .nav-links.open a:nth-child(4){transition-delay:.2s}
  .nav-links.open a:nth-child(5){transition-delay:.25s}
  .nav-links.open a:nth-child(6){transition-delay:.3s}
  .nav-links.open a:nth-child(7){transition-delay:.35s}
  .nav-links.open a:nth-child(8){transition-delay:.4s}
  .nav-toggle{display:flex;align-items:center;justify-content:center}
  .lang-sw.desk{display:none}
  .mob-lang{display:flex!important;margin-top:auto;padding-top:1.5rem}
}
@media(min-width:769px){
  .mob-lang{display:none!important}
}

/* ═══════════ HERO ═══════════ */
.hero{
  position:relative;width:100%;
  height:100vh;height:100dvh;
  display:flex;align-items:center;
  overflow:hidden;background:var(--dark);
}
.hero-bg{
  position:absolute;inset:0;width:100%;height:120%;z-index:0;
  background:
    radial-gradient(ellipse 80% 60% at 25% 40%,rgba(11,74,63,.55) 0%,transparent 60%),
    radial-gradient(ellipse 60% 50% at 75% 60%,rgba(8,33,31,.6) 0%,transparent 50%),
    radial-gradient(circle at 50% 80%,rgba(11,74,63,.3) 0%,transparent 40%),
    linear-gradient(165deg,#0a3a30 0%,#08211F 30%,#0B4A3F 55%,#0a3a30 75%,#08211F 100%);
  animation:kenburns 28s ease-in-out infinite alternate;
}
@keyframes kenburns{from{transform:scale(1)}to{transform:scale(1.05)}}

.hero-overlay{
  position:absolute;inset:0;z-index:1;pointer-events:none;
  background:
    linear-gradient(180deg,rgba(8,33,31,.85) 0%,rgba(8,33,31,.2) 18%,transparent 30%),
    linear-gradient(0deg,rgba(8,33,31,.9) 0%,rgba(8,33,31,.25) 18%,transparent 32%),
    linear-gradient(90deg,rgba(8,33,31,.35) 0%,transparent 20%,transparent 80%,rgba(8,33,31,.35) 100%);
}

.hero-content{
  position:relative;z-index:2;width:100%;max-width:var(--max-w);
  margin:0 auto;padding:0 var(--gutter);
  display:grid;grid-template-columns:1fr auto 1fr;gap:clamp(2rem,4vw,4rem);
  align-items:center;
}

/* Hero left - headline + wordmark */
.hero-left{max-width:480px}
.hero-left .label{color:var(--gold);margin-bottom:1.25rem;display:flex;align-items:center;gap:.8rem}
.hero-left .label::before{content:'';width:32px;height:1px;background:var(--gold)}
.hero-left h1{
  font-family:var(--serif);font-weight:700;
  font-size:clamp(2.6rem,5.5vw,4.8rem);line-height:1.08;
  color:#fff;margin-bottom:1.5rem;
}
.hero-left h1 em{font-style:italic;color:var(--gold-hi)}

/* Hero wordmark - styled like bottle label */
.hero-wordmark{margin-bottom:2rem;display:flex;flex-direction:column;align-items:flex-start;gap:0}
.hero-wm-rule{width:100%;max-width:320px;height:1px;background:linear-gradient(90deg,var(--gold),rgba(201,162,39,.15))}
.hero-wm-rivera{
  font-family:var(--serif);font-weight:900;
  font-size:clamp(2.8rem,6vw,4.5rem);
  color:#fff;letter-spacing:.06em;text-transform:uppercase;
  line-height:1;margin:.15rem 0 -.1rem;
}
.hero-wm-springs{
  font-family:var(--serif);font-weight:400;font-style:italic;
  font-size:clamp(1.6rem,3.5vw,2.6rem);
  color:var(--gold);letter-spacing:.04em;
  line-height:1;margin-bottom:.15rem;
}
.hero-wm-tagline{
  font-family:var(--serif);font-style:italic;
  font-size:clamp(.8rem,1.4vw,1rem);
  color:rgba(255,255,255,.55);letter-spacing:.02em;margin-top:.3rem;
}

.hero-cta{
  display:inline-flex;align-items:center;gap:.8rem;
  background:var(--gold);color:var(--dark);
  padding:.95rem 2.2rem;font-size:.75rem;letter-spacing:.15em;
  text-transform:uppercase;font-weight:700;
  transition:background .25s,transform .2s,box-shadow .3s;
  box-shadow:0 4px 20px rgba(201,162,39,.25);
}
.hero-cta:hover{background:var(--gold-hi);transform:translateY(-2px);box-shadow:0 8px 32px rgba(201,162,39,.35)}
.hero-cta svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:2.5}

/* Hero center - bottle */
.hero-bottle{
  position:relative;display:flex;align-items:center;justify-content:center;
  width:clamp(160px,20vw,260px);perspective:800px;
}
.bottle-wrap{
  position:relative;transition:transform .15s ease-out;
  animation:bottleFloat 4s ease-in-out infinite;
}
@keyframes bottleFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-14px)}}
.bottle-wrap img{
  width:100%;height:auto;position:relative;z-index:2;
  filter:drop-shadow(0 20px 40px rgba(0,0,0,.4)) drop-shadow(0 4px 12px rgba(0,0,0,.2));
}
.bottle-glow{
  position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
  width:160%;height:160%;border-radius:50%;
  background:radial-gradient(circle,rgba(201,162,39,.2) 0%,rgba(201,162,39,.08) 35%,transparent 60%);
  z-index:1;animation:glowPulse 3s ease-in-out infinite;
}
@keyframes glowPulse{0%,100%{opacity:.7;transform:translate(-50%,-50%) scale(1)}50%{opacity:1;transform:translate(-50%,-50%) scale(1.08)}}
.bottle-sweep{
  position:absolute;top:0;left:-30%;width:40%;height:100%;z-index:3;
  background:linear-gradient(105deg,transparent 30%,rgba(255,255,255,.1) 48%,rgba(255,255,255,.18) 50%,rgba(255,255,255,.1) 52%,transparent 70%);
  animation:sweep 5s ease-in-out infinite;pointer-events:none;
}
@keyframes sweep{0%,100%{left:-30%;opacity:0}40%{opacity:1}60%{opacity:1}100%{left:130%;opacity:0}}
.ripple-ring{
  position:absolute;bottom:-20px;left:50%;transform:translateX(-50%);
  width:120px;height:24px;border-radius:50%;
  border:1px solid rgba(201,162,39,.15);
  animation:rippleExpand 3s ease-out infinite;z-index:0;
}
.ripple-ring:nth-child(4){animation-delay:.8s}
.ripple-ring:nth-child(5){animation-delay:1.6s}
@keyframes rippleExpand{0%{width:80px;height:16px;opacity:.4}100%{width:200px;height:40px;opacity:0}}

/* Hero right - stat cards */
.hero-stats{display:flex;flex-direction:column;gap:1rem;max-width:220px;justify-self:end}
.stat-card{
  background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);
  -webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);
  padding:1.1rem 1.4rem;transition:border-color .3s,transform .3s;
}
.stat-card:hover{border-color:rgba(201,162,39,.3);transform:translateX(-4px)}
.stat-val{font-family:var(--serif);font-size:1.6rem;font-weight:700;color:#fff;line-height:1.1;margin-bottom:.2rem}
.stat-label{font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.5);font-weight:600}

/* Hero bottom elements */
.hero-scroll{
  position:absolute;bottom:2.5rem;left:50%;transform:translateX(-50%);z-index:2;
  color:rgba(255,255,255,.35);font-size:.58rem;letter-spacing:.22em;text-transform:uppercase;text-align:center;
}
.hero-scroll::after{
  content:'';display:block;width:1px;height:40px;
  background:var(--gold);margin:.7rem auto 0;opacity:.4;
  animation:scrollPulse 2.2s ease-in-out infinite;
}
@keyframes scrollPulse{0%,100%{opacity:.15;transform:scaleY(.5)}50%{opacity:.5;transform:scaleY(1)}}

.hero-certs{
  position:absolute;bottom:3rem;right:var(--gutter);z-index:2;
  display:flex;gap:.6rem;
}
.hero-cert{
  font-size:.55rem;letter-spacing:.1em;text-transform:uppercase;font-weight:700;
  color:rgba(255,255,255,.3);padding:.4rem .7rem;
  border:1px solid rgba(255,255,255,.08);
}

@media(max-width:900px){
  .hero-content{grid-template-columns:1fr;gap:2rem;text-align:center;padding-top:7rem;padding-bottom:6rem}
  .hero-left{max-width:100%;margin:0 auto}
  .hero-left .label{justify-content:center}
  .hero-left h1{font-size:clamp(2.2rem,7vw,3.4rem)}
  .hero-wordmark{align-items:center}
  .hero-wm-rule{margin:0 auto}
  .hero-bottle{width:140px;margin:0 auto;order:-1}
  .hero-stats{flex-direction:row;max-width:100%;justify-self:center;gap:.6rem;flex-wrap:wrap;justify-content:center}
  .stat-card{padding:.8rem 1rem}
  .stat-val{font-size:1.2rem}
  .hero-certs{display:none}
}
@media(max-width:480px){
  .hero-left h1{font-size:clamp(1.9rem,7vw,2.8rem)}
  .hero-wm-rivera{font-size:2.2rem}
  .hero-wm-springs{font-size:1.3rem}
}

/* ═══════════ SECTIONS PLACEHOLDER — chunks 2-4 add here ═══════════ */

</style>
</head>
<body>

<a href="#main" class="skip" data-i18n="skip">Skip to main content</a>

<!-- NAV -->
<nav class="nav" id="siteNav" aria-label="Main navigation">
  <div class="nav-inner">
    <a href="#hero" class="nav-brand" aria-label="Rivera Springs home">
      <img src="''' + b64.logo_dark + '''" alt="Rivera Springs" class="nav-logo" loading="eager">
      <div class="nav-wordmark">
        <span class="nav-wordmark-rivera">RIVERA</span>
        <span class="nav-wordmark-springs">Springs</span>
      </div>
    </a>
    <div class="nav-right">
      <div class="nav-links" id="navLinks" role="menubar">
        <a href="#source" role="menuitem" data-i18n="navSource">The Source</a>
        <a href="#products" role="menuitem" data-i18n="navRange">Our Range</a>
        <a href="#quality" role="menuitem" data-i18n="navQuality">Quality</a>
        <a href="#founder" role="menuitem" data-i18n="navFounder">Founder&#8217;s Journey</a>
        <a href="#factory" role="menuitem" data-i18n="navFactory">Factory</a>
        <a href="#retailers" role="menuitem" data-i18n="navRetailers">Retailers</a>
        <a href="#distributors" role="menuitem" data-i18n="navDistributors">Distributors</a>
        <a href="#contact" role="menuitem" data-i18n="navContact">Contact</a>
        <div class="lang-sw mob-lang" role="group" aria-label="Language">
          <button class="lang-btn active" data-lang="en" aria-label="English">EN</button>
          <button class="lang-btn" data-lang="hi" aria-label="Hindi">\u0939\u093F\u0902</button>
          <button class="lang-btn" data-lang="mr" aria-label="Marathi">\u092E\u0930\u093E</button>
        </div>
      </div>
      <div class="lang-sw desk" role="group" aria-label="Language">
        <button class="lang-btn active" data-lang="en" aria-label="English">EN</button>
        <button class="lang-btn" data-lang="hi" aria-label="Hindi">\u0939\u093F\u0902</button>
        <button class="lang-btn" data-lang="mr" aria-label="Marathi">\u092E\u0930\u093E</button>
      </div>
      <button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="navLinks" aria-label="Toggle menu">
        <span class="ham"></span>
        <span class="ham"></span>
        <span class="ham"></span>
      </button>
    </div>
  </div>
  <div class="nav-overlay" id="navOverlay"></div>
</nav>

<!-- HERO -->
<section class="hero" id="hero" aria-label="Hero">
  <div class="hero-bg" id="heroBg" aria-hidden="true"></div>
  <div class="hero-overlay" aria-hidden="true"></div>
  <div class="hero-content">
    <div class="hero-left">
      <div class="label" data-i18n="heroLabel">Packaged Drinking Water &middot; Added Minerals</div>

      <div class="hero-wordmark">
        <div class="hero-wm-rule"></div>
        <span class="hero-wm-rivera" data-i18n="heroRivera">RIVERA</span>
        <span class="hero-wm-springs" data-i18n="heroSprings">Springs</span>
        <div class="hero-wm-rule"></div>
        <span class="hero-wm-tagline" data-i18n="heroWmTag">Born from Nature. Bottled for You.</span>
      </div>

      <h1 data-i18n="heroH1" data-i18n-html="true">Pure water from the <em>heart of India.</em></h1>

      <a href="#source" class="hero-cta" data-i18n="heroCta">
        Discover the Source
        <svg viewBox="0 0 24 24"><polyline points="7 10 12 15 17 10"/></svg>
      </a>
    </div>

    <div class="hero-bottle" id="heroBottle">
      <div class="bottle-wrap" id="bottleWrap">
        <div class="bottle-glow" aria-hidden="true"></div>
        <img src="''' + b64.bottle_1l + '''" alt="Rivera Springs 1 Litre bottle" width="476" height="1584" loading="eager">
        <div class="bottle-sweep" aria-hidden="true"></div>
      </div>
      <div class="ripple-ring" aria-hidden="true"></div>
      <div class="ripple-ring" aria-hidden="true"></div>
      <div class="ripple-ring" aria-hidden="true"></div>
    </div>

    <div class="hero-stats">
      <div class="stat-card">
        <div class="stat-val" data-i18n="stat1Val">7 Stage</div>
        <div class="stat-label" data-i18n="stat1Label">Filtration</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">TDS &lt;80</div>
        <div class="stat-label" data-i18n="stat2Label">Parts Per Million</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">100%</div>
        <div class="stat-label" data-i18n="stat3Label">BIS Certified</div>
      </div>
    </div>
  </div>

  <div class="hero-certs" aria-hidden="true">
    <span class="hero-cert">ISO 22000</span>
    <span class="hero-cert">BIS 14543</span>
    <span class="hero-cert">FSSAI</span>
  </div>
  <div class="hero-scroll" data-i18n="scrollCue">Scroll</div>
</section>

<main id="main">
<!-- ═══════════ REMAINING SECTIONS — added by chunks 2-4 ═══════════ -->
</main>

<script>
(function(){
  /* Nav toggle (hamburger) */
  var toggle=document.getElementById('navToggle'),
      links=document.getElementById('navLinks'),
      overlay=document.getElementById('navOverlay');

  function closeMenu(){
    links.classList.remove('open');
    overlay.classList.remove('open');
    toggle.classList.remove('open');
    toggle.setAttribute('aria-expanded','false');
    document.body.style.overflow='';
  }
  function openMenu(){
    links.classList.add('open');
    overlay.classList.add('open');
    toggle.classList.add('open');
    toggle.setAttribute('aria-expanded','true');
    document.body.style.overflow='hidden';
  }
  toggle.addEventListener('click',function(){
    if(links.classList.contains('open'))closeMenu();else openMenu();
  });
  overlay.addEventListener('click',closeMenu);
  links.querySelectorAll('a').forEach(function(a){a.addEventListener('click',closeMenu)});

  /* Sticky nav + back-to-top */
  var nav=document.getElementById('siteNav'),ticking=false;
  function onScroll(){
    if(!ticking){requestAnimationFrame(function(){
      nav.classList.toggle('scrolled',window.scrollY>60);
      var btt=document.getElementById('backTop');
      if(btt)btt.classList.toggle('vis',window.scrollY>window.innerHeight*.7);
      ticking=false;
    });ticking=true}
  }
  window.addEventListener('scroll',onScroll,{passive:true});onScroll();

  /* Parallax hero bg */
  var heroBg=document.getElementById('heroBg');
  var rm=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(!rm){
    var pt=false;
    window.addEventListener('scroll',function(){
      if(!pt){requestAnimationFrame(function(){
        var sy=window.scrollY,vh=window.innerHeight;
        if(sy<vh*1.5)heroBg.style.transform='translateY('+sy*0.3+'px) scale('+(1+sy*0.00003)+')';
        pt=false;
      });pt=true}
    },{passive:true});
  }

  /* Mouse tilt bottle */
  var bottle=document.getElementById('bottleWrap');
  if(bottle&&!rm){
    document.getElementById('hero').addEventListener('mousemove',function(e){
      var r=this.getBoundingClientRect();
      var cx=(e.clientX-r.left)/r.width-.5;
      var cy=(e.clientY-r.top)/r.height-.5;
      bottle.style.transform='rotateY('+cx*8+'deg) rotateX('+(-cy*6)+'deg) translateY('+(Math.sin(Date.now()/700)*6)+'px)';
    });
    document.getElementById('hero').addEventListener('mouseleave',function(){bottle.style.transform=''});
  }

  /* Scroll reveal */
  if(!rm){
    var reveals=document.querySelectorAll('.rv');
    var obs=new IntersectionObserver(function(entries){
      entries.forEach(function(e){if(e.isIntersecting){e.target.classList.add('vis');obs.unobserve(e.target)}});
    },{threshold:.12,rootMargin:'0px 0px -50px 0px'});
    reveals.forEach(function(el){obs.observe(el)});
  }else{document.querySelectorAll('.rv').forEach(function(el){el.classList.add('vis')})}

})();
</script>
</body>
</html>'''

with open('rivera-springs.html', 'w', encoding='utf-8') as f:
    f.write(html)

size = os.path.getsize('rivera-springs.html')
print(f'Written rivera-springs.html: {size:,} bytes ({size//1024} KB)')
print(f'Lines: {html.count(chr(10))+1}')
