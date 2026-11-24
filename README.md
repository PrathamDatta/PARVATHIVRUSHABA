# parvathivrushabha.com

Static multipage site (no framework, no build step needed to host). Upload the folder contents to any static host
(Netlify, Vercel, Cloudflare Pages, GitHub Pages, cPanel) with the domain pointed at it.

- Edit content in `_build/build.py`, then run `python3 _build/build.py` to regenerate all HTML, sitemap.xml, robots.txt, llms.txt.
- Design system: `assets/css/styles.css`; interactions/animations: `assets/js/main.js`.
- The contact form opens WhatsApp / the email app pre-filled (no backend). Swap for Formspree/Netlify Forms if you want stored submissions.
- After launch: submit `/sitemap.xml` to Google Search Console + Bing Webmaster, and claim the Google Business Profile for the Nagadevanahalli address.
