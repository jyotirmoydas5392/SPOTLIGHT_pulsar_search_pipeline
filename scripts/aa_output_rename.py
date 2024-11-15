import numpy as np
import glob

def aa_output_rename(file_path, file_name):
    
    files = glob.glob(file_path +"/*harm*dat")
    
    lines = []
    for file in files:
        DM_value = str("{:.2f}".format(float(file.split("harm_")[1].split(".dat")[0])))
        os.system("cp " + str(file) + " " + file_path + "/" + file_name + "_DM" + DM_value + ".dat")