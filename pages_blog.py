# Blog: full articles migrated from jwlf.org/blog (page 1). Page 2 of the live
# blog has at least one more post ("How Men Can Become Better Allies to Women",
# Oct 22, 2018) — flagged in MIGRATION-CHECKLIST.md for follow-up.
from build import page, page_hero

def article(slug, title, date, author_line, img, img_alt, body_html, desc):
    body = page_hero(title, f"{date}{' \u2014 ' + author_line if author_line else ''}") + f"""
<section class="section">
  <div class="container" style="max-width:52rem">
    <img src="./{img}" alt="{img_alt}" style="border-radius:10px" loading="lazy" class="mb-2">
    {body_html}
    <p class="mt-2"><a href="./news.html">&#8249; Back to the JWLF Blog</a></p>
  </div>
</section>"""
    page(slug, title, desc, body, active="news.html", switch_to="news.html")
    return slug

POSTS = []

POSTS.append(dict(slug="blog-communication-career-trajectory.html",
 title="How Communication Shapes the Career Trajectory of Women in Senior Leadership",
 date="July 10, 2025", author="", img="images/photos/blog-communication.jpg",
 img_alt="Confident women speaking in a group",
 desc="How women communicate at senior levels influences leadership perception, promotion, and longevity.",
 body="""
<p>After decades working with Fortune 500 companies, I\u2019ve seen one factor stand out: <strong>how women
communicate at senior levels profoundly influences not only perceptions of their leadership, but also their
promotion opportunities and longevity in powerful roles</strong>. Below, we explore why this is true \u2014 and how
women can strengthen their impact through strategic communication.</p>
<h2>1. Communication as a Career Catalyst</h2>
<p>Research shows women who reach the C-suite tend to leverage <strong>transformational communication</strong>
\u2014 emotionally intelligent, relationship-focused, and inclusive messaging that both inspires and guides teams.
For instance, <a href="https://www.researchgate.net/publication/376298420_The_Influence_of_Women%27s_Leadership_and_Communication_Style_on_Employee_Engagement_at_PT_Biofarma">a recent Indonesian study</a>
found women\u2019s transformational leadership significantly boosted employee engagement partly <em>through their
communication style</em>.</p>
<p>However, gender norms and stereotypes often silence women\u2019s voices.
<a href="https://www.researchgate.net/publication/356620073_Gender_Communication_and_Leadership_A_Qualitative_Research_In_Menagerial_Level">A qualitative study highlighted</a>
that gender-based communication barriers \u2014 like being perceived as too soft or too aggressive \u2014 can hold
women back. Often, women are caught in a <strong>double bind</strong>: using assertive language gains competence,
but can reduce likability; staying relational risks being labeled \u201cineffectual.\u201d
<a href="https://assets.kpmg.com/content/dam/kpmg/ph/pdf/ThoughtLeadershipPublications/KPMGWomensLeadershipStudy.pdf">Another study by KPMG</a>
delves into why women aspire to lead but are hesitant to shake the lessons learned growing up that can hold them
back.</p>
<h2>2. Visibility Through Vocal Confidence</h2>
<p>Senior roles require visibility \u2014 and that means speaking up.
<a href="https://arxiv.org/abs/1711.10985">One study on academic seminars</a> showed women ask far fewer questions
than men, reducing their visibility and undermining perceptions of leadership presence. In business, the stakes
are even higher: speaking up in meetings, presenting ideas, and asking for resources all depend on vocal
confidence.</p>
<h2>3. Strategic Self-Promotion</h2>
<p>Women are less likely to self-promote due to concerns over appearing boastful. Yet promoting one\u2019s
achievements strategically \u2014 framing them in terms of team or organizational success \u2014 enhances perceived
credibility without triggering backlash.</p>
<h2>4. Network-Driven Communication</h2>
<p>Research in social network dynamics found that women in high-status roles not only need broad networks (for
market information), but also tight-knit inner circles of other women (for gender-specific guidance). Strong
communication within these circles helps women navigate unseen pitfalls and align their messaging with unwritten
organizational norms. Engaging with networks like the <a href="./index.html">Jacksonville Women\u2019s Leadership
Forum</a> can help you develop and nurture those crucial relationships.</p>
<h2>Evidence-Based Tips to Upgrade Your Communication</h2>
<ul>
<li><strong>Assertive voice</strong> \u2014 prevents being overshadowed in meetings. Practice speaking early; state
key points in the first 60 seconds; record and adjust tone in coaching sessions.</li>
<li><strong>Transformational style</strong> \u2014 drives engagement and team performance. Start presentations with
\u201cHere\u2019s what we achieved\u2026 and here\u2019s why it matters to our team\u201d; ask open-ended
questions.</li>
<li><strong>Self-promotion balance</strong> \u2014 builds visibility without backlash. Use \u201cwe\u201d
narratives: \u201cOur team delivered a 20% increase\u2026 by implementing\u2026\u201d; cite team wins.</li>
<li><strong>Network communication</strong> \u2014 unlocks hidden opportunities. Schedule monthly peer check-in
calls; share insider updates and themes; offer mutual referrals.</li>
<li><strong>Feedback and adaptation</strong> \u2014 keeps communication authentic and effective. After key
meetings, ask trusted colleagues: \u201cDid my tone come across as collaborative and confident? Where could I lean
in more?\u201d</li>
</ul>
<h2>Final Thoughts</h2>
<p>Strong communication is more than a soft skill \u2014 it\u2019s a <strong>strategic lever</strong> that shapes
how organizations perceive you, what roles you\u2019re offered, and how long you thrive in senior leadership. As
women advance, refining communication style \u2014 asserting ideas, celebrating wins, building trusted networks,
and seeking candid feedback \u2014 can differentiate between simply \u201cbeing at the table\u201d and truly
influencing what\u2019s on it.</p>"""))

