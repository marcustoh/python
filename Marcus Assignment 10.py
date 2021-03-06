Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> rows="""name,genus,vore,order,conservation,sleep_total,sleep_rem,sleep_cycle,awake,brainwt,bodywt
Cheetah,Acinonyx,carni,Carnivora,lc,12.1,NA,NA,11.9,NA,50
Owl monkey,Aotus,omni,Primates,NA,17,1.8,NA,7,0.0155,0.48
Mountain beaver,Aplodontia,herbi,Rodentia,nt,14.4,2.4,NA,9.6,NA,1.35
Greater short-tailed shrew,Blarina,omni,Soricomorpha,lc,14.9,2.3,0.133333333,9.1,0.00029,0.019
Cow,Bos,herbi,Artiodactyla,domesticated,4,0.7,0.666666667,20,0.423,600
Three-toed sloth,Bradypus,herbi,Pilosa,NA,14.4,2.2,0.766666667,9.6,NA,3.85
Northern fur seal,Callorhinus,carni,Carnivora,vu,8.7,1.4,0.383333333,15.3,NA,20.49
Vesper mouse,Calomys,NA,Rodentia,NA,7,NA,NA,17,NA,0.045
Dog,Canis,carni,Carnivora,domesticated,10.1,2.9,0.333333333,13.9,0.07,14
Roe deer,Capreolus,herbi,Artiodactyla,lc,3,NA,NA,21,0.0982,14.8
Goat,Capri,herbi,Artiodactyla,lc,5.3,0.6,NA,18.7,0.115,33.5
Guinea pig,Cavis,herbi,Rodentia,domesticated,9.4,0.8,0.216666667,14.6,0.0055,0.728
Grivet,Cercopithecus,omni,Primates,lc,10,0.7,NA,14,NA,4.75
Chinchilla,Chinchilla,herbi,Rodentia,domesticated,12.5,1.5,0.116666667,11.5,0.0064,0.42
Star-nosed mole,Condylura,omni,Soricomorpha,lc,10.3,2.2,NA,13.7,0.001,0.06
African giant pouched rat,Cricetomys,omni,Rodentia,NA,8.3,2,NA,15.7,0.0066,1
Lesser short-tailed shrew,Cryptotis,omni,Soricomorpha,lc,9.1,1.4,0.15,14.9,0.00014,0.005
Long-nosed armadillo,Dasypus,carni,Cingulata,lc,17.4,3.1,0.383333333,6.6,0.0108,3.5
Tree hyrax,Dendrohyrax,herbi,Hyracoidea,lc,5.3,0.5,NA,18.7,0.0123,2.95
North American Opossum,Didelphis,omni,Didelphimorphia,lc,18,4.9,0.333333333,6,0.0063,1.7
Asian elephant,Elephas,herbi,Proboscidea,en,3.9,NA,NA,20.1,4.603,2547
Big brown bat,Eptesicus,insecti,Chiroptera,lc,19.7,3.9,0.116666667,4.3,3e-04,0.023
Horse,Equus,herbi,Perissodactyla,domesticated,2.9,0.6,1,21.1,0.655,521
Donkey,Equus,herbi,Perissodactyla,domesticated,3.1,0.4,NA,20.9,0.419,187
European hedgehog,Erinaceus,omni,Erinaceomorpha,lc,10.1,3.5,0.283333333,13.9,0.0035,0.77
Patas monkey,Erythrocebus,omni,Primates,lc,10.9,1.1,NA,13.1,0.115,10
Western american chipmunk,Eutamias,herbi,Rodentia,NA,14.9,NA,NA,9.1,NA,0.071
Domestic cat,Felis,carni,Carnivora,domesticated,12.5,3.2,0.416666667,11.5,0.0256,3.3
Galago,Galago,omni,Primates,NA,9.8,1.1,0.55,14.2,0.005,0.2
Giraffe,Giraffa,herbi,Artiodactyla,cd,1.9,0.4,NA,22.1,NA,899.995
Pilot whale,Globicephalus,carni,Cetacea,cd,2.7,0.1,NA,21.35,NA,800
Gray seal,Haliochoerus,carni,Carnivora,lc,6.2,1.5,NA,17.8,0.325,85
Gray hyrax,Heterohyrax,herbi,Hyracoidea,lc,6.3,0.6,NA,17.7,0.01227,2.625
Human,Homo,omni,Primates,NA,8,1.9,1.5,16,1.32,62
Mongoose lemur,Lemur,herbi,Primates,vu,9.5,0.9,NA,14.5,NA,1.67
African elephant,Loxodonta,herbi,Proboscidea,vu,3.3,NA,NA,20.7,5.712,6654
Thick-tailed opposum,Lutreolina,carni,Didelphimorphia,lc,19.4,6.6,NA,4.6,NA,0.37
Macaque,Macaca,omni,Primates,NA,10.1,1.2,0.75,13.9,0.179,6.8
Mongolian gerbil,Meriones,herbi,Rodentia,lc,14.2,1.9,NA,9.8,NA,0.053
Golden hamster,Mesocricetus,herbi,Rodentia,en,14.3,3.1,0.2,9.7,0.001,0.12
Vole ,Microtus,herbi,Rodentia,NA,12.8,NA,NA,11.2,NA,0.035
House mouse,Mus,herbi,Rodentia,nt,12.5,1.4,0.183333333,11.5,4e-04,0.022
Little brown bat,Myotis,insecti,Chiroptera,NA,19.9,2,0.2,4.1,0.00025,0.01
Round-tailed muskrat,Neofiber,herbi,Rodentia,nt,14.6,NA,NA,9.4,NA,0.266
Slow loris,Nyctibeus,carni,Primates,NA,11,NA,NA,13,0.0125,1.4
Degu,Octodon,herbi,Rodentia,lc,7.7,0.9,NA,16.3,NA,0.21
Northern grasshopper mouse,Onychomys,carni,Rodentia,lc,14.5,NA,NA,9.5,NA,0.028
Rabbit,Oryctolagus,herbi,Lagomorpha,domesticated,8.4,0.9,0.416666667,15.6,0.0121,2.5
Sheep,Ovis,herbi,Artiodactyla,domesticated,3.8,0.6,NA,20.2,0.175,55.5
Chimpanzee,Pan,omni,Primates,NA,9.7,1.4,1.416666667,14.3,0.44,52.2
Tiger,Panthera,carni,Carnivora,en,15.8,NA,NA,8.2,NA,162.564
Jaguar,Panthera,carni,Carnivora,nt,10.4,NA,NA,13.6,0.157,100
Lion,Panthera,carni,Carnivora,vu,13.5,NA,NA,10.5,NA,161.499
Baboon,Papio,omni,Primates,NA,9.4,1,0.666666667,14.6,0.18,25.235
Desert hedgehog,Paraechinus,NA,Erinaceomorpha,lc,10.3,2.7,NA,13.7,0.0024,0.55
Potto,Perodicticus,omni,Primates,lc,11,NA,NA,13,NA,1.1
Deer mouse,Peromyscus,NA,Rodentia,NA,11.5,NA,NA,12.5,NA,0.021
Phalanger,Phalanger,NA,Diprotodontia,NA,13.7,1.8,NA,10.3,0.0114,1.62
Caspian seal,Phoca,carni,Carnivora,vu,3.5,0.4,NA,20.5,NA,86
Common porpoise,Phocoena,carni,Cetacea,vu,5.6,NA,NA,18.45,NA,53.18
Potoroo,Potorous,herbi,Diprotodontia,NA,11.1,1.5,NA,12.9,NA,1.1
Giant armadillo,Priodontes,insecti,Cingulata,en,18.1,6.1,NA,5.9,0.081,60
Rock hyrax,Procavia,NA,Hyracoidea,lc,5.4,0.5,NA,18.6,0.021,3.6
Laboratory rat,Rattus,herbi,Rodentia,lc,13,2.4,0.183333333,11,0.0019,0.32
African striped mouse,Rhabdomys,omni,Rodentia,NA,8.7,NA,NA,15.3,NA,0.044
Squirrel monkey,Saimiri,omni,Primates,NA,9.6,1.4,NA,14.4,0.02,0.743
Eastern american mole,Scalopus,insecti,Soricomorpha,lc,8.4,2.1,0.166666667,15.6,0.0012,0.075
Cotton rat,Sigmodon,herbi,Rodentia,NA,11.3,1.1,0.15,12.7,0.00118,0.148
Mole rat,Spalax,NA,Rodentia,NA,10.6,2.4,NA,13.4,0.003,0.122
Arctic ground squirrel,Spermophilus,herbi,Rodentia,lc,16.6,NA,NA,7.4,0.0057,0.92
Thirteen-lined ground squirrel,Spermophilus,herbi,Rodentia,lc,13.8,3.4,0.216666667,10.2,0.004,0.101
Golden-mantled ground squirrel,Spermophilus,herbi,Rodentia,lc,15.9,3,NA,8.1,NA,0.205
Musk shrew,Suncus,NA,Soricomorpha,NA,12.8,2,0.183333333,11.2,0.00033,0.048
Pig,Sus,omni,Artiodactyla,domesticated,9.1,2.4,0.5,14.9,0.18,86.25
Short-nosed echidna,Tachyglossus,insecti,Monotremata,NA,8.6,NA,NA,15.4,0.025,4.5
Eastern american chipmunk,Tamias,herbi,Rodentia,NA,15.8,NA,NA,8.2,NA,0.112
Brazilian tapir,Tapirus,herbi,Perissodactyla,vu,4.4,1,0.9,19.6,0.169,207.501
Tenrec,Tenrec,omni,Afrosoricida,NA,15.6,2.3,NA,8.4,0.0026,0.9
Tree shrew,Tupaia,omni,Scandentia,NA,8.9,2.6,0.233333333,15.1,0.0025,0.104
Bottle-nosed dolphin,Tursiops,carni,Cetacea,NA,5.2,NA,NA,18.8,NA,173.33
Genet,Genetta,carni,Carnivora,NA,6.3,1.3,NA,17.7,0.0175,2
Arctic fox,Vulpes,carni,Carnivora,NA,12.5,NA,NA,11.5,0.0445,3.38
Red fox,Vulpes,carni,Carnivora,NA,9.8,2.4,0.35,14.2,0.0504,4.23"""
>>> loop=0
>>> for row in rows.split('\n'):
	print("""
%s \t %s"""%(rows.split('\n')[loop].split(',')[0],rows.split('\n')[loop].split(',')[5]))
	loop=loop+1

	

