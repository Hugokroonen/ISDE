from typing import Any
from pydantic import BaseModel
from typing import Optional, Union, Any, List
from options import * 
from models import * 

# Voorwaarden 

postal_code_question = Question(
    id="postcode",
    question_text="Vul hier de eerste 4 cijfers van je postcode in",
    help_text="We gebruiken je postcode om te checken of jouw gemeente de gratis subsidiehulp aanbiedt",
    question_type= QuestionType.NUMBER,
    options=None
)

first_time_question = Question(
        id="vorige_subsidie",
        question_text="Je hebt nog niet eerder landelijke subsidie aangevraagd voor deze isolatiemaatregel",
        help_text="Je kunt maar één keer ISDE subsidie aanvragen voor een maatregel. Wel mag je deze combineren met lokale subsidies van de gemeente",
        question_type=QuestionType.SELECTBOX,
        options=YES_NO_OPTIONS
    )

property_ownership_question = Question(
        id="koopwoning",
        question_text="De woning is jouw eigendom",
        help_text="Je kunt alleen ISDE subsidie aanvragen als je eigenaar bent van de woning en zelf in deze woning woont",
        question_type=QuestionType.SELECTBOX,
        options=YES_NO_OPTIONS
    )

existing_house_question = Question(
        id="nieuwbouw",
        question_text="De maatregel is niet voor een nieuwbouwwoning",
        help_text="De ISDE is alleen voor bestaande woningen, met een bouwjaar van voor 1 januari 2019",
        question_type=QuestionType.SELECTBOX,
        options=YES_NO_OPTIONS
    )

certified_installer_question = Question(
        id="installatiebedrijf",
        question_text="De isolatiemaatregel is geplaatst door een professioneel installateur, en je hebt bewijs van de installatie",
        help_text = "Je mag de maatregel niet zelf uitvoeren. Bovendien heb je voor de aanvraag een foto van de uitvoering van de werkzaamheden nodig.",
        question_type=QuestionType.SELECTBOX,
        options=YES_NO_OPTIONS
    )

two_years_question = Question(
        id="datum",
        question_text="De maatregel is niet langer dan 24 maanden geleden aangeschaft",
        help_text = "De ISDE subsidie moet binnen 24 maanden na het uitvoeren van de maatregelen aangevraagd worden",
        question_type=QuestionType.SELECTBOX,
        options=YES_NO_OPTIONS
    )

# Maatregelen

measure_question = Question(
        id="measure",
        question_text="Selecteer voor welk type maatregel(en) je subsidie wilt aanvragen",
        help_text = "Je kunt ook voor twee maatregelen tegelijk ISDE subsidie aanvragen",
        question_type=QuestionType.SELECTBOX,
        options=MEASURE_OPTIONS
    )

heatpump_type_question = Question(
        id="type_warmtepomp",
        question_text="Selecteer voor welk type warmtepomp je subsidie aan wilt vragen",
        help_text = "Zoek op merk of type",
        question_type=QuestionType.SELECTBOX,
        options=HEATPUMP_OPTIONS
    )

insulation_type_question = Question(
        id="type_isolatie",
        question_text="Selecteer voor welk type isolatie je subsidie wilt aanvragen",
        help_text = "" ,
        question_type=QuestionType.SELECTBOX,
        options=INSULATION_OPTIONS
    )


glass_insulation_type_question = Question(
        id="type_glasisolatie",
        question_text="Wat voor type glasisolatie heb je laten plaatsen?",
        help_text = "Je kunt voor isolerend glas, panelen, en deuren ISDE subsidie aanvragen" ,
        question_type=QuestionType.SELECTBOX,
        options=GLASS_INSULATION_OPTIONS
    )

m2_question = Question(
        id="m2",
        question_text="Hoe veel m2 heb je geïsoleerd?",
        help_text = "Het aantal vierkante meters isolatie bepaald het uiteindelijke subsidiebedrag" ,
        question_type=QuestionType.NUMBER,
        options=None
    )

