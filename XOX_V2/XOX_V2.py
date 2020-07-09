from ftplib import FTP
from time import sleep,time
import os, pygame, requests, random
ACCEPTED_NAME='qazwsxedcrfvtgbyhnujmikolp1234567890'
ACCEPTED_KEY='1234567890'
NUMPAD=[256,257,258,259,260,261,262,263,264,265]
ButtonColor=(255,255,255)
MessageColor=(100,200,100)
TextColor=(0,0,0)
current_page=''
def loadImages():
    global xpng, opng
    open('xox_x.png','wb').write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00d\x00\x00\x00d\x08\x06\x00\x00\x00p\xe2\x95T\x00\x00\t\x9dIDATx^\xed\x9dk\x8c\x1bW\x15\xc7\xff\xc7\xdd\r\x15\x15"m<F\r*\x94\xf2\xa6<Cx\x8b$\xa5;\xd7i|\xb7O\x01R\x00\xb5R+\xc2\xab-\x95\xfa\t\xb5TP$\xbe \xc4\x1b\nTjT\x14\t\xaa\xd0\x12\x8f\xd3\xf8:i\xb6\xa1\xa4t\x9bDEID\x11\xa4\r\xb4\xda\x08\x8f\xd3\x07\x88*\xd9u|\xd0x\xfd\x18{\xed\xb5\xc7\x9e\xb9\xbe\x8e\xc6\xdf\x12\xdf\xc79\xff\xdf\xdc\x87\xcf\xb9w\x96\x10\x7f\x8cR\x80\x8c\xb2&6\x061\x10\xc3\x1e\x82\x18H\x0c\xc40\x05\x0c3\'\x1e!1\x10\xc3\x140\xcc\x9cx\x84\xc4@\x0cS\xc00s\xe2\x11\x12\x031L\x81\x01\xcdq\x8a\xf6o\x99\xe8Rb>*S\x85\xcf\x0e\xd8\xcc\x92j\xf1\x08\x19@\xc9\x9ck\xcf3h\xb2Q\x95\xf9waA\x89\x81\x04\x04\xe2\xb8\xe2\x14\x80W\xb5T\xd3\r$W\x14w \x81\xff$\x12\x89C\xe5S\x93\x87\xa6Wg_\t\xe8\xc7\xd8\x17w\x8a\xb6\x03\xd0\xe5 \x9c\xebw\x86\x80\xe72\x96zCX\x0e\xf6\x1c!NQ\xdc\x0c\xc2\x8fZ:$\x1c\x06\xa3\x02\xe6c2U\xb8.,cLm\'\xe7\x8a\'\x19X\xdbf\xdf\x190o\x0fk\xaa\xaa\xb7\xdd\x13\x887:\x98pw7\xb1\x18\x98c\xc6MW\xa6\xd4\xc3\xa6\n:\x8c]\x8e+~\x06\xe0\xcb\xcd\xf5\x02\xa7@\xbcGZ\x059L\xbb\xdd\xea\xf6\x04\xe2U\xac\x8e\x92\x04>\x08`\r\x18\xef\xe9\xd8\x18ak\x99p\xe7\xd5\xab\xd4sQ\x18:\x8a6\xdba0\xf3c\xd3\xa9\xc2\'\xa3\xb4\xa5/ ~\x03\xb2s\xd3\xaf\x9e8waM\xa5R\xb9\x9d\x19\x19\x00\x13\xbe\xa7\xe74\x08wHK}/J\xa3u\xb4\xbddd\x00?\x97\x96\xfaJ\xd4}\x07\x06\xe27\xe8\xa1\x93\xe2\xa2\t\xc6\xdd`\\\xdff\xe8\xc1\n\xe3\xceq\x9d\xc6F\x05\xc3\xd3p( u\x08;\x8a\xe2\x8a\xc4\xe2:\xe3Mk\xcd\xcf\x18Nc\xa3\x84\x11\x1a\x90:\x01\xc7\x15\xb7\x83\xf1\x1dP\xcb>\xbdL@!c\xa9MQ\x0f\xf7a\xdb\x1f5\x8c\xd0\x81x\r.3\x8d\x1d\x90\x96\xfa\xd0\xb0\xa2EU\xdf)\x89\xfd`|\xcc\xd7\xbe\x965\xa3\xdd\x9fP\xa6\xacN"\xd5\xa6\xb1_\x01x\xfd\xa8\x9d\\\x0e\xe2^\xde0\xf1Ji\xc5A\x06\xdek\x82\x9d\x91\x01iLcE\xf1\x18\x08\x9f0\xc1\xd9v0\xd9\xa2\xfdV"\xba\x1f\xc0G\x1a\xdf\x11feR5\xff\x1d\xd5\x90\xec\xd2n\xe4@\xbc~M\x98\x9b\xdb\xfd\xcf\x9d\x14v\xe5\x0c~C\x84T\xfd;\x02\x1e\xcdXj\x83f\x06m\xfb M\xbd\x9b\x04\xc5q\xc5\x17\x01\xdc\xd3\xe6\xfa\x16i\xa9_j\x92\xa3k7ZF\x88o\x17\xd6\x1a\x86\x00\x9e\x90\x96\xfa\xa8N\x11\xb2\xae\xd8C\xc0\xa7\xea}2\xa3\x988\x07\x9f\xcf\xacR\x05\x9dvt\xebK+\x90.\xd3\x97\x16(\xbb\xdc\xf4\x85g\xc0{\x19x\xbbO\x8c\'\x98\xf9\x0b\xd3\xa9\xc2\xdfM\x80\xe1\xd9\xa0\x1dH\r\xca\x9f[\x16\xd2\x88\xc3\x129WH^\x9c\xa2V7\x84g\x1c9\xcf\x9a\xff\xc0e4S6\x05\xc6\xc8\x80\xe8\x84\x92u\xed\x19\x02\xado\x11\x9dQ\x90)%L\x02\xe1\xdbX\x8c\xce\xac\x0e\x0b}\xa8?\x1es%\x91g\x86_\xf89\x02\xb6d,\xe5\x8c\xce\xeb\xe5{\x1e\xc9\x94\xe57\xa9\x1d\n\x11T&\xa9\xd2\xc3\nV\x8d\x18T\xf0L=\x1a\xcd\xc0\xd1I\x90\xbd\xd1\xca\x9f\x18\xb6\xed(\xeb\x8f\x1cHu\xfa*\x8a?\x81\xf0q\x9f\xa3k\xa5\xa5\x0e\x0e\xe3\xb8S\x12\xf7\xf9\xa2\xd0\xcfKK]4L{\xba\xea\x1a\x01\xa4\xb6\xa6xO\xf3\x9b\xaa\x8e3\x9e\x91)\xf5\xe6AE\xa8\x85mv\xd6\xebW\x18\x9b\xc6%\x15`\x12\x10/t\x7f\xa0\x01\x81pxb\x926l|m\xfe\x85\xa0`\x1cW<\xdf\x88\xa1\x11\xb6\xca\xa4\xba!h\x1b\xa3*o\x0c\x10O\x80\\I\x14\x981\xe5\x13\xe3\x1f\x15\xf0MWZ\x85G\xfb\x15\xc8i\x8d\x9d\x95\xcb\t\\2Nie\xa3\x80\xd4\xa6.O\xfcu~\x00D\xfc\xb5L\xb2\xf0\xd3^P:\x1cH\xd8%S\xea\x8a^\xf5L\xfa\xde8 \x8b\x8b\xbc\xfdi\x10\xdd\x0b\xe05>\xb1\xee\x91\x96\xfaR7\xf1rnz\x96\xc1\x8d|\x0b\x01\x072\x06\xe7_\xba\xf9a$\x10\xcf\xd8|I\xbcc\xa1\x82{[v_\x8c\xfd\x93\t\xdc\x98N\xaa\xa7[\xb7\xce\xe9\xdd\x00_\xee\xfb\xbf\x91$\x97\xc2\x18i\xc6\x02\xa9;\xe7\xb8\xe2\x17\x00\xb6\xf8\x9c\xfd/\x98o\x94\xa9\xc2\x03\xd5ug1,\x92\xf5m\x06\xf6\xcb\xa4\xf2\xe7_\xc2\xd0I[\x1b\xc6\x03Y\\\xec\xed\xaf2\xd3O\xdaT\xd9;\x01\xfa\\\x19\xec\xed\xcc\xea1\xaa\xa7\xa5\xa5\xde\xa9M\xbd\x08:\x1a\x0b \x9e\xdf;\\{}\x02\xf4k\x00oi\xe8\xc0\xde)\xc2\xc6Y\xdb\xb9\t\xd0Z\xd3\x7f\x89\xf7b86@<Gv\xbd\x9c\xbe\xa0<_\xf9#@\xefjw\x8c\x80i\x93cT\xbd@\xd4\xbf\x1f+ u\xa3s\xae\xf8\x17\x03\x8dP\x08\x01/g,\xb5\xb2_\xa7M.7v@r%q\x0b3~\xd8\x14\x95\xebi\x1d-\x89\xae\xa8a\x8e\x15\x10\xa7(\xae\x07\xe1>\x9f(^X\xe5\x82\xb3a\xbb;vSV\xae\x94\xbe\x8a\x99\x1fjnoi\x8fL\xe6m\xc7\x15\x8f\xeb\xcc>\xc6#\x04\xc0N\xd7^_\x01\xed\xf6\x9d\xb4?\xb801?u\xcd\xf93/y\x02-\xc9\xa9\x8c\xe9\xaft\xcf\x17\xe3\xa7\xac\\\xd1~?S\xa2\x00p\xb2\xf6t\x1e[(\'\xa6\xae\xb9p\xd7q\xff\xd3z6\xc4\xb1\x8c\x07\xf2\xe0\x89\x8d\x17ONT\xbc\x91Q\xcb\x8dP\x89\xb8bgR\x85\xa7:M\x1d\xe3\x1e\xe95\x1a\xc8\x83/nX9Y^\xe1\xc1\xa8_q(\'\xc0S\x9bz\x84\xe2\xc79\x17b2\x10rJ\xe9\x02\xb8\x190$\xa2\xab3\xc9\xfc\x1fz-\xaa\xe3\x9c-4\x16\x88S\xb4\xb7\x83\xe8Z_\x88\xe4\x06\x99R[{\xc1\xa8\x7f\xdf\x96O?!-\xd5<\x8f\xd5o##*g\xdc\xa2\x9es\xedY\x065\xf3\x1a\x84[3I\xd5z-\xbb\x87X\xb5\x13\'\xcf\x028\xa7Z\x94)\'S\xf9Hn\xcd\x86\xcd\xcd\x18 \xde=\x8d\xff\x95Vx\x91\xdb\xf75\x9d\xa4\xbb\xa4\x95\xff\xf6 Ng]\xb1\xc3\x8bo\xf9\xea\x0e}\x92e\x10;\x82\xd61\x02H\x97{\x1aC\xe75\x1c7}\x1c\xe07\xd6DyVZ\xea\x92\xa0\x02\xe9.?r \x9d\xeei\x00\xd8\'-\xd5z\xfcs\x00e\x1cW\xb4\x9eda\xec\x97)\xb3\x93W#\x05\xa2\xe3\x9eF\x87\xe3\xa4\xa1\x1eW\x1d\xe09Y\xb6\xca\xc8\x808%\xf1\x08\x18\x97\xd5\xad\x8b\xf2\x9e\x86\xe3\x8a\'\xe1{WIX\xc7U\xc3\x861\xb2mo\xd6\x15\x7f\xa1\xd6K\x96\x91\xdf\xd3\x88\xe2\xb8\xea\xd8\x03Q\xae\xbdz\x01\xb4\x8d\x81\xe6\xfa@8|\xde\xaa\xf95:\xeei8\xaeh\x1cW%\xc2\xf1LR-\x1e]5\xe8\xa3m\xca\xca\x96\xd2\x1f&\xe6m\xcd\xb8Tu\x80\xceH+\xdf\x98\xb6\xa2\xd6e\xe9"\xcfy\x99*l\x8c\xba\xdf \xedk\x01\xe2\xfc{\xeaZPb[\xcb\x1b\x1e\x08\xb7\xc8\xa4\xfaq\x10c\xc3(\xeb\xb8"\x07\xa0\xf1V\t\xd3r\xf1\x91\x03qJ\xe2f\xb0\xef\x05h\x8c\xd3\xe0\xcaf\xf9\xba\xdd\xbf\x0fC\xe0A\xdap\\\xfbo\x00\xbd\xadV\xd7\xa8\xd3*\x91\x02i\x0b\x87{\xfe\x1fc\xa2\xcd\xd3\xc9\xfc\xec B\x86U\xc7\xbb\x00j\xeay\xae\xc8\x808\xaex\x04hnk\xbdK\xf9\x93\xe0\xcd\xc2*\xcc\x85%\xec0\xed\x98z\xe21\x12 K\x9c\x05\x1d\x92V\xbe\xf5\xd5M\xc3\xa8\x19R]\xc75\xefLp\xe8@:L\x07\x7f\x95\x96Zr\xb0-$M\x87n\xa6\xfd\xd4<\x80Yi\x9dE\xef:1y\xc1\xecF\xaf\xc3m\xe0Pbi\x83<-\xa1\x8e\x10\xd3\xb7\x94\xcb\t\x94-\xda\x8f\x13Q\xf35\x1f#\xda\x96\x87\x06d\x1c~t\xf5zb\x9d\xa2x\n\xe4\xcb\xc7T*\xd7\xe9\xde\x9e\x87\x08\xc4>\x0eP5\xf7`jX\xa2\x17\x10\xef\xfb\x9c+f\x1a\xa1\x1d\xc6iN\xd0:\x9d\xdb\xf4P\x80\xe4N\xda\x0eW\xc8{el\xfd3\x16\xd9\xb9N\x80\xbcx\xdb<h\x9f/\xc4sl\x05x\x9d\xae\xed\xfa\xd0@:$\x81v\xca\x94\xf2\xc3\xe9\xe7\xc14\xaaL5\xeeV\xe1}\xf5P\x8f\xce\x17\x9b\r\r\xa4e\x88\x83\xfe)\xad\xfc\xc5F\xa9;\xa01\xd5\xf8["\xb1\xbdQ\x9dqD\xa6T\xe7\xb7z\x0f\xd8G\xa7jC\x01\xc9\xb9\xe26\x06\xbe\x7f6LU\x9d\xc4Y\x12\x87#\xde!\x93\x85\xabB\xd4\x7fISC\x01q\\\xfb[\x00}\xb3\xb6\x90\x7f#\x93T\xdf\x8d\xd2\xd8Q\xb4\xed\xb8i\xef\\\xf1\xe2\xcb\x0c\x08/\xc9\xa4:?J;\x86\x02R\xdb\x95\xdc\xc6\xe0\x95\xd2*\xdc\x15\xa5\xa1\xa3l\xdb)\x89\x17\xc1\xa8\xde\xd0b\xe6\xafO\xa7\n\xbe\x0bC\xe1Z64\x90p\xcd1\xb3\xb5l\xd1\xbe\x95\x88~P\x9b\t^\xc8$\xd5\xaa\xa8,\x8d\x81\xf4\xa9l\xae$N2\xd7nk\x11= \x93\xf9\xcf\xf4Y5P\xb1\x18H\x9fr9E\xf10\x08\xd5to\x94\xdb\xe0\x18H\xff@r\xa0Z\xea\x97\x11\xd9o\xad\x18H\x9f@\xb2\xae8B\xc0\xa5\xd5\x85\x1d8:m\xa9w\xf7Y5P\xb1\x18H\x9fry\x7fH\x12D\x8b\xebF\x88\x7f&\xaf\xbd\xfb\x18H\x9f@\xbcbU(\x00\xc2\xfe\xcbl~\x13b \x01\x80\xe8(\x1a\x03\xd1\xa1r\x80>b \x01\xc4\xd2Q4\x06\xa2C\xe5\x00}\xc4@\x02\x88\xa5\xa3h\x0cD\x87\xca\x01\xfa\x88\x81\x04\x10KG\xd1\x18\x88\x0e\x95\x03\xf4\x11\x03\t \x96\x8e\xa21\x10\x1d*\x07\xe8#\x06\x12@,\x1dEc :T\x0e\xd0G\x0c$\x80X:\x8a\xc6@t\xa8\x1c\xa0\x8f\x18H\x00\xb1t\x14\xfd?\xa6\x01\x84\x92_F\xb3\xf4\x00\x00\x00\x00IEND\xaeB`\x82')
    open('xox_o.png','wb').write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00d\x00\x00\x00d\x08\x06\x00\x00\x00p\xe2\x95T\x00\x00\x08\xfeIDATx^\xed\x9dk\xac]E\x15\x80\xbfu\xdbF\xc5\xc4\x07h\x14m}\x82\x0f\x8cAmE\xe3\xfb\x8d\xa0\xa8X\xd4\x9f\xfe\xd0`T|\xf0\x1b\xcaY\x87\xd6\xdf\x8aoM\xfc\xe1?m\x01\x15\xa9<\x02\xa8\x08Dm!\x1a\x14\x89\xd2J\xa1\x16H\x10\x8a\x89PSz\x97\x99}\xe7\xdc\xce\xdd\xf7\xdc\xc7\x9e={\xef9\xe7\xeeInr\xef={f\xd6\xacof\xcd\xec\x995\xeb\x08}\xcaJ\x03\x92\x954\xbd0\xf4@2\xeb\x04=\x90\x1eHf\x1a\xc8L\x9c~\x84\xf4@2\xd3@f\xe2\xf4#\xa4\x07\x92\x99\x062\x13\xa7\x1f!=\x90\xcc4\x90\x998\xfd\x08\xe9\x81d\xa6\x81\xcc\xc4\x99\xd8\x11\xa2\xc6\t\x06o\x10\xf8\np\x92\xc0\x15\x03\xe1;\x99\xe9\xb7\xb28\x13\x03D\x8d\x17\x00\xdf\x00^!0c\xf0\xdark\x05.\x98t(\xd9\x03Qc\x97\xc1f\x81\x97\xae\xd4\xddz +i\xa8\xc6\xe7\x97\x18g\xcd\xc0\x8f\x80\x93\x97*F\xe0N\xe0q\x83G\x04vO\xfa\xe8p\xed\xccn\x84\xec06=\t\xdb\x81O\x8f\x01\xb1O\xe0?\x06\xff3x\xa6\xc0\xac\xc0\x89\x0e\x08\xf0\xa0\x83\xa3\xc2Gj\xf4\x83\xce\xb3f\x05D\x8d\x9f\x01\xe7\x00\xeb\x02\xcd<\t\xfc\x12\xb8@\xe0\\\x83o\xaf\xa0\xb5\x87Uxn\xe7\x9a\x8d\x14 \x0b C+VJC\xd7\xebK\xed\xf8\xf1z\xd8v\xb1p\xbf\xfb\xff\xd0\xf8\xe2*\x80\xb8G\x8f\x02\xd7\xab\xf0\xe1H\xbdt\x96\xadS j\\\r\xbc\x15xVI\x03\x0f\xcc\xc2g.\x15\xae)k\xc6C9\x1bx\xb1\xb7\xb9\x85\xc92\xd8(\x8b\x81\xde\xa72\xf7\xdc\xa4\xa4\xce\x80\xa8\xb1\x17\xd8\x1c*J\xe01\x83\x1bU\xd8\x1a\xa3@\xb5b\x92\x7f%\xb0!\xc8\x7f\x84\xb92\'b\xb4t\x02d`\xfcQ\xe0\x8d\x81\xd2\x0e\x0b\xe8@\xb8,\x06D9\x8f\x1a\xf7\x01\x9bJ\xff\x9f\x88\xd1\xd2:\x105n\x00\xde\x1b(\xeb\x16\x15\xde\x9e\x02DX\x867\x87\xae\x9e\xa7N\xd2hi\x15\x88Za6\xdc\x8ai\x94nS)\xe6\x90\xc6\xd2\xb8\xd1"p\xff@xQc\x95\xd6(\xb85 _3N>J1o\xb8-\x10\x97\xeeV\xe1\xd55d_u\xd6%F\xcb\xdd\x1b\xe0=\x17\t\x0f\xac\xba\xa0\x16\x1el\r\x88\x1a\x7f\x03^\xe5\xdbth\x03li[\x19j\x1c\x80\x05#\xe3\x10\xf09\x95b\xb5\x97Ej\x05\x88\x1a\xb7\x02o\tZ|NWJ\x18\x1a7\xd8\xc29\xcc\x89u\xad\ng\xe5@\xa4q j\xec\x01\xb6\x8c\x1a+p\xe3@x_\x97\x8d\xf7s\xd9\x0f\x02\xf3\xe9\xc494\x0b\x9f\x1d\xf7\xee\xd3\xa6\xac\x8d\x02\xf1\xb6\xfbC\x01\x8c=\x03\xe1\x8c6\x1b\xb8T]~N\xfb\x8d\xdb\xce/=\xb3`w\xa0mY\x9b\x06\xf2D\xb0\xecldy[Waj\xc5\xaa\xef\x83\xc0\xfa\xa0,\xb7\x7fvM\x17\x1b\x95\x8d\x01)M\xa0GTxZ]\xe55\x95\x7f\x99\x1d\xe6\x03\xc7`\xebv\xe1\xf6\xa6\xea.\x97\xdb\x08\x105\xae\x03>\x10T\xb6{\x12\xb6.\x969\x83\xb9Ie\xc1\xcblc|\x92\x03\xd9fl^7\xf7\xbe1J\x07U\x16mc4\xd6\xa0\x14\x05{3V\xde\xfbj\x05Jr j\xdc;\xda\x895\xf8\xe7PxY\n%\xb5]\x86\xefX?\x05^>\xaa\xfb\x18li\xda|%\x05\xa2\xc6n\xc0m\x8d\x17\xa9\x8d\x064\rJ\x8d{\x02(\xf7\xa8pj\x93u&\x03R6U\xfe\x8c{"\xb6\xbc\x97S\xf0\x18\x13\xecV\x8e7\xab\x14+\xb3\xe4)\x19\x90\xd0T\x01\x07TxIri;*P\x8d\x9b\x80w\x87\xd5\x0b\\7h\x00J\x12 j\xfc\x02\x8e;\x17L\x83\xa9*\xb3W\xe3Z\xe0\x1d0\xbf|\x7fB\x85\x13R\xf7\x91\xda@\xd4x\x8e\xc0A\x83\xa7x\xe1\xaeV)\x1c\x15\xa62\xa9\xf1x\x00%\xf9\xcbn\n \xdf\x04\xbe\xe4\xb4/\xf0\xd0@x\xfeT\x92\xf0\x8d*o\x07\x19\xec\x19&\xdc\x0e\xaa\x05\xe4Rc\xf3l\xf0\xce!p\xde@\xb8b\x9a\x81\xb8\xb6\x957L\xdd\xa1[\xaam\x96Z@\xd4\xb8\xca\xfbQ99\x93\t5\t@\xd5\xb8\x19\xe6\x8f\x9e\xff\xa2\xb2\xd8\xd78\xa6\x1d\xd1@\x86\xc6V\x83\xcbG\x95\xce\xc0\x96KZ\xdc\xf3\x89il\xca<\xdb\x8c\xd3\xd7\xc1\x9f|\x99\x0fi"S]\x07\xc8\x83\x06\xcf\xf3\x02}K\x85/\xa7l\xf0$\x94\xa5V\xb8\xaf\x16:8\x06\xaf\xdb.\xfc\xb9\xae\xdcQ@\x9cG:p\x9e\x9f\xc8\x9d\x9f\xedF\x15\x1e\xae+\xcc\xa4\xe5W\xe3\xaf\xc0i^\x0f\xee~J\xa1\x93:)\n\xc8\xc0\xd8\x1f\\\x0f\xb82\xd6\xb1\xad\x8e\xe09\xe4\r;&pX\x85g\xd7\x95\xab2\x10\x7fq\xe6_A\xc5/T\xc19\x0b\xac\xc9\xa4\xc6\xa3#WX\x81\xaf\xd6u\xf6\x8b\x01\xf2\x13\xe0S^\xfb\xfbU\x8e\xef\x86\xaeE"\xceQ\xdc\xe6nv\xb9T{\x94\xc4\x00\xd9\x07\xf3[\xea;U\xe6\xe1\xacE\x1eE\x9b\xc3Q\x02\\\xae\xc2\'b\x95Q\tHo\xae\xc6\xabY\x8d+\x81s\xfd\xa7w\xa8,t"\xaf\x02\xa7*\x90\xd0\\\xb5\xe6yX\xa5A]<\xabV\x1cW\xbbck\x97nU\xe1m\xb1rT\x05\xf2k\xe0]\xbe\xb2_\xa90\xef\xe2\x13+\xc04\xe4Sc#\xcc]*\x02\x1eU\xe1\xc4\xd8vU\x05\xa2\xc0\xc0W6T\xc1\xfd\xdd\xa7\xb9y\xc4\xdds\x1c-{7\xa9p0F1U\x81\xb8\x1bM\xa3\x932wj\xf6\xce\x98J\xa71\x8f\x1a\xb7\xf8\xdb`\xaeyg\xaap}L;\xab\x02\xf9/\xcc\x1f\xca\xecR\xe1\x931\x95Nc\x9e\x92\xffr\xb4\xaf\xf0\xaa\x81\xa8\xb1\x13\xe6\x97s\xee\xfa\xf1\xd3\xa7Q\xb1\xb1mR\xe3\x0e\xe0\xf5>\x7f\xf4\xcew\x15 \x7f\x87y\x8f\x8b\xbbTxM\xac\xf0\xd3\x98/\xd5Fc\x15 \xa1\x8bO\xbf\xc2\nzU\xca\xad\xf8*@\xfa\x15\xd6\x12C\xbbtPW\xcbzT\x01\xf2[\xefu\xe1\xc4\x8a\x9e\xb4\xa6\xcd\\\x8d\xf1\xdb\xaa\xb5\xfb\xbdj Cc\xa7\x1d\x9f\xd4\x1fQ\xe1\xa4iSnL{J\xfeh\xf7\xaa\xac\x1c\xb5h\xb9zV\r\xc4\x15\xa2\xc6\xbfa\xee-4\xc5Vs\x8c\x02r\xca\xa3V8t||$S\n\x7f\xb4J@\xc2\xadf\x17ua \x8bBb\xe4\xa4\xaf\xc6eQ#\xdc\xf9\xbeJ\x85\x8f\xd6\xad\xb4\x12\x10W\xd9\xd08<\n\x12#\xb0k\xb0F_\x0e\x9b\xda\xf9\xae\x0c$<\xb6\x9c\xe4\xeb\x06u{r\xc9\rh\x9f\n\xa7\xd4-\xd3O\x05\xd5\x8ai\xaagT\x93\xa2\xdb\xa7\xd5\xf8.\xf0\xf9@\x8a\xe87\xf3rK*\x8f\x10W@\xc9\xc9\xa1\xd6\tY\xb7\xaa\xad^\xfb\x18\x18{U\x16\x04\xd2\xa9^h\x90#\nH\xb8\x046xl\xb8F&w5~\x0f\xbc)\xd0\xdf\xf7T\xf8B-\x02\xa5\xccQ@\xfc(q!\x95\x8a\x08pka\t\xdc\x06\x8c\xa89d\x044\xb5\xb7E\xca^\x96\xba\xac1f\xea\x0f*\xbc9u=\xb5\x80\xb8\xcc%o\x8b\xe4w%\x9ahp\xd52\xc7\x8c\x8c\xc6`\xa4\x00\xe2\xa2\xe8\x84\xe7\xeaI\'\xb8\xaa\xcaK\xfd|[f*\x94;z\x0e\x19\x152&vb\xb2%`j\x05W)\xafM3\x95\x14\x887]\xe1]\x89d/IU\x14\x98\xf2Y5~\x07\x0b\\y\x1a5SM\x00qQ\xe2&\xde\xdf\xd7/T\xdc\xb9O\x18\xb66\xf9\xd2v\xb9\xceS\xdbd\x05\xa6+<\xe2\xbds\x03\x9c\xd9v\xc4\xb8\xd8Q\xe2\x039_h>\x16pP\xce\xed*\xc7c}\xc5\x96_%_J \x0b\xa28\xb8\x80`\xb9\x85\xcf\x0b\x15\xe3\xb7\x80.3x\xff\x98\x00\xcc\x87\xbd\x07b\xeb\x81\x0f\x92\x01\xf1sI\xe8\xd9X\xb4\xdfEt08?\x87+\x0b\x1e\xc2\xc7\xbc\x1f\xee\xa2\xa8vB\x11\x93\xf1\xebu\xaf\x14T\x19\x11\xe5g\x93\x02\xf1P\\\xaf*\x87\xcfs\x1f\xed\x07\x9c#r\xb4gxLC/6N]\x0f;|\x98\xc1\xb1\x81p\xdc\xf6\xcf\x0c\x0c\xba\x041j[r \xae\xe0e\xc2\xe7\xb9\x8f\x97\x8c\xeb\x1e\xa3\xf0r\x1e5f|\xac.\xe7\x00\xed~\x96tWr\xc7\x073\xb07\xa73\x9dF\x80\x04\x13\xbds\xd3?=\xb8O\x12\xea/IlC\xef\xe8\xec\xee\xf9\x9dop\x9a\xbfj\x17F\xb3.3s\x91\xb5\xdd\xd7b\xfc<\x073\xda\xb8\xc9\x1a\xd7\xcb\xbd\xedv\xdf\xfb\xe1Bn\x94c\x1b\xbay\xe7\xb61\xf9F\xb1\xe1]T\xd3\xf0\xf73\x04\x9eas\x19\x1c\x88\x95\xee\xf5\x1dqs\x83Q\xdc\x90\xbd0G\x08\xc9\xdfCVkjV\xf8\xf6\x9c\xd5\x16\xb3\x9a\xe7\xdc\xedX\xe7\xec\\\xfc\xa80\xbb\x9aL9<\xd3\xa8\xc9Z\xaa\x81>\xb6\xe1\xf7KQ\xa6c\xf5\xe1.]\xde\xe5\xa2\x9f\n\xec?\n\x17\xed\x10\xfe\x11[X\xd7\xf9:\x01\x12\xcc1\xee\xbe\xbb\xfbz"\x17?\xb7\x9c\x962Y\xee\x9b\x14\x1c\x84\x1f:\x10\xb1\xf70\xbaV\xfcR\xf5w\n$W\xa5t)W\x0f\xa4K\xed\x8f\xa9\xbb\x07\xd2\x03\xc9L\x03\x99\x89\xd3\x8f\x90\x1eHf\x1a\xc8L\x9c~\x84\xf4@2\xd3@f\xe2\xf4#\xa4\x07\x92\x99\x062\x13\xa7\x1f!=\x90\xcc4\x90\x998\xfd\x08\xe9\x81d\xa6\x81\xcc\xc4\xf9?3\xe5\x94\x83\xcf%\xad(\x00\x00\x00\x00IEND\xaeB`\x82')
    xpng=pygame.image.load('xox_x.png')
    opng=pygame.image.load('xox_o.png')
def draw():
    pygame.draw.rect(scr,(0,34,64),(0,0,300,300))
    pygame.draw.line(scr,pygame.Color(255,255,0), (100,0), (100, 300))
    pygame.draw.line(scr,pygame.Color(255,255,0), (200,0), (200, 300))
    pygame.draw.line(scr,pygame.Color(255,255,0), (0,100), (300, 100))
    pygame.draw.line(scr,pygame.Color(255,255,0), (0,200), (300, 200))
    pygame.draw.line(scr,pygame.Color(0,0,0), (0,300), (300, 300))
    flip()
def XOX_OFFLINE():
    loadImages()
    DICT={0:[0,0],1:[0,1],2:[0,2],3:[1,0],4:[1,1],5:[1,2],6:[2,0],7:[2,1],8:[2,2]}
    PDICT={0:(0,0),1:(100,0),2:(200,0),3:(0,100),4:(100,100),5:(200,100),6:(0,200),7:(100,200),8:(200,200)}
    CONDT=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    clock = pygame.time.Clock()
    scr.fill((0,34,64))
    draw()
    pygame.draw.line(scr,(0,0,0),(150,300),(150,340))
    pygame.draw.rect(scr,(0,0,0),(225,313,20,10),1)
    pygame.draw.line(scr,(0,0,0),(235,323),(230,328))
    pygame.draw.line(scr,(0,0,0),(235,323),(240,328))
    pygame.draw.line(scr,(0,0,0),(230,328),(240,328))
    pygame.draw.ellipse(scr,(0,0,0),(60,315,16,24),1)
    pygame.draw.line(scr,(0,0,0),(62,330),(74,330))
    pygame.draw.circle(scr,(0,34,64),(68,315),6)
    pygame.draw.circle(scr,(0,0,0),(68,315),6,1)
    pygame.draw.rect(scr,(0,34,64),(60,331,16,9))
    backXOXOFF=pygame.draw.circle(scr,ButtonColor,(2,338),35)
    restart=pygame.draw.circle(scr,ButtonColor,(298,338),35)
    scr.blit(pygame.font.Font(None, 55).render('<', True, (100,100,100)),[5,306])
    pygame.draw.circle(scr,(100,100,100),(285,324),12,3)
    pygame.draw.circle(scr,ButtonColor,(276,324),5)
    pygame.draw.lines(scr,(100,100,100),False,[(275,313),(275,320),(283,320)],4)
    flip()
    def qtXOXOFF():
        os.remove('xox_x.png')
        os.remove('xox_o.png')
        raise Exception()
    def checkfull():
        global tableXOXOFF
        for i in tableXOXOFF:
            for n in i:
                if n==0:
                    return False
        return True
    def check():
        global tableXOXOFF, turnXOXOFF, scoreXOXOFF
        for i in CONDT:
            if tableXOXOFF[DICT[i[0]][0]][DICT[i[0]][1]]==1 & tableXOXOFF[DICT[i[1]][0]][DICT[i[1]][1]]==1 & tableXOXOFF[DICT[i[2]][0]][DICT[i[2]][1]]==1 :
                if playerXOXOFF=='X':scoreXOXOFF[0]+=1
                else:scoreXOXOFF[1]+=1
                if scoreXOXOFF[0]>=100 or scoreXOXOFF[1]>=100:qtXOXOFF()
                refresh_score()
                sleep(0.5)
                pygame.event.clear()
                tableXOXOFF=[[0,0,0],[0,0,0],[0,0,0]]
                turnXOXOFF=random.randint(0,1)
                draw()
            if tableXOXOFF[DICT[i[0]][0]][DICT[i[0]][1]]==2 & tableXOXOFF[DICT[i[1]][0]][DICT[i[1]][1]]==2 & tableXOXOFF[DICT[i[2]][0]][DICT[i[2]][1]]==2 :
                if playerXOXOFF=='O':scoreXOXOFF[0]+=1
                else:scoreXOXOFF[1]+=1
                if scoreXOXOFF[0]>=100 or scoreXOXOFF[1]>=100:qtXOXOFF()
                refresh_score()
                sleep(0.5)
                pygame.event.clear()
                tableXOXOFF=[[0,0,0],[0,0,0],[0,0,0]]
                turnXOXOFF=random.randint(0,1)
                draw()
            if checkfull():
                sleep(0.5)
                pygame.event.clear()
                tableXOXOFF=[[0,0,0],[0,0,0],[0,0,0]]
                turnXOXOFF=random.randint(0,1)
                draw()
    def refresh_score():
        global scoreXOXOFF
        pygame.draw.rect(scr,(0,34,64),(90,310,26,20))
        pygame.draw.rect(scr,(0,34,64),(190,310,26,20))
        scr.blit(pygame.font.Font(None, 25).render(str(scoreXOXOFF[0]), True, (50,200,50)),[93,312])
        scr.blit(pygame.font.Font(None, 25).render(str(scoreXOXOFF[1]), True, (250,150,0)),[193,312])
        flip()
    def restartXOXOFF():
        global tableXOXOFF, turnXOXOFF, botXOXOFF, playerXOXOFF, scoreXOXOFF
        tableXOXOFF=[[0,0,0],[0,0,0],[0,0,0]]
        turnXOXOFF+=random.randint(0,1)
        botXOXOFF=random.choice(['X','O'])
        playerXOXOFF='X' if botXOXOFF=='O' else 'O'
        scoreXOXOFF=[0,0]
        refresh_score()
        pygame.draw.rect(scr,(0,34,64),(118,304,30,30))
        pygame.draw.rect(scr,(0,34,64),(155,304,30,30))
        scr.blit(pygame.font.Font(None, 55).render(playerXOXOFF, True, (50,200,50)),[118,304])
        scr.blit(pygame.font.Font(None, 55).render(botXOXOFF, True, (250,150,0)),[155,304])
        draw()
    def engn():
        global tableXOXOFF, turnXOXOFF, botXOXOFF, playerXOXOFF, scoreXOXOFF
        turnXOXOFF=random.randint(0,1)
        botXOXOFF=random.choice(['X','O'])
        tableXOXOFF=[[0,0,0],[0,0,0],[0,0,0]]
        scoreXOXOFF=[1,1]
        refresh_score()
        playerXOXOFF='X' if botXOXOFF=='O' else 'O'
        scr.blit(pygame.font.Font(None, 55).render(playerXOXOFF, True, (50,200,50)),[118,304])
        scr.blit(pygame.font.Font(None, 55).render(botXOXOFF, True, (250,150,0)),[155,304])
        flip()
        while True:
            if turnXOXOFF%2==0:
                pygame.event.clear()
                i=inp() if botXOXOFF=='O' else bot_choose()
                if i==30:
                    restartXOXOFF()
                    continue
                scr.blit(xpng,PDICT[i])
                flip()
                tableXOXOFF[DICT[i][0]][DICT[i][1]]=1
            else:
                pygame.event.clear()
                i=inp() if botXOXOFF=='X' else bot_choose()
                if i==30:
                    restartXOXOFF()
                    continue
                scr.blit(opng,PDICT[i])
                flip()
                tableXOXOFF[DICT[i][0]][DICT[i][1]]=2
            check()
            turnXOXOFF+=1
    def bot_choose():
        availables=[]
        for k in range(3):
            for l in range(3):
                if tableXOXOFF[k][l]==0:
                    availables.append((k*3)+l)
        return random.choice(availables)
    def inp():
        clock.tick(60)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if backXOXOFF.collidepoint(event.pos):
                        qtXOXOFF()
                    if event.pos[1]<=300:
                        if event.pos[0]<=100:
                            if event.pos[1]<=100:
                                i=0
                            elif event.pos[1]>200:
                                i=6
                            else:
                                i=3
                        elif event.pos[0]>200:
                            if event.pos[1]<=100:
                                i=2
                            elif event.pos[1]>200:
                                i=8
                            else:
                                i=5
                        else:
                            if event.pos[1]<=100:
                                i=1
                            elif event.pos[1]>200:
                                i=7
                            else:
                                i=4
                        if tableXOXOFF[DICT[i][0]][DICT[i][1]]==0:
                            return i
                    if restart.collidepoint(event.pos):return 30
                if event.type == pygame.QUIT:
                    qtXOXOFF()
    engn() 
    pygame.quit()
    os.remove('xox_o.png')
    os.remove('xox_x.png')
def XOX(key=None,condition=None,join_name=None,RK=None,re=None):
    global scr,f,ftppass
    def turn_mark(place=0):
        if not RK:place=1 if place==0 else 0
        pygame.draw.rect(scr,(0,34,64),(100,301,10,39))
        scr.blit(pygame.font.Font(None, 20).render('>', True, (250,250,0)),[100,302+(place*22)])
        flip()
    def checkfull():
        global table
        for i in table:
            for n in i:
                if n==0:
                    return False
        return True
    def check(a):
        global table, SCORE, OppNameXOX
        if join_name:OppNameXOX=join_name
        for i in CONDT:
            if table[DICT[i[0]][0]][DICT[i[0]][1]]==1 & table[DICT[i[1]][0]][DICT[i[1]][1]]==1 & table[DICT[i[2]][0]][DICT[i[2]][1]]==1 :
                if this==b'\x10':
                    if RK:SCORE[0]+=1
                    else:SCORE[1]+=1
                else:
                    if RK:SCORE[1]+=1
                    else:SCORE[0]+=1
                XOX(key=key,condition=condition,join_name=join_name,RK=RK,re=[SCORE,OppNameXOX,a])
            if table[DICT[i[0]][0]][DICT[i[0]][1]]==2 & table[DICT[i[1]][0]][DICT[i[1]][1]]==2 & table[DICT[i[2]][0]][DICT[i[2]][1]]==2 :
                if this==b'\x11':
                    if RK:SCORE[0]+=1
                    else:SCORE[1]+=1
                else:
                    if RK:SCORE[1]+=1
                    else:SCORE[0]+=1
                XOX(key=key,condition=condition,join_name=join_name,RK=RK,re=[SCORE,OppNameXOX,a])
        if checkfull(): XOX(key=key,condition=condition,join_name=join_name,RK=RK,re=[SCORE,OppNameXOX,a])

    def redraw():
        global scr, backXOX, SCORE
        scr.fill((0,34,64))
        pygame.draw.line(scr,pygame.Color(255,255,0), (100,0), (100, 300))
        pygame.draw.line(scr,pygame.Color(255,255,0), (200,0), (200, 300))
        pygame.draw.line(scr,pygame.Color(255,255,0), (0,100), (300, 100))
        pygame.draw.line(scr,pygame.Color(255,255,0), (0,200), (300, 200))
        pygame.draw.line(scr,pygame.Color(0,0,0), (0,300), (300, 300))
        pygame.draw.line(scr,pygame.Color(0,0,0), (170,300), (170, 340))
        pygame.draw.line(scr,pygame.Color(0,0,0), (140,320), (300, 320))
        pygame.draw.line(scr,pygame.Color(0,0,0), (140,300), (140, 340))
        backXOX=pygame.draw.circle(scr,ButtonColor,(2,338),35)
        scr.blit(pygame.font.Font(None, 55).render('<', True, (100,100,100)),[5,306])
        scr.blit(pygame.font.Font(None, 23).render(key, True, (50,200,50)),[175,304])
        if re[1]:scr.blit(pygame.font.Font(None, 23).render(re[1], True, (250,150,0)),[175,322])
        scr.blit(pygame.font.Font(None, 23).render(str(re[0][0]), True, (50,200,50)),[147,304])
        scr.blit(pygame.font.Font(None, 23).render(str(re[0][1]), True, (250,150,0)),[147,324])
        pygame.draw.line(scr,(0,0,0),(110,300),(110,340))
        pygame.draw.line(scr,(0,0,0),(110,320),(140,320))
        player='X' if this==b'\x10' else 'O'
        opponent='X' if player=='O' else 'O'
        if join_name:
            scr.blit(pygame.font.Font(None, 23).render(opponent, True, (50,200,50)),[120,304])
            scr.blit(pygame.font.Font(None, 23).render(player, True, (250,150,0)),[120,324])
        if RK:
            scr.blit(pygame.font.Font(None, 23).render(player, True, (50,200,50)),[120,304])
            scr.blit(pygame.font.Font(None, 23).render(opponent, True, (250,150,0)),[120,324])
        flip()

    def gui_init():
        global scr, clock, backXOX,SCORE
        clock = pygame.time.Clock()
        scr.fill((0,34,64))
        pygame.draw.line(scr,pygame.Color(255,255,0), (100,0), (100, 300))
        pygame.draw.line(scr,pygame.Color(255,255,0), (200,0), (200, 300))
        pygame.draw.line(scr,pygame.Color(255,255,0), (0,100), (300, 100))
        pygame.draw.line(scr,pygame.Color(255,255,0), (0,200), (300, 200))
        pygame.draw.line(scr,pygame.Color(0,0,0), (0,300), (300, 300))
        pygame.draw.line(scr,pygame.Color(0,0,0), (170,300), (170, 340))
        pygame.draw.line(scr,pygame.Color(0,0,0), (140,320), (300, 320))
        pygame.draw.line(scr,pygame.Color(0,0,0), (140,300), (140, 340))
        backXOX=pygame.draw.circle(scr,ButtonColor,(2,338),35)
        scr.blit(pygame.font.Font(None, 55).render('<', True, (100,100,100)),[5,306])
        if RK:scr.blit(pygame.font.Font(None, 25).render('Key: '+RK, True, (200,200,200)),[45,313])
        scr.blit(pygame.font.Font(None, 23).render(key, True, (50,200,50)),[175,304])
        if join_name:scr.blit(pygame.font.Font(None, 23).render(join_name, True, (250,150,0)),[175,322])
        scr.blit(pygame.font.Font(None, 23).render(str(SCORE[0]), True, (50,200,50)),[147,304])
        scr.blit(pygame.font.Font(None, 23).render(str(SCORE[1]), True, (250,150,0)),[147,324])
        flip()
    def engn():
        global table
        while True:
            if this==b'\x10':
                turn_mark()
                pygame.event.clear()
                i=inp_xox()
                scr.blit(xpng,PDICT[i])
                flip()
                table[DICT[i][0]][DICT[i][1]]=1
                turn_mark(1)
                ni=ord(playandwait(i))
                scr.blit(opng,PDICT[ni])
                flip()
                table[DICT[ni][0]][DICT[ni][1]]=2
                check(3)
            elif this==b'\x11':
                turn_mark()
                pygame.event.clear()
                i=inp_xox()
                scr.blit(opng,PDICT[i])
                flip()
                table[DICT[i][0]][DICT[i][1]]=2
                turn_mark(1)
                ni=ord(playandwait(i))
                scr.blit(xpng,PDICT[ni])
                flip()
                table[DICT[ni][0]][DICT[ni][1]]=1
                check(3)

    def inp_xox():
        global backXOX
        clock.tick(60)
        clck=time()
        refresh=False
        while True:
            if int(clck-time())%5==0 and not refresh:refresh=True
            if refresh and int(clck-time())%5!=0:
                refresh=False
                try:f.voidcmd('NOOP')
                except:pass
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if backXOX.collidepoint(event.pos):
                        quit_msg()
                        XOX(condition=6)
                    if event.pos[1]<=300 and event.pos[0]<=300:
                        if event.pos[0]<=100:
                            if event.pos[1]<=100:
                                i=0
                            elif event.pos[1]>200:
                                i=6
                            else:
                                i=3
                        elif event.pos[0]>200:
                            if event.pos[1]<=100:
                                i=2
                            elif event.pos[1]>200:
                                i=8
                            else:
                                i=5
                        else:
                            if event.pos[1]<=100:
                                i=1
                            elif event.pos[1]>200:
                                i=7
                            else:
                                i=4
                        if table[DICT[i][0]][DICT[i][1]]==0:
                            return i
                if event.type == pygame.QUIT:
                    quit_msg()
                    XOX(condition=6)
    def dw_xox():
        with open('xox_server', 'wb') as fp:
            f.retrbinary('RETR mistik_'+room, fp.write)
    def read_xox():
        with open('xox_server', 'rb') as fp:
            return (fp.read())
    def up_xox():f.storbinary('STOR mistik_'+room,open('xox_server', 'rb'))
    def write_xox(a):
        with open('xox_server','w+b') as fp:
            fp.write(a)
    def update_xox(firstUp=None):
        global OppJoinedXOX,backXOX,cr_join_name, LoaderCounterXOX, this, OppNameXOX, lastsent_xox
        event=pygame.event.poll()
        if event.type==pygame.QUIT:
            if firstUp:
                if OppJoinedXOX:
                    quit_msg()
                    XOX(condition=6)
                else:
                    quit_msg()
                    XOX(condition=3)
            else:XOX(condition=6)
        if event.type==pygame.MOUSEBUTTONDOWN:
            if backXOX.collidepoint(event.pos):
                if firstUp:
                    if OppJoinedXOX:
                        quit_msg()
                        XOX(condition=6)
                    else:
                        quit_msg()
                        XOX(condition=3)
                else:XOX(condition=6)
        try:dw_xox()
        except:
            try:
                write_xox(last_sent_xox)
                up_xox()
            except:checkconnectionxox()
        if read_xox()==lastsent_xox:
            if (not OppJoinedXOX)and RK and firstUp:
                LoaderCounterXOX=(LoaderCounterXOX+1) if LoaderCounterXOX<5 else 1
                if LoaderCounterXOX==1:
                    pygame.draw.rect(scr,(0,34,64),(175,322,125,25),0)
                scr.blit(pygame.font.Font(None, 22).render('Waiting', True, (200,200,200)),[175,322])
                scr.blit(pygame.font.Font(None, 25).render('.', True, (200,200,200)),[227+(LoaderCounterXOX*6),322])
                flip()
            return False
        elif len(read_xox())>1:
            OppNameXOX=read_xox().decode()
            starter=OppNameXOX[0]
            if starter=='j':
                write_xox(lastsent_xox)
                up_xox()
            OppNameXOX=OppNameXOX[1:]
            pygame.draw.rect(scr,(0,34,64),(175,322,120,25),0)
            scr.blit(pygame.font.Font(None, 23).render(OppNameXOX, True, (250,150,0)),[175,322])
            pygame.draw.rect(scr,(0,34,64),(45,301,95,40),0)
            pygame.draw.line(scr,(0,0,0),(110,300),(110,340))
            pygame.draw.line(scr,(0,0,0),(110,320),(140,320))
            player='X' if this==b'\x10' else 'O'
            opponent='X' if player=='O' else 'O'
            scr.blit(pygame.font.Font(None, 23).render(player, True, (50,200,50)),[120,304])
            scr.blit(pygame.font.Font(None, 23).render(opponent, True, (250,150,0)),[120,324])
            flip()
            OppJoinedXOX=True
            if starter=='j':
                turn_mark(1)
                return False
            else:return chr(99)
        else:
            if read_xox()==b'\x66':XOX(condition=2)
            return read_xox()
    def checkconnectionxox():
        global f
        try:
            f.voidcmd('NOOP')
        except:
            try:
                f=FTP('ftp.dlptest.com')
                f.login(user='dlpuser@dlptest.com',passwd=ftppass)
            except:
                XOX(condition=1)
        try: dw_xox()
        except:
            f.storbinary('STOR mistik_'+room,open('xox_blank', 'w+b'))
            os.remove('xox_blank')
    def playandwait(a):
        global lastsent_xox
        b=bytes(chr(a),encoding='ASCII')
        dw_xox()
        if read_xox()==b'\x66':
            XOX(condition=2)
        write_xox(b)
        up_xox()
        lastsent_xox=b
        check(1)
        while True:
            updt=update_xox()
            if updt:
                return updt
    global room, lastsent_xox, xpng, opng, table, DICT, CONDT, PDICT, first, this, OppJoinedXOX, LoaderCounterXOX, SCORE
    if key:room=key
    if condition:
        if condition==6:
            write_xox(b'\x66')
            up_xox()
            os.remove('xox_x.png')
            os.remove('xox_o.png')
            os.remove('xox_server')
            raise Exception(1)
        os.remove('xox_x.png')
        os.remove('xox_o.png')
        os.remove('xox_server')
        if condition==2:
            button(150,150,50,(100,100,200),200,'',0)
            scr.blit(pygame.font.Font(None, 40).render('Opponent left.', True, MessageColor),[50,110])
            scr.blit(pygame.font.Font(None, 40).render('QUITTING...', True, MessageColor),[85,170])
            flip()
            raise Exception(2)
        if condition==3:raise Exception(2)
        raise Exception(1)
    if not key:return 'NoKey'
    OppJoinedXOX=False
    LoaderCounterXOX=0
    StartTurn=''
    SCORE=[0,0] if not re else re[0]
    table=[[0,0,0],[0,0,0],[0,0,0]]
    DICT={0:[0,0],1:[0,1],2:[0,2],3:[1,0],4:[1,1],5:[1,2],6:[2,0],7:[2,1],8:[2,2]}
    CONDT=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    PDICT={0:(0,0),1:(100,0),2:(200,0),3:(0,100),4:(100,100),5:(200,100),6:(0,200),7:(100,200),8:(200,200)}

    if SCORE[0]>=100 or SCORE[1]>=100:XOX(condition=6)
    loadImages()
    if not re:gui_init()
    else:redraw()
    if (not re) and join_name:
        button(150,150,30,(100,100,200),170,'',0)
        scr.blit(pygame.font.Font(None, 40).render('Loading...', True, (250,150,0)),[92,137])
        flip()
    checkconnectionxox()
    first=read_xox()
    if first==b'\x10':
        this=b'\x11'
        StartTurn=random.choice(['c','j'])
        write_xox(bytes(StartTurn+join_name,encoding='ASCII'))
        up_xox()
    if first==b'\x11':
        this=b'\x10'
        StartTurn=random.choice(['c','j'])
        write_xox(bytes(StartTurn+join_name,encoding='ASCII'))
        up_xox()
    pygame.event.clear()

    if re:
        if re[2]==1:
            if RK:turn_mark(1)
            else:turn_mark(1)
            write_xox(b'\x12')
            up_xox()
            lastsent_xox=b'\x12'
            i=False
            while not i:
                i=update_xox()
            i=ord(i)
            if this==b'\x10':
                scr.blit(opng,PDICT[i])
                flip()
                table[DICT[i][0]][DICT[i][1]]=2
            if this==b'\x11':
                scr.blit(xpng,PDICT[i])
                flip()
                table[DICT[i][0]][DICT[i][1]]=1
    if first==b'':
        this=random.choice([b'\x10',b'\x11'])
        write_xox(this)
        up_xox()
        lastsent_xox=this
        i=False
        while not i:
            i=update_xox(1)
        i=ord(i)
        if i != 99:
            if this==b'\x10':
                scr.blit(opng,PDICT[i])
                flip()
                table[DICT[i][0]][DICT[i][1]]=2
            if this==b'\x11':
                scr.blit(xpng,PDICT[i])
                flip()
                table[DICT[i][0]][DICT[i][1]]=1
    if (not re) and join_name:
        draw()
        pygame.draw.line(scr,(0,0,0),(110,300),(110,340))
        pygame.draw.line(scr,(0,0,0),(110,320),(140,320))
        player='X' if this==b'\x10' else 'O'
        opponent='X' if player=='O' else 'O'
        scr.blit(pygame.font.Font(None, 23).render(opponent, True, (50,200,50)),[120,304])
        scr.blit(pygame.font.Font(None, 23).render(player, True, (250,150,0)),[120,324])
        flip()
    if StartTurn=='c':
            lastsent_xox=read_xox()
            turn_mark(1)
            while not update_xox():
                pass
            i=ord(update_xox())
            if this==b'\x10':
                scr.blit(opng,PDICT[i])
                flip()
                table[DICT[i][0]][DICT[i][1]]=2
            if this==b'\x11':
                scr.blit(xpng,PDICT[i])
                flip()
                table[DICT[i][0]][DICT[i][1]]=1
    engn()
    pygame.quit()
    XOX(condition=1)
def quit_msg():
    button(150,150,30,(100,100,200),170,'',0)
    scr.blit(pygame.font.Font(None, 40).render('QUITTING...', True, (250,150,0)),[70,137])
    flip()
def qt():
    try:f.quit()
    except:pass
    if os.path.isfile('xox_server_main'):os.remove('xox_server_main')
    os._exit(1)
def dw():
    if not CheckConnection():
        with open('xox_server_main', 'wb') as fp:
            f.retrbinary('RETR mistik-MANAGER', fp.write)
def up():
    CheckConnection()
    f.storbinary('STOR mistik-MANAGER',open('xox_server_main', 'rb'))
def read():
    with open('xox_server_main', 'rb') as fp:
        return (fp.read())
def write(a):
    with open('xox_server_main','w+b') as fp:
        fp.write(a)
def in_rect(x,y,x_off,y_off,inp_pos):
    if inp_pos[0]>x and inp_pos[0]<=(x+x_off) and inp_pos[1]>y and inp_pos[1]<=(y+y_off): return True
    else: return False
def flip():pygame.display.update()
def scres():
    scr.fill((0,34,64))
    flip()
def button(x,y,rad,color,width,text,font,xoff=0,yoff=0):
    pygame.draw.circle(scr,color,(x-int(width/2),y),rad)
    pygame.draw.circle(scr,color,(x+int(width/2),y),rad)
    pygame.draw.rect(scr,color,(x-int(width/2),y-rad,width,rad*2))
    scr.blit(pygame.font.Font(None, font).render(text, True, TextColor),[x-xoff,y-yoff])
    flip()
def getftppass():
    r=requests.get("https://dlptest.com/ftp-test/").content.decode()
    return(r[r.index('Password:')+10:].split('<')[0])
def CheckConnection():
    global f, ftppass
    try:
        try:
            f.voidcmd('NOOP')
        except:
            try:
                if not ftppass:ftppass=getftppass()
                f=FTP('ftp.dlptest.com')
                f.login(user='dlpuser@dlptest.com',passwd=ftppass)
                f.voidcmd('NOOP')
            except:no_connection_page()
            try:
                with open('xox_server_main', 'wb') as fp:
                    f.retrbinary('RETR mistik-MANAGER', fp.write)
                return True
            except:
                write(b'')
                up()
                return False
    except: os._exit(6)
def no_connection_page(lby=None):
    scr.fill((225,50,50))
    scr.blit(pygame.font.Font(None, 40).render('Could not connect', True, (255,255,10)),[25,40])
    scr.blit(pygame.font.Font(None, 40).render('to the server!', True, (255,255,10)),[60,80])
    scr.blit(pygame.font.Font(None, 25).render('Please check your', True, (50,50,200)),[75,180])
    scr.blit(pygame.font.Font(None, 25).render('internet connection.', True, (50,50,200)),[70,210])
    flip()
    for count in range(5):
        pygame.event.pump()
        pygame.draw.circle(scr,(225,50,50),(150,270),25)
        scr.blit(pygame.font.Font(None, 50).render(str(5-count), True, (50,50,200)),[140,245])
        flip()
        sleep(1)
    if lby:lobby()
    else:os._exit(1)
def lobby():
    global current_page
    current_page='LB'
    scres()
    scr.blit(pygame.font.Font(None, 70).render('X O X', True, (255,255,100)),[90,40])
    scr.blit(pygame.font.Font(None, 17).render('github.com/mistik6821', True, (100,255,100)),[178,327])
    button(150,120,20,ButtonColor,170,'Create a Room',30,xoff=65,yoff=8)
    button(150,180,20,ButtonColor,170,'Join a Room',30,xoff=60,yoff=8)
    button(150,240,20,ButtonColor,170,'Play Offline',30,xoff=57,yoff=8)
    button(150,300,20,(255,100,100),60,'Exit',30,xoff=18,yoff=8)
def inp():
    clck=time()
    refresh=False
    while True:
        if int(clck-time())%5==0 and not refresh:refresh=True
        if refresh and int(clck-time())%5!=0:
            refresh=False
            try:f.voidcmd('NOOP')
            except:pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                qt()
            if current_page=='LB':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if in_rect(50, 100, 200, 40,event.pos):
                        create_room_page()
                    if in_rect(50, 160, 200, 40,event.pos):
                        join_a_room_page()
                    if in_rect(50, 220, 200, 40,event.pos):
                        try:XOX_OFFLINE()
                        except:pass
                        lobby()
                    if in_rect(105, 280, 90, 40,event.pos):
                        qt()
            if current_page=='CR':
                global current_string, inpField, NameFieldReferenceClickCR
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if in_rect(105,90,90,40,event.pos):
                        create_room()
                    if event.type==pygame.MOUSEBUTTONDOWN and inpField.collidepoint(event.pos)or NameFieldReferenceClickCR:
                        NameFieldReferenceClickCR=False
                        pygame.draw.rect(scr,(138,252,246),(150,20,150,20))
                        scr.blit(pygame.font.Font(None, 25).render('George', True, (150,150,150)),[150,22])
                        pygame.draw.line(scr,(0,0,0),(150,37),(300,37),1)
                        if current_string:
                            inpField=pygame.draw.rect(scr,ButtonColor,(150,10,150,40))
                            pygame.draw.rect(scr,(138,252,246),(150,20,150,20))
                            pygame.draw.line(scr,(0,0,0),(150,37),(300,37),1)
                            scr.blit(pygame.font.Font(None, 25).render(current_string, True, (0,0,0)),[150,22])
                        flip()
                        inpActive=True
                        while inpActive:
                            event = pygame.event.poll()
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                qt()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_BACKSPACE:
                                    current_string = current_string[0:-1]
                                elif event.key == pygame.K_RETURN or event.key==271:
                                    inpField=pygame.draw.rect(scr,ButtonColor,(150,10,150,40))
                                    pygame.draw.line(scr,(0,0,0),(150,37),(300,37),1)
                                    scr.blit(pygame.font.Font(None, 25).render(current_string, True, (0,0,0)),[150,22])
                                    if not current_string:scr.blit(pygame.font.Font(None, 25).render('George', True, (150,150,150)),[150,22])
                                    flip()
                                    create_room()
                                    break
                                elif ((chr(event.key) in ACCEPTED_NAME)  or (event.key in NUMPAD))and len(current_string)<9:
                                    if event.key in NUMPAD:current_string+=str(NUMPAD.index(event.key))
                                    else:current_string+=chr(event.key)
                                inpField=pygame.draw.rect(scr,ButtonColor,(150,10,150,40))
                                pygame.draw.rect(scr,(138,252,246),(150,20,150,20))
                                pygame.draw.line(scr,(0,0,0),(150,37),(300,37),1)
                                scr.blit(pygame.font.Font(None, 25).render(current_string, True, (0,0,0)),[150,22])
                                flip()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.type==pygame.MOUSEBUTTONDOWN and not inpField.collidepoint(event.pos):
                                    inpActive=False
                                    inpField=pygame.draw.rect(scr,ButtonColor,(150,10,150,40))
                                    if not current_string:scr.blit(pygame.font.Font(None, 25).render('George', True, (150,150,150)),[150,22])
                                    pygame.draw.line(scr,(0,0,0),(150,37),(300,37),1)
                                    scr.blit(pygame.font.Font(None, 25).render(current_string, True, (0,0,0)),[150,22])
                                    flip()
                                    if in_rect(105,90,90,40,event.pos):
                                        create_room()
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        if back.collidepoint(event.pos):
                            lobby()
            if current_page=='JR':
                global current_string_JR, keyFieldJR, current_name_JR, nameFieldJR, KeyFieldReferenceClick, NameFieldReferenceClick
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if in_rect(235,300,65,40,event.pos):
                        join_room()
                    if event.type==pygame.MOUSEBUTTONDOWN and nameFieldJR.collidepoint(event.pos) or NameFieldReferenceClick:
                        NameFieldReferenceClick=False
                        pygame.draw.rect(scr,(138,252,246),(165,20,150,17))
                        scr.blit(pygame.font.Font(None, 25).render('Beth', True, (150,150,150)),[167,22])
                        pygame.draw.line(scr,(0,0,0),(165,37),(300,37),1)
                        if current_name_JR:
                            nameFieldJR=pygame.draw.rect(scr,ButtonColor,(165,10,135,40))
                            pygame.draw.rect(scr,(138,252,246),(165,20,150,17))
                            pygame.draw.line(scr,(0,0,0),(165,37),(300,37),1)
                            scr.blit(pygame.font.Font(None, 25).render(current_name_JR, True, (0,0,0)),[167,22])
                        flip()
                        inpActive=True
                        while inpActive:
                            event = pygame.event.poll()
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                qt()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_BACKSPACE:
                                    current_name_JR = current_name_JR[0:-1]
                                elif event.key == pygame.K_RETURN or event.key==271:
                                    nameFieldJR=pygame.draw.rect(scr,ButtonColor,(165,10,135,40))
                                    pygame.draw.line(scr,(0,0,0),(165,37),(300,37),1)
                                    scr.blit(pygame.font.Font(None, 25).render(current_name_JR, True, (0,0,0)),[167,22])
                                    if not current_name_JR:scr.blit(pygame.font.Font(None, 25).render('Beth', True, (150,150,150)),[167,22])
                                    flip()
                                    break
                                elif ((chr(event.key) in ACCEPTED_NAME)or (event.key in NUMPAD))and len(current_name_JR)<9:
                                    if event.key in NUMPAD:current_name_JR+=str(NUMPAD.index(event.key))
                                    else:current_name_JR+=chr(event.key)
                                nameFieldJR=pygame.draw.rect(scr,ButtonColor,(165,10,135,40))
                                pygame.draw.rect(scr,(138,252,246),(165,20,150,17))
                                pygame.draw.line(scr,(0,0,0),(165,37),(300,37),1)
                                scr.blit(pygame.font.Font(None, 25).render(current_name_JR, True, (0,0,0)),[167,22])
                                flip()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if not nameFieldJR.collidepoint(event.pos):
                                    inpActive=False
                                    nameFieldJR=pygame.draw.rect(scr,ButtonColor,(165,10,135,40))
                                    if not current_name_JR:scr.blit(pygame.font.Font(None, 25).render('Beth', True, (150,150,150)),[167,22])
                                    pygame.draw.line(scr,(0,0,0),(165,37),(300,37),1)
                                    scr.blit(pygame.font.Font(None, 25).render(current_name_JR, True, (0,0,0)),[167,22])
                                    flip()
                                    if in_rect(235,300,65,40,event.pos):
                                        join_room()
                                    if keyFieldJR.collidepoint(event.pos):KeyFieldReferenceClick=True
                    if event.type==pygame.MOUSEBUTTONDOWN and keyFieldJR.collidepoint(event.pos) or KeyFieldReferenceClick:
                        KeyFieldReferenceClick=False
                        keyFieldJR=pygame.draw.rect(scr,ButtonColor,(200,70,100,40))
                        pygame.draw.rect(scr,(138,252,246),(215,80,60,17))
                        scr.blit(pygame.font.Font(None, 25).render('00000', True, (150,150,150)),[220,82])
                        pygame.draw.line(scr,(0,0,0),(200,97),(300,97),1)
                        if current_string_JR:
                            keyFieldJR=pygame.draw.rect(scr,ButtonColor,(200,70,100,40))
                            pygame.draw.rect(scr,(138,252,246),(215,80,60,17))
                            scr.blit(pygame.font.Font(None, 25).render(current_string_JR, True, (0,0,0)),[220,82])
                            pygame.draw.line(scr,(0,0,0),(200,97),(300,97),1)
                        flip()
                        inpActiveJR=True
                        while inpActiveJR:
                            event = pygame.event.poll()
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                qt()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_BACKSPACE:
                                    current_string_JR = current_string_JR[0:-1]
                                elif event.key == pygame.K_RETURN or event.key==271:
                                    keyFieldJR=pygame.draw.rect(scr,ButtonColor,(200,70,100,40))
                                    pygame.draw.line(scr,(0,0,0),(200,97),(300,97),1)
                                    scr.blit(pygame.font.Font(None, 25).render(current_string_JR, True, (0,0,0)),[220,82])
                                    if not current_string_JR:scr.blit(pygame.font.Font(None, 25).render('00000', True, (150,150,150)),[220,82])
                                    flip()
                                    join_room()
                                    break
                                elif ((chr(event.key) in ACCEPTED_KEY) or (event.key in NUMPAD)) and len(current_string_JR)<5:
                                    if event.key in NUMPAD:current_string_JR+=str(NUMPAD.index(event.key))
                                    else:current_string_JR+=chr(event.key)
                                keyFieldJR=pygame.draw.rect(scr,ButtonColor,(200,70,100,40))
                                pygame.draw.rect(scr,(138,252,246),(215,80,60,17))
                                pygame.draw.line(scr,(0,0,0),(200,97),(300,97),1)
                                scr.blit(pygame.font.Font(None, 25).render(current_string_JR, True, (0,0,0)),[220,82])
                                flip()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.type==pygame.MOUSEBUTTONDOWN and not keyFieldJR.collidepoint(event.pos):
                                    inpActiveJR=False
                                    keyFieldJR=pygame.draw.rect(scr,ButtonColor,(200,70,100,40))
                                    if not current_string_JR:scr.blit(pygame.font.Font(None, 25).render('00000', True, (150,150,150)),[220,82])
                                    pygame.draw.line(scr,(0,0,0),(200,97),(300,97),1)
                                    scr.blit(pygame.font.Font(None, 25).render(current_string_JR, True, (0,0,0)),[220,82])
                                    flip()
                                    if in_rect(235,300,65,40,event.pos):
                                        join_room()
                                    if nameFieldJR.collidepoint(event.pos):
                                        NameFieldReferenceClick=True
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        if backJR.collidepoint(event.pos):
                            lobby()
                    
def create_room_page():
    global current_page, current_string, inpField, back, NameFieldReferenceClickCR
    NameFieldReferenceClickCR=True
    current_page='CR'
    current_string=''
    scres()
    button(10,30,20,ButtonColor,70,'User:',25,5,9)
    button(300,30,20,ButtonColor,300,'',0,0,0)
    inpField=pygame.draw.rect(scr,ButtonColor,(150,10,150,40))
    scr.blit(pygame.font.Font(None, 25).render('George', True, (150,150,150)),[150,22])
    pygame.draw.line(scr,(0,0,0),(150,37),(300,37),1)
    button(150,110,20,ButtonColor,60,'Create',25,28,9)
    back=pygame.draw.circle(scr,ButtonColor,(2,338),35)
    scr.blit(pygame.font.Font(None, 55).render('<', True, (100,100,100)),[5,306])
    flip()

def join_a_room_page():
    global current_page, current_string_JR, keyFieldJR,current_name_JR, nameFieldJR, backJR, KeyFieldReferenceClick, NameFieldReferenceClick
    KeyFieldReferenceClick=False
    NameFieldReferenceClick=True
    current_page='JR'
    current_string_JR=''
    current_name_JR=''
    scres()
    button(0,30,20,ButtonColor,120,'Name:',25,-10,9)
    button(250,30,20,ButtonColor,170,'',0,0,0)
    nameFieldJR=pygame.draw.rect(scr,ButtonColor,(165,10,135,40))
    scr.blit(pygame.font.Font(None, 25).render('Beth', True, (150,150,150)),[167,22])
    pygame.draw.line(scr,(0,0,0),(165,37),(300,37),1)
    button(0,90,20,ButtonColor,190,'Invite Key:',25,-10,9)
    button(250,90,20,ButtonColor,100,'',0,0,0)
    keyFieldJR=pygame.draw.rect(scr,ButtonColor,(200,70,100,40))
    scr.blit(pygame.font.Font(None, 25).render('00000', True, (150,150,150)),[220,82])
    pygame.draw.line(scr,(0,0,0),(200,97),(300,97),1)
    button(300,320,20,ButtonColor,100,'Join',28,50,9)
    backJR=pygame.draw.circle(scr,ButtonColor,(2,338),35)
    scr.blit(pygame.font.Font(None, 55).render('<', True, (100,100,100)),[5,306])
def create_room():
    pygame.draw.rect(scr,(0,34,64),(69,159,200,20))
    flip()
    if (not current_string): return
    scr.blit(pygame.font.Font(None, 35).render('CONNECTING...', True, (MessageColor)),[60,160])
    flip()
    CheckConnection()
    pygame.draw.rect(scr,(0,34,64),(50,160,200,40))
    flip()
    dw()
    room_list=read().decode().split('+')
    if current_string in room_list:
        scr.blit(pygame.font.Font(None, 25).render('Room already exist.', True, (220,50,50)),[70,160])
        flip()
    else:
        pygame.draw.rect(scr,(0,34,64),(50,160,200,40))
        scr.blit(pygame.font.Font(None, 33).render('CREATING ROOM...', True, (MessageColor)),[47,163])
        flip()
        dw()
        randKey=str(int(random.randint(1000,9999)))
        if read()!=b'':write(read()+b'+'+current_string.encode()+b'+'+randKey.encode()+b'+0')
        else:write(current_string.encode()+b'+'+randKey.encode()+b'+0')
        up()
        try:XOX(current_string,RK=randKey)
        except TimeoutError:
            no_connection_page(1)
        except Exception as result:
            if type(result)==Exception:
                result=int(str(result))
                if result==2:f.delete('mistik_'+current_string)
        try:
            dw()
            room_list=read().decode().split('+')
            del room_list[room_list.index(current_string):room_list.index(current_string)+3]
            writeRaw=''
            for i in room_list:
                if room_list.index(i)==0:
                    writeRaw=i
                    continue
                writeRaw+='+'+i
            write(writeRaw.encode())
            up()
        except:
            try:up()
            except:CheckConnection()
        pygame.event.clear()
        lobby()
def join_room():
    pygame.draw.rect(scr,(0,34,64),(69,159,200,20))
    flip()
    if (not current_string_JR) or (not current_name_JR):return
    scr.blit(pygame.font.Font(None, 35).render('CONNECTING...', True, (MessageColor)),[60,160])
    flip()
    CheckConnection()
    pygame.draw.rect(scr,(0,34,64),(50,160,200,40))
    flip()
    dw()
    room_list=read().decode().split('+')
    if current_string_JR not in room_list:
        scr.blit(pygame.font.Font(None, 25).render('Room doesn\'t exist.', True, (220,50,50)),[70,160])
        flip()
    elif room_list[room_list.index(current_string_JR)+1]!='0':
        scr.blit(pygame.font.Font(None, 25).render('The room is full.', True, (220,50,50)),[80,160])
        flip()
    else:
        room_list[room_list.index(current_string_JR)+1]=1
        write_raw=''
        for i in room_list:
            write_raw+=str(i)+'+'
        write_raw=write_raw[:-1]
        write(bytes(write_raw,encoding='ascii'))
        up()
        room_name=room_list[room_list.index(current_string_JR)-1]
        try:XOX(room_name,join_name=current_name_JR)
        except TimeoutError:
            no_connection_page(1)
        except Exception as result:
            if type(result)==Exception:
                result=int(str(result))
                if result==2:f.delete('mistik_'+room_name)
        pygame.event.clear()
        lobby()
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.display.set_caption(u'XOX')
scr=pygame.display.set_mode((300, 340))
open('xox_ico.png','wb').write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 \x00\x00\x00 \x08\x06\x00\x00\x00szz\xf4\x00\x00\x03OIDATXG\xb5WMO\x13Q\x14=w0&PA`\xe5\xc6\x18\xdc\xba(l04lX\xbb\x96JBJ\x94\x05\x86?`ta\xfc\x88\t\xbf@tA\xc4\xea\xa6\xac\xdd\xb31\x10\xd9`\xff\x81\xfa\x03\xa4\xb6\xa9l\xe8\\s\xdf\xcc\x9b\xbe\xf7\xe6\xcdL+\xd0]\xdb\x979\xe7\x9d{\xee\xb9w\x08\x17\xfc\xa9r\xe5\x0f\x80\t\xe3\xb1\xed\x06\x1d\\7a\xaa\\\xf9\r`R~\xa3\x0b\xc6\xc72WB2\x9e\xcb\x00\xef\xd1A\xa0q\xaa\xbcXf\x84\xc7\xfa\xcc\x85\x13p\x15\x10\x02\x84`."\x10\xee30i\x12\xbc\x0c\x02"\xef\x94\xa3\xecI\xfc]d\xb70/\x81\x80-\xb1\x00\x8b\nq\xbd]<\x1e\x8a\x00\xaf\xa2\x8c\x00\xfb\x00F\x00\x8c\x03\xe8\x00\xe8!\xc4\x12}F\xb3_ge\xb2D\x05AO!\xab\xd2\xa05\x1c\x81\x1a\\\x87kL\xc1hi"\xae\xd1\\\xa3k_4\xe8ksX\x02aN\xe7(\x12T\xc7\xb4\x00\x8a\x19\x19\x98\xf0\x03p\xbbA\x87\xaa5\x07"`H\xef\x9a\xcbs9\xb4>-\xcfl|\xb9w\xa3A \xeb\xf9F)\x92l\x18\x8c@\r:8\x069\xcf\xeb\xdb\xf3\xd4\x1d\xbbb\x913}0t\t8]\xfb\xa8\xe6\x8c\r\x10\xde\xc7\xa9\xa6\xc8\xfd\xbcY\xc2\x93\xd7\xe5Bm#\x12\x03\x9a\x90kpk\xcfTG\x92n\x1c)\xa4\xca\xb3\xfev\x1e\xdd\x92{{fad\x06\x90\x96\xa7P\xd2\xb8\xfe\xc7\x8e_\xdaTG\x92\xef\xe6\x99\x87\xef\xee\xe2tT\xba4\xfaD\xd2\x07\xb3\x92\x82\xa6R\x83\x130ng\x14\xf5D\xbb=\x01\x8a\xcf=\xd8\xadX\xf2\xebY \xad\xe9\x8d\xe2h2\x05K\xd2\x93\xbe\xc1\xd4[C\'`\\3\xfec\x84\x983\x83G\xddt\x15e\x1e\xc1\xf7\x95\xdd\x05K,\x06\xf3\x1e\x1dZ\xc3\xc8$BU\xaeH\x81\xd4\xc0\xf0\x91\x08\xd7\xc0\xa4\x824\x96\x94\x80\xe0\xa3\xbf}\xe5l\x11\x81~ZF\x8a(\x02:\xaf\xc5\x95Z\r-\xd9\x87\xc7\xdf\xa6FO{\x16\x01\xeaa6K\x81G\xdb\xf38\x1d5M\xd8\x0f\x1d\x9f\xc2\t\x01\xc33\xad\x06\x1dL\xeb\xa5ag\xf3\x88J\xdd3o\xe0\x983@w\x82\xb4\xe1\xab\xa7w\xa2\xf3\x04t\xc7\xae\xcef\x95W\x1d\xd1\n\x18\xaee\x02w\x184.ms\xebW\x17[\xcf\x9b0\xcb`\x92\xd5ft\xb3B\x9a\xfc\xd9\x8br{k\xa6imC\xeeMR\x04|2\xedl\x1ea\xec\xef\x99\x8f\x84\x1co\xab\x89\x18\xadXI[\x0b\x81\x95\xdd\xc5\xdc\xdb\xc7\n\xd8\xf3\xdb\x1d\x9db\xd0\xdb?\xba\x9d7/\x9b\x08B5\x82\x0b\xb3#\xbe\x84\x95\x15\xbe\x8b\xc5UR\x93+\'\xeb\xfb&\xca\x08%\xdf\xb3\xad\xc9\x98\x05n\x10X\xb8\xcf@\x03 k|\xc5jX[ml\xb6\xd4je\xe5\x84\xb1\x1b\xe4\x81\x0f\xa4\x80\x1e\x1a\xba==[\x91~\x8eN\x8bd\'(\x02\xf7z \xce\x04\xb7\xd0JRi\xcfT?\xf6\xd7\xb4\xe8/g=+"!]\x90\xdab%>\xdd\xe9\x95\x97\x96E \xb9\x1e\xf0\xbdHD{\xbc\x9a^\xa9\xf5\xda\xa7\xc2\xb9\x08\xb8A\x04\xe0$J\xc2\xf4z-=\xef\xbef\x9d\x07<\x95\x84\xae\xccE\xafY\xe7\x05\xf7E\xb1\xba\xbd~p\xd6kV^\xb6\x0fK\xca\x99\x86\xf6H\xf6\x19T\x97hX\xa0\xcc$\x8c=\xe0m3\x8f\x0f2\xdb\xf1\x7f\t\xfd\x03\xe0+\xb5\xaf\xe9\xfe\xe6\x85\x00\x00\x00\x00IEND\xaeB`\x82')
pygame.display.set_icon(pygame.image.load('xox_ico.png'))
os.remove('xox_ico.png')
pygame.event.pump()
try:ftppass=getftppass()
except:ftppass=None
scres()
lobby()
inp()
