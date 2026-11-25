"""One-off patch: Entrepreneurial Legacy page, slogan under logo, founder schema, llms.txt."""
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def sub(path, pairs):
    s = open(os.path.join(ROOT, path), encoding="utf-8").read()
    for a, b in pairs:
        assert a in s, "missing: " + a[:70]
        s = s.replace(a, b, 1)
    open(os.path.join(ROOT, path), "w", encoding="utf-8").write(s)

# ------------------------------------------------------------ build.py
LEADER_HELPERS = r'''
def leader_strip():
    return f"""<section class="section tint-lime" id="leadership"><div class="container"><div class="split"><div{R(0, "left")}><p class="eyebrow">Entrepreneurial legacy</p>
<h2>Led by entrepreneurs who <span class="hl">build to last</span></h2>
<p class="lead">Founded in 2026 by Anithadevi E, with the guidance of Mr. Eshwarappa, an entrepreneur with over 30 years of business experience in Bengaluru.</p>
<div class="btn-row" style="margin-top:22px"><a class="btn green" href="/about/entrepreneurial-legacy/">Read our legacy {ic("arrow","go")}</a></div></div>
<div class="grid" style="gap:16px">
<a class="card lead-card" href="/about/entrepreneurial-legacy/#anithadevi"{R(1, "right")} style="display:flex;gap:20px;align-items:center;text-decoration:none;color:inherit"><span class="avatar">AE</span><span><b style="font-family:var(--head);font-size:1.25rem;display:block">Anithadevi E</b><span style="color:var(--ink-2)">Entrepreneur &amp; Designated Director</span></span></a>
<a class="card lead-card" href="/about/entrepreneurial-legacy/#eshwarappa"{R(2, "right")} style="display:flex;gap:20px;align-items:center;text-decoration:none;color:inherit"><span class="avatar g">E</span><span><b style="font-family:var(--head);font-size:1.25rem;display:block">Mr. Eshwarappa</b><span style="color:var(--ink-2)">Additional Designated Director</span></span></a>
</div></div></div></section>"""

'''

LEGACY_PAGE = r'''
def legacy_page():
    trail = [("Home", "/"), ("About us", "/about/"), ("Entrepreneurial legacy", None)]
    body = page_hero(trail, 'An entrepreneurial legacy, <span class="hl">built on trust</span>',
                     f"{NAME} is an emerging manpower, staffing, recruitment, placement and HR audit outsourcing company established in 2026 — guided by leadership with over 30 years of entrepreneurial experience in Bengaluru.",
                     f'<a class="btn" href="/contact/">Talk to us {ic("arrow","go")}</a><a class="btn ghost" href="/about/">Our story</a>')
    body += f"""<section class="section"><div class="container">
<div class="panel profile" id="anithadevi"{R(0, "left")}><span class="avatar">AE</span><div>
<span class="role">Entrepreneur &amp; Designated Director</span><h2 style="font-size:clamp(1.8rem,3vw,2.4rem);margin-bottom:12px">Anithadevi E</h2>
<div class="quals"><span>B.Com</span><span>DMLT</span><span>Financial advisory consultant</span></div>
<p>Anithadevi E is the Entrepreneur and Designated Director of ParvathiVrushabha HR Solution LLP, an emerging manpower, staffing, recruitment, placement and HR audit outsourcing company established in 2026.</p>
<p>Driven by a clear vision to establish a reliable and integrated workforce management partner, she founded ParvathiVrushabha with a commitment to delivering dependable manpower solutions, professional recruitment and manpower placement services, and comprehensive HR audit support. Her approach is built on the core values of reliability, transparency, professionalism and consistent service quality.</p>
<p>She is also a financial advisory consultant and pursued the Company Secretary programme under the Institute of Company Secretaries of India (ICSI) during 2014–2015, which was subsequently discontinued.</p>
<p style="margin:0">As the driving force behind ParvathiVrushabha, Anithadevi provides direction, leads the company's vision and drives its strategic development, supported by the valuable guidance and business leadership of her father and husband.</p></div></div>
<div class="panel profile" id="eshwarappa" style="margin-top:26px"{R(1, "right")}><span class="avatar g">E</span><div>
<span class="role">Additional Designated Director</span><h2 style="font-size:clamp(1.8rem,3vw,2.4rem);margin-bottom:12px">Mr. Eshwarappa</h2>
<div class="quals"><span>Transport &amp; travels entrepreneur</span><span>Est. 1996</span><span>30+ years in Bengaluru</span></div>
<p>Mr. Eshwarappa, father of Anithadevi E, serves as the Additional Designated Director of ParvathiVrushabha HR Solution LLP.</p>
<p>He is an established entrepreneur in the public transport and travel industry, having established his own transport and travels business in 1996. With over 30 years of entrepreneurial experience in Bengaluru, he brings extensive market knowledge, business acumen, operational expertise and valuable leadership guidance to the organization.</p>
<p style="margin:0">His entrepreneurial journey, business experience and commitment to building sustainable business operations provide a strong foundation for the organization's growth and long-term vision.</p></div></div>
</div></section>
<section class="section tint-warm"><div class="container"><div class="section-head center"{R()}><p class="eyebrow">The journey</p><h2>From a transport business to a <span class="hl">workforce partner</span></h2></div>
<div class="tl">
<div class="tl-item"{R(0, "right")}><span class="tl-year">1996</span><h3>A business is born</h3><p>Mr. Eshwarappa establishes his own transport and travels business in Bengaluru's public transport and travel industry.</p></div>
<div class="tl-item"{R(1, "right")}><span class="tl-year">30+ years</span><h3>Decades of enterprise</h3><p>Over thirty years of entrepreneurial experience in Bengaluru build market knowledge, business acumen and operational expertise.</p></div>
<div class="tl-item"{R(2, "right")}><span class="tl-year">2026</span><h3>ParvathiVrushabha is established</h3><p>Anithadevi E founds {NAME} with a vision of a reliable, integrated workforce management partner.</p></div></div></div></section>
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
    return page("/about/entrepreneurial-legacy/", "Entrepreneurial Legacy: Anithadevi E & Mr. Eshwarappa | Parvathi Vrushabha",
                "Meet the leadership of Parvathi Vrushabha HR Solution LLP: Anithadevi E, Entrepreneur & Designated Director, and Mr. Eshwarappa, Additional Designated Director with 30+ years in Bengaluru.",
                body, trail, persons)

'''

