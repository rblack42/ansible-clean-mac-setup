.PHONY: docs
docs:
	cd sphinx && \
		sphinx-build -b html . ../docs

.PHONY: setup
setup:
	cd ansible && \
		ansible-playbook main.yml
