from pathlib import Path
import html as H

ROOT = Path("/data/cache/scratch/fc-repo")

CSS = """
:root{--cream:#F7F4ED;--paper:#FEFDF9;--wine:#6E1728;--wine-dark:#5A1220;--ink:#281D19;
--ink-soft:#4A3B37;--line:#E4DCD2;--rose:#E9C9C1;--sand:#8A6A52}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);
font-family:"Plus Jakarta Sans",system-ui,-apple-system,sans-serif;line-height:1.65;
-webkit-font-smoothing:antialiased}
.wrap{max-width:820px;margin:0 auto;padding:0 24px}
header.top{border-bottom:1px solid var(--line);background:var(--cream)}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;height:72px}
header.top a.brand{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--wine);
font-weight:700;letter-spacing:.02em}
header.top img{height:34px;width:auto}
header.top nav a{color:var(--ink-soft);text-decoration:none;font-size:14.5px;margin-left:22px}
header.top nav a:hover{color:var(--wine)}
.hero{padding:64px 0 8px}
.kicker{font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--sand);margin:0 0 14px}
h1{font-family:"DM Serif Display",Georgia,serif;font-weight:400;
font-size:clamp(30px,4.6vw,46px);line-height:1.12;color:var(--wine);margin:0 0 18px;letter-spacing:-.01em}
.lead{font-size:18px;color:var(--ink-soft);margin:0 0 34px}
h2{font-family:"DM Serif Display",Georgia,serif;font-weight:400;
font-size:clamp(23px,3vw,30px);line-height:1.2;color:var(--wine);margin:46px 0 14px}
h3{font-size:17px;margin:26px 0 8px;color:var(--ink)}
p{margin:0 0 16px}
ul{margin:0 0 18px;padding-left:20px}
li{margin:0 0 9px}
a{color:var(--wine)}
.cta{margin:48px 0;padding:28px 26px;background:var(--cream);border-left:3px solid var(--wine);border-radius:2px}
.cta p{margin:0 0 14px;font-size:16.5px}
.btn{display:inline-block;background:var(--wine);color:#fff;text-decoration:none;
padding:13px 24px;border-radius:999px;font-weight:600;font-size:15px}
.faq{margin:52px 0 10px}
.faq details{border-top:1px solid var(--line);padding:16px 0}
.faq summary{cursor:pointer;font-weight:600;list-style:none}
.faq p{margin:10px 0 0;color:var(--ink-soft);font-size:15.5px}
footer{border-top:1px solid var(--line);margin-top:60px;padding:28px 0 40px;
font-size:13.5px;color:var(--ink-soft)}
footer a{color:var(--wine);text-decoration:none}
"""

def page(slug, title, desc, kicker, h1, intro_html, body_html, faq, related):
    faq_html = "".join(
        f'<details><summary>{H.escape(q)}</summary><p>{H.escape(a)}</p></details>'
        for q, a in faq
    )
    rel = "".join(f'<li><a href="{u}">{t}</a></li>' for t, u in related)
    doc = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://fameconnect.fr/{slug}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="FameConnect">
<meta property="og:locale" content="fr_FR">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://fameconnect.fr/{slug}">
<meta property="og:image" content="https://fameconnect.fr/assets/og-fameconnect.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/icon-192.webp" type="image/webp">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=DM+Serif+Display&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="/"><img src="assets/logo-fameco.webp" alt="FameConnect" width="34" height="34">FameConnect</a>
  <nav><a href="/">Accueil</a><a href="/#liste">Liste d'attente</a></nav>
</div></header>
<main class="wrap">
  <div class="hero">
    <p class="kicker">{kicker}</p>
    <h1>{h1}</h1>
    <p class="lead">{intro_html}</p>
  </div>
  {body_html}
  <div class="cta">
    <p><strong>FameConnect arrive bientôt en Provence.</strong> Inscrivez-vous en avant-première pour découvrir les expériences près de chez vous dès l'ouverture.</p>
    <a class="btn" href="/#liste">Rejoindre la liste d'attente</a>
  </div>
  <div class="faq">
    <h2>Questions fréquentes</h2>
    {faq_html}
  </div>
  <h2>À lire aussi</h2>
  <ul>{rel}</ul>
