# Local image path (relative to site root)  ->  source URL on the live site.
# Used to generate images-manifest.md and download-images.sh.
W = "https://www.jwlf.org/wp-content/uploads"

IMAGES = {
    "images/jwlf-logo.png": f"{W}/2017/02/jwlf-logo.png",

    # ---- Home / general event photography ----
    "images/photos/hero.jpg":                 f"{W}/2026/07/JWLF-2026253-scaled.jpg",
    "images/photos/hero-panel.jpg":           f"{W}/2018/06/panel-JWFL-2018-7921_preview.jpeg",
    "images/photos/hero-networking.jpg":      f"{W}/2018/06/young-JWFL-2018-7964_preview.jpeg",
    "images/photos/about-1.jpg":              f"{W}/2026/07/JWLF-2026395-Copy-scaled.jpg",
    "images/photos/about-2.jpg":              f"{W}/2026/07/Womens-Leadership-Forum-2025-09018-2-scaled.jpg",
    "images/photos/about-3.jpg":              f"{W}/2026/07/JWLF-2026337-scaled.jpg",
    "images/photos/sponsor-1.jpg":            f"{W}/2026/07/JWLF-2026212-scaled.jpg",
    "images/photos/sponsor-2.jpg":            f"{W}/2026/07/JWLF-2026278-scaled.jpg",
    "images/photos/sponsor-3.jpg":            f"{W}/2026/07/Womens-Leadership-Forum-2025-08986-scaled.jpg",
    "images/photos/sponsor-events.jpg":       f"{W}/2016/08/2015-events2-300x173.jpg",
    "images/photos/forum-2016.jpg":           f"{W}/2017/03/JWFL-2016-0127-1024x683.jpg",


    # ---- Blog article images ----
    "images/photos/blog-communication.jpg":     f"{W}/2025/06/Untitled-design-3.jpg",
    "images/photos/blog-executive-presence.jpg":f"{W}/2025/06/Blue-And-White-Modern-Confident-Woman-scaled.jpg",
    "images/photos/blog-mentoring.png":         f"{W}/2025/06/Mentoring-blog-scaled.png",
    "images/photos/blog-sponsorship.png":       f"{W}/2025/06/Untitled-design-2-scaled.png",
    "images/photos/blog-ally.jpg":              f"{W}/2019/02/StockSnap_MHRU2KPXWR.jpg",
    "images/photos/blog-hope.jpg":              f"{W}/2019/01/Libby-Gill.jpeg",

    # ---- Officers & board headshots ----
    "images/people/cari-smith.jpg":       f"{W}/2024/01/Cari-Smith.jpeg",
    "images/people/katie-mountain.jpg":   f"{W}/2025/01/K_Mountain_LNSTR-EVP-2021-scaled.jpg",
    "images/people/lisa-jennings.jpg":    f"{W}/2025/06/Jisa-Jennings-headshot-0Y5A4376-scaled.jpg",
    "images/people/landie-brooks.jpg":    f"{W}/2024/01/Landie-Brooks.jpeg",
    "images/people/laura-davis.jpg":      f"{W}/2023/02/Laura-Davis-headshot-r-scaled.jpg",
    "images/people/jennifer-mansfield.jpg": f"{W}/2019/06/Mansfield_Jennifer_300.jpg",
    "images/people/cory-seay.jpg":        f"{W}/2026/07/Cory-Seay-headshot-200x320-1.jpg",
    "images/people/diane-williams.jpg":   f"{W}/2019/06/DRW-Head-shot.jpg",
    "images/people/chelsea-carroll.jpg":  f"{W}/2021/02/chelsea-scaled.jpg",
    "images/people/vicki-harris.png":     f"{W}/2023/01/Vicki_headshot.png",
    "images/people/janie-smalley.jpg":    f"{W}/2024/10/Janie-Smalley.jpg",
    "images/people/sheri-clark.jpg":      f"{W}/2025/06/SClark-1.jpg",
    "images/people/cindy-rose.jpg":       f"{W}/2023/01/Rose_Cindy-2022a-1-scaled.jpg",

    # ---- 2026 speakers & panelists ----
    "images/people/janean-armstrong.jpg": f"{W}/2026/03/Janean-Headshot-scaled-e1774476494398-400x379.jpeg",
    "images/people/amelia-rose-earhart.jpg": f"{W}/2026/03/Amelias-Headshot-scaled.jpeg",
    "images/people/michael-burns.jpg":    f"{W}/2026/04/Mike-Burns-5881-e1775595780868.jpg",
    "images/people/terri-lewis.jpg":      f"{W}/2026/03/Landstar_ExecBoard_TerriLewis_72-1-scaled-e1774449472296.jpg",
    "images/people/ted-phillips.jpg":     f"{W}/2023/04/Ted-Phillips-web.jpg",
    "images/people/taryn-swietek.jpg":    f"{W}/2026/03/headshot22-1.jpg",

    # ---- Previous featured speakers ----
    "images/people/becky-blalock.jpg":    f"{W}/2025/04/Becky-Blalock-150x150.jpg",
    "images/people/rashmi-airan.jpg":     f"{W}/2025/04/Rashmi-Full-Shot-150x150.jpg",
    "images/people/rhonda-snipe.png":     f"{W}/2025/04/Rhonda-Snipe-Headshot-150x150.png",
    "images/people/heather-mcgowan.jpg":  f"{W}/2024/03/McGowan_Heather_PROMOPIC-150x150.jpg",
    "images/people/stephanie-oconnor.jpg":f"{W}/2024/03/Stephanie-OConnor-Headshot-2-150x150.jpg",
    "images/people/amanda-slavin.jpg":    f"{W}/2023/03/Amanda-Slavin-Main-Headshot-1024x731.jpg",
    "images/people/dana-barrett.png":     f"{W}/2023/03/Headhshot-DanaBarrett-e1774479661792-150x150.png",
    "images/people/sukhinder-singh-cassidy.jpg": f"{W}/2022/02/Joyus-Sukhinder-118-C-scaled.jpeg",
    "images/people/brenda-reynolds.jpg":  f"{W}/2022/02/BrendaReynolds_7730Eprt-1-150x150.jpg",
    "images/people/brigid-schulte.jpg":   f"{W}/2020/02/Brigid-Schulte-150x150.jpg",
    "images/people/nadia-bilchik.jpg":    f"{W}/2020/02/nadia_bilchik_red_portrait-150x150.jpg",
    "images/people/libby-gill.jpg":       f"{W}/2019/02/LIBBY-ABOUT-1-e1580762660147-110x150.jpg",
    "images/people/tammy-heermann.jpg":   f"{W}/2019/02/tammy-herman-e1580761294895-150x150.jpg",
    "images/people/leigh-thompson.jpg":   f"{W}/2018/03/Thompson_Leigh_101716-150x150.jpg",
    "images/people/jan-hargrave.jpg":     f"{W}/2017/04/Jan-Hargrave-1-150x150.jpg",
    "images/people/corinne-costa-davis.jpg": f"{W}/2018/03/Corinne-Costa-Davis-150x150.jpg",
    "images/people/tracy-alloway.jpg":    f"{W}/2017/04/download-1-150x150.jpg",
    "images/people/helen-fisher.jpg":     f"{W}/2017/04/drfishers-150x150.jpg",
    "images/people/tiffany-dufu.jpg":     f"{W}/2017/04/kh645mmc-150x150.jpg",
    "images/people/fawn-germer.png":      f"{W}/2017/04/FawnGermer-150x150.png",
    "images/people/betsy-myers.jpg":      f"{W}/2017/04/e77a5e5a8f8d1c97dfb8d2cb773d391b-150x150.jpeg",
    "images/people/pegine-echevarria.jpg":f"{W}/2017/04/ALP_PE_0032.Biz_.Headshot.3-150x150.jpg",
    "images/people/susan-packard.jpg":    f"{W}/2017/04/MG_4239-copy-150x150.jpeg",
    "images/people/pat-baxter.jpg":       f"{W}/2017/04/headshot-300x245-1-150x150.jpg",
    "images/people/sandra-yancey.jpg":    f"{W}/2017/04/Sandra-Yancey-150x150.jpg",
    "images/people/lois-frankel.jpg":     f"{W}/2017/04/Dr.-Lois-Frankel-1-1-150x150.jpg",
    "images/people/sylvia-ann-hewlett.jpg": f"{W}/2017/04/Sylvia_Hewlett_April_2011_cropped-150x150.jpg",

    # ---- Sponsor logos (deduped set used on Home + Sponsorship) ----
    "images/sponsors/mode.png":           f"{W}/2020/02/MODE_Logo_mechanical_RGB_large.png",
    "images/sponsors/ww.jpg":             f"{W}/2022/02/ww-social2.jpg",
    "images/sponsors/sponsor-0.png":      f"{W}/2019/02/0.png",
    "images/sponsors/regency-centers.jpg":f"{W}/2016/08/REGENCY-CENTERS.jpg",
    "images/sponsors/mayo-clinic.png":    f"{W}/2016/08/MAYO-CLINIC.png",
    "images/sponsors/landstar.jpg":       f"{W}/2016/08/LANDSTAR.jpg",
    "images/sponsors/kpmg.jpg":           f"{W}/2016/08/KPMG.jpg",
    "images/sponsors/jea.jpg":            f"{W}/2016/08/JEA.jpg",
    "images/sponsors/jaguars.jpg":        f"{W}/2016/08/JAGUARS.jpg",
    "images/sponsors/holland-knight.jpg": f"{W}/2016/08/HOLLAND-AND-KNIGHT.jpg",
    "images/sponsors/tea.jpg":            f"{W}/2020/02/TEA-Main-Logo-JPEG.jpg",
    "images/sponsors/csx.jpg":            f"{W}/2016/08/CSX.jpg",
    "images/sponsors/black-knight.png":   f"{W}/2016/08/BLACK-KNIGHT.png",
    "images/sponsors/adecco.png":         f"{W}/2016/08/ADECO.png",
    "images/sponsors/acosta.png":         f"{W}/2020/02/Acosta_only_1797_logo_RGB-2-1.png",
    "images/sponsors/sponsor-0-1.png":    f"{W}/2019/02/0-1.png",
    "images/sponsors/deutsche-bank.jpg":  f"{W}/2020/02/logotype_deutsche_bank_stacked_alignment_above_40mm_cmyk.jpg",
    "images/sponsors/50th-gold.png":      f"{W}/2020/02/50thGOLD.png",
    "images/sponsors/maximus.png":        f"{W}/2020/02/MAXIMUS_Box_Logo.png",
    "images/sponsors/wells-fargo.png":    f"{W}/2019/02/2000px-Wells_Fargo_Bank.svg.png",
    "images/sponsors/baptist-health.jpg": f"{W}/2017/11/Baptist-Health.jpg",
    "images/sponsors/iem.png":            f"{W}/2025/03/IEM-Logo-Red-RGB.png",
    "images/sponsors/vystar.jpg":         f"{W}/2019/02/VyStar_r-281blue-600dpi-1024-x-350.jpg",
    "images/sponsors/fields-auto-group.jpg": f"{W}/2020/02/fields-auto-group_logo.jpg",
    "images/sponsors/sponsor-embedded.png": f"{W}/2024/04/EmbeddedImage.png",
    "images/sponsors/sponsor-video-poster.png": f"{W}/2019/03/video-poster.png",

    # ---- Non-profit partner logos ----
    "images/partners/hubbard-house.png":      f"{W}/2026/04/Untitled-design-2.png",
    "images/partners/wib-unf.png":            f"{W}/2025/04/WIB-UNF-logo-150x150.png",
    "images/partners/stem-goes-red.jpg":      f"{W}/2024/04/Go-Red-STEM-logo-1-pdf-232x300.jpg",
    "images/partners/stem2hub.png":           f"{W}/2023/01/NE-FL-Regional-STEM2Hub-logo-300x102.png",
    "images/partners/women-veterans.png":     f"{W}/2020/02/Logo-300x153.png",
    "images/partners/girl-scouts-gateway.jpg":f"{W}/2019/02/GS_GATEWAY_servicemark-300x147.jpg",
    "images/partners/donna-foundation.png":   f"{W}/2018/03/0f884c16-fc77-4aa1-8684-309e1acca4f4-300x166.png",
    "images/partners/habijax.jpg":            f"{W}/2017/09/Habijax-logo-150x150.jpeg",
    "images/partners/community-connections.jpg": f"{W}/2017/09/Community-Connections-Logo-1-150x150.jpg",
    "images/partners/pace.jpg":               f"{W}/2017/09/PACE_Logo-150x150.jpg",
    "images/partners/aha.png":                f"{W}/2017/09/AHS-logo-150x150.png",
    "images/partners/girls-on-the-run.jpg":   f"{W}/2017/09/Girls-on-the-run-Logo-150x150.jpg",
    "images/partners/rethreaded.jpg":         f"{W}/2017/09/REthreaded-logo-150x150.jpg",
    "images/partners/dbwpc.jpg":              f"{W}/2023/04/Primary-DBWPC-Logo-300x133.jpg",
}

