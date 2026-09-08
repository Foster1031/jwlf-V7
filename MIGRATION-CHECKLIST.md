# Content Migration Checklist — jwlf.org → rebuilt site

Fetched and inventoried on 2026-09-06. ✅ = migrated; ⚠️ = needs review/decision.

## Page mapping

| Live page | New location | Status |
|---|---|---|
| / (Home) | index.html | ✅ Welcome copy, 4 value pillars, 2026–27 theme banner, Who Should Attend, testimonials (Carbone, Forbess, Mills), officers preview, sponsor logo wall, forum-idea & speaker CTAs, Eventbrite link, FL disclosure |
| /message-from-chair/ | message-from-chair.html | ✅ Full letter + Cari Smith photo; internal links repointed to new pages |
| /boards-of-directors/ | board.html | ✅ 13 directors + 4 officers with photos, titles, employers, LinkedIn links |
| /non-profit-partners/ | non-profit-partners.html | ✅ All 14 partners with logos + external links |
| /photo-gallery/ | gallery.html | ✅ All years 2012–2026 (~190 photos) with lightbox, lazy-loaded |
| /blog/ | news.html + blog-*.html | ✅ Blog restored: index plus **6 full articles** migrated verbatim (Communication & Career Trajectory; Executive Presence; Confidence Catalyst; Power of Sponsorship; Best Ally or Worst Enemy; Infusing Hope). ⚠️ Page 2 of the live blog has at least one older post ("How Men Can Become Better Allies to Women", Oct 22 2018) still to migrate |
| /forums/ | forum.html | ✅ 2026 recap, 2027 “details coming soon” state, Eventbrite link, educational-events note, forum-idea + speaker CTAs |
| /forums/current-speakers/ | speakers.html | ✅ Janean C. Armstrong & Amelia Rose Earhart keynotes + 4 panelists (Burns, Lewis, Phillips, Swietek), full bios |
| /previous-speakers/ | previous-speakers.html | ✅ Topics 2014–2026, 29 featured-speaker bios, 66 panelist names, Charlene West quote, Dave Dallas checklist PDF link |
| /sponsorship-information/ | sponsorship.html | ✅ Intro copy, Mercedes-Benz testimonial, 5 tiers verbatim, brochure PDF link, logo wall, sponsor-inquiry form |
| /volunteer/ | volunteer.html | ✅ Copy + 3 volunteer categories + interest form |
| /wolf-award/ | wolf-award.html | ✅ Full award description + criteria + email nomination CTA |
| /make-a-donation/ | donate.html | ✅ Copy + FL disclosure; ⚠️ PayPal button ID needed (below) |
| /#contact | contact.html | ✅ Dedicated page; form fields match live (name, email, subject, message) |
| /interested-becoming-partner/ | contact.html?subject=partner | ⚠️ Live sub-page not fetched; CTA rerouted to contact form. If that page has unique copy, migrate it |
| /interested-becoming-sponsor/ | sponsorship.html#sponsor-inquiry | ⚠️ Same as above — rerouted to the on-page sponsor form |

## Copy edits made (flagged for review — nothing rewritten silently)

1. **Typo/consistency cleanup only** in bios: “Steton Hall” → “Seton Hall”; “philosophy” → “philanthropy” (Corinne Costa Davis); “Scripps Network” → “Scripps Networks”; “Nadia Bilchick” → “Nadia Bilchik”; “Dr. Lois Frankle” heading → “Dr. Lois Frankel”; stray “H” before Nadia's bio removed; minor punctuation/spacing fixes throughout.
2. **Brenda Reynolds bio:** the live page appends two paragraphs that clearly belong to Brigid Schulte (Washington Post/Pulitzer/Alexandria). Removed from Brenda's bio; retained in Brigid's.
3. **Cari Smith title:** live home page says “Manager, Enterprise Risk Management”; the board page says “Vice President, Enterprise Risk Management.” Used the board-page title everywhere. Confirm which is current.
4. **Supporter Sponsorship — $7,500:** kept verbatim from the live site, but it duplicates the Champion price while offering fewer tickets — likely a typo (e.g. $2,500). Confirm before publishing.
5. Removed the stray “[Save]” wp-admin link inside the Advocate tier (live-site artifact).
6. **Partner descriptions:** the live page shows logos + “find out more” links only. One-line descriptions were added for usability — **new copy; please review.** Partner names were inferred from logo filenames/alt text; verify (esp. “Women Veterans Resource Center”).
7. Heather McGowan bio: removed one duplicated “Fidelity” in the client list.
8. Gallery alt text is generic (“Attendees, speakers, and networking at the YEAR JWLF Forum”) since images couldn't be viewed; refine for key photos if desired.
9. Sukhinder Singh Cassidy: “her new book” → “her book” (Choose Possibility, 2021 — no longer new).
10. Home hero: consolidated the four rotating slider headlines into one hero + section CTAs. The live slider's first slide image is a Gmail screenshot artifact (`screenshot-mail.google.com…png`) — not migrated.

