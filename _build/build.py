"""Generates the static pages of tutoring.hamraahadvisors.com (Hamraah Tutoring).

Run:  python3 _build/build.py   (from the repo root)
Edit content here, rebuild, commit the generated files.

_build/brand.css is a copy of the main site's styles.css (repo
Rashiasu/hamraah-website); tutoring-only styles live in _build/tutoring.css.
"""
import json, os, datetime, html

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SITE = "https://tutoring.hamraahadvisors.com"
MAIN_SITE = "https://www.hamraahadvisors.com"
BRAND = "Hamraah Tutoring"
LEGAL = "Hamraah Advisors (SMC-Private) Limited"
EMAIL = "info@hamraahadvisors.com"
WHATSAPP = "923354471262"
WHATSAPP_DISPLAY = "+92 335 4471262"
TODAY = datetime.date.today().isoformat()

NAV = [
    ("/", "Home"),
    ("/subjects", "Subjects"),
    ("/how-it-works", "How it works"),
    ("/tutors", "Tutors"),
    ("/pricing", "Pricing"),
    ("/safeguarding", "Safety"),
    ("/faq", "FAQ"),
]

# ---------------------------------------------------------------- data
ICONS = {
    "calc": '<path d="M6 2h12a2 2 0 0 1 2 2v16a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2zm1 3v4h10V5zm0 7v2h2v-2zm4 0v2h2v-2zm4 0v2h2v-2zm-8 4v2h2v-2zm4 0v2h2v-2zm4 0v2h2v-2z"/>',
    "book": '<path d="M4 3h7a3 3 0 0 1 1 .2A3 3 0 0 1 13 3h7v16h-7a2 2 0 0 0-1 .3 2 2 0 0 0-1-.3H4zm2 2v12h5l.5.1V5.5A1 1 0 0 0 11 5zm7 .5v11.6l.5-.1H18V5h-4.5a1 1 0 0 0-.5.5z"/>',
    "flask": '<path d="M9 2h6v2h-1v5.2l5.6 9.4A2 2 0 0 1 17.9 22H6.1a2 2 0 0 1-1.7-3.4L10 9.2V4H9zm3 9-2.9 5h5.8z"/>',
    "star": '<path d="M12 2l2.9 6.6 7.1.6-5.4 4.7 1.6 7L12 17.3 5.8 21l1.6-7L2 9.2l7.1-.6z"/>',
}

SUBJECTS = [  # slug, title, levels, intro, bullets
    ("maths", "Maths", "Grades 3 to 10",
     "From times tables and fractions to algebra, geometry and early trigonometry, taught step by step until it clicks.",
     ["Number sense, fractions and decimals", "Pre-algebra and Algebra 1 and 2", "Geometry and measurement",
      "Word problems and reasoning", "Homework help and test revision"]),
    ("english", "English", "Grades 3 to 10",
     "Confident reading, clear writing and strong grammar, matched to what your child is studying at school.",
     ["Reading comprehension and vocabulary", "Grammar, punctuation and spelling", "Essay and creative writing",
      "Book reports and literature", "Speaking and presentation skills"]),
    ("science", "Science", "Grades 3 to 10",
     "General science for younger children, then biology, chemistry and physics, explained with clear examples.",
     ["General and earth science", "Biology", "Chemistry", "Physics", "Lab report and project help"]),
    ("sat", "SAT prep", "Grades 9 to 12",
     "Focused preparation for the digital SAT, with practice tests, timing strategy and review of every mistake.",
     ["SAT Math", "SAT Reading and Writing", "Full practice tests with review", "Timing and test-day strategy",
      "A study plan up to your test date"]),
    ("gcse", "GCSE and IGCSE prep", "Years 9 to 11",
     "Exam preparation for GCSE and IGCSE students in the UK and international schools across Europe.",
     ["Maths (Foundation and Higher)", "English Language", "Biology, Chemistry and Physics",
      "Past papers and mark schemes", "AQA, Edexcel, OCR and Cambridge"]),
]

CURRICULA = [
    ("USA", "Common Core and state standards, grades 3 to 10, plus SAT."),
    ("UK", "National Curriculum Key Stage 2 to 4, GCSE and IGCSE."),
    ("Europe", "International schools: Cambridge, British curriculum and IB MYP."),
]

STEPS = [
    ("Book a free trial", "Tell us your child's grade, subject and the times that suit you. It takes two minutes on WhatsApp."),
    ("Meet your tutor", "A free 30-minute trial lesson online. The tutor finds out what your child knows and where they need help."),
    ("Get a learning plan", "After the trial you receive a short written plan with goals, a weekly schedule and the price."),
    ("Learn every week", "Regular one-to-one lessons at the same time each week, with notes after every lesson and a monthly progress report."),
]

