# Python Studies

My solutions to all 115 challenges of the Python course by [Curso em Vídeo](https://www.cursoemvideo.com/), taught by Gustavo Guanabara, plus the small tests I wrote while following the classes. The course is split into three modules ("Mundos"), and so is this repository.

The code, comments and program output are in Brazilian Portuguese, like the course.

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)

## Contents

| Folder | Challenges | Topics |
|---|---|---|
| [`PythonExercicios-Mundo1`](PythonExercicios-Mundo1) | 001 to 035 | input and output, operators, strings, the `math` and `random` modules, conditionals |
| [`PythonExercicios-Mundo2`](PythonExercicios-Mundo2) | 036 to 071 | nested conditionals, `for` and `while` loops, stopping loops with `break` |
| [`PythonExercicios-Mundo3`](PythonExercicios-Mundo3) | 072 to 115 | tuples, lists, dictionaries, functions, modules and packages, error handling, reading and writing files |
| [`Testes`](Testes) | | short experiments from the classes |

`exNNN.py` is challenge NNN. Files ending in `Part2` or `part2` (and sometimes `part3`) are second versions of the same challenge. Challenges 107 to 112 and 115 are folders instead of single files, because they are about splitting code into modules and packages.

## Highlights

Some challenges that show how the course builds up:

| Challenge | What it does | File |
|---|---|---|
| 028 | Guessing game: the computer picks a number from 0 to 5 and you try to guess it | [`ex028.py`](PythonExercicios-Mundo1/ex028.py) |
| 029 | Speed camera: charges R$ 7 for each km/h above 80 | [`ex029.py`](PythonExercicios-Mundo1/ex029.py) |
| 068 | Even or odd against the computer, counting your winning streak until you lose | [`ex068part2.py`](PythonExercicios-Mundo2/ex068part2.py) |
| 071 | ATM: the smallest number of R$ 50, 20, 10 and 1 notes for a withdrawal | [`ex071part2.py`](PythonExercicios-Mundo2/ex071part2.py) |
| 095 | Football stats: goals per match for several players, with a summary table and per-player details | [`ex095.py`](PythonExercicios-Mundo3/ex095.py) |
| 100 | Two functions: draw five random numbers, then add up the even ones | [`ex100.py`](PythonExercicios-Mundo3/ex100.py) |
| 112 | Package with currency helpers (`moeda`) and validated money input (`dado`) | [`ex112/`](PythonExercicios-Mundo3/ex112) |
| 114 | Checks whether a website is online with `urllib` | [`ex114part2.py`](PythonExercicios-Mundo3/ex114part2.py) |
| 115 | Final project: a menu-driven people registry saved to a text file | [`ex115part3/`](PythonExercicios-Mundo3/ex115part3) |

## Running

Requires Python 3. Most challenges are single files:

```bash
python3 PythonExercicios-Mundo1/ex028.py
```

Most folder challenges import their modules from the `PythonExercicios-Mundo3` folder, so run them from there as modules (the entry file is `main.py`, `teste.py` or `sistema.py`):

```bash
cd PythonExercicios-Mundo3
python3 -m ex115part3.sistema
python3 -m ex112.main
```

The first versions of 107 and 108 import their modules directly, so they run from their own folder: `cd PythonExercicios-Mundo3/ex107 && python3 main.py`.

Challenge 021 plays an MP3 with `pygame` (`pip install pygame`). The audio file is not in the repository: put any MP3 named `Audiomp3.mp3` in `PythonExercicios-Mundo1` before running it.

The output uses ANSI color codes, which show as colors in most terminals.

## License

My code is released under the [MIT License](LICENSE). The challenge statements belong to Curso em Vídeo.

## Author

Pedro Ross. [GitHub](https://github.com/PedroRossZny) | [LinkedIn](https://www.linkedin.com/in/pedro-ross)
