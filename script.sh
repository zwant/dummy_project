#!/bin/bash

for i in `seq 1 10`;
do
    echo "Hello this is test no ${i}" > testArtifact${i}.txt
done

mkdir -p test/dir/one
mkdir -p test/dir/two

for i in `seq 1 10`;
do
    echo "Hello this is test no ${i}" > test/dir/one/testArtifact${i}.txt
    echo "Hello this is test no ${i}" > test/dir/two/testArtifact${i}.txt
    echo "Hello this is test no ${i}" > test/dir/testArtifact${i}.txt
    echo "Hello this is test no ${i}" > test/testArtifact${i}.txt
done

sleep 1

BUILD_NUMBER=1 nosetests --quiet --with-xunit --xunit-file=fake.xml
BUILD_NUMBER=2 nosetests --quiet --with-xunit --xunit-file=fake2.xml
