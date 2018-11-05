#!/bin/bash

for SIZE in 500 1000 2000 ;do
    echo "======================";

    echo "matrix size=" $SIZE;
    python3 gen-mat.py $SIZE

    echo "------";
    echo "Sparse CA"
    /usr/bin/time -f "%M KB %E s" python3 casparse.py 

    echo "------";
    echo "existing method(Orange lib)"
    /usr/bin/time -f "%M KB %E s" python3 ca-orage.py
done