TUTORS = [  # role, tags, icon, description
    ("Maths tutor", "Grades 3 to 10 · Algebra · Geometry", "calc",
     "Degree in mathematics or engineering and years of experience teaching school maths, including US and British curricula."),
    ("English tutor", "Reading · Writing · Grammar", "book",
     "Degree in English or education, fluent and clear spoken English, and experience with US and UK reading and writing standards."),
    ("Science tutor", "Biology · Chemistry · Physics", "flask",
     "Degree in a science subject and experience teaching Cambridge, O Level and international school science."),
    ("Exam prep tutor", "SAT · GCSE · IGCSE", "star",
     "High personal exam scores and experience preparing students for the SAT, GCSE and IGCSE with past papers."),
]

VETTING = [
    ("Identity check", "We verify every tutor's national ID (CNIC) and meet them on camera."),
    ("Police and reference checks", "Every tutor provides a police character certificate and two professional references."),
    ("Qualifications and subject test", "We check degrees and certificates, and tutors pass a subject knowledge test."),
    ("Demo lesson and training", "Tutors teach a demo lesson we observe, and complete our child safeguarding training."),
]

SAFETY = [
    ("Parents in control", "All bookings, messages and scheduling go through you, the parent. Tutors never contact your child privately."),
    ("Supervised online lessons", "Lessons run on Zoom or Google Meet links we create. You are always welcome to sit in."),
    ("Recorded for safety", "With your consent, lessons are recorded and kept for 30 days, so any concern can be reviewed, then deleted."),
    ("Minimal data", "We only ask for your child's first name, grade and school curriculum. We never share or sell family data."),
]

PLANS = [  # name, usd, eur, per, lede, items, featured
    ("Pay as you go", 22, 20, "per lesson", "Flexible lessons, no commitment.",
     ["60-minute one-to-one lesson", "Maths, English or Science", "Book when you need it", "Notes after every lesson"], False),
    ("Weekly", 80, 74, "per month", "One lesson a week. $20 a lesson.",
     ["4 lessons a month", "The same tutor every week", "Notes after every lesson", "Monthly progress report"], False),
    ("Twice weekly", 144, 132, "per month", "Two lessons a week. $18 a lesson.",
     ["8 lessons a month", "The same tutor every week", "Homework help between lessons", "Monthly progress report and parent call"], True),
    ("Exam prep", 200, 184, "per month", "SAT, GCSE or IGCSE. $25 a lesson.",
     ["8 lessons a month", "Specialist exam tutor", "Practice tests and past papers", "Study plan to your exam date"], False),
]

FAQS = [
    ("Who are the tutors?",
     "Qualified teachers and subject specialists based in Pakistan, with university degrees and years of teaching experience. Every tutor speaks fluent English and is trained in the curriculum your child follows."),
    ("Why tutors from Pakistan?",
     "Pakistan has a large pool of highly educated teachers who already teach British and international curricula. That lets us offer experienced one-to-one tutors at a fraction of local prices in the USA or Europe."),
    ("Will the lesson times suit us?",
     "Yes. Our tutors teach on your schedule: after school and at weekends in US Eastern, Central, Mountain and Pacific time, and in UK and European time. You choose the slot."),
    ("Is the free trial really free?",
     "Yes. The first 30-minute lesson is free, with no payment details needed. If it is not the right fit, you owe nothing."),
    ("How do online lessons work?",
     "Lessons happen live on Zoom or Google Meet with a shared digital whiteboard. Your child needs a laptop or tablet with a camera and a quiet place to learn."),
    ("How do you keep my child safe?",
     "Every tutor passes ID, police and reference checks and our safeguarding training. Parents arrange everything, lessons can be recorded with your consent, and you can sit in at any time. See our safety page for the full policy."),
    ("Which curriculum do you follow?",
     "Your child's. Tell us the school grade or year, the curriculum (for example Common Core, GCSE, IGCSE or IB MYP) and what they are studying in class, and the tutor follows it."),
    ("How do I pay?",
     "Prices are in US dollars or euros. After the free trial we confirm your plan and payment details in writing. Online card payment is coming soon."),
    ("Can I change tutor or cancel?",
     "Yes. You can ask for a different tutor at any time. Lessons can be rescheduled with 24 hours' notice, and monthly plans can be stopped before the next month starts."),
    ("Do you offer a sibling discount?",
     "Yes. Each additional child from the same family gets 10% off their plan."),
]

# ---------------------------------------------------------------- helpers
e = html.escape


def svg_icon(name):
    return f'<svg viewBox="0 0 24 24">{ICONS[name]}</svg>'


def section_head(eyebrow, title, sub=None, left=False):
    s = f'<div class="section-head{" left" if left else ""}"><p class="eyebrow">{eyebrow}</p><h2>{title}</h2><span class="rule"></span>'
    if sub:
        s += f'<p class="sub">{sub}</p>'
    return s + "</div>"


