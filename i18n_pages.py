# Builds a full localized site (all pages) from a translation dict T.
# Speaker biographies, blog articles, and the Florida legal disclosure remain
# in their original English (standard practice for quoted bios and legal text);
# each localized page says so where relevant.
from build import page, page_hero, EMAIL, EVENTBRITE, BROCHURE
from pages1 import OFFICERS, BOARD, PARTNERS, SPONSOR_LOGOS, logo_wall
from pages2 import TOPICS, PANELISTS, speaker_block, JANEAN, AMELIA, BURNS, LEWIS, PHILLIPS, SWIETEK
from pages3 import TIERS
from pages_blog import POSTS
from images_data import GALLERY, gallery_local


def build_lang(lang, T):
    P = lambda *a, **k: page(*a, lang=lang, **k)

    # ------------------------------------------------ people cards (roles localized lightly)
    def officer_cards():
        out = ""
        for (name, role, org, img, li), lrole in zip(OFFICERS, T["officer_roles"]):
            out += f"""<div class="card person-card" data-reveal>
  <img class="person-photo" src="./{img}" alt="{name}" loading="lazy" width="132" height="132">
  <h3>{name}</h3><p class="person-role">{lrole}</p><p class="person-org">{org}</p>
  <a href="{li}">LinkedIn</a></div>"""
        return out

    def board_cards():
        out = ""
        for name, role, org, img, li, first in BOARD:
            out += f"""<div class="card person-card" data-reveal>
  <img class="person-photo" src="./{img}" alt="{name.split(',')[0]}" loading="lazy" width="132" height="132">
  <h3>{name.split(',')[0]}</h3><p class="person-role">{role}</p><p class="person-org">{org}</p>
  <a href="{li}">LinkedIn</a></div>"""
        return out

    # ------------------------------------------------ HOME
    pillars = "".join(f'<div class="card pillar-card" data-reveal><h3>{h}</h3><p>{b}</p></div>'
                      for h, b in T["pillars"])
    quotes = "".join(f"""<div class="card quote-card" data-reveal><blockquote>\u201c{q}\u201d</blockquote>
<cite><strong>{who}</strong>, {org} <span class="person-org">({T["translated_note"]})</span></cite></div>"""
                     for q, who, org in T["testimonials"])
    home = f"""
<div class="hero">
  <img class="hero-img" src="./images/photos/hero.jpg" alt="" aria-hidden="true">
  <div class="hero-inner">
    <h1>{T["hero_h1"]}</h1>
    <p>{T["hero_p"]}</p>
    <div class="btn-row">
      <a class="btn btn--gold" href="./forum.html">{T["hero_cta1"]}</a>
      <a class="btn btn--outline" href="./sponsorship.html">{T["hero_cta2"]}</a>
    </div>
  </div>
</div>
<section class="section"><div class="container">
  <h2>{T["welcome_h"]}</h2>
  <p class="lede">{T["welcome_p"]}</p>
  <div class="grid grid--4 mt-2">{pillars}</div>
</div></section>
<section class="theme-band"><div class="container">
  <p class="theme-line">{T["theme_pre"]}</p>
  <h2>Presence with Purpose</h2>
  <p class="theme-line">{T["theme_line"]}</p>
  <p class="status">{T["theme_status"]}</p>
  <a class="btn btn--gold" href="{EVENTBRITE}">{T["theme_btn"]}</a>
</div></section>
<section class="section"><div class="container two-col">
  <div>
    <h2>{T["who_h"]}</h2>
    <ul>{''.join(f'<li>{x}</li>' for x in T["who_items"])}</ul>
    <div class="btn-row"><a class="btn btn--primary" href="./forum.html">{T["who_btn"]}</a></div>
  </div>
  <div class="photo-strip" style="grid-template-columns:1fr">
    <img src="./images/photos/about-1.jpg" alt="{T["alt_networking"]}" loading="lazy">
    <img src="./images/photos/about-3.jpg" alt="{T["alt_speaker"]}" loading="lazy">
  </div>
</div></section>
<section class="section section--tint"><div class="container">
  <h2>{T["testimonials_h"]}</h2>
  <div class="grid grid--3">{quotes}</div>
</div></section>
<section class="section"><div class="container">
  <h2>{T["officers_h"]}</h2>
  <div class="grid grid--4">{officer_cards()}</div>
  <div class="btn-row"><a class="btn btn--outline" href="./board.html">{T["officers_btn"]}</a></div>
</div></section>
<section class="section section--tint"><div class="container">
  <h2>{T["sponsors_h"]}</h2>
  <p class="lede">{T["sponsors_p"]}</p>
  {logo_wall()}
  <div class="btn-row"><a class="btn btn--primary" href="./sponsorship.html">{T["sponsors_btn"]}</a></div>
</div></section>
<section class="section cta-band"><div class="container">
  <h2>{T["cta_h"]}</h2><p>{T["cta_p"]}</p>
  <div class="btn-row">
    <a class="btn btn--gold" href="{EVENTBRITE}">{T["cta_reg"]}</a>
    <a class="btn btn--light" href="./sponsorship.html">{T["cta_sponsor"]}</a>
    <a class="btn btn--outline" href="./donate.html">{T["cta_donate"]}</a>
  </div>
</div></section>"""
    P("index.html", T["t_home"], T["d_home"], home)

    # ------------------------------------------------ GET INVOLVED hub
    gi = page_hero(T["gi_h"], T["gi_sub"]) + f"""
<section class="section"><div class="container"><div class="grid grid--4">
  <div class="card" data-reveal><h3>{T["gi_sponsor_h"]}</h3><p>{T["gi_sponsor_p"]}</p>
    <a class="btn btn--primary" href="./sponsorship.html">{T["gi_sponsor_h"]}</a></div>
  <div class="card" data-reveal><h3>{T["gi_vol_h"]}</h3><p>{T["gi_vol_p"]}</p>
    <a class="btn btn--primary" href="./volunteer.html">{T["gi_vol_h"]}</a></div>
  <div class="card" data-reveal><h3>{T["gi_wolf_h"]}</h3><p>{T["gi_wolf_p"]}</p>
    <a class="btn btn--primary" href="./wolf-award.html">{T["gi_wolf_h"]}</a></div>
  <div class="card" data-reveal><h3>{T["gi_don_h"]}</h3><p>{T["gi_don_p"]}</p>
    <a class="btn btn--primary" href="./donate.html">{T["gi_don_h"]}</a></div>
</div></div></section>"""
    P("get-involved.html", T["t_gi"], T["d_gi"], gi)

    # ------------------------------------------------ ABOUT
    about = page_hero(T["about_h"], T["about_sub"]) + f"""
<section class="section"><div class="container two-col">
  <div>
    <h2>{T["about_who_h"]}</h2>{T["about_body"]}
    <div class="btn-row"><a class="btn btn--primary" href="./sponsorship.html">{T["sponsors_btn"]}</a>
    <a class="btn btn--outline" href="./donate.html">{T["cta_donate"]}</a></div>
  </div>
  <div class="photo-strip" style="grid-template-columns:1fr">
    <img src="./images/photos/about-1.jpg" alt="{T["alt_networking"]}" loading="lazy">
    <img src="./images/photos/about-2.jpg" alt="{T["alt_networking"]}" loading="lazy">
  </div>
</div></section>"""
    P("about.html", T["t_about"], T["d_about"], about)

    # ------------------------------------------------ CHAIR MESSAGE
    chair = page_hero(T["chair_h"]) + f"""
<section class="section"><div class="container two-col">
  <div>{T["chair_body"]}
    <p><strong>Cari Smith</strong><br>{T["chair_sig"]}</p></div>
  <div><img src="./images/people/cari-smith.jpg" alt="Cari Smith" style="border-radius:10px; max-width:360px" loading="lazy"></div>
</div></section>"""
    P("message-from-chair.html", T["t_chair"], T["d_chair"], chair)

    # ------------------------------------------------ BOARD
    board = page_hero(T["board_h"], T["board_sub"]) + f"""
<section class="section"><div class="container">
  <h2>{T["board_dir_h"]}</h2>
  <p class="notice">{T["titles_note"]}</p>
  <div class="grid grid--4 mt-2">{board_cards()}</div>
</div></section>
<section class="section section--tint"><div class="container">
  <h2>{T["board_off_h"]}</h2><div class="grid grid--4">{officer_cards()}</div>
</div></section>"""
    P("board.html", T["t_board"], T["d_board"], board)

    # ------------------------------------------------ PARTNERS
    pcards = ""
    for (name, img, link, _), desc in zip(PARTNERS, T["partner_descs"]):
        link_html = (f'<a href="{link}">{T["partner_more"]}</a>' if link
                     else f'<a href="./contact.html">{T["partner_contact"]}</a>')
        pcards += f"""<div class="card partner-card" data-reveal>
  <div class="logo-tile"><img src="./{img}" alt="{name}" loading="lazy"></div>
  <h3>{name}</h3><p>{desc}</p><p>{link_html}</p></div>"""
    partners = page_hero(T["partners_h"], T["partners_sub"]) + f"""
<section class="section"><div class="container">
  <div class="grid grid--3">{pcards}</div>
  <div class="btn-row"><a class="btn btn--primary" href="./contact.html">{T["partners_btn"]}</a></div>
</div></section>"""
    P("non-profit-partners.html", T["t_partners"], T["d_partners"], partners)

    # ------------------------------------------------ GALLERY
    by_year = {}
    for year, url in GALLERY:
        by_year.setdefault(year, []).append(url)
    sections = ""
    for year in sorted(by_year, reverse=True):
        items = "".join(
            f'<a href="./{gallery_local(year,u)}"><img src="./{gallery_local(year,u)}" alt="{T["gallery_alt"].format(year=year)}" loading="lazy"></a>'
            for u in by_year[year])
        sections += f'<div class="gallery-year"><h2>{T["gallery_year"].format(year=year)}</h2><div class="gallery-grid">{items}</div></div>'
    gallery = page_hero(T["gallery_h"], T["gallery_sub"]) + f"""
<section class="section"><div class="container">{sections}</div></section>
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="{T["gallery_h"]}">
  <button type="button" class="lightbox-close" aria-label="{T["lb_close"]}">&times;</button>
  <button type="button" class="lightbox-prev" aria-label="{T["lb_prev"]}">&#8249;</button>
  <img src="" alt="">
  <button type="button" class="lightbox-next" aria-label="{T["lb_next"]}">&#8250;</button>
  <p class="lightbox-caption"></p>
</div>"""
    P("gallery.html", T["t_gallery"], T["d_gallery"], gallery)

    # ------------------------------------------------ BLOG index (articles remain in English)
    cards = "".join(f"""<article class="card card--flush" data-reveal>
  <img class="card-photo" src="./{p["img"]}" alt="{p["img_alt"]}" loading="lazy">
  <div class="card-body"><h3><a href="../{p["slug"]}">{p["title"]}</a></h3>
  <p class="person-org">{p["date"]}</p><a href="../{p["slug"]}">{T["blog_read"]}</a></div></article>"""
        for p in POSTS)
    blog = page_hero(T["blog_h"], T["blog_sub"]) + f"""
<section class="section"><div class="container">
  <p class="notice">{T["blog_note"]}</p>
  <div class="grid grid--3 mt-2">{cards}</div>
</div></section>"""
    P("news.html", T["t_blog"], T["d_blog"], blog)

    # ------------------------------------------------ FORUM
    forum = page_hero(T["forum_h"], T["forum_sub"]) + f"""
<section class="theme-band"><div class="container">
  <p class="theme-line">{T["theme_pre"]}</p><h2>Presence with Purpose</h2>
  <p class="theme-line">{T["theme_line"]}</p><p class="status">{T["theme_status"]}</p>
  <a class="btn btn--gold" href="{EVENTBRITE}">{T["theme_btn"]}</a>
</div></section>
<section class="section"><div class="container two-col">
  <div>
    <h2>{T["forum26_h"]}</h2><p>{T["forum26_p"]}</p>
    <p><strong>\u201cShe Leads: Igniting, Elevating Voice, and Delivering Value\u201d</strong></p>
    <p><a href="./speakers.html">{T["forum26_link"]}</a></p>
    <h2 class="mt-2">{T["who_h"]}</h2>
    <ul>{''.join(f'<li>{x}</li>' for x in T["who_items"])}</ul>
  </div>
  <div>
    <img src="./images/photos/forum-2016.jpg" alt="{T["alt_networking"]}" style="border-radius:10px" loading="lazy">
    <div class="card mt-2"><h3>{T["idea_h"]}</h3><p>{T["idea_p"]}</p>
      <a class="btn btn--primary" href="./contact.html">{T["idea_btn"]}</a></div>
  </div>
</div></section>"""
    P("forum.html", T["t_forum"], T["d_forum"], forum)

    # ------------------------------------------------ SPEAKERS (bios stay in English)
    speakers = page_hero(T["speakers_h"], T["speakers_sub"]) + f"""
<section class="section"><div class="container">
  <p class="notice">{T["bios_note"]}</p>
  <h2 class="mt-2">{T["speakers_key_h"]}</h2>
  {speaker_block("Janean C. Armstrong", "Author and Seasoned Banking Executive", "images/people/janean-armstrong.jpg", JANEAN)}
  <div class="mb-2"></div>
  {speaker_block("Amelia Rose Earhart", "Aviator, Author, and Founder of the Flying with Amelia Foundation", "images/people/amelia-rose-earhart.jpg", AMELIA)}
  <h2 class="mt-2">{T["speakers_pan_h"]}</h2>
  {speaker_block("Michael Burns", "SVP, Chief Legal Officer and Corporate Secretary, CSX", "images/people/michael-burns.jpg", BURNS)}
  <div class="mb-2"></div>
  {speaker_block("Terri Lewis", "VP, Chief Human Resources Officer, Landstar Systems", "images/people/terri-lewis.jpg", LEWIS)}
  <div class="mb-2"></div>
  {speaker_block("Ted Phillips", "Chief Financial Officer, JEA", "images/people/ted-phillips.jpg", PHILLIPS)}
  <div class="mb-2"></div>
  {speaker_block("Taryn Swietek", "Head of Governance \u2013 gTech, Google", "images/people/taryn-swietek.jpg", SWIETEK)}
</div></section>"""
    P("speakers.html", T["t_speakers"], T["d_speakers"], speakers)

    # ------------------------------------------------ PREVIOUS SPEAKERS (topics + link to EN bios)
    topics_html = "".join(f"<li><strong>{y}</strong> \u2014 {t}</li>" for y, t in TOPICS)
    panelist_items = "".join(f"<li>{p}</li>" for p in PANELISTS)
    prev = page_hero(T["prev_h"], T["prev_sub"]) + f"""
<section class="section"><div class="container">
  <h2>{T["prev_topics_h"]}</h2>
  <p class="notice">{T["topics_note"]}</p>
  <ul style="list-style:none; padding:0" class="mt-2">{topics_html}</ul>
  <p><a class="btn btn--outline" href="../previous-speakers.html">{T["prev_bios_btn"]}</a></p>
</div></section>
<section class="section section--tint"><div class="container">
  <h2>{T["prev_pan_h"]}</h2><ul class="name-columns">{panelist_items}</ul>
</div></section>"""
    P("previous-speakers.html", T["t_prev"], T["d_prev"], prev)

    # ------------------------------------------------ SPONSORSHIP
    tier_cards = ""
    for (name, price, perks), lname in zip(TIERS, T["tier_names"]):
        items = "".join(f"<li>{T['perk_map'].get(p, p)}</li>" for p in perks)
        tier_cards += f'<div class="card tier-card" data-reveal><h3>{lname}</h3><p class="price">{price}</p><ul>{items}</ul></div>'
    sponsorship = page_hero(T["sp_h"], T["sp_sub"]) + f"""
<section class="section"><div class="container">
  <p class="lede">{T["sp_p1"]}</p><p class="lede">{T["sp_p2"]}</p>
  <div class="card quote-card mt-2" style="max-width:52rem" data-reveal>
    <blockquote>\u201c{T["sp_quote"]}\u201d</blockquote>
    <cite><strong>Debbie Mills</strong>, General Manager, Mercedes Benz of Orange Park <span class="person-org">({T["translated_note"]})</span></cite>
  </div>
</div></section>
<section class="section section--tint"><div class="container">
  <h2>{T["sp_pkg_h"]}</h2>
  <p>{T["sp_pkg_p"]} <a href="{BROCHURE}">{T["sp_brochure"]}</a></p>
  <div class="grid grid--3">{tier_cards}</div>
</div></section>
<section class="section"><div class="container">
  <h2>{T["sp_form_h"]}</h2>
  <p>{T["sp_form_p"]} <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  <form class="form" data-validate action="#" method="POST" novalidate>
    <div class="form-row"><label for="sp-name">{T["f_name"]} <span class="req">*</span></label>
      <input id="sp-name" name="name" type="text" required><p class="field-error">{T["e_name"]}</p></div>
    <div class="form-row"><label for="sp-company">{T["f_company"]} <span class="req">*</span></label>
      <input id="sp-company" name="company" type="text" required><p class="field-error">{T["e_company"]}</p></div>
    <div class="form-row"><label for="sp-email">{T["f_email"]} <span class="req">*</span></label>
      <input id="sp-email" name="email" type="email" required><p class="field-error">{T["e_email"]}</p></div>
    <div class="form-row"><label for="sp-message">{T["f_message"]} <span class="req">*</span></label>
      <textarea id="sp-message" name="message" required></textarea><p class="field-error">{T["e_message"]}</p></div>
    <button class="btn btn--primary" type="submit">{T["f_send"]}</button>
    <p class="form-note">{T["f_demo"]}</p>
  </form>
  <div class="form-success" role="status">{T["f_success"]}</div>
</div></section>
<section class="section section--tint"><div class="container">
  <h2>{T["sp_logos_h"]}</h2>{logo_wall()}
</div></section>"""
    P("sponsorship.html", T["t_sp"], T["d_sp"], sponsorship)

    # ------------------------------------------------ VOLUNTEER
    volunteer = page_hero(T["vol_h"], T["vol_sub"]) + f"""
<section class="section"><div class="container">
  <p class="lede">{T["vol_p"]}</p>
  <div class="grid grid--3 mt-2">
    <div class="card" data-reveal><h3>{T["vol_c1_h"]}</h3><p>{T["vol_c1_p"]}</p></div>
    <div class="card" data-reveal><h3>{T["vol_c2_h"]}</h3><p>{T["vol_c2_p"]}</p></div>
    <div class="card" data-reveal><h3>{T["vol_c3_h"]}</h3><p>{T["vol_c3_p"]}</p></div>
  </div>
</div></section>
<section class="section section--tint"><div class="container">
  <h2>{T["vol_form_h"]}</h2>
  <form class="form" data-validate action="#" method="POST" novalidate>
    <div class="form-row"><label for="v-name">{T["f_name"]} <span class="req">*</span></label>
      <input id="v-name" name="name" type="text" required><p class="field-error">{T["e_name"]}</p></div>
    <div class="form-row"><label for="v-email">{T["f_email"]} <span class="req">*</span></label>
      <input id="v-email" name="email" type="email" required><p class="field-error">{T["e_email"]}</p></div>
    <div class="form-row"><label for="v-message">{T["vol_f_msg"]} <span class="req">*</span></label>
      <textarea id="v-message" name="message" required></textarea><p class="field-error">{T["e_message"]}</p></div>
    <button class="btn btn--primary" type="submit">{T["f_send"]}</button>
    <p class="form-note">{T["f_demo"]}</p>
  </form>
  <div class="form-success" role="status">{T["f_success"]}</div>
</div></section>"""
    P("volunteer.html", T["t_vol"], T["d_vol"], volunteer)

    # ------------------------------------------------ WOLF AWARD
    wolf = page_hero(T["wolf_h"], T["wolf_sub"]) + f"""
<section class="section"><div class="container">
  <p class="lede">{T["wolf_p1"]}</p>
  <h2 class="mt-2">{T["wolf_crit_h"]}</h2><p>{T["wolf_crit_p"]}</p>
  <div class="grid grid--3 mt-2">
    <div class="card" data-reveal><h3>{T["wolf_c1_h"]}</h3><p>{T["wolf_c1_p"]}</p></div>
    <div class="card" data-reveal><h3>{T["wolf_c2_h"]}</h3><p>{T["wolf_c2_p"]}</p></div>
    <div class="card" data-reveal><h3>{T["wolf_c3_h"]}</h3><p>{T["wolf_c3_p"]}</p></div>
  </div>
</div></section>
<section class="section cta-band"><div class="container">
  <h2>{T["wolf_cta_h"]}</h2><p>{T["wolf_cta_p"]}</p>
  <div class="btn-row"><a class="btn btn--gold" href="mailto:{EMAIL}?subject=WoLF%20Award%20Nomination">{T["wolf_cta_btn"]}</a></div>
</div></section>"""
    P("wolf-award.html", T["t_wolf"], T["d_wolf"], wolf)

    # ------------------------------------------------ DONATE
    donate = page_hero(T["don_h"], T["don_sub"]) + f"""
<section class="section"><div class="container two-col">
  <div>
    <h2>{T["don_body_h"]}</h2><p class="lede">{T["don_p"]}</p>
    <div class="btn-row">
      <a class="btn btn--primary" href="https://www.paypal.com/donate/?hosted_button_id=REPLACE_WITH_JWLF_BUTTON_ID">{T["don_btn"]}</a>
      <a class="btn btn--outline" href="./contact.html">{T["don_q"]}</a>
    </div>
  </div>
  <div>
    <div class="card"><h3>{T["don_where_h"]}</h3><p>{T["don_where_p"]}</p></div>
  </div>
</div></section>"""
    P("donate.html", T["t_don"], T["d_don"], donate)

    # ------------------------------------------------ CONTACT
    contact = page_hero(T["con_h"], T["con_sub"]) + f"""
<section class="section"><div class="container two-col">
  <div>
    <h2>{T["con_form_h"]}</h2>
    <p>{T["con_p"]} <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    <form class="form" data-validate action="#" method="POST" novalidate>
      <div class="form-row"><label for="c-name">{T["f_name"]} <span class="req">*</span></label>
        <input id="c-name" name="name" type="text" required><p class="field-error">{T["e_name"]}</p></div>
      <div class="form-row"><label for="c-email">{T["f_email"]} <span class="req">*</span></label>
        <input id="c-email" name="email" type="email" required><p class="field-error">{T["e_email"]}</p></div>
      <div class="form-row"><label for="contact-subject">{T["f_subject"]}</label>
        <input id="contact-subject" name="subject" type="text"></div>
      <div class="form-row"><label for="c-message">{T["f_message"]} <span class="req">*</span></label>
        <textarea id="c-message" name="message" required></textarea><p class="field-error">{T["e_message"]}</p></div>
      <button class="btn btn--primary" type="submit">{T["f_send"]}</button>
      <p class="form-note">{T["f_demo"]}</p>
    </form>
    <div class="form-success" role="status">{T["f_success"]}</div>
  </div>
  <div>
    <div class="card"><h3>{T["con_follow_h"]}</h3>
      <ul style="list-style:none; padding:0">
        <li><a href="https://www.facebook.com/JaxWLF/">Facebook</a></li>
        <li><a href="https://www.linkedin.com/groups/4252397">LinkedIn</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      </ul></div>
  </div>
</div></section>"""
    P("contact.html", T["t_con"], T["d_con"], contact)
