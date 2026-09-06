# Forums & Events pages: forum.html, speakers.html, previous-speakers.html
from build import page, page_hero, EVENTBRITE

# ============================================================== UPCOMING FORUM & EVENTS
forum_body = page_hero("Forums &amp; Events",
    "One signature annual Forum, plus educational and networking events throughout the year.") + f"""
<section class="theme-band" aria-labelledby="forum-theme">
  <div class="container">
    <p class="theme-line">Our 2026\u20132027 Annual Theme</p>
    <h2 id="forum-theme">Presence with Purpose</h2>
    <p class="theme-line">Lead with clarity. Influence with confidence. Grow with intention.</p>
    <p class="status">Details about the 2027 Annual Forum \u2014 date, location, and program \u2014 are coming soon.
    Visit us in early 2027 for information and registration.</p>
    <a class="btn btn--gold" href="{EVENTBRITE}">Visit in 2027 to Register</a>
  </div>
</section>

<section class="section">
  <div class="container two-col">
    <div>
      <h2>Our 2026 Annual Forum</h2>
      <p>Our 2026 Annual Forum was held on April 17th, 2026:</p>
      <p><strong>\u201cShe Leads: Igniting, Elevating Voice, and Delivering Value\u201d</strong></p>
      <p><a href="./speakers.html">Learn more about our 2026 JWLF Forum keynote speakers</a>, or browse
      <a href="./previous-speakers.html">previous speakers and event topics</a> going back to 2014.</p>
      <h2 class="mt-2">Educational Events</h2>
      <p>Follow us on <a href="https://www.linkedin.com/groups/4252397">LinkedIn</a> for announcements on our
      educational events throughout the year.</p>
      <h2 class="mt-2">Who Should Attend?</h2>
      <ul>
        <li>Senior-level women identified as proactive leaders with high potential and accomplishment</li>
        <li>Mid- and senior-level managers who lead teams and typically have direct reports</li>
        <li>Women with several years of experience in leadership roles</li>
        <li>Women and men of influence within their organizations who are engaged in empowering the next
        generation of women leaders</li>
      </ul>
    </div>
    <div>
      <img src="./images/photos/forum-2016.jpg" alt="A full house at a Jacksonville Women's Leadership Forum"
           style="border-radius:10px" loading="lazy">
      <div class="card mt-2">
        <h3>Do you have a forum idea?</h3>
        <p>The Jacksonville Women\u2019s Leadership Forum is always looking for fresh ideas. Please reach out to us
        if you have any suggestions!</p>
        <a class="btn btn--primary" href="./contact.html?subject=forum-idea">Submit an Idea</a>
      </div>
      <div class="card mt-2">
        <h3>Want to speak at our events?</h3>
        <p>Interested in speaking at one of our educational series during the year? It\u2019s a great way to promote
        yourself and your company in our community.</p>
        <a class="btn btn--primary" href="./contact.html?subject=speaking">Contact Us</a>
      </div>
    </div>
  </div>
</section>
"""
page("forum.html", "Upcoming Forum & Events",
     "The JWLF annual Forum and year-round educational events. 2026-2027 theme: Presence with Purpose.",
     forum_body)

# ============================================================== CURRENT SPEAKERS
def speaker_block(name, role, img, paragraphs, link=None, link_label=None):
    body = "".join(f"<p>{p}</p>" for p in paragraphs)
    link_html = f'<p><a href="{link}">{link_label}</a></p>' if link else ""
    return f"""<article class="card speaker" data-reveal>
  <img src="./{img}" alt="{name}" loading="lazy">
  <div>
    <h3>{name}</h3>
    <p class="person-role">{role}</p>
    <details class="bio">
      <summary>Read {name.split()[0]}\u2019s biography</summary>
      {body}{link_html}
    </details>
  </div>
</article>"""

JANEAN = ["With over 28 years of transformative leadership in the financial industry, <strong>Janean C. Armstrong</strong> is not just a name; she\u2019s a force of nature. Her journey began at Bank One in Houston, Texas, where her exceptional talent and relentless work ethic propelled her to stardom. It wasn\u2019t long before she made her mark at SunTrust (now Truist Bank) as well as Wells Fargo, where she showcased her ability to inspire and motivate on a grand scale as well as refined her strategic acumen and deepened her impact in the banking community. Yet, it was her bold move to VyStar in 2023 that truly solidified her role as a transformative leader. At VyStar, Janean is at the forefront of growth initiatives, blending market insight with a passion for community engagement to drive both profitability and positive change. In 2025 Janean was promoted to Retail Market President for the states of Georgia and Florida, overseeing over 80 banking centers in her footprint.",
"Janean\u2019s influence extends far beyond balance sheets and branch operations. She is a passionate advocate for mentorship and community service, dedicating her time to organizations like I Am B.E.A.U.T.I.F.U.L, Lift Atlanta, the USO Military, and Habitat for Humanity. Through these roles, she uplifts others, igniting change and creating opportunities for those in need. As a proud member of Alpha Kappa Alpha Sorority, Inc. and the One Hundred Black Women of Metropolitan Atlanta, Janean champions initiatives that empower small businesses and foster community growth.",
"Her illustrious career hasn\u2019t gone unnoticed. Featured in a documentary on HBO Max and gracing the cover of \u201cGame Changers\u201d magazine, Janean has earned accolades such as being named one of the Top 50 Most Powerful Women in Atlanta by ATL+ Magazine in 2024 and 2025, one of the Top 50 Women in the Southern Crescent Region and, in December of 2025, Janean became a published author and founder of \u201cSis, Get your purse in order!\u201d These honors reflect not just her professional prowess, but her commitment to being a role model for future leaders.",
"Despite the accolades, Janean\u2019s heart remains firmly grounded in her personal life. A devoted wife and loving mother, she knows that true success is measured not just in achievements, but in the love and legacy we cultivate at home. With a spirit that inspires and a vision that transforms, Janean is a beacon of hope and an architect of change in both her industry and her community."]

