# Publication Citation Prediction

WIP

## Setup

- Install `git` (see https://github.com/git-guides/install-git)
- Install `mamba` (see https://mamba.readthedocs.io/en/latest/installation.html)
- Clone this repo somewhere locally (`git clone git@github.com:eric-czech/publication-citation-prediction.git`)
- From the repository root, create the necessary Python environment by running `mamba env create -f environment.yaml`
- Create the folder `$REPO_ROOT/data/raw` 
- Download the raw data at [publications.parquet](https://drive.google.com/file/d/1h3QG90DEI7f_pHeH32yB1KJKh4-zbEf9/view?usp=sharing) to `$REPO_ROOT/data/raw/publications.parquet` 
- Open this repository in VSCode and install the [Python extension from Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- Open the `citepred/notebooks/eda.ipynb` notebook and run it using the `citepred` environment 
- Create a file in the repository called `.env` to contain private variables (see "Environment Variables" below)

### Environment Variables

The variables currently necessary in `.env` are:

```bash
OPENAI_API_KEY="xxxxx"
```

### Development

In order to alter and push code, run this first:

```bash
mamba activate citepred
pre-commit install
```

Now after making edits, push code as follows:

```bash
git commit -a -m "Message describing changes" 
```

This will automatically run the [pre-commit hooks](https://pre-commit.com/) that will ensure the new code meets some basic standards.  

If any of the checks fail, the command will say so and you can keep running the `git commit` command until it works without failures, making changes where necessary.
