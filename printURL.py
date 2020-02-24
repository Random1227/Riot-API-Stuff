import requests;
import json;

SUM_NAME = 'Random1227';
SUM_ICON = '';
ACC_ID = '';
ACC_LVL = '';

print("Enter Your Summoner Name:");
SUM_NAME = input();



#info = [];

testincrement = 0;
MATCH_ID_ARRAY = [];


API_KEY = 'PUT YOUR PERSONAL API KEY HERE';
URL = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+SUM_NAME+'?api_key='+API_KEY;

#print(URL);
response = requests.get(URL);
info = response.json();
info2 = json.dumps(info);
#print(info);
ACC_ID = info["accountId"];
SUM_ICON = info["profileIconId"];
ACC_LVL = info["summonerLevel"];
print();
print('The account ID for ' + SUM_NAME + ' is ' + ACC_ID);
print('This account is level ' + str(ACC_LVL) +'.');
print();
#https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/' + ACC_ID + '?api_key=' + API_KEY

matchlist = requests.get('https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/' + ACC_ID + '?api_key=' + API_KEY);
#	use this, it is your hero
matchlist1 = matchlist.json();
#	this is a bait, don't fall for it like i did for 30 minutes
MATCH_LIST = json.dumps(matchlist1, sort_keys=True, indent=4);

#print(matchlist1["matches"][1]);

#for match in matchlist1["matches"]:
#	if (match["queue"] == 450) :
#		MATCH_ID_ARRAY.append(match["gameId"]);

print(MATCH_ID_ARRAY);
#want a loop that finds how many different individual champions were played
#be done by
CURCHAMP = 0;
NEXCHAMP = 0;
index = 0;
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