def section(inner, cls="", sid=None, pattern=False):
    idattr = f' id="{sid}"' if sid else ""
    pat = '<div class="pattern" aria-hidden="true"></div>' if pattern else ""
    return f'<section class="section {cls}"{idattr}>{pat}<div class="wrap">{inner}</div></section>'


def page_hero(eyebrow, title, lede, crumb):
    return f'''<section class="hero page-hero"><div class="pattern" aria-hidden="true"></div>
<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><span aria-current="page">{e(crumb)}</span></nav>
<p class="eyebrow">{eyebrow}</p><h1>{title}</h1><p class="lede">{lede}</p></div></section>'''


def cta_band(title="Give your child a tutor who really helps.", button="Book a free trial", href="/book"):
    return f'''<section class="band"><div class="pattern" aria-hidden="true"></div>
<div class="wrap band-inner"><h2>{title}</h2><a class="btn btn-gold" href="{href}">{button}</a></div></section>'''


def subjects_grid(detailed=True, link=False):
    out = []
    for i, (slug, title, levels, intro, bullets) in enumerate(SUBJECTS, 1):
        body = f'<p class="level">{e(levels)}</p>'
        body += f'<p class="svc-intro">{e(intro)}</p>'
        if detailed:
            body += "<ul>" + "".join(f"<li>{e(b)}</li>" for b in bullets) + "</ul>"
            body += f'<a class="more" href="/book?subject={e(title).replace(" ", "+")}">Book a free trial</a>'
        elif link:
            body += f'<a class="more" href="/subjects#{slug}">Learn more</a>'
        out.append(f'<article class="service" id="{slug}"><span class="idx">{i:02d}</span><h3>{e(title)}</h3>{body}</article>')
    # sixth tile: call to action, keeps the 3-column grid even
    out.append('<article class="service ask"><span class="idx">+</span><h3>Something else?</h3>'
               '<p class="svc-intro">Homework help across subjects, catching up after a move, or getting ahead before a new school year. Tell us what your child needs.</p>'
               f'<a class="more" href="https://wa.me/{WHATSAPP}" target="_blank" rel="noopener">Ask on WhatsApp</a></article>')
    return f'<div class="services three">{"".join(out)}</div>'


def curricula():
    return '<div class="curricula">' + "".join(
        f"<div><h3>{e(t)}</h3><p>{e(d)}</p></div>" for t, d in CURRICULA) + "</div>"


def steps():
    return '<ol class="steps">' + "".join(f"<li><h3>{e(a)}</h3><p>{e(b)}</p></li>" for a, b in STEPS) + "</ol>"


def tutors_grid(detailed=False):
    cards = []
    for name, tags, icon, desc in TUTORS:
        extra = f'<p class="desc">{e(desc)}</p>' if detailed else ""
        cards.append(
            f'<article class="expert"><div class="avatar" aria-hidden="true">{svg_icon(icon)}</div>'
            f'<h3>{e(name)}</h3><p class="tags">{e(tags)}</p>{extra}<p class="verified">Background checked</p>'
            f'<a class="btn btn-outline" href="/book">Book a free trial</a></article>')
    return f'<div class="experts">{"".join(cards)}</div>'


def plans_grid():
    cards = []
    for name, usd, eur, per, lede, items, featured in PLANS:
        badge = '<span class="badge">Most chosen</span>' if featured else ""
        btn = "btn-gold" if featured else "btn-outline"
        q = name.replace(" ", "+")
        cards.append(
            f'<article class="pkg{" featured" if featured else ""}">{badge}<h3>{name}</h3>'
            f'<p class="amount"><span class="cur">$</span>{usd}<span class="per">{per}</span></p>'
            f'<p class="eur">or €{eur} {per}</p>'
            f'<p class="pkg-lede">{e(lede)}</p><ul>{"".join(f"<li>{e(i)}</li>" for i in items)}</ul>'
            f'<a class="btn {btn}" href="/book?plan={q}">Start with a free trial</a></article>')
    return f'<div class="packages">{"".join(cards)}</div>'


def promises_grid(items):
    return '<div class="promises">' + "".join(
        f"<div><h3>{e(t)}</h3><p>{e(d)}</p></div>" for t, d in items) + "</div>"


def faq_list(items):
    return '<div class="faq">' + "".join(
        f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in items) + "</div>"


def compare():
    return '''<div class="compare">
  <div class="compare-col them"><p class="kicker">A typical tutoring app</p><ul>
    <li>A different tutor every time</li>
    <li>Short, rushed sessions</li>
    <li>Little feedback for parents</li>
    <li>Local prices of $50 to $80 an hour</li></ul></div>
  <div class="compare-col us"><p class="kicker">Hamraah Tutoring</p><ul>
    <li>The same vetted tutor every week</li>
    <li>Full 60-minute one-to-one lessons</li>
    <li>Notes after each lesson and a monthly report</li>
    <li>From $18 a lesson, with a free trial first</li></ul></div>
</div>'''


