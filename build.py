#!/usr/bin/env python3
"""
JWLF static-site generator.
Runs once to emit plain .html files with identical header/footer chrome.
The deployed artifact is the generated files only — no build step is
required on GitHub Pages. Re-run `python3 build.py` after editing.
"""
import os, textwrap

ROOT = os.path.dirname(os.path.abspath(__file__))
EMAIL = "jwlf.org@gmail.com"  # sourced from public listings; live site obfuscates it — VERIFY (see MIGRATION-CHECKLIST.md)
EVENTBRITE = "https://www.eventbrite.com/e/2026-jacksonville-womens-leadership-forum-individual-registration-registration-1985441859047?aff=oddtdtcreator"
FACEBOOK = "https://www.facebook.com/JaxWLF/"
LINKEDIN = "https://www.linkedin.com/groups/4252397"
BROCHURE = "https://www.jwlf.org/wp-content/uploads/2024/04/2024-JWLF-Sponsorship-Opportunity.pdf"

DISCLOSURE = ("The Jacksonville Women\u2019s Leadership Forum is a non-profit 501(c)(3) corporation. "
  "CONTRIBUTIONS ARE DEDUCTIBLE TO THE EXTENT ALLOWED BY LAW. A COPY OF THE OFFICIAL REGISTRATION AND "
  "FINANCIAL INFORMATION MAY BE OBTAINED FROM THE DIVISION OF CONSUMER SERVICES BY CALLING TOLL-FREE "
  "(800-435-7352) WITHIN THE STATE. REGISTRATION DOES NOT IMPLY ENDORSEMENT, APPROVAL, OR RECOMMENDATION "
  "BY THE STATE.")

# ---------------------------------------------------------------- navigation
NAV = [
    ("Home", "index.html", []),
    ("About", None, [
        ("About JWLF", "about.html"),
        ("Message from the Chair", "message-from-chair.html"),
        ("Board of Directors & Officers", "board.html"),
        ("Non-Profit Partners", "non-profit-partners.html"),
        ("Photo Gallery", "gallery.html"),
        ("News", "news.html"),
    ]),
    ("Forums & Events", None, [
        ("Upcoming Forum & Events", "forum.html"),
        ("Current Speakers & Panelists", "speakers.html"),
        ("Previous Speakers & Events", "previous-speakers.html"),
    ]),
    ("Get Involved", "get-involved.html", [
        ("Sponsorship Information", "sponsorship.html"),
        ("Volunteer", "volunteer.html"),
        ("WoLF Award", "wolf-award.html"),
        ("Make a Donation", "donate.html"),
    ]),
    ("Contact", "contact.html", []),
]

def header(active):
    items = []
    for label, href, subs in NAV:
        if subs:
            sub_html = "".join(
                f'<li><a href="./{h}"{aria(active, h)}>{l}</a></li>' for l, h in subs
            )
            top_link = (f'<a href="./{href}"{aria(active, href)}>{label}</a>'
                        if href else "")
            items.append(
                f'<li class="has-submenu">'
                f'<button type="button" class="submenu-toggle" aria-expanded="false">'
                f'{label} <span class="caret" aria-hidden="true">&#9662;</span></button>'
                f'<ul class="submenu">'
                + (f'<li><a href="./{href}"{aria(active, href)}>{label} overview</a></li>' if href else "")
                + sub_html + "</ul></li>"
            )
        else:
            items.append(f'<li><a href="./{href}"{aria(active, href)}>{label}</a></li>')
    return f"""<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="nav-bar">
    <a class="brand" href="./index.html" aria-label="Jacksonville Women's Leadership Forum — home">
      <img src="./images/jwlf-logo.png" alt="Jacksonville Women's Leadership Forum logo"
           onerror="this.style.display='none';this.nextElementSibling.style.display='inline'">
      <span class="brand-fallback" style="display:none">JWLF</span>
    </a>
    <button type="button" class="nav-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav id="site-nav" class="site-nav" aria-label="Primary">
      <ul>
        {''.join(items)}
        <li class="nav-cta"><a class="btn btn--primary" href="./get-involved.html">Get Involved</a></li>
      </ul>
    </nav>
  </div>
</header>"""