POSTS.append(dict(slug="blog-executive-presence.html",
 title="Executive Presence: A Cornerstone for Women Leaders",
 date="June 26, 2025", author="", img="images/photos/blog-executive-presence.jpg",
 img_alt="Illustration of a confident businesswoman",
 desc="Executive presence for women leaders: gravitas, communication, visibility, authenticity, and support.",
 body="""
<p><strong>Executive presence (EP)</strong> is often defined as the ability to inspire confidence \u2014 projecting
credibility, composure, and clarity so others believe you can lead under pressure. Sylvia Ann Hewlett\u2019s
research highlights three key pillars: <em>gravitas</em>, <em>communication</em>, and <em>appearance</em> \u2014 a
framework reaffirmed in studies spanning 2012 to 2022. Now, leadership requires inclusiveness \u2013 creating a
space where everyone\u2019s voice matters. Face-to-face charisma is no longer enough \u2013 you need to make your
presence felt through the screen through mastering the art of virtual communication.</p>
<p>Yet for women leaders, navigating executive presence comes with unique challenges. Due to role-congruity bias,
women who display traits like assertiveness or decisiveness can face backlash or be labeled \u201cbossy\u201d.
This \u2018double-bind\u2019 requires women to balance authority and warmth \u2014 a balance men rarely need to
strike.</p>
<h2>1. Gravitas with Authenticity</h2>
<p>Gravitas isn\u2019t about a stern demeanor \u2014 it\u2019s about calm confidence, intentionality, and conveying
that critical \u201cunder-control\u201d aura. Research shows women should amplify gravitas in ways aligned with
their style \u2014 thoughtful pauses, poised posture, moderated tone \u2014 projecting presence without triggering
bias.</p>
<h2>2. Communication That Connects</h2>
<p>Clear, structured delivery builds trust \u2014 and so does cultivating warmth. Amy Cuddy\u2019s work on
competence and warmth suggests leaders combine both to drive influence. Present <em>results-focused</em>
narratives, then reinforce them with empathy \u2014 e.g., \u201cThis is what we achieved \u2014 and here\u2019s how
we\u2019ll support each other moving forward.\u201d</p>
<h2>3. Strategic Visibility &amp; Self-Promotion</h2>
<p>Women often under-promote achievements due to fear of backlash \u2014 alongside stereotype threats. One study
noted women were 28% less likely than men to self-promote on platforms like X. To build executive presence, women
need to strategically share wins, advocate for themselves, and highlight impact. Frame accomplishments in service
to organizational goals to sidestep negative perceptions.</p>
<h2>4. Build Authentic Authority</h2>
<p>Traditional EP norms often prioritized a stiff managerial posture. Now,
<a href="https://www.brainzmagazine.com/post/c-suite-access-redefining-executive-presence-for-women-leaders">inclusive research</a>
is reshaping definitions to value emotional intelligence, collaboration, and being \u201cfully you.\u201d Lean
into what makes your leadership unique \u2014 empathy, active listening, cultural awareness. Companies benefit
when women bring diverse executive presence rather than mimicking male archetypes.</p>
<h2>5. Advocate for Structural Support</h2>
<p>The \u2018glass cliff\u2019 phenomenon \u2014 appointing women during crises \u2014 underlines how EP alone
doesn\u2019t level the playing field. Without sponsorship, resources, or mentoring, women risk high-stakes
failure. C-suite sponsors must invest in developing women\u2019s EP over time \u2014 not just in emergency
conditions.</p>
<h2>Building Your Executive Presence: A Practical Action Plan</h2>
<ul>
<li><strong>Gravitas</strong> \u2014 adopt intentional posture; practice pausing before responding; maintain a
steady tone under stress.</li>
<li><strong>Communication</strong> \u2014 tell result-driven stories; weave in emotional connection; adjust
delivery for clarity.</li>
<li><strong>Visibility</strong> \u2014 share successes in team meetings and updates; mentor peers; volunteer for
visible initiatives.</li>
<li><strong>Authenticity</strong> \u2014 reflect on personal style and values; seek feedback on how presence
lands; refine your \u201con-stage\u201d persona.</li>
<li><strong>Support systems</strong> \u2014 build a circle of champions; seek sponsors; ask for stretch
opportunities before crises arise.</li>
</ul>
<h2>Bring It All Together</h2>
<p>Executive presence is <strong>not a mask, but a craft</strong> \u2013 a blend of credible gravitas,
connection-building communication, and authentic self-expression. For women, it\u2019s about mastering the
balance: showing up confidently <em>and</em> genuinely, asserting influence <em>and</em> inclusion. As EP norms
evolve, women who claim their natural authority \u2013 and build supportive structures \u2013 will shape the
future of leadership.</p>"""))