# ---------------------------------------------------------------- structured data
ORG = {
    "@type": "EducationalOrganization",
    "@id": SITE + "/#organization",
    "name": BRAND,
    "legalName": LEGAL,
    "url": SITE + "/",
    "parentOrganization": {"@type": "EducationalOrganization", "name": "Hamraah Advisors", "url": MAIN_SITE + "/"},
    "logo": SITE + "/assets/logo/hamraah-crest-full-colour.png",
    "image": SITE + "/assets/og-image.jpg",
    "email": EMAIL,
    "description": "Online one-to-one tutoring in Maths, English and Science for school students in the USA, UK and Europe, grades 3 to 10, plus SAT and GCSE preparation, with vetted tutors from Pakistan.",
    "areaServed": [{"@type": "Country", "name": "United States"}, {"@type": "Country", "name": "United Kingdom"},
                   {"@type": "Place", "name": "Europe"}],
    "knowsAbout": ["Online tutoring", "Maths tutoring", "English tutoring", "Science tutoring", "SAT preparation", "GCSE preparation"],
}
WEBSITE = {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": BRAND,
           "publisher": {"@id": SITE + "/#organization"}, "inLanguage": "en"}


def breadcrumbs(path, name):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": SITE + path}]}


def faq_schema(items):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def offers_schema():
    offers = []
    for name, usd, eur, per, lede, items, _ in PLANS:
        for price, cur in ((usd, "USD"), (eur, "EUR")):
            offers.append({"@type": "Offer", "name": f"{name} tutoring plan", "price": str(price), "priceCurrency": cur,
                           "url": SITE + "/pricing", "description": f"{lede} " + "; ".join(items)})
    offers.append({"@type": "Offer", "name": "Free trial lesson (30 minutes)", "price": "0", "priceCurrency": "USD",
                   "url": SITE + "/book"})
    return {"@type": "Service", "serviceType": "Online tutoring",
            "provider": {"@id": SITE + "/#organization"}, "areaServed": ["United States", "United Kingdom", "Europe"],
            "audience": {"@type": "EducationalAudience", "educationalRole": "student"},
            "offers": offers}


def courses_schema():
    return {"@type": "ItemList", "itemListElement": [
        {"@type": "ListItem", "position": i, "item": {
            "@type": "Course", "name": f"{title} online tutoring", "description": intro,
            "educationalLevel": levels, "provider": {"@id": SITE + "/#organization"}}}
        for i, (_, title, levels, intro, _) in enumerate(SUBJECTS, 1)]}


# ---------------------------------------------------------------- layout
def layout(path, title, desc, body, schema=(), crumb=None):
    canonical = SITE + path
    nav = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == path else ""}>{label}</a>' for href, label in NAV)
    graph = [ORG, WEBSITE] + list(schema)
    if crumb:
        graph.append(breadcrumbs(path, crumb))
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    year = datetime.date.today().year
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(desc)}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="theme-color" content="#0F3D3A">
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="/assets/favicon-32.png" sizes="32x32" type="image/png">
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{BRAND}">
  <meta property="og:locale" content="en_US">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(desc)}">
  <meta property="og:image" content="{SITE}/assets/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Hamraah crest and logo">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{e(title)}">
  <meta name="twitter:description" content="{e(desc)}">
  <meta name="twitter:image" content="{SITE}/assets/og-image.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@400;500;600&family=Noto+Nastaliq+Urdu:wght@500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/styles.css">
  <script type="application/ld+json">
{ld}
  </script>
