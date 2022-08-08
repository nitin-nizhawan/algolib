#!/usr/bin/env bash

cd clrs/cpp
echo "Running csharp test"
./test
cd ../../
cd clrs/csharp
echo "Running csharp tests"
dotnet test
echo "Going back to root dir"
cd ../../
cd clrs/py
echo "Running py tests"
. ./test

