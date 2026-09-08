#!/usr/bin/env python3
"""
JWLF static-site generator (multilingual).
Emits plain .html files: English at the root, Spanish in ./es/, Portuguese in
./pt/. Same filenames in every language, so the flag switcher just swaps the
directory. No build step is needed to deploy; re-run `python3 build.py` after
editing content.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
EMAIL = "jwlf.org@gmail.com"  # sourced from public listings; live site obfuscates it — VERIFY
EVENTBRITE = "https://www.eventbrite.com/e/2026-jacksonville-womens-leadership-forum-individual-registration-registration-1985441859047?aff=oddtdtcreator"
FACEBOOK = "https://www.facebook.com/JaxWLF/"
LINKEDIN = "https://www.linkedin.com/groups/4252397"
BROCHURE = "https://www.jwlf.org/wp-content/uploads/2024/04/2024-JWLF-Sponsorship-Opportunity.pdf"

DISCLOSURE = ("The Jacksonville Women\u2019s Leadership Forum is a non-profit 501(c)(3) corporation. "
  "CONTRIBUTIONS ARE DEDUCTIBLE TO THE EXTENT ALLOWED BY LAW. A COPY OF THE OFFICIAL REGISTRATION AND "
  "FINANCIAL INFORMATION MAY BE OBTAINED FROM THE DIVISION OF CONSUMER SERVICES BY CALLING TOLL-FREE "
  "(800-435-7352) WITHIN THE STATE. REGISTRATION DOES NOT IMPLY ENDORSEMENT, APPROVAL, OR RECOMMENDATION "
  "BY THE STATE.")

# --------------------------------------------------------- localized strings
L10N = {
 "en": dict(htmllang="en", skip="Skip to content",
   nav=dict(home="Home", about="About", forums="Forums & Events", getinv="Get Involved",
            contact="Contact", overview="Get Involved overview",
            about_sub=[("About JWLF","about.html"),("Message from the Chair","message-from-chair.html"),
              ("Board of Directors & Officers","board.html"),("Non-Profit Partners","non-profit-partners.html"),
              ("Photo Gallery","gallery.html"),("JWLF Blog","news.html")],
            forums_sub=[("Upcoming Forum & Events","forum.html"),("Current Speakers & Panelists","speakers.html"),
              ("Previous Speakers & Events","previous-speakers.html")],
            getinv_sub=[("Sponsorship Information","sponsorship.html"),("Volunteer","volunteer.html"),
              ("WoLF Award","wolf-award.html"),("Make a Donation","donate.html")]),
   cta=("Donate","donate.html"),
   f_tag="Women working together to create leaders &amp; advance careers on the First Coast.",
   f_about="About", f_forums="Forums &amp; Events", f_get="Get Involved",
   f_reg="Registration (Eventbrite)", f_contact="Contact Us",
   f_charity_h="Charity Partners",
   f_charity="We promote and support non-profits who do work to benefit women on the First Coast. <a href=\"./non-profit-partners.html\">See our charity partners</a>.",
   f_copy="Copyright &copy; <span id=\"footer-year\">2026</span> Jacksonville Women's Leadership Forum | All Rights Reserved",
   disclosure_pre="",
   lang_label="Language"),
 "es": dict(htmllang="es", skip="Ir al contenido",
   nav=dict(home="Inicio", about="Acerca de", forums="Foros y Eventos", getinv="Participa",
            contact="Contacto", overview="Panorama de Participa",
            about_sub=[("Acerca de JWLF","about.html"),("Mensaje de la Presidenta","message-from-chair.html"),
              ("Junta Directiva y Oficiales","board.html"),("Organizaciones Aliadas","non-profit-partners.html"),
              ("Galer\u00eda de Fotos","gallery.html"),("Blog de JWLF","news.html")],
            forums_sub=[("Pr\u00f3ximo Foro y Eventos","forum.html"),("Ponentes y Panelistas Actuales","speakers.html"),
              ("Ponentes y Eventos Anteriores","previous-speakers.html")],
            getinv_sub=[("Informaci\u00f3n de Patrocinio","sponsorship.html"),("Voluntariado","volunteer.html"),
              ("Premio WoLF","wolf-award.html"),("Haz una Donaci\u00f3n","donate.html")]),
   cta=("Donar","donate.html"),
   f_tag="Mujeres trabajando juntas para formar l\u00edderes y avanzar carreras en la Primera Costa de Florida.",
   f_about="Acerca de", f_forums="Foros y Eventos", f_get="Participa",
   f_reg="Registro (Eventbrite)", f_contact="Cont\u00e1ctanos",
   f_charity_h="Organizaciones Aliadas",
   f_charity="Promovemos y apoyamos a organizaciones sin fines de lucro que benefician a las mujeres de la Primera Costa. <a href=\"./non-profit-partners.html\">Conoce a nuestras aliadas</a>.",
   f_copy="Copyright &copy; <span id=\"footer-year\">2026</span> Jacksonville Women's Leadership Forum | Todos los derechos reservados",
   disclosure_pre="<strong>Aviso legal de Florida (se conserva en ingl\u00e9s por requisito legal):</strong> ",
   lang_label="Idioma"),
 "pt": dict(htmllang="pt-BR", skip="Pular para o conte\u00fado",
   nav=dict(home="In\u00edcio", about="Sobre", forums="F\u00f3runs e Eventos", getinv="Participe",
            contact="Contato", overview="Vis\u00e3o geral de Participe",
            about_sub=[("Sobre a JWLF","about.html"),("Mensagem da Presidente","message-from-chair.html"),
              ("Conselho Diretor e Diretoria","board.html"),("Parceiras Sem Fins Lucrativos","non-profit-partners.html"),
              ("Galeria de Fotos","gallery.html"),("Blog da JWLF","news.html")],
            forums_sub=[("Pr\u00f3ximo F\u00f3rum e Eventos","forum.html"),("Palestrantes e Painelistas Atuais","speakers.html"),
              ("Palestrantes e Eventos Anteriores","previous-speakers.html")],
            getinv_sub=[("Informa\u00e7\u00f5es de Patroc\u00ednio","sponsorship.html"),("Voluntariado","volunteer.html"),
              ("Pr\u00eamio WoLF","wolf-award.html"),("Fa\u00e7a uma Doa\u00e7\u00e3o","donate.html")]),
   cta=("Doar","donate.html"),
   f_tag="Mulheres trabalhando juntas para formar l\u00edderes e impulsionar carreiras na First Coast, Fl\u00f3rida.",
   f_about="Sobre", f_forums="F\u00f3runs e Eventos", f_get="Participe",
   f_reg="Inscri\u00e7\u00f5es (Eventbrite)", f_contact="Fale Conosco",
   f_charity_h="Parceiras Sem Fins Lucrativos",
   f_charity="Promovemos e apoiamos organiza\u00e7\u00f5es sem fins lucrativos que beneficiam mulheres na First Coast. <a href=\"./non-profit-partners.html\">Conhe\u00e7a nossas parceiras</a>.",
   f_copy="Copyright &copy; <span id=\"footer-year\">2026</span> Jacksonville Women's Leadership Forum | Todos os direitos reservados",
   disclosure_pre="<strong>Aviso legal da Fl\u00f3rida (mantido em ingl\u00eas por exig\u00eancia legal):</strong> ",
   lang_label="Idioma"),
}

# Small inline SVG flags (20x14). Decorative; button carries the aria-label.
FLAG_US = ('<svg viewBox="0 0 20 14" width="20" height="14" aria-hidden="true">'
 '<rect width="20" height="14" fill="#b22234"/>'
 '<g fill="#fff"><rect y="1.6" width="20" height="1.5"/><rect y="4.7" width="20" height="1.5"/>'
 '<rect y="7.8" width="20" height="1.5"/><rect y="10.9" width="20" height="1.5"/></g>'
 '<rect width="9" height="7.5" fill="#3c3b6e"/></svg>')
FLAG_MX = ('<svg viewBox="0 0 20 14" width="20" height="14" aria-hidden="true">'
 '<rect width="20" height="14" fill="#fff"/><rect width="6.7" height="14" fill="#006847"/>'
 '<rect x="13.3" width="6.7" height="14" fill="#ce1126"/>'
 '<circle cx="10" cy="7" r="1.8" fill="#8a6d3b"/></svg>')
FLAG_BR = ('<svg viewBox="0 0 20 14" width="20" height="14" aria-hidden="true">'
 '<rect width="20" height="14" fill="#009c3b"/>'
 '<polygon points="10,1.5 18.5,7 10,12.5 1.5,7" fill="#ffdf00"/>'
 '<circle cx="10" cy="7" r="2.6" fill="#002776"/></svg>')

def lang_switcher(lang, filename, sw=None):
    # Same filename exists in every language directory.
    sw = sw or filename
    if lang == "en":
        hrefs = {"en": f"./{filename}", "es": f"./es/{sw}", "pt": f"./pt/{sw}"}
    else:
        other = "pt" if lang == "es" else "es"
        hrefs = {"en": f"../{filename}", lang: f"./{filename}", other: f"../{other}/{filename}"}
    items = [
        ("en", FLAG_US, "English"),
        ("es", FLAG_MX, "Espa\u00f1ol"),
        ("pt", FLAG_BR, "Portugu\u00eas"),
    ]
    out = ""
    for code, flag, label in items:
        cur = ' aria-current="true" class="flag-link current"' if code == lang else ' class="flag-link"'
        out += f'<a href="{hrefs[code]}" hreflang="{code}" lang="{code}" aria-label="{label}"{cur}>{flag}</a>'
    return (f'<div class="lang-switch" role="group" aria-label="{L10N[lang]["lang_label"]}">{out}</div>')

def aria(active, href):
    return ' aria-current="page"' if active == href else ""

def header(active, lang, filename, sw=None):
    t = L10N[lang]["nav"]
    def sub(items, top_label=None, top_href=None, overview=None):
        s = ""
        if top_href:
            s += f'<li><a href="./{top_href}"{aria(active, top_href)}>{overview}</a></li>'
        s += "".join(f'<li><a href="./{h}"{aria(active, h)}>{l}</a></li>' for l, h in items)
        return s
    cta_label, cta_href = L10N[lang]["cta"]
    return f"""<a class="skip-link" href="#main">{L10N[lang]["skip"]}</a>