</head>
<body class="tutoring">
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header" id="top">
    <div class="wrap header-inner">
      <a class="brand" href="/" aria-label="Hamraah Tutoring home">
        <img class="brand-light" src="/assets/logo/hamraah-horizontal-full-colour.svg" alt="Hamraah" width="729" height="230">
        <img class="brand-dark" src="/assets/logo/hamraah-horizontal-reversed.svg" alt="" width="729" height="230" aria-hidden="true">
        <span class="sub-brand">Tutoring</span>
      </a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Open menu"><span></span><span></span><span></span></button>
      <nav class="nav" id="nav" aria-label="Main">{nav}<a class="btn btn-small" href="/book">Free trial</a></nav>
    </div>
  </header>
  <main id="main">
{body}
  </main>
  <footer class="site-footer">
    <div class="wrap footer-inner">
      <div class="footer-brand">
        <img src="/assets/logo/hamraah-horizontal-gold-foil.svg" alt="Hamraah" width="729" height="230">
        <p>Online tutoring for school students in the USA, UK and Europe</p>
      </div>
      <nav class="footer-nav" aria-label="Footer">{nav}<a href="/book">Book a free trial</a></nav>
      <div class="footer-contact">
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <a href="https://wa.me/{WHATSAPP}" target="_blank" rel="noopener">WhatsApp {WHATSAPP_DISPLAY}</a>
        <a href="{MAIN_SITE}/">Studying abroad? Visit Hamraah Advisors</a>
        <p class="urdu" lang="ur" dir="rtl">ہمراہ ۔ آپ کے ہر قدم کے ساتھ</p>
      </div>
    </div>
    <div class="wrap legal">
      <p>© {year} {LEGAL}. Hamraah Tutoring is a service of Hamraah Advisors. All rights reserved.</p>
      <p>Lessons support, and do not replace, your child's school. We do not guarantee specific grades or exam scores.</p>
    </div>
  </footer>
  <a class="wa-float" href="https://wa.me/{WHATSAPP}" target="_blank" rel="noopener" aria-label="Chat with Hamraah Tutoring on WhatsApp"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.3-.5 0-1 .2-3.3-.7a11.6 11.6 0 0 1-4.6-4c-.4-.5-1.1-1.6-1.1-3s.7-2 1-2.3a1 1 0 0 1 .8-.4h.6c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.4 0 .6l-.4.6-.4.5c-.1.1-.3.3-.1.6a8.7 8.7 0 0 0 4.3 3.8c.3.1.5.1.6-.1l.9-1.1c.2-.3.4-.2.6-.1l2 1c.3.1.5.2.5.3a2.4 2.4 0 0 1-.1 1.3z"/></svg></a>
  <script src="/main.js" defer></script>
</body>
</html>
'''


# ---------------------------------------------------------------- pages
PAGES = {}


def page(path, filename, title, desc, crumb=None, schema=(), priority="0.8"):
    def deco(fn):
        PAGES[filename] = (path, title, desc, fn, crumb, schema, priority)
        return fn
    return deco


@page("/", "index.html",
      "Online Maths, English & Science Tutors | Hamraah Tutoring",
      "One-to-one online tutoring for grades 3 to 10 in the USA, UK and Europe, plus SAT and GCSE prep. Vetted tutors, lessons in your time zone, free trial.",
      priority="1.0")
def home():
    hero = f'''<section class="hero"><div class="pattern" aria-hidden="true"></div>
<div class="wrap hero-inner"><div class="hero-copy">
<p class="eyebrow">Online tutoring · USA, UK &amp; Europe</p>
<h1>Expert tutors who help your child <em>truly understand</em></h1>
<p class="lede">One-to-one online lessons in <strong>Maths, English and Science for grades 3 to 10</strong>, plus SAT and GCSE preparation. Qualified, background-checked tutors who follow your child's school curriculum, at times that fit your family.</p>
<div class="hero-cta"><a class="btn btn-gold" href="/book">Book a free trial lesson</a><a class="btn btn-ghost" href="/pricing">See prices</a></div>
<ul class="hero-badges"><li>Free 30-minute trial</li><li>Same tutor every week</li><li>Background-checked</li><li>From $18 a lesson</li></ul>
</div><div class="hero-mark" aria-hidden="true"><img src="/assets/logo/hamraah-crest-gold-foil.svg" alt="" width="500" height="500"><p class="tagline">Hamraah · learning together</p></div></div></section>
<section class="strip" aria-label="Highlights"><div class="wrap strip-inner">
<div><span class="num">3–10</span><span class="lbl">School grades in Maths, English and Science</span></div>
<div><span class="num">1:1</span><span class="lbl">Live lessons on Zoom or Google Meet</span></div>
<div><span class="num">Your time</span><span class="lbl">After school and weekends, US and European time</span></div>
<div><span class="num">$0</span><span class="lbl">Your first 30-minute lesson is free</span></div>
</div></section>'''
    return "\n".join([
        hero,
        section(section_head("Subjects", "What your child can learn",
                             "Lessons follow your child's school curriculum, so what they learn with us helps in class the next day.")
                + subjects_grid(detailed=False, link=True), "dark", pattern=True),
        section(section_head("How it works", "From free trial to steady progress") + steps()
                + '<p class="center-link"><a href="/how-it-works">More about how it works</a></p>'),
        section(section_head("Why parents choose Hamraah", "Real teaching, <em>real progress</em>",
                             "Experienced tutors, a consistent weekly routine and clear updates for parents, at a price that makes regular lessons possible.")
                + compare(), "tint"),
        section(section_head("Your child's safety comes first", "Safe, supervised lessons",
                             "Every tutor is vetted, and parents stay in control of every lesson.")
                + promises_grid(SAFETY) + '<p class="center-link"><a href="/safeguarding">Read our safeguarding policy</a></p>', "dark", pattern=True),
        section(section_head("Pricing", "Simple monthly plans",
                             "Prices in US dollars or euros. Start with a free trial, then choose a plan.")
                + plans_grid() + '<p class="center-link"><a href="/pricing">See all pricing details</a></p>', "tint"),
        cta_band(),
    ])


@page("/subjects", "subjects.html",
      "Maths, English, Science, SAT & GCSE Tutoring | Hamraah",
      "Online tutoring in Maths, English and Science for grades 3 to 10, plus SAT and GCSE or IGCSE prep, matched to US, UK and European school curricula.",
      crumb="Subjects", schema=(courses_schema(),))
def subjects():
    return "\n".join([
        page_hero("Subjects", "Lessons matched to <em>your child's school</em>",
                  "Maths, English and Science for grades 3 to 10, and exam preparation for the SAT, GCSE and IGCSE.", "Subjects"),
        section(subjects_grid(detailed=True), "dark", pattern=True),
        section(section_head("Curricula", "We follow the curriculum your child studies") + curricula()),
        cta_band("Not sure where your child needs help?", "Book a free assessment lesson", "/book"),
    ])


@page("/how-it-works", "how-it-works.html",
      "How Online Tutoring Works | Hamraah Tutoring",
      "Book a free trial, meet your tutor, get a written learning plan and start weekly one-to-one lessons online, with progress reports for parents.",
      crumb="How it works")
def how():
    need = '''<div class="excl"><div><h3>What your child needs</h3><ul>