# ---- Photo gallery, by year (full-size URLs; local name derived) ----
def _y(year, folder, names, prefix="", suffix="-scaled.jpg"):
    return [(year, f"{W}/{folder}/{prefix}{n}{suffix}") for n in names]

GALLERY = []
GALLERY += _y("2026", "2026/07", ["JWLF-2026253","JWLF-2026251","JWLF-2026270","JWLF-2026278","JWLF-2026294",
    "JWLF-2026152","JWLF-2026166","JWLF-2026337","JWLF-202611","JWLF-2026168","JWLF-2026171","JWLF-202614",
    "JWLF-2026174","JWLF-202641","JWLF-2026183","JWLF-202643","JWLF-202667","JWLF-2026212","JWLF-2026215","JWLF-202686"])
GALLERY += _y("2025", "2026/07", ["09018","09217","08959","01181","01164","01192","09299","09253","09239",
    "08986","09265","09046","01248","01229","09063"], prefix="Womens-Leadership-Forum-2025-")
GALLERY += _y("2024", "2024/10", ["jw-2024-222","jw-2024-541","jw-2024-535","jw-2024-533","jw-2024-522","jw-2024-511",
    "jw-2024-506","jw-2024-499","jw-2024-483","jw-2024-471","jw-2024-469","jw-2024-456","jw-2024-433","jw-2024-424",
    "jw-2024-403","jw-2024-325","jw-2024-312","jw-2024-303","jw-2024-292","jw-2024-285","jw-2024-267","jw-2024-239",
    "jw-2024-200","jw-2024-194","jw-2024-190","jw-2024-152","jw-2024-128","jw-2024-125","jw-2024-103","jw-2024-092",
    "jw-2024-028-1","jw-2024-021","jw-2024-007"])
