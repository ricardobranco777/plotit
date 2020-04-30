# PlotIt

Cool plotting tool that generates a PNG graph for each CSV file (with space as delimiter).

## Format of each line

`PLOT_NAME SECONDS_SINCE_EPOCH FLOAT_VALUE`

## Usage

`plotit [-k|--kind line|bar|area] FILENAME...`

Note: The type of graph may be specified with the `-k` (`--kind`) option.  The default is `line`.

## Example

`plotit example/*`

## Dependencies

The *python3-pandas* package will install these on Debian/Ubuntu & openSUSE:

- Matplotlib
- Pandas
