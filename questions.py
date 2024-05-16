import models
from options import *
import display

voorwaarden = [
    models.Question(
        id="postcode",
        question_text="Vul hier de 4 cijfers van je postcode in",
        help_text="We gebruiken je postcode om te checken of jouw gemeente de gratis subsidiehulp aanbiedt",
        display_fun=display.default_question_display,
        type=models.QuestionType.NUMBER,
        options=None
    ),
    models.Question(
        id="vorige_subsidie",
        question_text="Heb je eerder landelijke subsidie aangevraagd voor deze maatregel?",
        help_text="Je kunt maar één keer ISDE subsidie aanvragen voor een maatregel. Wel mag je deze combineren met lokale subsidies van de gemeente",
        display_fun=display.default_question_display,
        type=models.QuestionType.SELECTBOX,
        options=YES_NO_OPTIONS
    ),
    models.Question(
        id="koopwoning",
        question_text="Ben je eigenaar van de woning?",
        help_text="Je kunt alleen ISDE subsidie aanvragen als je eigenaar bent van de woning en zelf in deze woning woont",
        display_fun=display.default_question_display,
        type=models.QuestionType.SELECTBOX,
        options=YES_NO_OPTIONS,
    ),
    models.Question(
        id="nieuwbouw",
        question_text="Is de woning gebouwd voor 2019?",
        help_text="De ISDE is alleen voor bestaande woningen, met een bouwjaar van voor 1 januari 2019",
        display_fun=display.default_question_display,
        type=models.QuestionType.SELECTBOX,
        options=YES_NO_OPTIONS
    ),
    models.Question(
        id="installatiebedrijf",
        question_text="Is de maatregel geïnstalleerd door een professionele installateur?",
        help_text = "Je mag de maatregel niet zelf uitvoeren. Daarnaast heb je voor de aanvraag een foto van de uitvoering van de werkzaamheden nodig.",
        display_fun=display.default_question_display,
        type=models.QuestionType.SELECTBOX,
        options=YES_NO_OPTIONS
    ),
    models.Question(
        id="datum",
        question_text="Is de maatregele in de afgelopen 24 maanden aangeschaft?",
        help_text = "De ISDE subsidie moet binnen 24 maanden na het uitvoeren van de maatregelen aangevraagd worden",
        display_fun=display.default_question_display,
        type=models.QuestionType.SELECTBOX,
        options=YES_NO_OPTIONS
    ),
    models.Question(
        id="hoe_verder",
        question_text="Goed nieuws! Je komt waarschijnlijk in aanmerking voor ISDE subsidie",
        help_text = "Kies hieronder hoe je verder wilt. Je kan de aanvraag verder voorbereiden, of helpen je op weg met indienen.",
        display_fun=display.default_question_display,
        type=models.QuestionType.DISPLAY,
        options=None,
        show_previous_next = False
    ),
]

maatregelen = [
    models.Question(
        id="measure",
        question_text="Selecteer voor welk type maatregel(en) je subsidie wilt aanvragen",
        help_text = "Je kunt ook voor twee maatregelen tegelijk ISDE subsidie aanvragen",
        display_fun=display.default_question_display,
        type=models.QuestionType.MULTISELECT,
        options=MEASURE_OPTIONS
    ),
    models.Question(
        id="type_warmtepomp",
        question_text="Selecteer voor welk type warmtepomp je subsidie aan wilt vragen",
        help_text = "Zoek op merk of type",
        display_fun=display.default_question_display,
        type=models.QuestionType.SELECTBOX,
        options=HEATPUMP_OPTIONS
    ),
    models.Question(
        id="type_isolatie",
        question_text="Selecteer voor welk type isolatie je subsidie wilt aanvragen",
        help_text = "" ,
        display_fun=display.default_question_display,
        type=models.QuestionType.SELECTBOX,
        options=INSULATION_OPTIONS
    ),
    models.Question(
        id="type_glasisolatie",
        question_text="Wat voor type glasisolatie heb je laten plaatsen?",
        help_text = "Je kunt voor isolerend glas, panelen, en deuren ISDE subsidie aanvragen" ,
        display_fun=display.default_question_display,
        type=models.QuestionType.SELECTBOX,
        options=GLASS_INSULATION_OPTIONS
    ),
    models.Question(
        id="m2",
        question_text="Hoe veel m2 heb je geïsoleerd?",
        help_text = "Het aantal vierkante meters isolatie bepaald het uiteindelijke subsidiebedrag" ,
        display_fun=display.default_question_display,
        type=models.QuestionType.NUMBER,
        options=None
    ),
    models.Question(
        id="installatiedatum_maatregel",
        question_text="Wanneer is de maatregel uitgevoerd of geïnstalleerd?",
        help_text = "" ,
        display_fun=display.default_question_display,
        type=models.QuestionType.SELECTBOX,
        options=DATE_INSULATION_HEATPUMP_OPTIONS
    ),
    models.Question(
        id="installatiedatum_glas",
        question_text="Wanneer is de isolatiemaatregel uitgevoerd?",
        help_text = "" ,
        display_fun=display.default_question_display,
        type=models.QuestionType.SELECTBOX,
        options=DATE_GLASS_INSULATION_OPTIONS
    ),
    models.Question(
        id="prep_done",
        question_text="Je lijkt klaar te zijn voor de aanvraag!",
        help_text = "Klik op 'Direct aanvragen' en we helpen je nog een handje op weg.",
        display_fun=display.default_question_display,
        type=models.QuestionType.DISPLAY,
        options=None,
        show_previous_next = False
    ),
]

