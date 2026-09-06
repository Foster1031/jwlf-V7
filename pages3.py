# Sponsorship, Volunteer, WoLF Award, Donate, Contact + image manifest & download script
import os
from build import page, page_hero, EMAIL, EVENTBRITE, BROCHURE, DISCLOSURE, ROOT
from images_data import IMAGES
from pages1 import logo_wall

# ============================================================== SPONSORSHIP
TIERS = [
    ("Visionary Sponsorship", "$10,000", [
        "20 tickets to the Annual JWLF Forum",
        "Company recognition at JWLF Forum as highest-level sponsor",
        "Company logo included on all JWLF promotional and marketing materials (prominent position)",
        "Discounted rate for company participants to attend JWLF programming held throughout the year",
        "Opportunity to provide swag at all events",
        "Company full-page ad in JWLF event program",
        "Opportunity for company showcase or speaker at educational events",
        "Two sponsor board of director seats",
        "Group photo of company attendees at the Annual JWLF Forum",
        "Opportunity to provide panelist at JWLF Forum",
        "Opportunity to \u201cown\u201d your part in the JWLF Forum (luncheon, breakfast)"]),
    ("Champion Sponsorship", "$7,500", [
        "16 tickets to the Annual JWLF Forum",
        "Company recognition at JWLF Forum",
        "Company logo included on all JWLF promotional and marketing materials",
        "Discounted rate for company participants to attend JWLF programming held throughout the year",
        "Opportunity to provide swag at all events",
        "Company full-page ad in JWLF event program",
        "Opportunity for company showcase or speaker at educational events",
        "Two sponsor board of director seats",
        "Group photo of company attendees at the Annual JWLF Forum",
        "Opportunity to provide panelist at JWLF Forum"]),
    ("Ambassador Sponsorship", "$5,000", [
        "14 tickets to the Annual JWLF Forum",
        "Company recognition at JWLF Forum as sponsor",
        "Company logo included on all JWLF promotional and marketing materials",
        "Discounted rate for company participants to attend JWLF programming held throughout the year",
        "Opportunity to provide swag at all events",
        "Company full-page ad in JWLF event program",
        "Opportunity for company showcase or speaker at educational events",
        "Two sponsor board of director seats",
        "Group photo of company attendees at the Annual JWLF Forum"]),
    ("Advocate Sponsorship", "$3,000", [
        "4 tickets to the Annual JWLF Forum",
        "Company recognition at JWLF Forum as sponsor",
        "Company logo included on all JWLF promotional and marketing materials",
        "Discounted rate for company participants to attend JWLF programming held throughout the year",
        "Opportunity to provide swag at all events",
        "Company half-page ad in JWLF event program"]),
    # NOTE: "$7,500" for Supporter matches the live site verbatim but looks like a
    # typo (it duplicates Champion) — flagged for review in MIGRATION-CHECKLIST.md.
    ("Supporter Sponsorship", "$7,500", [
        "4 tickets to the Annual JWLF Forum",
        "Company recognition at JWLF Forum",
        "Company logo included on all JWLF promotional and marketing materials (prominent position)",
        "Discounted rate for company participants to attend JWLF programming held throughout the year",
        "Opportunity to provide swag at all events",
        "Company full-page ad in JWLF event program",
        "Opportunity to \u201cown\u201d your part in the JWLF Forum (pre-event reception, post-event social)"]),
]
tier_cards = ""
for name, price, perks in TIERS:
    items = "".join(f"<li>{p}</li>" for p in perks)
    tier_cards += f"""<div class="card tier-card" data-reveal>
  <h3>{name}</h3>
  <p class="price">{price}</p>
  <ul>{items}</ul>
</div>"""

