#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Written By Ismael Heredia in the year 2020

import os, shutil

class directoryCleaner(object):

    def __init__(self):

        self.ext_compressed = ["zip", "rar"]
        self.ext_videos = ["avi", "mp4", "mkv"]
        self.ext_pictures = ["ico", "bmp", "jpg", "jpeg", "png", "gif"]

        self.music_folder = os.path.join(os.path.expanduser("~"), "Music")
        self.pictures_folder = os.path.join(os.path.expanduser("~"), "Pictures")
        self.videos_folder = os.path.join(os.path.expanduser("~"), "Videos")
        self.downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        self.documents_folder = os.path.join(os.path.expanduser("~"), "Documents")

        self.compressed_folder = self.documents_folder + "\\Compressed Files"
        self.txt_folder = self.documents_folder + "\\TXT Files"
        self.pdf_folder = self.documents_folder + "\\PDF Files"
        self.exe_folder = self.documents_folder + "\\EXE Files"
        self.word_folder = self.documents_folder + "\\Word Files"
        self.html_folder = self.documents_folder + "\\HTML Files"
        self.srt_folder = self.documents_folder + "\\SRT Files"

        directories = [ self.compressed_folder, self.txt_folder, self.pdf_folder, self.exe_folder, self.word_folder, self.html_folder, self.srt_folder ]

        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)

    def process_file(self, fullpath, extension):
        name = os.path.basename(fullpath)
        if(extension == "mp3"):
            move_to = self.music_folder + "\\" + name
            print("[+] Move to : %s" % (move_to,))
            shutil.move(fullpath, move_to)
        elif(extension == "txt"):
            move_to = self.txt_folder + "\\" + name
            print("[+] Move to : %s" % (move_to,))
            shutil.move(fullpath, move_to)
        elif(extension == "pdf"):
            move_to = self.pdf_folder + "\\" + name
            print("[+] Move to : %s" % (move_to,))
            shutil.move(fullpath, move_to)
        elif(extension == "exe"):
            move_to = self.exe_folder + "\\" + name
            print("[+] Move to : %s" % (move_to,))
            shutil.move(fullpath, move_to)
        elif(extension == "docx"):
            move_to = self.word_folder + "\\" + name
            print("[+] Move to : %s" % (move_to,))
            shutil.move(fullpath, move_to)
        elif(extension == "html"):
            move_to = self.html_folder + "\\" + name
            print("[+] Move to : %s" % (move_to,))
            shutil.move(fullpath, move_to)
        elif(extension in self.ext_compressed):
            move_to = self.compressed_folder + "\\" + name
            print("[+] Move to : %s" % (move_to,))
            shutil.move(fullpath, move_to)
        elif(extension in self.ext_videos):
            move_to = self.videos_folder + "\\" + name
            print("[+] Move to : %s" % (move_to,))
            shutil.move(fullpath, move_to)
        elif(extension == "srt"):
            move_to = self.srt_folder + "\\" + name
            print("[+] Move to : %s" % (move_to,))
            shutil.move(fullpath, move_to)
        elif(extension in self.ext_pictures):
            move_to = self.pictures_folder + "\\" + name
            print("[+] Move to : %s" % (move_to,))
            shutil.move(fullpath, move_to)
        else:
            print("[-] No actions")

    def clean_directory(self, directory):
        print("\n[+] Cleaning directory %s ..." % (directory,))
        if(os.path.isdir(directory)):
            try:
                files = os.listdir(directory)
                for file in files:
                    fullpath = directory + "\\" + file
                    if(os.path.isfile(fullpath)):
                        extension = os.path.splitext(fullpath)[1]
                        extension = extension.replace(".", "").lower()
                        print("\n[+] File : %s" % (fullpath,))
                        self.process_file(fullpath, extension)
                    elif(os.path.isdir(fullpath)):
                        print("\n[+] Directory : %s" % (fullpath,))
                        dir_files = os.listdir(fullpath)
                        flag_dir = False
                        for dir_file in dir_files:
                            extension = os.path.splitext(dir_file)[1]
                            extension = extension.replace(".", "").lower()   
                            if(extension in self.ext_videos):
                                move_to = self.videos_folder
                                print("[+] Move to : %s" % (move_to,))
                                shutil.move(fullpath, move_to)
                                flag_dir = True
                        if not flag_dir:
                            print("[-] No actions")         
                    else:
                        print("\n[+] Unknown : %s" % (fullpath,))
            except:
                pass

            print("\n[+] Done")

        else:
            print("\n[-] Directory invalid")

        
