import aws_cdk as core
import aws_cdk.assertions as assertions
from demo_aws_cdk_celery_sqs.demo_aws_cdk_celery_sqs_stack import DemoAwsCdkCelerySqsStack


def test_sqs_queue_created():
    app = core.App()
    stack = DemoAwsCdkCelerySqsStack(app, "demo-aws-cdk-celery-sqs")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    app = core.App()
    stack = DemoAwsCdkCelerySqsStack(app, "demo-aws-cdk-celery-sqs")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