</main>
<footer><div class="wrap">
  <p>© 2026 FameConnect — <a href="/">fameconnect.fr</a> · Expériences entre femmes en Provence</p>
</div></footer>
</body>
</html>"""
    (ROOT / slug).write_text(doc, encoding="utf-8")
    return slug

# ---------- 1. Ateliers créatifs à Avignon ----------
p1 = page(
    "ateliers-creatifs-avignon.html",
    "Ateliers créatifs à Avignon : céramique, couture, peinture | FameConnect",
    "Où trouver un atelier créatif à Avignon, comment choisir, à quoi s'attendre. Le guide des ateliers entre femmes en Vaucluse, par FameConnect.",
    "Guide · Avignon & Vaucluse",
    "Ateliers créatifs à Avignon : par où commencer",
    "Céramique, couture, peinture, fleurs séchées, cuisine : Avignon regorge d'ateliers où l'on repart avec une pièce faite de ses mains. Encore faut-il savoir lequel choisir — et oser y aller seule.",
    """<h2>Pourquoi les ateliers créatifs ont la cote à Avignon</h2>
<p>La ville a un tissu d'artisans et d'ateliers dense, hérité de son histoire de cité papale et de son marché. Résultat : on trouve, dans un rayon de quinze minutes à pied, aussi bien un tour de potier qu'un cours de broderie ou un atelier de sérigraphie.</p>
<p>Ce qui a changé ces dernières années, c'est la façon de les pratiquer. On n'y va plus seulement pour apprendre une technique : on y va pour <strong>passer un moment</strong>. Un atelier de deux heures, dans un petit groupe, avec un verre et de la musique, est devenu une sortie en soi — souvent plus simple à organiser qu'un restaurant.</p>

<h2>Les grandes familles d'ateliers</h2>
<ul>
  <li><strong>La céramique et le modelage</strong> — la plus demandée. On touche la terre, on repart avec un bol ou un vase après cuisson. Prévoyez deux passages : un pour façonner, un pour récupérer la pièce émaillée.</li>
  <li><strong>La couture et le textile</strong> — du point de croix à la confection d'une pièce simple. Souvent proposé sous forme de cycles, plus rarement en séance unique.</li>
  <li><strong>La peinture et le dessin</strong> — aquarelle, gouache, croquis d'après nature. Le format « atelier apéro » y est fréquent.</li>
  <li><strong>Les fleurs et le végétal</strong> — bouquets de saison, couronnes, compositions séchées. Facile à offrir, facile à ramener chez soi.</li>
  <li><strong>La cuisine et la pâtisserie</strong> — ateliers courts, très conviviaux, souvent autour du marché des Halles.</li>
</ul>

<h2>Comment choisir son atelier</h2>
<p>Trois critères comptent plus que le reste. D'abord <strong>la taille du groupe</strong> : au-delà de huit personnes, on ne touche presque plus le matériel. Ensuite <strong>le matériel fourni</strong> : un atelier sérieux prête tout, y compris le tablier. Enfin <strong>ce qu'on emporte</strong> : une pièce finie vaut mieux qu'une photo de son propre travail en cours.</p>
<p>Un détail qu'on oublie souvent : demandez si la cuisson ou la finition est incluse. Sur la céramique notamment, certaines formules facturent la cuisson à part, ce qui change le budget réel.</p>

<h2>Y aller seule, ou pas</h2>
<p>C'est la vraie question. Beaucoup de femmes renoncent à un atelier non par manque d'envie, mais parce qu'elles n'ont personne avec qui y aller. Or les ateliers sont justement l'un des rares endroits où venir seule ne se voit pas : tout le monde a les mains occupées, et la conversation se fait d'elle-même autour de la table.</p>
<p>C'est exactement ce que FameConnect veut rendre plus simple : trouver l'expérience, réserver, et savoir qui d'autre y va.</p>""",
    [("Faut-il un niveau pour participer à un atelier créatif ?",
      "Non. La très grande majorité des ateliers avignonnais sont ouverts aux débutants, et le matériel est fourni. Les formules en cycle sont en revanche pensées pour progresser."),
     ("Combien de temps dure un atelier ?",
      "De deux heures pour une initiation à une demi-journée pour un atelier complet. La céramique demande souvent un second passage pour récupérer la pièce après cuisson."),
     ("Peut-on venir seul à un atelier ?",
      "Oui, et c'est très courant. Les groupes sont petits et l'activité crée naturellement la conversation.")],
    [("Expériences et sorties entre femmes à Avignon", "experiences-entre-femmes-avignon.html"),
     ("Que faire dans les Alpilles et le Luberon", "activites-alpilles-luberon.html")],
)

