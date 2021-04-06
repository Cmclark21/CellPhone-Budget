#!/usr/bin/env python
# coding: utf-8

# # Project Coding

# ### Importing Pandas and our data

# In[4]:


import pandas as pd
df = pd.read_csv('results.csv')


# ### Checking how our data looks like.

# In[5]:


df.head()


# ### Creating a list of all the teams that have ever played in the premier league in the past 12 years

# In[6]:


home_team_list = []
for team in df.home_team:
    if team not in home_team_list:
        home_team_list.append(team)
    else:continue
print(home_team_list)
print(len(home_team_list))


# In[7]:


df1 = df[((df["home_team"] == "Arsenal")& (df["away_team"]== "Manchester United"))]
df1


# In[8]:


df2 = df[((df["home_team"] == "Manchester United")& (df["away_team"]== "Arsenal"))]
df2


# ### This is the number of times team 1 / Arsenal won

# In[9]:


team_1_wins = 0
for outcome in df1.result:
    if outcome == "H":
        team_1_wins += 1
    #else:continue
for outcome in df2.result:
    if outcome == "A":
        team_1_wins += 1
    #else:continue
print (team_1_wins)


# ### This is the number of times team 2  / Manchester United won

# In[10]:


team_2_wins = 0
for outcome in df1.result:
    if outcome == "A":
        team_2_wins += 1
    else:continue
for outcome in df2.result:
    if outcome == "H":
        team_2_wins += 1
    else:continue
print (team_2_wins)


# ### This is the number of draws between the two teams. 

# In[11]:


draws = 0
for outcome in df1.result:
    if outcome == "D":
        draws += 1
    else:continue
for outcome in df2.result:
    if outcome == "D":
        draws += 1
    else:continue
print (draws)


# ### This is the total number of times the two teams have played against each other

# In[12]:


total_games = draws + team_1_wins + team_2_wins
print(total_games)


# ### Creating a function that does all the above for whatever teams that a user wants to compare

# In[13]:


def game_predictor(team_1,team_2):
    df1 = df[((df["home_team"] == team_1)& (df["away_team"]== team_2))]
    df2 = df[((df["home_team"] == team_2)& (df["away_team"]== team_1))]
    team_1_wins = 0
    team_2_wins = 0
    draws = 0
    
    for outcome in df1.result:
        if outcome == "H":
            team_1_wins += 1
    for outcome in df2.result:
        if outcome == "A":
            team_1_wins += 1
        
            
    for outcome in df1.result:
        if outcome == "A":
            team_2_wins += 1
    for outcome in df2.result:
        if outcome == "H":
            team_2_wins += 1
        
            
    for outcome in df1.result: 
        if outcome == "D":
            draws += 1
    for outcome in df2.result:
        if outcome == "D":
            draws += 1
            
    total_games = draws + team_1_wins + team_2_wins
    
    if total_games == 0:
        print('There is no past record for these 2 teams playing in the past 12 years')
    else:
        print(team_1, 'and', team_2, "have played", total_games, 'games in the past 12 years.')
        print(team_1, " has won a total of", str(team_1_wins), " times ") 
        print(team_2, " has won a total of ", str(team_2_wins), " times ")
        print('They have drawed ',draws, " times")
    
    
    


# ### Getting User Input for the teams to be compared and Calling out function

# In[ ]:


first_team = input("Enter the first team name: ") #could enter who is the home team here
if first_team not in home_team_list:
    print('This team is not in Premier League, try another team:') 
second_team = input("Enter the second team name: ") #could enter who is the away team
if second_team not in home_team_list:
    print('This team is not in Premier League, try another team:')
     
game_predictor(first_team, second_team)   #display line graph of two teams who play home and away then add a unit for
#one win and two units for two wins in a season


# In[ ]:





# In[ ]:





# In[ ]:




