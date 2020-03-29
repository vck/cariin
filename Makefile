env:
	source env/bin/activate

run:
	python scrapper.py
	sort db.txt | uniq -c >> uniq.txt
	
