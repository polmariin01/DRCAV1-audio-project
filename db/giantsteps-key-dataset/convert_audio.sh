#!/bin/bash -       
#title           :conver_audio.sh
#description     :This script will convert all audio files of the dataset from mp3 to wav.
#author		 :richard vogl (richard.vogl@jku.at)
#date            :2015 07 17
#version         :0.1    
#usage		 :bash conver_audio.sh
#notes           :uses sox
#bash_version    :3.2.57(1)-release
#==============================================================================

cd audio
for file in ./*.mp3; do
    printf "Converting : ${file} ..."
    #touch ../audiowav/${file%mp3}wav
    lame -b 44100 -f $file ../audiowav/${file%mp3}wav 
#    sox $file ${file%mp3}wav rate 44100 gain -0.1 remix -;
    printf " done!\n"
done;

# script modificat