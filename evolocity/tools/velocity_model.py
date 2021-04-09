from .featurize_seqs import get_model

def velocity_model(
    adata,
    model_name='esm1b',
    mkey='model',
    copy=False,
):
    adata = adata.copy() if copy else adata

    model = get_model(model_name)

    data.uns[mkey] = model

    return adata if copy else None
