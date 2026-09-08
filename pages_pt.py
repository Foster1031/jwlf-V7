# -*- coding: utf-8 -*-
# Brazilian Portuguese (pt) site content. Testimonial quotes are marked as
# translations; speaker bios, blog articles, and the FL legal disclosure remain
# in English.
from i18n_pages import build_lang

perk_map = {
 "Company recognition at JWLF Forum as highest-level sponsor": "Reconhecimento da empresa no F\u00f3rum JWLF como patrocinadora de mais alto n\u00edvel",
 "Company recognition at JWLF Forum as sponsor": "Reconhecimento da empresa como patrocinadora no F\u00f3rum JWLF",
 "Company recognition at JWLF Forum": "Reconhecimento da empresa no F\u00f3rum JWLF",
 "Company logo included on all JWLF promotional and marketing materials (prominent position)": "Logotipo da empresa em todos os materiais promocionais e de marketing da JWLF (posi\u00e7\u00e3o de destaque)",
 "Company logo included on all JWLF promotional and marketing materials": "Logotipo da empresa em todos os materiais promocionais e de marketing da JWLF",
 "Discounted rate for company participants to attend JWLF programming held throughout the year": "Tarifa com desconto para que participantes da empresa assistam \u00e0 programa\u00e7\u00e3o da JWLF ao longo do ano",
 "Opportunity to provide swag at all events": "Oportunidade de distribuir brindes em todos os eventos",
 "Company full-page ad in JWLF event program": "An\u00fancio de p\u00e1gina inteira no programa do evento da JWLF",
 "Company half-page ad in JWLF event program": "An\u00fancio de meia p\u00e1gina no programa do evento da JWLF",
 "Opportunity for company showcase or speaker at educational events": "Oportunidade de apresentar a empresa ou um palestrante nos eventos educacionais",
 "Two sponsor board of director seats": "Dois assentos de patrocinador no conselho diretor",
 "Group photo of company attendees at the Annual JWLF Forum": "Foto em grupo dos participantes da empresa no F\u00f3rum Anual da JWLF",
 "Opportunity to provide panelist at JWLF Forum": "Oportunidade de indicar um painelista no F\u00f3rum JWLF",
 "Opportunity to \u201cown\u201d your part in the JWLF Forum (luncheon, breakfast)": "Oportunidade de \u201cassinar\u201d uma parte do F\u00f3rum JWLF (almo\u00e7o, caf\u00e9 da manh\u00e3)",
 "Opportunity to \u201cown\u201d your part in the JWLF Forum (pre-event reception, post-event social)": "Oportunidade de \u201cassinar\u201d uma parte do F\u00f3rum JWLF (recep\u00e7\u00e3o pr\u00e9-evento, confraterniza\u00e7\u00e3o p\u00f3s-evento)",
}
for n in (20, 16, 14, 4):
    perk_map[f"{n} tickets to the Annual JWLF Forum"] = f"{n} ingressos para o F\u00f3rum Anual da JWLF"

