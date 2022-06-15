#!/usr/bin/bash

# Selecciona les columnes de nom i frase
sudo cat validated.tsv | tail -n +2 | tr "\t" "~" | cut -d"~" -f 2,3 > validated.data

# Adapta el format del contingut
sudo sed 's/^/(/' validated.data > validated2.data
rm -f validated.data
sed 's/$/)/' validated2.data > validated3.data
rm -f validated2.data
sed 's/~/ "/' validated3.data > validated4.data
rm -f validated3.data
sed 's/""/"/' validated4.data > validated5.data
rm -f validated4.data
sed 's/\.)/\.")/' validated5.data > validated6.data
rm -f validated5.data
sed 's/?)/?")/' validated6.data > validated7.data
rm -f validated6.data
sed 's/!)/!")/' validated7.data > validated8.data
rm -f validated7.data
sed 's/:)/:")/' validated8.data > validated9.data
rm -f validated8.data
sed 's/à)/à")/' validated9.data > validated10.data
rm -f validated9.data
sed 's/c)/c")/' validated10.data > validated11.data
rm -f validated10.data
sed 's/d)/d")/' validated11.data > validated12.data
rm -f validated11.data
sed 's/e)/e")/' validated12.data > validated13.data
rm -f validated12.data
sed 's/i)/i")/' validated13.data > validated14.data
rm -f validated13.data
sed 's/í)/í")/' validated14.data > validated15.data
rm -f validated14.data
sed 's/l)/l")/' validated15.data > validated16.data
rm -f validated15.data
sed 's/o)/o")/' validated16.data > validated17.data
rm -f validated16.data
sed 's/r)/r")/' validated17.data > validated18.data
rm -f validated17.data
sed 's/s)/s")/' validated18.data > validated19.data
rm -f validated18.data
sed 's/t)/t")/' validated19.data > validated20.data
rm -f validated19.data
sed 's/u)/u")/' validated20.data > validated21.data
rm -f validated20.data

# Ordena les frases
sort validated21.data > validated.data
rm -f validated21.data

# Selecciona els àudios que acaben en 00 i els guarda a "com.data"
cd clips00
while read line ; do ( 	
	nom=${line:1:28} ;
	echo "$nom" ;
	if [[ "$nom" == *"00.mp3" ]] ; then
		for i in * ; do ( 	
			if [ "$i" == "$nom" ] ; then
				echo "$line" >> "../com_utf8.data"
			fi
		) 
		done 
	fi 
) ; 
done < "../validated.data"

# Converteix "com.data" a ISO Latin1 per poder ser llegit correctament
iconv -f utf8 -t ISO-8859-1 com_utf8.data > com.data
rm -f com_utf8.data
cd ..
