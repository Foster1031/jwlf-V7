# Home, Get Involved hub, About, Message from Chair, Board, Partners, Gallery, News
from build import page, page_hero, EMAIL, EVENTBRITE, BROCHURE, DISCLOSURE
from images_data import GALLERY, gallery_local

# ---------------------------------------------------------------- shared bits
OFFICERS = [
    ("Cari Smith", "Chairwoman & President", "Vice President, Enterprise Risk Management, Fidelity National Financial", "images/people/cari-smith.jpg", "https://www.linkedin.com/in/cari-smith-a6465b58/"),
    ("Katie Mountain", "Vice Chairwoman & Vice President", "EVP of Business Development, Landstar", "images/people/katie-mountain.jpg", "https://www.linkedin.com/in/katiemountain/"),
    ("Lisa Jennings", "Secretary", "Manager, Community Relations & Project Outreach, JEA", "images/people/lisa-jennings.jpg", "https://www.linkedin.com/in/lisa-a-j-21387450/"),
    ("Landie Brooks", "Treasurer", "VP IT Governance & Compliance, Fidelity National Title", "images/people/landie-brooks.jpg", "https://www.linkedin.com/in/landie-brooks/"),
]

def officer_cards(link_board=True):
    cards = ""
    for name, role, org, img, li in OFFICERS:
        cards += f"""<div class="card person-card" data-reveal>
  <img class="person-photo" src="./{img}" alt="{name}, {role}" loading="lazy" width="132" height="132">
  <h3>{name}</h3>
  <p class="person-role">{role}</p>
  <p class="person-org">{org}</p>
  <a href="{li}">Connect with {name.split()[0]}</a>
</div>"""
    return cards

SPONSOR_LOGOS = [
    ("images/sponsors/mode.png", "MODE"),
    ("images/sponsors/ww.jpg", "WW"),
    ("images/sponsors/regency-centers.jpg", "Regency Centers"),
    ("images/sponsors/mayo-clinic.png", "Mayo Clinic"),
    ("images/sponsors/landstar.jpg", "Landstar"),
    ("images/sponsors/kpmg.jpg", "KPMG"),
    ("images/sponsors/jea.jpg", "JEA"),
    ("images/sponsors/jaguars.jpg", "Jacksonville Jaguars"),
    ("images/sponsors/holland-knight.jpg", "Holland & Knight"),
    ("images/sponsors/tea.jpg", "The Energy Authority"),
    ("images/sponsors/csx.jpg", "CSX"),
    ("images/sponsors/black-knight.png", "Black Knight"),
    ("images/sponsors/adecco.png", "Adecco"),
    ("images/sponsors/acosta.png", "Acosta"),
    ("images/sponsors/deutsche-bank.jpg", "Deutsche Bank"),
    ("images/sponsors/50th-gold.png", "Sponsor logo (50th)"),
    ("images/sponsors/maximus.png", "Maximus"),
    ("images/sponsors/wells-fargo.png", "Wells Fargo"),
    ("images/sponsors/baptist-health.jpg", "Baptist Health"),
    ("images/sponsors/iem.png", "Industrial Electric Mfg. (IEM)"),
    ("images/sponsors/vystar.jpg", "VyStar Credit Union"),
    ("images/sponsors/fields-auto-group.jpg", "Fields Auto Group"),
    ("images/sponsors/sponsor-0.png", "Sponsor logo"),
    ("images/sponsors/sponsor-0-1.png", "Sponsor logo"),
    ("images/sponsors/sponsor-embedded.png", "Sponsor logo"),
    ("images/sponsors/sponsor-video-poster.png", "Sponsor logo"),
]

def logo_wall():
    tiles = ""
    for img, name in SPONSOR_LOGOS:
        tiles += f'<div class="logo-tile"><img src="./{img}" alt="{name} logo" loading="lazy"></div>\n'
    return f'<div class="logo-wall">{tiles}</div>'

