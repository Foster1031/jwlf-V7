# JWLF Website — Rebuild of jwlf.org

A complete, ready-to-deploy static rebuild of the Jacksonville Women's Leadership
Forum website. Plain HTML, CSS, and vanilla JavaScript — no backend, database, or
build step is required to deploy.

## File structure

```
/
├── index.html                 Home
├── about.html                 About JWLF (About landing)
├── message-from-chair.html    Letter from Cari Smith
├── board.html                 Board of Directors & Officers
├── non-profit-partners.html   Charity/non-profit partners
├── gallery.html               Photo gallery (2012–2026) with lightbox
├── news.html                  News (migrated blog index — see checklist)
├── forum.html                 Upcoming Forum & Events
├── speakers.html              Current (2026) speakers & panelists
├── previous-speakers.html     Previous topics, speakers, panelists
├── get-involved.html          Get Involved hub (header CTA target)
├── sponsorship.html           Sponsorship info + tiers + inquiry form
├── volunteer.html             Volunteer info + interest form
├── wolf-award.html            WoLF Award criteria + nomination CTA
├── donate.html                Donation page + FL disclosure
├── contact.html               Contact form + social links
├── css/style.css              All styling; design tokens in :root
├── js/main.js                 Nav, lightbox, forms, scroll reveal
├── images/                    All site imagery (see below)
├── images-manifest.md         Every local image → its source URL on jwlf.org
├── download-images.sh         Fetches all images from the live site
├── MIGRATION-CHECKLIST.md     Page-by-page content mapping + flagged edits
└── build.py, pages*.py, images_data.py
                               Optional generator used to produce the HTML.
                               NOT needed for deployment — you may delete the
                               .py files from the deployed repo.
```

## One-time setup: images

This site was built in an environment without direct image access, so the
`images/` folders are empty placeholders. Before deploying:

1. **Windows:** double-click `download-images.bat`. **Mac/Linux:** run `bash download-images.sh`.
   (requires `curl`; downloads all 288 images from the live jwlf.org into place).
2. Any failures are printed — fetch those manually using `images-manifest.md`
   (local path → source URL) and drop them into the matching folder.
3. Pages degrade gracefully (alt text + tinted placeholders) until images exist.

### Image optimization (recommended)

The live site's photos are large. After downloading, compress for the web,
e.g. with ImageMagick:

```
find images -type f \( -iname '*.jpg' -o -iname '*.jpeg' \) \
  -exec mogrify -resize '1600x1600>' -quality 80 -strip {} \;
```

Gallery photos can go smaller (`-resize '1200x1200>'`). All photos are
`loading="lazy"` except the home hero.

## Deploying to GitHub Pages (drag-and-drop)

> **Important:** GitHub's drag-and-drop upload never deletes old files. To avoid
> stale assets from a previous version, deploy to a **fresh repository** (or
> delete the repo's contents first), then upload this folder.

1. Create a **new** repository (e.g. `jwlf-site`).
2. Drag the entire contents of this folder (not the folder itself) into the
   repo's file area and commit. Upload `images/` after running the download
   script. GitHub's web uploader keeps folder structure if you drag folders in
   a Chromium browser; otherwise use GitHub Desktop or `git push`.
3. Settings → Pages → Source: `main` branch, `/ (root)` → Save.
4. The site appears at `https://<user>.github.io/jwlf-site/`. All paths are
   relative (`./css/...`), so it works from any subdirectory. To use
   `www.jwlf.org`, add the custom domain under Settings → Pages and point the
   domain's DNS (CNAME) at `<user>.github.io`.

## Wiring the forms to Formspree (go-live)

There are three forms (Contact, Sponsor inquiry, Volunteer). Each currently runs
in **demo mode**: client-side validation plus a friendly confirmation, with
nothing sent anywhere.

1. Create a form at https://formspree.io (free tier is fine); it emails
   submissions to the address you choose.
2. On the `<form>` tag, set `action="https://formspree.io/f/YOUR_ID"` and keep
   `method="POST"`.
3. In `js/main.js`, follow the "GOING LIVE WITH FORMSPREE" comment: either
   remove the `e.preventDefault()` (simplest — Formspree shows its own thank-you
   page) or use the provided `fetch()` snippet to keep the inline confirmation.
4. Remove the "demo mode" note under each form.

“Forum idea”, “speak at our events”, and “become a partner” CTAs point at the
contact form and pre-fill the subject via `?subject=…` (handled in main.js).

## Design system

- Tokens live in `css/style.css` `:root`. Per the org's request the palette
  uses the Jacksonville Jaguars team colors: teal `--brand #006778`, black
  `--brand-deep #101820`, gold `--gold #d7a22a` (hover `#9f792c`). Change
  those values and the whole site follows. Desktop dropdown menus open on
  hover, keyboard focus, or click; on mobile they are tap accordions.
- Type: Poppins (headings) / Inter (body) via Google Fonts.
- Components: buttons, cards, quote cards, tier cards, logo walls, person
  cards, speaker rows with expandable bios, gallery + lightbox.
- Accessibility: semantic landmarks, skip link, one `h1` per page, visible
  focus states, keyboard-operable menus/lightbox (Esc/arrows), `alt` text,
  AA-contrast palette, `prefers-reduced-motion` honored (scroll-reveal and
  smooth scrolling disable themselves).

## Editing content later

Either edit the `.html` files directly, or edit the page strings in
`pages1–3.py` and re-run `python3 build.py` (regenerates all pages with the
shared header/footer). The generated HTML is the source of truth for deploys.

## Self-score vs. the quality bar

| Criterion | Status |
|---|---|
| Navigation: 5 top-level items, sticky header, persistent CTA, footer sitemap, no orphan pages, key tasks ≤3 clicks | ✅ Register/Sponsor/Donate/Volunteer/Contact all reachable in 1–2 clicks from any page |
| Responsive 320/768/1200, touch hamburger with accordion sub-nav | ✅ Single-column at ≤600px; accordion sub-menus ≤900px |
| Accessibility (WCAG 2.1 AA) | ✅ Landmarks, skip link, focus states, alt text, reduced-motion, AA contrast; **re-verify contrast after any palette tweak** |
| Performance | ✅ No JS/CSS frameworks; lazy images; ⚠️ requires the image compression step above — source photos are large |
| Content fidelity | ✅ Every live page has a migrated equivalent; FL disclosure verbatim in footer + donate page; external links retained. ⚠️ Open items flagged in MIGRATION-CHECKLIST.md (contact email, PayPal button ID, blog article bodies, “Supporter $7,500” likely typo) |
| Consistency | ✅ Identical generated header/footer, one type scale, single accent system (Jaguars teal/black/gold) |
