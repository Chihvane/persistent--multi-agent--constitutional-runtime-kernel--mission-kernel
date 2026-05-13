.PHONY: check public-check status serve build

check:
	./.internal/engineering/scripts/check_public_repo.sh

public-check: check

status:
	git status --short --branch

serve:
	cd .internal/engineering/site && bundle exec jekyll serve

build:
	cd .internal/engineering/site && bundle exec jekyll build
