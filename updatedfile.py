#Updated 2/25/20
#Main difference between this and the other file is I added better commenting to the majority of it. 
#This is the file I will be keeping updated, for no other reason than I am bad at letting go of ugly past programs.

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
API_KEY = 'RGAPI-3ca84c5e-487d-45e9-9607-aa4de10ba968';
#builds up the URL for the first request from the server, which returns the account info
#there could be an argument that you could spell this out in a much more modular way, such as having an array of every possible URL, but honestly not sure if that is better or not
URL = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+SUM_NAME+'?api_key='+API_KEY;


#These next three lines are where the magic happens. The first takes the URL, gets the info from it, and puts it into the response variable
response = requests.get(URL);
#this takes the response, parses it as a json and puts it into the info variable
info = response.json();
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
#https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/' + ACC_ID + '?api_key=' + API_KEY


#this will give champion INFO
asdfjkl = requests.get('https://ddragon.leagueoflegends.com/cdn/10.4.1/data/en_US/champion.json');
champlist = asdfjkl.json()
CHAMP_LIST = json.dumps(champlist);
#print(CHAMP_LIST);
champlistdata = champlist['data'];
#print(champlistdata['aatrox']);

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

x = 0;
CHAMPS_PLAYED = [];
for match in matchlist1["matches"]:
	CHAMPS_PLAYED.append(match['champion']);
	x = x + 1;
#print(CHAMPS_PLAYED.sort());
print(x);
		#yo i dont' freakin know just work please

CHAMPS_PLAYED.sort();
#print(CHAMPS_PLAYED);

print(CHAMPS_PLAYED);


