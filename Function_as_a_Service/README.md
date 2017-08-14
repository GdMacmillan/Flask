# Example: Function as a Service (FaaS)

This example deploys a function as a microservice accessible via an API POST request. The simple function shifts every number in an array up by 1 if method = 'add' and down by 1 if method = 'subtract'.

The implementation deploys the model using Flask.

This framework can be modified for other functions or to implement trained data science models.

### Using the function via curl:

Start the flask app (runs locally by default).

    curl -H "Content-Type: application/json" -X POST -d '{"data":[1, 5, 6], "method":"add"}' localhost:8080/shift_compute

returned results:

    {
        "result": [
            2,
            6,
            7
        ]
    }
