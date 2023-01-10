**Projet de cryptographie**

*Kireche Brice Laboudi Hocine*

Sommaire

1) *Introduction*
1) *Téléchargement des noms de domaines*
1) *Mise en place du téléchargement des Certificats X509*
1) *Extraction des clé RSA & Vérification des doublons*
1) *Batch GCD sur les clé*
1) *Conclusion*

Tous les liens qui ont pu être utilisés seront présentés en bas de page autant que possible.

Tous les dossiers que nous avons pu récupérer et obtenir dans le cadre de ce projet sont accessibles directement sur le Drive de l’école.

[Projet Crypto](https://etesiea-my.sharepoint.com/:f:/g/personal/kireche_et_esiea_fr/Evbm3qljE69EuoF0vQx-cDcBqRp-lcA6Wkceo-QxBEgqig?e=EJNVFm)

Vous y verrez notre code, le batch GCD utilisé, les certificats mais également les rapports de doublons et notre documentation la plus utile.

1. **Introduction**

L’idée du projet est de retracer une grande quantité de certificats et trouver une possible faille. En effet, tous les certificats( plusieurs centaines de millions) proviennent d’une fonction. Cependant, il arrive que cette fonction utilise un aérateur « Random » peu efficace de ce[label](../../../Downloads/Projet%20de%20cryptographie.pdf) fait la fonction sera totalement aléatoire. Cela aura pour effet de trouver un multiple commun lorsque l’on retracera un certain nombre de possibilités. Une fois ce multiple trouvé, il sera nécessaire de sauvegarder son nom de domaine auquel est rattaché sa clé puis son certificat comme nous le verrons dans les 2 prochains points de ce rapport.

C’est donc la raison pour laquelle, nous nous sommes dans un premier temps attelé à la recherche des noms de domaine directement lié aux certificats et ceux dont la quantité est la plus importante.

2. **Téléchargement des noms de domaines**

Après de sérieuses recherches nous sommes tombés sur l’outil Certstream open source, libre et facile d’accès.

Une fois les extensions installées nous avons pu télécharger de deux manière différentes, sur un format similaire à celui-ci, à l’aide de la commande Certstream dans le terminal.

[10/03/22 14:24:59] accountants-wales.co.uk (SAN: ) [10/03/22 14:24:59] \*.prbuild.surakota.people.aws.dev (SAN: )

Mais il n’était pas très judicieux de le mettre dans ce sens. Toutefois nous nous sommes rendus compte que les dates n’étaient pas utiles et que nous aurions préférés avoir seulement les noms de domaines pour pouvoir les placer correctement et sans risque dans mon code.

La très pratique commande « certstream --json | jq -r ‘.data.leaf\_cert.all\_domains[]’ » directement écrite dans le terminal nous a permis de récupérer directement les noms de domaines au format Json. Cela nous a donné accès aux noms de domaines suivants (disposés dans un fichier texte) :

healthyfuel24.com erinflorenceart.com [www.erinflorenceart.com](http://www.erinflorenceart.com)

Ci dessous, un screenshots du nombre de ligne attestant donc du nombre de noms de domaines :

![](Aspose.Words.e4b4e689-beba-4ffc-a2e3-aceb3dd60d7f.001.jpeg)

Pour expliquer un peu notre démarche, nous savions que le service de Certstream proposait de télécharger gratuitement 1 million de certificats en 6 heures approximativement (pour notre part). Cependant, plus le nombre de certificats est important, plus la chance de trouver une faille est grande. La base de données de Certstream contient 250 millions de certificats.

Nous avons donc, après coût, trouver un site proposant directement les noms de domaines. Plus de 10 millions noms de domaines en quelques secondes (lien en bas de page) pouvant  même aller jusqu’à 30 millions (non testé)

Mais après réflexion, sur un grand nombre de données, prendre le risque d’avoir des données inexactes peut être compliqué. En effet, avec Certstream, nous sommes sur d’avoir des données à jour et exact, provenant directement des serveurs de Google.

III.**Mise en place du téléchargement des**

**Certificats X509**

Afin de faire fonctionner les codes suivants, nous avons installé les extensions comme le module « Cryptographie » ainsi que « Request » qui nous ont été très utiles, et bien d’autres encore.

A l’aide de Certstream nous sommes parvenus à obtenir les certificats au format Json.

![](Aspose.Words.e4b4e689-beba-4ffc-a2e3-aceb3dd60d7f.002.jpeg)

Données sortant de Certstream

![](Aspose.Words.e4b4e689-beba-4ffc-a2e3-aceb3dd60d7f.003.jpeg)

Le certificat surligné nous avait donné du mal à récupérer et nous avions sollicité votre aide M.Larinier afin de la récupérer. Vous nous aviez aidé sur un bout de code et nous avons finalement eu accès aux informations les plus importantes :

-Le nom de domaine

-Le certificat X509 (As\_Der)

-Et la clé RSA (authorityKeyIdentifier normalement)

En s’appuyant sur un code exemple directement sur le Github Certstream, nous avons construit l’appel de la fonction. (Plus ou moins comme pour les noms de domaines) et avons ensuite appliqué votre code pour récupérer les informations.

Cependant, nous trouvions cette méthode fort efficace mais un peu trop consommatrice![](Aspose.Words.e4b4e689-beba-4ffc-a2e3-aceb3dd60d7f.004.jpeg) sur le plan hardware. Nous avions en parallèle sous les yeux depuis le début le code de Certificat Transparency, qui peut certainement être une très bonne alternative.

Cependant, nous retiendrons une solution efficace, nommée “Core” disponible sur le sharepoint.

Remarque : Tous ces projets ou du tout moins celui ci est capable de se connecter au logs listes de google car il fait appel ou aux librairies Certstream ou Certificates transaprency (qui appartient à google). Et ici, le code allait vite, voir très très vite.

![](Aspose.Words.e4b4e689-beba-4ffc-a2e3-aceb3dd60d7f.005.jpeg)

Nous avons donc opté pour cette solution, nous nous sommes posé la question au début du nom de domaine. En effet, via certificate transparency, nous ne sommes pas arrivé à trouver le moyen en python de générer aussi les noms de domaines. Quel est alors l’intérêt de dénicher une faille dans le certificat si le site est inconnu. Nous avons finalement trouvé un site web (également en description) qui permet de retrouver le site en question à partir du nom de domaine.

Cet ouvrage est un super outil. Très varié et divers.

Nous avons donc obtenu les dossiers directement sur le bureau plutôt que dans le dossier temporaire. 1,3 millions de certificats ont été téléchargés en 30 minutes le tout répertorié dans 40,000 fichiers excel, fusionnés en un seul. Il se présente avec en fichier « csv » avec la clé RSA puis le certificat et le nom de domaine après modification de bon nombre de lignes de code.

Nous voilà en possession de plus d’un million de clés, toutes fournies par Google.

4. **Extraction des clé RSA & Vérification des doublons**

Une fois les clés RSA extraites du fichier csv, nous les avons toutes analysées. Nous avons pris la liberté de faire un code pour les comparer mais forcé de voir qu’EXCEL est un bien meilleur outil, nous avons vérifié les doublons avec ce dernier. Comme nous nous attendions, le dossier était beaucoup trop lourd pour excel à ouvrir en 1 seule fois, nous avons donc découpé le fichier en 4. Ce qui nous donne plus ou moins 400,000 échantillons de clés par fichier.

**Nous avons alors vérifié les certificats x509, étaient tous différents sans exception,** et nous avons eu la confirmation logiciel (excel) qu’aucune similarité ne fut remarquée sur les certificats. Cependant, de nombreux doublons ont apparus dans le code.

nous avons d’ailleur demandé à M.Erra la provenance de ces derniers.

Environ 10% de ses clé sont des doublons.

Sur les memes doublons, les certificats était différent.

Selon nous laisse avec 1,3 Millions de certificats et 1.1/1.2 millions de clé.

Nous sommes arrivés à la conclusion que c’est donc bien la même clé RSA pour bon nombre de ces sites. (Sauf erreur de notre part, le certificat étant différent)

De ce fait, une faille importante serait accessible si nous arrivions à trouver la clé associée (un N ou un Q)

![](Aspose.Words.e4b4e689-beba-4ffc-a2e3-aceb3dd60d7f.006.jpeg)Il est vrai que nous avons plus d’un million de certificats et allons passer le Batch GCD sur tous les certificats différents de notre liste.

![](Aspose.Words.e4b4e689-beba-4ffc-a2e3-aceb3dd60d7f.007.png)

*Voici le total de lignes*

Le but étant de repérer les similarités de ces clés en les divisant par un échantillon prédéterminé et aléatoire.

En effet, le logiciel qui crée ces clés possède une fonction Random peu diverse ou qui peut se répéter dès lors que l’on compare un très grand échantillon de produit donc plus l’échantillon est grand, mieux c’est.

Nous avons donc compté soigneusement le nombre de clés différentes de notre liste, et il en ressort 120,000. Nous pouvons donc passer au Batch GCD au plus vite.

Pour ce projet, nous nous sommes grandement appuyés sur divers documents présents sur internet, ainsi que sur des projets GitHub, dont un Batch GCD codé en C++ d’une qualité, pour moi quasiment parfaite.

Plus de 10 batch ont été évalué et finalement le batch en Python (De fiona) excellent également à été retenu.

Ce sont les sources les plus notables, en description.

5. **Batch GCD sur les clés**

Après de nombreux projets et idées analysé, nous avons finalement jeté notre dévolu sur le Batch GCD de « Fiona » en Python.

En général, les clés RSA sont très difficiles à factoriser : le plus grand module RSA factorisé par les algorithmes standards compte 768 bits (232 chiffres décimaux \_\_ Source wikipédia), et les normes actuelles pour la plupart des services de chiffrement de haut niveau utilisent des modules RSA de 1024 ou 2048 bits. **Cependant, si une grande collection de clés RSA est construite à l'aide de nombres premiers donnés par un générateur de nombres aléatoires défectueux, un nombre significatif de ces clés peut partager des facteurs premiers.**

**L'algorithme batch GCD exploite cette faiblesse dans la génération de clés RSA.**

Supposons que deux clés RSA distinctes N1 et N2 partagent un facteur, c'est-à-dire que d= pgcd(N1,N2)>1 ; alors, puisque Ni=pi\*qi pour primepiandqi, il faut que soit d= Ni  ou d=q1.

Ainsi, si nous constatons que deux clés partagent des facteurs, nous pouvons rapidement factoriser les deux clés en utilisant leur PGCD. Le processus GCD par lots

Étant donné une liste {N1,N2,...,Nm} d'entiers que nous avons soigneusement fabriqué (cf code)

Avant de passer la liste, nous avons donc du créer une liste d’entier, comprise entre 0 et 100 ici, modifiables en fonction du besoin. Cette dernière comprend environ une quinzaine d’éléments. **La seul condition à cette liste est que ces nombres soient premiers bien évidemment**

Remarque:

Au dela d’un certain seul, la probabilité de trouver un PGCD est plus faible selon [wikipédia.](https://fr.wikipedia.org/wiki/Liste_de_nombres_premiers)

[En effet, la proportion des nombres premiers diminue](https://fr.wikipedia.org/wiki/Liste_de_nombres_premiers) avec au dela de 1,000,000

Cependant, prendre les 1000 premiers nombres semble correct pour une approche.

Remarque:

Lors d’une attaque, plus ce nombre est élevé, plus la manipulation sera efficace. Remarque:

On aurait plus facilement calculer le coût d’un programme [avec la command User Time par exemple](https://perso.isima.fr/~lacomme/temps/Temps_de_calcul.pdf)

Remarque :

En cas de nombre très important et de recherche poussé, adapté son code en conséquence aurait probablement été une bonne idée. Changer de language également.

Le python est exactement 86 fois plus lent que le C.

Le javascript est exactement 26 fois plus lent que le C.

La fonction retourn un G ou PGCD

Remarquez que {Ni|Gi>1} est l'ensemble de clés qui partagent un facteur avec une autre clé de la liste. La plupart du temps, Gi est premier et donc un facteur non trivial de Ni. En reconnaissant ces premiers Gi, on peut factoriser les clés Ni correspondantes.

Nous voilà au coeur du projet, et nous allons vous donner notre code pour la Batch GCD qui nous a donné beaucoup de mal !

Ce code vient totalement de nous, et a pour finalité de créer un dossier, que nous pourrons analyser (à également retrouver en annexe)

———————————————————————————————————————

from math import prod, floor, gcd from collections.abc import Sequence

def products(\*integers: int) -> list[list[int]]:

"""Tree with the root as the product, input as leaves and intermediate

states as intermediate nodes"""

xs = list(integers)

result = [xs]

while len(xs) > 1:

xs = [prod(xs[i \* 2: (i + 1) \* 2]) for i in range((len(xs) + 1) // 2)]

//la division en elle meme

result.append(xs)

return result

def batch\_gcd(\*integers: int) -> list[int]:

xs = list(integers)

tree = products(\*xs)

node = tree.pop()

while tree:

xs = tree.pop()

node = [node[floor(i / 2)] % xs[i] \*\* 2 for i in range(len(xs))] //la division en elle meme

res = []

for r, n in zip(node, xs):

res.append("GCD= " + str(gcd(r // n, n)) + ", r = " + str(r) + ", n = " + str(n)) //le résultat

return res counter = 0

result = []

with open("RSAkey.txt") as f:

for line in f:

key = int(line, base=16) result.append(key) counter += 1

if counter == 100:

break

result = batch\_gcd(\*result)

#after\_batch = batch\_gcd(\*result) # send the result for batch gcd

with open("result.txt", "w") as f: for item in result: f.write("%s\n" % item)

\# print(after\_batch) for item in result:

print(item) ———————————————————————————

Et voici son résultat :

![](Aspose.Words.e4b4e689-beba-4ffc-a2e3-aceb3dd60d7f.008.jpeg)Nous avons finalement réussi à créer un fichier txt en écrivant les données de la division entre notre liste et chaque clé. nous avons ensuite comparé les résultats

Nous avons finalement trouvé deux diviseurs communs et donc la faille associé Pour la repérer nous avons évidemment utilisé excel.

Pour générer un module RSAN, nous générons une paire d'étendues premières aléatoires et q satisfaisant quelques conditions techniques (comme pgcd(p−1,q−1)=2), puis nous les multiplions ensemble pour obtenir N.

**Ici nous voyons que le meme Q à été retrouvé![](Aspose.Words.e4b4e689-beba-4ffc-a2e3-aceb3dd60d7f.009.jpeg)**

Tous les N ont été générés en utilisant la méthode ci-dessous

Nous avons dans un premier temps comparé le PGCD et regarder la similarité. Remarque: Certains Batch avaient une fonction pour retrouver un n et q commun

Également, ici, nous ne connaissons que le modulos des nombres trouvés et non les nombres en eux-même.

Cependant, sur une multiplication simple de deux nombres, retrouver le nombre initial à partir du modulo  est possible assez facilement

Alors, ce ce fait, on à dans chaque clé l'équation la plus importante

Remarque : Nous n’avons pas eu l’occasion de savoir lequel P ou Q nous aurions pu trouver.

Selon nous, nous aurions pu très bien trouver un P ou Q, deux P ou deux Q.

**N = P \* Q**

Ici, nous avons trouvé le même PGCD pour 2 éléments (Fichier Last Résult) Le PGCD en question :

25680532640

Dès lors, nous l’avons divisé par un grand N est trouvé les équations ci dessous.

n = 11929413484016950905552721133125564964460656966152763801206748195494305685115033 38063159570377156202973050001186287708466899691128922122454571180605749959895170 80042105263427376322274266393116193517839570773505632231596681121927337473973220 312512599061231322250945506260066557538238517575390621262940383913963![](Aspose.Words.e4b4e689-beba-4ffc-a2e3-aceb3dd60d7f.010.png)

p = 10933766183632575817611517034730668287155799984632223454138745671121273456287670 008290843302875521274970245314593222946129064538358581018615539828479146469

q = 10910616967349110231723734078614922645337060882141748968209834225138976011179993 394299810159736904468554021708289824396553412180514827996444845438176099727![](Aspose.Words.e4b4e689-beba-4ffc-a2e3-aceb3dd60d7f.010.png)![](Aspose.Words.e4b4e689-beba-4ffc-a2e3-aceb3dd60d7f.010.png)

et

p = 57581761151703473066828715575758176115170347306682871557066828715579998463222345413874567112127345628 7670

008290843302875521274970245314593222946129064538358581018615539828479146469

q = 10910616967349110231723734078614922645337060882141748968209834225138976011179993 394299810159736904468554021708289824396553412180514827996444845438176099727![](Aspose.Words.e4b4e689-beba-4ffc-a2e3-aceb3dd60d7f.011.png)

n = 21927337473973220950905552721133125564964460656966152763801206748195494305685115033 38063159570377156202973050001186287708466899691128922122454571180605749959895170 800421052634273763222742663931161935178395707735056322315966811219231251259906123 1322250945506260066557538238517575390621262940383913963![](Aspose.Words.e4b4e689-beba-4ffc-a2e3-aceb3dd60d7f.012.png)

**L’ensemble est un ensemble de modules RSA.**

Dans le monde réel, il y a de fortes chances que certaines personnes aient utilisé des sources aléatoires faibles, mal configurées ou fatalement compromises.

En particulier, certains nombres premiers peuvent apparaître plus d'une fois !

C'est une très mauvaise nouvelle pour la sécurité Internet, mais une bonne nouvelle pour nous, car nous pouvons calculer efficacement ces nombres premiers partagés et casser les clés correspondantes. La raison pour laquelle nous pouvons faire cela est que s'il est difficile de factoriser un nombre, il est facile de détecter des facteurs communs entre n'importe quelle paire de nombres.

6. **Conclusion**

Grâce à toutes ces manipulations nous pouvons affirmer qu’une attaque est possible. Cependant, même si possible, la cible serait aléatoire, parmi les noms de domaines existants. Trouver un n ou q d’une de ses clé serait très utile dans le cas d’une clé multiple..

Faire cela à plus grande échelle serait également une solution. 250 millions de certificats sont présents sur la database dont Certstream à accès. Cependant, cette attaque ne sera résolu que lorsque les fonctions random seront efficaces, produisant une entropie maximum. On pourrait également envisager, si jamais la sécurité venait à manquer, le scindement d’un n ou q de manière à avoir 3 inconnues et multiplier ainsi la difficulté de calcul exponentiellement. N = p\*Q\*Z (Z étant le scindement).

Sur un plan moins technique, je pense que nous avons compris que l’apprentissage en action était plus efficace qu’en suivant seulement un TD. Le cours suivi a toutefois était essentiel dans la compréhension des bases qui nous ont permis de mener à bien ce projet. Nous en retirons des compétences techniques mais aussi une capacité accrue à travailler en équipe et cela nous servira évidemment dans le monde professionnel. Pour finir nous tenions à remercier M.Larinier pour ses cours et sa présence en TP.

**Annexe:**

Sources:

[Projet Crypto](https://etesiea-my.sharepoint.com/:f:/g/personal/kireche_et_esiea_fr/Evbm3qljE69EuoF0vQx-cDcBqRp-lcA6Wkceo-QxBEgqig?e=u5MGda)

[https://github.com/google/certificate-transparency-go ](https://github.com/google/certificate-transparency-go)[https://certstream.calidog.io/ ](https://certstream.calidog.io/)[https://github.com/CaliDog/Axeman ](https://github.com/CaliDog/Axeman)<https://www.di-mgt.com.au/rsa_alg.html>

Batch GCD :

1. En c++[ https://github.com/hfiuza/Euclid-vs-RSA-Cryptanalysis-with-batch-GCDs](https://github.com/hfiuza/Euclid-vs-RSA-Cryptanalysis-with-batch-GCDs)
1. <https://github.com/fionn/batch-gcd>
1. <https://github.com/ForeverAnApple/Tetanus>
1. <https://github.com/dieggoluis/rsa-attack>
1. <https://github.com/therealmik/batchgcd>

![](Aspose.Words.e4b4e689-beba-4ffc-a2e3-aceb3dd60d7f.013.jpeg)