sub("_build/build.py", [
    # nav dropdown for About
    ('        if p == "/services/":', '''        if p == "/about/":
            sub = f'<a href="/about/">{ic("building")}Our story</a><a href="/about/entrepreneurial-legacy/">{ic("star")}Entrepreneurial legacy</a>'
            lis.append(f'<li class="has-sub"><a class="nl" href="{p}"{cur(p)}>{n}{ic("chevron")}</a><div class="sub">{sub}</div></li>')
        elif p == "/services/":'''),
    # slogan under logo: header + footer
    ('<span><b>PARVATHI VRUSHABHA</b><small>HR Solution LLP</small></span></a>', '<span><b>PARVATHI VRUSHABHA</b><small>HR Solution LLP</small><em class="slogan-mini">{TAG}</em></span></a>'),
    ('<div><b>PARVATHI VRUSHABHA</b><small>HR Solution LLP</small></div></div>', '<div><b>PARVATHI VRUSHABHA</b><small>HR Solution LLP</small><small class="slg">{TAG}</small></div></div>'),
    # founder schema
    ('"slogan": TAG,', '"slogan": TAG, "foundingDate": "2026", "founder": {"@id": SITE + "/about/entrepreneurial-legacy/#anithadevi"},'),
    # hero slogan below logo
    ('<span class="chip-float cf4">Skilled · Semi-skilled · Unskilled</span>\n</div></div>\'\'\'', '<span class="chip-float cf4">Skilled · Semi-skilled · Unskilled</span>\n</div><p class="slogan-line"><span>{TAG}</span></p></div>\'\'\''),
    # helpers before pages
    ('# ================================================================ PAGES', LEADER_HELPERS + LEGACY_PAGE + '# ================================================================ PAGES'),
    # home teaser
    ('body = hero + stats + marquee + services + process + wheel + tiers + industries + why + faq + cta_band()', 'body = hero + stats + marquee + services + process + wheel + tiers + industries + why + leader_strip() + faq + cta_band()'),
    # about teaser
    ('    body += cta_band()\n    return page("/about/"', '    body += leader_strip() + cta_band()\n    return page("/about/"'),
    # pages list
    ('("/industries/", industries_page()),', '("/about/entrepreneurial-legacy/", legacy_page()), ("/industries/", industries_page()),'),
    # llms.txt
    ('- Legal name: {NAME}\n', '- Legal name: {NAME}\n- Established: 2026\n- Leadership: Anithadevi E (Entrepreneur & Designated Director); Mr. Eshwarappa (Additional Designated Director, transport & travels entrepreneur since 1996)\n'),
    ('- [Services]({SITE}/services/): All four service lines', '- [Entrepreneurial legacy]({SITE}/about/entrepreneurial-legacy/): Founder and director profiles, company established 2026\n- [Services]({SITE}/services/): All four service lines'),
])