## Items requiring org input (blocking go-live)

| Item | Where | Action |
|---|---|---|
| **Contact email** | Footer, contact/sponsor/volunteer/WoLF pages | Live site obfuscates it (Cloudflare). `jwlf.org@gmail.com` was sourced from a public business listing — **verify** and replace if wrong (search-and-replace across .html) |
| **PayPal donate button** | donate.html | Replace `REPLACE_WITH_JWLF_BUTTON_ID` with the org's PayPal hosted button ID (live site uses a PayPal form). Alternative: the org's verified GoFundMe charity page (EIN 46-3938058) |
| **Form endpoints** | contact, sponsorship, volunteer | Create Formspree forms and wire per README |
| **Sponsorship brochure PDF** | sponsorship.html | Currently links to the live-site PDF URL; download it into `./files/` and repoint before the old site goes away. Same for Dave Dallas's checklist PDF on previous-speakers.html |
| **Blog articles** | news.html | Decide: migrate the 6+ full article bodies from jwlf.org/blog before the old site is retired, or drop the News page from the nav |
| **Header CTA** | all pages | Currently “Get Involved” (registration closed). When 2027 registration opens, change the `.nav-cta` link to the Eventbrite URL and label it “Register” |
| **Logo & palette** | images/jwlf-logo.png, css :root | Palette changed to Jaguars teal/black/gold at the org's request — this intentionally departs from the original brief's "derive from the JWLF logo." Check the purple JWLF logo still reads well on the white header; consider a logo refresh or white-background lockup if it clashes |
| **Unidentified sponsor logos** | home + sponsorship logo walls | Four files had no identifying name (`0.png`, `0-1.png`, `EmbeddedImage.png`, `video-poster.png`, `50thGOLD.png`) — supply proper alt text or remove |

## Preserved verbatim

- Florida charitable-solicitation disclosure + 501(c)(3) statement (footer of every page + donate page).
- Eventbrite registration URL, facebook.com/JaxWLF, LinkedIn group 4252397.
- All testimonials with names/titles/companies; all sponsorship tier contents; WoLF Award text; Who Should Attend; value pillars; welcome copy; Message from the Chair.


## Changes made at the organization's request (this revision)

1. **Duplicate "Get Involved" resolved** — the header previously showed both a Get Involved nav dropdown and a Get Involved CTA button (the original brief required a persistent CTA with that label while registration is closed). The CTA is now **Donate** in all three languages; when 2027 registration opens, relabel it Register and point it at Eventbrite.
2. **Blog restored** — the original build had condensed the blog to a teaser index (the brief allowed omitting it); all six page-1 articles are now migrated in full. Ally article: the closing line's dead "download the eBook here" link and unfinished "learn more at" sentence from the live site were cleaned up; Tammy Heermann/Libby Gill "will be a keynote speaker at the 2019 Forum" updated to past tense.
3. **Spanish + Portuguese versions added** (flag switcher: US/Mexico/Brazil) — **this overrides the original brief's explicit "No multilingual support" exclusion**, at the organization's request. Translations are new copy produced for this build and **should be reviewed by a native speaker before launch**. Kept in English: bios, blog articles, theme titles, job titles, FL legal disclosure (translated preface added).