AMELIA = ["As a boundary-pushing around-the-world pilot, <strong>Amelia Rose Earhart</strong> knows exactly what it takes to venture into uncharted territory \u2014 with confidence.",
"With the odds stacked against her, Amelia not only trained to become a pilot, but to become the type of pilot to honor the person she was named after, Amelia Mary Earhart, by piloting a single-engine airplane (Pilatus PC-12NG) 28,000 nautical miles around the globe. To accomplish this, Amelia developed a flight plan all her own, and while reporting full-time as an on-air TV helicopter reporter, completed private, instrument and commercial pilot training, crafted an entrepreneurial and strategic business plan to design, fund and market her around-the-world attempt, raised close to $2 million in partnerships with 28 corporations, founded and ran the Fly With Amelia Foundation, which sent numerous teenage girls to flight school, and more.",
"Today, Amelia Rose Earhart is a full-time speaker, podcast host, and artist who incorporates the lessons of her 2014 global flight into every aspect of her professional and personal life. Amelia is excited to share the remaining funds from the Fly With Amelia Foundation with another aviation charity helping to promote women in aviation and will be sharing exciting details soon. From the Air Force Thunderbirds, to the Reagan Library, to corporations like Capital One, Lockheed Martin and United Healthcare, Amelia\u2019s list of clients who trust her message of agility continues to grow.",
"Amelia is currently submitting her manuscript, The Ups and the Downs of Turbulence, which she wrote with author Kristin Clark Taylor, during Winter of 2020. Memorabilia from Amelia\u2019s flight around the world can be found at her permanent display at Wings Over the Rockies Air and Space Museum in Denver, CO."]

BURNS = ["Mike Burns is CSX\u2019s Senior Vice President, Chief Legal Officer, and Corporate Secretary. Appointed in 2025, he oversees the company\u2019s legal and regulatory affairs, government affairs, community investments, the corporate secretary\u2019s office, risk management, freight claims, police and infrastructure protection, environmental and hazardous materials, and audit functions.",
"Mike brings a wealth of experience to his role, having previously served as CSX Vice President and General Counsel. Since joining the company in 2006, he has advanced through positions of increasing responsibility, initially focusing on employment and benefits law before assuming responsibility for the full law department and additional functions, including corporate secretary, risk management, environmental and hazardous materials, insurance and freight claims functions. Prior to joining CSX, Mike practiced labor and employment law for five years at a prestigious law firm in Indiana.",
"Beyond his legal expertise, Mike participated in the 2024 World50 Next Leader Program. Additionally, he serves on the Board of Directors of the Florida State College of Jacksonville Foundation.",
"Mike holds a bachelor\u2019s degree from Wabash College and a Juris Doctor from the Indiana University Robert H. McKinney School of Law. He has also completed the CSX Executive Development Program at Harvard Business School."]

LEWIS = ["Terri Lewis is Chief Human Resources Officer for Landstar Systems, Inc. and its 1,400 employees throughout the United States. Landstar is a technology-enabled, asset-light provider of integrated transportation management solutions delivering safe, specialized transportation services to a broad range of customers utilizing a network of agents, third-party capacity owners and employees.",
"As CHRO and a member of Landstar\u2019s Executive Leadership Team, Terri is responsible for talent acquisition and retention, leadership effectiveness, learning and development, succession planning, organizational design, total rewards, employee relations, and human resources compliance. She partners closely with executive leadership and the Landstar Board of Directors to advance a high-performance culture, strengthen Landstar\u2019s employer brand, and ensure the company\u2019s people strategy supports long-term growth and organizational effectiveness as a transportation leader.",
"Terri has over twenty-five years of human resources leadership experience in both the public and private sectors. She has held senior human resources leadership roles with organizations including One Call, Pontoon Solutions, PSS World Medical (now McKesson Corporation), CHEP USA (a unit of Brambles Limited), and General Electric. She holds a master\u2019s degree in human resources management from the University of South Carolina and a bachelor\u2019s degree in business management from Clemson University."]

PHILLIPS = ["Ted Phillips joined JEA as its Chief Financial Officer in August 2021. In this role, his responsibilities include oversight of Financial Services, Treasury Services, Risk Management Services, Supply Chain, Procurement, Facilities and Fleet Services, and Enterprise Planning and Analytics. He brings with him a wealth of experience leading finance teams for public utilities.",
"Prior to joining JEA, Ted worked for 10 years with Huntsville (Ala.) Utilities, leading teams in Finance/Accounting, MIS, Technical Services, Purchasing, Stores &amp; Warehouses, Fleet and Facilities. Previously, he spent over 20 years in the public sector working for the cities of Shelby, North Carolina; Monroe, North Carolina; Mecklenburg County, North Carolina; and the State Auditor\u2019s office in Missouri.",
"Ted received a Bachelor of Science in Business Administration from Southeast Missouri State University. He has been an active member in the communities he has called home, having served on the boards of the United Way and The Schools Foundation in Huntsville, and in various United Way campaign leadership positions. He is currently a member of the Salvation Army of Northeast Florida Advisory Board. He has also been a longtime leader for the Boy Scouts of America."]

SWIETEK = ["Taryn Swietek is an award-winning executive cybersecurity and risk leader with a proven track record of protecting multi-billion-dollar business operations for global organizations like Google, Deloitte, and Citigroup. Taryn specializes in architecting enterprise-wide security strategies and deploying comprehensive risk management frameworks that align with corporate objectives. A key part of her role involves advising the C-suite and the Board on emerging technology threats and risk posture. She is deeply committed to building and mentoring high-performance teams while fostering a durable culture of shared risk ownership and security awareness. With over 20 years of industry experience, Taryn is passionate about solving complex security challenges through sound governance and control guidance. Her leadership style is rooted in empowering others through positivity, empathy, and understanding. As a Member of the IANS Faculty, she remains an avid learner, committed to keeping pace with the ever-evolving cybersecurity landscape."]

speakers_body = page_hero("Current Speakers &amp; Panelists",
    "Visit us in early 2027 for information about our next Forum. In the meantime, read about our 2026 Forum speakers.") + f"""
<section class="section">
  <div class="container">
    <h2>2026 Keynote Speakers</h2>
    {speaker_block("Janean C. Armstrong", "Author and Seasoned Banking Executive", "images/people/janean-armstrong.jpg", JANEAN, "https://www.linkedin.com/in/janeanarmstrong02", "Learn more about Janean")}
    <div class="mb-2"></div>
    {speaker_block("Amelia Rose Earhart", "Aviator, Author, and Founder of the Flying with Amelia Foundation", "images/people/amelia-rose-earhart.jpg", AMELIA, "https://www.ameliaroseearhart.com/", "Learn more about Amelia")}
  </div>
</section>
<section class="section section--tint">
  <div class="container">
    <h2>2026 Panelists</h2>
    {speaker_block("Michael Burns", "SVP, Chief Legal Officer and Corporate Secretary, CSX", "images/people/michael-burns.jpg", BURNS)}
    <div class="mb-2"></div>
    {speaker_block("Terri Lewis", "VP, Chief Human Resources Officer, Landstar Systems", "images/people/terri-lewis.jpg", LEWIS)}
    <div class="mb-2"></div>
    {speaker_block("Ted Phillips", "Chief Financial Officer, JEA", "images/people/ted-phillips.jpg", PHILLIPS)}
    <div class="mb-2"></div>
    {speaker_block("Taryn Swietek", "Head of Governance \u2013 gTech, Google", "images/people/taryn-swietek.jpg", SWIETEK)}
    <div class="btn-row"><a class="btn btn--outline" href="./previous-speakers.html">View Previous Featured Speakers</a></div>
  </div>
</section>
"""
page("speakers.html", "Current Speakers & Panelists",
     "Keynote speakers and panelists from the 2026 Jacksonville Women's Leadership Forum.",
     speakers_body)

