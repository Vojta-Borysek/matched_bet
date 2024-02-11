from betano_fix import BetanoScraper
from sm import Smarkets
from matcher import Match
from upload_to_drive import UPLOAD

# List of URLs to loop through
betano_urls = [
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


def step1():
    print("started Betano")
    betano_scraper = BetanoScraper(betano_urls)
    bet_data = betano_scraper.scrape_all_urls()
    print("Betano finished")

    print("started Smarkets")
    sma_data = Smarkets().smarkets()
    print("Smarkets finished")

    print("started Matching")
    Match().match_sim(bet_data, sma_data)
    print("Matching finished")

    print("started uploading")
    UPLOAD().run_me()
    print("Uploading finished")