name 	 sleep_total

Cheetah 	 12.1

Owl monkey 	 17

Mountain beaver 	 14.4

Greater short-tailed shrew 	 14.9

Cow 	 4

Three-toed sloth 	 14.4

Northern fur seal 	 8.7

Vesper mouse 	 7

Dog 	 10.1

Roe deer 	 3

Goat 	 5.3

Guinea pig 	 9.4

Grivet 	 10

Chinchilla 	 12.5

Star-nosed mole 	 10.3

African giant pouched rat 	 8.3

Lesser short-tailed shrew 	 9.1

Long-nosed armadillo 	 17.4

Tree hyrax 	 5.3

North American Opossum 	 18

Asian elephant 	 3.9

Big brown bat 	 19.7

Horse 	 2.9

Donkey 	 3.1

European hedgehog 	 10.1

Patas monkey 	 10.9

Western american chipmunk 	 14.9

Domestic cat 	 12.5

Galago 	 9.8

Giraffe 	 1.9

Pilot whale 	 2.7

Gray seal 	 6.2

Gray hyrax 	 6.3

Human 	 8

Mongoose lemur 	 9.5

African elephant 	 3.3

Thick-tailed opposum 	 19.4

Macaque 	 10.1

Mongolian gerbil 	 14.2

Golden hamster 	 14.3