# ---------- 2. Expériences entre femmes à Avignon ----------
p2 = page(
    "experiences-entre-femmes-avignon.html",
    "Expériences et sorties entre femmes à Avignon | FameConnect",
    "Idées de sorties et d'expériences entre femmes à Avignon : ateliers, yoga, brunchs, balades. Le guide FameConnect pour ne plus y aller seule.",
    "Guide · Avignon",
    "Sortir entre femmes à Avignon : les vraies options",
    "Trouver une activité, c'est facile à Avignon. Trouver avec qui la vivre, c'est autre chose. Voici les formats qui fonctionnent vraiment, et comment s'y prendre.",
    """<h2>Le vrai frein n'est pas l'offre</h2>
<p>Avignon compte des dizaines d'ateliers, de studios et de lieux où faire quelque chose. Le problème n'est donc presque jamais de trouver une idée — c'est de la concrétiser. Un samedi après-midi se perd souvent entre les onglets ouverts et les messages restés sans réponse.</p>
<p>Trois causes reviennent : on ne sait pas à qui proposer, on craint d'arriver dans un groupe déjà formé, et on repousse jusqu'à ce que la date passe.</p>

<h2>Les formats qui marchent</h2>
<h3>Les ateliers courts, en petit groupe</h3>
<p>Deux heures, six à huit personnes, une pièce à ramener. C'est le format le plus accessible quand on vient seule : personne ne se connaît, l'activité donne un sujet de conversation, et il n'y a pas de moment gênant.</p>

<h3>Le yoga et le pilates en plein air</h3>
<p>Dès les beaux jours, les séances dehors se multiplient — sur les bords du Rhône, à la Barthelasse, ou dans les parcs de la ville. L'avantage : on peut venir seule sans que cela se remarque, et les groupes ont l'habitude d'accueillir de nouvelles personnes.</p>

<h3>Les brunchs et les apéros à thème</h3>
<p>Plus simples à organiser qu'un dîner, moins engageants qu'un week-end. Le brunch du dimanche reste le format le plus facile pour une première rencontre.</p>

<h3>Les balades et les sorties nature</h3>
<p>Le Rocher des Doms, les remparts, l'île de la Barthelasse : la ville se parcourt à pied, et une marche partagée vaut souvent mieux qu'un premier rendez-vous en face à face.</p>

<h2>Comment se lancer sans y passer la journée</h2>
<ul>
  <li>Choisissez <strong>une seule</strong> activité et une date précise — pas « un de ces jours ».</li>
  <li>Privilégiez les formats où l'on est <strong>assis côte à côte</strong> plutôt que face à face.</li>
  <li>Proposez à deux personnes maximum : au-delà, l'organisation devient un projet.</li>
  <li>Réservez à l'avance : c'est ce qui transforme une intention en sortie.</li>
</ul>

<h2>Ce que FameConnect change</h2>
<p>L'application réunira au même endroit les expériences de la région, la réservation, et la possibilité de voir qui participe — pour ne plus jamais renoncer à une sortie faute de compagnie.</p>""",
    [("Comment rencontrer d'autres femmes à Avignon ?",
      "Les ateliers en petit groupe et les activités régulières (yoga, danse, randonnée) sont les contextes les plus simples : l'activité crée la conversation sans avoir à la provoquer."),
     ("Quelles activités faire un dimanche à Avignon ?",
      "Un brunch, une balade sur les remparts ou à la Barthelasse, une exposition. Les ateliers sont plus rares le dimanche, mieux vaut vérifier les horaires."),
     ("Est-il gênant de venir seule à une activité ?",
      "Non, c'est très fréquent et les groupes sont habitués. C'est souvent plus simple que d'arriver à deux dans un groupe déjà constitué.")],
    [("Ateliers créatifs à Avignon", "ateliers-creatifs-avignon.html"),
     ("Que faire dans les Alpilles et le Luberon", "activites-alpilles-luberon.html")],
)