<header class="site-header">
  <div class="nav-bar">
    <a class="brand" href="./index.html" aria-label="Jacksonville Women's Leadership Forum">
      <img src="./images/jwlf-logo.png" alt="Jacksonville Women's Leadership Forum logo"
           onerror="this.style.display='none';this.nextElementSibling.style.display='inline'">
      <span class="brand-fallback" style="display:none">JWLF</span>
    </a>
    <button type="button" class="nav-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav id="site-nav" class="site-nav" aria-label="Primary">
      <ul>
        <li><a href="./index.html"{aria(active, "index.html")}>{t["home"]}</a></li>
        <li class="has-submenu">
          <button type="button" class="submenu-toggle" aria-expanded="false">{t["about"]} <span class="caret" aria-hidden="true">&#9662;</span></button>
          <ul class="submenu">{sub(t["about_sub"])}</ul>
        </li>
        <li class="has-submenu">
          <button type="button" class="submenu-toggle" aria-expanded="false">{t["forums"]} <span class="caret" aria-hidden="true">&#9662;</span></button>
          <ul class="submenu">{sub(t["forums_sub"])}</ul>
        </li>
        <li class="has-submenu">
          <button type="button" class="submenu-toggle" aria-expanded="false">{t["getinv"]} <span class="caret" aria-hidden="true">&#9662;</span></button>
          <ul class="submenu">{sub(t["getinv_sub"], top_href="get-involved.html", overview=t["overview"])}</ul>
        </li>
        <li><a href="./contact.html"{aria(active, "contact.html")}>{t["contact"]}</a></li>
        <li class="nav-cta"><a class="btn btn--primary" href="./{cta_href}">{cta_label}</a></li>
        <li>{lang_switcher(lang, filename, sw)}</li>
      </ul>
    </nav>
  </div>
