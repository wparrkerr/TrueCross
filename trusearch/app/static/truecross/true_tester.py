import Grid
import main

g = Grid.Grid(9)

g,hints = main.create_wordsearch(g, ["griff","app","yes","no","poultry","adam","interstellar","bella","brady","here","girl","cookies","milk","crossword","search","word","volume","will"])
print hints
g.write_to_file("search.txt")