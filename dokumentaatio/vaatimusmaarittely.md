# Vaatimusmäärittely

## Sovelluksen tarkoitus

"AutoKirja" on sovellus autojen hallintaan. Voit seurata milloin autosi pitää käyttää huollossa ja seurata autoilun kustannuksia. Sovellusta voi käyttää useampi käyttäjä, joilla kaikilla on pääsy omiin autotietoihinsa.

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

**Auton tiedot**

- käyttäjä voi lisätä sovellukseen autoja
    - autosta syötetään perustietoina merkki, malli, lisätiedot (esim. TDI), polttoaine, rekisterinumero ja vuosimalli
- käyttäjä voi lisätä autolle lisätietoja
    - ajetut kilometrit, viimeisin huolto, tulevia huoltoja, arvioitu myyntihinta, arvioitu kilometrimäärä kuukaudessa, arvioitu arvonalenema
- käyttäjä voi lisätä auton huolto-ohjelman
    - kilometrit, arvioitu kustannus, tehtävät toimenpiteet
- käyttäjä voi lisätä autolle ajettuja kilometrejä
    - syöttämällä uuden kokonaismäärän
- käyttäjä voi lisätä autolle uuden huollon
    - kilometrimäärä, hinta ja mitä tehtiin
- käyttäjä voi lisätä autolle kulutustietoja
    - tankkauksen mukaan keskikulutus ja kuinka monta kilometriä ajettu

**Kustannukset**

- käyttäjä näkee auton arvioidun kuukausikustannuksen
- käyttäjä näkee seuraavan huollon ajankohdan ja arvioidun kustannuksen
- käyttäjä näkee auton todelliset kustannukset
    - kuukausittain
    - vuoden tai tilastohistorian alusta

## Jatkokehitysideoita

- käyttäjä voi verrata valitun auton kustannuksia muihin kulkuvälineisiin
    - sähköauto vs. bensiini vs. diesel
    - julkinen vs. auto