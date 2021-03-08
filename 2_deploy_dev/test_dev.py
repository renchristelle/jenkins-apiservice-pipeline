import dataikuapi


def build_apinode_client(params):
    client_design = dataikuapi.DSSClient(params["host"], params["api"])
    api_deployer = client_design.get_apideployer()
    api_url = api_deployer.get_infra(params["api_dev_infra_id"]).get_settings().get_raw()['apiNodes'][0]['url']
    return dataikuapi.APINodeClient(api_url, params["api_service_id"])


def test_standard_call(params):
    client = build_apinode_client(params)
    print("Test is using API node URL {}".format(client.base_uri))
    record_to_predict = {
        "text_clean": "halftime lockerooms sacrosanct privilege allow entry they be like situation room white house tight security"
    }
    prediction = client.predict_record(params["api_endpoint_id"], record_to_predict)
    assert prediction['result']['prediction'] == 'Sci', "Prediction should be Sci but is {}".format(prediction['result']['prediction'])


def test_missing_param(params):
    client = build_apinode_client(params)
    print("Test is using API node URL {}".format(client.base_uri))
    record_to_predict = {
    }
    prediction = client.predict_record(params["api_endpoint_id"], record_to_predict)
    assert prediction['result']['ignored'] == False , "Request status status should be ignored = false is {}".format(prediction['result'])
    assert prediction['result']['ignoreReason'] == "IGNORED_BY_MODEL" , "Reason should be IGNORED_BY_MODELbut is {}".format(prediction['result'])
