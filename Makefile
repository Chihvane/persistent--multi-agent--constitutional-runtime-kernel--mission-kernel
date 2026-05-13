.PHONY: check status

check:
	./scripts/check_public_repo.sh

status:
	git status --short --branch