GALLERY += _y("2022", "2025/01", ["womansforum-046","womansforum-070","womansforum-064","womansforum-063",
    "womansforum-036","womansforum-095","womansforum-100","womansforum-009"])
GALLERY += _y("2019", "2019/04", ["w2XA8xsk-1","RPNqogXY","azOyBLQ0-1","kkxj9ch0","rxOkjfxQ-1","EVQdLoxw-1",
    "UHPUa9yg-1","e5KvweYg-1","9Df4pRpI","tHZjug3o-1","5NwO7abQ-2","avT_wxto-1","odaETKCA","JetxruvA-1","PH3LYSig",
    "qnxfj7rE-2","6nSAWKDE","pUDHVRVI-1","tHksmlU-1","y3Fkr_Ms-1","dAs6q0gY","6lUkQDtw-2","7JQ11-z0","LqQ3hjp0-2",
    "jEc98NJ0-1","OM9Cq8Jg","j8PZhsMQ"], suffix=".jpg")
GALLERY += _y("2018", "2018/07", ["JWFL-2018-5568","JWFL-2018-5610","JWFL-2018-5667","JWFL-2018-5682","JWFL-2018-5687",
    "JWFL-2018-5690","JWFL-2018-5702","JWFL-2018-5689","JWFL-2018-5754","JWFL-2018-5768","JWFL-2018-5788",
    "JWFL-2018-5874","JWFL-2018-5792","JWFL-2018-5832","JWFL-2018-5840","JWFL-2018-7803","JWFL-2018-7834",
    "JWFL-2018-7849","JWFL-2018-7850","JWFL-2018-7851","JWFL-2018-7852","JWFL-2018-7882","JWFL-2018-7912",
    "JWFL-2018-7907","JWFL-2018-7914","JWFL-2018-7968","JWFL-2018-7964","JWFL-2018-8009","JWFL-2018-8011"], suffix=".jpg")
