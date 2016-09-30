#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''A simple modifier for all html files in the folder (with subfolders)'''


import os

def walk(dir):
  for name in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, name)):
      if name.lower().endswith('.htm'):
        path = os.path.join(dir, name)
        html_modifier(path)
    elif os.path.isdir(name):
      pth = os.path.join(dir, name)
      walk(pth)

header = '''<!DOCTYPE html> 
<meta http-equiv="x-ua-compatible" content="IE=5">
'''

def html_modifier(path_to_file):
  with open(path_to_file, 'r') as datafile:
    old_data = datafile.read()
  if old_data.lower().startswith(header.lower()):
    pass
  else:
    os.rename(path_to_file, path_to_file+'.old')
    with open(path_to_file, 'w') as new_datafile:
      new_datafile.write(header + old_data)
    os.remove(path_to_file+'.old')
  with open('log.log', 'a+') as log:
    log.write(path_to_file + '\n')

    
def counter():
  try:
    with open('log.log', 'r') as log:
      numbers_of_lines = len(log.readlines())
  except:
    numbers_of_lines = 0
  return(numbers_of_lines)

def main():
  current_dir = os.getcwd()
  walk(current_dir)
  numbers_of_modifications = counter()
  print('Was modified {0} files'.format(numbers_of_modifications))
  # try:
    # os.remove('log.log')
  # except:
    # pass

if __name__ == '__main__':
    main()
