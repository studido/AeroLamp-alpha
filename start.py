import argparse
import os
import sys
from mediapipe_root import MediaPipe

def main(args):
    mediapipe = MediaPipe()
    mediapipe.initialize_mediapipe()


if __name__ == "__main__":
    print("AeroLamp Runtime 0.1")
    parser = argparse.ArgumentParser()
    parser.add_argument("--example_argument", help="What this argument does", default=0)
    try:
        args = parser.parse_args()
        main(args)
    except:
        print(sys.exc_info())