GALLERY += _y("2017", "2017/09", ["JWLF-6441","JWLF-6445"], suffix=".jpg")
GALLERY += _y("2017", "2017/10", ["JWLF-6452","JWLF-6459-1","JWLF-6475-1","JWLF-6514-1","JWLF-6538-1","JWLF-6546-1",
    "JWLF-6533-1","JWLF-6482"], suffix=".jpg")
GALLERY += _y("2016", "2017/10", ["JWFL-2016-0166","JWFL-2016-0156","JWFL-2016-0176","JWFL-2016-0172","JWFL-2016-0192",
    "JWFL-2016-0201","JWFL-2016-0212","JWFL-2016-0254","JWFL-2016-0293","JWFL-2016-0182"], suffix=".jpg")
GALLERY += _y("2015", "2017/10", ["JWLF-0502","JWLF-0450","JWLF-7554","JWLF-0718","JWLF-0679","JWLF-0186",
    "JWLF-0126","JWLF-0110","JWLF-0165","JWLF-0150"], suffix=".jpg")
GALLERY += _y("2014", "2017/10", ["JWLF2014__0126","JWLF2014__0116","JWLF2014__0130","JWLF2014__0223","JWLF2014__0140",
    "JWLF2014__0138","JWLF2014__0182","JWLF2014__0199","JWLF2014__0187","JWLF2014__0208"], suffix=".jpg")
GALLERY += _y("2013", "2017/10", ["DSC_2238","DSC_2168","DSC_2231","DSC_2166","DSC_2206","DSC_2222","DSC_2229",
    "DSC_2221"], suffix=".jpg")
GALLERY += _y("2012", "2017/10", ["P1100018","P1100023","P1100075","P1100027","P1100129","P1090986","P1100024",
    "IMG_2505","P1100181","P1100186"], suffix=".jpg")

def gallery_local(year, url):
    base = url.rsplit("/", 1)[-1]
    return f"images/gallery/{year}-{base}"

for year, url in GALLERY:
    IMAGES[gallery_local(year, url)] = url