# ============================================================== HOME
home_body = f"""
<div class="hero">
  <img class="hero-img" src="./images/photos/hero.jpg" alt="" aria-hidden="true">
  <div class="hero-inner">
    <h1>Women working together to create leaders &amp; advance careers</h1>
    <p>The Jacksonville Women\u2019s Leadership Forum is the premier organization on the First Coast that
    empowers women to successfully navigate the unique terrain of the corporate workplace and nurture
    their personal development.</p>
    <div class="btn-row">
      <a class="btn btn--gold" href="./forum.html">Learn About the Forum</a>
      <a class="btn btn--outline" href="./sponsorship.html">Become a Sponsor</a>
    </div>
  </div>
</div>

<section class="section">
  <div class="container">
    <h2>Welcome to the Jacksonville Women\u2019s Leadership Forum</h2>
    <p class="lede">JWLF will help transform the way participants approach leadership, networking, career
    advancement and life balance. Through annual Forums and educational and networking events throughout
    the year, you will gain insights from other smart and successful women all focused on tackling the
    issues that challenge women working their way to the top.</p>
    <p><strong>Ready to take your career to the next level? Then join us!</strong></p>
    <div class="grid grid--4 mt-2">
      <div class="card pillar-card" data-reveal>
        <h3>Enhance Leadership Skills</h3>
        <p>We serve to enhance leadership opportunities for future female executives in an exclusive peer-to-peer
        setting. Let JWLF expand your career potential, develop critical skills, and set career objectives that
        are both attainable and sustainable.</p>
      </div>
      <div class="card pillar-card" data-reveal>
        <h3>Broaden Professional Network</h3>
        <p>We strive to broaden the individual\u2019s professional network and visibility in the local Jacksonville
        business community. JWLF will help you maximize your networks and leverage their influence.</p>
      </div>
      <div class="card pillar-card" data-reveal>
        <h3>Advancing Careers</h3>
        <p>We provide opportunities for career development through mentorship and continuing education. Learn how
        to leverage your unique value proposition to advance your career.</p>
      </div>
      <div class="card pillar-card" data-reveal>
        <h3>Finding Life Balance</h3>
        <p>We help you find that elusive life balance that every professional woman desires. Learn new techniques
        and tips on finding what works best in your busy life. Obtain practical advice on balancing personal
        success while growing your professional brand.</p>
      </div>
    </div>
  </div>
</section>

<section class="theme-band" aria-labelledby="theme-heading">
  <div class="container">
    <p class="theme-line">Our 2026\u20132027 Annual Theme</p>
    <h2 id="theme-heading">Presence with Purpose</h2>
    <p class="theme-line">Lead with clarity. Influence with confidence. Grow with intention.</p>
    <p class="status">We look forward to sharing information about our 2027 Annual Forum in the coming months.</p>
    <a class="btn btn--gold" href="{EVENTBRITE}">Visit Us in 2027 to Register</a>
  </div>
</section>

<section class="section">
  <div class="container two-col">
    <div>
      <h2>Who Should Attend?</h2>
      <ul>
        <li>Senior-level women identified as proactive leaders with high potential and accomplishment</li>
        <li>Mid- and senior-level managers who lead teams and typically have direct reports</li>
        <li>Women with several years of experience in leadership roles</li>
        <li>Women and men of influence within their organizations who are engaged in empowering the next
        generation of women leaders</li>
      </ul>
      <div class="btn-row">
        <a class="btn btn--primary" href="./forum.html">See the Upcoming Forum</a>
        <a class="btn btn--outline" href="./speakers.html">Meet the 2026 Speakers</a>
      </div>
    </div>
    <div class="photo-strip" style="grid-template-columns:1fr">
      <img src="./images/photos/about-1.jpg" alt="Attendees networking at a JWLF Forum" loading="lazy">
      <img src="./images/photos/about-3.jpg" alt="A speaker presenting at the JWLF Forum" loading="lazy">
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <h2>What Attendees Say</h2>
    <div class="grid grid--3">
      <div class="card quote-card" data-reveal>
        <blockquote>\u201cThank you again for the opportunity to experience the Jacksonville Women\u2019s Leadership
        Forum. I learned some great things about negotiating, met some very interesting women, ate well, and most
        of all, came to work today refreshed and recharged. How did I live in Jax all these years and never know
        about this? No more!\u201d</blockquote>
        <cite><strong>Marisa Carbone</strong>, Manager of Multimedia Production, JEA</cite>
      </div>
      <div class="card quote-card" data-reveal>
        <blockquote>\u201cI was beyond excited to attend yesterday\u2019s Jacksonville Women\u2019s Leadership
        Forum. To say I left feeling empowered, motivated, and inspired would be an understatement.\u201d</blockquote>
        <cite><strong>Trina Forbess</strong>, ICE</cite>
      </div>
      <div class="card quote-card" data-reveal>
        <blockquote>\u201cIt\u2019s been a wonderful partnership between JWLF and Mercedes Benz of Orange Park and
        Jacksonville. As a long-term JWLF networking event sponsor, we have been able to showcase our automobiles
        to the attendees, share the Mercedes Benz message of the priority we place on our female customers, and
        we\u2019ve seen a tangible return on our investment.\u201d</blockquote>
        <cite><strong>Debbie Mills</strong>, General Manager, Mercedes Benz of Orange Park</cite>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2>Meet Our 2026/2027 Officers</h2>
    <div class="grid grid--4">
      {officer_cards()}
    </div>
    <div class="btn-row"><a class="btn btn--outline" href="./board.html">View Our 2026/2027 Board of Directors</a></div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <h2>Do You Have a Forum Idea?</h2>
    <div class="grid grid--2">
      <div class="card" data-reveal>
        <h3>Suggest a topic</h3>
        <p>The Jacksonville Women\u2019s Leadership Forum is always looking for fresh ideas. Please reach out to us
        if you have any suggestions!</p>
        <a class="btn btn--primary" href="./contact.html?subject=forum-idea">Submit an Idea</a>
      </div>
      <div class="card" data-reveal>
        <h3>Speak at our educational events</h3>
        <p>Interested in speaking at one of our educational series during the year? It\u2019s a great way to promote
        yourself and your company in our community. Contact us to find out more information.</p>
        <a class="btn btn--primary" href="./contact.html?subject=speaking">Contact Us</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2>Thank You to Our Current and Previous Sponsors</h2>
    <p class="lede">Over 150 executive women, from various large, locally-based companies attend the annual
    Jacksonville Women\u2019s Leadership Forum networking events and Forum, and receive world-class leadership
    training in the process.</p>
    {logo_wall()}
    <div class="btn-row"><a class="btn btn--primary" href="./sponsorship.html">Sponsorship Opportunities</a></div>
  </div>
</section>

<section class="section cta-band">
  <div class="container">
    <h2>Be Part of What\u2019s Next</h2>
    <p>Join us at the next Forum, put your company in front of Jacksonville\u2019s women leaders, or help us
    support the next generation.</p>
    <div class="btn-row">
      <a class="btn btn--gold" href="{EVENTBRITE}">Register</a>
      <a class="btn btn--light" href="./sponsorship.html">Sponsor</a>
      <a class="btn btn--outline" href="./donate.html">Donate</a>
    </div>
  </div>
</section>
"""
page("index.html", "Welcome to JWLF",
     "The Jacksonville Women's Leadership Forum empowers women to navigate the corporate workplace and nurture their personal development.",
     home_body)