</header>"""

def footer(lang):
    L = L10N[lang]
    t = L["nav"]
    about_links = "".join(f'<li><a href="./{h}">{l}</a></li>' for l, h in t["about_sub"])
    forums_links = "".join(f'<li><a href="./{h}">{l}</a></li>' for l, h in t["forums_sub"])
    get_links = "".join(f'<li><a href="./{h}">{l}</a></li>' for l, h in t["getinv_sub"])
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <h3>Jacksonville Women's Leadership Forum</h3>
        <p>{L["f_tag"]}</p>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <div class="footer-social">
          <a href="{FACEBOOK}" aria-label="Facebook">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 21v-8h2.7l.4-3h-3.1V8.1c0-.9.3-1.5 1.6-1.5h1.6V3.9c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4V10H7.8v3h2.7v8h3z"/></svg>
          </a>
          <a href="{LINKEDIN}" aria-label="LinkedIn">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4.98 3.5A2.49 2.49 0 1 1 5 8.48a2.49 2.49 0 0 1-.02-4.98zM3 9.75h4v11H3v-11zm6.5 0h3.8v1.5h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1v5.45h-4v-4.83c0-1.15-.02-2.63-1.6-2.63-1.6 0-1.85 1.25-1.85 2.55v4.91h-3.95v-11z"/></svg>
          </a>
          <a href="mailto:{EMAIL}" aria-label="Email">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h18a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zm9 7.3L4.4 7h15.2L12 12.3zM4 9.1V17h16V9.1l-8 5.2-8-5.2z"/></svg>
          </a>
        </div>
      </div>
      <div>
        <h3>{L["f_about"]}</h3>
        <ul>{about_links}</ul>
      </div>
      <div>
        <h3>{L["f_forums"]}</h3>
        <ul>{forums_links}<li><a href="{EVENTBRITE}">{L["f_reg"]}</a></li></ul>
      </div>
      <div>
        <h3>{L["f_get"]}</h3>
        <ul>{get_links}<li><a href="./contact.html">{L["f_contact"]}</a></li></ul>
        <h3 style="margin-top:1.25rem">{L["f_charity_h"]}</h3>
        <p style="font-size:0.875rem">{L["f_charity"]}</p>
      </div>
    </div>
    <p class="disclosure">{L["disclosure_pre"]}{DISCLOSURE}</p>
    <div class="footer-bottom"><p>{L["f_copy"]}</p></div>
  </div>
</footer>
<script src="./js/main.js"></script>"""