sponsorship_body = page_hero("Sponsorship Information",
    "Position your brand, message, and company representative among an ideal demographic of professional and leadership-minded women.") + f"""
<section class="section">
  <div class="container">
    <h2>JWLF Sponsorship Opportunities</h2>
    <p class="lede">The Jacksonville Women\u2019s Leadership Forum offers a variety of innovative and affordable
    sponsorships and recognition opportunities. Ensure that your brand, message and even your company
    representative is successfully positioned among an ideal demographic of professional and leadership-minded
    women.</p>
    <p class="lede">Over 150 executive women, from various large, locally-based companies attend the annual
    Jacksonville Women\u2019s Leadership Forum networking events and Forum, and receive world-class leadership
    training in the process.</p>
    <div class="card quote-card mt-2" style="max-width:52rem" data-reveal>
      <blockquote>\u201cIt\u2019s been a wonderful partnership between JWLF and Mercedes Benz of Orange Park and
      Jacksonville. As a long-term JWLF networking event sponsor, we have been able to showcase our automobiles to
      the attendees, share the Mercedes Benz message of the priority we place on our female customers and
      we\u2019ve seen a tangible return on our investment. We are delighted that several JWLF members and attendees
      are now proud owners of Mercedes Benz automobiles!\u201d</blockquote>
      <cite><strong>Debbie Mills</strong>, General Manager, Mercedes Benz of Orange Park</cite>
    </div>
    <div class="photo-strip mt-2">
      <img src="./images/photos/sponsor-1.jpg" alt="Sponsors and attendees at the 2026 JWLF Forum" loading="lazy">
      <img src="./images/photos/sponsor-2.jpg" alt="Networking at the 2026 JWLF Forum" loading="lazy">
      <img src="./images/photos/sponsor-3.jpg" alt="A session at the 2025 Women's Leadership Forum" loading="lazy">
    </div>
  </div>
</section>
<section class="section section--tint">
  <div class="container">
    <h2>Sponsorship Packages</h2>
    <p>Explore our opportunities \u2014 and if you don\u2019t see a package that fits the needs of your organization,
    contact us. We are always open to working with our partners to create a custom package that helps develop
    long-lasting and impactful relationships that benefit both our sponsors and our attendees.
    <a href="{BROCHURE}">Download the sponsorship brochure (PDF)</a> for more information.</p>
    <div class="grid grid--3">{tier_cards}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <h2 id="sponsor-inquiry">Become a Sponsor</h2>
    <p>Thank you for your interest in becoming a sponsor. Please fill out the form below to learn about becoming a
    sponsor, or email us at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    <!-- To go live: point action at your Formspree endpoint and see js/main.js ("GOING LIVE WITH FORMSPREE"). -->
    <form class="form" data-validate action="#" method="POST" novalidate>
      <div class="form-row">
        <label for="sp-name">Name <span class="req" aria-hidden="true">*</span></label>
        <input id="sp-name" name="name" type="text" autocomplete="name" required>
        <p class="field-error">Please enter your name.</p>
      </div>
      <div class="form-row">
        <label for="sp-company">Company <span class="req" aria-hidden="true">*</span></label>
        <input id="sp-company" name="company" type="text" autocomplete="organization" required>
        <p class="field-error">Please enter your company.</p>
      </div>
      <div class="form-row">
        <label for="sp-email">Email <span class="req" aria-hidden="true">*</span></label>
        <input id="sp-email" name="email" type="email" autocomplete="email" required>
        <p class="field-error">Please enter a valid email address.</p>
      </div>
      <div class="form-row">
        <label for="sp-phone">Phone</label>
        <input id="sp-phone" name="phone" type="tel" autocomplete="tel">
      </div>
      <div class="form-row">
        <label for="sp-pref">How should we contact you?</label>
        <select id="sp-pref" name="contact_preference">
          <option>Contact via email</option>
          <option>Contact via phone</option>
        </select>
      </div>
      <div class="form-row">
        <label for="sp-message">Comment or message <span class="req" aria-hidden="true">*</span></label>
        <textarea id="sp-message" name="message" required></textarea>
        <p class="field-error">Please include a short message.</p>
      </div>
      <button class="btn btn--primary" type="submit">Send sponsor inquiry</button>
      <p class="form-note">This form is in demo mode \u2014 submissions are validated in your browser but not yet
      sent anywhere.</p>
    </form>
    <div class="form-success" role="status">Thank you for your interest in sponsoring JWLF! This demo confirms your
    message validated correctly. Once the form is connected to Formspree, it will reach our team directly \u2014 in
    the meantime, please email <a href="mailto:{EMAIL}">{EMAIL}</a>.</div>
  </div>
</section>
<section class="section section--tint">
  <div class="container">
    <h2>We Are Proud to Recognize Our Previous and Current Sponsors</h2>
    {logo_wall()}
  </div>
</section>
"""
page("sponsorship.html", "Sponsorship Information",
     "Sponsorship packages and opportunities with the Jacksonville Women's Leadership Forum.",
     sponsorship_body)

