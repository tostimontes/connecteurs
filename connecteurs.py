import random
import difflib
from colorama import init, Fore, Back, Style

init(autoreset=True)  # initializes Colorama

# Dictionary of connectors: French to Spanish (including variations)
connectors = {
    "et": ["y"],
    "mais": ["pero", "mas"],
    "ou": ["o"],
    "donc": ["así que", "por lo tanto", "entonces"],
    "car": ["porque", "ya que"],
    "parce que": ["porque", "ya que"],
    "puisque": ["puesto que", "ya que"],
    "alors que": ["mientras que", "aunque"],
    "bien que": ["aunque", "a pesar de que"],
    "tant que": ["mientras", "en tanto que"],
    "pendant que": ["mientras", "durante"],
    "depuis que": ["desde que"],
    "avant que": ["antes de que"],
    "après que": ["después de que"],
    "lorsque": ["cuando", "al momento que"],
    "si": ["si"],
    "quoique": ["aunque", "a pesar de que"],
    "pour que": ["para que"],
    "afin que": ["para que", "a fin de que"],
    "comme": ["como", "ya que"],
    "puis": ["luego", "entonces"],
    "enfin": ["finalmente", "por fin"],
    "d'abord": ["primero", "en primer lugar"],
    "ensuite": ["luego", "después"],
    "en outre": ["además", "asimismo"],
    "par ailleurs": ["por otro lado", "además"],
    "néanmoins": ["sin embargo", "no obstante"],
    "toutefois": ["sin embargo", "no obstante"],
    "cependant": ["sin embargo", "no obstante"],
    "aussi": ["también", "así"],
    "ainsi que": ["así como"],
    "de plus": ["además"],
    "de sorte que": ["de modo que"],
    "en effet": ["en efecto"],
    "en tant que": ["como"],
    "jusqu'à ce que": ["hasta que"],
    "malgré que": ["a pesar de que"],
    "plutôt que": ["en lugar de"],
    "pour autant que": ["siempre y cuando"],
    "tant bien que mal": ["con dificultad", "a duras penas"],
    "tout comme": ["al igual que"],
    "vu que": ["dado que", "considerando que"],
    "or": ["ahora bien", "sin embargo"],
    "quant à": ["en cuanto a"],
    "sachant que": ["sabiendo que"],
    "soit ... soit": ["sea ... sea", "ya sea ... ya sea"],
    "supposé que": ["suponiendo que"],
    "tout bien considéré": ["todo bien considerado"],
    "voire même": ["incluso", "hasta"],
    # Additional translations
}

