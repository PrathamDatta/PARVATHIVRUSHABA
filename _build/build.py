#!/usr/bin/env python3
"""Static site generator for parvathivrushabha.com
Run:  python3 _build/build.py     (writes HTML, sitemap.xml, robots.txt, llms.txt into the project root)
All facts come from the company profile PDF. Edit content in this file, then rebuild."""
import json, os, html, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE = "https://www.parvathivrushabha.com"
TODAY = datetime.date.today().isoformat()
NAME = "Parvathi Vrushabha HR Solution LLP"
SHORT = "Parvathi Vrushabha HR Solution LLP"
TAG = "Strength in Service, Grace in Growth."
P1, P2 = "+91 70261 99239", "+91 73531 88999"
P1T, P2T = "+917026199239", "+917353188999"
E1, E2 = "info@parvathivrushabha.com", "hrd@parvathivrushabha.com"
ADDR_LINES = ["No. 112, Raju Layout Main Road, 3rd Cross,", "Opp. Devaraj Urs Road, Nagadevanahalli,", "Jnanabharathi Post, Bengaluru – 560056, Karnataka, India"]
ADDR_ONE = "No. 112, Raju Layout Main Road, 3rd Cross, Opp. Devaraj Urs Road, Nagadevanahalli, Jnanabharathi Post, Bengaluru – 560056, Karnataka, India"
MAPQ = "Raju Layout Main Road Nagadevanahalli Jnanabharathi Post Bengaluru 560056"

# ---------------------------------------------------------------- icons
ICONS = {
 "users": '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.5"/><path d="M17 14c2.5 0 4.5 2 4.5 4.5"/>',
 "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>',
 "cap": '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11.5V16c0 1.5 3 3 6 3s6-1.5 6-3v-4.5M22 9v6"/>',
 "building": '<rect x="4" y="3" width="16" height="18" rx="1.5"/><path d="M9 8h2M13 8h2M9 12h2M13 12h2M10 21v-4h4v4"/>',
 "rupee": '<path d="M7 5h10M7 9h10M7 5c5 0 7 1.5 7 4s-2 4-7 4l7 6"/>',
 "shield": '<path d="M12 3l7 3v5c0 4.5-3 8-7 10-4-2-7-5.5-7-10V6z"/><path d="M9 12l2 2 4-4"/>',
 "factory": '<path d="M3 21V10l6 4v-4l6 4V6h3v15z"/><path d="M7 17h2M12 17h2M17 17h1"/>',
 "cart": '<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.5 11h11L21 7H6"/>',
 "truck": '<path d="M2 6h11v10H2zM13 9h4l4 4v3h-8"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
 "medical": '<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M12 8v8M8 12h8"/>',
 "hotel": '<path d="M3 20V8M3 14h18v6M21 14v-2a3 3 0 0 0-3-3h-7v5"/><circle cx="7" cy="11" r="1.5"/>',
 "warehouse": '<path d="M3 10l9-6 9 6v10H3z"/><path d="M8 20v-6h8v6M8 17h8"/>',
 "store": '<path d="M4 9l1.5-5h13L20 9M4 9v11h16V9"/><path d="M4 9c0 2 3 2 4 0 1 2 3 2 4 0 1 2 3 2 4 0 1 2 4 2 4 0"/>',
 "gear": '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M5 19l2-2M17 7l2-2"/>',
 "phone": '<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2z"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 "pin": '<path d="M12 21s7-6 7-11a7 7 0 0 0-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>',
 "whatsapp": '<path d="M3 21l1.6-4.8A8.5 8.5 0 1 1 8 19.5z"/><path d="M9 9c0 3 3 6 6 6l1-1.5-2-1-1 .8c-1-.5-2-1.5-2.5-2.5l.8-1-1-2z"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "chevron": '<path d="M6 9l6 6 6-6"/>',
 "search": '<circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/>',
 "clipboard": '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4h6v3H9zM8.5 12h7M8.5 16h5"/>',
 "link": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
 "scale": '<path d="M12 4v16M6 20h12M5 7h14M5 7l-3 7a3.5 3 0 0 0 6 0zM19 7l-3 7a3.5 3 0 0 0 6 0z"/>',
 "lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
 "heart": '<path d="M12 21s-7-4.5-9-9.5C2 8 4 5 7 5c2 0 3.5 1 5 3 1.5-2 3-3 5-3 3 0 5 3 4 6.5-2 5-9 9.5-9 9.5z"/>',
 "leaf": '<path d="M5 19C5 10 10 5 20 4c0 10-5 15-14 15zM5 19l8-8"/>',
 "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
 "eye": '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
 "trend": '<path d="M3 17l6-6 4 4 8-8M15 7h6v6"/>',
 "book": '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2zM4 19V5M9 8h6"/>',
 "hardhat": '<path d="M3 17h18M5 17a7 7 0 0 1 14 0M12 6v5M8 8l1.5 3M16 8l-1.5 3"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "bucket": '<path d="M12 3v7M9 10h6l1 5H8zM7 15l-1 6h12l-1-6"/>',
 "file": '<path d="M6 3h8l4 4v14H6zM14 3v4h4M9 13h6M9 17h6"/>',
 "chart": '<path d="M4 20V4M4 20h16M8 16v-5M12 16V8M16 16v-3"/>',
 "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 "idcard": '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="11" r="2"/><path d="M6 16c0-1.5 1.5-2.5 3-2.5s3 1 3 2.5M14 10h4M14 14h3"/>',
 "userplus": '<circle cx="10" cy="8" r="3.5"/><path d="M3 20c0-3.5 3-6 7-6M18 8v6M15 11h6"/>',
 "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
 "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
}

def ic(n, cls=""):
    return f'<svg class="ic {cls}" aria-hidden="true" focusable="false"><use href="#i-{n}"/></svg>'

def sprite():
    s = "".join(f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICONS.items())
    return f'<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>{s}</defs></svg>'

def R(i=0, kind=""):
    return f' data-reveal="{kind}" style="--i:{i}"'

def esc(s): return html.escape(s, quote=True)

# ---------------------------------------------------------------- content
SERVICES = [
 dict(slug="campus-recruitment-placement", name="Campus Recruitment & Placement", icon="cap", tone="", short="Campus recruitment & placement",
      blurb="We help organizations connect with fresh talent from colleges and educational institutions through structured campus recruitment programs.",
      items=["Campus recruitment planning and coordination", "College partnerships and employer engagement", "Candidate screening and assessments", "On-campus, virtual and hybrid recruitment drives", "Interview coordination, selection and onboarding support"]),
 dict(slug="manpower-workforce-solutions", name="Specialized Manpower & Workforce Solutions", icon="users", tone="g", short="Manpower & workforce solutions",
      blurb="We provide reliable skilled, semi-skilled and unskilled manpower to support the operational requirements of different industries.",
      items=["Manufacturing and industrial workforce", "Retail, FMCG, logistics and supply chain", "Pharmaceutical / healthcare and hospitality", "Machine operators, technicians, production workers and helpers", "Drivers, housekeeping and office support staff"]),
 dict(slug="facility-management-housekeeping", name="Facility Management & Housekeeping", icon="building", tone="b", short="Facility management & housekeeping",
      blurb="We provide customized housekeeping and facility management solutions based on the specific requirements of our clients.",
      items=["Industrial and commercial housekeeping", "Office and facility maintenance support", "Skilled and unskilled workforce deployment", "Production and industrial support manpower", "Attendance and shift management coordination"]),
 dict(slug="payroll-hr-compliance", name="Payroll Management & HR Compliance", icon="rupee", tone="y", short="Payroll & HR compliance",
      blurb="We support organizations in managing HR operations, payroll activities and statutory compliance requirements.",
      items=["Payroll processing and salary administration", "Employee background verification and onboarding documentation", "HR outsourcing and HR audits", "EPF, ESI, Professional Tax and Labour Welfare Fund support", "Contract labour and factory compliance coordination", "Gratuity, bonus and employee benefits administration"]),
]
SV = {s["slug"]: s for s in SERVICES}

INDUSTRIES = [
 ("manufacturing", "Manufacturing & Engineering", "factory", "Production, machine operation, technical and helper manpower for plants and workshops.", ["Machine operators", "Technicians", "Production workers", "Helpers"], "manpower-workforce-solutions"),
 ("retail-fmcg", "Retail & FMCG", "store", "Flexible, dependable teams for stores, distribution and in-market operations.", ["Store support", "Sales support", "Distribution staff"], "manpower-workforce-solutions"),
 ("logistics-supply-chain", "Logistics & Supply Chain", "truck", "Drivers and operations support that keep goods moving on schedule.", ["Drivers", "Loaders", "Dispatch support"], "manpower-workforce-solutions"),
 ("pharma-healthcare", "Pharmaceutical / Healthcare", "medical", "Dependable support teams for hygiene-sensitive and regulated environments.", ["Production support", "Housekeeping", "Admin support"], "manpower-workforce-solutions"),
 ("hospitality", "Hospitality", "hotel", "Service and housekeeping teams for hotels, venues and guest-facing businesses.", ["Housekeeping", "Service staff", "Support staff"], "facility-management-housekeeping"),
 ("facility-management", "Facility Management", "bucket", "Housekeeping and maintenance workforce deployed to your premises, with shift coordination.", ["Housekeeping", "Maintenance support", "Supervisors"], "facility-management-housekeeping"),
 ("warehousing-distribution", "Warehousing & Distribution", "warehouse", "Shift-based warehouse teams for storage, handling and dispatch.", ["Warehouse helpers", "Loaders", "Shift teams"], "manpower-workforce-solutions"),
 ("commercial-establishments", "Commercial Establishments", "building", "Office support, administration and housekeeping for offices and commercial spaces.", ["Office support", "Housekeeping", "Admin staff"], "facility-management-housekeeping"),
 ("service-industries", "Service Industries", "gear", "Customized workforce and HR support for service-led businesses.", ["Support staff", "Operations teams", "HR outsourcing"], "payroll-hr-compliance"),
]

REGISTRATIONS = ["LLP Certificate of Incorporation", "PAN Registration", "GST Registration", "Shops & Commercial Establishments Registration", "EPF Registration", "ESI Registration",
                 "Professional Tax Registration", "MSME / Udyam Registration", "Contract Labour Licence, as applicable", "Labour Law Compliance Registrations", "ISO 9001:2015, ISO 14001:2015 & ISO 45001:2018 Certifications", "Campus Placement and Institutional Agreements"]

