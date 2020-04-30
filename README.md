# PlotIt

Cool plotting tool that generates a PNG graph for each CSV file (with space as delimiter).

## Format of each line

`PLOT_NAME SECONDS_SINCE_EPOCH FLOAT_VALUE`

## Usage

`plotit [-d|--delimiter DELIMITER] [-k|--kind line|bar|area] FILENAME...`

Notes:
- The default delimiter is a single ASCII space.  Separators longer than 1 character and different from '\s+' will be interpreted as regular expressions as noted [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
- The type of graph may be specified with the `-k` (`--kind`) option.  The default is `line`.

## Example

`plotit example/*`

## Dependencies

The **python3-pandas** package will install these on Debian/Ubuntu & openSUSE:

- Matplotlib
- Pandas
