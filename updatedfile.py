
#these are the magic words that make stuff do the thing
import requests;
import json;
#variable declaration
#honestly, not super sure how data types work in python, but all but thats what googling errors is for
SUM_NAME = 'Random1227';
SUM_ICON = '';
ACC_ID = '';
ACC_LVL = '';
#the first line in the command line, tells the user to enter the name. I'm using this to show that it works with any summoner name input
print("Enter Your Summoner Name:");
#this sets the variable SUM_NAME equal to the next thing that the user puts in the command line
#this is actually a somewhat dangerous way to go about it, because there is something with RIOT API where they blacklist you if you search for nonexistent summoners too often
SUM_NAME = input();



#info = [];

testincrement = 0;
MATCH_ID_ARRAY = [];

#used to collect the magic from the API, this is changed every 24 hours, and you should use your own personal one anyway
API_KEY = 'RGAPI-28737401-375e-490b-afea-86b1196f6ba9';
#builds up the URL for the first request from the server, which returns the account info
#there could be an argument that you could spell this out in a much more modular way, such as having an array of every possible URL, but honestly not sure if that is better or not
URL = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+SUM_NAME+'?api_key='+API_KEY;


#These next three lines are where the magic happens. The first takes the URL, gets the info from it, and puts it into the response variable
responseSUMINFO = requests.get(URL);
#this takes the response, parses it as a json and puts it into the info variable
info = responseSUMINFO.json();
#this is the final step to allow the info to be easily readable by python, using json.dumps() puts the info into a way that works
info2 = json.dumps(info);
#Unfortunately, I don't know exactly how it works, I just know that it works.

#this takes the stuff from the json named info, and specifically takes the accountId portion of it, and gives it to the variable ACC_ID
ACC_ID = info["accountId"];
#same as above
SUM_ICON = info["profileIconId"];
#same as above
ACC_LVL = info["summonerLevel"];
#the two prints at just formatting to make it nicer to view, the rest is simple outputs with print()
print();
print('The account ID for ' + SUM_NAME + ' is ' + ACC_ID);
#in python, you can't concatonate strings and ints together, so you must do str() in order to change the ACC_LVL (integer) into a string
print('This account is level ' + str(ACC_LVL) +'.');
print();

#	Alright, now we enter the wild west of not knowing what to do
#		Current goals:
#			1.0 Be able to identify champions played(DONE), how many times played in the last 100 games
#			2.0 Once I have the specific champions, I can begin figuring out the different formulas that will need to be done to compare the secondary rune effectiveness
#			3.0 Some kind of graphical interface/website integration
#				3.1 Website integration is the hope, because I actually do know at least the bare minimum HTML, CSS, and JavaScript to create some kind of website
#			4.0 CS/XP/Gold differentials between opponents at specific time intervals
#				4.1 Allow you to view a game and see why you were less effective in collecting gold/cs/xp during specific stages of the game
#				4.2 Could especially be helpful if we ever wanted to clash more often and needed to learn how to not ARAM mid-late game

#this will give champion INFO
responseCHAMPS = requests.get('https://ddragon.leagueoflegends.com/cdn/10.4.1/data/en_US/champion.json');
champlist = responseCHAMPS.json()
CHAMP_LIST = json.dumps(champlist);
champlistdata = champlist['data'];



#This successfully creates 2 arrays where each index can be translated to the appropiate name of the champion from the key given
CHAMP_KEY = [];
CHAMP_ID = [];
for champ in champlistdata:
	CHAMP_KEY.append(champlistdata[champ]['key']);
	CHAMP_ID.append(champlistdata[champ]['name']);
#print(CHAMP_ID[100]);
#print(CHAMP_KEY[100]);

#Next thing to do is print out the last 100 champions played by name instead of by key
matchlist = requests.get('https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/' + ACC_ID + '?api_key=' + API_KEY);
#	use this, it is your hero
matchlist1 = matchlist.json();
#	this is a bait, don't fall for it like i did for 30 minutes
MATCH_LIST = json.dumps(matchlist1, sort_keys=True, indent=4);

#print(matchlist1["matches"][1]);

#for match in matchlist1["matches"]:
#	if (match["queue"] == 450) :
#		MATCH_ID_ARRAY.append(match["gameId"]);

#print(MATCH_ID_ARRAY);
#want a loop that finds how many different individual champions were played
#be done by

CHAMPS_PLAYED = [];
CHAMPION_ID = '';
x=0;
for match in matchlist1["matches"]:
	CHAMPION_ID = match['champion'];
	for key in CHAMP_KEY:
		if (str(CHAMPION_ID) == str(key)):
			x = CHAMP_KEY.index(key);
			CHAMPS_PLAYED.append(CHAMP_ID[x]);

print('CHAMPS_PLAYED IS: '+str(len(CHAMPS_PLAYED))+' items long');

print(CHAMPS_PLAYED);

CHAMPS_PLAYED.sort();
print(CHAMPS_PLAYED);
#for x = 0 to len(CHAMPS_PLAYED-1):
#	if (CHAMPS_PLAYED[x] == CHAMPS_PLAYED[x+1]):
		
		






