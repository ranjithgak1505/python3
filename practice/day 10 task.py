developer={"frontent":"html","backent":"python","sql":"mysql"}
x=developer.get("sql")
print(x)

developer={"frontent":"html","backent":"python","sql":"mysql"}
developer.update({"testing":"selinium"})
print(developer)

developer={"frontent":"html","backent":"python","sql":"mysql","testing":"selinium"}
developer.pop("frontent")
print(developer)

developer={"backent":"python","sql":"mysql","testing":"selinium"}
developer.update({"sql":"postgresql"})
print(developer)


developer={"backent":"python","sql":"postgresql","testing":"selinium"}
for x in developer:
 print(developer[x])


team1={"name":"csk","caption":"msd"}
team2={"name":"rcb","caption":"faf"}
team3={"name":"mi","caption":"rohit"}
ipl_teams={
      "team1":team1,
      "team2":team2,
      "team3":team3
      }
print(team1["caption"])
 
