# ConsoleAPP #
```sh
python3 verify.py -h
usage: verify.py [-h] [--step] [--depth] [--test id [id ...]] [--data]

verify election

positional arguments:
                      Unique election event identifier

optional arguments:
  -h, --help          show this help message and exit
  --step              define in which distance the progress will printed,
                      default every 20%
  --depth             set the depth of tree, which will printed, default=5
  --test id [id ...]  use this for runing only a certain tests ,Format: [1-9](\.[1-9]){0,2}
  --data              append the test_data
```