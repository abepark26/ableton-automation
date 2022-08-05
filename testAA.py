from aaConext import *
import pyautogui

# const: directory names
SP = r'\SAMPLE'
TP = r'\TEMPLATE'
SV = r'\SAVED'

# open import paths
root_path = r'E:\AA'

# paths
sample_path = root_path + SP
template_path = root_path + TP
saved_path = root_path + SV

# genres = [r'\RNB', r'\TRAP', r'\ALTERNATIVE', r'\LOFI']
genres = [r'\RNB']
# bpm_range = [r'\80', r'\90', r'\100', r'\110', r'\120', r'\130', r'\140']
bpm_range = [r'\90', r'\110', r'\140']
sample_visited = set()

################################################################################
# SAMPLE + TEMPLATE selection
for g in genres:
    tp_genre_path = template_path + g
    sp_genre_path = sample_path + g

    for b in bpm_range:
        ########################################
        # TEMPLATE selection
        # tp = ableton_select_template(tp_genre_path, b)
        # open_file(tp)

        ableton_select_template2(tp_genre_path, b)

        ########################################
        # SAMPLE selection
        sp_bpm_path = sp_genre_path + b
        sample_name = grab_rand_file(sp_bpm_path)
        bpm = str(grab_first_num(sample_name))

        # focus instrument
        ableton_change_tempo(bpm)

        # load sample file and unwarp
        ableton_focus_instrument()
        ableton_open_path(sp_bpm_path)
        do_file(sample_name[:-4])
        ableton_unwarp()
        
        # slice
        # ableton_slice()

        # extract
        new_sample_name = sample_name + "_new" + get_time()
        ableton_extract(saved_path, new_sample_name)

        # break

        


# print(sample_name)
# print(bpm)

# INSTRUMENTS = ['SAMPLE', 'KICK', 'HH', 'SNARE']
# # for inst in INSTRUMENTS:
# inst = 'HH'
# pyautogui.typewrite(inst + '\n', interval=0)

# # select file
# inst_path = 'C:/Users/PC/Desktop/' + root_dir + '/' + template_dir + '/' + inst
# num_files = len(glob.glob1(inst_path, "*.mid"))
# rand_file = random.choice(os.listdir(inst_path))

# # print(rand_file)
# # rand_idx = random.randrange(num_files)

# pyautogui.typewrite(str(rand_file) + '\n', interval=0)

