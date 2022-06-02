#!usr/env/bin bash

# Author: David Curie
# A simple script to be run by the end-user of this lesson series to populate
# their lesson directory with necessary files without having to use git clone.
#
# Assumptions: Run this script from inside Computing-Essentials directory
#
# Results:
# - Create first-steps directory and populate it with dummy files
# - Write dummy data to some of the dummy files

lesson_directory=first-steps

function create_directory {
    dirname=$(basename $PWD)
    if [[ $dirname == "Computing-Essentials" ]]
    then
        mkdir -p $lesson_directory
    else
        echo "Error: Run this from a directory named Computing-Essentials"
        exit 1
    fi
}

function populate_directory {
    touch $lesson_directory/{0{8..9},{10..12}}{0{1..9},{10..30}}21_results.txt
    touch $lesson_directory/0{1..4}{0{1..9},{10..29}}22_results.txt
    touch $lesson_directory/{0{8..9},{10..12}}{11,22}21_high-temp_results.txt
    touch $lesson_directory/summary.csv
}

function populate_spectrum () {
    touch dummy.tmp
    for wavelength in {530..700}
    do
        echo "$wavelength\t$(($RANDOM % 100 + 256))" >> dummy.tmp
    done
    cat dummy.tmp > $1
    rm dummy.tmp
}

function simulate_noise () {
    sed -E -i '' 's/^600\t.{3}/600\t382/' $1
}

create_directory
populate_directory

for file in $lesson_directory/*.txt
do
    populate_spectrum $file
done

simulate_noise $lesson_directory/122521_results.txt
