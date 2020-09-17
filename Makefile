# Regenerate example
generate-example:
	# Remove any existing files
	rm -r ./generated
	# Regenerate example
	cookiecutter "$${PWD}/template" -o ./generated --no-input

# Deploy Heroku application
deploy-example-heroku:
	# Add Procfile, runtime.txt
	cp ./heroku/Procfile ./generated/dash_starter_app/
	cp ./heroku/runtime.txt ./generated/dash_starter_app/
	# Init git in folder and push to Heroku - all in one command to maintain shell session
	cd generated/dash_starter_app && \
	git init && git add . && git commit -m "Deploy Dash Starter App" && \
	heroku git:remote -a dash-starter-app && git push heroku master -f
