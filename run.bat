pytest -s -v -m "regression" testCases/ --browser chrome --html=./Reports/jenkinsRegressionExecution.html
pytest -s -v -m "sanity" testCases/ --browser chrome --html=./Reports/jenkinsSanityExecution.html