# ============================================================== GET INVOLVED (hub)
gi_body = page_hero("Get Involved",
    "Sponsor, volunteer, nominate, or donate \u2014 every path helps advance the next generation of women leaders on the First Coast.") + f"""
<section class="section">
  <div class="container">
    <div class="grid grid--4">
      <div class="card" data-reveal>
        <h3>Sponsor</h3>
        <p>Position your brand among an ideal demographic of professional and leadership-minded women.</p>
        <a class="btn btn--primary" href="./sponsorship.html">Sponsorship Information</a>
      </div>
      <div class="card" data-reveal>
        <h3>Volunteer</h3>
        <p>Lend your time and talent \u2014 promotion, event support, or forum content research.</p>
        <a class="btn btn--primary" href="./volunteer.html">Volunteer With Us</a>
      </div>
      <div class="card" data-reveal>
        <h3>WoLF Award</h3>
        <p>Nominate an outstanding woman in our community for our annual recognition.</p>
        <a class="btn btn--primary" href="./wolf-award.html">About the WoLF Award</a>
      </div>
      <div class="card" data-reveal>
        <h3>Donate</h3>
        <p>Your contribution helps support and advance the next generation of female leaders.</p>
        <a class="btn btn--primary" href="./donate.html">Make a Donation</a>
      </div>
    </div>
  </div>
</section>
"""
page("get-involved.html", "Get Involved",
     "Sponsor, volunteer, nominate a WoLF Award recipient, or donate to the Jacksonville Women's Leadership Forum.",
     gi_body)

