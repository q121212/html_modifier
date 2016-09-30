#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

class Folder:
  def __init__(self):
    self.files = []
    self.subfolders = []
    
  def list_of_dirs(self, dir):
    for i in os.walk(dir):
      self.subfolders.append(i[0])

  def list_of_files(self, root_dir):
    for name in self.subfolders:  
      full_path_to_dir = os.path.join(root_dir, name)
      for i in os.listdir(full_path_to_dir):
        self.files.append(os.path.join(full_path_to_dir, i))
   
# header = '''<!--[if lte IE 7]><!DOCTYPE html>
# <meta http-equiv="x-ua-compatible" content="IE=5"><!--<![endif]-->
# <!DOCTYPE html><!--<![endif]-->
# '''
   
header = '''<!DOCTYPE html> 
<meta http-equiv="x-ua-compatible" content="IE=5">
'''
    
def html_modifier(path_to_file):
  counter = 0
  if os.path.isfile(path_to_file):
    if path_to_file.endswith('.htm'):
      with open(path_to_file, 'r') as datafile:
        old_data = datafile.read()
      if old_data.lower().startswith(header.lower()):
        pass
      else:
        try:
          os.remove(path_to_file+'.old')
        except:
          os.rename(path_to_file, path_to_file+'.old')
          with open(path_to_file, 'w') as new_datafile:
            new_datafile.write(header + old_data)
          os.remove(path_to_file+'.old')
          counter+=1
  return counter
	
def main():
  root_dir = os.getcwd()
  f = Folder()
  f.list_of_dirs(root_dir)
  f.list_of_files(root_dir)
  counter = 0
  for path in f.files:
    counter+=html_modifier(path)
  print('Was modified {0} .htm files.'. format(counter))

if __name__ == '__main__':
    main()

