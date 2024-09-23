# python-test-mssql

## Overview

A utility to test connections to mssql databases. 

## Configuration

It is recommended to use a virtual environment with this. It was written in Python 3.11.5, however there should be nothing in here precluding using an early version of Python 3. 

Install the requirements:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Move the config.yaml.template file to config.yaml and edit the fields with the necessary details. The port is specified at 1433 by default, however this may need to be updated with your configuration. 

## Running the Tool

With all the pre-reqs in place, should be as easy as running the test client with no arguments. If successful, the output should be similar:

```bash
python test_client.py

SERVER VERSION:

Microsoft SQL Server 2019 (RTM-CU28) (KB5039747) - 15.0.4385.2 (X64)
	Jul 25 2024 21:32:40
	Copyright (C) 2019 Microsoft Corporation
	Enterprise Edition (64-bit) on Windows Server 2019 Standard 10.0 <X64> (Build 17763: ) (Hypervisor)
```

You can modify the query in the script itself if you want to test a more complex query. 