# ============================================================== ABOUT
about_body = page_hero("About JWLF",
    "The purpose of the Jacksonville Women\u2019s Leadership Forum is to help support and advance the next generation of female leaders within our organizations and business community.") + f"""
<section class="section">
  <div class="container">
    <div class="two-col">
      <div>
        <h2>Who we are</h2>
        <p>The Jacksonville Women\u2019s Leadership Forum is the premier organization on the First Coast that
        empowers women to successfully navigate the unique terrain of the corporate workplace and nurture their
        personal development. JWLF will help transform the way participants approach leadership, networking,
        career advancement and life balance.</p>
        <p>Through annual Forums and educational and networking events throughout the year, you will gain insights
        from other smart and successful women all focused on tackling the issues that challenge women working
        their way to the top.</p>
        <p>The Jacksonville Women\u2019s Leadership Forum is a non-profit 501(c)(3) corporation.</p>
        <div class="btn-row">
          <a class="btn btn--primary" href="./sponsorship.html">Sponsorship Opportunities</a>
          <a class="btn btn--outline" href="./donate.html">Make a Donation</a>
        </div>
      </div>
      <div class="photo-strip" style="grid-template-columns:1fr">
        <img src="./images/photos/about-1.jpg" alt="Attendees at the 2026 JWLF Forum" loading="lazy">
        <img src="./images/photos/about-2.jpg" alt="Networking at the 2025 Women's Leadership Forum" loading="lazy">
        <img src="./images/photos/about-3.jpg" alt="A session at the 2026 JWLF Forum" loading="lazy">
      </div>
    </div>
  </div>
</section>
<section class="section section--tint">
  <div class="container">
    <h2>Explore</h2>
    <div class="grid grid--4">
      <div class="card"><h3><a href="./message-from-chair.html">Message from the Chair</a></h3><p>A welcome from Chairwoman &amp; President Cari Smith.</p></div>
      <div class="card"><h3><a href="./board.html">Board &amp; Officers</a></h3><p>The 2026/2027 leaders who guide JWLF.</p></div>
      <div class="card"><h3><a href="./non-profit-partners.html">Non-Profit Partners</a></h3><p>Organizations we support that benefit women on the First Coast.</p></div>
      <div class="card"><h3><a href="./gallery.html">Photo Gallery</a></h3><p>Highlights from every Forum since 2012.</p></div>
    </div>
  </div>
</section>
"""
page("about.html", "About JWLF",
     "About the Jacksonville Women's Leadership Forum, a 501(c)(3) supporting the next generation of female leaders.",
     about_body)

# ============================================================== MESSAGE FROM CHAIR
chair_body = page_hero("Message from the Chair") + f"""
<section class="section">
  <div class="container two-col">
    <div>
      <h2 class="mt-0">Welcome to the Jacksonville Women\u2019s Leadership Forum (JWLF)</h2>
      <p>It is both an honor and a privilege to serve as President of an organization dedicated to empowering,
      connecting, and inspiring women throughout Northeast Florida.</p>
      <p>I believe leadership is not about having all the answers \u2013 it is about learning, growing, lifting
      others up, and creating opportunities for others to succeed. That spirit is what makes JWLF such a special
      community. Our members come from diverse backgrounds and experiences, yet we are united by a shared
      commitment to supporting one another\u2019s personal and professional growth.</p>
      <p>Throughout my career, I have found that the greatest successes happen through collaboration, shared
      experiences, and helping others reach their full potential. Leading by example, serving others, and treating
      people with kindness and respect are values that guide me every day and ones I am committed to bringing to
      JWLF.</p>
      <p>I am fortunate to serve alongside an exceptional <a href="./board.html">Board of Directors</a>, whose
      leadership helps shape the direction of our organization. Together with the support of
      <a href="./sponsorship.html">our sponsors</a>, we provide impactful programming featuring
      <a href="./previous-speakers.html">Forum speakers</a> and panel discussions that inspire women to lead with
      confidence, authenticity, and purpose. We are also proud to recognize outstanding women through the annual
      <a href="./wolf-award.html">JWLF WoLF Award</a> and to strengthen our community through
      <a href="./non-profit-partners.html">partnerships with local nonprofit organizations</a> dedicated to the
      growth and advancement of women and girls throughout Northeast Florida.</p>
      <p>I would also like to extend my sincere gratitude to our Board members, volunteers, sponsors, and speakers
      whose dedication and passion make JWLF possible. Your commitment is what allows our organization to thrive
      and continue making a meaningful impact.</p>
      <p>Thank you for being part of this extraordinary community. I look forward to connecting with you
      throughout the year and celebrating all that we will accomplish together.</p>
      <p>Warm regards,</p>
      <p><strong>Cari Smith</strong><br>Chairwoman and President,<br>Jacksonville Women\u2019s Leadership Forum</p>
      <a class="btn btn--primary" href="./sponsorship.html">Sponsorship Opportunities</a>
    </div>
    <div>
      <img src="./images/people/cari-smith.jpg" alt="Cari Smith, Chairwoman and President of JWLF"
           style="border-radius:10px; max-width:360px" loading="lazy">
    </div>
  </div>
</section>
"""
page("message-from-chair.html", "Message from the Chair",
     "A welcome message from Cari Smith, Chairwoman and President of the Jacksonville Women's Leadership Forum.",
     chair_body)

