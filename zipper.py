#! /usr/bin/python

import enquiries
from zipfile import ZipFile

print('')
print("          .--._________   _...._    _________   _...._            __.....__              ")
print("          |__|\        |.'      '-. \        |.'      '-.     .-''         '.            ")
print("          .--. \        .'```'.    '.\        .'```'.    '.  /     .-''"'-.  `. .-,.--.  ')
print('          |  |  \      |       \     |\      |       \     \/     /________\   \|  .-. | ')
print('.--------.|  |   |     |        |    | |     |        |    ||                  || |  | | ')
print("|____    ||  |   |      \      /    .  |      \      /    . \    .-------------'| |  | | ")
print("    /   / |  |   |     |\`'-.-'   .'   |     |\`'-.-'   .'   \    '-.____...---.| |  '-  ")
print("  .'   /  |__|   |     | '-....-'`     |     | '-....-'`      `.             .' | |      ")
print(" /    /___      .'     '.             .'     '.                 `''-...... -'   | |      ")
print("|         |   '-----------'         '-----------'                               |_|      ")
print("|_________|                                                                              ")
print('')


opt = ['Extract in created folder' , 'Extract in this folder' , 'Exit']
coi = enquiries.choose ( 'Choose one of the options below: ' , opt )

if coi == ('Extract in created folder'):
    opte = ['File Name' , 'Custom Name' , 'Exit']
    coie = enquiries.choose ( 'Choose Folder name: ' , opte )

    if coie == ('File Name'):
        ECFFileName = input ( 'Input file name without .zip extensions -->' )
        #FoldName = input('Input folder name to create -->')
        with ZipFile ( f"{ECFFileName}.zip" , 'r' ) as zipObj :
            zipObj.extractall ( f'{ECFFileName}' )
            print ( 'Done extracting into created folder! Exiting!' )

    if coie == ('Custom Name'):
        ECFFileName = input ( 'Input file name without .zip extensions -->' )
        FoldName = input('Input folder name to create -->')
        with ZipFile ( f"{ECFFileName}.zip" , 'r' ) as zipObj :
            zipObj.extractall ( f'{FoldName}' )
            print ( 'Done extracting into created folder! Exiting!' )

if coie == ('Exit'):
    print('Exiting')
    exit()

if coi == ('Extract in this folder'):
    EFFileName = input('Input file name -->')
    with ZipFile ( EFFileName , 'r' ) as zipObj :
        zipObj.extractall ( 'zipper-temp' )
        print('Done extracting! Exiting!')

if coi == ('Exit'):
    print('Exiting')
    exit()