woning_info = [
    models.Question(
        id="straatnaam",
        question_text="Straatnaam",
        help_text = "We hebben de straatnaam van je woning nodig, om de subsidieaanvraag bij het RVO in te dienen",
        display_fun=display.default_question_display,
        type=models.QuestionType.TEXT,
        options=None
    ),
    models.Question(
        id="huisnummer",
        question_text="Huisnummer",
        help_text =  "We hebben de straatnaam van je woning nodig, om de subsidieaanvraag bij het RVO in te dienen",
        display_fun=display.default_question_display,
        type=models.QuestionType.NUMBER,
        options=None
    ),
    models.Question(
        id="plaats",
        question_text="Plaats",
        help_text = "We hebben je woonplaats nodig, om de subsidieaanvraag bij het RVO in te dienen",
        display_fun=display.default_question_display,
        type=models.QuestionType.TEXT,
        options=None
    ),
    models.Question(
        id="bouwjaar",
        question_text="Bouwjaar",
        help_text = "We hebben het bouwjaar van je woning nodig, om de subsidieaanvraag bij het RVO in te dienen",
        display_fun=display.default_question_display,
        type=models.QuestionType.NUMBER,
        options=None
    ),
    models.Question(
        id="woonoppervlakte",
        question_text="Woonoppevlakte",
        help_text = "We hebben de oppervlakte van je woning nodig, om de subsidieaanvraag bij het RVO in te dienen",
        display_fun=display.default_question_display,
        type=models.QuestionType.NUMBER,
        options=None
    ),
    models.Question(
        id="type_woning",
        question_text="Type woning",
        help_text = "We hebben het type van je woning nodig, om de subsidieaanvraag bij het RVO in te dienen",
        display_fun=display.default_question_display,
        type=models.QuestionType.SELECTBOX,
        options=HOUSE_TYPE_OPTIONS
    )
]

persoonlijke_gegevens = [
    models.Question(
        id="voorletters",
        question_text="Voorletters",
        help_text = "We hebben je voorletters nodig om de subsidieaanvraag bij het RVO in te dienen",
        display_fun=display.default_question_display,
        type=models.QuestionType.TEXT,
        options=None
    ),
    models.Question(
        id="achternaam",
        question_text="Achternaam",
        help_text = "We hebben je achternaam nodig om de subsidieaanvraag bij het RVO in te dienen",
        display_fun=display.default_question_display,
        type=models.QuestionType.TEXT,
        options=None
    ),
    models.Question(
        id="email",
        question_text="Email",
        help_text = "We hebben je e-mail nodig, zodat we je op de hoogte kunnen houden van de status van je aanvraag",
        display_fun=display.default_question_display,
        type=models.QuestionType.TEXT,
        options=None
    ),
    models.Question(
        id="telefoonnummer",
        question_text="Telefoonnummer",
        help_text = "We hebben je telefoonnummer nodig, zodat we contact met je kunnen opnemen voor advies of aanvullende informatie",
        display_fun=display.default_question_display,
        type=models.QuestionType.NUMBER,
        options=None
    ),
    models.Question(
        id="BSN",
        question_text="BSN",
        help_text = "We hebben je BSN nodig om de subsidieaanvraag in te dienen bij het RVO",
        display_fun=display.default_question_display,
        type=models.QuestionType.NUMBER,
        options=None
    ),
    models.Question(
        id="IBAN",
        question_text="IBAN",
        help_text = "Het RVO heeft je IBAN nodig om het subsidiebedrag over te maken",
        display_fun=display.default_question_display,
        type=models.QuestionType.TEXT,
        options=None
    ),
    models.Question(
        id="done",
        question_text="Je komt waarschijnlijk in aanmerking voor ISDE subsidie",
        help_text = "Dien je aanvraag in op <a href='https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren'>rvo.nl</a>.<br /><br />",
        display_fun=display.default_question_display,
        type=models.QuestionType.DISPLAY,
        options=None,
        show_previous_next = False
    ),
    models.Question(
        id="vervolg",
        question_text="Hoe wil je verder gaan?",
        help_text = "",
        display_fun=display.display_kick_off_request,
        type=models.QuestionType.RADIO,
        options=[
            Option(text="Ik ga zelf mijn aanvraag indienen.", value="self"),
            Option(text="Neem contact met mij op en help me bij mijn aanvraag.", value="contact"),
            Option(text="Aanvragen met Sobolt als intermediair (€ 99,- _no cure, no pay_).", value="request"),
        ],
        show_previous_next = False
    ),
    models.Question(
        id="go_to_rvo",
        question_text="Zelf indienen doe je bij de RvO",
        help_text = "Ga verder op <a href='https://www.rvo.nl/subsidies-financiering/isde/woningeigenaren'>rvo.nl</a>.<br /><br />",
        display_fun=display.default_question_display,
        type=models.QuestionType.DISPLAY,
        options=None,
        show_previous_next = False
    ),
    models.Question(
        id="contact_me",
        question_text="Laat hier je email achter en wij nemen binnen 2 werkdagen contact met je op",
        help_text = "",
        display_fun=display.display_email_field,
        type=models.QuestionType.TEXT,
        options=None,
        show_previous_next = False
    ),
    models.Question(
        id="aanvragen",
        question_text="Vul je e-mailadres in om de aanvraag te starten",
        help_text = "We sturen je een bericht met verdere instructies.",
        display_fun=display.display_email_field,
        type=models.QuestionType.TEXT,
        options=None,
        show_previous_next = False
    ),
    models.Question(
        id="bedankt_voor_je_aanvraag",
        question_text="Bedankt voor je aanvraag!",
        help_text = "We nemen binnen 2 werkdagen contact met je op.",
        display_fun=display.default_question_display,
        type=models.QuestionType.DISPLAY,
        options=None,
        show_previous_next = False
    ),
]

questions = voorwaarden + maatregelen + woning_info + persoonlijke_gegevens