# ============================================================== BOARD
BOARD = [
    ("Cari Smith, Chairwoman and President", "Vice President, Enterprise Risk Management", "Fidelity National Financial", "images/people/cari-smith.jpg", "https://www.linkedin.com/in/cari-smith-a6465b58/", "Cari"),
    ("Katie Mountain, Vice Chair and Vice President", "EVP of Business Development", "Landstar", "images/people/katie-mountain.jpg", "https://www.linkedin.com/in/katiemountain/", "Katie"),
    ("Lisa Jennings, Secretary", "Manager, Community Relations & Project Outreach", "JEA", "images/people/lisa-jennings.jpg", "https://www.linkedin.com/in/lisa-a-j-21387450/", "Lisa"),
    ("Landie Brooks, Treasurer", "VP IT Governance & Compliance", "Fidelity National Title", "images/people/landie-brooks.jpg", "https://www.linkedin.com/in/landie-brooks/", "Landie"),
    ("Chelsea Carroll", "Managing Director", "KPMG LLP", "images/people/chelsea-carroll.jpg", "https://www.linkedin.com/in/chelsea-carroll-46ba9814/", "Chelsea"),
    ("Sheri Clark", "Director of People Operations", "The Energy Authority (TEA)", "images/people/sheri-clark.jpg", "https://www.linkedin.com/in/sclark0077475/", "Sheri"),
    ("Laura Davis", "Director, Corporate Responsibility & Social Impact", "Regency Centers", "images/people/laura-davis.jpg", "https://www.linkedin.com/in/laura-davis-89aa9566/", "Laura"),
    ("Vicki Harris", "Vice President, Information Security and Assurance", "Maximus", "images/people/vicki-harris.png", "https://www.linkedin.com/in/vicki-harris-83a3aa7/", "Vicki"),
    ("Jennifer Mansfield", "Partner", "Holland & Knight", "images/people/jennifer-mansfield.jpg", "https://www.linkedin.com/in/jennifer-mansfield-908ba910/", "Jennifer"),
    ("Cindy Rose", "Consultant; Partner (Retired)", "KPMG LLP", "images/people/cindy-rose.jpg", "https://www.linkedin.com/in/cindy-rose-jax/", "Cindy"),
    ("Cory Seay", "Vice President of Corporate Services and Chief of Staff", "Landstar", "images/people/cory-seay.jpg", "http://linkedin.com/in/cory-seay-b6207716", "Cory"),
    ("Janie Smalley", "Grants Manager", "JEA", "images/people/janie-smalley.jpg", "https://www.linkedin.com/in/janie-k-s-3b1609242/", "Janie"),
    ("Diane Williams", "Director of Talent Development", "Industrial Electric Mfg. (IEM)", "images/people/diane-williams.jpg", "https://www.linkedin.com/in/diane-williams-sphr-shrm-scp-7a381221/", "Diane"),
]
board_cards = ""
for name, role, org, img, li, first in BOARD:
    board_cards += f"""<div class="card person-card" data-reveal>
  <img class="person-photo" src="./{img}" alt="{name.split(',')[0]}" loading="lazy" width="132" height="132">
  <h3>{name}</h3>
  <p class="person-role">{role}</p>
  <p class="person-org">{org}</p>
  <a href="{li}">Connect with {first}</a>
</div>"""

