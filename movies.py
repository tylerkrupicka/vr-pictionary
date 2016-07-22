import time, random

movies = ["The Shawshank Redemption (1994)",
"The Godfather (1972)",
"The Godfather: Part II (1974)",
"The Dark Knight (2008)",
"12 Angry Men (1957)",
"Schindler's List (1993)",
"Pulp Fiction (1994)",
"The Lord of the Rings: The Return of the King (2003)",
"The Good, the Bad and the Ugly (1966)",
"Fight Club (1999)",
"The Lord of the Rings: The Fellowship of the Ring (2001)",
"Inception (2010)",
"Forrest Gump (1994)",
"Star Wars: Episode V - The Empire Strikes Back (1980)",
"The Lord of the Rings: The Two Towers (2002)",
"Airlift (2016)",
"One Flew Over the Cuckoo's Nest (1975)",
"Goodfellas (1990)",
"Seven Samurai (1954)",
"The Matrix (1999)",
"Star Wars (1977)",
"City of God (2002)",
"Se7en (1995)",
"It's a Wonderful Life (1946)",
"Life Is Beautiful (1997)",
"The Usual Suspects (1995)",
"Interstellar (2014)",
"The Silence of the Lambs (1991)",
"Léon: The Professional (1994)",
"Spirited Away (2001)",
"Once Upon a Time in the West (1968)",
"City Lights (1931)",
"The Intouchables (2011)",
"The Message (1976)",
"Saving Private Ryan (1998)",
"Casablanca (1942)",
"American History X (1998)",
"Modern Times (1936)",
"Psycho (1960)",
"The Green Mile (1999)",
"Raiders of the Lost Ark (1981)",
"Baahubali: The Beginning (2015)",
"Rear Window (1954)",
"The Pianist (2002)",
"The Departed (2006)",
"Terminator 2: Judgment Day (1991)",
"Whiplash (2014)",
"Gladiator (2000)",
"Back to the Future (1985)",
"Sunset Blvd. (1950)",
"Memento (2000)",
"The Prestige (2006)",
"Cinema Paradiso (1988)",
"Apocalypse Now (1979)",
"Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb (1964)",
"The Lion King (1994)",
"The Great Dictator (1940)",
"The Dark Knight Rises (2012)",
"Grave of the Fireflies (1988)",
"The Lives of Others (2006)",
"Captain America: Civil War (2016)",
"Alien (1979)",
"Paths of Glory (1957)",
"Django Unchained (2012)",
"3 Idiots (2009)",
"The Shining (1980)",
"Witness for the Prosecution (1957)",
"Princess Mononoke (1997)",
"WALL·E (2008)",
"American Beauty (1999)",
"Das Boot (1981)",
"M (1931)91",
"Once Upon a Time in America (1984)",
"Oldboy (2003)",
"Aliens (1986)",
"Citizen Kane (1941)",
"North by Northwest (1959)",
"Amélie (2001)",
"Vertigo (1958)",
"A Separation (2011)",
"Star Wars: Episode VI - Return of the Jedi (1983)",
"Braveheart (1995)",
"Double Indemnity (1944)",
"Requiem for a Dream (2000)",
"Reservoir Dogs (1992)",
"Lawrence of Arabia (1962)",
"To Kill a Mockingbird (1962)",
"A Clockwork Orange (1971)",
"The Kid (1921)",
"Eternal Sunshine of the Spotless Mind (2004)",
"Bicycle Thieves (1948)",
"Toy Story 3 (2010)",
"Taxi Driver (1976)",
"Singin' in the Rain (1952)",
"Amadeus (1984)",
"The Sting (1973)",
"Bhaag Milkha Bhaag (2013)",
"All About Eve (1950)",
"Yojimbo (1961)",
"Sunrise (1927)",
"Full Metal Jacket (1987)",
"2001: A Space Odyssey (1968)",
"Rashomon (1950)",
"Monty Python and the Holy Grail (1975)",
"Snatch. (2000)",
"The Apartment (1960)",
"Gangs of Wasseypur (2012)",
"Zootopia (2016)",
"The Treasure of the Sierra Madre (1948)",
"Ikiru (1952)",
"Metropolis (1927)",
"For a Few Dollars More (1965)",
"Inglourious Basterds (2009)",
"Swades (2004)",
"Toy Story (1995)",
"Scarface (1983)",
"The Third Man (1949)",
"OMG: Oh My God! (2012)",
"Haider (2014)",
"L.A. Confidential (1997)",
"The Hunt (2012)",
"Dilwale Dulhania Le Jayenge (1995)",
"Some Like It Hot (1959)",
"Batman Begins (2005)",
"Indiana Jones and the Last Crusade (1989)",
"Inside Out (2015)",
"Room (2015)",
"Good Will Hunting (1997)",
"Up (2009)",
"Unforgiven (1992)",
"Star Wars: Episode VII - The Force Awakens (2015)",
"Downfall (2004)",
"PK (2014)",
"Ran (1985)",
"Raging Bull (1980)",
"The Great Escape (1963)",
"On the Waterfront (1954)",
"Mr. Smith Goes to Washington (1939)",
"The Gold Rush (1925)",
"My Neighbor Totoro (1988)",
"Judgment at Nuremberg (1961)",
"The General (1926)",
"Chinatown (1974)",
"Kahaani (2012)",
"Heat (1995)",
"Wild Strawberries (1957)",
"Die Hard (1988)",
"The Secret in Their Eyes (2009)",
"The Seventh Seal (1957)",
"Pan's Labyrinth (2006)",
"Deadpool (2016)",
"The Bridge on the River Kwai (1957)",
"Howl's Moving Castle (2004)",
"Incendies (2010)",
"Blade Runner (1982)",
"Warrior (2011)",
"Lock, Stock and Two Smoking Barrels (1998)",
"The Wolf of Wall Street (2013)",
"V for Vendetta (2005)",
"The Elephant Man (1980)",
"The Wages of Fear (1953)",
"Casino (1995)",
"Barfi! (2012)",
"Rebecca (1940)",
"A Beautiful Mind (2001)",
"Gone with the Wind (1939)",
"It Happened One Night (1934)",
"The Big Lebowski (1998)",
"Cool Hand Luke (1967)",
"Dial M for Murder (1954)",
"How to Train Your Dragon (2010)",
"Gran Torino (2008)",
"Lagaan: Once Upon a Time in India (2001)",
"The Deer Hunter (1978)",
"Mary and Max (2009)",
"Into the Wild (2007)",
"Trainspotting (1996)",
"Lage Raho Munna Bhai (2006)",
"My Sassy Girl (2001)",
"Fargo (1996)",
"Persona (1966)",
"Rush (2013)",
"The Thing (1982)",
"Stalker (1979)",
"Hachi: A Dog's Tale (2009)",
"Baby (2015)",
"The 400 Blows (1959)",
"Finding Nemo (2003)",
"The Sixth Sense (1999)",
"Tae Guk Gi: The Brotherhood of War (2004)",
"The Best Years of Our Lives (1946)",
"The Maltese Falcon (1941)",
"Gone Girl (2014)",
"The Legend of 1900 (1998)",
"Wild Tales (2014)",
"No Country for Old Men (2007)",
"Network (1976)",
"Life of Brian (1979)",
"The Princess Bride (1987)",
"Hotel Rwanda (2004)",
"Captain America: Civil War (2016)",
"The Jungle Book (2016)",
"Deadpool (2016)",
"Star Wars: Episode VII - The Force Awakens (2015)",
"10 Cloverfield Lane (2016)",
"Zootopia (2016)",
"The Revenant (2015)",
"Avengers: Age of Ultron (2015)",
"Captain America: The Winter Soldier (2014)",
"The Hateful Eight (2015)",
"Mad Max: Fury Road (2015)",
"The Avengers (2012)",
"The Big Short (2015)",
"Guardians of the Galaxy (2014)",
"Room (2015)",
"Spotlight (2015)",
"The Martian (2015)",
"The Dark Knight (2008)",
"X-Men: Days of Future Past (2014)",
"The Shawshank Redemption (1994)",
"Creed (2015)",
"Brooklyn (2015)",
"Star Wars (1977)",
"Iron Man (2008)",
"The Godfather (1972)",
"Ex Machina (2015)",
"Inside Out (2015)",
"Interstellar (2014)",
"Kingsman: The Secret Service (2014)",
"The Princess Bride (1987)",
"Harry Potter and the Sorcerer's Stone (2001)",
"The Sandlot (1993)",
"The Wolf of Wall Street (2013)",
"The Jungle Book (1967)",
"Pulp Fiction (1994)",
"Bridge of Spies (2015)",
"Sicario (2015)",
"The Breakfast Club (1985)",
"The Dark Knight Rises (2012)",
"The Hunger Games: Catching Fire (2013)",
"Lone Survivor (2013)",
"Inception (2010)",
"Titanic (1997)",
"Schindler's List (1993)",
"Gone Girl (2014)",
"Frozen (2013)",
"The Departed (2006)",
"Inglourious Basterds (2009)",
"Fight Club (1999)",
"Pleasantville (1998)",
"Watchmen (2009)",
"X-Men: First Class (2011)",
"The Lord of the Rings: The Fellowship of the Ring (2001)",
"Forrest Gump (1994)",
"Into the Wild (2007)",
"Straight Outta Compton (2015)",
"Harry Potter and the Deathly Hallows: Part 2 (2011)",
"The Matrix (1999)",
"Scott Pilgrim vs. the World (2010)",
"The Notebook (2004)",
"Whiplash (2014)",
"The Wizard of Oz (1939)",
"Django Unchained (2012)",
"The Prestige (2006)",
"Kick-Ass (2010)",
"Jurassic Park (1993)",
"V for Vendetta (2005)",
"Gladiator (2000)",
"Skyfall (2012)",
"American Beauty (1999)",
"Mission: Impossible - Rogue Nation (2015)",
"Batman Begins (2005)",
"Ghostbusters (1984)",
"Batman (1989)",
"Trumbo (2015)",
"The Lion King (1994)",
"The Silence of the Lambs (1991)",
"The Big Lebowski (1998)",
"The Grand Budapest Hotel (2014)",
"Fury (2014)",
"The Goonies (1985)",
"E.T. the Extra-Terrestrial (1982)",
"Saving Private Ryan (1998)",
"Good Will Hunting (1997)",
"Love Actually (2003)",
"Jaws (1975)",
"The Usual Suspects (1995)",
"Blade Runner (1982)",
"Se7en (1995)",
"Léon: The Professional (1994)",
"Goodfellas (1990)",
"The Truman Show (1998)",
"Requiem for a Dream (2000)",
"The Perks of Being a Wallflower (2012)",
"Alien (1979)",
"Avatar (2009)",
"A Clockwork Orange (1971)",
"The Imitation Game (2014)",
"Star Wars: Episode VI - Return of the Jedi (1983)",
"Star Wars: Episode III - Revenge of the Sith (2005)",
"Harry Potter and the Goblet of Fire (2005)",
"The Godfather: Part II (1974)",
"Her (2013)",
"The Shining (1980)",
"Edge of Tomorrow (2014)",
"Psycho (1960)",
"300 (2006)",
"One Flew Over the Cuckoo's Nest (1975)",
"Braveheart (1995)",
"Stardust (2007)",
"The Conjuring (2013)",
"Back to the Future (1985)",
"Big Hero 6 (2014)",
"Black Swan (2010)",
"The Girl with the Dragon Tattoo (2011)",
"Birdman or (The Unexpected Virtue of Ignorance) (2014)",
"Pirates of the Caribbean: The Curse of the Black Pearl (2003)",
"Aliens (1986)",
"Star Wars: Episode V - The Empire Strikes Back (1980)",
"Prisoners (2013)",
"Me and Earl and the Dying Girl (2015)",
"Finding Nemo (2003)",
"The Theory of Everything (2014)",
"Stand by Me (1986)",
"The Incredibles (2004)",
"The Lord of the Rings: The Return of the King (2003)",
"The Fault in Our Stars (2014)",
"Reservoir Dogs (1992)",
"The Intouchables (2011)",
"Harry Potter and the Prisoner of Azkaban (2004)",
"Casino Royale (2006)",
"The Lego Movie (2014)",
"No Country for Old Men (2007)",
"Les Misérables (2012)",
"The Help (2011)",
"Trainspotting (1996)",
"The Fifth Element (1997)",
"Scarface (1983)",
"Raiders of the Lost Ark (1981)",
"Drive (2011)",
"The Green Mile (1999)",
"Fargo (1996)",
"Kill Bill: Vol. 1 (2003)",
"Apocalypse Now (1979)",
"Zodiac (2007)",
"City of God (2002)",
"A Beautiful Mind (2001)",
"Taxi Driver (1976)",
"Ferris Bueller's Day Off (1986)",
"Eternal Sunshine of the Spotless Mind (2004)",
"Superbad (2007)",
"Rocky (1976)",
"American History X (1998)",
"Rush (2013)",
"Casablanca (1942)",
"The Wicker Man (1973)",
"Shutter Island (2010)",
"Memento (2000)",
"Donnie Darko (2001)",
"The Pianist (2002)",
"Sin City (2005)",
"Full Metal Jacket (1987)",
"The Exorcist (1973)",
"Snatch. (2000)",
"American Psycho (2000)",
"Almost Famous (2000)",
"Breakfast at Tiffany's (1961)",
"Blue Is the Warmest Color (2013)",
"Pride & Prejudice (2005)",
"Zombieland (2009)",
"Warrior (2011)",
"Terminator 2: Judgment Day (1991)",
"Dazed and Confused (1993)",
"Star Trek (2009)",
"There Will Be Blood (2007)",
"12 Years a Slave (2013)",
"Catch Me If You Can (2002)",
"Serenity (2005)",
"Pan's Labyrinth (2006)",
"About Time (2013)",
"The Birds (1963)",
"Spirited Away (2001)",
"Life Is Beautiful (1997)",
"2001: A Space Odyssey (1968)",
"Ocean's Eleven (2001)",
"Oldboy (2003)",
"The Hobbit: An Unexpected Journey (2012)",
"Looper (2012)",
"Willy Wonka & the Chocolate Factory (1971)",
"Remember the Titans (2000)",
"The Good, the Bad and the Ugly (1966)",
"Silver Linings Playbook (2012)",
"The Boy in the Striped Pajamas (2008)",
"12 Angry Men (1957)",
"Predator (1987)",
"Brokeback Mountain (2005)",
"The Impossible (2012)",
"Interview with the Vampire: The Vampire Chronicles (1994)",
"The Hangover (2009)",
"The Social Network (2010)"]

random.shuffle(movies)
i = 0
#print("Welcome to Pictionary")

while True:
    input("Press ENTER..                                       ")
    print(movies[i], end='\r')
    time.sleep(10)
    i += 1