STATUTORY = [
 ("EPF", "Employees' Provident Fund", "Registration, contribution and filing support for provident fund.", "shield"),
 ("ESI", "Employees' State Insurance", "ESI coverage, contribution and compliance coordination.", "heart"),
 ("PT", "Professional Tax", "Professional Tax deduction and remittance support.", "file"),
 ("LWF", "Labour Welfare Fund", "Labour Welfare Fund contribution and filing support.", "users"),
 ("Contract Labour", "Contract labour compliance", "Coordination of contract labour licensing and records.", "clipboard"),
 ("Factory", "Factory compliance", "Coordination of factory-related statutory requirements.", "factory"),
 ("Gratuity", "Gratuity administration", "Gratuity computation and administration support.", "rupee"),
 ("Bonus & Benefits", "Bonus and employee benefits", "Bonus and employee benefits administration.", "star"),
]

VALUES = [
 ("Integrity", "Maintaining honesty and ethical business practices.", "scale"), ("Customer Focus", "Understanding and fulfilling client requirements.", "target"),
 ("Transparency", "Building relationships through trust and openness.", "eye"), ("Confidentiality", "Protecting client and employee information.", "lock"),
 ("Accountability", "Taking responsibility for our commitments.", "clipboard"), ("Human Values", "Respecting people and promoting employee welfare.", "heart"),
 ("Quality & Safety", "Maintaining service quality and workplace safety.", "hardhat"), ("Empowerment", "Encouraging learning, development and growth.", "trend"),
 ("Diversity", "Promoting equal opportunities and inclusion.", "globe"), ("Sustainability", "Supporting responsible and long-term development.", "leaf"),
]
STRENGTHS = ["Customized manpower and staffing solutions", "Skilled, semi-skilled and unskilled workforce availability", "Industry-focused recruitment and placement support",
             "Dedicated HR and workforce management services", "Employee welfare and retention initiatives", "Payroll and statutory compliance coordination", "Client-focused service delivery and long-term partnerships"]

FAQ_GENERAL = [
 ("What does Parvathi Vrushabha HR Solution LLP do?",
  "Parvathi Vrushabha HR Solution LLP is a Bengaluru-based HR and workforce solutions company. We provide manpower services, staffing and placement, campus recruitment, facility management and housekeeping, payroll management, HR audits and statutory compliance support."),
 ("Where is Parvathi Vrushabha HR Solution LLP located?",
  f"Our office is at {ADDR_ONE}. You can reach us on {P1} or {P2}, or email {E1}."),
 ("What types of manpower do you provide?",
  "We provide skilled, semi-skilled and unskilled manpower, including machine operators, technicians, production workers, helpers, drivers, housekeeping staff and office support staff, for industries such as manufacturing, retail, FMCG, logistics, pharmaceutical and healthcare, and hospitality."),
 ("Do you handle payroll and statutory compliance?",
  "Yes. We support payroll processing and salary administration, EPF, ESI, Professional Tax and Labour Welfare Fund compliance, contract labour and factory compliance coordination, and gratuity, bonus and benefits administration. We also conduct HR audits and offer HR outsourcing."),
 ("Do you offer campus recruitment?",
  "Yes. We plan and coordinate campus recruitment programs, build college partnerships, screen and assess candidates, and run on-campus, virtual and hybrid drives, along with interview coordination and onboarding support."),
 ("How can I request manpower or an HR service quote?",
  f"Call or WhatsApp {P1} or {P2}, email {E1} or {E2}, or use the enquiry form on our contact page. Tell us your industry, the roles you need and your location, and we will respond with a customized proposal."),
]

# ---------------------------------------------------------------- layout pieces
NAV = [("/", "Home"), ("/about/", "About"), ("/services/", "Services"), ("/industries/", "Industries"), ("/compliance/", "Compliance"), ("/careers/", "Careers"), ("/contact/", "Contact")]

def header(path):
    def cur(p): return ' aria-current="page"' if (path == p or (p != "/" and path.startswith(p))) else ""
    lis = []
    for p, n in NAV:
        if p == "/about/":
            sub = f'<a href="/about/">{ic("building")}Our story</a><a href="/about/entrepreneurial-legacy/">{ic("star")}Entrepreneurial legacy</a>'
            lis.append(f'<li class="has-sub"><a class="nl" href="{p}"{cur(p)}>{n}{ic("chevron")}</a><div class="sub">{sub}</div></li>')
        elif p == "/services/":
            sub = "".join(f'<a href="/services/{s["slug"]}/">{ic(s["icon"])}{esc(s["short"])}</a>' for s in SERVICES)
            lis.append(f'<li class="has-sub"><a class="nl" href="{p}"{cur(p)}>{n}{ic("chevron")}</a><div class="sub">{sub}</div></li>')
        else:
            lis.append(f'<li><a class="nl" href="{p}"{cur(p)}>{n}</a></li>')
    return f'''<header class="site-header"><div class="container nav-wrap">
<a class="brand" href="/" aria-label="{NAME} — home"><img src="/assets/img/logo.webp" width="50" height="50" alt="{NAME} logo"><span><b>Parvathi Vrushabha <span>HR Solution LLP</span></b><em class="slogan-mini">{TAG}</em></span></a>
<nav class="nav" id="site-nav" aria-label="Main"><ul>{"".join(lis)}</ul><span class="nav-cta"><a class="btn sm" href="/contact/">Get a free quote {ic("arrow","go")}</a></span></nav>
<button class="burger" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu"><span></span></button>
</div></header>'''

def footer():
    svc = "".join(f'<li><a href="/services/{s["slug"]}/">{esc(s["short"])}</a></li>' for s in SERVICES)
    links = "".join(f'<li><a href="{p}">{n}</a></li>' for p, n in NAV)
    return f'''<footer class="site-footer"><div class="container">
<div class="foot-grid">
<div><div class="foot-brand"><img src="/assets/img/logo.webp" width="64" height="64" alt="" loading="lazy"><div><b>Parvathi Vrushabha HR Solution LLP</b><small class="slg">{TAG}</small></div></div>
<p>{TAG} Bengaluru-based manpower, staffing &amp; placement, facility management, payroll and HR audit partner.</p></div>
<div><h4>Explore</h4><ul>{links}</ul></div>
<div><h4>Services</h4><ul>{svc}</ul></div>
<div><h4>Contact</h4><address style="font-style:normal"><ul>
<li class="contact-li">{ic("pin")}<span>{"<br>".join(ADDR_LINES)}</span></li>
<li class="contact-li">{ic("phone")}<span><a href="tel:{P1T}">{P1}</a><br><a href="tel:{P2T}">{P2}</a></span></li>
<li class="contact-li">{ic("mail")}<span><a href="mailto:{E1}">{E1}</a><br><a href="mailto:{E2}">{E2}</a></span></li>
</ul></address></div></div>
<div class="foot-bottom"><span>© {datetime.date.today().year} {NAME}. All rights reserved.</span><span>Manpower · Staffing-Placement · Facility Management · HR Audits</span></div>
</div></footer>
<a class="wa-float" href="https://wa.me/{P1T[1:]}?text={esc('Hello, I would like to know more about your HR and manpower services.').replace(' ', '%20')}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{ic("whatsapp")}</a>
<button class="to-top" aria-label="Back to top">{ic("arrow")}</button>'''

def org_schema():
    return {
        "@type": ["Organization", "EmploymentAgency"], "@id": SITE + "/#org", "name": NAME, "legalName": NAME, "alternateName": "Parvathi Vrushabha HR Solution",
        "url": SITE + "/", "logo": SITE + "/assets/img/icon-512.png", "image": SITE + "/assets/img/og-image.jpg", "slogan": TAG, "foundingDate": "2026", "founder": {"@id": SITE + "/about/entrepreneurial-legacy/#anithadevi"},
        "description": "Bengaluru-based HR and workforce solutions company offering manpower services, staffing and placement, campus recruitment, facility management and housekeeping, payroll management, HR audits and statutory compliance support.",
        "email": E1, "telephone": [P1T, P2T],
        "address": {"@type": "PostalAddress", "streetAddress": "No. 112, Raju Layout Main Road, 3rd Cross, Opp. Devaraj Urs Road, Nagadevanahalli, Jnanabharathi Post",
                    "addressLocality": "Bengaluru", "addressRegion": "Karnataka", "postalCode": "560056", "addressCountry": "IN"},
        "areaServed": [{"@type": "City", "name": "Bengaluru"}, {"@type": "State", "name": "Karnataka"}, {"@type": "Country", "name": "India"}],
        "contactPoint": [{"@type": "ContactPoint", "contactType": "customer service", "telephone": P1T, "email": E1, "availableLanguage": ["en", "kn", "hi"]},
                         {"@type": "ContactPoint", "contactType": "human resources", "telephone": P2T, "email": E2}],
        "knowsAbout": ["Manpower services", "Staffing and placement", "Campus recruitment", "Facility management", "Housekeeping services", "Payroll management", "HR audits", "EPF ESI statutory compliance", "Contract labour compliance", "HR outsourcing"],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "HR & workforce services", "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"], "url": f"{SITE}/services/{s['slug']}/"}} for s in SERVICES]},
    }

def faq_schema(faqs):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def faq_html(faqs, first_open=False):
    out = []
    for i, (q, a) in enumerate(faqs):
        out.append(f'<details{" open" if first_open and i == 0 else ""}><summary>{esc(q)}</summary><div class="ans"><p>{esc(a)}</p></div></details>')
    return f'<div class="faq">{"".join(out)}</div>'

def breadcrumbs_html(trail):
    items = "".join((f'<li><a href="{u}">{esc(n)}</a></li>' if u else f'<li aria-current="page">{esc(n)}</li>') for n, u in trail)
    return f'<nav aria-label="Breadcrumb"><ol class="crumbs">{items}</ol></nav>'