board_body = page_hero("Board of Directors &amp; Officers",
    "The 2026/2027 leaders who guide the Jacksonville Women\u2019s Leadership Forum.") + f"""
<section class="section">
  <div class="container">
    <h2>2026/2027 Board of Directors</h2>
    <div class="grid grid--4">{board_cards}</div>
  </div>
</section>
<section class="section section--tint">
  <div class="container">
    <h2>2026/2027 Officers</h2>
    <div class="grid grid--4">{officer_cards()}</div>
  </div>
</section>
"""
page("board.html", "Board of Directors & Officers",
     "Meet the 2026/2027 Board of Directors and Officers of the Jacksonville Women's Leadership Forum.",
     board_body)

# ============================================================== NON-PROFIT PARTNERS
# Note: the live site shows logos with "find out more" links only; the one-line
# descriptions below are new editorial copy — flagged in MIGRATION-CHECKLIST.md.
PARTNERS = [
    ("Hubbard House", "images/partners/hubbard-house.png", "https://www.hubbardhouse.org/", "Safety, empowerment, and support for survivors of domestic violence in Duval and Baker counties."),
    ("Women in Business Society \u2013 UNF", "images/partners/wib-unf.png", "https://www.linkedin.com/company/unf-wibs/about/", "A University of North Florida student organization connecting and developing future businesswomen."),
    ("STEM Goes Red \u2013 American Heart Association", "images/partners/stem-goes-red.jpg", "http://goredforwomen.org/en/get-involved/attend/stem-goes-red", "Introducing girls to STEM careers while advancing women\u2019s heart health."),
    ("Northeast Florida Regional STEM2 Hub", "images/partners/stem2hub.png", "https://stem2hub.org/", "Accelerating STEM learning opportunities for students across Northeast Florida."),
    ("Women Veterans Resource Center", "images/partners/women-veterans.png", "https://womenveteransresources.org/", "Resources and support for women who have served."),
    ("Girl Scouts of Gateway Council", "images/partners/girl-scouts-gateway.jpg", "https://www.girlscouts-gateway.org/", "Building girls of courage, confidence, and character across North Florida."),
    ("The DONNA Foundation", "images/partners/donna-foundation.png", "http://thedonnafoundation.org/", "Financial assistance and support for families living with breast cancer."),
    ("HabiJax \u2013 Habitat for Humanity of Jacksonville", "images/partners/habijax.jpg", "http://habijax.org/", "Affordable homeownership opportunities for Jacksonville families."),
    ("Community Connections", "images/partners/community-connections.jpg", None, "Housing and support services for women and children in Jacksonville."),
    ("PACE Center for Girls", "images/partners/pace.jpg", "https://www.pacecenter.org/", "Education, counseling, and advocacy for girls and young women."),
    ("American Heart Association", "images/partners/aha.png", "http://www.heart.org/HEARTORG/", "Fighting heart disease and stroke \u2014 the leading health threats to women."),
    ("Girls on the Run", "images/partners/girls-on-the-run.jpg", "https://www.girlsontherun.org/", "Inspiring girls to be joyful, healthy, and confident through running-based programs."),
    ("Rethreaded", "images/partners/rethreaded.jpg", "https://www.rethreaded.com/", "Renewing hope and careers for survivors of human trafficking."),
    ("Delores Barr Weaver Policy Center", "images/partners/dbwpc.jpg", "https://www.seethegirl.org/", "Research, advocacy, and action to engage communities on behalf of girls."),
]
partner_cards = ""
for name, img, link, desc in PARTNERS:
    link_html = (f'<a href="{link}">Find out more and get involved</a>' if link
                 else f'<a href="./contact.html">Contact JWLF to learn more</a>')
    partner_cards += f"""<div class="card partner-card" data-reveal>
  <div class="logo-tile"><img src="./{img}" alt="{name} logo" loading="lazy"></div>
  <h3>{name}</h3>
  <p>{desc}</p>
  <p>{link_html}</p>
</div>"""