POSTS.append(dict(slug="blog-confidence-catalyst-mentoring.html",
 title="The Confidence Catalyst: Why Every Woman Needs a Mentor in Today\u2019s Corporate World",
 date="January 23, 2025", author="", img="images/photos/blog-mentoring.png",
 img_alt="Two women in a business office; one coaching the other",
 desc="Why every woman needs a mentor, and how corporate mentoring programs build confidence and careers.",
 body="""
<p><strong>Why Every Woman Needs a Mentor \u2014 And How Corporate Programs Can Help</strong></p>
<p>Have you ever found yourself in a professional situation thinking, \u201cI wish someone could just show me the
ropes\u201d? If you have, you\u2019re not alone. Many of us, especially women, have looked up at a leadership team
and felt a twinge of uncertainty about where we fit in. Enter: mentoring programs. These programs aren\u2019t just
corporate checkboxes; they can be life-changing pathways to success, belonging, and confidence.</p>
<h2>The Power of Seeing Yourself Represented</h2>
<p>Women often find themselves in environments where they\u2019re one of only a few at the table. It can feel
daunting, especially if you\u2019re trying to figure out how you can succeed in that environment. Having a mentor,
particularly a woman who\u2019s navigated a similar path, can make all the difference. When you see someone who
looks like you, shares your background, or has faced familiar challenges, it\u2019s easier to trust that your
goals are achievable.</p>
<h2>Mentorship as a Confidence Booster</h2>
<p>Women sometimes struggle with self-doubt and the dreaded imposter syndrome \u2014 those nagging thoughts that
you\u2019re not quite good enough or haven\u2019t truly earned your seat. A mentor can help shake off those
insecurities. Think of it like having your own personal coach, someone who\u2019s already tackled the hurdles
you\u2019re facing and can remind you that you have every reason to believe in yourself. These confidence boosts
aren\u2019t about empty praise. They come from a mentor who\u2019s walked the road and says, \u201cTrust me,
you\u2019ve got this.\u201d</p>
<h2>Learning from Someone Else\u2019s Experience</h2>
<p>One of the biggest perks of a mentoring relationship is that you don\u2019t have to learn everything by trial
and error. Mentors share their wisdom \u2014 what worked, what failed, and what they might do differently if they
could turn back the clock. That\u2019s gold! Through a steady flow of insights, cautionary tales, and practical
tips, you can save yourself a ton of missteps. This guidance helps you navigate organizational politics, sharpen
your leadership style, or even figure out how to balance career goals with personal life. Mentors provide a peek
into the future so you can plan your path more effectively.</p>
<h2>Networking and Visibility</h2>
<p>Let\u2019s talk about networking. It\u2019s important for everyone, but it can be especially critical for women
who are forging new paths in leadership roles. A mentor can open doors and help you build connections. Whether
you\u2019re aspiring to a leadership position or trying to find the perfect niche within your company, these
corporate mentoring programs can expand your sphere of influence. It\u2019s like tapping into someone else\u2019s
professional black book \u2014 one that can lead to opportunities you might never have found on your own.</p>
<h2>Mentoring Beyond Company Walls</h2>
<p>While corporate mentoring programs are incredible, there\u2019s also real value in looking outside your
organization. Sometimes you need an external perspective, someone who doesn\u2019t work with you day-to-day but
understands the broader challenges women face in the workplace. External mentors can offer unbiased advice and
connections across different industries. They can help you see the \u201cbig picture\u201d of your career path and
sometimes even suggest moves that you might not have considered. For instance, maybe you work in finance but have
an external mentor in tech who inspires you to explore data analytics. This kind of cross-pollination of ideas
can be a game-changer!</p>
<p><em>Additional benefits of external mentorship:</em></p>
<ul>
<li><strong>Fresh perspective:</strong> when everyone at your workplace is immersed in the same culture, you might
miss out on innovative ways of thinking. A mentor from outside can help shake up your approach and problem-solving
skills.</li>
<li><strong>Wider network:</strong> stepping outside your usual company circles often results in meeting people
who are tackling similar professional issues but from entirely different vantage points.</li>
<li><strong>Expanded opportunities:</strong> you never know \u2014 an external mentor may open your eyes to new
career paths or side projects that you hadn\u2019t considered within your current environment.</li>
</ul>
<h2>Cultivating an Inclusive Culture</h2>
<p>Strong mentoring programs for women contribute to a healthier, more inclusive corporate culture overall. When
a company invests time and resources into mentoring women, it sends a clear message: \u201cWe value your potential
and your growth.\u201d This approach not only helps individual women succeed, but also encourages other employees
\u2014 women and men alike \u2014 to value diversity of thought, background, and experience. It\u2019s a win-win.
Organizations with effective mentoring programs often see higher retention rates, improved job satisfaction, and
better overall performance.</p>
<h2>Tips for Starting or Improving a Mentoring Program</h2>
<ul>
<li><strong>Match with intent:</strong> a random pairing might work occasionally, but intentional matching \u2014
based on goals, career aspirations, and even personality types \u2014 tends to yield better, longer-lasting
relationships.</li>
<li><strong>Set clear expectations:</strong> mentors and mentees should understand the purpose of their
relationship. Is it purely developmental? Focused on leadership growth? Crafting a growth plan can help avoid
confusion.</li>
<li><strong>Train mentors:</strong> being a mentor isn\u2019t always intuitive. Offer mentors resources to ensure
they have the tools and understanding to guide effectively. This could be as simple as a workshop or a discussion
guide.</li>
<li><strong>Encourage communication:</strong> establish regular check-ins so that both parties stay on track.
Whether it\u2019s a monthly coffee date or a virtual check-in, consistency matters.</li>
<li><strong>Track success:</strong> gather feedback and measure results. Are mentees reporting better confidence,
clarity in career direction, or promotions? That data can help refine and grow your program.</li>
</ul>
<h2>Finding a Mentor on Your Own</h2>
<p>Not every organization has a formal mentoring program, or maybe you\u2019d like to supplement the one
you\u2019re in. If you\u2019re seeking a mentor on your own, don\u2019t be afraid to reach out. Attend industry
conferences, webinars, and networking events (I recommend Jacksonville Women\u2019s Leadership Forum events!) Ask
for introductions from friends or colleagues. Most people are flattered to be asked for guidance. The key is to
be genuine: share why you admire them, what you hope to learn, and how you envision the relationship working.</p>
<h2>Paying It Forward</h2>
<p>Finally, remember that mentorship is a two-way street. Even if you consider yourself \u201cup-and-coming,\u201d
there\u2019s always someone who can benefit from your insights. Mentorship fosters a cycle of learning and support
that makes work more collaborative, open-minded, and, frankly, a lot more fun. If you have knowledge to share
\u2014 whether it\u2019s about navigating a particular role or advocating for yourself \u2014 consider offering to
mentor a colleague or a student. The ripple effect of mentorship is powerful and uplifting.</p>"""))

