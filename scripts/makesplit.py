import os
from os.path import basename, dirname
from glob import glob
import pandas as pd


def main():
	# create train/dev/test splits for each language
	# balance splits based on number of characters per document
	result = []
	for langpath in glob('Coreference_data_0912/*_whole'):
		lang = basename(langpath).removesuffix('_whole')
		sizes = sorted([
			(os.path.getsize(fname), basename(fname))
			for fname in glob(f'{langpath}/source/*.txt')])
		splits = {split: [] for split in ('train', 'dev', 'test')}
		for n, (size, fname) in enumerate(sizes):
			if (n - 4) % 10 == 0:
				split = 'dev'
			elif (n - 5) % 10 == 0:
				split = 'test'
			else:
				split = 'train'
			result.append((lang, fname, size, split))
	columns = ['language', 'filename', 'size', 'split']
	df = pd.DataFrame(result, columns=columns)
	df.to_csv('splits.csv', index=False)


if __name__ == '__main__':
	main()