installation_date_question = Question(
        id="installatiedatum_maatregel",
        question_text="Wanneer is de maatregel uitgevoerd of geïnstalleerd?",
        help_text = "" ,
        question_type=QuestionType.SELECTBOX,
        options=DATE_INSULATION_HEATPUMP_OPTIONS
    )

glass_installation_date_question = Question(
        id="installatiedatum_glas",
        question_text="Wanneer is de isolatiemaatregel uitgevoerd?",
        help_text = "" ,
        question_type=QuestionType.SELECTBOX,
        options=DATE_GLASS_INSULATION_OPTIONS
    )


# Adres & woninggegevens 

streetname_question = Question(
        id="straatnaam",
        question_text="Straatnaam",
        help_text = "We hebben de straatnaam van je woning nodig, om de subsidieaanvraag bij het RVO in te dienen",
        question_type=QuestionType.TEXT,
        options=None
    )

housenumber_question = Question(
        id="huisnummer",
        question_text="Huisnummer",
        help_text =  "We hebben de straatnaam van je woning nodig, om de subsidieaanvraag bij het RVO in te dienen",
        question_type=QuestionType.NUMBER,
        options=None
    )

city_question = Question(
        id="plaats",
        question_text="Plaats",
        help_text = "We hebben je woonplaats nodig, om de subsidieaanvraag bij het RVO in te dienen",
        question_type=QuestionType.TEXT,
        options=None
    )

building_year_question = Question(
        id="bouwjaar",
        question_text="Bouwjaar",
        help_text = "We hebben het bouwjaar van je woning nodig, om de subsidieaanvraag bij het RVO in te dienen",
        question_type=QuestionType.NUMBER,
        options=None
    )

surface_area_question = Question(
        id="woonoppervlakte",
        question_text="Woonoppevlakte",
        help_text = "We hebben de oppervlakte van je woning nodig, om de subsidieaanvraag bij het RVO in te dienen",
        question_type=QuestionType.NUMBER,
        options=None
    )

house_type_question = Question(
        id="type_woning",
        question_text="Type woning",
        help_text = "We hebben het type van je woning nodig, om de subsidieaanvraag bij het RVO in te dienen",
        question_type=QuestionType.SELECTBOX,
        options=HOUSE_TYPE_OPTIONS
    )

# Persoonlijke gegevens

intials_question = Question(
        id="voorletters",
        question_text="Voorletters",
        help_text = "We hebben je voorletters nodig om de subsidieaanvraag bij het RVO in te dienen",
        question_type=QuestionType.TEXT,
        options=None
    )


last_name_question = Question(
        id="achternaam",
        question_text="Achternaam",
        help_text = "We hebben je achternaam nodig om de subsidieaanvraag bij het RVO in te dienen",
        question_type=QuestionType.TEXT,
        options=None
    )

email_question = Question(
        id="email",
        question_text="Email",
        help_text = "We hebben je e-mail nodig, zodat we je op de hoogte kunnen houden van de status van je aanvraag",
        question_type=QuestionType.TEXT,
        options=None
    )

phone_number_question = Question(
        id="telefoonnummer",
        question_text="Telefoonnummer",
        help_text = "We hebben je telefoonnummer nodig, zodat we contact met je kunnen opnemen voor advies of aanvullende informatie",
        question_type=QuestionType.NUMBER,
        options=None
    )

BSN_question = Question(
        id="BSN",
        question_text="BSN",
        help_text = "We hebben je BSN nodig om de subsidieaanvraag in te dienen bij het RVO",
        question_type=QuestionType.NUMBER,
        options=None
    )

bank_account_question = Question(
        id="IBAN",
        question_text="IBAN",
        help_text = "Het RVO heeft je IBAN nodig om het subsidiebedrag over te maken",
        question_type=QuestionType.TEXT,
        options=None
    )