<li>A laptop or tablet with a camera and microphone</li><li>A stable internet connection</li><li>A quiet place to learn, ideally where you can see them</li><li>Their school books or homework, if they want help with it</li></ul></div>
<div><h3>What parents receive</h3><ul>
<li>A written learning plan after the free trial</li><li>Short notes after every lesson</li><li>A monthly progress report</li><li>A parent call whenever you want one</li></ul></div></div>'''
    zones = '''<div class="zones">
<div><p class="kicker">US East Coast</p><p class="t">4 pm to 8 pm</p><p>Weekdays after school, plus weekend mornings</p></div>
<div><p class="kicker">US Central to Pacific</p><p class="t">3 pm to 7 pm</p><p>Weekdays after school, plus weekend mornings</p></div>
<div><p class="kicker">UK and Europe</p><p class="t">4 pm to 9 pm</p><p>Weekdays after school, plus weekends all day</p></div>
</div><p class="center-note">Times shown in your local time. Our tutors in Pakistan work the hours that suit you.</p>'''
    return "\n".join([
        page_hero("How it works", "Simple for parents, <em>effective for children</em>",
                  "Four easy steps from your first message to steady progress, with you informed at every stage.", "How it works"),
        section(section_head("Getting started", "Four steps to steady progress") + steps()),
        section(section_head("Lesson times", "Lessons in your time zone") + zones, "tint"),
        section(need),
        cta_band("Ready to meet your tutor?", "Book a free trial", "/book"),
    ])


@page("/tutors", "tutors.html",
      "Qualified, Vetted Online Tutors | Hamraah Tutoring",
      "Meet our tutors: qualified Maths, English, Science and exam specialists from Pakistan, each ID, police and reference checked and trained in child safety.",
      crumb="Tutors")
def tutors():
    join = f'''<div class="join"><div><p class="eyebrow">For teachers in Pakistan</p><h2>Become a Hamraah tutor</h2><span class="rule"></span>
<p class="sub left">Are you a qualified teacher with fluent English and experience of US, British or international curricula? Teach students abroad from home, on a steady schedule.</p></div>
<a class="btn btn-maroon" href="mailto:{EMAIL}?subject=Become%20a%20Hamraah%20tutor">Apply to teach</a></div>'''
    return "\n".join([
        page_hero("Our tutors", "Experienced teachers, <em>carefully chosen</em>",
                  "Our tutors are qualified teachers and subject specialists in Pakistan, with fluent English and experience teaching US, British and international curricula.", "Tutors"),
        section(tutors_grid(detailed=True) + '<p class="center-note">Individual tutor profiles with photos, qualifications and parent reviews are coming soon.</p>'),
        section(section_head("How we choose tutors", "Every tutor is checked, <em>before they teach</em>",
                             "Only a small share of applicants become Hamraah tutors.") + promises_grid(VETTING), "dark", pattern=True),
        section(join),
    ])


@page("/pricing", "pricing.html",
      "Online Tutoring Prices from $18 a Lesson | Hamraah",
      "Clear prices in US dollars and euros: pay-as-you-go lessons at $22, monthly plans from $18 a lesson, SAT and GCSE prep at $25. Free trial lesson first.",
      crumb="Pricing", schema=(offers_schema(),))
def pricing():
    good = '''<div class="excl"><div><h3>Every plan includes</h3><ul>
