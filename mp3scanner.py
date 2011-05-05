#!/usr/bin/python -tt

from mutagen.easyid3 import EasyID3
import sys, glob, os

def main():
  files = glob.glob(sys.argv[1] + "/**/*.mp3")
  files.extend(glob.glob( sys.argv[1] + "/*.mp3"))
  n = len(files)
  renamed = 0;
  skipped = 0;
  for i in range(n):
    file = os.path.abspath(files[i])
    id3 = EasyID3(file)
    if 'artist' in id3 and 'title' in id3:      
      destname = id3['artist'][0] + ' - ' + id3['title'][0] + '.mp3'
      destname = destname.replace('/', ' ')      
      print str(int(1.0 * (i+1)/n * 100)) + "%\t", destname
      os.rename(file, os.path.dirname(file) + '/' + destname)
      renamed += 1
    else:
      skipped += 1
  else:
    print "%d song(s) renamed, %d song(s) skipped" % (renamed, skipped)

if __name__ == '__main__':
  main()

