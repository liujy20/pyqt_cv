import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--a', type=str)
parser.add_argument('--b', type=str)
opt = parser.parse_args()

print(type(opt.a),int(opt.a)+int(opt.b))