<li>A free 30-minute trial lesson before you pay</li><li>60-minute live one-to-one lessons</li><li>Notes after every lesson</li><li>A dedicated tutor and a parent coordinator</li></ul></div>
<div><h3>Good to know</h3><ul>
<li>Prices are per child. Each extra child from the same family gets 10% off.</li>
<li>Reschedule any lesson for free with 24 hours' notice.</li>
<li>Monthly plans can be stopped before the next month starts.</li>
<li>Card payment online is coming soon. We confirm payment details in writing after the trial.</li></ul></div></div>'''
    pfaq = [f for f in FAQS if f[0] in ("Is the free trial really free?", "How do I pay?", "Can I change tutor or cancel?", "Do you offer a sibling discount?")]
    return "\n".join([
        page_hero("Pricing", "Quality tutoring at a <em>fair price</em>",
                  "Clear monthly plans in US dollars or euros, with no sign-up fee. Every family starts with a free trial lesson.", "Pricing"),
        section(section_head("Plans", "Choose the plan that fits") + plans_grid()),
        section(good, "tint"),
        section(section_head("Questions", "About payments") + faq_list(pfaq), "narrow-wrap"),
        cta_band(),
    ])


@page("/safeguarding", "safeguarding.html",
      "Child Safety & Safeguarding Policy | Hamraah Tutoring",
      "How Hamraah Tutoring keeps children safe online: vetted tutors, parent-led communication, supervised and recorded lessons, and minimal data collection.",
      crumb="Safety")
def safeguarding():
    rules = '''<div class="excl"><div><h3>Rules every tutor follows</h3><ul>
<li>Teach only on lesson links created by Hamraah</li>
<li>Never contact a child by phone, text, email or social media</li>
<li>Communicate only with the parent or through our coordinator</li>
<li>Keep cameras on, in a quiet, professional setting</li>
<li>Never ask a child for personal information or photos</li>
<li>Report any concern about a child's welfare to us the same day</li></ul></div>
<div><h3>What we ask of parents</h3><ul>
<li>Be at home during lessons, and sit in whenever you wish</li>
<li>Have your child learn in a shared space, not a closed bedroom</li>
<li>Join or open the lesson link from your own account</li>
<li>Tell us straight away if anything worries you</li></ul>
<p>Any parent, child or tutor can raise a concern at any time. We take every report seriously, act on it within 24 hours, and remove any tutor who breaks these rules.</p></div></div>'''
    data = '''<div class="dest"><div><h3>Lesson recordings</h3><p>With your consent, lessons are recorded so they can be reviewed if a question or concern ever comes up. Recordings are stored privately, are never shared, and are deleted after 30 days. You can opt out of recording at any time.</p></div>
<div><h3>Your family's data</h3><p>We ask only for what we need: your name and contact details, and your child's first name, grade and curriculum. We never sell or share family data, and we delete it on request when you stop lessons.</p></div></div>'''
    report = f'''<div class="join"><div><p class="eyebrow">Report a concern</p><h2>Worried about something?</h2><span class="rule"></span>
<p class="sub left">Contact us straight away by WhatsApp on {WHATSAPP_DISPLAY} or by email with the subject "Safeguarding". If a child is in immediate danger, call your local emergency number first (911 in the USA, 999 in the UK, 112 in Europe).</p></div>
<a class="btn btn-maroon" href="mailto:{EMAIL}?subject=Safeguarding%20concern">Report a concern</a></div>'''
    return "\n".join([
        page_hero("Safeguarding", "Your child's safety <em>comes first</em>",
                  "Online lessons should be as safe as a classroom. Here is exactly how we protect every child we teach.", "Safety"),
        section(section_head("Our approach", "Four layers of protection") + promises_grid(SAFETY)
                + '<div class="gap"></div>' + section_head("Tutor vetting", "Every tutor is checked before they teach") + promises_grid(VETTING), "dark", pattern=True),
        section(rules),
        section(section_head("Privacy", "Recordings and data") + data, "tint"),
        section(report),
    ])


@page("/faq", "faq.html",
      "Online Tutoring FAQ for Parents | Hamraah Tutoring",
      "Answers for parents in the USA, UK and Europe: who the tutors are, lesson times, the free trial, online safety, curricula, prices and payments.",
      crumb="FAQ", schema=(faq_schema(FAQS),))
def faq():
    return "\n".join([
        page_hero("FAQ", "Questions from <em>parents</em>",
                  "Straight answers about our tutors, lessons, safety and prices. Can't find yours? Message us on WhatsApp.", "FAQ"),
        section(faq_list(FAQS), "narrow-wrap"),
        cta_band("Still have a question?", "Ask us on WhatsApp", f"https://wa.me/{WHATSAPP}"),
    ])


@page("/book", "book.html",
      "Book a Free Trial Tutoring Lesson | Hamraah Tutoring",
      "Book a free 30-minute online trial lesson in Maths, English, Science, SAT or GCSE prep. Tell us your child's grade and the times that suit you.",
      crumb="Free trial", priority="0.9")
def book():
    subj_opts = "".join(f"<option>{e(t)}</option>" for _, t, *_ in SUBJECTS) + "<option>Not sure yet</option>"
    plan_opts = "<option>Decide after the trial</option>" + "".join(f"<option>{e(n)}</option>" for n, *_ in PLANS)
    grade_opts = "".join(f"<option>Grade {g}</option>" for g in range(3, 13))
    return "\n".join([
        page_hero("Free trial", "Book a free <em>trial lesson</em>",
                  "Tell us a little about your child. We reply within one working day to arrange a 30-minute trial lesson at a time that suits you.", "Free trial"),
        f'''<section class="section"><div class="wrap contact-grid">
