.PHONY:deploy-example-heroku
deploy-example-heroku:
	# Deploy Heroku application
	echo "Test"
	# Add Procfile, runtime.txt
	# Init git
	# Clean up - delete files
	# Clean up - remove git repository

.PHONY:generate-example
generate-example:
	# Remove any existing files
	rm -r ./generated
	# Regenerate example
	cookiecutter "$${PWD}/template" -o ./generated --no-input
