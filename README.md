# Publication Citation Prediction

WIP

## Development

- Clone this repo
- Download mamba from https://mamba.readthedocs.io/en/latest/installation.html.
- From the repository root, create the environment by running `mamba env create -f environment.yaml`
- Create the folder `$REPO_ROOT/data/raw` 
- Download the raw data at `publications.parquet` to `$REPO_ROOT/data/raw/publications.parquet` 
- Open this repository in VSCode and install the [Python extension from Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- Open the `citepred/notebooks/eda.ipynb` notebook and run it using the `citepred` environment 
- Create a file in the repository called `.env` to contain private variables (see "Environment Variables" below)

### Environment Variables

The variables currently necessary in `.env` are:

```bash
OPENAI_API_KEY="xxxxx"
```