def aria(active, href):
    return ' aria-current="page"' if active == href else ""

FOOTER = f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <h3>Jacksonville Women's Leadership Forum</h3>
        <p>Women working together to create leaders &amp; advance careers on the First Coast.</p>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <div class="footer-social">
          <a href="{FACEBOOK}" aria-label="JWLF on Facebook">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 21v-8h2.7l.4-3h-3.1V8.1c0-.9.3-1.5 1.6-1.5h1.6V3.9c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4V10H7.8v3h2.7v8h3z"/></svg>
          </a>
          <a href="{LINKEDIN}" aria-label="JWLF LinkedIn group">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4.98 3.5A2.49 2.49 0 1 1 5 8.48a2.49 2.49 0 0 1-.02-4.98zM3 9.75h4v11H3v-11zm6.5 0h3.8v1.5h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1v5.45h-4v-4.83c0-1.15-.02-2.63-1.6-2.63-1.6 0-1.85 1.25-1.85 2.55v4.91h-3.95v-11z"/></svg>
          </a>
          <a href="mailto:{EMAIL}" aria-label="Email JWLF">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h18a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zm9 7.3L4.4 7h15.2L12 12.3zM4 9.1V17h16V9.1l-8 5.2-8-5.2z"/></svg>
          </a>
        </div>
      </div>
      <div>
        <h3>About</h3>
        <ul>
          <li><a href="./about.html">About JWLF</a></li>
          <li><a href="./message-from-chair.html">Message from the Chair</a></li>
          <li><a href="./board.html">Board &amp; Officers</a></li>
          <li><a href="./non-profit-partners.html">Non-Profit Partners</a></li>
          <li><a href="./gallery.html">Photo Gallery</a></li>
          <li><a href="./news.html">News</a></li>
        </ul>
      </div>
      <div>
        <h3>Forums &amp; Events</h3>
        <ul>
          <li><a href="./forum.html">Upcoming Forum &amp; Events</a></li>
          <li><a href="./speakers.html">Current Speakers</a></li>
          <li><a href="./previous-speakers.html">Previous Speakers &amp; Events</a></li>
          <li><a href="{EVENTBRITE}">Registration (Eventbrite)</a></li>
        </ul>
      </div>
      <div>
        <h3>Get Involved</h3>
        <ul>
          <li><a href="./sponsorship.html">Sponsorship Information</a></li>
          <li><a href="./volunteer.html">Volunteer</a></li>
          <li><a href="./wolf-award.html">WoLF Award</a></li>
          <li><a href="./donate.html">Make a Donation</a></li>
          <li><a href="./contact.html">Contact Us</a></li>
        </ul>
        <h3 style="margin-top:1.25rem">Charity Partners</h3>
        <p style="font-size:0.875rem">We promote and support non-profits who do work to benefit women on the First Coast. <a href="./non-profit-partners.html">See our charity partners</a>.</p>
      </div>
    </div>
    <p class="disclosure">{DISCLOSURE}</p>
    <div class="footer-bottom">
      <p>Copyright &copy; <span id="footer-year">2026</span> Jacksonville Women's Leadership Forum | All Rights Reserved</p>
    </div>
  </div>
</footer>
<script src="./js/main.js"></script>"""

def page(filename, title, desc, body, active=None, extra_head=""):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Jacksonville Women's Leadership Forum</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="./css/style.css">
<link rel="icon" href="./images/jwlf-logo.png">
{extra_head}</head>
<body>
{header(active or filename)}
<main id="main">
{body}
</main>
{FOOTER}
</body>
</html>
"""
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)

def page_hero(h1, sub=""):
    subhtml = f"<p>{sub}</p>" if sub else ""
    return f"""<div class="page-hero"><div class="hero-inner"><h1>{h1}</h1>{subhtml}</div></div>"""

if __name__ == "__main__":
    import pages1  # noqa: F401  Home, About, Board, Partners, Gallery, News, Get Involved
    import pages2  # noqa: F401  Forums & Events
    import pages3  # noqa: F401  Get Involved detail pages, Contact, manifest
    print("Build complete.")