# ------------------------------------------------------------ CSS
css = r'''
/* ---------- slogan under logo ---------- */
.brand em.slogan-mini { display: block; font-style: italic; font-size: .66rem; font-weight: 700; color: var(--orange-d); line-height: 1.25; margin-top: 1px; letter-spacing: .01em; }
.slogan-line { display: flex; align-items: center; justify-content: center; gap: 14px; margin: 30px 0 0; font-family: var(--head); font-style: italic; font-weight: 700; font-size: clamp(1rem, 1.6vw, 1.2rem); color: var(--green); text-align: center; }
.slogan-line::before, .slogan-line::after { content: ""; flex: 1; max-width: 56px; height: 2px; border-radius: 2px; background: linear-gradient(90deg, transparent, var(--orange)); }
.slogan-line::after { transform: scaleX(-1); }
.foot-brand small { display: block; }
.foot-brand small.slg { font-size: .8rem; margin-top: 2px; }

/* ---------- leadership ---------- */
.avatar { width: 84px; height: 84px; border-radius: 50%; display: grid; place-items: center; font-family: var(--head); font-weight: 800; font-size: 1.8rem; color: #fff; flex: none;
  background: linear-gradient(135deg, var(--orange), var(--amber)); box-shadow: 0 12px 24px -10px rgba(242, 106, 61, .7), 0 0 0 5px #fff, 0 0 0 7px var(--lime); transition: transform .6s var(--ease); }
.avatar.g { background: linear-gradient(135deg, var(--green), #2f8a6c); box-shadow: 0 12px 24px -10px rgba(27, 77, 62, .7), 0 0 0 5px #fff, 0 0 0 7px var(--aqua); }
.lead-card:hover .avatar, .profile:hover .avatar { transform: rotate(-8deg) scale(1.06); }
.profile { display: grid; grid-template-columns: auto 1fr; gap: clamp(20px, 3vw, 36px); align-items: start; }
.profile .avatar { width: 116px; height: 116px; font-size: 2.5rem; }
.profile p { color: var(--ink-2); }
.role { display: inline-block; background: var(--bg-lime); color: var(--green); font-weight: 800; font-size: .76rem; letter-spacing: .08em; text-transform: uppercase; padding: 5px 14px; border-radius: 999px; margin-bottom: 12px; }
.quals { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 18px; }
.quals span { background: var(--bg-warm); border: 1px solid #f0d9bf; border-radius: 999px; padding: 5px 14px; font-weight: 700; font-size: .88rem; }
.tl { position: relative; display: grid; gap: 26px; max-width: 820px; margin: 0 auto; padding-left: 44px; }
.tl::before { content: ""; position: absolute; left: 12px; top: 8px; bottom: 8px; width: 4px; border-radius: 4px; background: linear-gradient(var(--lime), var(--aqua), var(--orange)); transform-origin: top; transform: scaleY(0); transition: transform 1.8s var(--ease); }
.tl.in::before, html:not(.js) .tl::before { transform: scaleY(1); }
.tl-item { position: relative; background: #fff; border: 1px solid var(--line); border-radius: 18px; padding: 22px 26px; box-shadow: var(--shadow); }
.tl-item::before { content: ""; position: absolute; left: -41px; top: 30px; width: 20px; height: 20px; border-radius: 50%; background: #fff; border: 4px solid var(--orange); box-shadow: 0 0 0 7px rgba(242, 106, 61, .15); animation: pulse-ring 3.5s ease-in-out infinite; }
.tl-year { display: block; font-family: var(--head); font-weight: 800; font-size: 2rem; color: var(--orange-d); line-height: 1; margin-bottom: 6px; }
.tl-item h3 { margin-bottom: 6px; } .tl-item p { margin: 0; color: var(--ink-2); }
@media (max-width: 640px) { .profile { grid-template-columns: 1fr; } .profile .avatar { width: 92px; height: 92px; font-size: 2rem; } .brand small { display: none; } }
'''
p = os.path.join(ROOT, "assets/css/styles.css")
s = open(p, encoding="utf-8").read()
s = s.replace(".brand small { display: none; }\n  .cta", "  .cta") if ".brand small { display: none; }\n  .cta" in s else s
s += css
open(p, "w", encoding="utf-8").write(s)

# ------------------------------------------------------------ JS: observe timeline
j = os.path.join(ROOT, "assets/js/main.js")
t = open(j, encoding="utf-8").read()
assert "'[data-reveal], .tier, .ring-card, .reg, .clock, [data-count]'" in t
t = t.replace("'[data-reveal], .tier, .ring-card, .reg, .clock, [data-count]'", "'[data-reveal], .tier, .ring-card, .reg, .clock, .tl, [data-count]'")
open(j, "w", encoding="utf-8").write(t)
print("patched")
