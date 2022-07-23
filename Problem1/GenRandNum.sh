
for n in `seq "0" "$1"`
    do  
        randomNumber=$(shuf -i 1-100 -n1)
        echo $n, $randomNumber
        echo $n, $randomNumber > inputFile
    done