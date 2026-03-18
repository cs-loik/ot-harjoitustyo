# Vaatimusmäärittely

## Sovelluksen tarkoitus

ValmistuJo on opintojen seurantasovellus. Voit tallentaa opintosuunnitelman, merkitä edistymistä ja seurata opintojen tilannetta. Sovellusta voi käyttää useampi käyttäjä, joilla kaikilla on pääsy omiin opintotietoihinsa.

## Käyttäjät

Sovelluksella on normaalikäyttäjiä. Jatkossa voi olla, että lisätään pääkäyttäjiä.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- käyttäjä voi luoda käyttäjätunnuksen
    - käyttäjätunnus on suojattu salasanalla
- käyttäjä voi kirjautua sisään
    - käyttäjätunnus vahvistetaan salasanalla
    - jos salasana on väärin, tästä huomautetaan

### Kirjautumisen jälkeen

- käyttäjä voi syöttää opintokokonaisuuksia käsin
    - kokonaisuudesta syötetään nimi, minimilaajuus
- käyttäjä voi syöttää kursseja yksitellen käsin
    - kurssista syötetään nimi, laajuus ja suorituspäivä (valinnainen)
- käyttäjä voi kurssit listana
- käyttäjä voi suodattaa suoritetut ja suorittamattomat kurssit listasta
- käyttäjä voi merkitä kurssin suoritetuksi
- käyttäjä voi poistaa kurssin

## Jatkokehitysideoita

- käyttäjä voi asettaa suunnitellun suoritusajankohdan
    - periodi ja vuosi
- käyttäjä voi nähdä listan kursseista lajiteltuna suoritusajankohdan mukaan
- käyttäjä voi lisätä kurssisivulinkin kurssin tietoihin
- käyttäjä voi lisätä tärkeitä deadlineja kurssille
- käyttäjä voi nähdä yksittäisen kurssin tietonäkymän
    - kurssin perustiedot
    - kurssin suorittamisen tiedot (linkki kurssisivulle, deadlinet)
    - toiminnot
        - merkitse suoritetuksi
        - muokkaa
        - poista