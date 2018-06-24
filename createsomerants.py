from textgenrnn import textgenrnn
import argparse

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--input-file", type=str, default="./Checkpoint\ Files/Linuxxx-epoch-90.hdf5", help="Which hdf5 file to grab input data from")
# args = vars(ap.parse_args())

input_file = "./Checkpoint\ Files/Linuxxx-epoch-90.hdf5"

textgen_2 = textgenrnn(input_file)

while True:
    textgen_2.generate(3, temperature=1.0)