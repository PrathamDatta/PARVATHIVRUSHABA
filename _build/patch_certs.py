"""One-off: process certification logos and add the Certification & Accreditation section (Home + About)."""
import os, json
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = "/tmp/claude-0/-home-user/2f1ef1b8-be71-53c1-9996-373925785f9b/scratchpad/logos"
OUT = os.path.join(ROOT, "assets/img/certs")
os.makedirs(OUT, exist_ok=True)

files = sorted(f for f in os.listdir(SRC) if f.endswith(".jpeg"))
# index in sorted order -> (slug, caption)  (order follows the client's reference sheet)
ORDER = [(11, "certificate-of-incorporation", "Certificate of Incorporation"), (10, "psara", "PSARA — Private Security Agencies Regulation Act"),
         (9, "iso-certified-company", "ISO Certified Company"), (6, "iso-45001-2018", "ISO 45001:2018"), (1, "iso-9001-2015", "ISO 9001:2015"),
         (12, "iso-14001-2015", "ISO 14001:2015"), (7, "gst", "GST Registration"), (14, "professional-tax", "Professional Tax"),
         (13, "msme", "MSME — Ministry of MSME, Govt. of India"), (0, "shram-suvidha", "Shram Suvidha"), (3, "epf", "EPF — Employees' Provident Fund"),
         (2, "esic", "ESIC — Employees' State Insurance"), (8, "contract-labour-licence", "Contract Labour Licence"), (5, "pan", "PAN Card"),
         (4, "shop-establishment", "Shops & Establishment Act")]
meta = []
for idx, slug, cap in ORDER:
    im = Image.open(os.path.join(SRC, files[idx])).convert("RGB")
    w, h = im.size
    # background colour = median of the border pixels; map it to pure white so logos sit cleanly on white cards
    px = im.load(); border = [px[x, y] for x in range(w) for y in (0, h - 1)] + [px[x, y] for y in range(h) for x in (0, w - 1)]
    bg = [sorted(c[i] for c in border)[len(border) // 2] for i in range(3)]
    im = Image.eval(im, lambda v: v)  # no-op, keeps type
    chans = [c.point(lambda v, b=bg[i]: min(255, int(v * 255 / max(b, 1)))) for i, c in enumerate(im.split())]
    im = Image.merge("RGB", chans)
    im = im.point(lambda v: 255 if v >= 243 else v)
    im = im.resize((int(w * 1.5), int(h * 1.5)), Image.LANCZOS)
    im.save(os.path.join(OUT, slug + ".webp"), quality=92, method=6)
    meta.append((slug, cap, im.size))
json.dump(meta, open(os.path.join(ROOT, "_build/certs.json"), "w"))

# ---------------------------------------------------------------- build.py
p = os.path.join(ROOT, "_build/build.py")
s = open(p, encoding="utf-8").read()

helper = '''
CERTS = json.load(open(os.path.join(os.path.dirname(__file__), "certs.json")))

def cert_section(idp="certifications"):
    cards = "".join(f\'\'\'<figure class="cert"{R(i % 5)}><span class="cert-img"><img src="/assets/img/certs/{slug}.webp" width="{w}" height="{h}" alt="{esc(cap)} logo" loading="lazy"></span><figcaption>{esc(cap)}</figcaption></figure>\'\'\' for i, (slug, cap, (w, h)) in enumerate(CERTS))
    return f\'\'\'<section class="section tint-aqua" id="{idp}"><div class="container"><div class="section-head center"{R()}><span class="cert-banner">Certification &amp; Accreditation</span>
<h2 style="margin-top:22px">Registered, certified &amp; <span class="hl">compliant</span></h2><p class="lead">The registrations, licences and management-system certifications behind {NAME}.</p></div>
<div class="cert-grid">{cards}</div>
<p class="note center" style="margin:30px auto 0;max-width:760px"{R()}>Logos belong to their respective issuing authorities. Certificates and registration documents are available on request — write to <a href="mailto:{E2}">{E2}</a>. Subject to applicability and current validity.</p></div></section>\'\'\'

'''
assert "def leader_strip" in s
s = s.replace("\ndef leader_strip", helper + "\ndef leader_strip", 1)
s = s.replace("why + leader_strip() + faq", "why + cert_section() + leader_strip() + faq", 1)
s = s.replace("    body += leader_strip() + cta_band()\n    return page(\"/about/\"", "    body += cert_section() + leader_strip() + cta_band()\n    return page(\"/about/\"", 1)
s = s.replace('"ISO Certification, if obtained and valid"', '"ISO 9001:2015, ISO 14001:2015 & ISO 45001:2018 Certifications"', 1)
open(p, "w", encoding="utf-8").write(s)

# ---------------------------------------------------------------- CSS
css = '''
/* ---------- certifications ---------- */
.cert-banner { display: inline-block; background: #0b1530; color: #ff9d1c; font-family: var(--head); font-weight: 800; font-size: clamp(1.2rem, 3vw, 2rem); letter-spacing: -.01em;
  padding: 12px clamp(34px, 6vw, 64px); clip-path: polygon(22px 0, calc(100% - 22px) 0, 100% 50%, calc(100% - 22px) 100%, 22px 100%, 0 50%); position: relative; overflow: hidden; }
.cert-banner::after { content: ""; position: absolute; inset: 0; background: linear-gradient(105deg, transparent 35%, rgba(255, 255, 255, .28) 50%, transparent 65%); transform: translateX(-120%); animation: certshine 5s ease-in-out 1s infinite; }
@keyframes certshine { 0%, 55% { transform: translateX(-120%); } 100% { transform: translateX(120%); } }
.cert-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: clamp(12px, 1.6vw, 20px); }
.cert { margin: 0; background: #fff; border: 1px solid var(--line); border-radius: 18px; padding: 16px 12px 14px; display: flex; flex-direction: column; align-items: center; gap: 10px; box-shadow: var(--shadow);
  transition: transform .45s var(--ease), box-shadow .4s, border-color .4s; position: relative; overflow: hidden; }
.cert:hover { transform: translateY(-8px) scale(1.03); box-shadow: var(--shadow-lg); border-color: #8fd8dc; }
.cert-img { height: 118px; width: 100%; display: grid; place-items: center; }
.cert-img img { max-height: 118px; max-width: 100%; width: auto; height: auto; object-fit: contain; transition: transform .6s var(--ease); }
.cert:hover .cert-img img { transform: scale(1.1) rotate(-2deg); }
.cert figcaption { font-weight: 700; font-size: .84rem; line-height: 1.3; text-align: center; color: var(--ink-2); }
@media (max-width: 1040px) { .cert-grid { grid-template-columns: repeat(3, 1fr); } }
@media (max-width: 640px) { .cert-grid { grid-template-columns: repeat(2, 1fr); } .cert-img { height: 96px; } .cert-img img { max-height: 96px; } }
'''
open(os.path.join(ROOT, "assets/css/styles.css"), "a", encoding="utf-8").write(css)
print("ok", len(meta))
