
WORK_FOLDER = 'bin/'

# ==============================================================
# NEURAL NET
# ==============================================================

DEFAULT_NEURAL_NET_SETTINGS = {
    'no_of_possible_actions' : None,      # The number of actions the softmax layer produces
    'value_hidden_size' : 128,             # Size of hidden layer in value head 
    'res_layer_n' : 5,                    # The number of residual layers
    'filter_n' : 32,                     # The number of filters in a conv layer
    'kernel_size' : 3,
    'batch_size' : 100,                    
    'epochs' : 1,
    'verbose' : 1,
    'validation_split' : 0.05,
    'input_shape' : None,
    'history' : []
}

# ==============================================================
# TRAINING
# ==============================================================

# When a move is chosen, this temperature controls
# the level of exploration. If it dropbs below this value,
# it will be considered as 0.
MINIMUM_TEMPERATURE_ACCEPTED = 0.2

# How many seconds to think on a move while training
DEFAULT_TRAIN_THINK_TIME = 1.2
DEFAULT_NUMBER_OF_SIMULATIONS = 160

# The maximum number of positions to save
MEMORY_SIZE = 10000

NO_OF_EPISODES = 200
NO_OF_ITERATIONS = 50
NO_OF_GAMES_TO_BATTLE = 20
SAVE_THRESHOLD = 0.5501


# These variables must be overridden in the game's config files

TEMP_THRESHOLD = None
TEMP_DECAY = None