POSTS.append(dict(slug="blog-power-of-sponsorship.html",
 title="The Power of Sponsorship for Corporate Women",
 date="January 18, 2025", author="", img="images/photos/blog-sponsorship.png",
 img_alt="Businesswoman revealing a superhero costume",
 desc="Mentorship guides; sponsorship propels. Why sponsorship is the real catalyst for women's advancement.",
 body="""
<p>When we talk about advancing women in the workplace, terms like \u201cmentorship\u201d and
\u201csponsorship\u201d often surface. While they may seem interchangeable at first glance, they represent
fundamentally different dynamics \u2014 and one of them has the power to significantly move the needle for
women\u2019s progress in corporate environments. That\u2019s sponsorship.</p>
<p>Mentorship helps women navigate the corporate maze. Sponsorship, however, doesn\u2019t just give women the map
\u2014 it helps them climb ladders, break glass ceilings, and open doors that might otherwise remain shut.
Let\u2019s dive into why sponsorship is crucial for women in the workplace and how it differs from mentorship in
ways that matter.</p>
<h2>Mentorship vs. Sponsorship: The Key Differences</h2>
<p>Think of mentorship as guidance. A mentor is someone who provides advice, shares their own experiences, and
offers a sounding board when you\u2019re unsure of your next step. Mentorship is valuable, don\u2019t get me wrong
\u2014 it helps build confidence, provides clarity, and can equip women with essential skills.</p>
<p>Sponsorship, on the other hand, is all about action. A sponsor is someone who doesn\u2019t just advise but
actively advocates for you. They use their influence, network, and credibility to create opportunities for you.
Sponsors will put their name \u2014 and sometimes even their reputation \u2014 on the line to ensure you\u2019re
seen, heard, and considered for key roles or projects.</p>
<ul>
<li>Mentors talk to you. <strong><em>Sponsors talk about you.</em></strong></li>
<li>Mentors guide you behind the scenes. <strong><em>Sponsors champion you in the spotlight.</em></strong></li>
<li>Mentorship is about personal development. <strong><em>Sponsorship is about career advancement.</em></strong></li>
</ul>
<h2>Why Sponsorship Matters More for Women</h2>
<p>We all know that women have been underrepresented in leadership roles. Even as workplaces prioritize diversity,
equity, and inclusion, systemic barriers persist. Here\u2019s where sponsorship becomes a game-changer.</p>
<h3>1. It Breaks Through the \u201cBoys\u2019 Club\u201d Culture</h3>
<p>Corporate environments often operate on networks \u2014 who you know and who knows you can sometimes matter
more than your qualifications. Men have traditionally benefitted from informal sponsorship relationships within
these networks. Women, particularly women of color, have historically been excluded from these spaces.</p>
<p>Sponsors can help level the playing field by ensuring women aren\u2019t just part of the conversation \u2014
they\u2019re leading it. A sponsor vouches for your capabilities, connects you to decision-makers, and ensures
you\u2019re considered for opportunities that might otherwise be offered to someone else.</p>
<h3>2. It Challenges Implicit Bias</h3>
<p>Research shows that women are often promoted based on performance, while men are promoted based on potential.
How\u2019s that for fairness? This bias means women have to prove themselves repeatedly before earning a shot at
leadership roles. Sponsors challenge this norm by highlighting women\u2019s potential and pushing for their
advancement, even when others hesitate.</p>
<p>For instance, imagine a senior leader saying, \u201cI think Sarah is ready to lead this project. Let\u2019s
give her a chance.\u201d That\u2019s sponsorship in action \u2014 someone actively advocating for Sarah and
ensuring she\u2019s considered for opportunities that stretch her abilities and demonstrate her worth.</p>
<h3>3. It Closes the Pay and Position Gaps</h3>
<p>Sponsorship can directly impact the pay and position disparities between men and women. By ensuring women are
positioned for high-visibility roles, leadership opportunities, and promotions, sponsors help close the gaps that
often widen as careers progress. A sponsor\u2019s advocacy ensures women aren\u2019t overlooked for executive
roles, board seats, or critical assignments.</p>
<h2>The Human Side of Sponsorship: Real Stories</h2>
<p><strong>Scenario 1: The Mentor.</strong> Emma is a marketing manager looking to grow into a leadership role.
Her mentor, Lisa, is a VP of Marketing who meets with Emma monthly, offering advice on navigating office politics
and honing her skills. Lisa encourages Emma to build her network and keep her resume polished. Emma feels
supported but finds herself struggling to get noticed by senior leadership.</p>
<p><strong>Scenario 2: The Sponsor.</strong> Now, let\u2019s tweak the story. Lisa doesn\u2019t just mentor Emma
\u2014 she becomes her sponsor. During executive meetings, Lisa mentions Emma\u2019s stellar work on a recent
campaign. When a new director role opens up, Lisa directly recommends Emma, saying, \u201cEmma is ready for this.
Her work speaks for itself, and she\u2019s already acting at a director level.\u201d The result? Emma gets the
opportunity she\u2019s been preparing for, thanks to Lisa\u2019s active sponsorship.</p>
<p>This is the difference. <strong><em>Sponsorship doesn\u2019t just empower \u2014 it propels.</em></strong></p>
<h2>What Women Can Do to Secure Sponsors</h2>
<ul>
<li><strong>Excel in your current role.</strong> Sponsors are more likely to advocate for individuals who
consistently deliver results. Make your work undeniable \u2014 showcase your skills, take ownership of projects,
and exceed expectations.</li>
<li><strong>Build strategic relationships.</strong> Sponsors are often senior leaders who have the influence to
open doors. Look for opportunities to connect with leaders who align with your career aspirations. This
doesn\u2019t mean forcing connections \u2014 it\u2019s about building genuine relationships based on mutual
respect.</li>
<li><strong>Be vocal about your goals.</strong> A sponsor can\u2019t advocate for you if they don\u2019t know what
you want. Be clear and intentional about your career goals, and let potential sponsors see your ambition.</li>
<li><strong>Seek out stretch assignments.</strong> Volunteer for projects that push you outside your comfort
zone. These high-visibility assignments can catch the attention of leaders who may become your sponsors.</li>
</ul>
<h2>What Companies Can Do to Foster Sponsorship</h2>
<p><strong><em>It\u2019s not enough for women to find sponsors on their own.</em></strong> Companies must actively
create environments where sponsorship flourishes:</p>
<ul>
<li><strong>Formalize sponsorship programs.</strong> Many organizations have mentorship programs, but sponsorship
often happens informally. By creating structured sponsorship initiatives, companies can ensure women have access
to influential advocates.</li>
<li><strong>Hold leaders accountable.</strong> Companies should track metrics around promotions, pay equity, and
representation in leadership roles. Senior leaders must be held accountable for sponsoring high-potential women
and ensuring diverse talent is recognized.</li>
<li><strong>Encourage cross-gender sponsorship.</strong> Some men hesitate to sponsor women due to fears of
appearances or misinterpretation. Companies can address this by normalizing cross-gender sponsorships, providing
guidelines, and creating safe, professional structures for these relationships. If business is happening in the
male locker room, just think how critical it is to have a sponsor there to advocate for you!</li>
<li><strong>Celebrate success stories.</strong> When sponsorship leads to tangible results \u2014 promotions,
increased representation, or impactful projects \u2014 celebrate them. Highlighting these stories reinforces the
importance of sponsorship and inspires others to get involved.</li>
</ul>
<h2>The Ripple Effect of Sponsorship</h2>
<p>When women are sponsored, it\u2019s not just their careers that benefit. The ripple effects are profound. Teams
led by women tend to be more collaborative and innovative. Organizations with diverse leadership are more
profitable. And perhaps most importantly, when women see other women in positions of power, it inspires the next
generation to aim higher.</p>
<p>Sponsorship creates a virtuous cycle. A sponsored woman becomes a leader who, in turn, sponsors others. This is
how systemic change happens \u2014 not just by breaking barriers, but by building bridges for others to cross.</p>
<h2>Sponsorship \u2013 the Real Catalyst</h2>
<p>If mentorship is about guidance, sponsorship is about advocacy. And in today\u2019s corporate environments,
advocacy is what women need most. Sponsorship accelerates careers, challenges biases, and ensures women have a
seat \u2014 and a voice \u2014 at the table.</p>
<p>So, let\u2019s rethink how we support women in the workplace. Mentors are invaluable, but sponsors?
They\u2019re the real catalysts for change. If we want to see more women in leadership, we need more sponsors to
step up and say, \u201cI believe in her. Let\u2019s make it happen.\u201d That\u2019s the kind of action that
moves mountains \u2014 and careers.</p>"""))