example_phrases = {
    "et": {
        "french": [
            "Il a mangé **et** il est parti.",
            "Elle est malade **et** elle reste à la maison.",
        ],
        "spanish": [
            "Ha comido **y** se ha ido.",
            "La persona está herida **y** se retira de la casa.",
        ],
    },
    "mais": {
        "french": [
            "Il aime le fromage **mais** pas le vin.",
            "Elle travaille dur **mais** est heureuse.",
        ],
        "spanish": [
            "Él ama el queso **pero** no el vino.",
            "Ella trabaja duro **pero** está feliz.",
        ],
        "alt_spanish": [
            "Él ama el queso **mas** no el vino.",
            "Ella trabaja duro **mas** está feliz.",
        ],
    },
    "ou": {
        "french": [
            "Voulez-vous du thé **ou** du café?",
            "Nous pouvons aller au cinéma **ou** au théâtre.",
        ],
        "spanish": ["¿Quieres té **o** café?", "Podemos ir al cine **o** al teatro."],
    },
    "donc": {
        "french": [
            "Il pleut **donc** prends un parapluie.",
            "Elle est malade **donc** elle reste à la maison.",
        ],
        "spanish": [
            "Llueve **así que** toma un paraguas.",
            "Está enferma **así que** se queda en casa.",
        ],
        "alt_spanish": [
            "Llueve **por lo tanto** toma un paraguas.",
            "Está enferma **por lo tanto** se queda en casa.",
        ],
        "alt2_spanish": [
            "Llueve **entonces** toma un paraguas.",
            "Está enferma **entonces** se queda en casa.",
        ],
    },
    "car": {
        "french": [
            "Je reste à la maison **car** il pleut.",
            "Elle est triste **car** son chat est malade.",
        ],
        "spanish": [
            "Me quedo en casa **porque** llueve.",
            "Ella está triste **porque** su gato está enfermo.",
        ],
        "alt_spanish": [
            "Me quedo en casa **ya que** llueve.",
            "Ella está triste **ya que** su gato está enfermo.",
        ],
    },
    "parce que": {
        "french": [
            "Je cours tous les jours **parce que** c'est sain.",
            "Il lit beaucoup **parce que** il aime apprendre.",
        ],
        "spanish": [
            "Corro todos los días **porque** es saludable.",
            "Él lee mucho **porque** le gusta aprender.",
        ],
        "alt_spanish": [
            "Corro todos los días **ya que** es saludable.",
            "Él lee mucho **ya que** le gusta aprender.",
        ],
    },
    "puisque": {
        "french": [
            "Je suis heureux **puisque** je suis en vacances.",
            "Elle chante **puisque** elle est joyeuse.",
        ],
        "spanish": [
            "Estoy feliz **puesto que** estoy de vacaciones.",
            "Ella canta **puesto que** está alegre.",
        ],
        "alt_spanish": [
            "Estoy feliz **ya que** estoy de vacaciones.",
            "Ella canta **ya que** está alegre.",
        ],
    },
    "alors que": {
        "french": [
            "Il travaille **alors que** ses amis s'amusent.",
            "Elle lit **alors que** son frère regarde la télévision.",
        ],
        "spanish": [
            "Él trabaja **mientras que** sus amigos se divierten.",
            "Ella lee **mientras que** su hermano mira la televisión.",
        ],
        "alt_spanish": [
            "Él trabaja **aunque** sus amigos se divierten.",
            "Ella lee **aunque** su hermano mira la televisión.",
        ],
    },
    "bien que": {
        "french": [
            "Elle sort **bien que** il pleuve.",
            "Il sourit **bien que** il soit triste.",
        ],
        "spanish": [
            "Ella sale **aunque** llueva.",
            "Él sonríe **aunque** esté triste.",
        ],
        "alt_spanish": [
            "Ella sale **a pesar de que** llueva.",
            "Él sonríe **a pesar de que** esté triste.",
        ],
    },
    "tant que": {
        "french": [
            "Profite de la vie **tant que** tu es jeune.",
            "Il jouera au football **tant que** il le pourra.",
        ],
        "spanish": [
            "Disfruta la vida **mientras** eres joven.",
            "Él jugará al fútbol **mientras** pueda.",
        ],
        "alt_spanish": [
            "Disfruta la vida **en tanto que** eres joven.",
            "Él jugará al fútbol **en tanto que** pueda.",
        ],
    },
    "pendant que": {
        "french": [
            "Il étudie **pendant que** ses amis dorment.",
            "Elle cuisine **pendant que** son mari lit le journal.",
        ],
        "spanish": [
            "Él estudia **mientras** sus amigos duermen.",
            "Ella cocina **mientras** su marido lee el periódico.",
        ],
        "alt_spanish": [
            "Él estudia **durante** sus amigos duermen.",
            "Ella cocina **durante** su marido lee el periódico.",
        ],
    },
    "depuis que": {
        "french": [
            "Il est heureux **depuis qu'**il a rencontré Marie.",
            "Je fais du yoga **depuis que** je suis jeune.",
        ],
        "spanish": [
            "Él está feliz **desde que** conoció a María.",
            "Hago yoga **desde que** soy joven.",
        ],
    },
    "avant que": {
        "french": [
            "Il faut finir le travail **avant qu'**il ne soit trop tard.",
            "Elle appelle sa mère **avant que** celle-ci parte au travail.",
        ],
        "spanish": [
            "Hay que terminar el trabajo **antes de que** sea demasiado tarde.",
            "Ella llama a su madre **antes de que** esta vaya al trabajo.",
        ],
    },
    "après que": {
        "french": [
            "Nous irons au cinéma **après que** le dîner sera terminé.",
            "Elle se reposera **après qu'**elle aura fini ses devoirs.",
        ],
        "spanish": [
            "Iremos al cine **después de que** la cena haya terminado.",
            "Ella descansará **después de que** haya terminado sus deberes.",
        ],
    },
    "lorsque": {
        "french": [
            "Je t'appellerai **lorsque** j'arriverai.",
            "Il a commencé à pleuvoir **lorsque** nous sommes sortis.",
        ],
        "spanish": [
            "Te llamaré **cuando** llegue.",
            "Empezó a llover **cuando** salimos.",
        ],
        "alt_spanish": [
            "Te llamaré **al momento que** llegue.",
            "Empezó a llover **al momento que** salimos.",
        ],
    },
    "si": {
        "french": [
            "**Si** tu viens, nous irons au parc.",
            "**Si** elle étudie, elle réussira l'examen.",
        ],
        "spanish": [
            "**Si** vienes, iremos al parque.",
            "**Si** estudia, pasará el examen.",
        ],
    },
    "quoique": {
        "french": [
            "Elle sortira **quoique** il pleuve.",
            "Il sourit **quoique** triste.",
        ],
        "spanish": [
            "Ella saldrá **aunque** llueva.",
            "Él sonríe **aunque** esté triste.",
        ],
        "alt_spanish": [
            "Ella saldrá **a pesar de que** llueva.",
            "Él sonríe **a pesar de que** esté triste.",
        ],
    },
    "pour que": {
        "french": [
            "Je travaille dur **pour que** mes enfants aient une bonne éducation.",
            "Elle économise **pour que** nous puissions voyager.",
        ],
        "spanish": [
            "Trabajo duro **para que** mis hijos tengan una buena educación.",
            "Ella ahorra **para que** podamos viajar.",
        ],
    },
    "afin que": {
        "french": [
            "Je me lève tôt **afin que** je puisse méditer en paix.",
            "Il étudie beaucoup **afin qu'**il puisse réussir.",
        ],
        "spanish": [
            "Me levanto temprano **para que** pueda meditar.",
            "Empezó a estudiar mucho **para que** pueda dormir.",
        ],
    },
    "comme": {
        "french": [
            "**Comme** il pleut, nous resterons à l'intérieur.",
            "**Comme** elle est malade, elle ne viendra pas.",
        ],
        "spanish": [
            "**Como** llueve, nos quedaremos adentro.",
            "**Como** está enferma, no vendrá.",
        ],
        "alt_spanish": [
            "**Ya que** llueve, nos quedaremos adentro.",
            "**Ya que** está enferma, no vendrá.",
        ],
    },
    "puis": {
        "french": [
            "Nous irons au cinéma, **puis** au restaurant.",
            "Elle a lu le livre, **puis** elle a dormi.",
        ],
        "spanish": [
            "Iremos al cine, **luego** al restaurante.",
            "Ella leyó el libro, **luego** se durmió.",
        ],
        "alt_spanish": [
            "Iremos al cine, **entonces** al restaurante.",
            "Ella leyó el libro, **entonces** se durmió.",
        ],
    },
    "enfin": {
        "french": [
            "**Enfin** le weekend est arrivé!",
            "**Enfin**, il a réussi à résoudre le problème.",
        ],
        "spanish": [
            "**Finalmente** llegó el fin de semana!",
            "**Finalmente**, logró resolver el problema.",
        ],
        "alt_spanish": [
            "**Por fin** llegó el fin de semana!",
            "**Por fin**, logró resolver el problema.",
        ],
    },
    "d'abord": {
        "french": [
            "**D'abord**, nous devons finir nos devoirs.",
            "**D'abord**, mangeons, puis nous parlerons.",
        ],
        "spanish": [
            "**Primero**, debemos terminar nuestros deberes.",
            "**Primero**, comamos, luego hablaremos.",
        ],
        "alt_spanish": [
            "**En primer lugar**, debemos terminar nuestros deberes.",
            "**En primer lugar**, comamos, luego hablaremos.",
        ],
    },
    "ensuite": {
        "french": [
            "Fais tes devoirs, **ensuite** tu peux jouer.",
            "Nous irons au marché, **ensuite** au café.",
        ],
        "spanish": [
            "Haz tus tareas, **luego** puedes jugar.",
            "Iremos al mercado, **luego** al café.",
        ],
        "alt_spanish": [
            "Haz tus tareas, **después** puedes jugar.",
            "Iremos al mercado, **después** al café.",
        ],
    },
    "en outre": {
        "french": [
            "Elle est intelligente, **en outre**, elle est drôle.",
            "**En outre**, il faut considérer les coûts.",
        ],
        "spanish": [
            "Ella es inteligente, **además**, es divertida.",
            "**Además**, hay que considerar los costos.",
        ],
        "alt_spanish": [
            "Ella es inteligente, **asimismo**, es divertida.",
            "**Asimismo**, hay que considerar los costos.",
        ],
    },
    "par ailleurs": {
        "french": [
            "Il est bon cuisinier, **par ailleurs**, il est aussi un excellent jardinier.",
            "**Par ailleurs**, il faut noter les changements récents.",
        ],
        "spanish": [
            "Es un buen cocinero, **por otro lado**, también es un excelente jardinero.",
            "**Por otro lado**, hay que notar los cambios recientes.",
        ],
        "alt_spanish": [
            "Es un buen cocinero, **además**, también es un excelente jardinero.",
            "**Además**, hay que notar los cambios recientes.",
        ],
    },
    "néanmoins": {
        "french": [
            "Il est jeune, **néanmoins**, il est très responsable.",
            "C'est cher, **néanmoins**, cela en vaut la peine.",
        ],
        "spanish": [
            "Es joven, **sin embargo**, es muy responsable.",
            "Es caro, **sin embargo**, vale la pena.",
        ],
        "alt_spanish": [
            "Es joven, **no obstante**, es muy responsable.",
            "Es caro, **no obstante**, vale la pena.",
        ],
    },
    "toutefois": {
        "french": [
            "Elle veut participer, **toutefois**, elle n'a pas le temps.",
            "Ce plan est bon, **toutefois**, il y a des risques.",
        ],
        "spanish": [
            "Ella quiere participar, **sin embargo**, no tiene tiempo.",
            "Este plan es bueno, **sin embargo**, hay riesgos.",
        ],
        "alt_spanish": [
            "Ella quiere participar, **no obstante**, no tiene tiempo.",
            "Este plan es bueno, **no obstante**, hay riesgos.",
        ],
    },
    "cependant": {
        "french": [
            "Il veut sortir, **cependant** il pleut.",
            "Elle est riche, **cependant** elle est humble.",
        ],
        "spanish": [
            "Quiere salir, **sin embargo** llueve.",
            "Es rica, **sin embargo** es humilde.",
        ],
        "alt_spanish": [
            "Quiere salir, **no obstante** llueve.",
            "Es rica, **no obstante** es humilde.",
        ],
    },
    "aussi": {
        "french": [
            "Elle aime le thé, **aussi** le café.",
            "Il travaille ici, **aussi** il connaît bien l'endroit.",
        ],
        "spanish": [
            "Le gusta el té, **también** el café.",
            "Trabaja aquí, **también** conoce bien el lugar.",
        ],
        "alt_spanish": [
            "Le gusta el té, **así** el café.",
            "Trabaja aquí, **así** conoce bien el lugar.",
        ],
    },
    "ainsi que": {
        "french": [
            "Elle a apporté des fruits **ainsi que** des gâteaux.",
            "Il sait jouer du piano **ainsi que** de la guitare.",
        ],
        "spanish": [
            "Ella trajo frutas **así como** pasteles.",
            "Sabe tocar el piano **así como** la guitarra.",
        ],
    },
    "de plus": {
        "french": [
            "Il est intelligent, **de plus**, il est travailleur.",
            "Elle est gentille, **de plus**, elle est généreuse.",
        ],
        "spanish": [
            "Es inteligente, **además**, es trabajador.",
            "Es amable, **además**, es generosa.",
        ],
    },
    "de sorte que": {
        "french": [
            "Il étudie beaucoup **de sorte que** il réussisse.",
            "Elle économise **de sorte que** elle puisse voyager.",
        ],
        "spanish": [
            "Estudia mucho **de modo que** tenga éxito.",
            "Ahorra **de modo que** pueda viajar.",
        ],
    },
    "en effet": {
        "french": [
            "Il est **en effet** le meilleur dans sa classe.",
            "Elle a **en effet** gagné le concours.",
        ],
        "spanish": [
            "Es **en efecto** el mejor de su clase.",
            "Ella ha **en efecto** ganado el concurso.",
        ],
    },
    "en tant que": {
        "french": [
            "**En tant que** médecin, il doit être prudent.",
            "**En tant que** professeur, elle connaît bien les enfants.",
        ],
        "spanish": [
            "**Como** médico, debe ser cuidadoso.",
            "**Como** profesora, conoce bien a los niños.",
        ],
    },
    "jusqu'à ce que": {
        "french": [
            "Il attendra **jusqu'à ce que** elle arrive.",
            "Nous jouerons **jusqu'à ce que** il fasse nuit.",
        ],
        "spanish": [
            "Esperará **hasta que** ella llegue.",
            "Jugaremos **hasta que** anochezca.",
        ],
    },
    "malgré que": {
        "french": [
            "Elle est sortie **malgré qu'**il pleuvait.",
            "Il a réussi **malgré qu'**il ait eu peu de temps pour étudier.",
        ],
        "spanish": [
            "Salió **a pesar de que** llovía.",
            "Tuvo éxito **a pesar de que** tuvo poco tiempo para estudiar.",
        ],
    },
    "plutôt que": {
        "french": [
            "Il choisit de marcher **plutôt que** de courir.",
            "Elle mange des fruits **plutôt que** des bonbons.",
        ],
        "spanish": [
            "Elige caminar **en lugar de** correr.",
            "Come frutas **en lugar de** dulces.",
        ],
    },
    "pour autant que": {
        "french": [
            "Je viendrai **pour autant que** tu me le demandes.",
            "Il participera **pour autant que** les conditions soient remplies.",
        ],
        "spanish": [
            "Vendré **siempre y cuando** me lo pidas.",
            "Participará **siempre y cuando** se cumplan las condiciones.",
        ],
    },
    "tant bien que mal": {
        "french": [
            "Il a fini le projet **tant bien que mal**.",
            "Elle a réussi **tant bien que mal** à ouvrir la porte.",
        ],
        "spanish": [
            "Terminó el proyecto **con dificultad**.",
            "Logró abrir la puerta **a duras penas**.",
        ],
    },
    "tout comme": {
        "french": [
            "Elle aime le cinéma **tout comme** son frère.",
            "Il étudie l'histoire **tout comme** sa sœur.",
        ],
        "spanish": [
            "Le gusta el cine **al igual que** a su hermano.",
            "Estudia historia **al igual que** su hermana.",
        ],
    },
    "vu que": {
        "french": [
            "**Vu qu'**il est tard, nous devrions rentrer.",
            "**Vu que** la salle est pleine, attendons dehors.",
        ],
        "spanish": [
            "**Dado que** es tarde, deberíamos regresar.",
            "**Dado que** la sala está llena, esperemos afuera.",
        ],
        "alt_spanish": [
            "**Considerando que** es tarde, deberíamos regresar.",
            "**Considerando que** la sala está llena, esperemos afuera.",
        ],
    },
    "or": {
        "french": [
            "Il veut acheter une voiture, **or** il n'a pas assez d'argent.",
            "Elle pensait arriver à l'heure, **or** il y avait des embouteillages.",
        ],
        "spanish": [
            "Quiere comprar un coche, **ahora bien**, no tiene suficiente dinero.",
            "Pensaba llegar a tiempo, **sin embargo**, había tráfico.",
        ],
    },
    "quant à": {
        "french": [
            "**Quant à** moi, je préfère le café.",
            "**Quant à** lui, il aime le thé.",
        ],
        "spanish": [
            "**En cuanto a** mí, prefiero el café.",
            "**En cuanto a** él, le gusta el té.",
        ],
    },
    "sachant que": {
        "french": [
            "Il est parti tôt, **sachant que** le trafic serait dense.",
            "Elle a apporté un parapluie, **sachant que** la météo prévoyait de la pluie.",
        ],
        "spanish": [
            "Se fue temprano, **sabiendo que** el tráfico sería denso.",
            "Trajo un paraguas, **sabiendo que** el pronóstico del tiempo preveía lluvia.",
        ],
    },
    "soit ... soit": {
        "french": [
            "**Soit** tu travailles dur, **soit** tu échoueras.",
            "**Soit** nous partons maintenant, **soit** nous manquons le train.",
        ],
        "spanish": [
            "**Sea** que trabajes duro, **sea** que fracases.",
            "**Ya sea** que partamos ahora, **ya sea** que perdamos el tren.",
        ],
    },
    "supposé que": {
        "french": [
            "**Supposé que** tu gagnes la loterie, que ferais-tu?",
            "**Supposé que** elle ne vienne pas, nous devrons commencer sans elle.",
        ],
        "spanish": [
            "**Suponiendo que** ganes la lotería, ¿qué harías?",
            "**Suponiendo que** ella no venga, tendremos que empezar sin ella.",
        ],
    },
    "tout bien considéré": {
        "french": [
            "**Tout bien considéré**, il a décidé de rester.",
            "**Tout bien considéré**, ce n'est pas une mauvaise idée.",
        ],
        "spanish": [
            "**Todo bien considerado**, decidió quedarse.",
            "**Todo bien considerado**, no es una mala idea.",
        ],
    },
    "voire même": {
        "french": [
            "Il pourrait gagner, **voire même** battre le record.",
            "Elle aime les livres, **voire même** les collectionne.",
        ],
        "spanish": [
            "Podría ganar, **incluso** romper el récord.",
            "Le gustan los libros, **incluso** los colecciona.",
        ],
        "alt_spanish": [
            "Podría ganar, **hasta** romper el récord.",
            "Le gustan los libros, **hasta** los colecciona.",
        ],
    },
}

