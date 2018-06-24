from textgenrnn import textgenrnn
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-e", "--num-epochs", type=int, default=100, help="Number epochs for generation")
ap.add_argument("-i", "--input-file", type=str, default="./input.txt", help="Which file to grab input data from")
args = vars(ap.parse_args())

textgen = textgenrnn()

textgen.train_from_file(args["input-file"], num_epochs=args["num-epochs"])