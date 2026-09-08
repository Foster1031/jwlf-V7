# -*- coding: utf-8 -*-
# Spanish (es) site content. Testimonial quotes are marked as translations;
# speaker bios, blog articles, and the FL legal disclosure remain in English.
from i18n_pages import build_lang

perk_map = {
 "Company recognition at JWLF Forum as highest-level sponsor": "Reconocimiento de la empresa en el Foro JWLF como patrocinador de m\u00e1s alto nivel",
 "Company recognition at JWLF Forum as sponsor": "Reconocimiento de la empresa como patrocinador en el Foro JWLF",
 "Company recognition at JWLF Forum": "Reconocimiento de la empresa en el Foro JWLF",
 "Company logo included on all JWLF promotional and marketing materials (prominent position)": "Logotipo de la empresa en todos los materiales promocionales y de marketing de JWLF (posici\u00f3n destacada)",
 "Company logo included on all JWLF promotional and marketing materials": "Logotipo de la empresa en todos los materiales promocionales y de marketing de JWLF",
 "Discounted rate for company participants to attend JWLF programming held throughout the year": "Tarifa con descuento para que participantes de la empresa asistan a la programaci\u00f3n de JWLF durante todo el a\u00f1o",
 "Opportunity to provide swag at all events": "Oportunidad de entregar art\u00edculos promocionales en todos los eventos",
 "Company full-page ad in JWLF event program": "Anuncio de p\u00e1gina completa en el programa del evento de JWLF",
 "Company half-page ad in JWLF event program": "Anuncio de media p\u00e1gina en el programa del evento de JWLF",
 "Opportunity for company showcase or speaker at educational events": "Oportunidad de presentar a la empresa o a un ponente en los eventos educativos",
 "Two sponsor board of director seats": "Dos asientos de patrocinador en la junta directiva",
 "Group photo of company attendees at the Annual JWLF Forum": "Foto grupal de los asistentes de la empresa en el Foro Anual de JWLF",
 "Opportunity to provide panelist at JWLF Forum": "Oportunidad de aportar un panelista en el Foro JWLF",
 "Opportunity to \u201cown\u201d your part in the JWLF Forum (luncheon, breakfast)": "Oportunidad de \u201capadrinar\u201d una parte del Foro JWLF (almuerzo, desayuno)",
 "Opportunity to \u201cown\u201d your part in the JWLF Forum (pre-event reception, post-event social)": "Oportunidad de \u201capadrinar\u201d una parte del Foro JWLF (recepci\u00f3n previa, convivencia posterior)",
}
for n in (20, 16, 14, 4):
    perk_map[f"{n} tickets to the Annual JWLF Forum"] = f"{n} boletos para el Foro Anual de JWLF"