reverse_lookup = {}
for fr_connector, sp_translations in connectors.items():
    for sp_connector in sp_translations:
        reverse_lookup[sp_connector] = fr_connector


def get_random_connector():
    """Select a random connector and its translations."""
    fr_connector, sp_translations = random.choice(list(connectors.items()))
    if random.choice([True, False]):
        return fr_connector, sp_translations, "FR", "ES"
    else:
        return random.choice(sp_translations), [fr_connector], "ES", "FR"


def check_answer(user_answer, correct_answers):
    """Check if the user answer is close to any of the correct answers."""
    for answer in correct_answers:
        if user_answer.lower() == answer.lower():
            return "correct", answer
        elif (
            difflib.SequenceMatcher(None, user_answer.lower(), answer.lower()).ratio()
            > 0.8
        ):
            return "almost", answer
    return "wrong", None


def display_examples(connector, from_lang):
    if from_lang == "ES":
        connector = reverse_lookup.get(connector, connector)

    french_examples = example_phrases[connector]["french"]
    spanish_examples = example_phrases[connector]["spanish"]

    print(Style.BRIGHT + Fore.BLUE + "French Examples:" + Style.RESET_ALL)
    for example in french_examples:
        # Apply bright style only to the connector
        highlighted_example = example.replace("**", Style.BRIGHT, 1).replace(
            "**", Style.RESET_ALL + Fore.BLUE, 1
        )
        print(Fore.BLUE + highlighted_example)

    print(Style.BRIGHT + Fore.CYAN + "Spanish Examples:" + Style.RESET_ALL)
    for example in spanish_examples:
        # Apply bright style only to the connector
        highlighted_example = example.replace("**", Style.BRIGHT, 1).replace(
            "**", Style.RESET_ALL + Fore.CYAN, 1
        )
        print(Fore.CYAN + highlighted_example)

    # Check for alternative Spanish translations
    if "alt_spanish" in example_phrases[connector]:
        alt_spanish_examples = example_phrases[connector]["alt_spanish"]
        print(
            Style.BRIGHT + Fore.CYAN + "Alternative Spanish Examples:" + Style.RESET_ALL
        )
        for example in alt_spanish_examples:
            # Apply bright style only to the connector
            highlighted_example = example.replace("**", Style.BRIGHT, 1).replace(
                "**", Style.RESET_ALL + Fore.CYAN, 1
            )
            print(Fore.CYAN + highlighted_example)