# ============================================================== PREVIOUS SPEAKERS & EVENTS
TOPICS = [
    ("2026", "\u201cShe Leads: Igniting Vision, Elevating Voice, and Delivering Value\u201d"),
    ("2025", "\u201cLeading the Way: Empowering Women Through Mentorship and Sponsorship\u201d"),
    ("2024", "\u201cFuture of Work: Women Redefining Tomorrow Through Technology\u201d"),
    ("2023", "\u201cThe Great Rethink \u2013 Reconnecting with Purpose, People and Perceptions\u201d"),
    ("2022", "\u201cChange &amp; Transformation \u2013 An Opportunity for Creativity &amp; Innovation\u201d"),
    ("2021", "\u201cAuthentic Leadership \u2013 Acting on What Matters\u201d"),
    ("2020", 'Dave Dallas: \u201cNetworking With Authenticity\u201d (download Dave\u2019s <a href="https://www.jwlf.org/wp-content/uploads/2020/01/Dave_Dallas_Networking_with_Authenticity-1.pdf">one-page checklist</a>)'),
    ("2019", "\u201cBe Fearless! Influence, Innovate, and Inspire!\u201d"),
    ("2018", "\u201cCharting Your Career Path: The Art of Navigation and Negotiation\u201d"),
    ("2017", "\u201cGame On! The Power of Women \u2013 It\u2019s Our Time to Lead!\u201d"),
    ("2016", "\u201cTraits of Resilient Leaders\u201d"),
    ("2015", "\u201cElevating your Game: Strategies to Build Your Brand, Raise your Confidence and Maximize your Network!\u201d"),
    ("2014", "\u201cThe Way Women Lead\u201d"),
]
topics_html = "".join(f"<li><strong>{y}</strong> \u2014 {t}</li>" for y, t in TOPICS)

def prev_speaker(name, role, img, paragraphs, link=None):
    body = "".join(f"<p>{p}</p>" for p in paragraphs)
    link_html = f'<p><a href="{link}">Read more</a></p>' if link else ""
    return f"""<article class="card speaker" data-reveal>
  <img src="./{img}" alt="{name}" loading="lazy">
  <div>
    <h3>{name}</h3>
    <p class="person-role">{role}</p>
    <details class="bio"><summary>Biography</summary>{body}{link_html}</details>
  </div>
</article><div class="mb-2"></div>"""

