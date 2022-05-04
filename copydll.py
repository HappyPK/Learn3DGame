# -*- coding: utf-8 -*-  
import os
import glob
import shutil

def copyAssets(chapterNum):
    if os.path.exists(os.getcwd()+r"\build\vc16\src" + chapterNum + r"\Assets"):
        shutil.rmtree(os.getcwd()+r"\build\vc16\src" + chapterNum + r"\Assets")
    shutil.copytree(os.getcwd()+r"\src" + chapterNum + r"\Assets", os.getcwd()+r"\build\vc16\src" + chapterNum + r"\Assets")

if __name__ == '__main__':  
    SDLDLLPath = glob.glob(os.getcwd()+ r"\3rdParty\SDL\lib\x64\*.dll")
    for dll in SDLDLLPath:
        fpath,fname=os.path.split(dll)  
        shutil.copy(dll, os.path.join(os.getcwd()+r"\bin\vc16\x64\Debug",fname))
        shutil.copy(dll, os.path.join(os.getcwd()+r"\bin\vc16\x64\Release",fname))
       
    copyAssets(r"\Chapter02")
    copyAssets(r"\Chapter03")
    copyAssets(r"\Chapter04")