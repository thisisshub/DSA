#/bin/bash

for i in $(find . -name '*.py'); do
{   
    echo "=======";
    echo $i;
    python3 $i;
} done