POSTS.append(dict(slug="blog-best-ally-or-worst-enemy.html",
 title="Are You Your Own Best Ally, Or Worst Enemy?",
 date="February 6, 2019", author="By Tammy Heermann, Leadership Development Expert",
 img="images/photos/blog-ally.jpg", img_alt="A professional woman deep in thought",
 desc="Tammy Heermann on five common ways women hold themselves back at work — and how to stop.",
 body="""
<p>When you\u2019re in the zone, doing your thing, you feel invincible, right? You know you can harness your
mindset to make the impossible feel possible. It\u2019s a powerful thing. But too often we use that power for evil
rather than good.</p>
<p>In fact, I\u2019ve seen many ways that women sabotage their own chances for advancement at work. Maybe
it\u2019s how you unwittingly confuse being a good team player with making yourself subservient. Maybe it\u2019s
because you hold onto control so tight you drown in long to do lists. Over years of working with female leaders
the world over, I have identified 10 common ways that women hold themselves back. Below I describe 5. Do you
recognize any of these?</p>
<h2>Doubting Your Own Potential</h2>
<p>Many women I work with believe they will never be ready or qualified to take on a more senior role. It\u2019s
a chronic problem. In fact, in interviews with current and former female CEOs of the Fortune 1000, it was
discovered that 65% of the women never sought to be CEOs until someone told them they had the potential. Only 9%
said they\u2019d always wanted to be CEO.</p>
<p>When contemplating a new opportunity, women, I find too often, wallow in negative questions and talk themselves
out of going for it. We ask ourselves, \u2018Am I ready?\u2019 Or, \u2018How will I stand a chance against more
experienced candidates?\u2019 If you doubt your own full potential, you\u2019ll never actually achieve it.</p>
<h2>Working Heads Down</h2>
<p>Do you believe that networking is a nebulous time suck? Do you cringe at the mere mention of the word? Really,
isn\u2019t it just schmoozing? Who\u2019s got time for that? It turns out, we all must make time for that. Working
hard only gets you so far and your accomplishments won\u2019t always be noticed or rewarded.</p>
<p>The good news is that women inherently value relationship building. The bad news, however, is that women are
reluctant to apply this talent for their own gain. They make connections that benefit their organizations, but
somehow fail to implement it as a strategy to promote their own career aspirations.</p>
<h2>Accepting the Role of a Wallflower</h2>
<p>Deborah Tannen, a linguistics professor at Georgetown University, has found in her research that in public
forums, women talk less than men. And when they did, their ideas were not often picked up or attributed to
them.</p>
<p>I have seen females at all levels clam up during conversations. More often than not, it comes down to a
mistaken belief that they have nothing to add to the conversation, that they know less than the other person, or
that they will sound stupid. But when you choose to stay silent and not participate, you are projecting the exact
image that you want to avoid. You look like you have no ideas, and nothing to contribute.</p>
<h2>The Hamster-Wheel of Tactical Work</h2>
<p>I was having a lively discussion with a group of HR leaders on the barriers women face in advancing to more
senior roles. One of these barriers was described as being willingly trapped in the \u201chamster wheel of
tactical work.\u201d</p>
<p>A senior male HR leader said he\u2019d observed how, at the end of every meeting of his team, the female peers
volunteered to take on all the action items and the administrative details. They even stayed to clean up the
debris left over from the meeting. Essentially, they willingly bore the brunt of the grunt work, while the men
just skated away.</p>
<p>Women need to be aware that when you get stuck in tactical work, it creates the impression that you are unable
to take on strategic thinking and tasks. The same holds true when you can\u2019t delegate responsibilities (at
work and at home!). It will erode the quality of what you do and it diminishes your profile as a leader.</p>
<h2>Endless Rumination</h2>
<p>I was listening with rapt attention to a guest speaker address a group of high-potential female partner
hopefuls. She was asked: what is the single most important lesson she learned over her career as the lone female
amidst a sea of male partners? She said she was much happier and more successful when she learned to \u201cjust
get over herself.\u201d</p>
<p>This meant not ruminating incessantly about every decision, beating herself up when she had a setback, taking
everything so seriously, or holding onto grudges. When she got over herself, she could project the confidence of
a leader. Not only did this lead to greater success, but it also allowed her to sleep better at night.</p>
<p>It\u2019s hard to get control of the voices that take up office in our heads. Those that make us question
ourselves, tell us we\u2019re not good enough, or make us hang on to unproductive feelings when they\u2019re past
their due date. Overtime this leads to cynicism, unhealthy relationships and burnout, none of which are helpful
for productive functioning at work.</p>
<h2>Final Thoughts</h2>
<p>As women leaders, we sometimes spend an inordinate amount of time ruminating about the things we can\u2019t
control and ignoring the things that we can. We become obsessed with the negative people and traditions and
mechanisms that keep us from reaching the highest levels of leadership, but devote precious little time examining
our own talk tracks and mindsets. The end result is that we unconsciously sabotage our own chances for
success.</p>
<p>Research has consistently shown that women who adopt mindsets that demonstrate confidence in their strengths
and key attributes tend to ultimately achieve higher levels of leadership success. That\u2019s hardly
revolutionary; our mindsets and beliefs shape our behaviors, which in turn forge the image that others have of
us.</p>
<p>I encourage you to devote some time every day to reminding yourself of the strength and value you bring to
your organization. And help other women never doubt the fact that they too have a lot to offer. Let\u2019s not
have the greatest barrier faced on the road to leadership success be ourselves.</p>
<p><em>Tammy Heermann was a keynote speaker at the 2019 Jacksonville Women\u2019s Leadership Forum and is
specifically sought out by global Fortune 500 companies for her expertise in gender diversity and award winning
programs that accelerate women\u2019s advancement. You can learn more about Tammy\u2019s work at
<a href="https://www.tammyheermann.com/">tammyheermann.com</a>.</em></p>"""))

