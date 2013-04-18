# Grabs stats from Victoria Fantasy Hockey League
from bs4 import BeautifulSoup
import urllib2
import simplejson as json
import os
import time

json_file = 'static/data.json'

def write_json():
	json_dict = {}
	with open(json_file, 'w+') as outfile:
		for i in everybody:
			json_dict[str(i['name'])] = i
		outfile.write(json.dumps(json_dict))
	return json.dumps(json_dict)

def age_of_json():
	'''
	Determines the age of the JSON file.
	'''
	t = os.path.getmtime(json_file)
	return time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(t))

def what_if_penalties():
	print "Alternative penalties score!  What if they were negative instead of positive points?"
	for i in everybody:
		print i.name, "new score:", i.points - i.pim*2

def download_page():
	output = open('output.html', 'w+')
	output.write(soup.encode('utf8'))
	return True

def load_data(team):
	'''
	Puts all the teams stats in a list. Team should be an int 0-9.  Returns a list.
	Order of items in list is:
		0: Overall rank 1: Team name 2: Goals 3: Assists 4: PIM 5: SHG 6: PPP
		7: W 8:GA 9: SV 10: SO 11: Total pts 12: sorting number 13: total change	
	'''
	stats_list = []
	for string in raw_list[team].strings:
		stats_list.append(string)
	
	#Deletes empty values in list - formatting issues from BeautifulSoup
	del stats_list[2]
	del stats_list[7]
	del stats_list[11]

	return stats_list

class Team:
	'''
	DEPRECEATED.  Replaced with create_team_dict()
	'''
	def __init__(self, rank, name, goals, assists, pim, shg, ppp, wins, ga, sv, so, points, sorting, change):
		self.rank = rank
		self.name = name
		self.goals = goals
		self.assists = assists
		self.pim = pim
		self.shg = shg
		self.ppp = ppp
		self.wins = wins
		self.ga = ga
		self.sv = sv
		self.so = so
		self.points = points
		self.sorting = sorting #Unsure of what this number is for, it's from ESPN
		self.change = change

def setup_teams(team):
	'''
	DEPRECEATED
	Creates an instance of the Team class.  
	The order of the return correlate to the class attributes.
	'''
	x = load_data(team)
	return Team(int(x[0]), x[1], int(x[2]), int(x[3]), float(x[4]), int(x[5]), int(x[6]), int(x[7]), int(x[8]), float(x[9]), int(x[10]), float(x[11]), x[12], float(x[13]))

def create_team_dict(input):
	'''
	Instead of setup_teams which creates a class instance, it creates a dictionary.
	Easier to import across modules? Should still work with JSON.
	'''
	team = load_data(input)
	d = {}
	d['rank'] = team[0]
	d['name'] = team[1]
	d['goals'] = team[2]
	d['assists']= team[3]
	d['pim']= team[4]
	d['shg']= team[5]
	d['ppp']= team[6]
	d['wins']= team[7]
	d['ga']= team[8]
	d['sv']= team[9]
	d['so']= team[10]
	d['points']= team[11]
	d['sorting']= team[12]
	d['change']= team[13]
	return d


#The link below is to the 'official' team stats, which only update at the end of the day after games are done playing.
soup = BeautifulSoup(urllib2.urlopen('http://games.espn.go.com/fhl/standings?leagueId=39372&view=official').read())

#Having huge troubles getting any other searches to work properly, might have to make do with this.
bg_sort_a, bg_sort_b = soup.find_all(bgcolor="#f4f1e8"), soup.find_all(bgcolor='#f7f8f2')
raw_list = list(bg_sort_a) + list(bg_sort_b)
#Each list, _a and _b, both duplicate themselves.  Items 0-4 are also 5-9. 

live_soup = BeautifulSoup(urllib2.urlopen('http://games.espn.go.com/fhl/standings?leagueId=39372&view=live').read())

#Instead of using BeautifulSoup, will attempt to use the ESPN API
#http://developer.espn.com/blog/read/20120905_football
#API Key:  x4ywrm5qwd352zf59unnecdc
#FUCKING ESPN WANTS ME TO PAY?!  FUCK THE API.


Brandon = create_team_dict(0)
Kevin = create_team_dict(1)
Connor = create_team_dict(2)
Adam = create_team_dict(3)
Cam = create_team_dict(4)
#Because raw_list and bg_sort_x are fucked up, it jumps around now: 
Ryan = create_team_dict(10)
Max = create_team_dict(11)
Keegan = create_team_dict(12)
Luke = create_team_dict(13)
Dwayne = create_team_dict(14)

everybody = [Brandon, Kevin, Connor, Adam, Cam, Ryan, Max, Keegan, Luke, Dwayne]
write_json()



