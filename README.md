![Build Status](https://github.com/ricardobranco777/plotit/actions/workflows/ci.yml/badge.svg)

# PlotIt

Cool plotting tool that generates a PNG graph for each CSV file (with space as delimiter).

## Format of each line

`PLOT_NAME SECONDS_SINCE_EPOCH FLOAT_VALUE`

## Usage

```
plotit [-s|--separator FIELD_SEPARATOR] [-k|--kind line|bar|area]
       [-o|--output OUTPUT] [-d|--dir DIRECTORY]
       [-t|--type png|svg|pdf] FILES...
```

Notes:
- The default delimiter is a single ASCII space.  Separators longer than 1 character and different from '\s+' will be interpreted as regular expressions as noted [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
- The type of graph may be specified with the `-k` (`--kind`) option.  The default is `line`.
- The `-o` or (`--output`) option specifies the path of the image file to be saved. It does only work with one input file.
- The `-d` or (`--dir`) option specifies the output directory. In this case the name of the files is automatically defined from the input names and cannot be specified with the `-o` (`output`) option.
- The `-t` or (`--type`) option specifies the output file type.

## Example

`plotit example/*`

## Dependencies

- Tested on Python 3.9+
- The `python3-pandas` package will install these on Debian/Ubuntu & openSUSE: Matplotlib & Pandas
