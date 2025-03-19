### 1. Praktilise töö sooritamise käik
**Eesmärk:** Luua ping-pongi laadne mäng kasutades Pygame teeki.
**Lühikirjeldus:** Mängus liigub pall automaatselt ning põrkub seintelt ja aluselt. Alus liigub automaatselt vasakult paremale ning mängija saab punkte, kui pall põrkab aluselt tagasi. Kui pall langeb ekraani alla, kaotab mängija punkti ning pall asetatakse aluse kohale.
**Töötasid üksi või meeskonnas?** Üksi
**Abi saamine/andmine:** Ei kasutanud kaasõppijate abi ega andnud abi teistele. leitsin asjad pygame originaalsel lehelt

### 2. Esinenud probleemid ja nende lahenduskäik
- **Probleem:** Pygame ei leidnud pilte (`FileNotFoundError`).
  - **Lahendus:** Muutsin failiteed `img/ball.png` ja `img/pad.png`, et need vastaksid tegelikule kaustastruktuurile.
- **Probleem:** Pall kukkus mõnikord aluse alt läbi.
  - **Lahendus:** Lisatud tingimus `ball_speed_y > 0`, et pall ei muudaks suunda, kui ta juba liigub ülespoole.
- **Probleem:** Pall ei liikunud alati aluse poole peale kukkumist.
  - **Lahendus:** Pall paigutatakse nüüd aluse kohale ning talle antakse uus suvaline horisontaalne liikumissuund.

### 3. Testimine
**Testimismeetod:** Manuaalne testimine.
**Tulemused:**
- Kontrolliti, et pall põrkuks õigesti seintelt ja aluselt.
- Kontrolliti, et skoor suureneks õigesti peale aluse puudutamist.
- Kontrolliti, et skoor väheneks peale palli kukkumist.
- Testitud mängu taaskäivitamist pärast palli kukkumist.
- Kõik funktsioonid töötasid ootuspäraselt.

### 4. Eneseanalüüs
**4.1. Kuidas sul läks?**
Mängu loomine läks sujuvalt, kuid esines mõned probleemid pildi laadimise ja palli liikumise loogikaga. Need sai lahendatud katsetamise ja paranduste abil.

**4.2. Kas avastasid uusi Python'i tehnikaid või lähenemisi?**
Jah, sain paremini aru, kuidas `pygame.Rect.colliderect()` töötab ning kuidas kasutada `pygame.image.load()` funktsiooni, et laadida ja skaleerida pilte.

**4.3. Enesehinnang (2–5):** 4
Ülesanne sai lahendatud korrektselt ja vastab ootustele, kuid oleksin võinud lisada rohkem kasutaja kontrolli (nt nooleklahvidega aluse juhtimise võimaluse).

**4.4. Mida teeksid järgmisel korral teisiti?**
- Lisaksin kasutajale võimaluse juhtida alust.
- Teeksin mängu keerulisemaks, lisades kiireneva palli või takistusi.
- Lisaksin heliefektid palli põrkumisele, et muuta mäng interaktiivsemaks.