Vole  	 12.8

House mouse 	 12.5

Little brown bat 	 19.9

Round-tailed muskrat 	 14.6

Slow loris 	 11

Degu 	 7.7

Northern grasshopper mouse 	 14.5

Rabbit 	 8.4

Sheep 	 3.8

Chimpanzee 	 9.7

Tiger 	 15.8

Jaguar 	 10.4

Lion 	 13.5

Baboon 	 9.4

Desert hedgehog 	 10.3

Potto 	 11

Deer mouse 	 11.5

Phalanger 	 13.7

Caspian seal 	 3.5

Common porpoise 	 5.6

Potoroo 	 11.1

Giant armadillo 	 18.1

Rock hyrax 	 5.4

Laboratory rat 	 13

African striped mouse 	 8.7

Squirrel monkey 	 9.6

Eastern american mole 	 8.4

Cotton rat 	 11.3

Mole rat 	 10.6

Arctic ground squirrel 	 16.6

Thirteen-lined ground squirrel 	 13.8

Golden-mantled ground squirrel 	 15.9

Musk shrew 	 12.8

Pig 	 9.1

Short-nosed echidna 	 8.6

Eastern american chipmunk 	 15.8

Brazilian tapir 	 4.4

Tenrec 	 15.6

Tree shrew 	 8.9

Bottle-nosed dolphin 	 5.2

Genet 	 6.3

Arctic fox 	 12.5

Red fox 	 9.8
>>> 