def page(filename, title, desc, body, active=None, lang="en", switch_to=None):
    L = L10N[lang]
    sw = switch_to or filename
    # hreflang alternates (same filename in each language dir)
    if lang == "en":
        alt = (f'<link rel="alternate" hreflang="en" href="./{filename}">'
               f'<link rel="alternate" hreflang="es" href="./es/{sw}">'
               f'<link rel="alternate" hreflang="pt-BR" href="./pt/{sw}">')
    else:
        other = "pt" if lang == "es" else "es"
        alt = (f'<link rel="alternate" hreflang="en" href="../{filename}">'
               f'<link rel="alternate" hreflang="{L["htmllang"]}" href="./{filename}">'
               f'<link rel="alternate" hreflang="{"pt-BR" if other=="pt" else "es"}" href="../{other}/{filename}">')
    html = f"""<!DOCTYPE html>
<html lang="{L["htmllang"]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Jacksonville Women's Leadership Forum</title>
<meta name="description" content="{desc}">
{alt}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="./css/style.css">
<link rel="icon" href="./images/jwlf-logo.png">
</head>
<body>
{header(active or filename, lang, filename, sw)}
<main id="main">
{body}
</main>
{footer(lang)}
</body>
</html>
"""
    if lang == "en":
        out = os.path.join(ROOT, filename)
    else:
        os.makedirs(os.path.join(ROOT, lang), exist_ok=True)
        # Rewrite shared-asset paths one directory up. Page-to-page links
        # (./x.html) stay untouched: every language dir has every page.
        for a in ("css/", "js/", "images/"):
            html = html.replace(f'"./{a}', f'"../{a}')
        out = os.path.join(ROOT, lang, filename)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", os.path.relpath(out, ROOT))

def page_hero(h1, sub=""):
    subhtml = f"<p>{sub}</p>" if sub else ""
    return f"""<div class="page-hero"><div class="hero-inner"><h1>{h1}</h1>{subhtml}</div></div>"""

if __name__ == "__main__":
    import pages1      # noqa: F401  EN: Home, About, Board, Partners, Gallery, Get Involved (+ placeholder news)
    import pages2      # noqa: F401  EN: Forums & Events
    import pages3      # noqa: F401  EN: Get Involved detail pages, Contact, image manifest
    import pages_blog  # noqa: F401  EN: Blog index (news.html) + article pages
    import pages_es    # noqa: F401  Spanish site in ./es/
    import pages_pt    # noqa: F401  Portuguese site in ./pt/
    print("Build complete.")