POSTS.append(dict(slug="blog-infusing-hope.html",
 title="Top Tips for Infusing Hope into Your Corporate Culture",
 date="January 25, 2019", author="By Libby Gill",
 img="images/photos/blog-hope.jpg", img_alt="Libby Gill speaking",
 desc="Libby Gill on the four traits followers want from leaders, and practical ways to feed hope at work.",
 body="""
<p><strong><em>When your team is faced with change, challenge, or chaos, inspire them with a future-focused vision
of shared success!</em></strong></p>
<p>You may never see these traits in a job description for an executive position, but there are four key
characteristics that followers want from their leaders: compassion, stability, trust, and hope.</p>
<p>In a Gallup poll of more than 10,000 workplace participants, those four traits were cited most often. Absent
these people-centric leadership qualities, which can be in short supply when leaders are focused on reorganization
or change, employees are often not at their most engaged or productive. In the study, when Gallup researchers
asked workers if their managers and leaders made them feel <em>hopeful</em> about the future, among those who
said yes, 69% also scored high on a scale of engagement in their work. Of those who said their managers did not
instill a sense of hopefulness about the future, only 1% scored high on the engagement measure. Which kind of
employee would you rather have? Disengaged and unproductive or engaged and hopeful?</p>
<p><strong>In my ongoing research on hope in the workplace with client companies around the world, I see a clear
pattern emerging, highlighted by the following:</strong></p>
<ul>
<li><em>Most</em> professionals see hope as an essential element of leadership.</li>
<li><em>Some</em> professionals feel that they intentionally feed hope in their workplace.</li>
<li><em>Few</em> professionals believe that their organizations inspire hopefulness among their employees.</li>
</ul>
<p>Obviously, leaders need to <em>feed hope</em> as they guide their teams to see a vivid picture of the future,
understand precisely where they fit into it, and navigate change as seamlessly as possible. Here are some ideas
to help you infuse hopefulness into your culture.</p>
<ul>
<li><strong>Share your purpose.</strong> The <em>why</em> behind your team, division, or organization may be
obvious to you, but don\u2019t assume everyone else gets it. Look at companies like Tom\u2019s Shoes, with its
\u201cOne for One\u201d program where they donate a pair of shoes to a child in need with every purchase. Putting
shoes on kids is a purpose anyone can get behind.</li>
<li><strong>Paint a vivid picture of the future.</strong> Feeding hope is about looking toward a better future.
Your employees need to understand where the organization is heading and what that means to them individually.
Communicate the vision so fully and frequently \u2013 through town hall meetings, internal newsletters, and
one-on-one conversations \u2013 that everyone is crystal clear on where you\u2019re headed.</li>
<li><strong>Offer information appropriately.</strong> Information is the organizational life-blood on which
decisions are made in every company. Honor people with your trust and willingness to give them the facts. Except
for confidential info that can\u2019t be shared, pass information readily up and down the pipeline that can help
others make timely decisions.</li>
<li><strong>Find the formal and informal change agents.</strong> Don\u2019t succumb to the notion that only the
senior leadership team or HR can manage change. Find those influential people at all levels of the organization
who others listen to, respect, and follow. Instill them with hope about the future \u2013 as well as the realities
of the business \u2013 and enlist their help in easing others through change.</li>
<li><strong>Be open and transparent.</strong> Have a common language around your shared values and pre-determined
standards. Don\u2019t fall into corporate-speak or platitudes that would be better posted in the employee
cafeteria or embroidered on a pillow. Instead, share real, honest, down-to-earth talk about what the company
stands for and what is expected of employees.</li>
<li><strong>Avoid micro-managing.</strong> Nothing makes employees lose hope and heart like being over-managed.
Hire the right people, then give them both challenge and choice. People who are charged with mastering new skills
and taking ownership of projects get \u2013 and stay \u2013 engaged.</li>
<li><strong>Warm up your emails.</strong> It\u2019s not so hard to say please, thank you, and job well done.
Don\u2019t leave employees guessing, or worse, wondering what they did wrong, when they get overly curt emails or
texts from you.</li>
<li><strong>Embrace your frontline.</strong> Don\u2019t forget about the people who are out front doing hard duty
with customers, clients, products and more. When you flip the conventional wisdom and think about leaders as
working for their followers, and not the other way around, you are feeding hope. Recognize them with celebrations
for big and small wins.</li>
<li><strong>Know your people.</strong> This seems obvious but, believe me, it\u2019s not intuitive to everyone.
Get to know your team not just as workers (although that\u2019s important), but as human beings. You spend a lot
of time with your co-workers so take the time to discover their passions, their kids\u2019 names, and their hopes
and dreams for the future.</li>
</ul>
<p>As a senior leader at Sony, Universal, and Turner Broadcasting, I found that it was not only working together,
but also sharing personal triumphs and tragedies including illnesses, marriages, divorces, births and more that we
came to truly trust and respect one another. Feed hope and people will follow you anywhere!</p>
<p><em>Libby Gill was a keynote speaker at the 2019 Jacksonville Women\u2019s Leadership Forum and is an executive
coach, leadership expert, and international speaker. She is the former head of communications and PR for Sony,
Universal, and Turner Broadcasting, and author of the award-winning</em> You Unstuck: Mastering the New Rules of
Risk-taking in Work and Life <em>and</em> The Hope-Driven Leader: Harness the Power of Positivity at Work.
<em>You can learn more about Libby\u2019s work at <a href="https://libbygill.com/">libbygill.com</a>.</em></p>"""))

