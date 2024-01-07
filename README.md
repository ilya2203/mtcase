# mtcase
## Structure of repository:
```sh
├── .github
│   └── workflows
│       ├── cf_deploy.yml
│       ├── cf_destroy.yml
│       ├── sam_deploy.yml
│       └── sam_destroy.yml
├── README.md
├── iac
│   └── CF.yaml
└── sam_app
    ├── app
    │   ├── Dockerfile
    │   ├── app.py
    │   └── requirements.txt
    ├── samconfig.toml
    └── template.yaml
```

## How to use it:
### 1. Creating infrastructure.
In Github, go to the Actions tab, select AWS CF Deploy, tap *"Run Workflow"* in the top right corner, after filling in the *"Name of the stack to deploy"* field, it will be the name of the future AWS Cloudformation infrastructure stack.
### 2. Build and deploy application.
In Github, go to the Actions tab, select AWS SAM Deploy, tap *"Run Workflow"* in the top right corner, after filling in the *"Name of the application to deploy"* field, it will be the name of the future AWS Cloudformation application stack.
**NOTE:** The required field is *"Stack Name"* and should be filled with the same value as in point 1 *"Name of the stack to deploy"*. This action allows to use the output of the stack that was deployed in 1 step.
After the deployment is completed, drop down to run workflow and select job then reveal *"run: sam deploy"* step.
There are two links to AWS API Gateway, one for GET request and one for POST request.
### 3. Destroy application.
In Github, go to the Actions tab, select AWS CF Destroy, tap *"Run Workflow"* in the top right corner, after filling in the *"Name of the application to destroy"* field, it will remove the AWS Cloudformation application stack.
### 4. Destroy infrastructure.
In Github, go to the Actions tab, select AWS CF Destroy, tap *"Run Workflow"* in the top right corner, after filling in the *"Name of the stack to destroy"* field, it will remove the AWS Cloudformation infrastructure stack.