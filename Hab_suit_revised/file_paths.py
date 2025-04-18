### Make reproducible file paths
data_dir = os.path.join(
    ### home directory
    pathlib.Path.home(),
    
    ### eda directory
    'earth-analytics',
    'data',

    ### Project dir
    'hab_suit'
)

### make the dir
os.makedirs(data_dir, exist_ok=True)