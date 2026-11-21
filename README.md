# Hamraah Tutoring website

Static site for **tutoring.hamraahadvisors.com**: online one-to-one tutoring (Maths, English, Science for grades 3 to 10, plus SAT and GCSE/IGCSE prep) for school students in the USA, UK and Europe. A service of Hamraah Advisors (SMC-Private) Limited. Hosted on Vercel; each push to `main` deploys.

- Content lives in `_build/build.py` (subjects, prices, tutors, FAQ, contact details). Edit there, then run `python3 _build/build.py` to regenerate the `.html` pages, `styles.css`, `sitemap.xml` and `robots.txt`, and commit the output.
- `_build/brand.css` is a copy of the main site's `styles.css` (repo Rashiasu/hamraah-website); `_build/tutoring.css` adds the teal accent and tutoring-only styles.
- `main.js` menu, scroll effects, free-trial form (sends via WhatsApp or email; number and email are constants at the top, keep them in sync with `build.py`).
- `vercel.json` clean URLs (`/pricing` serves `pricing.html`).