<div>
<h2 class="h-small">What happens next</h2>
<ol class="next-steps"><li>Send your request on WhatsApp or by email.</li><li>We match a tutor and confirm the trial time in your time zone.</li><li>Your child meets the tutor online for 30 minutes, free.</li><li>You receive a learning plan and choose whether to continue.</li></ol>
<ul class="contact-list">
<li><span class="ico" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.3-.5 0-1 .2-3.3-.7a11.6 11.6 0 0 1-4.6-4c-.4-.5-1.1-1.6-1.1-3s.7-2 1-2.3a1 1 0 0 1 .8-.4h.6c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.4 0 .6l-.4.6-.4.5c-.1.1-.3.3-.1.6a8.7 8.7 0 0 0 4.3 3.8c.3.1.5.1.6-.1l.9-1.1c.2-.3.4-.2.6-.1l2 1c.3.1.5.2.5.3a2.4 2.4 0 0 1-.1 1.3z"/></svg></span><a href="https://wa.me/{WHATSAPP}" target="_blank" rel="noopener">WhatsApp {WHATSAPP_DISPLAY}</a></li>
<li><span class="ico" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4-8 5-8-5V6l8 5 8-5z"/></svg></span><a href="mailto:{EMAIL}">{EMAIL}</a></li>
</ul>
<p class="hours">For your child's privacy we only ask for their first name.</p>
</div>
<form class="form" id="book-form" novalidate>
<div class="row2"><label>Parent's name<input name="name" type="text" autocomplete="name" required></label>
<label>WhatsApp number<input name="phone" type="tel" autocomplete="tel" placeholder="+1 555 123 4567" required></label></div>
<div class="row2"><label>Email<input name="email" type="email" autocomplete="email" required></label>
<label>Country<select name="country"><option>USA</option><option>UK</option><option>Germany</option><option>France</option><option>Netherlands</option><option>Ireland</option><option>Italy</option><option>Spain</option><option>Other in Europe</option><option>Other</option></select></label></div>
<div class="row2"><label>Child's first name<input name="child" type="text" autocomplete="off"></label>
<label>School grade<select name="grade">{grade_opts}</select></label></div>
<div class="row2"><label>Subject<select name="subject">{subj_opts}</select></label>
<label>Plan you are interested in<select name="plan">{plan_opts}</select></label></div>
<label>Best days and times (your local time)<input name="times" type="text" placeholder="e.g. Mon and Wed after 4 pm, Saturday morning"></label>
<label>Anything we should know?<textarea name="message" rows="4" placeholder="Curriculum (Common Core, GCSE, IGCSE, IB), topics they find hard, upcoming tests..."></textarea></label>
<div class="form-actions"><button class="btn btn-maroon" type="submit" name="via" value="whatsapp">Send on WhatsApp</button>
<button class="btn btn-outline" type="submit" name="via" value="email">Send by email</button></div>
<p class="form-note" role="status" aria-live="polite">Your details are kept strictly confidential.</p>
</form></div></section>''',
    ])


# ---------------------------------------------------------------- build
def build_css():
    """styles.css = main-site brand styles (_build/brand.css) + tutoring.css."""
    base = open(os.path.join(HERE, "brand.css"), encoding="utf-8").read()
    extra = open(os.path.join(HERE, "tutoring.css"), encoding="utf-8").read()
    with open(os.path.join(ROOT, "styles.css"), "w", encoding="utf-8") as f:
        f.write("/* Generated by _build/build.py from brand.css + tutoring.css. Do not edit here. */\n")
        f.write(base + "\n\n" + extra)


def build():
    build_css()
    urls = []
    for filename, (path, title, desc, fn, crumb, schema, priority) in PAGES.items():
        out = layout(path, title, desc, fn(), schema, crumb)
        with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
            f.write(out)
        urls.append((path, priority))
        print("built", filename, f"title={len(title)}ch desc={len(desc)}ch")
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, pr in urls:
        sm.append(f"  <url><loc>{SITE}{path}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")


if __name__ == "__main__":
    build()
