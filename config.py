html_path = "./"

# to display both neurons and visual stimuli
#MOVIE_W, MOVIE_H, SHIFT_H = 512.0, 768.0, 0.0
#ZOOM, TOP, LEFT = 1.0, 0.0, 0.0

# to display only the neurons without visual stimuli
MOVIE_W, MOVIE_H, SHIFT_H = 512.0, 512.0, -256.0
ZOOM, TOP, LEFT = 2.0, 128.0, 128.0

FPS = 30
DFF_THRESHOLD = 0.2
REWARD = 100
PENALTY = 50
#EVAL_TOUCH_METHOD = "mask" 
EVAL_TOUCH_METHOD = "distance" 
EVAL_TOUCH_RADIUS = 20

file_chosen = 7

FILEPATH_LIST = ['./data/496908818/natural_movie_one_70290-71191', 
'./data/496935917/natural_movie_one_31442-32343', 
'./data/496935917/natural_movie_two_63943-64844', 
'./data/500964514/natural_movie_one_70426-71331', 
'./data/501271265/natural_movie_one_38756-39660', 
'./data/501271265/natural_movie_three_19746-23366', 
'./data/501317920/natural_movie_one_70463-71367', 
'./data/501337989/natural_movie_one_31520-32423', 
'./data/501337989/natural_movie_two_64104-65007', 
'./data/501498760/natural_movie_one_70439-71342', 
'./data/501773889/natural_movie_one_31524-32428', 
'./data/501773889/natural_movie_two_64128-65032', 
'./data/501788003/natural_movie_one_31521-32425', 
'./data/501788003/natural_movie_two_64122-65026', 
'./data/501839084/natural_movie_one_31452-32354', 
'./data/501839084/natural_movie_two_63966-64867', 
'./data/501876401/natural_movie_one_38682-39584', 
'./data/501876401/natural_movie_three_19716-23327', 
'./data/530958091/natural_movie_one_38757-39661', 
'./data/530958091/natural_movie_three_19750-23369']


FILEPATH = FILEPATH_LIST[file_chosen]