# ============================================================== VOLUNTEER
volunteer_body = page_hero("Volunteer",
    "We welcome women who would like to volunteer their time, talent and treasure to JWLF.") + f"""
<section class="section">
  <div class="container">
    <p class="lede">Our program relies on dedicated volunteers to promote its mission. If you have a talent you can
    contribute, let us know what it is and we will work with you on how to have a meaningful volunteer service. We
    can always use volunteers in the following categories:</p>
    <div class="grid grid--3 mt-2">
      <div class="card" data-reveal>
        <h3>Promotion</h3>
        <p>Volunteer your support by promoting JWLF through social media sites and/or by assisting with newsletter
        content.</p>
      </div>
      <div class="card" data-reveal>
        <h3>Event Support</h3>
        <p>Help us get our event venues ready for guests and/or volunteer your time to assist during the event.</p>
      </div>
      <div class="card" data-reveal>
        <h3>Forum Content</h3>
        <p>Help us locate and research potential future speakers, forum topics, and/or local non-profit
        partners.</p>
      </div>
    </div>
  </div>
</section>
<section class="section section--tint">
  <div class="container">
    <h2>Sign Up to Volunteer</h2>
    <!-- To go live: point action at your Formspree endpoint and see js/main.js ("GOING LIVE WITH FORMSPREE"). -->
    <form class="form" data-validate action="#" method="POST" novalidate>
      <div class="form-row">
        <label for="v-name">Your name <span class="req" aria-hidden="true">*</span></label>
        <input id="v-name" name="name" type="text" autocomplete="name" required>
        <p class="field-error">Please enter your name.</p>
      </div>
      <div class="form-row">
        <label for="v-email">Your email <span class="req" aria-hidden="true">*</span></label>
        <input id="v-email" name="email" type="email" autocomplete="email" required>
        <p class="field-error">Please enter a valid email address.</p>
      </div>
      <div class="form-row">
        <label for="v-phone">Phone</label>
        <input id="v-phone" name="phone" type="tel" autocomplete="tel">
      </div>
      <div class="form-row">
        <label for="v-message">How would you like to help? <span class="req" aria-hidden="true">*</span></label>
        <textarea id="v-message" name="message" required></textarea>
        <p class="field-error">Please tell us how you\u2019d like to help.</p>
      </div>
      <button class="btn btn--primary" type="submit">Send volunteer interest</button>
      <p class="form-note">This form is in demo mode \u2014 submissions are validated in your browser but not yet
      sent anywhere.</p>
    </form>
    <div class="form-success" role="status">Thank you for offering your time and talent! This demo confirms your
    message validated correctly. Once connected to Formspree it will reach our team \u2014 in the meantime, please
    email <a href="mailto:{EMAIL}">{EMAIL}</a>.</div>
  </div>
</section>
"""
page("volunteer.html", "Volunteer",
     "Volunteer your time and talent with the Jacksonville Women's Leadership Forum.",
     volunteer_body)

