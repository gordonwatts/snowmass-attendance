# Snowmass 2022 Attendance Survey Results

This website can be found here: [https://gordonwatts.github.io/snowmass-attendance](https://gordonwatts.github.io/snowmass-attendance).

## Working with the data

The data is availible to all members of the Seattle Snowmass LOC. Please request it.

1. By far the easiest thing to do is run this repo in `vscode`. It will ask you to start a `devcontainer`. It will take a short while while the docker container is downloaded and prepared for you. However, you'll end up with an environment that is setup to run these notebooks inside `vscode`, with all the necessary compoents (automatically).
1. Put the survey data as `survey.csv` in the root directory of the repo (MAKE SURE NOT TO CHECK IT INTO GITHUB).
1. Run the `cleaning.ipynb` notebook to clean the original data and produce a clean `csv` file.
1. Have fun with any of the other notebooks!

If you add new cells, please do not forget to add `"tags": ["hide-input"]` to the cell metadata to hide the input python (unless you want people to see it first-thing). Even after hiding, anyone can reveal the code, so keep that in mind when you are writing the code.

## Updating The Book

Once you've prepared new plots, etc., you can update the information online using the following commands.

```bash
jupyter-book build ./attendance
ghp-import -n -p -f ./attendance/_build/html
```