partners_body = page_hero("Non-Profit Partners",
    "We promote and support non-profits who do work to benefit women on the First Coast.") + f"""
<section class="section">
  <div class="container">
    <div class="grid grid--3">{partner_cards}</div>
    <div class="btn-row"><a class="btn btn--primary" href="./contact.html?subject=partner">Interested in Becoming a Partner?</a></div>
  </div>
</section>
"""
page("non-profit-partners.html", "Non-Profit Partners",
     "JWLF's non-profit partners doing work to benefit women and girls on the First Coast.",
     partners_body)

# ============================================================== PHOTO GALLERY
years_seen, gallery_sections = [], ""
by_year = {}
for year, url in GALLERY:
    by_year.setdefault(year, []).append(url)
for year in sorted(by_year.keys(), reverse=True):
    items = ""
    for url in by_year[year]:
        local = gallery_local(year, url)
        items += (f'<a href="./{local}"><img src="./{local}" '
                  f'alt="Attendees, speakers, and networking at the {year} JWLF Forum" loading="lazy"></a>\n')
    gallery_sections += f"""<div class="gallery-year"><h2>{year} Forum</h2>
<div class="gallery-grid">{items}</div></div>\n"""

gallery_body = page_hero("Photo Gallery",
    "Highlights from the annual Jacksonville Women\u2019s Leadership Forum, 2012 to today.") + f"""
<section class="section">
  <div class="container">
    {gallery_sections}
  </div>
</section>
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Photo viewer">
  <button type="button" class="lightbox-close" aria-label="Close photo viewer">&times;</button>
  <button type="button" class="lightbox-prev" aria-label="Previous photo">&#8249;</button>
  <img src="" alt="">
  <button type="button" class="lightbox-next" aria-label="Next photo">&#8250;</button>
  <p class="lightbox-caption"></p>
</div>
"""
page("gallery.html", "Photo Gallery",
     "Photos from Jacksonville Women's Leadership Forum annual events, 2012 through 2026.",
     gallery_body)

# ============================================================== NEWS
# Post index migrated from the live blog. Full article bodies still live at
# jwlf.org — flagged in MIGRATION-CHECKLIST.md for follow-up migration.
POSTS = [
    ("How Communication Shapes the Career Trajectory of Women in Senior Leadership", "July 10, 2025",
     "After decades working with Fortune 500 companies, I\u2019ve seen one factor stand out: how women communicate at senior levels profoundly influences not only perceptions of their leadership, but also their promotion opportunities and longevity."),
    ("Executive Presence: A Cornerstone for Women Leaders", "June 26, 2025",
     "Executive presence (EP) is often defined as the ability to inspire confidence \u2014 projecting credibility, composure, and clarity so others believe you can lead under pressure."),
    ("The Confidence Catalyst: Why Every Woman Needs a Mentor in Today\u2019s Corporate World", "January 23, 2025",
     "Have you ever found yourself in a professional situation thinking, \u201cI wish someone could just show me the ropes\u201d? If you have, you\u2019re not alone."),
    ("The Power of Sponsorship for Corporate Women", "January 18, 2025",
     "When we talk about advancing women in the workplace, terms like \u201cmentorship\u201d and \u201csponsorship\u201d often surface. While they may seem interchangeable at first glance, they represent fundamentally different things."),
    ("Are You Your Own Best Ally, Or Worst Enemy?", "February 6, 2019",
     "By Tammy Heermann, Leadership Development Expert. When you\u2019re in the zone, doing your thing, you feel invincible, right? You know you can harness your mindset to make the impossible feel possible."),
    ("Top Tips for Infusing Hope into Your Corporate Culture", "January 25, 2019",
     "By Libby Gill. When your team is faced with change, challenge, or chaos, inspire them with a future-focused vision of shared success!"),
]
post_cards = ""
for title, date, teaser in POSTS:
    post_cards += f"""<article class="card" data-reveal>
  <h3>{title}</h3>
  <p class="person-org">{date}</p>
  <p>{teaser}</p>
</article>"""

news_body = page_hero("News",
    "Articles from JWLF on leadership, communication, mentorship, and career development.") + f"""
<section class="section">
  <div class="container">
    <p class="notice">Full articles are being migrated from our previous site. If you\u2019d like a copy of any
    article in the meantime, <a href="./contact.html">contact us</a>.</p>
    <div class="grid grid--2 mt-2">{post_cards}</div>
  </div>
</section>
"""
page("news.html", "News",
     "News and articles from the Jacksonville Women's Leadership Forum.",
     news_body)
print("pages1 done")