PREV = [
("Janean C. Armstrong", "Author and Seasoned Banking Executive", "images/people/janean-armstrong.jpg", JANEAN, "https://www.linkedin.com/in/janeanarmstrong02"),
("Amelia Rose Earhart", "Aviator, Author, and Founder of the Flying with Amelia Foundation", "images/people/amelia-rose-earhart.jpg", AMELIA, "https://www.ameliaroseearhart.com/"),
("Becky Blalock", "Best-Selling Author, Managing Director at Advisory Capital", "images/people/becky-blalock.jpg", [
 "<strong>Becky Blalock</strong> has over 30 years of executive management and board-level experience. During her career with Southern Company, she held a variety of leadership positions in various organizations including accounting, finance, marketing, corporate communications, external affairs, and customer service.",
 "As the former Senior Vice President and Chief Information Officer for Southern Company, she spent almost a decade directing IT strategy and operations across the nine subsidiaries of Southern Company. Under her leadership, Southern Company invested more than a billion dollars in new technology initiatives and was recognized as one of the utility industry\u2019s most innovative companies and one of the best places to work in IT.",
 "Ms. Blalock is recognized as a thought leader in several industries and is the recipient of numerous honors, including CIO of the Year in the utility industry, a Premier IT Leader by Computerworld magazine, Agenda Magazine\u2019s Digital 50, a CIO Lifetime Achievement Award and the Legacy Award from Women in Technology.",
 "She is currently the Managing Partner at Advisory Capital, a consulting firm providing strategic insight for companies involved in the energy, information technology, and medical industries. In 2013, her bestselling book DARE: Straight Talk on Confidence, Courage, and Career for Women in Charge (Wiley) was published. Ms. Blalock is a sought-after speaker for corporate, community and philanthropic events.",
 "Ms. Blalock is an advocate for women and children, and chairs board committees for The Community Foundation of Greater Atlanta. Ms. Blalock is on the board of the Electric Power Research Institute. She chairs the Emory Healthcare Advisory Board and serves on the Advisory Boards of Catavolt, Gigabark and SolAmerica Energy."],
 "https://www.beckyblalock.com/"),
("Rashmi Airan", "Speaker, Consultant, and Unapologetic Truth-Teller", "images/people/rashmi-airan.jpg", [
 "<strong>Rashmi Airan</strong> is a force of nature. A keynote speaker, consultant, and unapologetic truth-teller, she shakes up rooms with her raw, riveting story \u2014 one that challenges everything you think you know about leadership, ethics, and the hidden traps of ambition. She doesn\u2019t just speak about resilience; she lives it, proving that even the most crushing failures can be transformed into a catalyst for growth, authenticity, and unshakable courage.",
 "As a first-generation Indian American, Rashmi was raised to chase excellence. She graduated with honors from Columbia Law School, thriving in corporate America, and building her own law practice. But success has a dark side. During the housing boom, she made a decision that, at the time, seemed small \u2014 but had devastating consequences. A single ethical blind spot, fueled by the pressure to provide for her children, led to a federal prison sentence for bank fraud.",
 "Prison shattered everything she thought she knew about herself. And then? She rebuilt \u2014 stronger, bolder, and more awake than ever. Through six months behind bars, Rashmi stripped away the layers of ego, guilt, and fear that had defined her. She emerged with a powerful message: our worst mistakes don\u2019t define us \u2014 our response to them does.",
 "Now a \u201crecovering government, corporate, and real estate lawyer,\u201d Rashmi is a globally recognized speaker who fearlessly tackles the complexities of human behavior, decision-making, and ethical leadership. With 30+ years in business, law, and finance, she has a front-row seat to the pressures that push good people into bad decisions \u2014 and she\u2019s on a mission to wake up individuals and organizations before they fall into the same traps.",
 "Her insights are backed by cutting-edge research in behavioral psychology, ethics, and leadership, and she\u2019s partnered with global powerhouses like Coca-Cola, Cardinal Health, Merck, Comcast, Sotheby\u2019s, and Hershey\u2019s. Deloitte has recognized her transformational impact, and her story has been featured on ABC, PBS, The Washington Post, and The Wall Street Journal.",
 "Rashmi doesn\u2019t do surface-level inspiration \u2014 she sparks deep, uncomfortable, necessary conversations. She challenges Fortune 100 leaders, financial firms, legal teams, and women\u2019s groups to confront their blind spots, own their decisions, and rise through their struggles with integrity and courage."],
 "https://rashmiairan.com/"),
("Rhonda Snipe", "Principal Managing Director, Dale Carnegie", "images/people/rhonda-snipe.png", [
 "<strong>Rhonda Snipe</strong> is the Principal Managing Partner for the Dale Carnegie Franchise in North Florida and Southeast Georgia, leading a professional team of Senior Sales Consultants and experienced Dale Carnegie Certified Trainers, delivering exceptional leadership training in Jacksonville, Gainesville, Lake City, and Tallahassee, FL, and sparking momentum in Valdosta, GA. Her career demonstrates a unique blend of high-level military leadership experience and expertise in Dale Carnegie\u2019s renowned human relations and leadership principles.",
 "Dale Carnegie Training reflects her passion for developing leaders and empowering individuals to reach their full potential. As a Certified Dale Carnegie Trainer and now Managing Partner, she leverages her expertise in leadership and communication to deliver transformative training programs. Her high-stakes military leadership skills with proven principles of Dale Carnegie equip her with the experience needed to guide individuals and organizations to lead. Prior to her current role, Rhonda served as a Deputy Legislative Assistant in the Office of the Chairman of the Joint Chiefs of Staff at the Pentagon, providing direct support to the highest-ranking military officer in the United States. This experience honed her skills in strategic communication, policy analysis, and advising senior leadership on congressional affairs. Her ability to navigate complex situations and deliver impactful results under pressure is a testament to her strong leadership and organizational capabilities.",
 "Rhonda earned a master\u2019s degree in political management from George Washington University, and a master\u2019s degree in Military Operational Science from the United States Army Command and General Staff College."],
 "https://inspiredgrowthleader.com/"),
("Heather McGowan", "Best-Selling Author, Future of Work Strategist", "images/people/heather-mcgowan.jpg", [
 "Future-of-work strategist <strong>Heather E. McGowan</strong> helps leaders prepare their people and organizations for the post-pandemic world of work. The last few years have forever changed where we work, who works, how we work and measure work, what we do for work, and, most importantly, why we work. McGowan is a sense maker, a dot connector, a deep thinker, and a pattern matcher who sees things that others miss. Heather gives people the courage and insight that illuminates their path forward. She\u2019s transforming mindsets and entire organizations around the globe with her message about how the next phase of work will focus on continuous learning, rather than simply learning once in order to work. Pulitzer Prize\u2013winning NYT columnist Thomas Friedman frequently quotes Heather in his books and columns and describes her as \u201cthe oasis\u201d when it comes to insights into the future of work. In 2020 Heather was recognized as one of the top 50 female futurists in the world by Forbes. Heather\u2019s sessions help employees and leaders alike prepare for and adapt to jobs that do not yet exist.",
 "McGowan has provided keynote addresses for audiences from start-ups to government organizations to universities to publicly traded Fortune 100 companies, including AMP Financial, SAP, Abbvie, Biogen, Fidelity, FIS, Mastercard, AT&amp;T, Financial Times, Siemens, Microsoft, Google, Facebook, Kaiser Permanente, JPMorgan Chase, Lockheed Martin, MassMutual, MetLife, Best Buy, Raytheon, The US Army, Accor Hotels, Paramount, Chevron, AARP, Zendesk, Tableau, de Beers, Professional Beauty Association, and The World Bank among hundreds of others. Heather addresses audiences in person from small summits for C-suite executives to large events in the tens of thousands. Her virtual talks have reached hundreds of thousands. Often quoted in the media, notably in the New York Times, McGowan serves on the advisory board for Sparks &amp; Honey, a New York\u2013based culture-focused agency looking to the future for brands. McGowan\u2019s academic work has included roles at Rhode Island School of Design, and Jefferson University, where she was the strategic architect of the first undergraduate college focused exclusively on innovation. In 2019 Heather was appointed as a faculty member of the Swinburne University Centre for the New Workforce in Melbourne, Australia. In 2022, McGowan was awarded an honorary doctorate from Pennsylvania College of Art and Design in addition to earning her MBA from Babson College and her BFA in Industrial Design from Rhode Island School of Design. McGowan is the co-editor and author of the book Disrupt Together: How Teams Consistently Innovate and a Forbes contributor. McGowan\u2019s first book on the future of work, published in 2020, The Adaptation Advantage: Let Go, Learn Fast, and Thrive in the Future of Work, reached number three in business management books on Amazon and was named one of the best business books of 2021 by Soundview. McGowan\u2019s most recent book The Empathy Advantage: Leading the Empowered Workforce published in March 2023 and is a finalist for the Next Big Idea Book Club and identified as a top ten business book to read in 2023 by Business Chief."],
 "https://heathermcgowan.com/"),
("Stephanie O\u2019Connor", "Senior Vice President, City Utilities of Springfield, MO", "images/people/stephanie-oconnor.jpg", [
 "<strong>Stephanie O\u2019Connor</strong> has the unique ability to bring people and technology together! Her career began at City Utilities of Springfield, Missouri in 1992 as an intern in Information Technology. Now, she is the Senior Vice President \u2013 Chief Technology and People Officer and is responsible for Information Technology, Human Resources, and SpringNet Broadband Fiber, a division of City Utilities. In addition, she serves as a liaison to City Utilities\u2019 Board of Public Utilities. She holds a B.S. in Computer Information Systems from Missouri State University and is active in the community, serving on the Springfield Area Chamber of Commerce Board of Directors, Leadership Springfield Board of Directors, Springfield Tech Council, Human Capital Council of Southwest Missouri, Community Blood Center of the Ozarks Board of Directors, Women United as part of United Way of the Ozarks, and Electricity Subsector Coordinating Council Cyber Mutual Assistance Committee. Stephanie has a passion for helping others, and this is reflected in her establishment of the Strong Women Achieving Goals (SWAG) program. In 2021, Stephanie was named one of BIZ417\u2019s Women Who Mean Business, Springfield Business Journal\u2019s 20 Most Influential Women, and received the Missouri Public Utility Alliance Honor Award which recognizes employees who have significant contributions towards meeting their municipal utilities\u2019 objectives. In 2018, she was the first woman selected as Association of Information Technology Professionals (AITP) IT Executive of the Year. She is a graduate of Leadership Springfield Signature Class 34, a member of Sunrise Rotary, and a 2001 Springfield Business Journal 40 Under 40 recipient. It\u2019s evident that Stephanie is making a positive difference in the Springfield community and is excited to share how women can leverage technology to enhance their ability to be SWAG!"],
 "https://www.linkedin.com/in/stephanie-o-connor-4b07493/"),
("Amanda Slavin", "Educator, Author, Advisor", "images/people/amanda-slavin.jpg", [
 "Amanda Slavin is a renowned educator with a Masters in Curriculum and Instruction, a Cannes Lion award-winning community designer, and Forbes 30 Under 30 honoree. Her Seventh Level Engagement Framework has transformed how we measure learning success and is taught in MBA programs worldwide. Amanda is the author of the best-selling book, \u201cThe Seventh Level,\u201d and co-founder of CatalystCreativ and CatalystU, where she\u2019s increased engagement for top brands like Google and Coca-Cola. Additionally, Amanda is a co-founder of Runway Health and is an advisor to 20+ startups, including HubSpot. She has been featured in Inc, Entrepreneur, Adweek, and Fast Company publications. Amanda is a sought-after speaker, with two TEDx talks under her belt, and has spoken at prestigious events such as INBOUND and Summit."],
 "https://amandaslavin.com/"),
("Dana Barrett", "Entrepreneur, Award-Winning TV, Radio, and Podcast Host", "images/people/dana-barrett.png", [
 "<strong>Dana Barrett</strong> is a former tech executive, a serial entrepreneur, and an award-winning TV, radio, and podcast host. She was a candidate for US Congress in 2020 and was elected to serve as a County Commissioner in November of 2022. She is also a communications consultant and frequent emcee and speaker. Dana has written for Forbes and the Atlanta Business Chronicle and has appeared on Headline News to discuss women\u2019s workplace issues, including pay equity and sexual harassment. A breast cancer survivor, and a long-time advocate for women, Dana serves on several nonprofit boards focusing on these issues. Originally from Philadelphia, she has called Atlanta home since graduating from Cornell University in 1988. Dana is proud to have raised her now full-grown daughter as a working single mom and believes that failure is just a pit stop on the road to success."],
 "https://www.linkedin.com/in/thedanabarrett/"),
("Sukhinder Singh Cassidy", "Tech Executive", "images/people/sukhinder-singh-cassidy.jpg", [
 "<strong>Sukhinder Singh Cassidy</strong> is one of the most well-respected female tech executives in Silicon Valley. Named one of Fast Company\u2019s Most Creative People in Business, she\u2019s served as president of StubHub, helped scale companies like Google and Amazon, and founded theBoardlist: a premium talent marketplace for diverse leaders. But despite her many successes, she\u2019s the first to admit her path hasn\u2019t always been linear. In her book Choose Possibility, Singh Cassidy reveals the many poor choices, misfires, and unexpected headwinds she\u2019s encountered along her path \u2014 providing a thoughtful new perspective on risk-taking: what it is, what it isn\u2019t, and how to master it to achieve lasting success."],
 "https://www.thelavinagency.com/speakers/sukhinder-singh-cassidy"),
("Brenda Reynolds", "Executive Coach, Best-Selling Author, TEDx Speaker", "images/people/brenda-reynolds.jpg", [
 "Brenda K. Reynolds, M.S., is a change agent who provides organization development and leadership solutions to Fortune 500s, non-profits, education, and individuals navigating complexity. Brenda draws on her own corporate leadership roles and extensive consulting experience to equip clients with easy-to-apply strategies and inspiration during their \u201cnow what?\u201d moments. She has been trusted by a broad range of clients including Special Olympics, Delaware Hospice, Sherwin Williams, Moen, QVC, McDonalds, and Penn State University.",
 "Brenda is author of Amazon best-seller TBD \u2013 To Be Determined: Leading with Clarity and Confidence in Uncertain Times (2017). She\u2019s also the creator of the \u201cNow What?\u201d Transformation\u2122 Clarity Card Deck and Kit. Brenda also hosts the COMING TO.GET.HER series and online community for women in leadership.",
 "Brenda has graced the TEDx stage as a speaker on Navigating Transition Fog, and has delighted and inspired audiences in a variety of venues, including Vistage International, The International Organization Development and Change Conference in Beijing, China, and The Designed for Impact Bermuda Women\u2019s Conference. She is a frequent radio and podcast guest, residing in the Greater Philadelphia area, and proud mom of two amazing sons!"],
 "https://www.brendakreynolds.com/"),
("Brigid Schulte", "Director of the Better Life Lab", "images/people/brigid-schulte.jpg", [
 "Brigid is the Director of the Better Life Lab and The Good Life Initiative at New America, a nonpartisan think tank, and author of the New York Times bestselling Overwhelmed: Work, Love and Play When No One Has the Time, which was named a notable book of the year by the Washington Post and NPR. She has spoken all over the world about how to make time for a better life by redesigning work cultures to focus on effective work, by re-imagining gender roles for a fairer division of labor and opportunity at work and at home, by rewiring social policy to meet the needs of diverse 21st-century families, and, instead of seeking status in busyness, by recapturing the value of leisure.",
 "She was an award-winning journalist at the Washington Post and Washington Post Magazine, where she was part of the team that won the 2008 Pulitzer Prize. Her work has appeared in a number of publications, including Time, the Boston Globe, the Toronto Globe &amp; Mail, the Guardian, and the Sydney Morning Herald. She has been quoted as an expert or featured in numerous publications, including Forbes, Fortune, the Atlantic, The Times of London, Macleans, the Irish Times, The Financial Times and Fast Company, and has appeared on the Today Show, Good Morning America, the Katie Couric Show, MSNBC, CNN, Morning Joe, the BBC, CBC, Fresh Air with Terry Gross, NPR\u2019s Morning Edition, Tell Me More, On Point, the Diane Rehm Show, the Leonard Lopate Show, the Bob Edwards Show, Efecto Naim with Moises Naim, the Australian Broadcast Company, and other television and radio programs.",
 "She lives in Alexandria, Virginia with her husband, Tom Bowman, who covers the military for NPR, and their two children. She grew up in Portland, Oregon, and spent her summers in Wyoming on her family\u2019s sheep ranch, where she did not feel so overwhelmed."],
 None),
("Nadia Bilchik", "President of Greater Impact Communications", "images/people/nadia-bilchik.jpg", [
 "Nadia, President of Greater Impact Communication, is an internationally renowned television personality, communication and professional development training expert, author and keynote speaker.",
 "Nadia has anchored and hosted feature programs for CNN International, CNN Airport Network and MNet Television (South Africa) and reported for CNN Weekend. Nadia is currently Editorial Producer for CNN\u2019s Weekend Morning program.",
 "Her uniquely dynamic, entertaining and substantive approach to communication skills training comes from her extensive experience in conducting training workshops, coaching business professionals and delivering keynote addresses to a broad range of audiences both in the USA and globally, as well as interviewing high-profile figures, celebrities and corporate leaders. They include President Nelson Mandela, Tom Hanks, Meryl Streep, Anthony Hopkins, Morgan Freeman, Matt Damon, and George Clooney amongst others.",
 "A sought-after moderator, Nadia has hosted events for Coca-Cola, Ted Turner\u2019s Captain Planet Foundation, as well as the International Women in Film Crystal Awards with Alfre Woodard. She has opened the SOS Children\u2019s Villages in South Africa with President Nelson Mandela.",
 "Nadia is the author of three books including The Little Book of Big Networking Ideas, small changes BIG IMPACT \u2013 Maximize the Power of Your Presence and Leverage the Power of Your Personal Brand, and OWN YOUR SPACE \u2013 The Toolkit for the Working Woman.",
 "Nadia received a Licentiate in Speech and Drama from Trinity College, London, and a Bachelor of Arts degree with majors in Drama and English from the University of Cape Town, South Africa."],
 "https://nadiaspeaks.com/about/"),
("Libby Gill", "Leadership Expert", "images/people/libby-gill.jpg", [
 "Helping you be your most fearless self in work and life, Libby Gill guides your group of emerging and established women leaders to challenge limiting assumptions, take bold risks, and support each other on their journey to success. She looks at issues we continue to struggle with, despite our growth and gains, including career advancement, wage inequality, gender bias, and work/life balance.",
 "In her dynamic interactive keynote, Libby shares leadership strategies as well as scientific data on hope theory to show participants how to link beliefs and behaviors to create a powerful future-focused vision. They\u2019ll leave your event feeling renewed purpose, recharged passion, and reinvigorated commitment to excellence.",
 "The former head of communications for Sony, Universal, and Turner Broadcasting, Libby is the CEO of Libby Gill &amp; Company, an executive coaching and consulting firm. She has been featured on CNN, NPR, the Today Show, and in BusinessWeek, The New York Times, Wall Street Journal, and more. Libby has delivered keynote presentations for women\u2019s leadership events including ADP, AMC Networks, EY, Genentech, Intel, Microsoft, Safeway, Urenco Nuclear, Wells Fargo, Viacom, Zurich Insurance, and many others."],
 "https://libbygill.com/"),
("Tammy Heermann", "Leadership Development Expert", "images/people/tammy-heermann.jpg", [
 "Tammy Heermann is a sought-after advisor who helps individuals and organizations get serious about leadership. She has developed pioneering and multiple award-winning programs aimed at changing mindsets to achieve high performance. Passionate about advancing female leaders, she is specifically sought out by Fortune 500 companies for her expertise in gender diversity and programs that accelerate female talent around the world.",
 "While having significant impact in the C-Suite, she is happiest when pushing up-and-coming leaders to break through organizational and self-imposed barriers to reach their potential. With real-world stories of her own journey from Senior Consultant to Senior Vice-President, people express the value of Tammy\u2019s down-to-earth, practical style in creating an environment of trust in a room of strangers.",
 "Tammy sits on the Women\u2019s Leadership Advisory Committee for Women in Communications and Technology. She is a graduate of the London School of Economics with a Master of Science degree in Personnel Management and Industrial Relations and holds an Honours Bachelor of Commerce degree from the University of Saskatchewan. She lives in Toronto with her daughter Ava and husband Thomas."],
 "https://www.tammyheermann.com/"),
("Dr. Leigh Thompson", "Kellogg School of Management at Northwestern", "images/people/leigh-thompson.jpg", [
 "Dr. Leigh Thompson is the J. Jay Gerber Professor of Dispute Resolution &amp; Organizations in the Kellogg School of Management at Northwestern University. She is the director of the Kellogg Team and Group Research Center, the Kellogg Leading High Impact Teams Executive program, and co-director of the Constructive Collaboration Executive program and the Negotiation Strategies Executive program. In addition, she is an Adjunct Professor of Psychology at Northwestern.",
 "Her research focuses on negotiation skills and strategies, group decision making, creativity, and analogical reasoning. Her most recent research projects include investigations of divergent versus convergent thinking on negotiation performance; mindfulness and negotiation performance; gender and the use of ethically-questionable negotiation strategies; embarrassment and pride and their effects on creativity; and how analogical reasoning improves negotiation performance.",
 "She has published more than 130 research articles and chapters in edited books. She has authored 9 books, including Stop Spending, Start Managing (Harvard Business Review, 2015); Making The Team (6th edition, Pearson); The Mind and Heart of the Negotiator (6th edition, Pearson, 2015); Creative Conspiracy: The New Rules of Breakthrough Collaboration (Harvard Business Review, 2013); and The Truth About Negotiations (2nd edition, Pearson, 2013)."],
 "http://www.leighthompson.com/"),
("Jan Hargrave", "Author & Professional Public Speaker", "images/people/jan-hargrave.jpg", [
 "Jan Hargrave is an expert on nonverbal communication. She is presently the CEO of Jan Hargrave and Associates, a Houston-based consulting firm, and continues to provide many of today\u2019s leading corporations such as Merrill Lynch, Rockwell, El Paso Energy, Exxon, Chase Manhattan Bank, and NASA with seminars and specialized training in how to take advantage of nonverbal communication. She has been a guest on many shows, including but not limited to The Maury Povich Show, The Ricki Lake Show, The Gayle King Show, Talk Soup and The Learning Channel."],
 "http://www.janhargrave.com/store/about.php"),
("Corinne Costa Davis", "Former CHRO, E*Trade Financial Services", "images/people/corinne-costa-davis.jpg", [
 "Ms. Corinne Costa Davis is an experienced corporate executive who held leadership roles as a Chief Human Resources Officer, Chief Information Officer and Chief Operating Officer. She has worked with global organizations in multiple industry sectors including banking, asset management, financial services, telecommunications, insurance, healthcare and philanthropy. Her expertise is in driving productivity and bottom-line results through the transformation of corporate functions (Human Resources, Technology, Operations, Finance, Procurement and Marketing) from traditional infrastructure models into best-practice providers of products and services.",
 "She has chaired Corporate Giving, Health &amp; Welfare Benefit and 401k Committees for publicly traded companies. Additionally, she has worked closely with independent Boards of Directors in the development of compensation plan design and succession planning processes. She has advised executive teams and external boards as they managed significant operating model and organizational structure transformation.",
 "Corinne holds a B.S. and M.B.A. from Seton Hall University. Additionally, she is a professionally trained modern dancer who continues to practice this performance art. Corinne sits on the Board of Directors of the Chronic Obstructive Pulmonary Disease Foundation and is the Chairperson of the Foundation\u2019s Development Committee."],
 "https://www.linkedin.com/in/corinne-costa-davis-5827328/"),
("Dr. Tracy Alloway", "Award-Winning Psychologist", "images/people/tracy-alloway.jpg", [
 "Dr. Tracy Alloway is an award-winning psychologist, TEDx speaker and author. Dr. Alloway\u2019s research has contributed to the scientific understanding of working memory, specifically in relation to education and learning needs. She has shared her research with organizations such as the National Center for Learning Disabilities, The Japanese Society for Developmental Psychology and the Individual Development and Adaptive Education of Children At Risk in Germany, among others. In addition to more than 100 peer-reviewed journal articles and book chapters, 7 books, and 2 standardized test batteries on the topic of working memory, her work has also been featured on Good Morning America, the Today Show, Forbes, Bloomberg, The Washington Post, and Newsweek, to name only a few. Dr. Alloway also blogs for Psychology Today and the Huffington Post."],
 "http://tracyalloway.com/"),
("Dr. Helen Fisher", "PhD, Biological Anthropologist", "images/people/helen-fisher.jpg", [
 "Dr. Helen Fisher is an American anthropologist who specializes in the evolution, biology, and psychology of human sexuality, monogamy, adultery and divorce, gender differences in the brain, and the neural chemistry of romantic love and attachment. She is a Senior Research Fellow at the Kinsey Institute at Indiana University as well as a member of the Center for Human Evolutionary Studies in the Department of Anthropology at Rutgers University. Prior to her work at Rutgers she was a research associate at the American Museum of Natural History in New York. She is a contributor on ABC News as well as at the 2006 and 2008 TED Conferences."],
 "http://www.helenfisher.com/about.html"),
("Tiffany Dufu", "Chief Leadership Officer for Levo", "images/people/tiffany-dufu.jpg", [
 "Tiffany Dufu is a nationally recognized expert on women\u2019s and millennial leadership, and the author of \u201cDrop the Ball: Achieve More by Doing Less.\u201d In 2012, she was named one of Huffington Post\u2019s 19 Women Who Are Leading the Way. Tiffany was featured in The Seattle Times, The New York Times, NPR and Bloomberg for raising over $20 million toward causes for women and girls. She is a frequent speaker on women\u2019s leadership and nonprofit fundraising, recently presenting at Fortune magazine\u2019s Most Powerful Women Summit and TEDxWomen."],
 "https://www.levo.com/tiffany-dufu"),
("Fawn Germer", "Bestselling Author", "images/people/fawn-germer.png", [
 "Fawn Germer is a four-time Pulitzer Prize-nominated author and is one of the nation\u2019s most sought-after motivational speakers and corporate trainers. Oprah featured Germer and her book Hard Won Wisdom on her award-winning talk show. Germer has personally interviewed more than 300 of the most accomplished leaders of our times, including Olympic athletes, CEOs, prime ministers, presidents, Academy Award winners and many others who shared with her their secrets of true success."],
 "http://fawngermer.com/about-fawn/bio"),
("Betsy Myers", "Founding Director, Center for Women and Business at Bentley University", "images/people/betsy-myers.jpg", [
 "Betsy Myers is the founding director of Bentley University\u2019s Center for Women and Business. She was also a senior advisor in former President Barack Obama\u2019s presidential campaign. She served at first as his Chief Operating Officer and then as the Chair of Women for Obama. She also spent several years at Harvard\u2019s School for Government, ending as the Executive Director of its Center for Public Leadership. During the Clinton Administration, Myers spent several years at the U.S. Small Business Administration in posts that included Director of the Office of Women\u2019s Business Ownership, President Clinton\u2019s senior adviser on women\u2019s issues, and Director of the Office for Women\u2019s Initiatives and Outreach."],
 "http://betsymyers.com/about-betsy"),
("Pegine Echevarria", "CEO of Team Pegine Inc.", "images/people/pegine-echevarria.jpg", [
 "Pegine Echevarria is the CEO of the locally based Team Pegine Inc. and is also a motivational speaker, author, life coach and entrepreneur. Her company Team Pegine ranks amongst the 50 fastest growing businesses in Northeast Florida. Echevarria also created the foundation Success4Vets to help veterans acquire leadership skills and settle back into civilian life. She is a Certified Speaking Professional member of the National Speakers Association and is the only Latina inducted into the 58-member Motivational Speakers Hall of Fame. She is also the only Latina in the Million Dollar Speakers Group.",
 "Echevarria was also named the \u201c2010 Women in Business Champion of the Year for the North Florida District and the State of Florida.\u201d She has been featured in Minority Business Entrepreneur Magazine and was on the cover as a \u201cWoman Who Rocks In Business.\u201d She was interviewed by columnist Devin Thorpe in the Forbes article \u201cRenowned Speaker Offers Tips To Women Entrepreneurs.\u201d"],
 "http://www.pegine.com/about-pegine-echevarria/"),
("Susan Packard", "Co-founder of Scripps Networks", "images/people/susan-packard.jpg", [
 "Susan Packard is the co-founder of Scripps Networks Interactive (SNI), the former Chief Operating Officer for HGTV and an award-winning author. She was the second employee of SNI and helped build the company to a market value of more than $10 billion. Under Packard\u2019s helm, HGTV became one of the fastest growing cable networks in television history. She has been widely recognized as an innovator, a role model and mentor for women aspiring to climb the corporate ladder. She received the Woman of the Year award from Women in Cable &amp; Telecommunications (WICT) and was inducted into the Cable Hall of Fame in 2008."],
 "http://susanpackard.com/about/"),
("Pat Baxter", "Former Senior Manager of Leadership for Bi-Lo Holdings", "images/people/pat-baxter.jpg", [
 "Pat Baxter was the Senior Manager of Organizational Effectiveness at Bi-Lo Holdings, LLC, the nation\u2019s ninth largest grocery chain. Her corporate experience includes functional leadership roles in Citigroup, Sykes Enterprises, Inc., UNISYS, AchieveGlobal, Right Management and The Prudential. Pat holds a doctorate from Argosy University in Organizational Leadership, which she has used to great effectiveness as a consultant and executive coach for firms such as American Express, Dollar General, Sweetbay Supermarkets, Comcast, and Toyota. Dr. Baxter has served on the Advisory Board at the Center for Ethics at the University of Tampa, the Latin Community Advisory Committee (LCAC) at the University of South Florida and as the Education Chair at the Florida Diversity Council, Tampa Bay chapter."],
 "https://www.linkedin.com/in/patbaxter/"),
("Sandra Yancey", "Founder and CEO of eWomen Network", "images/people/sandra-yancey.jpg", [
 "Sandra Yancey is the founder and CEO of eWomen Network, a multi-million dollar company that helps women across the globe build their businesses. Sandra was recognized by the International Alliance for Women as one of the world\u2019s 100 Top Difference Makers and by CNN as an American Hero. She is the bestselling author of Doubt, Fear &amp; Crisis, which rose to #1 status in five categories at Amazon.com. She is a mentor and example for women across the globe."],
 "https://www.ewomennetwork.com/page/meet-our-ceo"),
("Dr. Lois Frankel", "President of Corporate Coaching International", "images/people/lois-frankel.jpg", [
 "Dr. Lois Frankel is the President of Corporate Coaching International and an internationally known author. Her books Nice Girls Don\u2019t Get the Corner Office, Nice Girls Don\u2019t Get Rich, and Nice Girls Just Don\u2019t Get It are translated into over 25 languages worldwide. Dr. Frankel has appeared on the Today Show, Larry King Live, CNN and Fox News and has been featured in USA Today, People Magazine, and The Wall Street Journal."],
 "http://www.drloisfrankel.com/about_dr_lois_frankel.html"),
("Dr. Sylvia Ann Hewlett", "Founder and CEO of the Center for Talent Innovation", "images/people/sylvia-ann-hewlett.jpg", [
 "Dr. Sylvia Ann Hewlett is an economist and the Founder and CEO of the Center for Talent Innovation, a Manhattan-based think tank. She is also the Founder of Hewlett Consulting Partners LLC, the co-director of the Women\u2019s Leadership Program at the Columbia Business School, and a member of the Council on Foreign Relations and the Century Association.",
 "Hewlett is the author of 11 Harvard Business Review articles and 12 critically acclaimed books. Her writings have been published in the New York Times, the Financial Times, and the Wall Street Journal and she\u2019s a featured blogger on HBR Blog Network and the Huffington Post. She has appeared on NewsHour with Jim Lehrer, Charlie Rose, The Today Show, and BBC World News.",
 "In 2011 she received the Isabel Benham Award from the Women\u2019s Bond Club, as well as Women of the Year awards from the Financial Women\u2019s Association. In 2013 she received a Work Life Legacy Award from the Families and Work Institute, and in 2014 she was recognized as the Most Influential International Thinker by HR Magazine and was honored by the European Diversity Awards with its Global Diversity Award."],
 "http://www.sylviaannhewlett.com/about.html"),
]

