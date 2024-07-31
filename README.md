
- [apigw-websocket-api-fargate-cdk](https://github.com/aws-samples/serverless-patterns/)
- [aws-batch-celery-worker-example](https://github.com/aws-samples/aws-batch-celery-worker-example)
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
npx cdk synth
pytest
```

![PlantUML](//www.plantuml.com/plantuml/png/NOz1hi8W443td88Bz08_3Mb-Jw3Hk1xBI2eKxComyFOEAuiR0hp7l32n04dTae60MUoC2UazfxKTnj4_8OVYdDahLhItGl7KTefuPxrVolOg-Vko6KYA7q0115Nn8707Hdj6hadu7vQ8sQj3wDSsn7JLmHqwV_RAEky27DbqYI4TnH_cbVKvC-cY__m0)

```plantuml
@startuml
agent CeleryClient <<django>>
queue WorkQueue <<sqs>>
component CeleryWorker <<fargate>>
database ResultsBackend <<redis>>

CeleryClient -> WorkQueue : User Tasks
CeleryWorker -l-> WorkQueue
CeleryWorker -d-> ResultsBackend
@enduml
```
