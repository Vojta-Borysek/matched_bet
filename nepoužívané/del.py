from difflib import SequenceMatcher

def similarity_ratio(a, b):
    return SequenceMatcher(None, a, b).ratio()

def merge_lists(list1, list2, threshold=0.7):
    merged_list = []

    for item2 in list2:
        max_similarity = 0
        selected_item1 = None

        for item1 in list1:
            sim = similarity_ratio(item1, item2)

            if sim > threshold and sim > max_similarity:
                max_similarity = sim
                selected_item1 = item1

        if selected_item1:
            merged_list.append(selected_item1)
        else:
            merged_list.append(item2)

    return merged_list

# Example usage:
list1 = [
            'https://www.betano.cz/sport/fotbal/ceska-republika/1-liga/16952/',
            'https://www.betano.cz/sport/fotbal/ceska-republika/2-liga/17460r/',
            'https://www.betano.cz/sport/fotbal/liga-mistru/kvalifikace/195396r/',
            'https://www.betano.cz/sport/fotbal/souteze/evropska-liga/188567/',
            'https://www.betano.cz/sport/fotbal/souteze/evropska-konferencni-liga/189602/',
            'https://www.betano.cz/sport/fotbal/anglie/premier-league/1r/',
            'https://www.betano.cz/sport/fotbal/anglie/efl-cup/10215r/',
            'https://www.betano.cz/sport/fotbal/anglie/championship/2r/',
            'https://www.betano.cz/sport/fotbal/anglie/league-one/527r/',
            'https://www.betano.cz/sport/fotbal/anglie/league-two/4r/',
            'https://www.betano.cz/sport/fotbal/spanelsko/laliga/5r/',
            'https://www.betano.cz/sport/fotbal/spanelsko/segunda-division/10000r/',
            'https://www.betano.cz/sport/fotbal/italie/serie-a/1635r/',
            'https://www.betano.cz/sport/fotbal/italie/serie-b/10210r/',
            'https://www.betano.cz/sport/fotbal/nemecko/bundesliga/216r/',
            'https://www.betano.cz/sport/fotbal/nemecko/2-bundesliga/217r/',
            'https://www.betano.cz/sport/fotbal/nemecko/3-liga/17313r/',
            'https://www.betano.cz/sport/fotbal/francie/ligue-1/215r/',
            'https://www.betano.cz/sport/fotbal/francie/ligue-2/10467r/',
            'https://www.betano.cz/sport/fotbal/portugalsko/primeira-liga/17083r/',
            'https://www.betano.cz/sport/fotbal/portugalsko/liga-2/17385r/',
            'https://www.betano.cz/sport/fotbal/nizozemsko/eredivisie/17067r/',
            'https://www.betano.cz/sport/fotbal/nizozemsko/eerste-divisie/17370r/',
            'https://www.betano.cz/sport/fotbal/turecko/super-lig/17093r/',
            'https://www.betano.cz/sport/fotbal/skotsko/premiership/1647r/',
            'https://www.betano.cz/sport/fotbal/skotsko/ligovy-pohar/10345r/',
            'https://www.betano.cz/sport/fotbal/skotsko/championship/1630r/',
            'https://www.betano.cz/sport/fotbal/skotsko/league-one/1672r/',
            'https://www.betano.cz/sport/fotbal/skotsko/league-two/1673r/'
        ]
list2 = ["https://www.betano.cz/sport/fotbal/souteze/ceska-republika/11338/",
        "https://www.betano.cz/sport/fotbal/souteze/liga-mistru/188566/",
        "https://www.betano.cz/sport/fotbal/souteze/evropska-konferencni-liga/189602/",
        "https://www.betano.cz/sport/fotbal/souteze/anglie/1/",
        "https://www.betano.cz/sport/fotbal/souteze/spanelsko/2/",
        "https://www.betano.cz/sport/fotbal/souteze/italie/87/",
        "https://www.betano.cz/sport/fotbal/souteze/nemecko/24/",
        "https://www.betano.cz/sport/fotbal/souteze/francie/23/",
        "https://www.betano.cz/sport/fotbal/souteze/portugalsko/11382/",
        "https://www.betano.cz/sport/fotbal/souteze/nizozemsko/11376/",
        "https://www.betano.cz/sport/fotbal/souteze/turecko/11384/",
        "https://www.betano.cz/sport/fotbal/souteze/evropska-liga/188567/",
        "https://www.betano.cz/sport/fotbal/souteze/albanie/11317/",
        "https://www.betano.cz/sport/fotbal/souteze/belgie/11324/",
        "https://www.betano.cz/sport/fotbal/souteze/bosna-a-hercegovina/11478/",
        "https://www.betano.cz/sport/fotbal/souteze/bulharsko/11328/",
        "https://www.betano.cz/sport/fotbal/souteze/chorvatsko/11334/",
        "https://www.betano.cz/sport/fotbal/souteze/dansko/11339/",
        "https://www.betano.cz/sport/fotbal/souteze/estonsko/11411/",
        "https://www.betano.cz/sport/fotbal/souteze/finsko/11355/",
        "https://www.betano.cz/sport/fotbal/souteze/gruzie/11436/",
        "https://www.betano.cz/sport/fotbal/souteze/irsko/11367/",
        "https://www.betano.cz/sport/fotbal/souteze/island/10008/",
        "https://www.betano.cz/sport/fotbal/souteze/izrael/11429/",
        "https://www.betano.cz/sport/fotbal/souteze/kypr/11336/",
        "https://www.betano.cz/sport/fotbal/souteze/madarsko/11363/",
        "https://www.betano.cz/sport/fotbal/souteze/malta/11491/",
        "https://www.betano.cz/sport/fotbal/souteze/moldavsko/11442/",
        "https://www.betano.cz/sport/fotbal/souteze/norsko/11378/",
        "https://www.betano.cz/sport/fotbal/souteze/polsko/11381/",
        "https://www.betano.cz/sport/fotbal/souteze/rakousko/11322/",
        "https://www.betano.cz/sport/fotbal/souteze/recko/90/",
        "https://www.betano.cz/sport/fotbal/souteze/rumunsko/11383/",
        "https://www.betano.cz/sport/fotbal/souteze/severni-irsko/11377/",
        "https://www.betano.cz/sport/fotbal/souteze/skotsko/91/",
        "https://www.betano.cz/sport/fotbal/souteze/slovensko/11392/",
        "https://www.betano.cz/sport/fotbal/souteze/slovinsko/11435/",
        "https://www.betano.cz/sport/fotbal/souteze/srbsko/11389/",
        "https://www.betano.cz/sport/fotbal/souteze/svedsko/11393/",
        "https://www.betano.cz/sport/fotbal/souteze/svycarsko/11394/",
        "https://www.betano.cz/sport/fotbal/souteze/ukrajina/11386/",
        "https://www.betano.cz/sport/fotbal/souteze/wales/11433/"]

merged_list = merge_lists(list1, list2, threshold=0.7)
print(merged_list)