PANELISTS = ["Dr. John Avendano","Martha Barrett","Sandy Bartow","Pat Baxter","Matt Berseth","Grace Brasington",
"Jody Brooks","Mike Burns","Tammy Butler","Sandy Cook","Gary Chartrand","Dave Dallas","Lisa Davis","Kristi Dosh",
"Marty Evans","Brian Fay","Latoria Farmer","Pat Geraghty","Dr. Nathaniel \u2018Nat\u2019 Glover","Jared Graybeal",
"Dr. Diana Green","Thomas E. Harvey","Angelia Hiers","John Hirabayashi","Dr. Carolyn Landolfo","Melanie Lawson",
"E. Denise Lee","Tiffani Lee","Rachel Levanger","Terri Lewis","Nancy Hogshead-Makar","Kawanza Humphrey",
"Sandra Madigan","Jennifer Mansfield","Dr. Beth Massey","Michelle McManamon","Ann Wong Meyers","Audrey Moran",
"Lisa Palmer","Ju\u2019Coby Pittman","Holly Bohn Pittman","Michael Pyle","Raymond Rhee","Jen Devore Richter",
"Meg Rose","Lyndsay Rossman-Hill","Betzy Santiago","Laura Schepis","Kristine Schoonmaker",
"Dr. Veronica Scott-Fulton","Darnell Smith","Rebecca Steele","Kerri Stewart","Travis Storey","Taryn Swietek",
"Craig Thomas","Nicole Thomas","Katy Thompson","Dr. Linda Travelute","Tera Tuten","Sharon Wamble-King",
"Angela Williams","Wyman Winbush","Brian Wolfburg","Scott Wooten","Christina Zorn, J.D."]