def highlight_differences(user_answer, correct_answer):
    """Highlight the differences between the user's answer and the correct answer."""
    highlighted = ""
    for i, s in enumerate(difflib.ndiff(user_answer, correct_answer)):
        if s[0] == " ":
            highlighted += s[-1]
        elif s[0] == "-":
            highlighted += Fore.RED + Style.BRIGHT + s[-1] + Style.RESET_ALL
        elif s[0] == "+":
            # Skip as these are additions in the correct answer
            continue
    return highlighted


def main():
    while True:
        connector, translations, from_lang, to_lang = get_random_connector()

        print(
            f"Translate {Style.BRIGHT + Fore.YELLOW}'{connector}'{Style.RESET_ALL} from {from_lang} to {to_lang}: ",
            end="",
        )
        user_answer = input().strip()

        check_result, correct_answer = check_answer(user_answer, translations)
        if check_result == "correct":
            print(Style.BRIGHT + Fore.GREEN + "Correct!")
        elif check_result == "almost":
            print(Style.BRIGHT + Fore.YELLOW + "Almost.")
            corrected = highlight_differences(user_answer, correct_answer)
            print(
                "Corrected: "
                + Style.BRIGHT
                + Fore.MAGENTA
                + correct_answer
                + Style.RESET_ALL
            )
            print("Your answer: " + corrected)
        else:
            print(
                Style.BRIGHT
                + Fore.RED
                + "Incorrect."
                + Style.RESET_ALL
                + Fore.MAGENTA
                + " The correct translation(s): "
                + Style.BRIGHT
                + ", ".join(translations)
            )

        display_examples(connector, from_lang)

        print()

        response = input("Try another? (Enter to continue, 'no' to quit): ")
        print("\033[A\033[K", end="")  # Move cursor up and clear line
        if response.lower() in ["no", "n"]:
            break


if __name__ == "__main__":
    main()
