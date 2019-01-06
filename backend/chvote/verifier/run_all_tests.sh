#!/bin/bash

for py_file in $(find -name \*.py)
do
  case "$py_file" in
    *__*)
    continue
      ;;
  esac
  echo 'Test' $py_file
  python $py_file
done
echo 'All test are done'
read
