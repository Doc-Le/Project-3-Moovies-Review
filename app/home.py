import logging
# from app import (app, mongo)
from app import app
from flask import render_template

@app.route("/")
def main_page():
    #movies = mongo.db.movies.find({})
    movies=  [
        {
            "adult": False,
            "backdrop_path": "/tmpY6f0Lf7Dnx6inByjvHby4AYf.jpg",
            "genre_ids": [
                35,
                18
            ],
            "id": 454283,
            "original_language": "en",
            "original_title": "Action Point",
            "overview": "A daredevil designs and operates his own theme park with his friends.",
            "popularity": 11.214,
            "poster_path": "/5lqJx0uNKrD1cEKgaqF1LBsLAoi.jpg",
            "release_date": "2018-06-01",
            "title": "Action Point",
            "video": False,
            "vote_average": 5.4,
            "vote_count": 252
        },
        {
            "adult": False,
            "backdrop_path": "/bumIpNTKmLY380bruTgIDTrXfpZ.jpg",
            "genre_ids": [
                12,
                14,
                28,
                35,
                10751
            ],
            "id": 9593,
            "original_language": "en",
            "original_title": "Last Action Hero",
            "overview": "Danny is obsessed with a fictional movie character action hero Jack Slater. When a magical ticket transports him into Jack's latest adventure, Danny finds himself in a world where movie magic and reality collide. Now it's up to Danny to save the life of his hero and new friend.",
            "popularity": 12.722,
            "poster_path": "/yTfjHPqh7C7bkfMtEKx2mPdorQw.jpg",
            "release_date": "1993-06-18",
            "title": "Last Action Hero",
            "video": False,
            "vote_average": 6.4,
            "vote_count": 1910
        },
        {
            "adult": False,
            "backdrop_path": "/bE6SwIJrDuDchsXXoE2njVFu795.jpg",
            "genre_ids": [
                16,
                35,
                10751
            ],
            "id": 10715,
            "original_language": "en",
            "original_title": "Looney Tunes: Back in Action",
            "overview": "Fed up with all the attention going to Bugs Bunny, Daffy Duck quits Hollywood, teams up with recently-fired stuntman Damien Drake Jr. and embarks on a round-the-world adventure, along with Bugs and The VP of Warner Bros. Their mission? Find Damien's father, and the missing blue diamond... and stay one step ahead of The Acme Corp., who wants the diamond for their own purposes.",
            "popularity": 25.178,
            "poster_path": "/pNrQaH0ATrz9wFrNpwfB1aU4MpK.jpg",
            "release_date": "2003-11-14",
            "title": "Looney Tunes: Back in Action",
            "video": False,
            "vote_average": 6.3,
            "vote_count": 1122
        },
        {
            "adult": False,
            "backdrop_path": "/9RLRkSeBll1xBhIaedjPUxyBMeM.jpg",
            "genre_ids": [
                28,
                12,
                53,
                10752
            ],
            "id": 15379,
            "original_language": "en",
            "original_title": "Missing in Action",
            "overview": "American servicemen are still being held captive in Vietnam and it's up to one man to bring them home in this blistering, fast-paced action/adventure starring martial arts superstar Chuck Norris.Following a daring escape from a Vietnamese POW camp, Special Forces Colonel James Braddock (Norris) is on a mission to locate and save remaining MIAs.",
            "popularity": 9.878,
            "poster_path": "/nBrDcnNQca88ed1gRwZ1Q5cjNxE.jpg",
            "release_date": "1984-11-16",
            "title": "Missing in Action",
            "video": False,
            "vote_average": 5.8,
            "vote_count": 317
        },
        {
            "adult": False,
            "backdrop_path": "/9BrAptGRPR81MOjZeRBiyiUz8mW.jpg",
            "genre_ids": [
                28,
                12,
                35,
                80,
                18
            ],
            "id": 10117,
            "original_language": "en",
            "original_title": "Action Jackson",
            "overview": "Vengeance drives a tough Detroit cop to stay on the trail of a power hungry auto magnate who's systematically eliminating his competition.",
            "popularity": 6.666,
            "poster_path": "/ooRTSbr0MBkQ5LcyGo4FtEtyfaB.jpg",
            "release_date": "1988-02-12",
            "title": "Action Jackson",
            "video": False,
            "vote_average": 5.4,
            "vote_count": 152
        },
        {
            "adult": False,
            "backdrop_path": "/vcI8kweLIpGv7jb9NWVunOyZ2O7.jpg",
            "genre_ids": [
                18
            ],
            "id": 9422,
            "original_language": "en",
            "original_title": "A Civil Action",
            "overview": "Jan Schlickmann is a cynical lawyer who goes out to 'get rid of' a case, only to find out it is potentially worth millions. The case becomes his obsession, to the extent that he is willing to give up everything—including his career and his clients' goals—in order to continue the case against all odds.",
            "popularity": 8.378,
            "poster_path": "/6VsitR71vVKiGEDFPT71dKigbGN.jpg",
            "release_date": "1998-12-25",
            "title": "A Civil Action",
            "video": False,
            "vote_average": 6.4,
            "vote_count": 297
        },
        {
            "adult": False,
            "backdrop_path": "/iwIgSq0uOJA9oJd38XbjG5hiMg4.jpg",
            "genre_ids": [
                99
            ],
            "id": 634233,
            "original_language": "en",
            "original_title": "Class Action Park",
            "overview": "Class Action Park explores the legend, legacy, and truth behind the 1980's water park in Vernon, New Jersey that long ago entered the realm of myth. Known for its dangerous, unsupervised rides and lack of regulation, guests of Action Park expected to walk away with injuries and were lucky if they made it out alive. Shirking the trappings of nostalgia, the film uses investigative journalism, original animations,  recordings, and interviews with the people who lived it to reveal the True story of Action Park.",
            "popularity": 6.849,
            "poster_path": "/AoNojvxMhZtdVu9V8LtjfXJ6TPT.jpg",
            "release_date": "2020-08-22",
            "title": "Class Action Park",
            "video": False,
            "vote_average": 6.5,
            "vote_count": 65
        },
        {
            "adult": False,
            "backdrop_path": "/7zOLoxkdqEZj6zd2Uw9zrjXDwql.jpg",
            "genre_ids": [
                10751,
                16,
                14
            ],
            "id": 260234,
            "original_language": "en",
            "original_title": "Monster High: Frights, Camera, Action!",
            "overview": "When Draculaura is led to believe she's the rightful heir to the vampire throne, she and her best ghoulfriends are whisked away to Transylvania for a royal coronation to die for. But they soon discover the hunt for the queen is not over yet. The Ghouls must locate an ancient artifact known as the Vampire's Heart in order to discover the identity of the True Vampire Queen. It's a fangtastic adventure that will lead them from the Tower of Londoom, to a haunted river boat in New Goreleans and finally to the glamorous boo-vie lots of Hauntlywood. Could this be the moment when Draculara finally receives her vampire powers and discovers screams really can come True?",
            "popularity": 12.646,
            "poster_path": "/kGlTFeilg6RtyYi86kRQRml8CRG.jpg",
            "release_date": "2014-03-25",
            "title": "Monster High: Frights, Camera, Action!",
            "video": False,
            "vote_average": 7,
            "vote_count": 84
        },
        {
            "adult": False,
            "backdrop_path": "/juugwVQ6OO0WFJcMlKhm3KVAr49.jpg",
            "genre_ids": [
                18,
                80
            ],
            "id": 15771,
            "original_language": "en",
            "original_title": "Class Action",
            "overview": "A Liberal activist lawyer alienated his daughter Maggie years ago when she discovered his many affairs. Now a conservative corporate lawyer, Maggie agrees to go up against her father in court. To gain promotion, she must defend an auto manufacturer against charges that their explosion-prone station wagons are unsafe. As her mother begs for peace, Maggie takes on her dad in a trial that turns increasingly personal and nasty.",
            "popularity": 5.234,
            "poster_path": "/vCl4v5oKEtPANXe0L7Q0feJgCYa.jpg",
            "release_date": "1991-03-15",
            "title": "Class Action",
            "video": False,
            "vote_average": 6.2,
            "vote_count": 105
        },
        {
            "adult": False,
            "backdrop_path": "/dLR19YNqv8eZYQTRVDYoM8gunvq.jpg",
            "genre_ids": [
                28,
                10752
            ],
            "id": 27352,
            "original_language": "en",
            "original_title": "Braddock: Missing in Action III",
            "overview": "When Colonel James Braddock is told that his Asian wife and 12-year-old son are still alive in Communist Vietnam, he mounts a one-man assault to free them. Armed with the latest high-tech firepower, Braddock fights his way into the heart of the country and ends up battling his way out with several dozen abused Amerasian children in tow! Struggling to keep them alive while outmaneuvering a sadistic Vietnamese officer, Braddock ignites the jungle in a blazing cross-country race for freedom.",
            "popularity": 9.773,
            "poster_path": "/eFaW1GWwkuuTWwLehMOHRBSG3BC.jpg",
            "release_date": "1988-01-22",
            "title": "Braddock: Missing in Action III",
            "video": False,
            "vote_average": 5.8,
            "vote_count": 170
        },
        {
            "adult": False,
            "backdrop_path": "/dc4WaGwzYPL0t88TZFM3sqEYh0S.jpg",
            "genre_ids": [
                28,
                10752
            ],
            "id": 12764,
            "original_language": "en",
            "original_title": "Missing in Action 2: The Beginning",
            "overview": "Prequel to the first Missing In Action, set in the early 1980s it shows the capture of Colonel Braddock during the Vietnam war in the 1970s, and his captivity with other American POWs in a brutal prison camp, and his plans to escape.",
            "popularity": 10.668,
            "poster_path": "/vOgiL2KQYyTHJ225lT5QB5B9kO0.jpg",
            "release_date": "1985-03-01",
            "title": "Missing in Action 2: The Beginning",
            "video": False,
            "vote_average": 5.9,
            "vote_count": 183
        },
        {
            "adult": False,
            "backdrop_path": "/3bsCC10rhLaL60D2GBqcJguEaJN.jpg",
            "genre_ids": [
                18
            ],
            "id": 137599,
            "original_language": "en",
            "original_title": "Action",
            "overview": "Bruno is an idealistic hero who questions the meaning of life in this confusing and sometimes hallucinatory erotic drama. After a night in jail, he is gang-raped by punk rockers in a garbage dump. He later saves an old man who believes he is Garibaldi and a woman he believes is Ophelia. Bruno watches helplessly as she later jumps from a window.",
            "popularity": 3.016,
            "poster_path": "/9VhkxeP1uX39skDb1l4KEn8EsKS.jpg",
            "release_date": "1980-01-04",
            "title": "Action",
            "video": False,
            "vote_average": 4.5,
            "vote_count": 11
        },
        {
            "adult": False,
            "backdrop_path": "/vln6rDLYPYiLMz0PCN7z5mvVLhG.jpg",
            "genre_ids": [
                28,
                12,
                80,
                53
            ],
            "id": 28280,
            "original_language": "en",
            "original_title": "Direct Action",
            "overview": "Frank Gannon, a veteran cop, is being hunted by his fellow police officers after they learned he has betrayed the brotherhood and exposed to the feds wide scale corruption of the LAPD. He has one day left to prove his case and survive.",
            "popularity": 4.077,
            "poster_path": "/cgS2xvButiNQtT1dGf1cukdoMcR.jpg",
            "release_date": "2004-01-01",
            "title": "Direct Action",
            "video": False,
            "vote_average": 5.7,
            "vote_count": 29
        },
        {
            "adult": False,
            "backdrop_path": "/s67Pj026QeQe4ricdR78KWORmop.jpg",
            "genre_ids": [
                35
            ],
            "id": 624582,
            "original_language": "ml",
            "original_title": "Love Action Drama",
            "overview": "Dineshan is in love with Shoba, but she insists he give up smoking and drinking before marriage. It’s easier said than done, but will love triumph?",
            "popularity": 2.349,
            "poster_path": "/mVqV88crk9evENJB0DeVQzIL94v.jpg",
            "release_date": "2019-09-06",
            "title": "Love Action Drama",
            "video": False,
            "vote_average": 7,
            "vote_count": 14
        },
        {
            "adult": False,
            "backdrop_path": "/6SGbP7YBDDxwTA9LBdvfrM2sX9o.jpg",
            "genre_ids": [
                53,
                28,
                80
            ],
            "id": 306325,
            "original_language": "en",
            "original_title": "Violence of Action",
            "overview": "The Ghost's personal money launderer is due in town and Bojan, a ghost from Kane'e past suddenly appears on the scene. The CIA is convinced that Bojan has come to protect the money launderer.",
            "popularity": 3.255,
            "poster_path": "/dXkMSDU9EjCUY4eEmvYwpZIoobH.jpg",
            "release_date": "2012-12-24",
            "title": "Violence of Action",
            "video": True,
            "vote_average": 6.5,
            "vote_count": 12
        },
        {
            "adult": False,
            "backdrop_path": "/jHvUu1G1C176OfIBnVwwVhRC6nU.jpg",
            "genre_ids": [
                28,
                37
            ],
            "id": 552872,
            "original_language": "en",
            "original_title": "Legal Action",
            "overview": "Big-city lawyer Casey McKay, is drawn to a small town by his ex-wife to defend her brother, accused of murdering a DA. He discovers a web of conspiracy that puts him face-to-face with the town's most corrupt land developer, Mr. Gates.",
            "popularity": 2.96,
            "poster_path": "/k22cE5YBgQpuf8Vsh2LpkyOEM2F.jpg",
            "release_date": "2020-02-27",
            "title": "Legal Action",
            "video": False,
            "vote_average": 4,
            "vote_count": 1
        },
        {
            "adult": False,
            "backdrop_path": "",
            "genre_ids": [
                35,
                10749,
                878
            ],
            "id": 49679,
            "original_language": "hi",
            "original_title": "Action Replayy",
            "overview": "A young man tries to revive his parents' wilting marriage in a unique manner - travel to the 1970s when their romance was budding and make it bloom. This is more complex than he expects.",
            "popularity": 2.948,
            "poster_path": "/8YzWja1cgzIaaKys6Ajk95kJxQY.jpg",
            "release_date": "2010-11-05",
            "title": "Action Replayy",
            "video": False,
            "vote_average": 5.4,
            "vote_count": 50
        },
        {
            "adult": False,
            "backdrop_path": "/ymLLxJEm3HSM63A8lZ3oZAxiHR1.jpg",
            "genre_ids": [
                28,
                80,
                18,
                36,
                53
            ],
            "id": 29142,
            "original_language": "en",
            "original_title": "Executive Action",
            "overview": "Rogue intelligence agents, right-wing politicians, greedy capitalists, and free-lance assassins plot and carry out the JFK assassination in this speculative agitprop.",
            "popularity": 2.894,
            "poster_path": "/98G5HS7hU03wjiTjJ7SDuq20AHx.jpg",
            "release_date": "1973-11-07",
            "title": "Executive Action",
            "video": False,
            "vote_average": 6.4,
            "vote_count": 26
        },
        {
            "adult": False,
            "backdrop_path": "",
            "genre_ids": [
                28,
                53
            ],
            "id": 628900,
            "original_language": "en",
            "original_title": "Violence of Action",
            "overview": "After being involuntarily discharged from the U.S. Special Forces, James Harper (Pine) decides to support his family by joining a private contracting organization alongside his best friend (Foster) and under the command of a fellow veteran (Sutherland). Overseas on a covert mission, Harper must evade those trying to kill him while making his way back home.",
            "popularity": 3.235,
            "poster_path": "/jWdz6qEu4ShWjQbzlOaIMUVIFsH.jpg",
            "release_date": "2021-12-09",
            "title": "Violence of Action",
            "video": False,
            "vote_average": 0,
            "vote_count": 0
        },
        {
            "adult": False,
            "backdrop_path": "/qc5yiiYYVPxsUgQVnaWQQ6glkY7.jpg",
            "genre_ids": [],
            "id": 693357,
            "original_language": "ja",
            "original_title": "Futabu Live Action",
            "overview": "A girl joins a club where she is the only girl who is not a hermaphrodite.",
            "popularity": 3.129,
            "poster_path": "/dGteNP779HON7O944hkKeOHkQjs.jpg",
            "release_date": "2016-02-19",
            "title": "Futabu Live Action",
            "video": False,
            "vote_average": 9,
            "vote_count": 1
        }
    ]
    logging.info(movies)
    return render_template("index.html", movies=movies)
