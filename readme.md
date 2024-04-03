# Amazon EMR Ops Review


## How to collect EMR metadata collector?

### Step 0: Requirements

1.Install Python3

2.Install python library:

```shell
pip install emr-metadata-collector
```

Enure Python package directory is included in your PATH environment. Otherwise, you will have to use absolute path, for example "/home/hadoop/.local/bin/emr_metadata_collector"
```shell
emr-metadata-collector -h
```

### Step 1: List the all running EMR cluster, run the following command:

 ```shell
emr_metadata_collector list_clusters -r {region}
 ```
Note down the cluster id which need to collect data.

### Step 2: Collect Metadata by running the following command:

```shell
emr_metadata_collector collect_data -c {cluster_id} -r {region} -o {output_folder}
```


### Step 3: Send the collected metadata zip file to AWS
All the output files are in the directory specified by "--output"(for example, "collected_emr_data" directory).




### Build pip
```
python setup.py sdist bdist_wheel

### Set up

```
pip install emr_metadata_collector-1.0.0-py3-none-any.whl 

```
/home/hadoop/.local/bin/emr_metadata_collector collect_data -c j-QP5U4DP0ROLS -r us-west-2 -o emr_data

