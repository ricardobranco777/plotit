test:
	@pylint plotit --disable=consider-using-f-string
	@flake8 plotit --ignore=E501