for p in POSTS:
    article(p["slug"], p["title"], p["date"], p["author"], p["img"], p["img_alt"], p["body"], p["desc"])

# ---------------- Blog index (replaces the earlier teaser-only news.html) ----
cards = ""
for p in POSTS:
    cards += f"""<article class="card card--flush" data-reveal>
  <img class="card-photo" src="./{p["img"]}" alt="{p["img_alt"]}" loading="lazy">
  <div class="card-body">
    <h3><a href="./{p["slug"]}">{p["title"]}</a></h3>
    <p class="person-org">{p["date"]}</p>
    <p>{p["desc"]}</p>
    <a href="./{p["slug"]}">Read the article</a>
  </div>
</article>"""

blog_index = page_hero("JWLF Blog",
    "Women\u2019s leadership articles to advance your career and opportunities.") + f"""
<section class="section">
  <div class="container">
    <div class="grid grid--3">{cards}</div>
    <p class="notice mt-2">Older posts from our previous site (2018 and earlier) are still being migrated \u2014
    <a href="./contact.html">contact us</a> if you\u2019re looking for a specific article.</p>
  </div>
</section>
"""
page("news.html", "JWLF Blog",
     "The JWLF Blog: women's leadership articles on communication, executive presence, mentorship, and sponsorship.",
     blog_index)
print("blog pages done:", len(POSTS), "articles")
