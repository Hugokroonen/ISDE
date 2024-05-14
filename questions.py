from models import Question, QuestionType
from options import *

voorwaarden = [
    Question(
        id="postcode",
        question_text="Vul hier de 4 cijfers van je postcode in",
        help_text="We gebruiken je postcode om te checken of jouw gemeente de gratis subsidiehulp aanbiedt",
        type=QuestionType.NUMBER,
        options=None
    ),
    Question(
        id="vorige_subsidie",
        question_text="Je hebt nog niet eerder landelijke subsidie aangevraagd voor deze isolatiemaatregel",
        help_text="Je kunt maar één keer ISDE subsidie aanvragen voor een maatregel. Wel mag je deze combineren met lokale subsidies van de gemeente",
        type=QuestionType.SELECTBOX,
        options=YES_NO_OPTIONS
    ),
    Question(
        id="koopwoning",
        question_text="De woning is jouw eigendom",
        help_text="Je kunt alleen ISDE subsidie aanvragen als je eigenaar bent van de woning en zelf in deze woning woont",
        type=QuestionType.SELECTBOX,
        options=YES_NO_OPTIONS
    ),
    Question(
        id="nieuwbouw",
        question_text="De maatregel is niet voor een nieuwbouwwoning",
        help_text="De ISDE is alleen voor bestaande woningen, met een bouwjaar van voor 1 januari 2019",
        type=QuestionType.SELECTBOX,
        options=YES_NO_OPTIONS
    ),
    Question(
        id="installatiebedrijf",
        question_text="De isolatiemaatregel is geplaatst door een professioneel installateur, en je hebt bewijs van de installatie",
        help_text = "Je mag de maatregel niet zelf uitvoeren. Bovendien heb je voor de aanvraag een foto van de uitvoering van de werkzaamheden nodig.",
        type=QuestionType.SELECTBOX,
        options=YES_NO_OPTIONS
    ),
    Question(
        id="datum",
        question_text="De maatregel is niet langer dan 24 maanden geleden aangeschaft",
        help_text = "De ISDE subsidie moet binnen 24 maanden na het uitvoeren van de maatregelen aangevraagd worden",
        type=QuestionType.SELECTBOX,
        options=YES_NO_OPTIONS
    )
]

maatregelen = [
    Question(
        id="measure",
        question_text="Selecteer voor welk type maatregel(en) je subsidie wilt aanvragen",
        help_text = "Je kunt ook voor twee maatregelen tegelijk ISDE subsidie aanvragen",
        type=QuestionType.SELECTBOX,
        options=MEASURE_OPTIONS
    ),
    Question(
        id="type_warmtepomp",
        question_text="Selecteer voor welk type warmtepomp je subsidie aan wilt vragen",
        help_text = "Zoek op merk of type",
        type=QuestionType.SELECTBOX,
        options=HEATPUMP_OPTIONS
    ),
    Question(
        id="type_isolatie",
        question_text="Selecteer voor welk type isolatie je subsidie wilt aanvragen",
        help_text = "" ,
        type=QuestionType.SELECTBOX,
        options=INSULATION_OPTIONS
    ),
    Question(
        id="type_glasisolatie",
        question_text="Wat voor type glasisolatie heb je laten plaatsen?",
        help_text = "Je kunt voor isolerend glas, panelen, en deuren ISDE subsidie aanvragen" ,
        type=QuestionType.SELECTBOX,
        options=GLASS_INSULATION_OPTIONS
    ),
    Question(
        id="m2",
        question_text="Hoe veel m2 heb je geïsoleerd?",
        help_text = "Het aantal vierkante meters isolatie bepaald het uiteindelijke subsidiebedrag" ,
        type=QuestionType.NUMBER,
        options=None
    ),
    Question(
        id="installatiedatum_maatregel",
        question_text="Wanneer is de maatregel uitgevoerd of geïnstalleerd?",
        help_text = "" ,
        type=QuestionType.SELECTBOX,
        options=DATE_INSULATION_HEATPUMP_OPTIONS
    ),
    Question(
        id="installatiedatum_glas",
        question_text="Wanneer is de isolatiemaatregel uitgevoerd?",
        help_text = "" ,
        type=QuestionType.SELECTBOX,
        options=DATE_GLASS_INSULATION_OPTIONS
    )
]

woning_info = [
    Question(
        id="straatnaam",
        question_text="Straatnaam",
        help_text = "We hebben de straatnaam van je woning nodig, om de subsidieaanvraag bij het RVO in te dienen",
        type=QuestionType.TEXT,
        options=None
    ),
    Question(
        id="huisnummer",
        question_text="Huisnummer",
        help_text =  "We hebben de straatnaam van je woning nodig, om de subsidieaanvraag bij het RVO in te dienen",
        type=QuestionType.NUMBER,
        options=None
    ),
    Question(
        id="plaats",
        question_text="Plaats",
        help_text = "We hebben je woonplaats nodig, om de subsidieaanvraag bij het RVO in te dienen",
        type=QuestionType.TEXT,
        options=None
    ),
    Question(
        id="bouwjaar",
        question_text="Bouwjaar",
        help_text = "We hebben het bouwjaar van je woning nodig, om de subsidieaanvraag bij het RVO in te dienen",
        type=QuestionType.NUMBER,
        options=None
    ),
    Question(
        id="woonoppervlakte",
        question_text="Woonoppevlakte",
        help_text = "We hebben de oppervlakte van je woning nodig, om de subsidieaanvraag bij het RVO in te dienen",
        type=QuestionType.NUMBER,
        options=None
    ),
    Question(
        id="type_woning",
        question_text="Type woning",
        help_text = "We hebben het type van je woning nodig, om de subsidieaanvraag bij het RVO in te dienen",
        type=QuestionType.SELECTBOX,
        options=HOUSE_TYPE_OPTIONS
    )
]

persoonlijke_gegevens = [
    Question(
            id="voorletters",
            question_text="Voorletters",
            help_text = "We hebben je voorletters nodig om de subsidieaanvraag bij het RVO in te dienen",
            type=QuestionType.TEXT,
            options=None
    ),
    Question(
            id="achternaam",
            question_text="Achternaam",
            help_text = "We hebben je achternaam nodig om de subsidieaanvraag bij het RVO in te dienen",
            type=QuestionType.TEXT,
            options=None
    ),
    Question(
            id="email",
            question_text="Email",
            help_text = "We hebben je e-mail nodig, zodat we je op de hoogte kunnen houden van de status van je aanvraag",
            type=QuestionType.TEXT,
            options=None
    ),
    Question(
            id="telefoonnummer",
            question_text="Telefoonnummer",
            help_text = "We hebben je telefoonnummer nodig, zodat we contact met je kunnen opnemen voor advies of aanvullende informatie",
            type=QuestionType.NUMBER,
            options=None
    ),
    Question(
            id="BSN",
            question_text="BSN",
            help_text = "We hebben je BSN nodig om de subsidieaanvraag in te dienen bij het RVO",
            type=QuestionType.NUMBER,
            options=None
    ),
    Question(
            id="IBAN",
            question_text="IBAN",
            help_text = "Het RVO heeft je IBAN nodig om het subsidiebedrag over te maken",
            type=QuestionType.TEXT,
            options=None
    ),
    Question(
        id="done",
        question_text="Je bent klaar!",
        help_text = "We gaan voor je aan de slag",
        type=QuestionType.DISPLAY,
        options=None
    )
]

questions = voorwaarden + maatregelen + woning_info + persoonlijke_gegevens 