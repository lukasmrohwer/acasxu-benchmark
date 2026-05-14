# ACAS Xu Isomorphic Networks Benchmark

This repository contains the **ACAS Xu Isomorphic Networks Benchmark**, developed explicitly to serve as a benchmark for **VNN-COMP 2026**.

## Overview

This benchmark evaluates the ability of neural network verification tools to analyze properties across multi-network systems. Specifically, it focuses on **isomorphic networks**—networks with identical architectures but slightly different weights. The primary task is to check the bounded output distance ($\epsilon$-equivalence) between original ACAS Xu networks and their randomly perturbed variants.

The project includes scripts to automatically apply random normal noise to the weights of the networks and generate the corresponding `VNN-LIB` property specifications.

## Repository Structure

- `generate_properties.py`: The main script to generate `.vnnlib` property files, perturb models, and create the `instances.csv` manifest.
- `python_scripts/`: Contains utility scripts:
  - `perturb_network.py`: Applies normal noise to an ONNX model's initializers.
  - `create_specifications.py`: Generates the VNN-LIB templates.
- `onnx/original/`: Contains the original unperturbed ACAS Xu ONNX models.
- `onnx/perturbed/`: Destination folder for the generated perturbed ONNX models.
- `vnnlib/`: Destination folder for the generated property specifications.
- `instances.csv`: The benchmark manifest file formatted for VNN-COMP multi-network evaluation.

## Generating Instances

To generate the verification properties and perturbed networks, run the `generate_properties.py` script with an integer random seed:

```bash
python generate_properties.py <random_seed>
```

For example:
```bash
python generate_properties.py 42
```

This script will:
1. Randomly select an original ACAS Xu network.
2. Apply a small random perturbation ($P=0.001$) to the network weights.
3. Save the perturbed model to the `onnx/perturbed/` directory.
4. Generate a `.vnnlib` property file in the `vnnlib/` directory specifying the input bounds and output equivalence constraints.
5. Populate the `instances.csv` file mapping the network pairs to their properties and timeouts.

## Property Description

The generated VNN-LIB properties use the `(isomorphic-to ...)` declaration to indicate architectural equivalence. They enforce standard input bounds for the ACAS Xu domain and define constraints to test if the outputs of the perturbed network remain within an epsilon bound ($\epsilon = 0.05$) of the original network's outputs for identical inputs. 
