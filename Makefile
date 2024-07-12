.PHONY: build

# Initialise the build 
build:
	sam.cmd build

# Deploy any infra updates to the site
deploy-infra:
	sam.cmd build && aws-vault exec insertuser --no-session -- sam.cmd deploy

# Deploy any updates to the Site
deploy-site:
	aws-vault exec insertuser --no-session -- aws s3 sync ./resume-site s3://recreated-website2351

invoke-put:
	sam.cmd build && aws-vault exec anthonydev --no-session -- sam local invoke PutFunction

invoke-get:
	sam.cmd build && aws-vault exec anthonydev --no-session -- sam local invoke GetFunction