def page(path, title, desc, body, trail=None, extra=None, og_type="website", hero_img=None):
    url = SITE + path
    graph = [org_schema(),
             {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": NAME, "publisher": {"@id": SITE + "/#org"}, "inLanguage": "en-IN"},
             {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title, "description": desc, "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": SITE + "/#org"}, "inLanguage": "en-IN",
              "primaryImageOfPage": SITE + "/assets/img/og-image.jpg", "dateModified": TODAY}]
    if trail and len(trail) > 1:
        graph.append({"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + (u or path)} for i, (n, u) in enumerate(trail)]})
    graph += (extra or [])
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)
    head = f'''<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en-IN" href="{url}"><link rel="alternate" hreflang="x-default" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="author" content="{NAME}"><meta name="theme-color" content="#fffdf8">
<meta name="geo.region" content="IN-KA"><meta name="geo.placename" content="Bengaluru">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="{NAME}"><meta property="og:locale" content="en_IN">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og-image.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{NAME} logo — Manpower, Staffing, Placement">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{SITE}/assets/img/og-image.jpg">
<link rel="icon" href="/assets/img/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="192x192" href="/assets/img/icon-192.png"><link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest">
<link rel="alternate" type="text/markdown" href="/llms.txt" title="LLM-readable site summary">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..800&family=Figtree:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="/assets/css/styles.css?v={TODAY}">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">{ld}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="progress" aria-hidden="true"><i></i></div>
{sprite()}
{header(path)}
<main id="main">
'''
    tail = f'''
</main>
{footer()}
<script src="/assets/js/main.js?v={TODAY}" defer></script>
</body></html>'''
    return head + body + tail

def write(path, content):
    fp = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/404.html" and path != "/" else os.path.join(ROOT, "404.html" if path == "/404.html" else "index.html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8") as f: f.write(content)

def page_hero(trail, h1, lead, buttons="", art=""):
    return f'''<section class="page-hero"><span class="leaf a" aria-hidden="true"></span><span class="leaf b" aria-hidden="true"></span>
<div class="container">{breadcrumbs_html(trail)}<p class="eyebrow"{R()}>{esc(trail[-1][0])}</p><h1{R(1)}>{h1}</h1><p class="lead"{R(2)}>{lead}</p>{f'<div class="btn-row" style="margin-top:28px"{R(3)}>{buttons}</div>' if buttons else ""}</div></section>'''

def cta_band(title="Let's build your reliable team.", text="Tell us what you need — manpower, payroll, compliance or campus hiring — and we'll come back with a customized proposal.", svc=""):
    q = f"?service={svc}" if svc else ""
    return f'''<section class="section" style="padding-top:20px"><div class="container"><div class="cta"{R(0, "zoom")}>
<h2>{title}</h2><p>{text}</p>
<div class="btn-row" style="margin-top:26px"><a class="btn" data-magnetic href="/contact/{q}">Request a proposal {ic("arrow","go")}</a><a class="btn ghost" href="tel:{P1T}">{ic("phone")} Call {P1}</a></div></div></div></section>'''

def service_cards(slugs=None, home=False):
    out = []
    for n, s in enumerate(SERVICES, 1):
        if slugs and s["slug"] not in slugs: continue
        items = "".join(f"<li>{esc(i)}</li>" for i in s["items"][:3 if home else 5])
        out.append(f'''<article class="card service-card" data-tilt{R(n % 4)}><span class="num" aria-hidden="true">0{n}</span><div class="icon-badge {s["tone"]}">{ic(s["icon"])}</div>
<h3>{esc(s["name"])}</h3><p>{esc(s["blurb"])}</p><ul class="ticks">{items}</ul><a class="more" href="/services/{s["slug"]}/">Explore service {ic("arrow")}</a></article>''')
    return "".join(out)

def steps_html(steps):
    out = "".join(f'<li class="step"{R(i)}><div class="dot">{ic(icon)}<em>{i + 1}</em></div><div><h4>{esc(t)}</h4><p>{esc(d)}</p></div></li>' for i, (icon, t, d) in enumerate(steps))
    return f'<ol class="steps" style="list-style:none;padding:0;margin:0">{out}</ol>'

def tiers_html():
    t = [("Skilled", "hardhat", "var(--green)", ["Technicians", "Machine operators"]),
         ("Semi-skilled", "gear", "var(--blue)", ["Production workers", "Drivers", "Office support staff"]),
         ("Unskilled", "users", "#c98a00", ["Helpers", "Housekeeping staff"])]
    return '<div class="tiers">' + "".join(f'<div class="tier" style="--c:{c}"{R(i)}><h3>{ic(icon)}{n}</h3><div class="roles">{"".join(f"<span>{r}</span>" for r in roles)}</div></div>' for i, (n, icon, c, roles) in enumerate(t)) + '</div>'

def tiles_html(items=STATUTORY):
    return '<div class="grid g4">' + "".join(f'<div class="tile"{R(i % 4)}>{ic(icon)}<div><b>{esc(a)}</b><small>{esc(d)}</small></div></div>' for i, (a, full, d, icon) in enumerate(items)) + '</div>'

def reg_html():
    chk = '<svg viewBox="0 0 28 28" aria-hidden="true"><circle cx="14" cy="14" r="12.5"/><path d="M8.5 14.5l4 4 7-8"/></svg>'
    return '<ul class="reg">' + "".join(f'<li style="--i:{i}">{chk}<span>{esc(r)}</span></li>' for i, r in enumerate(REGISTRATIONS)) + '</ul>'


CERTS = json.load(open(os.path.join(os.path.dirname(__file__), "certs.json")))

def cert_section(idp="certifications"):
    cards = "".join(f'''<figure class="cert"{R(i % 5)}><span class="cert-img"><img src="/assets/img/certs/{slug}.webp" width="{w}" height="{h}" alt="{esc(cap)} logo" loading="lazy"></span><figcaption>{esc(cap)}</figcaption></figure>''' for i, (slug, cap, (w, h)) in enumerate(CERTS))
    return f'''<section class="section tint-aqua" id="{idp}"><div class="container"><div class="section-head center"{R()}><span class="cert-banner">Certification &amp; Accreditation</span>
<h2 style="margin-top:22px">Registered, certified &amp; <span class="hl">compliant</span></h2><p class="lead">The registrations, licences and management-system certifications behind {NAME}.</p></div>
<div class="cert-grid">{cards}</div>
<p class="note center" style="margin:30px auto 0;max-width:760px"{R()}>Logos belong to their respective issuing authorities. Certificates and registration documents are available on request — write to <a href="mailto:{E2}">{E2}</a>. Subject to applicability and current validity.</p></div></section>'''


def leader_strip():
    return f"""<section class="section tint-lime" id="leadership"><div class="container"><div class="split"><div{R(0, "left")}><p class="eyebrow">Entrepreneurial legacy</p>
<h2>Led by entrepreneurs who <span class="hl">build to last</span></h2>
<p class="lead">Founded in 2026 by Anithadevi E, with the guidance of Mr. Eshwarappa, an entrepreneur with over 30 years of business experience in Bengaluru.</p>
<div class="btn-row" style="margin-top:22px"><a class="btn green" href="/about/entrepreneurial-legacy/">Read our legacy {ic("arrow","go")}</a></div></div>
<div class="grid" style="gap:16px">
<a class="card lead-card" href="/about/entrepreneurial-legacy/#anithadevi"{R(1, "right")} style="display:flex;gap:20px;align-items:center;text-decoration:none;color:inherit"><span class="avatar">AE</span><span><b style="font-family:var(--head);font-size:1.25rem;display:block">Anithadevi E</b><span style="color:var(--ink-2)">Entrepreneur &amp; Designated Director</span></span></a>
<a class="card lead-card" href="/about/entrepreneurial-legacy/#eshwarappa"{R(2, "right")} style="display:flex;gap:20px;align-items:center;text-decoration:none;color:inherit"><span class="avatar g">E</span><span><b style="font-family:var(--head);font-size:1.25rem;display:block">Mr. Eshwarappa</b><span style="color:var(--ink-2)">Additional Designated Director</span></span></a>
</div></div></div></section>"""


def legacy_page():
    trail = [("Home", "/"), ("About us", "/about/"), ("Entrepreneurial legacy", None)]
    body = page_hero(trail, 'An entrepreneurial legacy, <span class="hl">built on trust</span>',
                     f"{NAME} is an emerging manpower, staffing, recruitment, placement and HR audit outsourcing company established in 2026 — guided by leadership with over 30 years of entrepreneurial experience in Bengaluru.",
                     f'<a class="btn" href="/contact/">Talk to us {ic("arrow","go")}</a><a class="btn ghost" href="/about/">Our story</a>')
    body += f"""<section class="section"><div class="container">
<div class="panel profile" id="anithadevi"{R(0, "left")}><span class="avatar">AE</span><div>
<span class="role">Entrepreneur &amp; Designated Director</span><h2 style="font-size:clamp(1.8rem,3vw,2.4rem);margin-bottom:12px">Anithadevi E</h2>
<div class="quals"><span>B.Com</span><span>DMLT</span><span>Financial advisory consultant</span></div>
<p>Anithadevi E is the Entrepreneur and Designated Director of Parvathi Vrushabha HR Solution LLP, an emerging manpower, staffing, recruitment, placement and HR audit outsourcing company established in 2026.</p>
<p>Driven by a clear vision to establish a reliable and integrated workforce management partner, she founded Parvathi Vrushabha HR Solution LLP with a commitment to delivering dependable manpower solutions, professional recruitment and manpower placement services, and comprehensive HR audit support. Her approach is built on the core values of reliability, transparency, professionalism and consistent service quality.</p>
<p>She is also a financial advisory consultant and pursued the Company Secretary programme under the Institute of Company Secretaries of India (ICSI) during 2014–2015, which was subsequently discontinued.</p>
<p style="margin:0">As the driving force behind Parvathi Vrushabha HR Solution LLP, Anithadevi provides direction, leads the company's vision and drives its strategic development, supported by the valuable guidance and business leadership of her father and husband.</p></div></div>
<div class="panel profile" id="eshwarappa" style="margin-top:26px"{R(1, "right")}><span class="avatar g">E</span><div>
<span class="role">Additional Designated Director</span><h2 style="font-size:clamp(1.8rem,3vw,2.4rem);margin-bottom:12px">Mr. Eshwarappa</h2>
<div class="quals"><span>Transport &amp; travels entrepreneur</span><span>Est. 1996</span><span>30+ years in Bengaluru</span></div>
<p>Mr. Eshwarappa, father of Anithadevi E, serves as the Additional Designated Director of Parvathi Vrushabha HR Solution LLP.</p>
<p>He is an established entrepreneur in the public transport and travel industry, having established his own transport and travels business in 1996. With over 30 years of entrepreneurial experience in Bengaluru, he brings extensive market knowledge, business acumen, operational expertise and valuable leadership guidance to the organization.</p>
<p style="margin:0">His entrepreneurial journey, business experience and commitment to building sustainable business operations provide a strong foundation for the organization's growth and long-term vision.</p></div></div>
</div></section>
<section class="section tint-warm"><div class="container"><div class="section-head center"{R()}><p class="eyebrow">The journey</p><h2>From a transport business to a <span class="hl">workforce partner</span></h2></div>
<div class="tl">
<div class="tl-item"{R(0, "right")}><span class="tl-year">1996</span><h3>A business is born</h3><p>Mr. Eshwarappa establishes his own transport and travels business in Bengaluru's public transport and travel industry.</p></div>
<div class="tl-item"{R(1, "right")}><span class="tl-year">30+ years</span><h3>Decades of enterprise</h3><p>Over thirty years of entrepreneurial experience in Bengaluru build market knowledge, business acumen and operational expertise.</p></div>
<div class="tl-item"{R(2, "right")}><span class="tl-year">2026</span><h3>Parvathi Vrushabha HR Solution LLP is established</h3><p>Anithadevi E founds {NAME} with a vision of a reliable, integrated workforce management partner.</p></div></div></div></section>
<section class="section"><div class="container"><div class="section-head center"{R()}><p class="eyebrow">Founding principles</p><h2>The values behind <span class="hl">every placement</span></h2></div>
<div class="grid g4">
<div class="tile"{R(0)}>{ic("shield")}<div><b>Reliability</b><small>Dependable manpower and service delivery.</small></div></div>
<div class="tile"{R(1)}>{ic("eye")}<div><b>Transparency</b><small>Trust through openness with clients and employees.</small></div></div>
<div class="tile"{R(2)}>{ic("briefcase")}<div><b>Professionalism</b><small>Professional recruitment, placement and HR audit support.</small></div></div>
<div class="tile"{R(3)}>{ic("star")}<div><b>Consistent quality</b><small>The same standard of service, every engagement.</small></div></div></div></div></section>"""
    body += cta_band("Work with a team built on trust.", "Tell us about your manpower, placement or HR audit needs and we'll respond with a customized proposal.")
    persons = [
        {"@type": "Person", "@id": SITE + "/about/entrepreneurial-legacy/#anithadevi", "name": "Anithadevi E", "jobTitle": "Entrepreneur & Designated Director", "worksFor": {"@id": SITE + "/#org"},
         "description": "Entrepreneur and Designated Director of Parvathi Vrushabha HR Solution LLP; financial advisory consultant."},
        {"@type": "Person", "@id": SITE + "/about/entrepreneurial-legacy/#eshwarappa", "name": "Mr. Eshwarappa", "jobTitle": "Additional Designated Director", "worksFor": {"@id": SITE + "/#org"},
         "description": "Established entrepreneur in the public transport and travel industry since 1996, with over 30 years of entrepreneurial experience in Bengaluru."}]
    return page("/about/entrepreneurial-legacy/", "Entrepreneurial Legacy: Anithadevi E & Mr. Eshwarappa | Parvathi Vrushabha HR Solution LLP",
                "Meet the leadership of Parvathi Vrushabha HR Solution LLP: Anithadevi E, Entrepreneur & Designated Director, and Mr. Eshwarappa, Additional Designated Director with 30+ years in Bengaluru.",
                body, trail, persons)

# ================================================================ PAGES
def home():
    words = ["Manpower", "Staffing", "Placement", "Audits"]
    ring_text = "   •   ".join(words) + "   •   "
    orbit = f'''<div class="hero-visual"{R(2, "zoom")}><div class="orbit" role="img" aria-label="Parvathi Vrushabha HR Solution LLP logo surrounded by service icons: recruitment, manpower, facility management and payroll">
<span class="ring r3"></span><span class="ring r2"></span>
<svg class="textring" viewBox="0 0 400 400" aria-hidden="true"><defs><path id="tp" d="M200,200 m-176,0 a176,176 0 1,1 352,0 a176,176 0 1,1 -352,0"/></defs><text><textPath href="#tp" textLength="1096" lengthAdjust="spacing">{"MANPOWER  •  STAFFING  •  PLACEMENT  •  AUDITS  •  "}</textPath></text></svg>
<div class="ring r1"><span class="node n1">{ic("cap")}</span><span class="node n2">{ic("users")}</span><span class="node n3">{ic("building")}</span><span class="node n4">{ic("rupee")}</span></div>
<div class="core"><img src="/assets/img/logo.webp" width="320" height="320" alt="{NAME} logo" fetchpriority="high"></div>
<span class="chip-float cf1">Campus Recruitment</span><span class="chip-float cf2">Facility Management</span><span class="chip-float cf3">Payroll &amp; Compliance</span><span class="chip-float cf4">Skilled · Semi-skilled · Unskilled</span>
</div><p class="slogan-line"><span>{TAG}</span></p></div>'''
    hero = f'''<section class="hero"><span class="leaf a" aria-hidden="true"></span><span class="leaf b" aria-hidden="true"></span><span class="blob" style="width:260px;height:260px;left:-80px;bottom:40px;background:rgba(201,242,91,.35)" aria-hidden="true"></span>
<div class="container hero-grid"><div>
<p class="eyebrow"{R()}>Bengaluru · HR &amp; Workforce Solutions LLP</p>
<h1{R(1)}>Manpower, Staffing &amp; <span class="hl">HR Solutions</span> in Bengaluru</h1>
<p class="lead"{R(2)}>{NAME} provides manpower services, staffing &amp; placement, campus recruitment, facility management, payroll management, HR audits and statutory compliance support to businesses across industries.</p>
<p{R(2)} style="font-family:var(--head);font-weight:700;font-size:1.3rem;margin-bottom:28px">Connecting the right people with the right <span class="rotator" data-rotate="organizations|opportunities|teams|careers">organizations</span></p>
<div class="btn-row"{R(3)}><a class="btn" data-magnetic href="/contact/?service=Manpower%20%26%20Workforce%20Solutions">Request manpower {ic("arrow","go")}</a><a class="btn ghost" data-magnetic href="/services/">Explore services</a></div>
<div class="hero-meta"{R(4)}><span>{ic("pin")} Nagadevanahalli, Bengaluru 560056</span><span>{ic("phone")} <a href="tel:{P1T}" style="color:inherit">{P1}</a></span><span>{ic("mail")} {E1}</span></div>
</div>{orbit}</div></section>'''
    stats = f'''<div class="container"><div class="stats" role="list" aria-label="Company at a glance">
<div class="stat" role="listitem"><b data-count="4">4</b><span>Core service lines</span></div><div class="stat" role="listitem"><b data-count="9">9</b><span>Industries served</span></div>
<div class="stat" role="listitem"><b data-count="3">3</b><span>Workforce levels supplied</span></div><div class="stat" role="listitem"><b data-count="10">10</b><span>Core values we work by</span></div>
<div class="stat" role="listitem"><b data-count="12">12</b><span>Registration &amp; compliance areas</span></div></div></div>'''
    marq = "".join(f'<span>{ic(i[2])}{esc(i[1])}</span>' for i in INDUSTRIES)
    marquee = f'<div class="marquee" style="margin-top:70px" aria-label="Industries we serve"><div class="marquee-track">{marq}{marq}</div></div>'
    services = f'''<section class="section" id="services"><div class="container"><div class="section-head center"{R()}><p class="eyebrow">What we do</p><h2>Four service lines. <span class="hl">One dependable partner.</span></h2>
<p class="lead">From the first hire to the monthly payslip and the statutory filing, we manage the workforce tasks that keep your business running.</p></div>
<div class="grid g2">{service_cards(home=True)}</div></div></section>'''
    process = f'''<section class="section tint-aqua" id="process"><div class="container"><div class="section-head center"{R()}><p class="eyebrow">How we work</p><h2>From requirement to a <span class="hl">reliable team</span> in six steps</h2>
<p class="lead">A simple, transparent flow — you always know where your hiring stands.</p></div>
{steps_html([("search", "Understand", "We study your roles, volumes, shifts and site."), ("users", "Source", "We tap our skilled, semi-skilled and unskilled talent pool."), ("clipboard", "Screen & assess", "Screening, assessments and background verification."), ("handshake" if False else "link", "Select & onboard", "Interviews, selection and onboarding documentation."), ("briefcase", "Deploy & manage", "Attendance, shifts and payroll coordination."), ("shield", "Retain & comply", "Welfare, training, safety and statutory compliance.")])}
</div></section>'''
    panes = [
        ("Recruit", "Recruit", "cap", "Staffing, placement & campus hiring", "We source, screen and place talent — from campus drives with colleges to experienced hires for your teams.", ["Candidate screening and assessments", "On-campus, virtual and hybrid drives", "Interview coordination and onboarding support"], [("Campus recruitment", "campus-recruitment-placement"), ("Manpower solutions", "manpower-workforce-solutions")]),
        ("Deploy", "Deploy", "users", "Manpower & facility workforce", "Skilled, semi-skilled and unskilled teams deployed to your plant, warehouse, office or facility with attendance and shift coordination.", ["Industrial and commercial housekeeping", "Production and industrial support manpower", "Attendance and shift management coordination"], [("Facility management", "facility-management-housekeeping"), ("Manpower solutions", "manpower-workforce-solutions")]),
        ("Pay", "Pay", "rupee", "Payroll & benefits administration", "Accurate payroll processing, salary administration and employee benefits so your people are paid correctly and on time.", ["Payroll processing and salary administration", "Gratuity, bonus and benefits administration", "Employee onboarding documentation"], [("Payroll & HR compliance", "payroll-hr-compliance")]),
        ("Comply", "Comply", "shield", "Statutory compliance & HR audits", "Stay on the right side of labour law with EPF, ESI, Professional Tax and Labour Welfare Fund support, plus audits that surface gaps early.", ["EPF, ESI, PT and LWF support", "Contract labour and factory compliance coordination", "HR audits and HR outsourcing"], [("Payroll & HR compliance", "payroll-hr-compliance"), ("Compliance overview", None)]),
        ("Retain", "Retain", "heart", "Welfare, training & safety", "Our services go beyond recruitment — focusing on employee welfare, retention, training and workplace safety.", ["Employee welfare and retention initiatives", "Training and capability building", "Workplace safety and quality focus"], [("About our values", "about")]),
    ]
    nodes = "".join(f'<button class="wnode" data-hub="{a}" aria-pressed="false" aria-label="{a}">{ic(i)}<span>{a}</span></button>' for a, _, i, *_ in panes)
    pane_html = ""
    for a, _, i, t, d, items, links in panes:
        ls = "".join(f'<a href="{"/compliance/" if s is None else ("/about/" if s == "about" else "/services/" + s + "/")}">{esc(n)}</a>' for n, s in links)
        pane_html += f'<div class="pane"><span class="tag">{a}</span><h3>{esc(t)}</h3><p>{esc(d)}</p><ul class="ticks">{"".join(f"<li>{esc(x)}</li>" for x in items)}</ul><div class="wlist">{ls}</div></div>'
    wheel = f'''<section class="section" id="lifecycle"><div class="container"><div class="section-head center"{R()}><p class="eyebrow">Employee lifecycle</p><h2>We support your people at <span class="hl">every stage</span></h2>
<p class="lead">Hover or tap a stage to see how we help.</p></div>
<div class="wheel-wrap"><div class="wheel"{R(0, "zoom")}>
<svg class="rings" viewBox="0 0 100 100" aria-hidden="true"><defs><linearGradient id="wg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#c9f25b"/><stop offset=".5" stop-color="#8fecf0"/><stop offset="1" stop-color="#f26a3d"/></linearGradient></defs>
<circle cx="50" cy="50" r="40" fill="none" stroke="#ece4d6" stroke-width="1.2"/>
<g style="transform-origin:50px 50px;animation:spin 40s linear infinite"><circle cx="50" cy="50" r="40" fill="none" stroke="url(#wg)" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="52 200"/></g>
<g style="transform-origin:50px 50px;animation:spin 70s linear infinite reverse"><circle cx="50" cy="50" r="46" fill="none" stroke="#9fa9bb" stroke-width=".35" stroke-dasharray="1 3"/></g></svg>
<div class="hub"><div><small>Your workforce</small><strong>Recruit</strong></div></div>{nodes}</div>
<div class="wdetail" aria-live="polite">{pane_html}</div></div></div></section>'''
    tiers = f'''<section class="section tint-warm" id="workforce"><div class="container"><div class="split top"><div{R(0, "left")}><p class="eyebrow">Workforce solutions</p><h2>Skilled, semi-skilled &amp; unskilled — <span class="hl">at every level</span></h2>
<p class="lead">Whatever the operational need, we supply the right workforce for it — and manage the HR work behind it.</p><div class="btn-row" style="margin-top:20px"><a class="btn green" href="/services/manpower-workforce-solutions/">Manpower solutions {ic("arrow","go")}</a></div></div>
<div><p style="font-weight:700;color:var(--ink-3);margin-bottom:12px">Examples of roles we supply</p>{tiers_html()}</div></div></div></section>'''
    ind_cards = "".join(f'''<a class="ind-link" href="/industries/#{s}"{R(i % 3)}><article class="card ind" data-tilt><div class="icon-badge {["", "g", "b", "y"][i % 4]}">{ic(ic_)}</div><h3>{esc(n)}</h3><p style="margin:0">{esc(d)}</p></article></a>''' for i, (s, n, ic_, d, r, sv) in enumerate(INDUSTRIES))
    industries = f'''<section class="section" id="industries"><div class="container"><div class="section-head center"{R()}><p class="eyebrow">Industries we serve</p><h2>Built for the way <span class="hl">your industry</span> works</h2></div>
<div class="grid g3">{ind_cards}</div></div></section>'''
    strengths = "".join(f'<li class="strength"{R(i % 4)}><b>{esc(s)}</b></li>' for i, s in enumerate(STRENGTHS))
    why = f'''<section class="section tint-lime" id="why"><div class="container"><div class="split top"><div{R(0, "left")}><p class="eyebrow">Why Parvathi Vrushabha</p><h2>Trust, transparency and <span class="hl">long-term relationships</span></h2>
<p class="lead">We believe people are the foundation of every successful organization. Our commitment is to connect the right talent with the right opportunities while helping businesses build productive and reliable teams.</p>
<div class="btn-row" style="margin-top:20px"><a class="btn" href="/about/">About us {ic("arrow","go")}</a></div></div><ul class="strengths" style="list-style:none;padding:0;margin:0">{strengths}</ul></div></div></section>'''
    faq = f'''<section class="section" id="faq"><div class="container"><div class="section-head center"{R()}><p class="eyebrow">FAQ</p><h2>Quick answers</h2></div>{faq_html(FAQ_GENERAL, True)}</div></section>'''
    body = hero + stats + marquee + services + process + wheel + tiers + industries + why + cert_section() + leader_strip() + faq + cta_band()
    return page("/", "Manpower, Staffing & HR Solutions in Bengaluru | Parvathi Vrushabha HR Solution LLP",
                "Bengaluru HR & workforce solutions LLP: manpower supply, staffing & placement, campus recruitment, housekeeping & facility management, payroll, HR audits and EPF/ESI compliance.",
                body, extra=[faq_schema(FAQ_GENERAL)])

def about():
    rings = [("Employee welfare", "heart", "var(--orange)"), ("Retention", "link", "var(--green)"), ("Training", "book", "var(--blue)"), ("Workplace safety", "hardhat", "#c98a00"), ("Workforce management", "users", "var(--orange)")]
    ring_html = "".join(f'''<div class="card ring-card" style="--c:{c}"{R(i)}><div class="ringsvg"><svg viewBox="0 0 120 120" aria-hidden="true"><circle class="bg" cx="60" cy="60" r="52"/><circle class="fg" cx="60" cy="60" r="52" pathLength="1"/></svg>{ic(icn)}</div><h3 style="margin:0;font-size:1.1rem">{n}</h3></div>''' for i, (n, icn, c) in enumerate(rings))
    vals = "".join(f'''<div class="vcard" tabindex="0" style="--c:{["var(--orange)", "var(--green)", "var(--blue)", "#c98a00"][i % 4]}"{R(i % 5)}><div class="in"><div class="f">{ic(ic_)}<span>{n}</span></div><div class="b"><strong>{n}</strong><span>{d}</span></div></div></div>''' for i, (n, d, ic_) in enumerate(VALUES))
    body = page_hero([("Home", "/"), ("About us", None)], f"People are the foundation of <span class=\"hl\">every organization</span>",
                     f"{NAME} is a Bengaluru-based Human Resource and Workforce Solutions company committed to providing reliable and customized HR services to businesses across various industries.",
                     f'<a class="btn" href="/contact/">Talk to us {ic("arrow","go")}</a><a class="btn ghost" href="/services/">Our services</a>')
    body += f'''<section class="section"><div class="container"><div class="split"><div{R(0, "left")}><p class="eyebrow">Who we are</p><h2>Reliable, customized HR &amp; workforce services</h2>
<p>We specialize in manpower services, staffing-placement, campus recruitment, facility management, payroll management, HR audits and statutory compliance support. We provide skilled, semi-skilled and unskilled manpower to meet the diverse workforce requirements of our clients.</p>
<p>With industry knowledge, professional expertise and a customer-focused approach, we deliver efficient and quality HR solutions. Our services go beyond recruitment, focusing on employee welfare, retention, training, workplace safety and effective workforce management.</p>
<p>We believe that people are the foundation of every successful organization. Our commitment is to connect the right talent with the right opportunities while helping businesses build productive and reliable teams.</p>
<p>At Parvathi Vrushabha HR Solution LLP, we value trust, transparency, quality service and long-term relationships with our clients and employees.</p>
<p><strong>Our goal is simple — to connect the right people with the right organizations and empower businesses through effective workforce solutions.</strong></p></div>
<div class="panel center"{R(1, "right")}><img src="/assets/img/logo.webp" width="220" height="220" alt="{NAME} emblem" style="margin:0 auto 18px;animation:bob 6s ease-in-out infinite" loading="lazy"><p style="font-family:var(--head);font-size:1.6rem;font-weight:800;line-height:1.15;margin-bottom:6px"><span class="hl">{TAG}</span></p><p style="color:var(--ink-3);margin:0">Manpower · Staffing-Placement · Facility Management · HR Audits</p></div></div></div></section>
<section class="section tint-warm"><div class="container"><div class="vm"><div class="card v"{R(0, "left")}><div class="icon-badge g">{ic("eye")}</div><p class="eyebrow">Our vision</p><p class="big">To become a trusted and preferred HR, Staffing and Facility Management solutions partner by creating employment opportunities, developing workforce capabilities and supporting sustainable business growth.</p></div>
<div class="card m"{R(1, "right")}><div class="icon-badge b">{ic("target")}</div><p class="eyebrow">Our mission</p><p class="big">To deliver quality, reliable and cost-effective HR and workforce solutions through professional service, operational excellence, employee welfare and strong client relationships.</p></div></div></div></section>
<section class="section" id="values"><div class="container"><div class="section-head center"{R()}><p class="eyebrow">Core values</p><h2>Ten values that guide <span class="hl">every engagement</span></h2><p class="lead">Hover, focus or tap a card to flip it.</p></div><div class="grid g4" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr))">{vals}</div></div></section>
<section class="section tint-aqua"><div class="container"><div class="section-head center"{R()}><p class="eyebrow">Beyond recruitment</p><h2>We look after the people <span class="hl">behind the headcount</span></h2></div>
<div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(190px,1fr))">{ring_html}</div></div></section>
<section class="section"><div class="container"><div class="section-head center"{R()}><p class="eyebrow">Strengths</p><h2>What clients can count on</h2></div><ul class="strengths" style="list-style:none;padding:0;margin:0 auto;max-width:820px">{"".join(f'<li class="strength"{R(i % 3)}><b>{esc(s)}</b></li>' for i, s in enumerate(STRENGTHS))}</ul></div></section>
<section class="section tint-lime"><div class="container"><div class="panel center" style="max-width:900px;margin:auto"{R(0, "zoom")}><p class="eyebrow" style="justify-content:center">Our commitment</p><p class="big" style="font-family:var(--head);font-size:clamp(1.3rem,2.4vw,1.8rem);line-height:1.35;font-weight:600">We are committed to delivering dependable HR and workforce solutions through quality service, professional ethics and customer satisfaction — building strong relationships, creating employment opportunities and supporting organizations in achieving their business goals.</p></div></div></section>'''
    body += cert_section() + leader_strip() + cta_band()
    return page("/about/", "About Parvathi Vrushabha HR Solution LLP | Bengaluru HR Company",
                "Meet Parvathi Vrushabha HR Solution LLP — a Bengaluru HR and workforce solutions company. Our vision, mission, ten core values and strengths in staffing, payroll and compliance.",
                body, [("Home", "/"), ("About us", None)])

def services_page():
    rows = ""
    for n, s in enumerate(SERVICES, 1):
        sats = {"campus-recruitment-placement": ["clipboard", "users", "calendar"], "manpower-workforce-solutions": ["hardhat", "truck", "gear"], "facility-management-housekeeping": ["bucket", "clock", "shield"], "payroll-hr-compliance": ["file", "scale", "chart"]}[s["slug"]]
        rows += f'''<section class="svc-row" id="{s["slug"]}"><div class="svc-copy"{R(0, "left")}><p class="eyebrow">Service 0{n}</p><h2>{esc(s["name"])}</h2><p class="lead">{esc(s["blurb"])}</p>
<ul class="ticks" style="margin:18px 0 26px">{"".join(f"<li>{esc(i)}</li>" for i in s["items"])}</ul><div class="btn-row"><a class="btn" href="/services/{s["slug"]}/">Learn more {ic("arrow","go")}</a><a class="btn ghost" href="/contact/?service={esc(s["short"]).replace(" ", "%20").replace("&amp;", "%26")}">Get a quote</a></div></div>
<div class="svc-art"{R(1, "right")}>{ic(s["icon"], "big-ic")}<span class="sat">{ic(sats[0])}</span><span class="sat">{ic(sats[1])}</span><span class="sat">{ic(sats[2])}</span></div></section>'''
    sub = "".join(f'<a href="#{s["slug"]}">{esc(s["short"])}</a>' for s in SERVICES)
    body = page_hero([("Home", "/"), ("Services", None)], "HR, staffing &amp; <span class=\"hl\">facility services</span> under one roof",
                     "Campus recruitment, specialized manpower, facility management and housekeeping, payroll management and HR compliance — customized to your business.")
    body += f'<div class="subnav"><div class="container">{sub}</div></div><div class="container">{rows}</div>' + cta_band("Not sure which service fits?", "Share your requirement and we'll recommend the right combination.")
    sch = [{"@type": "ItemList", "name": "Services", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": s["name"], "url": f"{SITE}/services/{s['slug']}/"} for i, s in enumerate(SERVICES)]}]
    return page("/services/", "HR, Manpower & Facility Management Services in Bengaluru | Parvathi Vrushabha HR Solution LLP",
                "Explore our services: campus recruitment, skilled & unskilled manpower, housekeeping & facility management, payroll processing and HR compliance for businesses in Bengaluru.",
                body, [("Home", "/"), ("Services", None)], sch)

SVC_DETAIL = {
 "campus-recruitment-placement": dict(
   title="Campus Recruitment & Placement Services in Bengaluru | Parvathi Vrushabha HR Solution LLP",
   desc="Structured campus recruitment: college partnerships, candidate screening and assessments, on-campus, virtual and hybrid drives, interviews and onboarding support in Bengaluru.",
   h1='Campus recruitment that brings <span class="hl">fresh talent</span> to your team',
   lead="Structured campus recruitment programs that connect your organization with fresh talent from colleges and educational institutions.",
   who=["Companies hiring freshers and trainees", "Colleges seeking placement partners", "HR teams without a campus-hiring desk"],
   steps=[("calendar", "Plan the drive", "Define roles, eligibility, timelines and format."), ("link", "Partner with colleges", "Coordinate with institutions and placement cells."), ("clipboard", "Screen & assess", "Shortlisting and structured assessments."), ("cap", "Run the drive", "On-campus, virtual or hybrid execution."), ("users", "Interview & select", "Interview coordination and final selection."), ("userplus", "Onboard", "Offer follow-up and onboarding support.")],
   faq=[("What is campus recruitment?", "Campus recruitment is hiring fresh talent directly from colleges and educational institutions through organized drives. We plan, coordinate and manage these programs end to end for employers."),
        ("Do you run virtual or hybrid campus drives?", "Yes. We run on-campus, virtual and hybrid recruitment drives, with candidate screening, assessments, interview coordination, selection and onboarding support."),
        ("Can colleges partner with you for placements?", "Yes. We build college partnerships and maintain campus placement and institutional agreements. Colleges can contact us at " + E2 + " or " + P2 + ".")]),
 "manpower-workforce-solutions": dict(
   title="Manpower Supply & Staffing Services in Bengaluru | Parvathi Vrushabha HR Solution LLP",
   desc="Skilled, semi-skilled and unskilled manpower supplier in Bengaluru for manufacturing, retail, FMCG, logistics, pharma, healthcare and hospitality. Operators, technicians, drivers and helpers.",
   h1='Reliable manpower for <span class="hl">every operational need</span>',
   lead="Skilled, semi-skilled and unskilled manpower to support the operational requirements of manufacturing, retail, logistics, healthcare, hospitality and more.",
   who=["Manufacturing & engineering units", "Retail, FMCG and distribution", "Logistics, warehousing and supply chain", "Pharmaceutical, healthcare and hospitality"],
   steps=[("search", "Understand", "Roles, headcount, shifts and site conditions."), ("users", "Source", "Candidates from our workforce pool."), ("shield", "Screen & verify", "Screening and background verification."), ("clipboard", "Interview / trade test", "Skills evaluation as needed."), ("briefcase", "Deploy", "Onboarding documentation and site deployment."), ("chart", "Monitor & support", "Attendance, payroll and ongoing coordination.")],
   faq=[("What kinds of manpower do you supply?", "We supply skilled, semi-skilled and unskilled manpower — machine operators, technicians, production workers, helpers, drivers, housekeeping staff and office support staff."),
        ("Which industries do you support with manpower?", "Manufacturing and engineering, retail and FMCG, logistics and supply chain, pharmaceutical and healthcare, hospitality, warehousing and distribution, commercial establishments and service industries."),
        ("Can you also manage payroll for deployed staff?", "Yes. Our payroll management and HR compliance services cover salary administration, EPF, ESI, Professional Tax and Labour Welfare Fund support, so staffing and payroll can sit with one partner.")]),
 "facility-management-housekeeping": dict(
   title="Housekeeping & Facility Management Services in Bengaluru | Parvathi Vrushabha HR Solution LLP",
   desc="Industrial and commercial housekeeping and facility management in Bengaluru: office maintenance, skilled and unskilled workforce deployment, attendance and shift coordination.",
   h1='Housekeeping &amp; facility management, <span class="hl">tailored to your site</span>',
   lead="Customized housekeeping and facility management solutions designed around the specific requirements of your premises and operations.",
   who=["Factories and industrial units", "Offices and commercial establishments", "Hospitality and healthcare premises", "Warehouses and distribution centres"],
   steps=[("search", "Site study", "Understand the premises, scope and standards."), ("clipboard", "Custom plan", "Manpower and shift plan for your site."), ("users", "Deploy team", "Trained housekeeping and support staff."), ("clock", "Shift & attendance", "Attendance and shift management coordination."), ("shield", "Quality & safety", "Supervision with a focus on safety."), ("trend", "Review", "Regular review and improvement.")],
   faq=[("What facility management services do you offer?", "Industrial and commercial housekeeping, office and facility maintenance support, skilled and unskilled workforce deployment, production and industrial support manpower, and attendance and shift management coordination."),
        ("Is the service customized to my premises?", "Yes. Every solution is based on the specific requirements of the client — site type, scope, shifts and headcount."),
        ("Do you manage attendance and shifts?", "Yes. Attendance and shift management coordination is part of our facility management service.")]),
 "payroll-hr-compliance": dict(
   title="Payroll, HR Audit & EPF/ESI Compliance Services in Bengaluru | Parvathi Vrushabha HR Solution LLP",
   desc="Payroll processing, HR outsourcing, HR audits, background verification and EPF, ESI, Professional Tax, LWF, contract labour and factory compliance support in Bengaluru.",
   h1='Payroll &amp; HR compliance <span class="hl">without the headaches</span>',
   lead="Support for HR operations, payroll activities and statutory compliance, so your team can focus on running the business.",
   who=["Growing companies without an in-house HR desk", "Factories and contract-labour users", "Businesses preparing for an HR audit", "Organizations outsourcing HR operations"],
   steps=[("file", "Collect inputs", "Attendance, joiners, leavers and changes."), ("rupee", "Compute salary", "Payroll processing and salary administration."), ("scale", "Statutory deductions", "EPF, ESI, PT and LWF support."), ("mail", "Disburse & payslips", "Salary and payslip coordination."), ("clipboard", "Records & returns", "Documentation and compliance coordination."), ("search", "Audit & review", "HR audits and improvement.")],
   faq=[("What payroll services do you provide?", "Payroll processing and salary administration, gratuity, bonus and employee benefits administration, and employee background verification and onboarding documentation."),
        ("Which statutory compliances do you support?", "EPF, ESI, Professional Tax and Labour Welfare Fund support, plus contract labour and factory compliance coordination."),
        ("Do you conduct HR audits?", "Yes. We offer HR audits and HR outsourcing to help organizations review their HR practices, documentation and statutory compliance.")]),
}

def service_page(slug):
    s, c = SV[slug], SVC_DETAIL[slug]
    trail = [("Home", "/"), ("Services", "/services/"), (s["short"], None)]
    body = page_hero(trail, c["h1"], c["lead"], f'<a class="btn" data-magnetic href="/contact/?service={esc(s["short"]).replace(" ", "%20").replace("&amp;", "%26")}">Request a proposal {ic("arrow","go")}</a><a class="btn ghost" href="tel:{P1T}">{ic("phone")} {P1}</a>')
    body += f'''<section class="section"><div class="container"><div class="split top"><div{R(0, "left")}><p class="eyebrow">What we do</p><h2>{esc(s["name"])}</h2><p class="lead">{esc(s["blurb"])}</p>
<ul class="ticks" style="margin-top:18px">{"".join(f"<li>{esc(i)}</li>" for i in s["items"])}</ul></div>'''
    # unique infographic per service
    if slug == "campus-recruitment-placement":
        body += f'''<div class="panel"{R(1, "right")} data-tabs><h3 style="margin-bottom:14px">Choose your drive format</h3>
<div class="tabs" role="tablist" aria-label="Drive format"><button class="tab" role="tab" aria-selected="true">On-campus</button><button class="tab" role="tab" aria-selected="false">Virtual</button><button class="tab" role="tab" aria-selected="false">Hybrid</button></div>
<div class="tabpanel" role="tabpanel"><p>Structured drives held at the college with coordinated logistics, assessments and panel interviews.</p><ul class="ticks"><li>Pre-placement talk and registration</li><li>Written / skills assessment</li><li>Panel interviews and same-day shortlisting</li></ul></div>
<div class="tabpanel" role="tabpanel"><p>Remote assessments and video interviews so students can participate from anywhere.</p><ul class="ticks"><li>Online registration and screening</li><li>Remote assessments</li><li>Video interviews and virtual selection</li></ul></div>
<div class="tabpanel" role="tabpanel"><p>A blend of both — early rounds online, final rounds on campus — flexible for employers and institutions.</p><ul class="ticks"><li>Online screening for wider reach</li><li>On-campus final interviews</li><li>Single coordinated schedule</li></ul></div></div></div></div></div></section>'''
    elif slug == "manpower-workforce-solutions":
        body += f'<div{R(1, "right")}><p style="font-weight:700;color:var(--ink-3);margin-bottom:12px">Examples of roles we supply</p>{tiers_html()}</div></div></div></section>'
    elif slug == "facility-management-housekeeping":
        body += f'''<div class="panel center"{R(1, "right")}><div class="clock" role="img" aria-label="Illustrative 24-hour three-shift coverage ring"><svg viewBox="0 0 320 320"><circle cx="160" cy="160" r="120" fill="none" stroke="#ece4d6" stroke-width="26"/>
<circle class="arc" cx="160" cy="160" r="120" stroke="#f2b01e" style="--len:245" transform="rotate(0 160 160)"/><circle class="arc" cx="160" cy="160" r="120" stroke="#f26a3d" style="--len:245;transition-delay:.3s" transform="rotate(120 160 160)"/><circle class="arc" cx="160" cy="160" r="120" stroke="#1f55a4" style="--len:245;transition-delay:.6s" transform="rotate(240 160 160)"/>
<g font-family="Figtree,sans-serif" font-size="13" font-weight="700" fill="#4b5567" text-anchor="middle"><text x="160" y="16">00:00</text><text x="312" y="165">06:00</text><text x="160" y="312">12:00</text><text x="10" y="165">18:00</text></g>
<g class="hand"><line x1="160" y1="160" x2="160" y2="58" stroke="#1d2330" stroke-width="3" stroke-linecap="round"/><circle cx="160" cy="160" r="7" fill="#1d2330"/></g>
<text x="160" y="154" text-anchor="middle" font-family="Bricolage Grotesque,sans-serif" font-weight="800" font-size="30" fill="#1b4d3e">24h</text><text x="160" y="178" text-anchor="middle" font-family="Figtree,sans-serif" font-weight="700" font-size="12" fill="#6b7587">COVERAGE</text></svg>
<div class="legend"><span><i style="--c:#f2b01e"></i>Shift A</span><span><i style="--c:#f26a3d"></i>Shift B</span><span><i style="--c:#1f55a4"></i>Shift C</span></div></div>
<p class="form-note" style="margin-top:14px">Illustrative three-shift pattern. Actual shift timings and headcount are planned around your site.</p></div></div></div></section>'''
    else:
        body += f'<div{R(1, "right")}><div class="panel"><h3>Statutory support at a glance</h3>{tiles_html(STATUTORY[:4]).replace("g4", "g2")}</div></div></div></div></section>'
    body += f'''<section class="section tint-aqua"><div class="container"><div class="section-head center"{R()}><p class="eyebrow">How it works</p><h2>Our process, <span class="hl">step by step</span></h2></div>{steps_html(c["steps"])}</div></section>
<section class="section"><div class="container"><div class="split"><div{R(0, "left")}><p class="eyebrow">Who it's for</p><h2>Built for teams like yours</h2><ul class="ticks" style="margin-top:16px">{"".join(f"<li>{esc(w)}</li>" for w in c["who"])}</ul></div>
<div class="grid" {R(1, "right")}><p class="lead" style="margin:0">Looking at more than {esc(s["short"].lower())}? Combine services under a single partner for simpler vendor management.</p>{service_cards([x["slug"] for x in SERVICES if x["slug"] != slug][:1], True)}</div></div></div></section>
<section class="section tint-warm"><div class="container"><div class="section-head center"{R()}><p class="eyebrow">FAQ</p><h2>Questions about {esc(s["short"].lower())}</h2></div>{faq_html(c["faq"], True)}</div></section>'''
    body += cta_band(svc=esc(s["short"]).replace(" ", "%20").replace("&amp;", "%26"))
    svc_schema = [{"@type": "Service", "@id": f"{SITE}/services/{slug}/#service", "name": s["name"], "description": s["blurb"], "serviceType": s["short"], "provider": {"@id": SITE + "/#org"},
                   "areaServed": {"@type": "City", "name": "Bengaluru"}, "url": f"{SITE}/services/{slug}/"}, faq_schema(c["faq"])]
    return page(f"/services/{slug}/", c["title"], c["desc"], body, trail, svc_schema)

def industries_page():
    cards = ""
    for i, (s, n, icn, d, roles, sv) in enumerate(INDUSTRIES):
        cards += f'''<article class="card ind" id="{s}" data-tilt{R(i % 3)}><div class="icon-badge {["", "g", "b", "y"][i % 4]}">{ic(icn)}</div><h3>{esc(n)}</h3><p>{esc(d)}</p><div class="roles">{"".join(f"<span>{r}</span>" for r in roles)}</div>
<p style="margin:16px 0 0"><a class="more" href="/services/{sv}/">{esc(SV[sv]["short"])} {ic("arrow")}</a></p></article>'''
    marq = "".join(f'<span>{ic(i[2])}{esc(i[1])}</span>' for i in INDUSTRIES)
    body = page_hero([("Home", "/"), ("Industries", None)], 'Workforce solutions for <span class="hl">nine industries</span>',
                     "From factory floors and warehouses to hotels, hospitals and offices — we supply the people and the HR support each industry depends on.")
    body += f'<div class="marquee"><div class="marquee-track">{marq}{marq}</div></div><section class="section"><div class="container"><div class="grid g3">{cards}</div></div></section>'
    body += cta_band("Don't see your industry listed?", "Our solutions are customized. Tell us about your workforce challenge and we'll design a plan around it.")
    return page("/industries/", "Industries We Serve: Manufacturing, Retail, Logistics, Healthcare | Parvathi Vrushabha HR Solution LLP",
                "Workforce, staffing and HR services for manufacturing & engineering, retail & FMCG, logistics, pharma/healthcare, hospitality, facility management, warehousing and more in Bengaluru.",
                body, [("Home", "/"), ("Industries", None)],
                [{"@type": "ItemList", "name": "Industries we serve", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": x[1]} for i, x in enumerate(INDUSTRIES)]}])

def compliance_page():
    audit = steps_html([("file", "Document review", "Review HR records and policies."), ("scale", "Statutory check", "Check against applicable labour laws."), ("search", "Gap report", "Clear list of gaps and risks."), ("clipboard", "Corrective plan", "Practical, prioritized fixes."), ("users", "Implementation", "Support in closing the gaps."), ("shield", "Ongoing monitoring", "Stay compliant going forward.")])
    faq = [("Which registrations does Parvathi Vrushabha HR Solution LLP maintain?", "We maintain the applicable business registrations and statutory compliance documentation required for our operations, including LLP incorporation, PAN, GST, Shops & Commercial Establishments, EPF, ESI, Professional Tax and MSME / Udyam registrations, plus Contract Labour Licence and labour law registrations as applicable. Documentation is available on request, subject to applicability and current validity."),
           ("Can you help us with EPF, ESI and Professional Tax?", "Yes. We provide EPF, ESI, Professional Tax and Labour Welfare Fund support as part of our Payroll Management & HR Compliance services."),
           ("Do you handle contract labour and factory compliance?", "We coordinate contract labour and factory compliance requirements for clients, alongside gratuity, bonus and employee benefits administration.")]
    body = page_hero([("Home", "/"), ("Registrations & Compliance", None)], 'Compliance you can <span class="hl">trust and verify</span>',
                     "We maintain the applicable business registrations and statutory documentation required for our operations — and help our clients stay compliant with theirs.",
                     f'<a class="btn" href="/contact/?service=Payroll%20%26%20HR%20compliance">Request compliance support {ic("arrow","go")}</a>')
    body += f'''<section class="section"><div class="container"><div class="section-head"{R()}><p class="eyebrow">Our registrations</p><h2>Registrations &amp; documentation</h2></div>{reg_html()}
<p class="note" style="margin-top:20px"{R()}>Documents are maintained subject to applicability and current validity. Copies of relevant certificates are available on request — write to <a href="mailto:{E2}">{E2}</a>.</p></div></section>
<section class="section tint-lime"><div class="container"><div class="section-head center"{R()}><p class="eyebrow">Statutory support for clients</p><h2>Labour-law compliance, <span class="hl">covered</span></h2><p class="lead">Part of our Payroll Management &amp; HR Compliance service.</p></div>{tiles_html()}</div></section>
<section class="section tint-aqua"><div class="container"><div class="section-head center"{R()}><p class="eyebrow">HR audits</p><h2>How an HR audit works</h2><p class="lead">A clear path from review to ongoing compliance.</p></div>{audit}</div></section>
<section class="section"><div class="container"><div class="section-head center"{R()}><p class="eyebrow">FAQ</p><h2>Compliance questions</h2></div>{faq_html(faq, True)}</div></section>'''
    body += cta_band("Need a compliance health check?", "Ask us about an HR audit or statutory compliance support for your organization.", "Payroll%20%26%20HR%20compliance")
    return page("/compliance/", "Registrations & Statutory Compliance (EPF, ESI, PT, LWF) | Parvathi Vrushabha HR Solution LLP",
                "Parvathi Vrushabha HR Solution LLP maintains applicable registrations — PAN, GST, EPF, ESI, PT, MSME — and supports clients with EPF, ESI, PT, LWF, contract labour and factory compliance.",
                body, [("Home", "/"), ("Registrations & Compliance", None)], [faq_schema(faq)])

def careers_page():
    steps = steps_html([("mail", "Share your CV", "Email or WhatsApp your updated CV."), ("search", "Profile review", "We review skills, experience and preferences."), ("clipboard", "Assessment / interview", "Screening, trade test or interview."), ("briefcase", "Placement", "Placement with a suitable organization."), ])
    cats = ["Machine operators", "Technicians", "Production workers", "Helpers", "Drivers", "Housekeeping staff", "Office support staff", "Freshers & graduates"]
    faq = [("How can I apply for a job through Parvathi Vrushabha HR Solution LLP?", f"Send your updated CV to {E2} or WhatsApp it to {P1}. Our team reviews your profile and contacts you about suitable openings."),
           ("What kind of jobs do you place candidates in?", "We place skilled, semi-skilled and unskilled candidates in roles such as machine operators, technicians, production workers, helpers, drivers, housekeeping and office support, across manufacturing, retail, FMCG, logistics, pharmaceutical, healthcare and hospitality."),
           ("I am a college. How can we partner with you?", f"We run campus recruitment programs and campus placement partnerships. Write to {E2} or call {P2} to start a conversation.")]
    body = page_hero([("Home", "/"), ("Careers & Placement", None)], 'Find the right opportunity, <span class="hl">find the right fit</span>',
                     "We connect job seekers and fresh graduates with organizations across manufacturing, retail, logistics, healthcare, hospitality and more.",
                     f'<a class="btn" href="mailto:{E2}?subject=CV%20for%20placement">{ic("mail")} Email your CV</a><a class="btn wa" href="https://wa.me/{P1T[1:]}?text=Hello%2C%20I%20would%20like%20to%20share%20my%20CV." target="_blank" rel="noopener">{ic("whatsapp")} WhatsApp us</a>')
    body += f'''<section class="section"><div class="container"><div class="section-head center"{R()}><p class="eyebrow">For job seekers</p><h2>Four steps to <span class="hl">your next role</span></h2></div>{steps}</div></section>
<section class="section tint-warm"><div class="container"><div class="split"><div{R(0, "left")}><p class="eyebrow">Roles we place</p><h2>Skilled, semi-skilled &amp; unskilled opportunities</h2><p class="lead">Tell us your trade, experience and preferred location — we'll match you with suitable openings.</p></div>
<div class="roles" style="display:flex;flex-wrap:wrap;gap:10px"{R(1, "right")}>{"".join(f'<span class="card" style="padding:12px 20px;border-radius:999px;font-weight:700;box-shadow:var(--shadow)">{c}</span>' for c in cats)}</div></div></div></section>
<section class="section tint-aqua"><div class="container"><div class="split"><div class="panel"{R(0, "left")}><div class="icon-badge b">{ic("cap")}</div><h3>For colleges &amp; institutions</h3><p>Partner with us for structured campus recruitment, assessments and placement drives — on-campus, virtual or hybrid.</p><a class="more" href="/services/campus-recruitment-placement/">Campus recruitment {ic("arrow")}</a></div>
<div class="panel"{R(1, "right")}><div class="icon-badge g">{ic("building")}</div><h3>For employers</h3><p>Need people? Tell us your roles, volumes and location and we'll propose a customized staffing plan.</p><a class="more" href="/contact/">Request manpower {ic("arrow")}</a></div></div></div></section>
<section class="section"><div class="container"><div class="section-head center"{R()}><p class="eyebrow">FAQ</p><h2>Careers &amp; placement questions</h2></div>{faq_html(faq, True)}</div></section>'''
    body += cta_band("Ready to get started?", "Send your CV or call our team — we'll take it from there.")
    return page("/careers/", "Jobs & Placement in Bengaluru | Parvathi Vrushabha HR Solution LLP",
                "Job seekers and freshers: share your CV with Parvathi Vrushabha HR Solution LLP for placement in manufacturing, retail, logistics, pharma, healthcare and hospitality roles in Bengaluru.",
                body, [("Home", "/"), ("Careers & Placement", None)], [faq_schema(faq)])

def contact_page():
    opts = ["Campus recruitment & placement", "Manpower & workforce solutions", "Facility management & housekeeping", "Payroll & HR compliance", "HR audit", "Job placement (candidate)", "Something else"]
    options = "".join(f'<option>{o}</option>' for o in opts)
    body = page_hero([("Home", "/"), ("Contact", None)], 'Let\'s talk about <span class="hl">your workforce</span>',
                     "Tell us what you need. We'll reply with a customized proposal — usually the same working day.".replace(" — usually the same working day", ""))
    body += f'''<section class="section"><div class="container"><div class="contact-grid"><div class="info-list">
<div class="info"{R(0, "left")}><span class="icon-badge">{ic("pin")}</span><div><b>Office</b><span>{"<br>".join(ADDR_LINES)}</span></div></div>
<div class="info"{R(1, "left")}><span class="icon-badge g">{ic("phone")}</span><div><b>Phone / WhatsApp</b><a href="tel:{P1T}">{P1}</a><br><a href="tel:{P2T}">{P2}</a></div></div>
<div class="info"{R(2, "left")}><span class="icon-badge b">{ic("mail")}</span><div><b>Email</b><a href="mailto:{E1}">{E1}</a><br><a href="mailto:{E2}">{E2}</a></div></div>
<div class="info"{R(3, "left")}><span class="icon-badge y">{ic("globe")}</span><div><b>Website</b><a href="{SITE}/">www.parvathivrushabha.com</a></div></div>
<a class="btn wa" href="https://wa.me/{P1T[1:]}" target="_blank" rel="noopener"{R(4)}>{ic("whatsapp")} Chat on WhatsApp</a></div>
<form class="form" data-contact novalidate{R(1, "right")}><h2 style="font-size:1.7rem">Send an enquiry</h2>
<div class="two"><div class="field"><label for="f-name">Your name *</label><input id="f-name" name="name" required autocomplete="name"></div><div class="field"><label for="f-company">Company / institution</label><input id="f-company" name="company" autocomplete="organization"></div></div>
<div class="two"><div class="field"><label for="f-phone">Phone *</label><input id="f-phone" name="phone" type="tel" required autocomplete="tel"></div><div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email"></div></div>
<div class="field"><label for="f-service">I'm interested in</label><select id="f-service" name="service">{options}</select></div>
<div class="field"><label for="f-msg">Your requirement</label><textarea id="f-msg" name="message" placeholder="Industry, roles needed, headcount, location…"></textarea></div>
<div class="btn-row"><button class="btn wa" type="submit" value="wa">{ic("whatsapp")} Send via WhatsApp</button><button class="btn ghost" type="submit" value="mail">{ic("mail")} Send via email</button></div>
<p class="form-note">This form opens WhatsApp or your email app with your message pre-filled. Nothing is stored on this website.</p></form></div>
<div style="margin-top:56px"{R()}><iframe class="map" title="Map of Parvathi Vrushabha HR Solution LLP, Nagadevanahalli, Bengaluru" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q={MAPQ.replace(" ", "+")}&output=embed"></iframe></div></div></section>'''
    return page("/contact/", "Contact Parvathi Vrushabha HR Solution LLP | Bengaluru 560056",
                f"Call {P1} / {P2}, WhatsApp or email {E1}. Office: Raju Layout Main Road, Nagadevanahalli, Jnanabharathi Post, Bengaluru 560056.",
                body, [("Home", "/"), ("Contact", None)], [{"@type": "ContactPage", "@id": SITE + "/contact/#contact", "url": SITE + "/contact/", "about": {"@id": SITE + "/#org"}}])

def not_found():
    body = f'''<section class="page-hero"><div class="container center"><img src="/assets/img/logo.webp" width="160" height="160" alt="" style="margin:0 auto 20px;animation:bob 5s ease-in-out infinite"><p class="eyebrow" style="justify-content:center">Error 404</p><h1 style="max-width:none">This page took a <span class="hl">day off</span></h1>
<p class="lead">The page you're looking for doesn't exist or has moved.</p><div class="btn-row" style="justify-content:center;margin-top:24px"><a class="btn" href="/">Back to home</a><a class="btn ghost" href="/contact/">Contact us</a></div></div></section>'''
    return page("/404.html", "Page not found | Parvathi Vrushabha HR Solution LLP", "The page you requested could not be found.", body).replace('content="index,follow', 'content="noindex,follow')

# ================================================================ run
PAGES = [("/", home())]
PAGES += [("/about/", about()), ("/services/", services_page())] + [(f"/services/{s['slug']}/", service_page(s["slug"])) for s in SERVICES]
PAGES += [("/about/entrepreneurial-legacy/", legacy_page()), ("/industries/", industries_page()), ("/compliance/", compliance_page()), ("/careers/", careers_page()), ("/contact/", contact_page()), ("/404.html", not_found())]
for p, c in PAGES: write(p, c)

prio = {"/": "1.0", "/services/": "0.9", "/contact/": "0.8", "/about/": "0.8"}
urls = [p for p, _ in PAGES if p != "/404.html"]
with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f'  <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>{prio.get(u, "0.7")}</priority></url>\n' for u in urls) + "</urlset>\n")

bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot", "anthropic-ai", "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended", "Bingbot", "CCBot", "Meta-ExternalAgent", "Amazonbot", "cohere-ai", "DuckAssistBot"]
with open(os.path.join(ROOT, "robots.txt"), "w") as f:
    f.write("# Search engines and AI assistants are welcome to crawl and cite this site.\nUser-agent: *\nAllow: /\n\n" + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"Sitemap: {SITE}/sitemap.xml\n")

with open(os.path.join(ROOT, "llms.txt"), "w") as f:
    f.write(f"""# {NAME}

> Bengaluru-based Human Resource and Workforce Solutions company. {TAG} We provide manpower services, staffing and placement, campus recruitment, facility management and housekeeping, payroll management, HR audits and statutory compliance support to businesses across industries.

## Key facts
- Legal name: {NAME}
- Established: 2026
- Leadership: Anithadevi E (Entrepreneur & Designated Director); Mr. Eshwarappa (Additional Designated Director, transport & travels entrepreneur since 1996)
- Location: {ADDR_ONE}
- Phone / WhatsApp: {P1}, {P2}
- Email: {E1}, {E2}
- Website: {SITE}/
- Workforce supplied: skilled, semi-skilled and unskilled manpower (machine operators, technicians, production workers, helpers, drivers, housekeeping and office support staff)
- Industries: Manufacturing & Engineering; Retail & FMCG; Logistics & Supply Chain; Pharmaceutical / Healthcare; Hospitality; Facility Management; Warehousing & Distribution; Commercial Establishments; Service Industries
- Vision: To become a trusted and preferred HR, Staffing and Facility Management solutions partner by creating employment opportunities, developing workforce capabilities and supporting sustainable business growth.
- Mission: To deliver quality, reliable and cost-effective HR and workforce solutions through professional service, operational excellence, employee welfare and strong client relationships.

## Services
""" + "".join(f"- [{s['name']}]({SITE}/services/{s['slug']}/): {s['blurb']}\n" for s in SERVICES) + f"""
## Pages
- [Home]({SITE}/): Overview of services, process and FAQs
- [About us]({SITE}/about/): Vision, mission, ten core values, strengths
- [Entrepreneurial legacy]({SITE}/about/entrepreneurial-legacy/): Founder and director profiles, company established 2026
- [Services]({SITE}/services/): All four service lines
- [Industries]({SITE}/industries/): Nine industries served
- [Registrations & Compliance]({SITE}/compliance/): Registrations maintained (subject to applicability and validity) and statutory support (EPF, ESI, PT, LWF, contract labour, factory, gratuity, bonus)
- [Careers & Placement]({SITE}/careers/): For job seekers, freshers and colleges
- [Contact]({SITE}/contact/): Enquiry form, phone, WhatsApp, email, map
""")

with open(os.path.join(ROOT, "site.webmanifest"), "w") as f:
    json.dump({"name": NAME, "short_name": SHORT, "start_url": "/", "display": "browser", "background_color": "#fffdf8", "theme_color": "#fffdf8",
               "icons": [{"src": "/assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, f, indent=2)

print(f"Built {len(PAGES)} pages + sitemap.xml, robots.txt, llms.txt, site.webmanifest")
