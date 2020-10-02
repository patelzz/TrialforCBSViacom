
# Recreating Serverless Workloads with AWS Python CDK 

## Table of Contents
* [Project Description](#project-description)
* [Pre-Requisites](#pre-requisites)
* [Project Components](#project-components)
* [Helpful Commands](#helpful-commands)
* [Adding Additional Dependencies](#adding-additional-dependencies)
* [Keeping your Project Up to Date](#keeping-your-project-up-to-date)
* [Current Status](#current-status)
* [Author](#author)


# Project Description 

This project demonstrates a CDK app with an instance of a stack (`cbsapp_stack`)
which contains various AWS Services that can be useful for CBSViacom. 

## Pre-Requisites

* Be sure to have Python version 3 downloaded and installed locally. 
* Be sure to have aws configured in the CLI. 

# Project Components
The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization process also creates
a virtualenv within this project, stored under the .env directory.  To create the virtualenv
it assumes that there is a `python3` executable in your path with access to the `venv` package.
If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv
manually once the init process completes.

# Helpful Commands 
To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .env/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .env\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

You can now begin exploring the source code, contained in the hello directory.
There is also a very trivial test included that can be run like this:

```
$ pytest
```

# Adding Additional Dependencies 
To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

## Keeping your Project Up to Date

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation


## Current Status
All components of this Project are: _finished_ as of 10/01/2020.

## Author

>Shivani Patel
>AWS Professional Services Consultant
>patelzz@amazon.com