# ---------- 3. Alpilles & Luberon ----------
p3 = page(
    "activites-alpilles-luberon.html",
    "Que faire dans les Alpilles et le Luberon : activités et ateliers | FameConnect",
    "Idées d'activités dans les Alpilles et le Luberon : villages, ateliers d'artisans, balades, expériences à partager. Le guide FameConnect en Provence.",
    "Guide · Alpilles & Luberon",
    "Que faire dans les Alpilles et le Luberon",
    "Deux massifs, une vingtaine de villages, et beaucoup plus d'options qu'on ne le croit quand on cherche une activité à faire à plusieurs.",
    """<h2>Deux territoires, deux rythmes</h2>
<p>Les Alpilles, au sud d'Avignon, sont une chaîne calcaire de trente kilomètres, ponctuée de villages comme Saint-Rémy-de-Provence ou Les Baux-de-Provence. Le Luberon, plus à l'est, s'étire autour de Gordes, Roussillon et L'Isle-sur-la-Sorgue.</p>
<p>Les deux se parcourent en une journée depuis Avignon. Les Alpilles sont plus minérales, plus sèches, avec des panoramas ouverts. Le Luberon est plus vert, plus agricole, avec des villages perchés et beaucoup d'ateliers d'artisans.</p>

<h2>Les activités qui valent le déplacement</h2>
<h3>Les ateliers d'artisans</h3>
<p>Le Luberon concentre une densité rare de céramistes, de verriers et de peintres installés dans les villages. Beaucoup ouvrent leur atelier au public et proposent des initiations courtes — c'est l'un des meilleurs moyens de repartir avec une pièce qui a une histoire.</p>

<h3>Les marchés</h3>
<p>L'Isle-sur-la-Sorgue est connue pour ses antiquaires et son marché du dimanche. Saint-Rémy a son marché du mercredi, réputé dans toute la région. Un marché est aussi une sortie en soi : on flâne, on goûte, on discute.</p>

<h3>Les balades et les points de vue</h3>
<p>Le sentier des Crêtes à Fontvieille, les carrières des Baux, la route des Crêtes entre La Ciotat et Cassis : il existe des dizaines de boucles de deux à trois heures, accessibles sans équipement particulier.</p>

<h3>Les sites à visiter</h3>
<p>Les Carrières de Lumières aux Baux, l'abbaye de Montmajour, la Fontaine-de-Vaucluse, les ocres de Roussillon. Ces lieux se visitent bien à plusieurs, et se combinent facilement avec un déjeuner sur place.</p>

<h2>Comment organiser une journée</h2>
<ul>
  <li>Partez tôt : les villages perchés sont vite saturés en fin de matinée.</li>
  <li>Réservez les ateliers et les visites à l'avance, surtout le week-end.</li>
  <li>Prévoyez une voiture : les transports en commun desservent mal l'intérieur des massifs.</li>
  <li>Gardez une marge : le charme de la région, c'est aussi de s'arrêter sans avoir prévu.</li>
</ul>

<h2>Et pour ne pas y aller seule</h2>
<p>C'est précisément le sujet de FameConnect : rassembler les expériences de Provence et permettre de voir qui d'autre y participe, pour transformer une belle idée de sortie en dimanche réellement vécu.</p>""",
    [("Combien de temps faut-il pour visiter les Alpilles ?",
      "Une journée suffit pour deux ou trois villages. Deux jours permettent d'ajouter les balades et un atelier sans courir."),
     ("Faut-il une voiture pour visiter le Luberon ?",
      "C'est fortement recommandé. Les villages sont mal desservis par les transports en commun, et les navettes saisonnières restent limitées."),
     ("Quelle est la meilleure période pour visiter ?",
      "Le printemps et le début de l'automne : températures douces, lumière longue et moins de monde qu'en juillet-août.")],
    [("Ateliers créatifs à Avignon", "ateliers-creatifs-avignon.html"),
     ("Expériences et sorties entre femmes à Avignon", "experiences-entre-femmes-avignon.html")],
)

print("pages créées:", p1, p2, p3)
