# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:39:12 2020

@author: WILLY
"""

from os import walk
from os import path
from shutil import move
import getpass
import click

mac_username = getpass.getuser()
includes_file_extensn = ([".jpg", ".gif", ".png", ".jpeg", ])
search_dir = path.dirname('/Users/' + mac_username + '/Documents/')
target_foldr = path.dirname('/Users/' + mac_username + '/Pictures/Archive/')
exclude_foldr = set([target_foldr,
                    path.dirname('/Users/' + mac_username +
                                 '/Documents/GitHub/'),
                     path.dirname('/Users/' + mac_username +
                                  '/Documents/Random/'),
                     path.dirname('/Users/' + mac_username +
                                  '/Documents/Stupid_Folder/'),
                     ])

if click.confirm("Would you like to move files?",
                 default=False):
    question_moving = True
else:
    question_moving = False


def organize_files():
    """THE MODULE HAS BEEN BUILD FOR KEEPING YOUR FILES ORGANIZED."""
    # topdown=True required for filtering.
    # "Root" had all info i needed to filter folders not dir...
    for root, dir, files in walk(search_dir, topdown=True):
        for file in files:
            # creating a directory to str and excluding folders that start with
            if (not (str(root) + '/').startswith(tuple(exclude_foldr))):
                # showcase only the file types looking for
                if (file.endswith(tuple(includes_file_extensn))):
                    # using path.normpath as i found an issue with double //
                    # in file paths.
                    filetomove = path.normpath(str(root) + '/' +
                                               str(file))
                    # forward slash required for both to split
                    movingfileto = path.normpath(str(target_foldr) + '/' +
                                                 str(file))
                    # Answering "NO" this only prints the files "TO BE Moved"
                    print('Files To Move: ' + str(filetomove))
                    # This is using the prompt you answered at the beginning
                    if question_moving is True:
                        print('Moving File: ' + str(filetomove) +
                              "\n To:" + str(movingfileto))
                        # This is the command that moves the file
                        move(filetomove, movingfileto)
                        pass

            # The rest is ignoring explicitly and continuing
                    else:
                        pass
                    pass
                else:
                    pass
            else:
                pass


if __name__ == '__main__':
    organize_files()