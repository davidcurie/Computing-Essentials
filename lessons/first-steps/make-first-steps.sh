#! /bin/bash

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

create_directory () {
    dirname=$(basename $PWD)
    if [ "$dirname" = "Computing-Essentials" ]
    then
        mkdir -p $lesson_directory
    else
        echo "Error: Run this from a directory named Computing-Essentials"
        exit 1
    fi
}

populate_directory () {
    curl https://raw.githubusercontent.com/davidcurie/Computing-Essentials/main/lessons/${lesson_directory}/filenames.txt > ${lesson_directory}/filenames.txt
    filenames=$(cat ${lesson_directory}/filenames.txt)
    for filename in ${filenames}
    do
        touch ${lesson_directory}/${filename}
    done
    rm ${lesson_directory}/filenames.txt
}

populate_spectrum_for_file () {
    touch ${lesson_directory}/dummy.tmp
    for wavelength in {530..700}
    do
        echo -e "${wavelength}\t$((256 + RANDOM % 100))" >> ${lesson_directory}/dummy.tmp
    done
    cat ${lesson_directory}/dummy.tmp > $1
    rm ${lesson_directory}/dummy.tmp
}

simulate_noise_for_file () {
    touch ${lesson_directory}/modified.txt
    sed -E 's/^600\t.{3}/600\t382/' $1 > ${lesson_directory}/modified.txt
    mv ${lesson_directory}/modified.txt $1
}

create_directory
populate_directory

for file in $lesson_directory/*.txt
do
    populate_spectrum_for_file $file
done

simulate_noise_for_file $lesson_directory/122521_results.txt
