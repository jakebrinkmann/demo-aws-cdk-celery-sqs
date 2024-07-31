#!/usr/bin/env python3

import aws_cdk as cdk

from demo_aws_cdk_celery_sqs.demo_aws_cdk_celery_sqs_stack import DemoAwsCdkCelerySqsStack


app = cdk.App()
DemoAwsCdkCelerySqsStack(app, "DemoAwsCdkCelerySqsStack")

app.synth()