# ============================================================== WOLF AWARD
wolf_body = page_hero("The WoLF Award",
    "Recognizing one outstanding woman in our community each year.") + f"""
<section class="section">
  <div class="container">
    <p class="lede">The WoLF Award was created to recognize one outstanding woman in our community each year.
    Intentionally so, a strong link exists between JWLF and WoLF, as demonstrated by certain key attributes. Wolves
    are highly intelligent, social animals who draw their strength from interaction with one another and share a
    common sense of purpose: to ensure the survival of the pack. As a member of the pack family, each adult wolf
    assumes responsibility for providing care, food, shelter, training, protection and play as they embrace the
    fact that the future of the pack is in the hands of their young. They act strategically and with a sense of
    shared purpose.</p>
    <h2 class="mt-2">WoLF Award Nomination Criteria</h2>
    <p>The WoLF Award recipient will be a woman in our community who has demonstrated these attributes in an
    extraordinary way. We have identified the following attributes for consideration: intelligence, loyalty,
    survival, discipline, communication, compassion, family, teamwork, and work/life balance.</p>
    <div class="grid grid--3 mt-2">
      <div class="card" data-reveal>
        <h3>Loyalty, Survival and Family</h3>
        <p>No other mammal shows more spirited devotion to its family, organization or social group than the wolf.
        A wolf\u2019s purpose for existing is to ensure the survival of the pack. Where the pups are concerned, each
        member of the pack assumes the responsibility for food, shelter, training, protection and play. The pack
        always knows the young are their future.</p>
      </div>
      <div class="card" data-reveal>
        <h3>Discipline, Compassion, and Work/Life Balance</h3>
        <p>Wolves are very social animals that draw their strength from physical contact with each other. Play
        refines their skills of communication, teamwork and hunting. They become physically stronger and mentally
        tougher through play. Wolves do not aimlessly choose or harass their prey. They are keen observers,
        analyzing the physical and mental state of each member of the caribou herd. When they do attack it is with
        purpose \u2014 they are aware that one well-placed hoof of a caribou can kill a member of their pack. The
        wolf seeks long-term victory rather than short-term success.</p>
      </div>
      <div class="card" data-reveal>
        <h3>Intelligence, Teamwork and Communication</h3>
        <p>Not every member of the pack aspires to be the boss. Some prefer to be hunters, caretakers or scouts.
        But each has a crucial role to play as part of the team. Wolves don\u2019t rely upon any single form of
        communication. They howl, nuzzle, lick and use intricate body language including lips, eyes, and their tail
        position. As they hunt, the situation changes by the second and these different communication techniques
        allow the pack to constantly adjust their strategy to achieve success.</p>
      </div>
    </div>
  </div>
</section>
<section class="section cta-band">
  <div class="container">
    <h2>Nominate a WoLF</h2>
    <p>If you know a woman in our community who exhibits the characteristics above, has achieved something
    monumental, or values these attributes and acts accordingly, please consider nominating her for our next WoLF
    Award. WoLF Awards are given every May during our Annual Forum. To make a nomination, please submit a candidate
    and bio to <a href="mailto:{EMAIL}" style="color:#fff">{EMAIL}</a>.</p>
    <div class="btn-row"><a class="btn btn--gold" href="mailto:{EMAIL}?subject=WoLF%20Award%20Nomination">Submit a Nomination</a></div>
  </div>
</section>
"""
page("wolf-award.html", "WoLF Award",
     "The JWLF WoLF Award recognizes one outstanding woman in the Jacksonville community each year. Nominate a candidate.",
     wolf_body)

# ============================================================== DONATE
donate_body = page_hero("Make a Donation",
    "Your contribution helps support and advance the next generation of female leaders.") + f"""
<section class="section">
  <div class="container">
    <div class="two-col">
      <div>
        <h2>Support JWLF today</h2>
        <p class="lede">Please consider making a donation to the Jacksonville Women\u2019s Leadership Forum today!
        Your contribution will help support and advance the next generation of female leaders within our
        organizations and business community.</p>
        <!--
          DONATIONS: the current jwlf.org donation page uses a PayPal donation
          form. Replace the placeholder hosted_button_id below with the value
          from the organization's PayPal account (PayPal > Pay & Get Paid >
          PayPal Buttons), or swap the href for the org's PayPal.Me / donate
          link. Flagged in MIGRATION-CHECKLIST.md.
        -->
        <div class="btn-row">
          <a class="btn btn--primary" href="https://www.paypal.com/donate/?hosted_button_id=REPLACE_WITH_JWLF_BUTTON_ID">
            Donate via PayPal</a>
          <a class="btn btn--outline" href="./contact.html">Questions? Contact us</a>
        </div>
        <p class="form-note mt-2">Prefer another way to give? Sponsorships fund most of our programming \u2014 see
        <a href="./sponsorship.html">sponsorship opportunities</a>.</p>
      </div>
      <div>
        <div class="card">
          <h3>Where your gift goes</h3>
          <p>JWLF is a volunteer-run 501(c)(3). Donations and sponsorships fund the annual Forum, year-round
          educational and networking events, and our support of
          <a href="./non-profit-partners.html">non-profit partners</a> serving women on the First Coast.</p>
        </div>
        <p class="notice mt-2">{DISCLOSURE}</p>
      </div>
    </div>
  </div>
</section>
"""
page("donate.html", "Make a Donation",
     "Donate to the Jacksonville Women's Leadership Forum, a 501(c)(3) non-profit. Contributions are deductible to the extent allowed by law.",
     donate_body)

