# DevOps Capstone Project

[![CI Build](https://github.com/Pranavkhaire/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/Pranavkhaire/devops-capstone-project/actions/workflows/ci-build.yaml)

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9](https://img.shields.io/badge/Python-3.9-green.svg)](https://www.python.org/)

This repository contains the starter code for the project in [**IBM-CD0285EN-SkillsNetwork DevOps Capstone Project**](https://www.coursera.org/learn/devops-capstone-project?specialization=devops-and-software-engineering), which is part of the [**IBM DevOps and Software Engineering Professional Certificate**](https://www.coursera.org/professional-certificates/devops-and-software-engineering).

## Usage

This repository contains the code required to complete the DevOps Capstone Project. The project focuses on developing a REST API microservice and implementing DevOps practices, including automated testing, continuous integration, containerization, and deployment.

## Development Environment

These labs are designed to run in the IBM Developer Skills Network Cloud IDE with OpenShift. Please use the links provided in the Coursera Capstone Project to access the lab environment.

Initialize the development environment by sourcing the setup script:

```bash
source bin/setup.sh
```

**Note:** Do not run this program as a Bash script. It sets environment variables, so it must be sourced.

This installs Python 3.9, makes it the default Python version, modifies the Bash prompt, creates a Python virtual environment, and activates it.

After sourcing the script, your prompt should look similar to:

```text
(venv) theia:project$
```

## Useful Commands

These commands are normally performed automatically during setup but may be useful if something goes wrong.

### Activate the Python 3.9 Virtual Environment

```bash
source ~/venv/bin/activate
```

### Install Python Dependencies

Ensure that the Python 3.9 virtual environment is activated, then run:

```bash
make install
```

### Start the PostgreSQL Docker Container

The labs use PostgreSQL running in a Docker container. If the database service is unavailable, run:

```bash
make db
```

Verify that the container is running with:

```bash
docker ps
```

## Project Layout

The microservice code is contained in the `service` package, and the tests are located in the `tests` folder. The code follows the **Model-View-Controller (MVC)** pattern, with database code and business logic in `models.py` and REST API routing in `routes.py`.

```text
├── service/
│   ├── common/          # Common logging and error handlers
│   ├── config.py        # Flask configuration
│   ├── models.py        # Persistent data model
│   └── routes.py        # REST API routes
├── tests/
│   ├── factories.py
│   ├── test_cli_commands.py
│   ├── test_models.py
│   └── test_routes.py
├── .github/
│   └── workflows/
│       └── ci-build.yaml
├── setup.cfg
├── requirements.txt
└── Dockerfile
```

## Data Model

The Account model contains the following fields:

| Name | Type | Optional |
|---|---|---|
| `id` | Integer | False |
| `name` | String(64) | False |
| `email` | String(64) | False |
| `address` | String(256) | False |
| `phone_number` | String(32) | True |
| `date_joined` | Date | False |

## Your Task

Complete the microservice by implementing REST APIs for **READ**, **UPDATE**, **DELETE**, and **LIST**, while maintaining at least **95% code coverage**.

Following the principles of **Test-Driven Development (TDD)**, write tests for the expected functionality before implementing the code that makes those tests pass.

## Local Kubernetes Development

This repository can also be used for local Kubernetes development. Running these commands in the Cloud IDE environment is not recommended. They are intended to simulate the Cloud IDE environment locally.

At a minimum, you need [Docker Desktop](https://www.docker.com/products/docker-desktop). For the full development environment, you will also need [Visual Studio Code](https://code.visualstudio.com/) with the [Remote Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

These tools can be installed manually or through a package manager such as Homebrew on macOS or Chocolatey on Windows.

Use the following commands only in the local VS Code Remote Containers environment.

### 1. Bring Up a Local K3D Kubernetes Cluster

```bash
make cluster
```

### 2. Install Tekton

```bash
make tekton
```

### 3. Install the ClusterTasks

```bash
make clustertasks
```

You can then perform Tekton development locally, similar to the Cloud IDE lab environment.

## Author

[John Rofrano](https://www.coursera.org/instructor/johnrofrano), Senior Technical Staff Member, DevOps Champion at IBM Research, and instructor at Coursera.

## License

Licensed under the Apache License 2.0. See the [LICENSE file](https://github.com/Pranavkhaire/devops-capstone-project/blob/main/LICENSE).
