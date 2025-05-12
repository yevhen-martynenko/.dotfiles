#!/bin/bash


############################
########### basic ##########
############################
cd /
jump pin root
cd /mnt/
jump pin mnt


################
##### home #####
################
cd /home/spes/
jump pin home

cd /home/spes/Downloads/
jump pin d
cd /home/spes/Downloads/
jump pin dow
cd /home/spes/Downloads/
jump pin downloads


################
##### conf #####
################
cd /home/spes/.config/
jump pin conf
cd /home/spes/.config/sway/
jump pin sway
cd /etc/sway/ 
jump pin esw
cd /usr/share/sway/
jump pin usw



############################
########## refuli ##########
############################

###########################
######## variables ########
###########################
refuli="/mnt/refuli/refuli"

notes=" __notes__"
files=" __files__"
games=" __games__"
saved=" __saved__"

entertainment=" __entertainment__"
books=" __books__"
music=" __music__"
anime=" __anime__"
videos=" __videos__"

programming=" __programming__"
projects=" __projects__"
web=" __web__"
programs=" __programs__"


##########################
######## commands ########
##########################
cd "$refuli"
jump pin r

cd "$refuli/$saved"
jump pin s
cd "$refuli/$notes"
jump pin n
cd "$refuli/$games"
jump pin g


#########################
##### entertainment #####
#########################
cd "$refuli/$entertainment"
jump pin e
cd "$refuli/$entertainment"
jump pin ent
cd "$refuli/$entertainment"
jump pin entertainment

cd "$refuli/$entertainment/$anime"
jump pin a
cd "$refuli/$entertainment/$anime"
jump pin anime

cd "$refuli/$entertainment/$music"
jump pin m
cd "$refuli/$entertainment/$music"
jump pin mus
cd "$refuli/$entertainment/$music"
jump pin music

cd "$refuli/$entertainment/$videos"
jump pin v
cd "$refuli/$entertainment/$videos"
jump pin vid
cd "$refuli/$entertainment/$videos"
jump pin videos
cd "$refuli/$entertainment/$videos/freetube/"
jump pin vf
cd "$refuli/$entertainment/$videos/freetube/"
jump pin vft
cd "$refuli/$entertainment/$videos/freetube/"
jump pin vfreetube

cd "$refuli/$entertainment/$books"
jump pin b


#################
##### files #####
#################
cd "$refuli/$files"
jump pin f
cd "$refuli/$files"
jump pin files

cd "$refuli/$files/documents/"
jump pin fd
cd "$refuli/$files/documents/"
jump pin fdocs
cd "$refuli/$files/documents/"
jump pin fdocuments

cd "$refuli/$files/files/"
jump pin ff
cd "$refuli/$files/files/"
jump pin ffiles

cd "$refuli/$files/music/"
jump pin fm
cd "$refuli/$files/music/"
jump pin fmusic

cd "$refuli/$files/pictures/"
jump pin fpic
cd "$refuli/$files/pictures/"
jump pin fpics
cd "$refuli/$files/pictures/"
jump pin fi
cd "$refuli/$files/pictures/"
jump pin fimag
cd "$refuli/$files/pictures/"
jump pin fimages

cd "$refuli/$files/programming/"
jump pin fp
cd "$refuli/$files/programming/"
jump pin fpr
cd "$refuli/$files/programming/"
jump pin fprog
cd "$refuli/$files/programming/"
jump pin fprogramming

cd "$refuli/$files/videos/"
jump pin fv
cd "$refuli/$files/videos/"
jump pin fvid
cd "$refuli/$files/videos/"
jump pin fvideos


#######################
##### programming #####
#######################
cd "$refuli/$programming"
jump pin p

cd "$refuli/$programming/$projects"
jump pin pp
cd "$refuli/$programming/$projects"
jump pin pprojects

cd "$refuli/$programming/$programs"
jump pin ppr
cd "$refuli/$programming/$programs"
jump pin pprog
cd "$refuli/$programming/$programs"
jump pin pprograms

cd "$refuli/$programming/$web"
jump pin pw
cd "$refuli/$programming/$web"
jump pin pweb

cd "$refuli/$programming/web"
jump pin ppw
cd "$refuli/$programming/web"
jump pin ppweb

cd "$refuli/$programming/python"
jump pin py
cd "$refuli/$programming/python"
jump pin python

cd "$refuli/$programming/javascript"
jump pin js
cd "$refuli/$programming/javascript"
jump pin javascript

cd "$refuli/$programming/arduino"
jump pin ard
cd "$refuli/$programming/arduino"
jump pin arduino


###################
##### scripts #####
###################
cd "$refuli/scripts/"
jump pin scripts
