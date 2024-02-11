from difflib import SequenceMatcher
import sys


class Match:
    def similar(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

    def remove_duplicates(self, filename):
        try:
            # Try to open the file in read mode
            with open(filename, 'r', encoding='utf-8') as file:
                # Read all lines from the file
                lines = file.readlines()

            # Use a set to store unique lines while preserving their order
            unique_lines = []

            # Iterate through lines, adding them to the set if not already present
            for line in lines:
                if line not in unique_lines:
                    unique_lines.append(line)

            # Write the unique lines back to the file
            with open(filename, 'w', encoding='utf-8') as file:
                file.writelines(unique_lines)
                # print(f"Removed duplicates from '{filename}'.")

        except FileNotFoundError:
            # If the file doesn't exist, print an error message
            print("Error: The file does not exist.")

    def check_and_add_lines(self, existing_file, lines_to_check_file):
        try:
            # Try to open the existing file in read mode
            with open(existing_file, 'r', encoding='utf-8') as file:
                # Read all lines from the existing file
                existing_lines = file.readlines()

            # Try to open the file containing lines to check in read mode
            with open(lines_to_check_file, 'r', encoding='utf-8') as lines_file:
                # Read all lines from the lines_to_check file
                lines_to_check = lines_file.readlines()

            # Check each line in lines_to_check and add it to the existing file if not present
            for line_to_check in lines_to_check:
                if line_to_check not in existing_lines:
                    with open(existing_file, 'a', encoding='utf-8') as file:
                        file.write(line_to_check)
                        # print(f"Added '{line_to_check.strip()}' to '{existing_file}'.")
                else:
                    pass
                    # print(f"'{line_to_check.strip()}' already exists in '{existing_file}'.")

        except FileNotFoundError:
            # If either file doesn't exist, print an error message
            print("Error: One of the files does not exist.")

    def match_sim(self, data1, data2):
        # data1 = ['Estoril-Praia - Rio Ave', ['2.94', '3.25', '2.92'], 'Le Mans FC - Dijon FCO', ['2.62', '4.1', '3.7'], 'FC Porto - Farense', ['1.18', '9.2', '29'], 'FC Sudtirol - Spezia', ['3.95', '3.25', '2.44'], 'Swindon Town - Arsenal U21', ['2.7', '4.8', '3.15'], 'AC Ajaccio - Girondins de Bordeaux', ['3.2', '3.3', '2.9'], 'Cittadella - Reggiana', ['2.2', '3.35', '4.4'], 'Vizela - Futebol Clube de Arouca', ['2.34', '3.5', '3.85'], 'Walsall - Brighton U21', ['2.7', '4.7', '3.2'], 'Lille OSC - FC Nantes', ['1.55', '5.7', '9.4'], 'Parma - Feralpisalo', ['1.61', '4.2', '7.8'], 'FC Lorient - OGC Nice', ['3.55', '3.55', '2.36'], 'Famalicão - Moreirense FC', ['2', '3.6', '4.6'], 'Venezia - Como', ['2.26', '3.6', '3.8'], 'Stockport County - Manchester United U21', ['2.4', '4.7', '3.25'], 'MVV Maastricht - FC Eindhoven', ['ASK', 'ASK', 'ASK'], 'Sampdoria - Pisa', ['1.99', '4.4', '6'], 'Le Havre AC - Stade Brestois 29', ['3', '3.3', '2.84'], 'Portsmouth - Fulham U21', ['1.94', '5.3', '5.1'], 'Club Football Estrela - Estoril-Praia', ['3.1', '3.5', '3.5'], 'Reading U21 - Crystal Palace U21', ['3.3', '4.5', '2.24'], 'Stade Reims - Clermont Foot', ['2.04', '3.85', '4.4'], 'Jong Ajax - De Graafschap', ['3.1', '4.6', '2.36'], 'Rakow Czestochowa - FC København', ['2.54', '3.5', '3.25'], 'Eintracht Braunschweig - FC Schalke 04', ['3.9', '4', '2.16'], 'Hearts - Partick Thistle', ['1.88', '4.2', '4.8'], 'AS Roma - Salernitana', ['1.63', '4.1', '7.4'], 'Jong FC Utrecht - FC Groningen', ['6.4', '5.1', '1.64'], 'AS Monaco - RC Strasbourg', ['1.84', '4.3', '4.6'], 'Rangers - PSV Eindhoven', ['2.86', '3.75', '2.72'], 'Holstein Kiel - 1. FC Magdeburg', ['2.4', '4.1', '3.15'], 'Sassuolo - Atalanta', ['3.85', '3.85', '2.14'], 'Hibernian - Raith Rovers', ['1.65', '4.7', '6.4'], 'RC Lens - Stade Rennais', ['2.58', '3.75', '3'], 'Royal Antwerp - AEK Athens', ['2.42', '5.1', '4.9'], 'VfL Osnabrück - 1. FC Nürnberg', ['2.5', '3.65', '3.3'], 'FC Hradec Králové - FC Fastav Zlín', ['1.94', '4.6', '4.2'], 'Lecce - Lazio', ['4', '3.35', '2.24'], 'Kilmarnock - Celtic', ['10.5', '6.2', '1.4'], 'FC Nantes - AS Monaco', ['3.85', '4.4', '2.08'], 'Maccabi Haifa - BSC Young Boys', ['2.54', '3.75', '3'], 'Udinese - Juventus', ['4.2', '3.5', '2.12'], 'FC Viktoria Plzen - SK Sigma Olomouc', ['1.59', '5.1', '6.6'], 'FC Schalke 04 - Holstein Kiel', ['1.85', '5.5', '1,000'], 'Molde - Galatasaray SK', ['2.96', '3.7', '2.6'], 'Torino - Cagliari', ['1.75', '3.95', '6.2'], 'SK Ceské Budejovice - Bohemians 1905', ['3.1', '4.1', '2.4'], 'SC Paderborn 07 - 1. FC Kaiserslautern', ['2.14', '4.6', '3.6'], 'Braga - Panathinaikos', ['1.76', '3.95', '6.2'], 'Bologna - AC Milan', ['4.3', '3.7', '2.06'], 'SK Slavia Praha - FC Baník Ostrava', ['1.35', '7.2', '12.5'], 'Norwich City - Millwall', ['2.04', '3.9', '4.4'], 'Hull City - Bristol City', ['2.6', '3.75', '3.25'], 'Union Berlin - 1. FSV Mainz 05', ['2.22', '3.55', '3.9'], 'Eintracht Frankfurt - SV Darmstadt 98', ['1.48', '5.2', '8'], 'RB Leipzig - VfB Stuttgart', ['1.54', '5', '7.4']]
        # data2 = ['SFC Opava - SK Sigma Olomouc B', ['1.83', '3.45', '3.95'], 'Burton Albion - Bolton', ['3.65', '3.50', '1.93'], 'FC Vysocina Jihlava - MFk Chrudim', ['1.80', '3.45', '4.05'], 'Cheltenham - Northampton Town', ['2.25', '3.30', '3.00'], 'Exeter City - Reading FC', ['2.18', '3.20', '3.25'], '1. FK Příbram - FK Dukla Praha', ['2.70', '3.40', '2.37'], 'Leyton Orient - Cambridge United', ['2.30', '3.20', '3.00'], 'MFK Vyškov - AC Sparta Praha B', ['1.62', '3.80', '4.75'], '1. SK Prostějov - FC Zbrojovka Brno', ['3.45', '3.40', '1.98'], 'Lincoln City - Blackpool FC', ['2.65', '3.20', '2.55'], 'Norwich City - Millwall FC', ['2.98', '3.70', '3.70'], 'SK Líšeň - SK Hanácká Slavia Kroměříž', ['1.90', '3.45', '3.65'], 'Port Vale - Carlisle United', ['1.98', '3.35', '3.60'], 'Hull City - Bristol City', ['2.42', '3.45', '2.90'], 'Stevenage Borough - Portsmouth FC', ['2.65', '3.25', '2.52'], 'FK Viktoria Žižkov - FC Vlašim', ['2.15', '3.30', '3.10'], 'Southampton FC - Queens Park Rangers', ['1.39', '4.90', '7.80'], 'Wigan - Barnsley FC', ['2.37', '3.40', '2.75'], 'FK Varnsdorf - Táborsko', ['2.55', '3.05', '2.72'], 'Preston - Swansea City', ['2.55', '3.45', '2.70'], 'Fleetwood Town - Shrewsbury', ['2.07', '3.20', '3.55'], 'Bristol Rovers - Wycombe', ['2.18', '3.30', '3.15'], 'Slavia - FC Zorya Luhansk', ['1.28', '5.90', '10.25'], 'Rotherham - Leicester', ['5.80', '4.10', '1.57'], 'Plzeň - SK Sigma Olomouc', ['1.55', '4.35', '5.70'], 'Oxford Utd - Charlton', ['1.75', '3.70', '4.20'], 'BK Hacken - Aberdeen FC', ['1.87', '3.70', '4.10'], 'Birmingham - Plymouth Argyle', ['2.02', '3.45', '3.80'], 'Olimpija Ljubljana - Qarabağ FK', ['2.80', '3.20', '2.62'], 'Peterborough - Derby County', ['2.67', '3.20', '2.55'], 'Hr. Králové - FC Trinity Zlin', ['1.88', '3.75', '4.00'], 'Coventry City - Sunderland', ['2.10', '3.70', '3.30'], 'PFC Ludogorets Razgrad - AFC Ajax', ['4.05', '3.95', '1.82'], 'SK Dynamo České Budějovice - Bohemians 1905', ['2.90', '3.55', '2.37'], 'Ipswich Town - Leeds United', ['2.18', '3.25', '3.50'], 'GNK Dinamo Zagreb - AC Sparta Praha', ['2.12', '3.50', '3.45'], 'Slavia - Ostrava', ['1.32', '5.70', '8.50'], 'Real Oviedo - Racing Ferrol', ['2.02', '3.10', '4.30'], 'Union Saint-Gilloise - FC Lugano', ['1.65', '4.10', '5.00'], 'Cardiff City - Sheffield Wednesday', ['2.15', '3.25', '3.55'], 'FC Trinity Zlin - Teplice', ['2.35', '3.30', '3.10'], 'Aston Villa - Everton FC', ['1.75', '3.85', '4.55'], 'Sporting Gijon - CD Mirandes', ['1.83', '3.35', '4.85'], 'Millwall FC - Stoke City', ['2.18', '3.35', '3.40'], 'SK Slovan Bratislava - Aris Limassol', ['2.27', '3.40', '3.15'], 'Pardubice - Slovácko', ['3.20', '3.50', '2.22'], 'West Ham United - Chelsea FC', ['3.60', '3.60', '2.12'], 'Albacete Balompie - SD Amorebieta', ['1.65', '3.55', '6.30'], 'Ostrava - SK Dynamo České Budějovice', ['1.62', '4.15', '5.10'], 'Huddersfield Town - Norwich City', ['3.45', '3.35', '2.15'], 'KI Klaksvik - FC Sheriff Tiraspol', ['3.45', '3.35', '2.15'], 'FC Crystal Palace - Arsenal FC', ['5.40', '4.15', '1.60'], 'Villarreal CF B - CD Eldense', ['2.32', '3.25', '3.20'], 'West Bromwich Albion - Middlesbrough FC', ['2.25', '3.45', '3.15'], 'Bohemians 1905 - Hr. Králové', ['1.88', '3.50', '4.30'], 'Linzer ASK - Zrinjski Mostar', ['1.55', '4.35', '5.70'], 'Rakow Czestochowa - FC Kodaň', ['2.45', '3.35', '2.95'], 'Chelsea FC - Luton Town', ['1.23', '6.40', '12.00'], 'SD Huesca - CD Tenerife', ['2.92', '2.82', '2.82'], 'Watford FC - Blackburn Rovers', ['2.07', '3.50', '3.50'], 'AFC Bournemouth - Tottenham Hotspur', ['3.45', '3.90', '1.98'], 'FC Cartagena - Levante UD', ['2.72', '3.30', '2.67'], 'Olympiacos Piraeus - FK Cukaricki', ['1.45', '4.30', '7.80'], 'Jablonec - Slavia', ['8.00', '5.00', '1.38'], 'Rangers FC - PSV Eindhoven', ['2.70', '3.45', '2.57'], 'Arsenal FC - Fulham FC', ['1.23', '6.50', '12.00'], 'SK Sigma Olomouc - Liberec', ['2.12', '3.45', '3.50'], 'Burgos CF - Real Oviedo', ['2.60', '3.10', '2.90'], 'Royal Antwerp FC - AEK Atény', ['2.18', '3.50', '3.25'], 'Brentford FC - FC Crystal Palace', ['1.91', '3.75', '3.85'], 'FK Mladá Boleslav - Plzeň', ['3.30', '3.30', '2.25'], 'CD Tenerife - Real Zaragoza', ['2.05', '3.25', '3.90'], 'Maccabi Haifa - BSC Young Boys', ['2.37', '3.50', '2.92'], 'Manchester United - Nottingham Forest', ['1.33', '5.40', '8.75'], 'Elche CF - Villarreal CF B', ['1.75', '3.50', '5.20'], 'AC Sparta Praha - MFK Karvina', ['1.18', '7.10', '16.00'], 'Molde FK - Galatasaray SK', ['2.80', '3.40', '2.52'], 'Real Valladolid - AD Alcorcon', ['1.72', '3.45', '5.50'], 'Everton FC - Wolverhampton Wanderers', ['2.20', '3.35', '3.40'], 'SC Braga - Panathinaikos', ['1.70', '3.50', '5.80'], 'Racing Ferrol - Sporting Gijon', ['2.37', '3.15', '3.20'], 'Brighton and Hove Albion - West Ham United', ['1.50', '4.60', '6.20'], 'Fulham FC - Tottenham Hotspur', ['3.10', '3.60', '2.22'], 'SD Amorebieta - FC Andorra', ['3.95', '3.05', '2.12'], 'Burnley FC - Aston Villa', ['3.45', '3.55', '2.10'], 'Birmingham - Cardiff City', ['2.15', '3.30', '3.20'], 'CD Mirandes - RCD Espanyol', ['3.25', '3.15', '2.35'], 'Bolton - Middlesbrough FC', ['2.70', '3.45', '2.40'], 'Sheffield United - Manchester City', ['15.00', '6.50', '1.21'], 'CD Leganes - Albacete Balompie', ['2.32', '3.20', '3.30'], 'Bristol City - Norwich City', ['2.47', '3.40', '2.62'], 'Newcastle United - Liverpool FC', ['2.15', '4.05', '3.00'], 'CD Eldense - SD Eibar', ['3.35', '3.05', '2.35'], 'Exeter City - Stevenage Borough', ['2.05', '3.50', '3.25'], 'Racing Santander - SD Huesca', ['2.02', '3.15', '4.15'], 'Luton Town - Gillingham FC', ['1.30', '5.10', '9.00'], 'AFC Wimbledon - Forest Green Rovers', ['2.15', '3.35', '3.15'], 'Newport County - Brentford FC', ['6.70', '4.45', '1.42'], 'Barrow FC - Wrexham FC', ['2.65', '3.30', '2.50'], 'Plymouth Argyle - FC Crystal Palace', ['3.50', '3.55', '1.95'], 'Bradford City - Crewe Alexandra', ['1.57', '3.95', '5.40'], 'Port Vale - Crewe Alexandra', ['1.72', '3.70', '4.35'], 'Gillingham FC - Colchester United', ['2.10', '3.10', '3.55'], 'Portsmouth FC - Peterborough', ['2.02', '3.50', '3.30'], 'Harrogate Town - Morecambe FC', ['2.45', '3.30', '2.72'], 'Sheffield Wednesday - Mansfield Town', ['1.47', '4.25', '6.00'], 'MK Dons - Doncaster', ['1.75', '3.60', '4.35'], 'Stoke City - Rotherham', ['1.65', '3.75', '4.75'], 'Mansfield Town - Stockport County', ['2.25', '3.25', '3.05'], 'Swansea City - AFC Bournemouth', ['3.05', '3.50', '2.15'], 'Newport County - Sutton United', ['2.10', '3.30', '3.35'], 'Tranmere - Leicester', ['4.35', '3.75', '1.70'], 'Notts County - Tranmere', ['1.65', '3.80', '4.85'], 'Wolverhampton Wanderers - Blackpool FC', ['1.37', '4.55', '7.70'], 'Salford City - Accrington Stanley', ['1.91', '3.40', '3.85'], 'Wrexham FC - Bradford City', ['2.10', '3.40', '3.20'], 'Swindon - Crawley Town', ['1.87', '3.65', '3.70'], 'Wycombe - Sutton United', ['1.75', '3.70', '4.20'], 'Walsall FC - Grimsby Town', ['2.40', '3.10', '2.92'], 'Reading FC - Ipswich Town', ['2.77', '3.40', '2.37'], 'Salford City - Leeds United', ['4.15', '3.80', '1.75'], 'Nottingham Forest - Burnley FC', ['2.15', '3.55', '3.35'], 'Chelsea FC - AFC Wimbledon', ['1.14', '6.80', '17.00'], 'Harrogate Town - Blackburn Rovers', ['4.20', '3.70', '1.75'], 'Sheffield United - Lincoln City', ['1.42', '4.50', '6.50'], 'Doncaster - Everton FC', ['8.00', '4.60', '1.35']]
        print(data1)
        print(data2)
        similar_low_odds_teams = []
        for i in range(0, len(data1), 2):
            team1 = data1[i]
            odds1 = data1[i + 1]

            for j in range(0, len(data2), 2):
                team2 = data2[j]
                odds2 = data2[j + 1]

                similarity = self.similar(team1, team2)


                # Check odds condition
                try:
                    if similarity > 0.8:
                        try:
                            if float(odds1[0]) > float(odds2[0]) or float(odds1[1]) > float(odds2[1]) or float(odds1[2]) > float(odds2[2]):
                                # print(odds1)
                                similar_low_odds_teams.append((team1, odds1, team2, odds2, similarity))
                        except:
                            pass
                except:
                    pass

        # print(data1)
        # print(data2)

        original_stdout = sys.stdout  # Save a reference to the original standard output

        with open('Matched.txt', 'w', encoding="utf-8") as ff:
            sys.stdout = ff  # Change the standard output to the file we created.
            for team1, odds1, team2, odds2, similarity in similar_low_odds_teams:
                if odds2 != [' ', ' ', ' ']:
                    print(f"Betano-'{team1}' {odds1} ### Smarkets-'{team2}' {odds2}")
            sys.stdout = original_stdout  # Reset the standard output to its original value

        self.remove_duplicates('Matched.txt')

        existing_file = 'today_football.txt'
        lines_to_check_file = 'Matched.txt'
        self.check_and_add_lines(existing_file, lines_to_check_file)