T = dict(
 translated_note="traducci\u00f3n",
 # Home
 t_home="Bienvenida a JWLF", d_home="El Jacksonville Women's Leadership Forum empodera a las mujeres para navegar el mundo corporativo y cultivar su desarrollo personal.",
 hero_h1="Mujeres trabajando juntas para formar l\u00edderes y avanzar carreras",
 hero_p="El Jacksonville Women\u2019s Leadership Forum es la organizaci\u00f3n l\u00edder de la Primera Costa de Florida que empodera a las mujeres para navegar con \u00e9xito el terreno \u00fanico del mundo corporativo y cultivar su desarrollo personal.",
 hero_cta1="Conoce el Foro", hero_cta2="Convi\u00e9rtete en Patrocinador",
 welcome_h="Bienvenida al Jacksonville Women\u2019s Leadership Forum",
 welcome_p="JWLF transformar\u00e1 la manera en que las participantes abordan el liderazgo, las redes profesionales, el avance de su carrera y el equilibrio de vida. A trav\u00e9s del Foro anual y de eventos educativos y de networking durante todo el a\u00f1o, obtendr\u00e1s las perspectivas de otras mujeres inteligentes y exitosas, enfocadas en los retos de las mujeres que avanzan hacia la cima.",
 pillars=[
  ("Fortalecer Habilidades de Liderazgo","Ampliamos las oportunidades de liderazgo para futuras ejecutivas en un entorno exclusivo entre pares. Deja que JWLF expanda tu potencial profesional, desarrolle habilidades cr\u00edticas y establezca objetivos de carrera alcanzables y sostenibles."),
  ("Ampliar tu Red Profesional","Buscamos ampliar la red profesional y la visibilidad de cada participante en la comunidad empresarial de Jacksonville. JWLF te ayudar\u00e1 a maximizar tus redes y aprovechar su influencia."),
  ("Avanzar Carreras","Ofrecemos oportunidades de desarrollo profesional mediante mentor\u00eda y educaci\u00f3n continua. Aprende a aprovechar tu propuesta de valor \u00fanica para avanzar en tu carrera."),
  ("Encontrar Equilibrio de Vida","Te ayudamos a encontrar ese equilibrio de vida que toda profesional desea. Aprende nuevas t\u00e9cnicas y consejos pr\u00e1cticos para equilibrar el \u00e9xito personal mientras creces tu marca profesional."),
 ],
 theme_pre="Nuestro tema anual 2026\u20132027",
 theme_line="Lidera con claridad. Influye con confianza. Crece con intenci\u00f3n.",
 theme_status="Compartiremos la informaci\u00f3n de nuestro Foro Anual 2027 en los pr\u00f3ximos meses.",
 theme_btn="Reg\u00edstrate en 2027",
 who_h="\u00bfQui\u00e9n deber\u00eda asistir?",
 who_items=["Mujeres en puestos directivos identificadas como l\u00edderes proactivas con alto potencial y logros",
  "Gerentes de nivel medio y alto que lideran equipos y suelen tener personal a su cargo",
  "Mujeres con varios a\u00f1os de experiencia en roles de liderazgo",
  "Mujeres y hombres con influencia en sus organizaciones, comprometidos con empoderar a la pr\u00f3xima generaci\u00f3n de mujeres l\u00edderes"],
 who_btn="Ver el pr\u00f3ximo Foro",
 alt_networking="Asistentes en un Foro de JWLF", alt_speaker="Una ponente en el Foro de JWLF",
 testimonials_h="Lo que dicen las asistentes",
 testimonials=[
  ("Gracias de nuevo por la oportunidad de vivir el Jacksonville Women\u2019s Leadership Forum. Aprend\u00ed cosas valiosas sobre negociaci\u00f3n, conoc\u00ed a mujeres muy interesantes, com\u00ed muy bien y, sobre todo, llegu\u00e9 hoy al trabajo renovada y con energ\u00eda. \u00bfC\u00f3mo viv\u00ed tantos a\u00f1os en Jacksonville sin conocer esto? \u00a1Nunca m\u00e1s!","Marisa Carbone","Manager of Multimedia Production, JEA"),
  ("Estaba m\u00e1s que emocionada de asistir al Jacksonville Women\u2019s Leadership Forum de ayer. Decir que sal\u00ed sinti\u00e9ndome empoderada, motivada e inspirada se queda corto.","Trina Forbess","ICE"),
  ("Ha sido una alianza maravillosa entre JWLF y Mercedes Benz of Orange Park y Jacksonville. Como patrocinador de largo plazo de los eventos de networking de JWLF, hemos podido exhibir nuestros autom\u00f3viles, compartir el mensaje de Mercedes Benz sobre la prioridad que damos a nuestras clientas, y hemos visto un retorno tangible de nuestra inversi\u00f3n.","Debbie Mills","General Manager, Mercedes Benz of Orange Park"),
 ],
 officers_h="Nuestras Oficiales 2026/2027",
 officer_roles=["Presidenta de la Junta y Presidenta","Vicepresidenta de la Junta y Vicepresidenta","Secretaria","Tesorera"],
 officers_btn="Ver la Junta Directiva 2026/2027",
 sponsors_h="Gracias a nuestros patrocinadores actuales y anteriores",
 sponsors_p="M\u00e1s de 150 mujeres ejecutivas de grandes empresas locales asisten a los eventos de networking y al Foro anual del Jacksonville Women\u2019s Leadership Forum, recibiendo capacitaci\u00f3n de liderazgo de clase mundial.",
 sponsors_btn="Oportunidades de Patrocinio",
 cta_h="S\u00e9 parte de lo que viene", cta_p="\u00danete al pr\u00f3ximo Foro, presenta tu empresa ante las l\u00edderes de Jacksonville o ayuda a apoyar a la pr\u00f3xima generaci\u00f3n.",
 cta_reg="Registrarse", cta_sponsor="Patrocinar", cta_donate="Donar",
 # Get involved
 t_gi="Participa", d_gi="Patrocina, s\u00e9 voluntaria, nomina o dona al Jacksonville Women's Leadership Forum.",
 gi_h="Participa", gi_sub="Patrocina, s\u00e9 voluntaria, nomina o dona \u2014 cada camino ayuda a impulsar a la pr\u00f3xima generaci\u00f3n de mujeres l\u00edderes de la Primera Costa.",
 gi_sponsor_h="Patrocinio", gi_sponsor_p="Posiciona tu marca ante un p\u00fablico ideal de mujeres profesionales con mentalidad de liderazgo.",
 gi_vol_h="Voluntariado", gi_vol_p="Aporta tu tiempo y talento: promoci\u00f3n, apoyo en eventos o investigaci\u00f3n de contenidos.",
 gi_wolf_h="Premio WoLF", gi_wolf_p="Nomina a una mujer destacada de nuestra comunidad para nuestro reconocimiento anual.",
 gi_don_h="Donar", gi_don_p="Tu contribuci\u00f3n ayuda a apoyar y avanzar a la pr\u00f3xima generaci\u00f3n de mujeres l\u00edderes.",
 # About
 t_about="Acerca de JWLF", d_about="Acerca del Jacksonville Women's Leadership Forum, una organizaci\u00f3n 501(c)(3).",
 about_h="Acerca de JWLF",
 about_sub="El prop\u00f3sito del Jacksonville Women\u2019s Leadership Forum es apoyar y avanzar a la pr\u00f3xima generaci\u00f3n de mujeres l\u00edderes dentro de nuestras organizaciones y comunidad empresarial.",
 about_who_h="Qui\u00e9nes somos",
 about_body="""<p>El Jacksonville Women\u2019s Leadership Forum es la organizaci\u00f3n l\u00edder de la Primera Costa que empodera a las mujeres para navegar con \u00e9xito el terreno \u00fanico del mundo corporativo y cultivar su desarrollo personal. JWLF transformar\u00e1 la manera en que las participantes abordan el liderazgo, las redes profesionales, el avance de su carrera y el equilibrio de vida.</p>
<p>A trav\u00e9s del Foro anual y de eventos educativos y de networking durante todo el a\u00f1o, obtendr\u00e1s las perspectivas de otras mujeres inteligentes y exitosas, todas enfocadas en abordar los retos que enfrentan las mujeres que avanzan hacia la cima.</p>
<p>El Jacksonville Women\u2019s Leadership Forum es una corporaci\u00f3n sin fines de lucro 501(c)(3).</p>""",
 # Chair
 t_chair="Mensaje de la Presidenta", d_chair="Mensaje de bienvenida de Cari Smith, Presidenta del JWLF.",
 chair_h="Mensaje de la Presidenta",
 chair_body="""<h2 class="mt-0">Bienvenida al Jacksonville Women\u2019s Leadership Forum (JWLF)</h2>
<p>Es un honor y un privilegio servir como Presidenta de una organizaci\u00f3n dedicada a empoderar, conectar e inspirar a las mujeres del noreste de Florida.</p>
<p>Creo que el liderazgo no consiste en tener todas las respuestas: consiste en aprender, crecer, elevar a los dem\u00e1s y crear oportunidades para que otros tengan \u00e9xito. Ese esp\u00edritu es lo que hace de JWLF una comunidad tan especial. Nuestras integrantes provienen de or\u00edgenes y experiencias diversas, pero nos une un compromiso compartido de apoyar el crecimiento personal y profesional de cada una.</p>
<p>A lo largo de mi carrera he comprobado que los mayores \u00e9xitos surgen de la colaboraci\u00f3n, de las experiencias compartidas y de ayudar a los dem\u00e1s a alcanzar su m\u00e1ximo potencial. Liderar con el ejemplo, servir a los dem\u00e1s y tratar a las personas con amabilidad y respeto son valores que me gu\u00edan cada d\u00eda y que me comprometo a aportar a JWLF.</p>
<p>Tengo la fortuna de servir junto a una <a href="./board.html">Junta Directiva</a> excepcional, cuyo liderazgo ayuda a definir el rumbo de nuestra organizaci\u00f3n. Junto con el apoyo de <a href="./sponsorship.html">nuestros patrocinadores</a>, ofrecemos una programaci\u00f3n de impacto con <a href="./previous-speakers.html">ponentes del Foro</a> y paneles que inspiran a las mujeres a liderar con confianza, autenticidad y prop\u00f3sito. Tambi\u00e9n nos enorgullece reconocer a mujeres sobresalientes a trav\u00e9s del <a href="./wolf-award.html">Premio WoLF</a> anual y fortalecer nuestra comunidad mediante <a href="./non-profit-partners.html">alianzas con organizaciones sin fines de lucro</a> dedicadas al crecimiento de mujeres y ni\u00f1as en el noreste de Florida.</p>
<p>Quiero extender mi sincero agradecimiento a las integrantes de la Junta, voluntarias, patrocinadores y ponentes cuya dedicaci\u00f3n hace posible JWLF. Gracias por ser parte de esta comunidad extraordinaria. Espero conectar contigo durante el a\u00f1o y celebrar todo lo que lograremos juntas.</p>
<p>Con afecto,</p>""",
 chair_sig="Presidenta de la Junta y Presidenta,<br>Jacksonville Women\u2019s Leadership Forum",
 # Board
 t_board="Junta Directiva y Oficiales", d_board="Conoce a la Junta Directiva y Oficiales 2026/2027 del JWLF.",
 board_h="Junta Directiva y Oficiales", board_sub="Las l\u00edderes 2026/2027 que gu\u00edan al Jacksonville Women\u2019s Leadership Forum.",
 board_dir_h="Junta Directiva 2026/2027", board_off_h="Oficiales 2026/2027",
 titles_note="Los cargos profesionales y nombres de empresas se muestran en ingl\u00e9s, tal como aparecen oficialmente.",
 # Partners
 t_partners="Organizaciones Aliadas", d_partners="Organizaciones sin fines de lucro aliadas de JWLF que benefician a mujeres y ni\u00f1as.",
 partners_h="Organizaciones Aliadas", partners_sub="Promovemos y apoyamos a organizaciones sin fines de lucro que benefician a las mujeres de la Primera Costa.",
 partner_more="Conoce m\u00e1s y participa", partner_contact="Contacta a JWLF para saber m\u00e1s",
 partners_btn="\u00bfInteresada en ser aliada?",
 partner_descs=[
  "Seguridad, empoderamiento y apoyo para sobrevivientes de violencia dom\u00e9stica en los condados de Duval y Baker.",
  "Organizaci\u00f3n estudiantil de la University of North Florida que conecta y desarrolla a futuras empresarias.",
  "Acerca a las ni\u00f1as a las carreras STEM mientras promueve la salud cardiaca de las mujeres.",
  "Acelera las oportunidades de aprendizaje STEM para estudiantes del noreste de Florida.",
  "Recursos y apoyo para mujeres veteranas.",
  "Forma ni\u00f1as con valent\u00eda, confianza y car\u00e1cter en el norte de Florida.",
  "Asistencia financiera y apoyo para familias que viven con c\u00e1ncer de mama.",
  "Oportunidades de vivienda accesible para familias de Jacksonville.",
  "Vivienda y servicios de apoyo para mujeres y ni\u00f1os en Jacksonville.",
  "Educaci\u00f3n, consejer\u00eda y defensa para ni\u00f1as y mujeres j\u00f3venes.",
  "Lucha contra las enfermedades cardiacas y los derrames cerebrales, las principales amenazas para la salud de las mujeres.",
  "Inspira a las ni\u00f1as a ser alegres, sanas y seguras a trav\u00e9s de programas basados en correr.",
  "Renueva la esperanza y las carreras de sobrevivientes de trata de personas.",
  "Investigaci\u00f3n, defensa y acci\u00f3n en favor de las ni\u00f1as.",
 ],
 # Gallery
 t_gallery="Galer\u00eda de Fotos", d_gallery="Fotos de los Foros anuales del JWLF, de 2012 a la fecha.",
 gallery_h="Galer\u00eda de Fotos", gallery_sub="Momentos del Foro anual del Jacksonville Women\u2019s Leadership Forum, de 2012 a hoy.",
 gallery_year="Foro {year}", gallery_alt="Asistentes y ponentes en el Foro JWLF {year}",
 lb_close="Cerrar visor de fotos", lb_prev="Foto anterior", lb_next="Foto siguiente",
 # Blog
 t_blog="Blog de JWLF", d_blog="Art\u00edculos de liderazgo femenino del JWLF.",
 blog_h="Blog de JWLF", blog_sub="Art\u00edculos de liderazgo para avanzar tu carrera y tus oportunidades.",
 blog_note="Los art\u00edculos del blog se publican en su ingl\u00e9s original.",
 blog_read="Leer el art\u00edculo (en ingl\u00e9s)",
 # Forum
 t_forum="Pr\u00f3ximo Foro y Eventos", d_forum="El Foro anual del JWLF y eventos educativos durante el a\u00f1o.",
 forum_h="Foros y Eventos", forum_sub="Un Foro anual insignia, m\u00e1s eventos educativos y de networking durante todo el a\u00f1o.",
 forum26_h="Nuestro Foro Anual 2026", forum26_p="Nuestro Foro Anual 2026 se celebr\u00f3 el 17 de abril de 2026:",
 forum26_link="Conoce a las ponentes principales del Foro JWLF 2026",
 idea_h="\u00bfTienes una idea para el Foro?",
 idea_p="El Jacksonville Women\u2019s Leadership Forum siempre busca ideas frescas. \u00a1Escr\u00edbenos si tienes alguna sugerencia o te interesa ser ponente en nuestros eventos educativos!",
 idea_btn="Cont\u00e1ctanos",
 # Speakers
 t_speakers="Ponentes y Panelistas Actuales", d_speakers="Ponentes principales y panelistas del Foro JWLF 2026.",
 speakers_h="Ponentes y Panelistas Actuales",
 speakers_sub="Visita en 2027 para conocer nuestro pr\u00f3ximo Foro. Mientras tanto, conoce a las ponentes del Foro 2026.",
 bios_note="Las biograf\u00edas de ponentes y panelistas se muestran en su ingl\u00e9s original.",
 speakers_key_h="Ponentes Principales 2026", speakers_pan_h="Panelistas 2026",
 # Previous
 t_prev="Ponentes y Eventos Anteriores", d_prev="Temas de foros anteriores, ponentes y panelistas del JWLF desde 2014.",
 prev_h="Ponentes y Eventos Anteriores", prev_sub="M\u00e1s de una d\u00e9cada de ponentes, autoras y ejecutivas de renombre nacional en el Foro JWLF.",
 prev_topics_h="Temas de eventos anteriores",
 topics_note="Los t\u00edtulos de los temas se conservan en su ingl\u00e9s original.",
 prev_bios_btn="Ver biograf\u00edas completas de ponentes (en ingl\u00e9s)",
 prev_pan_h="Panelistas anteriores",
 # Sponsorship
 t_sp="Informaci\u00f3n de Patrocinio", d_sp="Paquetes y oportunidades de patrocinio con el JWLF.",
 sp_h="Informaci\u00f3n de Patrocinio",
 sp_sub="Posiciona tu marca, tu mensaje y a tu representante ante un p\u00fablico ideal de mujeres profesionales con mentalidad de liderazgo.",
 sp_p1="El Jacksonville Women\u2019s Leadership Forum ofrece patrocinios innovadores y accesibles, con diversas oportunidades de reconocimiento. Aseg\u00farate de que tu marca, tu mensaje e incluso tu representante se posicionen con \u00e9xito ante un p\u00fablico ideal de mujeres profesionales y con mentalidad de liderazgo.",
 sp_p2="M\u00e1s de 150 mujeres ejecutivas de grandes empresas locales asisten a los eventos de networking y al Foro anual, recibiendo capacitaci\u00f3n de liderazgo de clase mundial.",
 sp_quote="Ha sido una alianza maravillosa entre JWLF y Mercedes Benz of Orange Park y Jacksonville. Como patrocinador de largo plazo, hemos podido exhibir nuestros autom\u00f3viles, compartir el mensaje de Mercedes Benz sobre la prioridad que damos a nuestras clientas, y hemos visto un retorno tangible de nuestra inversi\u00f3n. \u00a1Nos encanta que varias integrantes y asistentes de JWLF sean ahora orgullosas propietarias de autom\u00f3viles Mercedes Benz!",
 sp_pkg_h="Paquetes de Patrocinio",
 sp_pkg_p="Explora nuestras oportunidades; si no encuentras un paquete que se ajuste a tu organizaci\u00f3n, cont\u00e1ctanos: siempre estamos abiertos a crear un paquete a la medida.",
 sp_brochure="Descarga el folleto de patrocinio (PDF, en ingl\u00e9s)",
 tier_names=["Patrocinio Visionario","Patrocinio Campe\u00f3n","Patrocinio Embajador","Patrocinio Defensor","Patrocinio Colaborador"],
 perk_map=perk_map,
 sp_form_h="Convi\u00e9rtete en Patrocinador",
 sp_form_p="Gracias por tu inter\u00e9s en ser patrocinador. Completa el formulario o escr\u00edbenos a",
 sp_logos_h="Con orgullo reconocemos a nuestros patrocinadores anteriores y actuales",
 # Forms
 f_name="Nombre", f_company="Empresa", f_email="Correo electr\u00f3nico", f_subject="Asunto",
 f_message="Mensaje", f_send="Enviar", 
 e_name="Por favor escribe tu nombre.", e_company="Por favor escribe tu empresa.",
 e_email="Por favor escribe un correo v\u00e1lido.", e_message="Por favor incluye un mensaje.",
 f_demo="Este formulario est\u00e1 en modo de demostraci\u00f3n: se valida en tu navegador pero a\u00fan no se env\u00eda.",
 f_success="\u00a1Gracias por tu mensaje! Esta demostraci\u00f3n confirma que tu mensaje se valid\u00f3 correctamente. Mientras conectamos el formulario, escr\u00edbenos por correo electr\u00f3nico.",
 # Volunteer
 t_vol="Voluntariado", d_vol="S\u00e9 voluntaria con el Jacksonville Women's Leadership Forum.",
 vol_h="Voluntariado", vol_sub="Damos la bienvenida a las mujeres que deseen aportar su tiempo, talento y recursos a JWLF.",
 vol_p="Nuestro programa depende de voluntarias dedicadas para promover su misi\u00f3n. Si tienes un talento que aportar, cu\u00e9ntanos cu\u00e1l es y trabajaremos contigo para que tu servicio voluntario sea significativo. Siempre necesitamos voluntarias en las siguientes categor\u00edas:",
 vol_c1_h="Promoci\u00f3n", vol_c1_p="Apoya promoviendo a JWLF en redes sociales y/o ayudando con el contenido del bolet\u00edn.",
 vol_c2_h="Apoyo en Eventos", vol_c2_p="Ay\u00fadanos a preparar las sedes para recibir a las invitadas y/o apoya durante el evento.",
 vol_c3_h="Contenido del Foro", vol_c3_p="Ay\u00fadanos a identificar e investigar futuras ponentes, temas del foro y/o organizaciones aliadas locales.",
 vol_form_h="Inscr\u00edbete como voluntaria", vol_f_msg="\u00bfC\u00f3mo te gustar\u00eda ayudar?",
 # WoLF
 t_wolf="Premio WoLF", d_wolf="El Premio WoLF del JWLF reconoce cada a\u00f1o a una mujer sobresaliente de la comunidad.",
 wolf_h="El Premio WoLF", wolf_sub="Reconociendo cada a\u00f1o a una mujer sobresaliente de nuestra comunidad.",
 wolf_p1="El Premio WoLF se cre\u00f3 para reconocer cada a\u00f1o a una mujer sobresaliente de nuestra comunidad. De manera intencional existe un fuerte v\u00ednculo entre JWLF y WoLF (\u201cloba\u201d en ingl\u00e9s), demostrado por ciertos atributos clave. Los lobos son animales muy inteligentes y sociales que obtienen su fuerza de la interacci\u00f3n mutua y comparten un prop\u00f3sito com\u00fan: asegurar la supervivencia de la manada. Como parte de la familia, cada lobo adulto asume la responsabilidad de brindar cuidado, alimento, refugio, formaci\u00f3n, protecci\u00f3n y juego, consciente de que el futuro de la manada est\u00e1 en manos de sus cr\u00edas. Act\u00faan con estrategia y con un sentido de prop\u00f3sito compartido.",
 wolf_crit_h="Criterios de nominaci\u00f3n",
 wolf_crit_p="La galardonada ser\u00e1 una mujer de nuestra comunidad que haya demostrado estos atributos de manera extraordinaria: inteligencia, lealtad, resiliencia, disciplina, comunicaci\u00f3n, compasi\u00f3n, familia, trabajo en equipo y equilibrio de vida.",
 wolf_c1_h="Lealtad, Resiliencia y Familia",
 wolf_c1_p="Ning\u00fan otro mam\u00edfero muestra una devoci\u00f3n tan intensa hacia su familia u organizaci\u00f3n como el lobo. Su prop\u00f3sito de vida es asegurar la supervivencia de la manada; cada integrante asume la responsabilidad del alimento, el refugio, la formaci\u00f3n, la protecci\u00f3n y el juego de los cachorros. La manada siempre sabe que los j\u00f3venes son su futuro.",
 wolf_c2_h="Disciplina, Compasi\u00f3n y Equilibrio de Vida",
 wolf_c2_p="Los lobos son animales muy sociales que obtienen su fuerza del contacto entre s\u00ed. El juego refina sus habilidades de comunicaci\u00f3n, trabajo en equipo y caza, y los hace m\u00e1s fuertes f\u00edsica y mentalmente. No eligen ni acosan a su presa sin sentido: son observadores agudos que act\u00faan con prop\u00f3sito, buscando la victoria de largo plazo en lugar del \u00e9xito inmediato.",
 wolf_c3_h="Inteligencia, Trabajo en Equipo y Comunicaci\u00f3n",
 wolf_c3_p="No todos los integrantes de la manada aspiran a ser el jefe; algunos prefieren ser cazadores, cuidadores o exploradores, pero cada uno tiene un papel crucial en el equipo. Los lobos no dependen de una sola forma de comunicaci\u00f3n: a\u00fallan, se acarician y usan un lenguaje corporal intrincado que les permite ajustar su estrategia a cada segundo para alcanzar el \u00e9xito.",
 wolf_cta_h="Nomina a una WoLF",
 wolf_cta_p="Si conoces a una mujer de nuestra comunidad que exhiba estas caracter\u00edsticas, haya logrado algo monumental o viva estos valores, consid\u00e9rala para nuestro pr\u00f3ximo Premio WoLF. Los premios se entregan durante nuestro Foro Anual. Para nominar, env\u00eda el nombre de la candidata y su biograf\u00eda por correo.",
 wolf_cta_btn="Enviar una nominaci\u00f3n",
 # Donate
 t_don="Haz una Donaci\u00f3n", d_don="Dona al Jacksonville Women's Leadership Forum, organizaci\u00f3n 501(c)(3).",
 don_h="Haz una Donaci\u00f3n", don_sub="Tu contribuci\u00f3n ayuda a apoyar y avanzar a la pr\u00f3xima generaci\u00f3n de mujeres l\u00edderes.",
 don_body_h="Apoya a JWLF hoy",
 don_p="\u00a1Considera hacer una donaci\u00f3n al Jacksonville Women\u2019s Leadership Forum hoy! Tu contribuci\u00f3n ayudar\u00e1 a apoyar y avanzar a la pr\u00f3xima generaci\u00f3n de mujeres l\u00edderes dentro de nuestras organizaciones y comunidad empresarial.",
 don_btn="Donar v\u00eda PayPal", don_q="\u00bfPreguntas? Cont\u00e1ctanos",
 don_where_h="A d\u00f3nde va tu donativo",
 don_where_p="JWLF es una organizaci\u00f3n 501(c)(3) operada por voluntarias. Los donativos y patrocinios financian el Foro anual, los eventos educativos y de networking, y nuestro apoyo a organizaciones aliadas que sirven a las mujeres de la Primera Costa.",
 # Contact
 t_con="Contacto", d_con="Contacta al Jacksonville Women's Leadership Forum.",
 con_h="Contacta a JWLF", con_sub="\u00a1Nos encantar\u00eda saber de ti!",
 con_form_h="Env\u00edanos un mensaje", con_p="Escr\u00edbenos por correo a", con_follow_h="S\u00edguenos",
)

build_lang("es", T)
print("Spanish site done")