# ============================================================== CONTACT
contact_body = page_hero("Contact JWLF", "We\u2019d love to hear from you!") + f"""
<section class="section">
  <div class="container two-col">
    <div>
      <h2>Send us a message</h2>
      <p>Send us an email at <a href="mailto:{EMAIL}">{EMAIL}</a> or fill out the form below.</p>
      <!-- To go live: point action at your Formspree endpoint and see js/main.js ("GOING LIVE WITH FORMSPREE"). -->
      <form class="form" data-validate action="#" method="POST" novalidate>
        <div class="form-row">
          <label for="c-name">Your name <span class="req" aria-hidden="true">*</span></label>
          <input id="c-name" name="name" type="text" autocomplete="name" required>
          <p class="field-error">Please enter your name.</p>
        </div>
        <div class="form-row">
          <label for="c-email">Your email <span class="req" aria-hidden="true">*</span></label>
          <input id="c-email" name="email" type="email" autocomplete="email" required>
          <p class="field-error">Please enter a valid email address.</p>
        </div>
        <div class="form-row">
          <label for="contact-subject">Subject</label>
          <input id="contact-subject" name="subject" type="text">
        </div>
        <div class="form-row">
          <label for="c-message">Your message <span class="req" aria-hidden="true">*</span></label>
          <textarea id="c-message" name="message" required></textarea>
          <p class="field-error">Please enter a message.</p>
        </div>
        <button class="btn btn--primary" type="submit">Send message</button>
        <p class="form-note">This form is in demo mode \u2014 submissions are validated in your browser but not yet
        sent anywhere.</p>
      </form>
      <div class="form-success" role="status">Thanks for reaching out! This demo confirms your message validated
      correctly. Once the form is connected to Formspree it will reach our team \u2014 in the meantime, please email
      <a href="mailto:{EMAIL}">{EMAIL}</a>.</div>
    </div>
    <div>
      <div class="card">
        <h3>Follow us</h3>
        <ul style="list-style:none; padding:0">
          <li><a href="https://www.facebook.com/JaxWLF/">Facebook \u2014 facebook.com/JaxWLF</a></li>
          <li><a href="https://www.linkedin.com/groups/4252397">LinkedIn group</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
      </div>
      <div class="card mt-2">
        <h3>Common reasons to write</h3>
        <ul>
          <li>Submitting a <a href="./contact.html?subject=forum-idea">forum idea</a></li>
          <li>Interest in <a href="./contact.html?subject=speaking">speaking at our educational events</a></li>
          <li><a href="./sponsorship.html#sponsor-inquiry">Sponsorship inquiries</a></li>
          <li><a href="./volunteer.html">Volunteering</a></li>
          <li>Becoming a <a href="./contact.html?subject=partner">non-profit partner</a></li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""
page("contact.html", "Contact",
     "Contact the Jacksonville Women's Leadership Forum by email or through our contact form.",
     contact_body)

# ============================================================== manifest + download script
manifest = ["# Image manifest \u2014 local file \u2192 source URL on jwlf.org",
"",
"The container that generated this site cannot download binaries, so every image",
"referenced by the pages is listed here. Run `./download-images.sh` from the site",
"root (requires curl) to fetch them all into place, then re-compress large photos",
"for the web (see README).",
"",
"| Local path | Source URL |",
"|---|---|"]
for local, url in sorted(IMAGES.items()):
    manifest.append(f"| {local} | {url} |")
with open(os.path.join(ROOT, "images-manifest.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(manifest) + "\n")

lines = ["#!/usr/bin/env bash",
"# Downloads every migrated image from the live jwlf.org site into ./images/.",
"# Run from the site root:  bash download-images.sh",
"# Then (optional, recommended) compress:  see README 'Image optimization'.",
"set -u",
"ok=0; fail=0",
"fetch () {",
'  mkdir -p "$(dirname "$1")"',
'  if curl -fsSL --retry 2 -o "$1" "$2"; then ok=$((ok+1)); else fail=$((fail+1)); echo "FAILED: $2"; fi',
"}",""]
for local, url in sorted(IMAGES.items()):
    lines.append(f'fetch "{local}" "{url}"')
lines += ["", 'echo "Downloaded: $ok   Failed: $fail"',
'echo "Any failures are listed above — download those manually into the path shown in images-manifest.md."']
with open(os.path.join(ROOT, "download-images.sh"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
os.chmod(os.path.join(ROOT, "download-images.sh"), 0o755)
print("pages3 + manifest done;", len(IMAGES), "images in manifest")