T = dict(
 translated_note="tradu\u00e7\u00e3o",
 # Home
 t_home="Bem-vinda \u00e0 JWLF", d_home="O Jacksonville Women's Leadership Forum capacita mulheres a navegar o mundo corporativo e cultivar seu desenvolvimento pessoal.",
 hero_h1="Mulheres trabalhando juntas para formar l\u00edderes e impulsionar carreiras",
 hero_p="O Jacksonville Women\u2019s Leadership Forum \u00e9 a principal organiza\u00e7\u00e3o da First Coast, na Fl\u00f3rida, que capacita mulheres a navegar com sucesso o terreno \u00fanico do mundo corporativo e a cultivar seu desenvolvimento pessoal.",
 hero_cta1="Conhe\u00e7a o F\u00f3rum", hero_cta2="Torne-se Patrocinadora",
 welcome_h="Bem-vinda ao Jacksonville Women\u2019s Leadership Forum",
 welcome_p="A JWLF vai transformar a maneira como as participantes abordam lideran\u00e7a, networking, avan\u00e7o de carreira e equil\u00edbrio de vida. Por meio do F\u00f3rum anual e de eventos educacionais e de networking ao longo do ano, voc\u00ea ter\u00e1 acesso \u00e0s perspectivas de outras mulheres inteligentes e bem-sucedidas, todas focadas nos desafios das mulheres que avan\u00e7am rumo ao topo.",
 pillars=[
  ("Fortalecer Habilidades de Lideran\u00e7a","Ampliamos as oportunidades de lideran\u00e7a para futuras executivas em um ambiente exclusivo entre pares. Deixe a JWLF expandir seu potencial profissional, desenvolver habilidades cr\u00edticas e definir objetivos de carreira alcan\u00e7\u00e1veis e sustent\u00e1veis."),
  ("Ampliar a Rede Profissional","Buscamos ampliar a rede profissional e a visibilidade de cada participante na comunidade empresarial de Jacksonville. A JWLF vai ajudar voc\u00ea a maximizar suas redes e aproveitar sua influ\u00eancia."),
  ("Impulsionar Carreiras","Oferecemos oportunidades de desenvolvimento profissional por meio de mentoria e educa\u00e7\u00e3o continuada. Aprenda a usar sua proposta de valor \u00fanica para avan\u00e7ar na carreira."),
  ("Encontrar Equil\u00edbrio de Vida","Ajudamos voc\u00ea a encontrar aquele equil\u00edbrio de vida que toda profissional deseja. Aprenda novas t\u00e9cnicas e dicas pr\u00e1ticas para equilibrar o sucesso pessoal enquanto fortalece sua marca profissional."),
 ],
 theme_pre="Nosso tema anual 2026\u20132027",
 theme_line="Lidere com clareza. Influencie com confian\u00e7a. Cres\u00e7a com inten\u00e7\u00e3o.",
 theme_status="Compartilharemos as informa\u00e7\u00f5es do nosso F\u00f3rum Anual de 2027 nos pr\u00f3ximos meses.",
 theme_btn="Inscreva-se em 2027",
 who_h="Quem deve participar?",
 who_items=["Mulheres em cargos s\u00eaniores identificadas como l\u00edderes proativas com alto potencial e realiza\u00e7\u00f5es",
  "Gestoras de n\u00edvel m\u00e9dio e s\u00eanior que lideram equipes e normalmente t\u00eam subordinados diretos",
  "Mulheres com v\u00e1rios anos de experi\u00eancia em fun\u00e7\u00f5es de lideran\u00e7a",
  "Mulheres e homens com influ\u00eancia em suas organiza\u00e7\u00f5es, engajados em capacitar a pr\u00f3xima gera\u00e7\u00e3o de mulheres l\u00edderes"],
 who_btn="Ver o pr\u00f3ximo F\u00f3rum",
 alt_networking="Participantes em um F\u00f3rum da JWLF", alt_speaker="Uma palestrante no F\u00f3rum da JWLF",
 testimonials_h="O que dizem as participantes",
 testimonials=[
  ("Obrigada novamente pela oportunidade de vivenciar o Jacksonville Women\u2019s Leadership Forum. Aprendi coisas valiosas sobre negocia\u00e7\u00e3o, conheci mulheres muito interessantes, comi bem e, acima de tudo, cheguei hoje ao trabalho renovada e recarregada. Como vivi tantos anos em Jacksonville sem conhecer isso? Nunca mais!","Marisa Carbone","Manager of Multimedia Production, JEA"),
  ("Eu estava mais do que animada para participar do Jacksonville Women\u2019s Leadership Forum de ontem. Dizer que sa\u00ed me sentindo empoderada, motivada e inspirada seria pouco.","Trina Forbess","ICE"),
  ("Tem sido uma parceria maravilhosa entre a JWLF e a Mercedes Benz of Orange Park e Jacksonville. Como patrocinadora de longa data dos eventos de networking da JWLF, pudemos apresentar nossos autom\u00f3veis, compartilhar a mensagem da Mercedes Benz sobre a prioridade que damos \u00e0s nossas clientes, e vimos um retorno tang\u00edvel do nosso investimento.","Debbie Mills","General Manager, Mercedes Benz of Orange Park"),
 ],
 officers_h="Nossa Diretoria 2026/2027",
 officer_roles=["Presidente do Conselho e Presidente","Vice-Presidente do Conselho e Vice-Presidente","Secret\u00e1ria","Tesoureira"],
 officers_btn="Ver o Conselho Diretor 2026/2027",
 sponsors_h="Agradecemos \u00e0s nossas patrocinadoras atuais e anteriores",
 sponsors_p="Mais de 150 mulheres executivas de grandes empresas locais participam dos eventos de networking e do F\u00f3rum anual do Jacksonville Women\u2019s Leadership Forum, recebendo treinamento de lideran\u00e7a de classe mundial.",
 sponsors_btn="Oportunidades de Patroc\u00ednio",
 cta_h="Fa\u00e7a parte do que vem a\u00ed", cta_p="Participe do pr\u00f3ximo F\u00f3rum, apresente sua empresa \u00e0s l\u00edderes de Jacksonville ou ajude a apoiar a pr\u00f3xima gera\u00e7\u00e3o.",
 cta_reg="Inscrever-se", cta_sponsor="Patrocinar", cta_donate="Doar",
 # Get involved
 t_gi="Participe", d_gi="Patrocine, seja volunt\u00e1ria, indique ou doe ao Jacksonville Women's Leadership Forum.",
 gi_h="Participe", gi_sub="Patrocine, seja volunt\u00e1ria, indique ou doe \u2014 cada caminho ajuda a impulsionar a pr\u00f3xima gera\u00e7\u00e3o de mulheres l\u00edderes da First Coast.",
 gi_sponsor_h="Patroc\u00ednio", gi_sponsor_p="Posicione sua marca diante de um p\u00fablico ideal de mulheres profissionais com mentalidade de lideran\u00e7a.",
 gi_vol_h="Voluntariado", gi_vol_p="Contribua com seu tempo e talento: divulga\u00e7\u00e3o, apoio em eventos ou pesquisa de conte\u00fado.",
 gi_wolf_h="Pr\u00eamio WoLF", gi_wolf_p="Indique uma mulher not\u00e1vel da nossa comunidade para o nosso reconhecimento anual.",
 gi_don_h="Doar", gi_don_p="Sua contribui\u00e7\u00e3o ajuda a apoiar e impulsionar a pr\u00f3xima gera\u00e7\u00e3o de mulheres l\u00edderes.",
 # About
 t_about="Sobre a JWLF", d_about="Sobre o Jacksonville Women's Leadership Forum, uma organiza\u00e7\u00e3o 501(c)(3).",
 about_h="Sobre a JWLF",
 about_sub="O prop\u00f3sito do Jacksonville Women\u2019s Leadership Forum \u00e9 apoiar e impulsionar a pr\u00f3xima gera\u00e7\u00e3o de mulheres l\u00edderes em nossas organiza\u00e7\u00f5es e na comunidade empresarial.",
 about_who_h="Quem somos",
 about_body="""<p>O Jacksonville Women\u2019s Leadership Forum \u00e9 a principal organiza\u00e7\u00e3o da First Coast que capacita mulheres a navegar com sucesso o terreno \u00fanico do mundo corporativo e a cultivar seu desenvolvimento pessoal. A JWLF vai transformar a maneira como as participantes abordam lideran\u00e7a, networking, avan\u00e7o de carreira e equil\u00edbrio de vida.</p>
<p>Por meio do F\u00f3rum anual e de eventos educacionais e de networking ao longo do ano, voc\u00ea ter\u00e1 acesso \u00e0s perspectivas de outras mulheres inteligentes e bem-sucedidas, todas focadas em enfrentar os desafios das mulheres que avan\u00e7am rumo ao topo.</p>
<p>O Jacksonville Women\u2019s Leadership Forum \u00e9 uma corpora\u00e7\u00e3o sem fins lucrativos 501(c)(3).</p>""",
 # Chair
 t_chair="Mensagem da Presidente", d_chair="Mensagem de boas-vindas de Cari Smith, Presidente da JWLF.",
 chair_h="Mensagem da Presidente",
 chair_body="""<h2 class="mt-0">Bem-vinda ao Jacksonville Women\u2019s Leadership Forum (JWLF)</h2>
<p>\u00c9 uma honra e um privil\u00e9gio servir como Presidente de uma organiza\u00e7\u00e3o dedicada a capacitar, conectar e inspirar mulheres em todo o nordeste da Fl\u00f3rida.</p>
<p>Acredito que lideran\u00e7a n\u00e3o \u00e9 ter todas as respostas: \u00e9 aprender, crescer, elevar os outros e criar oportunidades para que os demais tenham sucesso. Esse esp\u00edrito \u00e9 o que torna a JWLF uma comunidade t\u00e3o especial. Nossas integrantes v\u00eam de origens e experi\u00eancias diversas, mas estamos unidas por um compromisso compartilhado de apoiar o crescimento pessoal e profissional umas das outras.</p>
<p>Ao longo da minha carreira, descobri que os maiores sucessos acontecem por meio da colabora\u00e7\u00e3o, das experi\u00eancias compartilhadas e de ajudar os outros a alcan\u00e7ar seu pleno potencial. Liderar pelo exemplo, servir aos outros e tratar as pessoas com gentileza e respeito s\u00e3o valores que me guiam todos os dias e que me comprometo a trazer para a JWLF.</p>
<p>Tenho a sorte de servir ao lado de um <a href="./board.html">Conselho Diretor</a> excepcional, cuja lideran\u00e7a ajuda a definir o rumo da nossa organiza\u00e7\u00e3o. Com o apoio dos <a href="./sponsorship.html">nossos patrocinadores</a>, oferecemos uma programa\u00e7\u00e3o de impacto com <a href="./previous-speakers.html">palestrantes do F\u00f3rum</a> e pain\u00e9is que inspiram mulheres a liderar com confian\u00e7a, autenticidade e prop\u00f3sito. Tamb\u00e9m temos orgulho de reconhecer mulheres not\u00e1veis por meio do <a href="./wolf-award.html">Pr\u00eamio WoLF</a> anual e de fortalecer nossa comunidade por meio de <a href="./non-profit-partners.html">parcerias com organiza\u00e7\u00f5es sem fins lucrativos</a> dedicadas ao crescimento de mulheres e meninas no nordeste da Fl\u00f3rida.</p>
<p>Estendo minha sincera gratid\u00e3o \u00e0s integrantes do Conselho, volunt\u00e1rias, patrocinadores e palestrantes cuja dedica\u00e7\u00e3o torna a JWLF poss\u00edvel. Obrigada por fazer parte desta comunidade extraordin\u00e1ria. Espero me conectar com voc\u00ea ao longo do ano e celebrar tudo o que vamos conquistar juntas.</p>
<p>Com carinho,</p>""",
 chair_sig="Presidente do Conselho e Presidente,<br>Jacksonville Women\u2019s Leadership Forum",
 # Board
 t_board="Conselho Diretor e Diretoria", d_board="Conhe\u00e7a o Conselho Diretor e a Diretoria 2026/2027 da JWLF.",
 board_h="Conselho Diretor e Diretoria", board_sub="As l\u00edderes 2026/2027 que guiam o Jacksonville Women\u2019s Leadership Forum.",
 board_dir_h="Conselho Diretor 2026/2027", board_off_h="Diretoria 2026/2027",
 titles_note="Os cargos profissionais e nomes de empresas s\u00e3o exibidos em ingl\u00eas, como constam oficialmente.",
 # Partners
 t_partners="Parceiras Sem Fins Lucrativos", d_partners="Organiza\u00e7\u00f5es parceiras da JWLF que beneficiam mulheres e meninas.",
 partners_h="Parceiras Sem Fins Lucrativos", partners_sub="Promovemos e apoiamos organiza\u00e7\u00f5es sem fins lucrativos que beneficiam as mulheres da First Coast.",
 partner_more="Saiba mais e participe", partner_contact="Fale com a JWLF para saber mais",
 partners_btn="Interessada em ser parceira?",
 partner_descs=[
  "Seguran\u00e7a, empoderamento e apoio para sobreviventes de viol\u00eancia dom\u00e9stica nos condados de Duval e Baker.",
  "Organiza\u00e7\u00e3o estudantil da University of North Florida que conecta e desenvolve futuras mulheres de neg\u00f3cios.",
  "Aproxima meninas das carreiras STEM enquanto promove a sa\u00fade card\u00edaca das mulheres.",
  "Acelera oportunidades de aprendizagem STEM para estudantes do nordeste da Fl\u00f3rida.",
  "Recursos e apoio para mulheres veteranas.",
  "Forma meninas com coragem, confian\u00e7a e car\u00e1ter no norte da Fl\u00f3rida.",
  "Assist\u00eancia financeira e apoio para fam\u00edlias que vivem com c\u00e2ncer de mama.",
  "Oportunidades de moradia acess\u00edvel para fam\u00edlias de Jacksonville.",
  "Moradia e servi\u00e7os de apoio para mulheres e crian\u00e7as em Jacksonville.",
  "Educa\u00e7\u00e3o, aconselhamento e defesa de direitos para meninas e mulheres jovens.",
  "Combate \u00e0s doen\u00e7as card\u00edacas e ao AVC, as principais amea\u00e7as \u00e0 sa\u00fade das mulheres.",
  "Inspira meninas a serem alegres, saud\u00e1veis e confiantes por meio de programas baseados em corrida.",
  "Renova a esperan\u00e7a e as carreiras de sobreviventes do tr\u00e1fico de pessoas.",
  "Pesquisa, advocacy e a\u00e7\u00e3o em favor das meninas.",
 ],
 # Gallery
 t_gallery="Galeria de Fotos", d_gallery="Fotos dos F\u00f3runs anuais da JWLF, de 2012 at\u00e9 hoje.",
 gallery_h="Galeria de Fotos", gallery_sub="Momentos do F\u00f3rum anual do Jacksonville Women\u2019s Leadership Forum, de 2012 at\u00e9 hoje.",
 gallery_year="F\u00f3rum {year}", gallery_alt="Participantes e palestrantes no F\u00f3rum JWLF {year}",
 lb_close="Fechar visualizador de fotos", lb_prev="Foto anterior", lb_next="Pr\u00f3xima foto",
 # Blog
 t_blog="Blog da JWLF", d_blog="Artigos de lideran\u00e7a feminina da JWLF.",
 blog_h="Blog da JWLF", blog_sub="Artigos de lideran\u00e7a para impulsionar sua carreira e suas oportunidades.",
 blog_note="Os artigos do blog s\u00e3o publicados em seu ingl\u00eas original.",
 blog_read="Ler o artigo (em ingl\u00eas)",
 # Forum
 t_forum="Pr\u00f3ximo F\u00f3rum e Eventos", d_forum="O F\u00f3rum anual da JWLF e eventos educacionais ao longo do ano.",
 forum_h="F\u00f3runs e Eventos", forum_sub="Um F\u00f3rum anual de destaque, al\u00e9m de eventos educacionais e de networking ao longo do ano.",
 forum26_h="Nosso F\u00f3rum Anual de 2026", forum26_p="Nosso F\u00f3rum Anual de 2026 foi realizado em 17 de abril de 2026:",
 forum26_link="Conhe\u00e7a as palestrantes principais do F\u00f3rum JWLF 2026",
 idea_h="Tem uma ideia para o F\u00f3rum?",
 idea_p="O Jacksonville Women\u2019s Leadership Forum est\u00e1 sempre em busca de ideias novas. Escreva para n\u00f3s se tiver alguma sugest\u00e3o ou se quiser palestrar em nossos eventos educacionais!",
 idea_btn="Fale conosco",
 # Speakers
 t_speakers="Palestrantes e Painelistas Atuais", d_speakers="Palestrantes principais e painelistas do F\u00f3rum JWLF 2026.",
 speakers_h="Palestrantes e Painelistas Atuais",
 speakers_sub="Volte em 2027 para conhecer nosso pr\u00f3ximo F\u00f3rum. Enquanto isso, conhe\u00e7a as palestrantes do F\u00f3rum 2026.",
 bios_note="As biografias de palestrantes e painelistas s\u00e3o exibidas em seu ingl\u00eas original.",
 speakers_key_h="Palestrantes Principais 2026", speakers_pan_h="Painelistas 2026",
 # Previous
 t_prev="Palestrantes e Eventos Anteriores", d_prev="Temas de f\u00f3runs anteriores, palestrantes e painelistas da JWLF desde 2014.",
 prev_h="Palestrantes e Eventos Anteriores", prev_sub="Mais de uma d\u00e9cada de palestrantes, autoras e executivas de renome nacional no F\u00f3rum JWLF.",
 prev_topics_h="Temas de eventos anteriores",
 topics_note="Os t\u00edtulos dos temas s\u00e3o mantidos em seu ingl\u00eas original.",
 prev_bios_btn="Ver biografias completas das palestrantes (em ingl\u00eas)",
 prev_pan_h="Painelistas anteriores",
 # Sponsorship
 t_sp="Informa\u00e7\u00f5es de Patroc\u00ednio", d_sp="Pacotes e oportunidades de patroc\u00ednio com a JWLF.",
 sp_h="Informa\u00e7\u00f5es de Patroc\u00ednio",
 sp_sub="Posicione sua marca, sua mensagem e sua representante diante de um p\u00fablico ideal de mulheres profissionais com mentalidade de lideran\u00e7a.",
 sp_p1="O Jacksonville Women\u2019s Leadership Forum oferece patroc\u00ednios inovadores e acess\u00edveis, com diversas oportunidades de reconhecimento. Garanta que sua marca, sua mensagem e at\u00e9 sua representante sejam posicionadas com sucesso diante de um p\u00fablico ideal de mulheres profissionais e com mentalidade de lideran\u00e7a.",
 sp_p2="Mais de 150 mulheres executivas de grandes empresas locais participam dos eventos de networking e do F\u00f3rum anual, recebendo treinamento de lideran\u00e7a de classe mundial.",
 sp_quote="Tem sido uma parceria maravilhosa entre a JWLF e a Mercedes Benz of Orange Park e Jacksonville. Como patrocinadora de longa data, pudemos apresentar nossos autom\u00f3veis, compartilhar a mensagem da Mercedes Benz sobre a prioridade que damos \u00e0s nossas clientes, e vimos um retorno tang\u00edvel do nosso investimento. Ficamos felizes que v\u00e1rias integrantes e participantes da JWLF sejam hoje orgulhosas propriet\u00e1rias de autom\u00f3veis Mercedes Benz!",
 sp_pkg_h="Pacotes de Patroc\u00ednio",
 sp_pkg_p="Explore nossas oportunidades; se n\u00e3o encontrar um pacote adequado \u00e0 sua organiza\u00e7\u00e3o, fale conosco: estamos sempre abertos a criar um pacote sob medida.",
 sp_brochure="Baixe o folheto de patroc\u00ednio (PDF, em ingl\u00eas)",
 tier_names=["Patroc\u00ednio Vision\u00e1rio","Patroc\u00ednio Campe\u00e3o","Patroc\u00ednio Embaixador","Patroc\u00ednio Defensor","Patroc\u00ednio Apoiador"],
 perk_map=perk_map,
 sp_form_h="Torne-se Patrocinadora",
 sp_form_p="Obrigado pelo interesse em patrocinar. Preencha o formul\u00e1rio ou escreva para",
 sp_logos_h="Com orgulho reconhecemos nossas patrocinadoras anteriores e atuais",
 # Forms
 f_name="Nome", f_company="Empresa", f_email="E-mail", f_subject="Assunto",
 f_message="Mensagem", f_send="Enviar",
 e_name="Por favor, escreva seu nome.", e_company="Por favor, escreva sua empresa.",
 e_email="Por favor, informe um e-mail v\u00e1lido.", e_message="Por favor, inclua uma mensagem.",
 f_demo="Este formul\u00e1rio est\u00e1 em modo de demonstra\u00e7\u00e3o: \u00e9 validado no navegador, mas ainda n\u00e3o \u00e9 enviado.",
 f_success="Obrigado pela sua mensagem! Esta demonstra\u00e7\u00e3o confirma que sua mensagem foi validada corretamente. Enquanto conectamos o formul\u00e1rio, escreva para n\u00f3s por e-mail.",
 # Volunteer
 t_vol="Voluntariado", d_vol="Seja volunt\u00e1ria no Jacksonville Women's Leadership Forum.",
 vol_h="Voluntariado", vol_sub="Damos as boas-vindas \u00e0s mulheres que desejam doar seu tempo, talento e recursos \u00e0 JWLF.",
 vol_p="Nosso programa depende de volunt\u00e1rias dedicadas para promover sua miss\u00e3o. Se voc\u00ea tem um talento a contribuir, conte para n\u00f3s e trabalharemos juntas para que seu servi\u00e7o volunt\u00e1rio seja significativo. Sempre precisamos de volunt\u00e1rias nas seguintes categorias:",
 vol_c1_h="Divulga\u00e7\u00e3o", vol_c1_p="Apoie divulgando a JWLF nas redes sociais e/ou ajudando com o conte\u00fado do boletim informativo.",
 vol_c2_h="Apoio em Eventos", vol_c2_p="Ajude a preparar os locais dos eventos para receber as convidadas e/ou apoie durante o evento.",
 vol_c3_h="Conte\u00fado do F\u00f3rum", vol_c3_p="Ajude a identificar e pesquisar futuras palestrantes, temas do f\u00f3rum e/ou organiza\u00e7\u00f5es parceiras locais.",
 vol_form_h="Inscreva-se como volunt\u00e1ria", vol_f_msg="Como voc\u00ea gostaria de ajudar?",
 # WoLF
 t_wolf="Pr\u00eamio WoLF", d_wolf="O Pr\u00eamio WoLF da JWLF reconhece anualmente uma mulher not\u00e1vel da comunidade.",
 wolf_h="O Pr\u00eamio WoLF", wolf_sub="Reconhecendo a cada ano uma mulher not\u00e1vel da nossa comunidade.",
 wolf_p1="O Pr\u00eamio WoLF foi criado para reconhecer, a cada ano, uma mulher not\u00e1vel da nossa comunidade. Intencionalmente, existe um forte v\u00ednculo entre JWLF e WoLF (\u201cloba\u201d em ingl\u00eas), demonstrado por certos atributos essenciais. Os lobos s\u00e3o animais muito inteligentes e sociais, que tiram sua for\u00e7a da intera\u00e7\u00e3o entre si e compartilham um prop\u00f3sito comum: garantir a sobreviv\u00eancia da alcateia. Como parte da fam\u00edlia, cada lobo adulto assume a responsabilidade de oferecer cuidado, alimento, abrigo, forma\u00e7\u00e3o, prote\u00e7\u00e3o e brincadeira, sabendo que o futuro da alcateia est\u00e1 nas m\u00e3os dos filhotes. Agem com estrat\u00e9gia e com um senso de prop\u00f3sito compartilhado.",
 wolf_crit_h="Crit\u00e9rios de indica\u00e7\u00e3o",
 wolf_crit_p="A homenageada ser\u00e1 uma mulher da nossa comunidade que tenha demonstrado esses atributos de forma extraordin\u00e1ria: intelig\u00eancia, lealdade, resili\u00eancia, disciplina, comunica\u00e7\u00e3o, compaix\u00e3o, fam\u00edlia, trabalho em equipe e equil\u00edbrio de vida.",
 wolf_c1_h="Lealdade, Resili\u00eancia e Fam\u00edlia",
 wolf_c1_p="Nenhum outro mam\u00edfero demonstra devo\u00e7\u00e3o t\u00e3o intensa \u00e0 sua fam\u00edlia ou grupo quanto o lobo. Seu prop\u00f3sito de vida \u00e9 garantir a sobreviv\u00eancia da alcateia; cada integrante assume a responsabilidade pelo alimento, abrigo, forma\u00e7\u00e3o, prote\u00e7\u00e3o e brincadeira dos filhotes. A alcateia sempre sabe que os jovens s\u00e3o o seu futuro.",
 wolf_c2_h="Disciplina, Compaix\u00e3o e Equil\u00edbrio de Vida",
 wolf_c2_p="Os lobos s\u00e3o animais muito sociais que tiram sua for\u00e7a do contato entre si. A brincadeira refina suas habilidades de comunica\u00e7\u00e3o, trabalho em equipe e ca\u00e7a, tornando-os mais fortes f\u00edsica e mentalmente. N\u00e3o escolhem nem perseguem sua presa sem sentido: s\u00e3o observadores atentos que agem com prop\u00f3sito, buscando a vit\u00f3ria de longo prazo em vez do sucesso imediato.",
 wolf_c3_h="Intelig\u00eancia, Trabalho em Equipe e Comunica\u00e7\u00e3o",
 wolf_c3_p="Nem todos os integrantes da alcateia aspiram a ser o chefe; alguns preferem ser ca\u00e7adores, cuidadores ou batedores, mas cada um tem um papel crucial na equipe. Os lobos n\u00e3o dependem de uma \u00fanica forma de comunica\u00e7\u00e3o: uivam, se acariciam e usam uma linguagem corporal intrincada que lhes permite ajustar a estrat\u00e9gia a cada segundo para alcan\u00e7ar o sucesso.",
 wolf_cta_h="Indique uma WoLF",
 wolf_cta_p="Se voc\u00ea conhece uma mulher da nossa comunidade que apresenta essas caracter\u00edsticas, realizou algo monumental ou vive esses valores, considere indic\u00e1-la para o nosso pr\u00f3ximo Pr\u00eamio WoLF. Os pr\u00eamios s\u00e3o entregues durante o nosso F\u00f3rum Anual. Para indicar, envie o nome da candidata e sua biografia por e-mail.",
 wolf_cta_btn="Enviar uma indica\u00e7\u00e3o",
 # Donate
 t_don="Fa\u00e7a uma Doa\u00e7\u00e3o", d_don="Doe ao Jacksonville Women's Leadership Forum, organiza\u00e7\u00e3o 501(c)(3).",
 don_h="Fa\u00e7a uma Doa\u00e7\u00e3o", don_sub="Sua contribui\u00e7\u00e3o ajuda a apoiar e impulsionar a pr\u00f3xima gera\u00e7\u00e3o de mulheres l\u00edderes.",
 don_body_h="Apoie a JWLF hoje",
 don_p="Considere fazer uma doa\u00e7\u00e3o ao Jacksonville Women\u2019s Leadership Forum hoje! Sua contribui\u00e7\u00e3o ajudar\u00e1 a apoiar e impulsionar a pr\u00f3xima gera\u00e7\u00e3o de mulheres l\u00edderes em nossas organiza\u00e7\u00f5es e na comunidade empresarial.",
 don_btn="Doar via PayPal", don_q="D\u00favidas? Fale conosco",
 don_where_h="Para onde vai sua doa\u00e7\u00e3o",
 don_where_p="A JWLF \u00e9 uma organiza\u00e7\u00e3o 501(c)(3) operada por volunt\u00e1rias. Doa\u00e7\u00f5es e patroc\u00ednios financiam o F\u00f3rum anual, os eventos educacionais e de networking, e nosso apoio a organiza\u00e7\u00f5es parceiras que servem \u00e0s mulheres da First Coast.",
 # Contact
 t_con="Contato", d_con="Fale com o Jacksonville Women's Leadership Forum.",
 con_h="Fale com a JWLF", con_sub="Adorar\u00edamos ouvir voc\u00ea!",
 con_form_h="Envie uma mensagem", con_p="Escreva para n\u00f3s em", con_follow_h="Siga-nos",
)

build_lang("pt", T)
print("Portuguese site done")