prev_blocks = "".join(prev_speaker(*s) for s in PREV)
panelist_items = "".join(f"<li>{p}</li>" for p in PANELISTS)

prev_body = page_hero("Previous Speakers &amp; Events",
    "More than a decade of nationally recognized speakers, authors, and executives at the JWLF Forum.") + f"""
<section class="section">
  <div class="container">
    <h2>Previous Event Topics</h2>
    <ul style="list-style:none; padding:0">{topics_html}</ul>
  </div>
</section>
<section class="section section--tint">
  <div class="container">
    <h2>Previous Featured Speakers</h2>
    {prev_blocks}
  </div>
</section>
<section class="section">
  <div class="container">
    <h2>Previous Panelists</h2>
    <ul class="name-columns">{panelist_items}</ul>
  </div>
</section>
<section class="section section--tint">
  <div class="container">
    <h2>Feedback From Past Participants</h2>
    <div class="card quote-card" style="max-width:44rem">
      <blockquote>\u201cThe Jacksonville Women\u2019s Leadership Forum annual event provides a unique opportunity to
      meet the female leaders in our local community. It\u2019s a valuable learning and networking day.\u201d</blockquote>
      <cite><strong>Charlene West</strong>, JEA</cite>
    </div>
  </div>
</section>
"""
page("previous-speakers.html", "Previous Speakers & Events",
     "Previous JWLF Forum topics, featured speakers, and panelists from 2014 to today.",
     prev_body)
print("pages2 done")
