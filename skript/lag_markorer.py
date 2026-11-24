import json
K = "Språkrådet (2025): Rapport fra test av språkroboter, sha256 73b84a52…a4702f"
def m(id, gruppe, regex, side, sitat, merknad=""):
    return dict(id=id, gruppe=gruppe, regex=regex, flagg="i", kilde=K if side else "oppgavespesifikasjon (strukturmarkør)", side=side, sitat=sitat, merknad=merknad)
L = [
 # (a) stående fraser
 m("komplekst_og_viktig","stående frase",r"\bkomplekse?t?\s+og\s+viktige?\b",14,"«Komplekst og viktig» og lignende er standardfraser som går igjen i de fleste tekstene."),
 m("viktig_komponent","stående frase",r"\bviktige?\s+komponent\w*",15,"«Viktig komponent», «innebærer» og «dette kan inkludere» er standardformuleringer"),
 m("innebærer","stående frase",r"\binneb(?:ærer|er)\b",15,"«Viktig komponent», «innebærer» og «dette kan inkludere» er standardformuleringer","nn-form «inneber» lagt til"),
 m("dette_kan_inkludere","stående frase",r"\bdette\s+kan\s+inkludere\b",15,"«dette kan inkludere» er standardformuleringer"),
 m("dynamisk_felt","stående frase",r"\bdynamiske?\s+felt\w*",15,"«Fiskeripolitikk er et dynamisk felt som krever kontinuerlig tilpasning og innovasjon.» … ordgyting"),
 m("kontinuerlig_tilpasning","stående frase",r"\bkontinuerleg?\s+tilpas\w*",15,"«…krever kontinuerlig tilpasning og innovasjon.»","nn «kontinuerleg» lagt til"),
 m("fleksibel_tilpasningsdyktig","stående frase",r"\bfleksib\w*\s+og\s+tilpasningsdykt\w*",15,"standardformuleringen «fleksibel og tilpasningsdyktig tilnærming» notert som et ordgytingsproblem"),
 m("aspekt","stående frase",r"\baspekt(?:er|ene|a|ane)?\b",15,"«aspektene» og «kompleksiteten» i siste setning, som går igjen i mange tekster"),
 m("kompleksitet","stående frase",r"\bkompleksitet(?:en|a)?\b",15,"«aspektene» og «kompleksiteten» … går igjen i mange tekster"),
 m("komplekst_felt","stående frase",r"\bkomplekse?t?\s+felt\w*",15,"«I sammendrag er landbrukspolitikk et komplekst felt som krever et balansert syn …»"),
 m("balansert","stående frase",r"\bbalanserte?\s+(?:syn|linje|tilnærming)\w*",14,"«Norge inntok en forsiktig og balansert linje» (s. 14); «et balansert syn» (s. 15)"),
 m("balansegang","stående frase",r"\bbalansegang\w*",15,"«Samlet sett er fiskeripolitikk en balansegang mellom ulike hensyn og interesser.»"),
 m("skjæringspunkt","stående frase",r"\bskjæringspunkt\w*\s+mellom\b",14,"«Det er nettopp i skjæringspunktet mellom disse ulike målene at …»"),
 m("dypt_forankret","stående frase",r"\bdj?y?u?pt\s+forankr\w*",15,"«Alt i alt er Norges forhold til NATO dypt forankret i landets historie …»","nn «djupt» dekkes"),
 m("ikke_bare_ogsaa","stående frase",r"\bikkj?e\s+(?:bare|berre)\b[^.!?]{0,80}?\bogså\b",15,"«Fiskerinæringen er ikke bare en økonomisk aktivitet; den er også en kulturell bærebjelke …»","nn «ikkje berre» dekkes"),
 # (a) avslutningsformler
 m("alt_i_alt","avslutningsformel",r"\balt\s+i\s+alt\b",15,"Oppsummeringsformuleringen «alt i alt … forankret» er registrert som feil."),
 m("samlet_sett","avslutningsformel",r"\bsaml(?:et|a)\s+sett\b",15,"Oppsummeringsformuleringen «samlet sett … balansegang» er notert som en tekstfeil","nn «samla sett» lagt til"),
 m("i_sammendrag","avslutningsformel",r"\bi\s+sam(?:m|)(?:endrag|andrag)\b",15,"oppsummeringsformuleringen «[er] i sammendrag et komplekst felt» notert som feil","nn «i samandrag» lagt til"),
 # (a) kalker / oversettelseslån
 m("gjore_en_forskjell","kalk",r"\bgj(?:ø|e)re?\w*\s+(?:en|ein|ei)\s+(?:forskjell|skilnad)\b",10,"gjøre en forskjell (av engelsk make a difference)","fotnote 4; nn-former lagt til"),
 m("fanget_oyet","kalk",r"\bfang\w*\s+(?:øyet|auget|blikket)\b",10,"plutselig fanget øyet hans noe (ChatGPT)"),
 m("dypt_pust","kalk",r"\b(?:et|eit)\s+dj?y?u?pt\s+pust\b",10,"ho tok eit djupt pust (Copilot)"),
 m("tilfreds_med_aa","kalk",r"\btilfreds\s+med\s+å\b",10,"for no var han tilfreds med å vere i byen (Copilot)"),
 m("som_sine_egne_lommer","kalk",r"\bsom\s+sin(?:e)?\s+eig?ne?\s+lomm\w*",10,"begge kjente den [skogen] som sine egne lommer (Le Chat)"),
 m("med_en_x_stemme","kalk",r"\bmed\s+(?:en|ei|ein)\s+\w+\s+stemme\b",10,"sa hun med en stolt stemme (Le Chat)"),
 m("aktorene_involvert","kalk",r"\b\w+(?:ene|ane|a)\s+involvert\b",10,"de ulike aktørene involvert (Le Chat)"),
 m("ut_av_kontroll","kalk",r"\but\s+av\s+kontroll\b",10,"en kveld som hadde gått fullstendig ut av kontroll (NorMistral)"),
 m("ny_start","kalk",r"\b(?:en|ein|ei)\s+ny\s+start\b",10,"en kopp [kaffe] som kunne tilby henne en ny start (ChatGPT)"),
 # (b) strukturmarkører
 m("tankestrek_uten_mellomrom","struktur",r"(?<=\S)—(?=\S)",None,"tankestrek uten mellomrom (—)","Norsk tankestrek med mellomrom ( – / — ) telles ikke"),
 m("title_case_overskrift","struktur",r"(?m)^(?=[^\n]{3,80}$)(?:#+\s*)?[A-ZÆØÅ][\wæøå]*(?:\s+(?:[A-ZÆØÅ][\wæøå]*|og|i|for|av|på|til|med|eller|en|et|ei|ein|eit))*\s+[A-ZÆØÅ][\wæøå]+(?:\s+[A-ZÆØÅ][\wæøå]+)+\s*$",None,"store forbokstaver i overskrifter etter engelsk mønster","flagg uten i: egen linje, ≥3 ord med stor forbokstav, ingen sluttpunktum"),
 m("ikke_x_men_y","struktur",r"\bikkj?e\s+[^.,;!?\n]{1,60},\s*men\b",None,"«ikke X, men Y»"),
 m("tredelt_oppramsing","struktur",r"\b[\wæøå-]+(?:\s[\wæøå-]+){0,2},\s[\wæøå-]+(?:\s[\wæøå-]+){0,2},?\s(?:og|eller)\s[\wæøå-]+",None,"tredelte oppramsinger","«A, B og C» med 1–3 ord per ledd"),
 m("punktliste_fet_tittel","struktur",r"(?m)^\s*(?:[-*•]|\d+[.)])\s+\*\*[^*\n]+\*\*",None,"punktlister med fete titler"),
]
for x in L:
    if x["id"] == "title_case_overskrift": x["flagg"] = ""
json.dump({"versjon":"v0","frosset":"2026-11-24","telleregel":"re.finditer per regex over NFC-tekst; hvert treff = 1; flagg 'i' = re.IGNORECASE","markorer":L}, open("markorer_v0.json","w"), ensure_ascii=False, indent=1)
print(len(L))
